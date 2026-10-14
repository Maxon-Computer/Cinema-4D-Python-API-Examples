"""Demonstrates mxutils helpers for diagnosing Cinema 4D scene data.

Run this example in the Cinema 4D Script Manager. It prints a container, parameter,
and scene graph tree for the active document and its selected object.

Topics:
    * mxutils.DebugPrint.GetBaseList
    * mxutils.DebugPrint.GetContainer
    * mxutils.DebugPrint.GetFlags
    * mxutils.DebugPrint.GetGraph
    * mxutils.DebugPrint.GetParameters
    * mxutils.DebugPrint.DiffParameters
    * mxutils.DebugPrint.DiffFlags
    * mxutils.DebugPrint.DiffBaseList
    * mxutils.DebugPrint.DiffGraph
    * mxutils.DebugPrint.PrintContainer
"""
__author__ = "Ferdinand Hoppe"
__copyright__ = "Copyright (C) 2026 MAXON Computer GmbH"
__license__ = "Apache-2.0 License"
__version__ = "2027.0"

import c4d
import mxutils

doc: c4d.documents.BaseDocument # The active Cinema 4D document.

def main() -> None:
    """Runs the example for the active document.
    """
    # Create an example scene, get the first and second object, and their data containers.
    mxutils.g_scene_faker.RandomizeScene(doc, randomizeParameters=False)
    c4d.EventAdd()

    first: c4d.BaseObject = mxutils.CheckType(doc.GetFirstObject())
    second: c4d.BaseObject = mxutils.CheckType(first.GetDown() or first.GetNext())
    bc1: c4d.BaseContainer = first.GetDataInstance()
    bc2: c4d.BaseContainer = second.GetDataInstance()

    print("\n--- DebugPrint.GetContainer -------------------------------------------------------\n")

    # The class DebugPrint provides various static methods to inspect and debug different aspects of 
    # Cinema 4D scene data. At its core, the class returns a DebugNode object that represents the 
    # debug information in a structured tree format.

    # Get the debug nodes for the first and second objects and their data containers.
    debug1: mxutils.DebugNode = mxutils.DebugPrint.GetContainer(bc1)
    debug2: mxutils.DebugNode = mxutils.DebugPrint.GetContainer(bc2)

    # We can print the nodes like this, which will give us a tree view of the container.
    print(f"GetContainer(bc1) = \n{debug1.ToString()}")
    print(f"GetContainer(bc2) = \n{debug2.ToString()}")

    # A shorter path can be to directly use the PrintContainer function when we do not need the nodes.
    mxutils.DebugPrint.PrintContainer(bc1)
    mxutils.DebugPrint.PrintContainer(bc2)

    # Debugging containers can also be complemented with a symbol hint which can be useful for better
    # readability when we can predict the symbolic names of the IDs. Here we poll for the current 
    # mouse input state and the print the result, predicting that most will have a symbolic name 
    # starting with 'BFM_'. When there is no symbolic name, or the match is ambiguous, the raw ID 
    # will be shown.
    state: c4d.BaseContainer = c4d.BaseContainer()
    c4d.gui.GetInputState(c4d.BFM_INPUT_MOUSE, 0, state)
    debug: mxutils.DebugNode = mxutils.DebugPrint.GetContainer(state, '^BFM_')
    print(f"\nMouse Input State:\n\n{debug.ToString()}")

    print("\n--- DebugPrint.GetParameters ------------------------------------------------------\n")

    # But when inspecting BaseList2D data containers, it is often more useful to use GetParameters, 
    # as it uses the description of the node and therefore always shows the correct symbolic names 
    # for the parameters and can also do more things. GetParameters has multiple arguments to display
    # ids, data types, do filtering, and more, see the docs for details.
    debug: mxutils.DebugNode = mxutils.DebugPrint.GetParameters(first)
    print(f"GetParameters(first) = \n{debug.ToString()}")

    print(f"\n--- DebugPrint.GetFlags -----------------------------------------------------------\n")

    # With GetFlags, you can inspect the flags of a node in a tree structure, similar to how
    # GetParameters works for parameters. This is useful for debugging the state of various
    # flags on a node. There are multiple parameters with which you can control the output, similar 
    # to GetParameters.
    debug: mxutils.DebugNode = mxutils.DebugPrint.GetFlags(first)
    print(f"GetFlags(first) = \n{debug.ToString()}")

    print("\n--- DebugPrint.GetBaseList --------------------------------------------------------\n")

    # GetBaseList combines the parameter and flag trees into one debug tree (and also offers the
    # combined tuning arguments of the other debug functions).
    debug: mxutils.DebugNode = mxutils.DebugPrint.GetBaseList(first)
    print(f"GetBaseList(first) = \n{debug.ToString()}")

    print(f"\n--- DebugPrint.GetGraph -----------------------------------------------------------\n")

    # And then there is GetGraph, which allows you to inspect the scene graph structure of a passed
    # node. We can use just as the other node related debug functions on any form of BaseList2D node,
    # e.g., a whole document as we do here, or just a single object within the scene. This will
    # effectively return the output of mxutils.IterateGraph as a tree, i.e., unpack hierarchical,
    # branching, and cache relationships of the passed node.

    debug: mxutils.DebugNode = mxutils.DebugPrint.GetGraph(doc)
    print(f"GetGraph(doc) = \n{debug.ToString()}")

    print(f"\n--- DebugPrint Diffing -----------------------------------------------------------\n")

    # All methods shown of the form GetXYZ also have a PrintXYZ counterpart that directly prints 
    # the debug information, but it is not shown for each case. But there are also diffing functions
    # for each category which let you compare the debug output of two inputs. This can be helpful
    # when trying to find out 'why does A not behave like B', which is a common debugging scenario.
    diff: str = mxutils.DebugPrint.DiffContainer(bc1, bc2)
    print(f"DiffContainer(bc1, bc2) = \n{diff}")

    diff: str = mxutils.DebugPrint.DiffParameters(first, second)
    print(f"DiffParameters(first, second) = \n{diff}")

    diff: str = mxutils.DebugPrint.DiffFlags(first, second)
    print(f"DiffFlags(first, second) = \n{diff}")

    diff: str = mxutils.DebugPrint.DiffBaseList(first, second)
    print(f"DiffBaseList(first, second) = \n{diff}")

    diff: str = mxutils.DebugPrint.DiffGraph(first, second)
    print(f"DiffGraph(first, second) = \n{diff}")

    
import importlib
if __name__ == "__main__":
    c4d.ClearPythonConsole()
    importlib.reload(mxutils.mxu_base)
    importlib.reload(mxutils.mxu_scene)
    importlib.reload(mxutils.mxu_provider)
    importlib.reload(mxutils)
    main()