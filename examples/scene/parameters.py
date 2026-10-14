"""Demonstrates different ways to access and modify parameters of Cinema 4D scene elements.

Topics:
    - Atomic parameter access
    - Bracket operator access
    - Data container access

Related:
    - data/_c4d_basecontainer.py
    - data/_c4d_descid.py
    - scene/_c4d_atom.py
    - scene/_c4d_gelistnode.py
    - scene/_c4d_baselist2d.py
"""
__author__ = "Ferdinand Hoppe"
__copyright__ = "Copyright (C) 2026 MAXON Computer GmbH"
__license__ = "Apache-2.0 License"
__version__ = "2027.0.0"
__date__ = "07/09/2026"

import c4d
import mxutils


doc: c4d.documents.BaseDocument # The active Cinema 4D document.
op: c4d.BaseObject | None # The currently selected object in the Cinema 4D document, can be None.


def main() -> None:
    """Runs the example.
    """
    # Instantiate a cube. What is shown here would work for any type of BaseList2D scene element,
    # not just objects. E.g., documents, materials, tags, etc.
    cube: c4d.BaseObject = mxutils.CheckType(c4d.BaseObject(c4d.Ocube))
    doc.InsertObject(cube)

    # Cinema 4D has a parameter model then provides multiple ways to get or set parameters for scene 
    # elements.

    print(f"--- Atom Access --------------------------------------------------------------------\n")

    # First of all, there is the atomic parameter access via C4DAtom.Get/SetParameter methods. It is
    # the most powerful way to access and modify parameters of scene elements but usually also the
    # most cumbersome one.

    # Set the size parameter of the cube using the atomic access methods.
    cube.SetParameter(c4d.PRIM_CUBE_LEN, c4d.Vector(200, 200, 200), c4d.DESCFLAGS_SET_NONE)
    print(f"{cube.GetParameter(c4d.PRIM_CUBE_LEN) = }")

    # We can also set parameters using DescIDs instead of integer symbols.
    cube.SetParameter(c4d.DescID(c4d.PRIM_CUBE_LEN), c4d.Vector(200, 200, 200), c4d.DESCFLAGS_SET_NONE)
    print(f"{cube.GetParameter(c4d.DescID(c4d.PRIM_CUBE_LEN)) = }")

    # What makes SetParameter calls more powerful is that we have here the get/set flags. We can
    # for example simulate a user interaction as shown below. Other than for the two other methods,
    # we also get a return value for set operations, indicating whether the operation was successful.
    # But failure is extremely rare in typical usage scenarios.
    if not cube.SetParameter(c4d.PRIM_CUBE_LEN, c4d.Vector(200, 200, 200), c4d.DESCFLAGS_SET_USERINTERACTION):
        print("Failed to set cube size with user interaction.")

    print(f"--- Bracket Operator Access --------------------------------------------------------\n")

    # Unique to Python is the bracket operator access for parameters. We can again use both plain
    # integers and DescIDs with the bracket operator. For example:

    cube[c4d.PRIM_CUBE_LEN] = c4d.Vector(200, 200, 200)
    cube[c4d.DescID(c4d.PRIM_CUBE_LEN)] = c4d.Vector(200, 200, 200)

    print(f"{cube[c4d.PRIM_CUBE_LEN] = }")
    print(f"{cube[c4d.DescID(c4d.PRIM_CUBE_LEN)] = }")

    print(f"--- Data Container Access ----------------------------------------------------------\n")

    # Each scene element has a data container that stores the parameters unique to that element. I.e.,
    # things that show up in the Basic Tab (Name, Color, etc.) or Coordinates Tab (Position, 
    # Rotation, Scale) are not part of the data container. Only the parameters that are specific to 
    # the element itself are stored there. We also cannot use DescIDs with the data container; only 
    # the integer symbols work.

    data: c4d.BaseContainer = cube.GetDataInstance()
    
    # Modify the cube length parameter in the data container. This will affect the node in the document
    # since we are working on the actual data instance of the node.
    data[c4d.PRIM_CUBE_LEN] = c4d.Vector(200, 200, 200)

    # Sometimes we do not want to modify the actual data instance directly. In such cases, we can
    # work on a copy of the data container instead.
    copy: c4d.BaseContainer = data.GetClone(c4d.COPYFLAGS_NONE)
    copy[c4d.PRIM_CUBE_LEN] = c4d.Vector(100, 100, 100)
    print(f"{copy = }")

    # We can also overwrite the full container of an element. Here we write our copy into the cube.
    # This is an easy way to copy most of the parameters from one object to another.
    cube.SetData(copy)

    # There exist also type specific access methods.
    copy.SetVector(c4d.PRIM_CUBE_LEN, c4d.Vector(300, 300, 300))
    size: c4d.Vector = copy.GetVector(c4d.PRIM_CUBE_LEN)
    print(f"{size = }")

if __name__ == "__main__":
    c4d.ClearPythonConsole()
    main()
