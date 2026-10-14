"""Demonstrates important functions for the types c4d.DescID and c4d.DescLevel.

Topics:
    - Creating and using DescID and DescLevel objects
    - Accessing and modifying object parameters using DescID
    - Handling multi-level DescID for complex parameters

Related:
    scene/basics_parameters.py
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
    # Instantiate a cube object and insert it into the document.
    cube: c4d.BaseObject = mxutils.CheckType(c4d.BaseObject(c4d.Ocube))
    doc.InsertObject(cube) 
    doc.SetActiveObject(cube)

    # A DescID is an identifier for a specific parameter within an scene elements description. A
    # simple DescID can be constructed with just the parameter ID, as here done with the relative
    # position parameter of the object.
    pos: c4d.DescID = c4d.DescID(c4d.ID_BASEOBJECT_REL_POSITION)
    print(f"{pos = }")

    # This descID can be used to access or modify the corresponding parameter of the cube object.
    cube[pos] = c4d.Vector(100, 200, 300) # Example of setting the position using the DescID.
    # Which in this case is the same as:
    cube[c4d.ID_BASEOBJECT_REL_POSITION] = c4d.Vector(100, 200, 300)

    # But what we used above was actually a shorthand for creating a DescID. A DescID is composed
    # of up to three DescLevels and we could also define #pos like this. Practically, this is the
    # same as the shorthand we used earlier, but it explicitly shows the DescLevel structure.
    pos: c4d.DescID = c4d.DescID(c4d.DescLevel(c4d.ID_BASEOBJECT_REL_POSITION))

    # But even this was not the full complexity, as we used a shorthand for the DescLevel 
    # construction. At its fully complexity, the ID_BASEOBJECT_REL_POSITION parameter is being+
    # addressed like this:
    pos: c4d.DescID = c4d.DescID(
        # First desc level of the ID.
        c4d.DescLevel(
            c4d.ID_BASEOBJECT_REL_POSITION, # The ID of the parameter.
            c4d.DTYPE_VECTOR,               # The data type of the parameter.
            c4d.Ocube)                      # The creator of the parameter, passing 0 is also allowed
                                            # (at least in most cases).
        )

    # This full complexity #pos acts the same way as the shorthand versions above. In some very
    # rare cases such as constructing ports for Xpresso nodes, Cinema however forces us to be 
    # explicit about the full DescID structure.

    # Do exactly the same thing.
    print(f"\n{cube[pos] = }")
    print(f"{cube[c4d.ID_BASEOBJECT_REL_POSITION] = }")

    # So why exist there 'up to three DescLevels' in a DescID? The reason is that some parameters in 
    # Cinema 4D can be decomposed into sub-parameters, for example vectors.

    # Print the X component of the position vector.
    posx: c4d.DescID = c4d.DescID(
        # First level, the vector itself.
        c4d.DescLevel(c4d.ID_BASEOBJECT_REL_POSITION, c4d.DTYPE_VECTOR, c4d.Ocube),
        # Second level, the X component of the vector.
        c4d.DescLevel(c4d.VECTOR_X, c4d.DTYPE_REAL, c4d.Ocube)
    )
    print(f"\n{posx = }")
    print(f"{cube[posx] = }")

    # User data is another case of multi level DescIDs, as each user data parameter is nested under 
    # the user data container.

    # Add a new user data vector parameter to the cube.
    vector: c4d.BaseContainer = c4d.GetCustomDataTypeDefault(c4d.DTYPE_VECTOR)
    vector[c4d.DESC_NAME] = "Vector"
    did: c4d.DescID = cube.AddUserData(vector)

    # did is itself an example for a two-level DescID, because all user data parameters are 
    # nested under the user data container (ID_USERDATA).
    print(f"{did = }") # The full descID
    print(f"{did.GetDepth() = }") # it has two levels
    print(f"\n{cube[did] = }") # access the parameter value

    # Specifically access the levels and their data.
    print(f"\n{did[0].id = }")      # ID of the first level: ID_USERDATA
    print(f"{did[0].dtype = }")     # Type of the first level: DTYPE_SUBCONTAINER
    print(f"{did[0].creator = }")   # Creator of the first level: Ocube or 0.
    print(f"{did[1].id = }")        # ID of the second level: 1 (first user data parameter)
    print(f"{did[1].dtype = }")     # Type of the second level: DTYPE_REAL
    print(f"{did[1].creator = }")   # Creator of the second level, always 0. Because sub-levels do 
                                    # not have a creator.

    # These again are equivalent.
    cube[did] = c4d.Vector(1, 2, 3)
    cube[c4d.ID_USERDATA, 1] = c4d.Vector(3, 2, 1)

    c4d.EventAdd()

if __name__ == "__main__":
    c4d.ClearPythonConsole()
    main()
