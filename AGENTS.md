# Agent Instructions

This file contains guidance for agents that generate code for the Cinema 4D Python SDK.

ALWAYS follow the [Guidelines](#Guidelines) when generating code for the Cinema 4D Python SDK. 

## Entry Points

- [Vocabulary](.agents/_vocabulary.ttl): Contains the vocabulary that is used to organize this SDK. When you do not find a direct skill instruction below, you can use this vocabulary to find code examples for your task.
- [Assets](.agents/assets.md): Learn how to create, read, or modify assets in Cinema 4D, such as textures, materials, and models.
- [Debugging](.agents/debug.md): Learn how to inspect scene data, check assumptions, trace and time code, test Script Manager scripts through the VS Code Cinema 4D Connector, and track down crashes caused by threading violations.
- [Nodes](.agents/nodes.md): Learn how to create, read, or modify nodes in a node graph. For node materials, ask whether to use Graph Description API or Nodes API; for Scene Nodes, always use Nodes API.
- [Node Spaces](.agents/nodespaces/_overview.md): Contains dumped node space metadata. You will need this information when building material or scene nodes graphs.
- [Scaffolds](.agents/scaffolds.md): Learn how to scaffold plugins (dialog, command, object, tag, preference, message, shader, tool, scene and image loader and saver plugins, and render tokens) in the `projects/` folder. Use it first for any request to create, build, or implement a plugin or tool, including informal requests such as "create a plugin" or "create a tool." It describes which questions you must ask the user in a chat selection menu before generating any files.
- [Scene](.agents/scene.md): Learn how to create, read, or modify scenes, and which operations are allowed on which thread.

## Script Manager Testing

- For scripts intended for Cinema 4D's Script Manager, use the VS Code Cinema 4D Connector to execute in the user's already-running Cinema 4D instance. Do not use `c4dpy` as the default: it starts a separate process, is often slower, does not test the active document, and its output is not in the connected app's `Cinema 4D` Output channel. A `c4dpy` run or `py_compile` pass alone is not live Script Manager validation.
- Check that the `maxonc4dsdk.cinema4d-connector` extension is installed and enabled. In VS Code, `C4D ✓` with a `Connected to: ...` tooltip means connected; `C4D X` means disconnected. Use `C4D: Toggle Connection with Cinema 4D` to connect, then verify the status again.
- Save the intended script and make it the active editor. Run `C4D: Execute in Cinema 4D as a Script in Script Manager` (command ID `cinema4d-connector.execute_in_c4d`). Read Python output and exceptions in the VS Code Output panel, selecting the `Cinema 4D` channel. A successful dispatch alone is not a pass: inspect the output and confirm the expected result in Cinema 4D.
- If the agent's VS Code command tool cannot invoke that command, do not conclude the Connector is unavailable or tell the user to run it. Check the configured WebSocket endpoint (`c4d.IP` and `c4d.port`, defaults `127.0.0.1:7788`) using subprotocol `c4d_py_code_exchange`. A response to `{"action":"idea2c4d.get_pid"}` confirms the live app connection. Then send `{"action":"idea2c4d.execute","script_path":"empty","value":"<script source>","debug":false}` and read `c4d2ide.console` messages. Report clearly that this was direct Connector protocol execution, not invocation of the VS Code command. If neither path works, report runtime validation as pending and ask for user assistance only when needed to restore the connection.
- Use `c4dpy` only when the user specifically asks for headless testing or the code is suited to isolated execution.

## Current Python Documentation

- Start at <https://developers.maxon.net/docs/py>, which always points to the newest Python SDK documentation.
- Search that site for the exact manual title, API symbol, or topic named by the relevant agent file. Verify the result against the current Cinema 4D version before applying it.
- Do not construct or keep version-pinned documentation URLs. When referring an agent to documentation, provide the current documentation root and the search terms to use.

## Workspace Boundaries

- `examples/` is read-only reference material. Read, search, and run examples to understand SDK patterns, but never create, edit, delete, rename, reformat, or otherwise modify files under `examples/`.
- `projects/` is the writable destination for new SDK code. When a request asks to create or implement code and does not identify an existing target file or project, create a new file or project under `projects/`. Do not use an example file as the target, even when the requested feature resembles one.
- When a request identifies an existing file under `projects/`, work in that project. Never overwrite existing files or expand into unrelated files without a clear need.
- Treat projects as user-owned work. Do not add `__copyright__` or `__license__` fields, copyright/license notices, or statements claiming or implying that Maxon owns the project's intellectual property. Do not copy those headers from examples into projects.
- Whenever you can predict even one plausible answer to a question, present a multiple-choice or multi-select input with that answer as a recommended option and an explicit `Other (enter a custom answer)` option when custom answers are valid. Do this for names, descriptions, and behavior as well as finite technical choices. Use a text-only input only when no plausible answer can be predicted or the value must be supplied exactly (for example, a registered plugin ID). Do not offer `Other` for strict API enums that cannot accept custom values; explain that the choices are constrained.
- Requests for information or examples do not authorize code changes. Examples can be used to explain or inform an implementation in `projects/`.
- Use absolute filesystem paths unless the user explicitly requests relative paths. Do not assume a relative path resolves from the script's directory or the workspace; if an input path is unknown, ask the user or use a file picker and use its absolute result.

## Guidelines

### Basic

- IMPORTANT: Never delete or overwrite existing files without user confirmation.
- IMPORTANT: Follow PEP8 coding style and naming conventions in all Python code. The maximum line length is 100 characters. 
- IMPORTANT: Use 4 spaces for indentation, do not use tabs.
- IMPORTANT: In the Cinema API camel case is used for class names, functions, methods, attributes, and variables. Use camel case for all identifiers in your code. Do not use snake case. Classes, functions, and methods start with a capital letter, attributes and variables start with a lowercase letter. Global constants are all uppercase with underscores.
- IMPORTANT: Never use `multiprocessing`, the Cinema 4D Python VM does not support interpreter parallelism and will crash if you try to use it. `subprocess.run([sys.executable, “my_script.py”], …)` is therefore also off limits. Do not use `threading`. Use `c4d.threading` instead.
- IMPORTANT: Avoid abstraction/helper functions when writing Nodes, Graph Description, or Asset API code. Use literals such `file://C:/Users/username/Documents/scene.c4d` instead of `os.path.join(os.path.expanduser("~"), "Documents", "scene.c4d")`. Especially graph descriptions should be as literal as possible to avoid unnecessary complexity. Only start abstracting when the user is explicitly asking for a more compressed solution.
- Use type hinting for all function parameters, return types, class attributes, and variables where possible.
- Avoid using Python std lib modules other than `os`, `sys`, `math`, `typing`, `re`, `itertools`, `functools`, `collections`, and `json`, and `logging`.
- Avoid using `typing` in favour of modern built-in types (e.g., use `list` instead of `List`, `dict` instead of `Dict`, etc.).
- Use Google style doc strings for all functions, classes, and modules. Doc strings end in line break. Avoid documenting 
  arguments and return types in favour of verbose short descriptions and detailed descriptions. But generally documentation 
  should be sparse. E.g.:
```python
def collapse(obj: c4d.BaseObject, moveTags: bool = False) -> c4d.BaseObject:
    """Collapse the given #obj into a single object and returns the result.

    When #moveTags is True, all tags in the input hierarchy of #obj will be moved to the resulting object.
    """
    ...
```

#### Cinema

- *.pyp is the Cinema 4D Python SDK plugin extension, it is equivalent to a normal *.py file.
- Script Manager scripts have the active document auto exposed as `doc` and the active object auto exposed as `op`. Do not use `c4d.documents.GetActiveDocument()` or `doc.GetActiveObject()`, instead use the `doc` and `op` hints. The active document is always a `c4d.documents.BaseDocument`, the active object is always a `c4d.BaseObject` or None.
- For other script forms such as plugin or scripting elements, this is not the case.

### Structure of an Example

An example should always have at least a `main()` function that is invoked in the `__main_` block. Functions should not be much longer than 100 lines. When an example breaks into multiple sub-examples, each sub-example should be its own function. Avoid overly short examples that split into dozens of files (e.g., `container_get_string.py`, `container_get_int.py`, `container_get_float.py`, etc.). Instead, combine them into a single example with multiple functions (e.g., `container_get.py`). Only add the `doc` and `op` hints when you use them. Never manually get the active document or active object in an example. Use the `doc` and `op` hints instead. 
Structure of an example:

An example should also have a doc string at the top of the file that describes what the example does. The doc string should be sparse. It should have a short description of the example, optionally a longer description when more complex topics or ideas must be explained, always usage instructions (are there run-time requirements, how to run the example, etc.), and a list of topics that the example covers. The topics should be a bulleted list of short phrases that describe the concepts covered in the example. The topics should be used to generate the table of contents for the SDK documentation.

Finally, an example should have a header with the author, copyright, license, and version information. The author should be `{ModelName}`, the copyright should be `Copyright (C) {Year} MAXON Computer GmbH`, the license should be `Apache-2.0 License`, and the version should be `{Version}`. {ModelName} is the name of the model that generated the example, {Year} is the current year, and {Version} is the version of the Cinema 4D Python SDK that generated the example.

```python
"""Demonstrates how to get and set values in a BaseContainer.

You can run this example by executing it in the Script Manager of Cinema 4D. It will create multiple 
BaseContainer objects, set values in them, and print the values to the console.

Topics:
    - Creating a BaseContainer
    - Reading values from a BaseContainer
"""
__author__ = "{ModelName}"
__copyright__ = "Copyright (C) {Year} MAXON Computer GmbH"
__license__ = "Apache-2.0 License"
__version__ = "{Version}"

doc: c4d.documents.BaseDocument # The active document
op: c4d.BaseObject | None # The active object, can be None.

def create_container() -> c4d.BaseContainer:
    """Creates a BaseContainer and sets some values in it.
    """
    # And example function should have at least ten lines of code, but not more than 100 lines of code. Split up longer
    # functions into logical blocks.
    ...

def read_container(container: c4d.BaseContainer) -> None:
    """Reads values from the given BaseContainer and prints them to the console.
    """
    ...

def main() -> None:
    """Runs the example.
    """
    # Create a BaseContainer and then read values from it.
    container: c4d.BaseContainer = create_container()
    read_container(container)

if __name__ == "__main__":
    main()
```

#### Comments

Use a clustered and sparse comment style in all code. Comments should be analytical and not just 
repeat function or class names that are invoked.

NO:

```python
# Create a cube.
cube: c4d.BaseObject = mxutils.CheckType(c4d.BaseObject(c4d.Ocube))

# Create a phong tag on the cube.
phongTag: c4d.BaseTag = mxutils.CheckType(cube.MakeTag(c4d.Tphong))

# Create a null object.
null: c4d.BaseObject = mxutils.CheckType(c4d.BaseObject(c4d.Onull))

# Insert the cube under the null object.
sphere.InsertUnder(null)

# Insert the null object into the scene.
doc.InsertObject(null)
```

YES:

```python
# Create a cube object with a phong tag and insert it under a null object, which is then inserted 
# into the scene.
cube: c4d.BaseObject = mxutils.CheckType(c4d.BaseObject(c4d.Ocube))
phongTag: c4d.BaseTag = mxutils.CheckType(cube.MakeTag(c4d.Tphong))
null: c4d.BaseObject = mxutils.CheckType(c4d.BaseObject(c4d.Onull))
cube.InsertUnder(null)
```