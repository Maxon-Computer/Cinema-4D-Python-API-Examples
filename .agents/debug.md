# Debugging Documentation

Python code in Cinema 4D mostly runs inside the application, often in callbacks that Cinema 4D calls on its own schedule and on a thread of its choosing. This document describes how to find errors in such code, and how to write code that is easy to debug. For current API details, start at <https://developers.maxon.net/docs/py> and search for `Debugging manual`.

# TOC

- [Rules](#rules): Hard rules for agents that debug or write debuggable code.
- [Toolbox](#toolbox): Which tool answers which question.
- [Workflows](#workflows): Step by step procedures for common debugging tasks.
- [Test a Script Manager script](#test-a-script-manager-script): Check the VS Code connector and run a safe script in Cinema 4D.
- [Threading Violations](#threading-violations): How to find and fix crashes caused by threading violations.
- [Examples](#examples): Runnable examples for all tools.

# Rules

- IMPORTANT: The VS Code debugger is currently broken for Cinema 4D. Do not suggest breakpoints, `debugpy`, the Cinema 4D Connector debug mode, or debugging `c4dpy` with `F5`. Use the techniques of this document, none of which depend on an IDE.
- IMPORTANT: Debugging code must be removed or disabled when you are done. Put it behind an `IS_DEBUG: bool` constant, or delete it. Never leave `DebugPrint`, `REPORT` or `TIMEIT` calls active in code that runs often (callbacks, generators, tags, `Draw` methods), they are expensive and spam the console.
- Start a script with `c4d.ClearPythonConsole()` when it prints a lot, so that the output of the last run is easy to find.
- Prefer `mxutils.DebugPrint` over hand written `print` loops for containers, parameters, flags and scene graphs. It resolves symbols and data types for you, and its output is stable enough to diff.
- Use `mxutils.CheckType` and `mxutils.CheckIterable` to fail early at allocations and function boundaries instead of ten lines later. Do not wrap them around values in loops.
- Do not guess the cause of a crash without a traceback. Establish facts first: on which thread does the code run, which callback was involved, what is the minimal scene that triggers it.
- A crash that "only happens sometimes" is almost always a [threading violation](#threading-violations). A fix is only confirmed when the reproduction procedure no longer crashes, not when the code ran once without a crash.
- Very large outputs (e.g., `GetGraph` of a whole document) can exceed what the console prints in one go. Print slices, or write the output to a file.
- The Python standard library rules of `AGENTS.md` have one exception for debugging: `faulthandler` may be used to capture crash logs.

# Toolbox

| Question | Tool |
| --- | --- |
| What is in this container, node, or scene? | `mxutils.DebugPrint.Get*` and `Print*` functions |
| What is different between these two nodes? | `mxutils.DebugPrint.Diff*` functions |
| Is this value what I think it is? | `mxutils.CheckType`, `mxutils.CheckIterable` |
| Was my function called, how often, how long did it take? | `mxutils.REPORT`, `mxutils.TIMEIT` |
| I need a scene to test my code with. | `mxutils.SceneFaker` (`mxutils.g_scene_faker`) |
| Cinema 4D crashes or hangs, but not always. | [Threading violations](#threading-violations), `faulthandler` |
| What is the symbol name of this integer ID? | `mxutils.g_c4d_symbol_translation_cache.Get(value, "^M[a-z]")` |

## DebugPrint

`mxutils.DebugPrint` converts Cinema API data into trees of `mxutils.DebugNode`. Each kind of data has up to three functions: `Get` returns the tree, `Print` prints it, and `Diff` returns the differences of two inputs as a unified diff.

| Data | Get | Print | Diff |
| --- | --- | --- | --- |
| `c4d.BaseContainer` | `GetContainer` | `PrintContainer` | `DiffContainer` |
| Parameters of a `c4d.BaseList2D` | `GetParameters` | `PrintParameters` | `DiffParameters` |
| `BIT_` and `NBIT_` flags of a node | `GetFlags` | `PrintFlags` | `DiffFlags` |
| Parameters and flags combined | `GetBaseList` | | `DiffBaseList` |
| Scene graph below a node | `GetGraph` | `PrintGraph` | `DiffGraph` |

- `PrintParameters` reads the description of the node and therefore always shows the correct symbols, names and types. Narrow the output down with `whiteList` and `blackList` (parameter or group IDs), `showDescId`, `showType`, and `showDefaultValues`.
- `PrintContainer` can only resolve IDs to symbols with a regular expression hint, e.g., `'^BFM_'`. Resolved symbols are numerically correct but can imply a different meaning than the entry has, only use hints when you know which family of symbols to expect.
- `PrintFlags` filters with `hint` (a regular expression) and `showSetOnly`. Use it to find out which flags changed after a user action.
- `PrintGraph` shows the hierarchy, caches and branches below a node. It is the quickest way to see what a generator has built. See `.agents/scene.md` for what the output means.
- `Diff*` functions return only the differences. The first line of a diff always differs, as it contains the name of the node.
- None of the functions modifies the scene, but they walk descriptions, containers and graphs, which is expensive.

```python
# Only show the parameters in the Object Properties group of a cube.
mxutils.DebugPrint.PrintParameters(cube, whiteList=(c4d.ID_OBJECTPROPERTIES,), showDescId=False)

# Find out what is different between two objects which should behave the same.
print(mxutils.DebugPrint.DiffParameters(a, b, whiteList=(c4d.ID_OBJECTPROPERTIES,)))
print(mxutils.DebugPrint.DiffFlags(a, b, showBit=False, hint="OM|OHIDE"))
```

Custom reports can be built with `mxutils.DebugNode` (`Add()`, `ToString()`, `FromString()`), and `mxutils.DebugPrint.GetTreeString()` prints any node type that exposes children through an attribute or `GetDown`/`GetNext`.

## CheckType and CheckIterable

Both return the value when the check passes, so they can be used inline. A failed allocation returns `None` in the Cinema API, the script then fails later with a message that points to the wrong place.

```python
# Fails here and not in the next line, when the allocation fails.
cube: c4d.BaseObject = mxutils.CheckType(c4d.BaseObject(c4d.Ocube))

data: list[str | int] = ["1", 2]
mxutils.CheckIterable(data, str)
# TypeError: Expected iterable 'data' to be composed of type <class 'str'>. Found item of type: <class 'int'>
```

The name of the checked expression can only be discovered in saved files. In the Script Manager and the console the error message is generic.

## REPORT and TIMEIT

- `@mxutils.REPORT()` prints the name of a function when it is called and an empty line when it returns. Use it to follow call chains without breakpoints.
- `@mxutils.TIMEIT(IS_DEBUG, showArgs=True, showResult=True)` times a call. The first argument is a flag, when it is `False` the function is returned unchanged, so the decorator can stay in the code. `TIMEIT` can profile with `cProfile` instead of timing. For recursive functions pass `inCallProtection=True` (not thread-safe).
- Profiling has a high impact on the runtime, timing a low one. Neither should ship in released code.

```python
IS_DEBUG: bool = True

@mxutils.TIMEIT(IS_DEBUG, showArgs=True, showResult=True)
def Factorial(n: int) -> int:
    return 1 if n == 0 else n * Factorial(n - 1)
```

## SceneFaker

`mxutils.g_scene_faker` creates objects, materials, tags, layers, render data and animation tracks for tests. `AddHierarchyFromString` builds an object hierarchy from an indented string, where `::` followed by an object type ID selects the type, and objects without one are Null objects. The `AddRandom...` methods and `RandomizeScene` add random content. Pass a seeded `mxutils.Random` to a new `mxutils.SceneFaker` to get identical content on every run. The faker builds caches, so it must run on the main thread, e.g., in a Script Manager script.

```python
objects: list[c4d.BaseObject] = mxutils.g_scene_faker.AddHierarchyFromString(doc, f"""
    A
        B::{c4d.Ocube}
        C::{c4d.Osphere}
        D
            E
    """)

mxutils.DebugPrint.PrintGraph(objects[0]) # Check that the scene is what the test needs.
```

# Workflows

## Test a Script Manager script

Follow the connection, execution, and output-reading procedure in [AGENTS.md](../AGENTS.md#script-manager-testing). Only execute scripts whose effects are safe to test; prefer a disposable document or reversible operation, and ask before destructive or otherwise risky actions. Do not claim runtime validation passed unless output was inspected and the expected result confirmed. Never use the connector's Debug command or `debugpy`; the VS Code debugger is currently broken for Cinema 4D.

## A value or node does not look right

1. Print it with the matching `DebugPrint` function and a narrow `whiteList`/`hint`.
2. When a working reference exists, `Diff*` the broken node against it instead of comparing by eye.
3. Add `mxutils.CheckType` where a `None` could enter the code, and re-run.

## A plugin callback does not do what it should

1. Decorate the callback with `@mxutils.REPORT()` (or guard a `print` with `IS_DEBUG`) to verify that it is called at all, and how often.
2. Print the input of the callback, e.g., `mxutils.DebugPrint.PrintParameters(op, whiteList=(...))`.
3. For generators print the output with `mxutils.DebugPrint.PrintGraph(op)`, a generator has no cache before the document has been executed once.
4. Remove the debugging code again.

## Code is slow

1. Wrap the suspicious function with `@mxutils.TIMEIT(IS_DEBUG, showArgs=True)`.
2. When the timing does not explain it, switch to the profiling mode of `TIMEIT`.
3. Do not time and profile at the same time, and remove both when done.

## I need a reproducible scene

Build it with `mxutils.g_scene_faker` and a seeded `mxutils.Random`, and verify it with `PrintGraph`. Reproducible scenes are the basis for the crash procedure below.

# Threading Violations

Ignoring the threading restrictions (see `.agents/scene.md`) is the most common reason for crashes of Python plugins and scripting elements. The result is undefined behavior: Cinema 4D does not raise an error at the faulty line, it is left with a dangling pointer that is dereferenced later, elsewhere, or on another thread.

Typical signs:

- Cinema 4D terminates without a Python traceback, or stops responding.
- The crash only happens sometimes, or in specific situations: playback, rendering, an open Object Manager showing the affected nodes, after the scene has been edited for a while.
- The code works in the Script Manager (always the main thread) but not as a plugin or scripting element.
- The crash location, if there is one, does not match the code that caused it.

## 1. Find out where the code runs

`c4d.threading.GeIsMainThreadAndNoDrawThread()` is `True` on the main thread when it is not executing drawing code. `c4d.threading.GeIsMainThread()` is also `True` during drawing.

```python
import functools

import c4d

def GetContext() -> str:
    """Returns a description of the thread context the caller is running in.
    """
    if c4d.threading.GeIsMainThreadAndNoDrawThread():
        return "main thread"
    if c4d.threading.GeIsMainThread():
        return "main thread (drawing)"
    return "threaded context"

def LogContext(func):
    """Prints the context a function is called in.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"{func.__qualname__}: {GetContext()}")
        return func(*args, **kwargs)
    return wrapper
```

Decorate the callbacks and all helpers they call. The violation is often in a helper that was written for a script and later reused in a callback. Remove the logging afterwards.

## 2. Turn violations into errors

Replace the silent undefined behavior with an exception while debugging. Place the guard in front of each operation that the restrictions table in `.agents/scene.md` marks as forbidden in a threaded context.

```python
IS_DEBUG: bool = True

def AssertMainThread() -> None:
    """Raises an error when called from a threaded context, instead of risking a crash.
    """
    if IS_DEBUG and not c4d.threading.GeIsMainThreadAndNoDrawThread():
        raise RuntimeError("Main thread only code has been called from a threaded context.")
```

A guard is not the fix. It only shows where the code is wrong.

## 3. Capture the crash

`faulthandler` writes the Python stack of the crashing thread to a file, also without a traceback. The first entry is the Python line that called into the Cinema API which crashed. The cause can lie earlier, the log tells which callback and thread were involved. Keep the file object alive as long as the handler is enabled.

```python
import faulthandler
import os

# The file object must stay open as long as faulthandler is enabled.
g_crashLog = open(os.path.join(os.path.dirname(__file__), "crash.log"), "w")
faulthandler.enable(file=g_crashLog, all_threads=True)
```

For hangs (e.g., a lock held while calling into the Cinema API) dump all stacks after a timeout:

```python
faulthandler.dump_traceback_later(10, repeat=False, file=g_crashLog)
# ... run the code that hangs ...
faulthandler.cancel_dump_traceback_later()
```

This has been verified for `c4dpy`. In the Cinema 4D application its own crash handling is involved, so test the setup once with a deliberate crash in a scratch session before relying on it.

## 4. Reduce and reproduce

Make Cinema 4D busy while the code under test runs: play the timeline, start a render in the Picture Viewer, open the Object Manager and Attribute Manager with the affected nodes, drag sliders. Combine this with a small `SceneFaker` scene and remove parts of the callback until the crash disappears. The last removed part contains the violation. After the fix run the same procedure again.

## 5. Fix the violation

A callback cannot modify the document on its own. Move the work to the main thread: with `c4d.SpecialEventAdd` and a `c4d.plugins.MessageData` plugin, or in the `Message` method of a node (e.g., tied to a button click). Never use Python's `threading` or `multiprocessing` to access Cinema 4D data. See `.agents/scene.md` for the pattern.

# Examples

- [DebugPrint](../examples/misc/mxutils_debugprint.py): Demonstrates all `DebugPrint` Get, Print and Diff functions.
- [Decorators](../examples/misc/mxutils_decorators.py): Demonstrates `TIMEIT`, `REPORT` and `SET_STATUS`.
- [CheckType](../examples/misc/mxutils_checktype.py): Demonstrates `CheckType` and `CheckIterable`.
- [Symbol Translation Cache](../examples/misc/mxutils_symboltranslationcache.py): Demonstrates how to translate integer IDs to symbol names.
- [Traversal](../examples/scene/traversal.py): A scene built with the `SceneFaker`.
