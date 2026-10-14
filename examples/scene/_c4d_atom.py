"""Demonstrates important functions for the type c4d.C4DAtom.

The Cinema 4D scene data model is built around three fundamental base types which are in an 
inheritance relation, from which then almost all tangible scene elements such as documents, objects, 
tags, and materials are derived.

    Type                                            Example

    C4DAtom                                         scene/_c4d_atom.py
        GeListNode                                  scene/_c4d_gelistnode.py
            BaseList2D                              scene/_c4d_baselist2d.py
                [BaseDocument]
                [BaseMaterial]
                [BaseObject]
                [BaseTag]
                ...

Topics:
    - Type checks
    - Dirty checks
    - Identity and lifetime checks

Related:
    - data/_c4d_description.py
    - scene/basics_parameters.py
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
    # Instantiate a cube object which is a BaseObject derived from BaseList2D (and ultimately C4DAtom).
    cube: c4d.BaseObject = mxutils.CheckType(c4d.BaseObject(c4d.Ocube))
    doc.InsertObject(cube)

    # Atoms have many methods of which only a a subset is being covered in this example.

    print(f"--- Type Checks ------------------------------------------------------------------\n")

    # One of the fundamental functions of atoms are type checks. Other than native Python type checks
    # via isinstance(), or mxutils.CheckType(), atoms do type checking over integer IDs which allows
    # for more granular type checks compared to native Python type checks. Each scene element in 
    # Cinema 4D must be registered with a plugin ID which will then become its type ID.

    # Will print the integer type ID corresponding to c4d.Ocube: 5159.
    print(f"{cube.GetType() = }")
    print(f"{cube.GetType() == c4d.Ocube = }")

    # A native Python type check can only determine that #cube is of type c4d.BaseObject, but it 
    # cannot determine the specific type of the object (e.g., whether it is a cube, sphere, etc.).
    print(f"{isinstance(cube, c4d.BaseObject) = }")

    # There is also the method IsInstanceOf() which checks if the object is an instance of a specific 
    # type or any of its derived types. To do base class checks, there exist also symbols for base
    # types such as Obase for objects, Tbase for tags, Mbase for materials, and so on. There is also
    # the method CheckType() which does exactly the same as IsInstanceOf() but is a legacy method. We
    # recommend using IsInstanceOf() for type checks instead of CheckType().
    print(f"{cube.IsInstanceOf(c4d.Ocube) = }")
    print(f"{cube.IsInstanceOf(c4d.Obase) = }")

    # Such checks are commonly used in conditional statements to ensure that operations are performed
    # only on objects of the expected type. For example:
    if not cube.IsInstanceOf(c4d.Osphere):
        print(f"{cube} is not a sphere: {cube.IsInstanceOf(c4d.Osphere) = }")

    print(f"\n--- Dirty Checks -----------------------------------------------------------------\n")

    # Another important aspect of atoms is are checking dirty counts. BaseObject also provides an
    # IsDirty() method that can be used to check if the object has been modified since the last 
    # evaluation. But the atom methods are the atomic way to perform dirtiness checks (and also work
    # for all scene elements, not just BaseObjects.)

    # In principal there are two types of dirtiness checks: shallow and deep. Shallow get/set 
    # operations are done with GetDirty/SetDirty. They wil get or increment the dirty count of the
    # element the have been invoked on.

    # Get the dirty counts for the data and matrix flags, i.e., the counters for changes to the 
    # parameters and the transformation matrix of the object.
    print(f"{cube.GetDirty(c4d.DIRTYFLAGS_DATA) = }")
    print(f"{cube.GetDirty(c4d.DIRTYFLAGS_MATRIX) = }")

    # Now we change the cube's parameters and transformation matrix to trigger dirtiness.
    cube[c4d.PRIM_CUBE_LEN] = c4d.Vector(200, 200, 300)
    cube.SetMg(c4d.utils.MatrixMove(c4d.Vector(100, 100, 100)))

    # Get the updated dirty counts after the changes. Note that there is no guarantee that we might
    # consider a singular change entails an increment of exactly one in the dirty count. Here we
    # set a vector on the scene element which will result in an increment for each component of the 
    # vector. Changes guarantee an increment in the dirty count; but never assume the exact value.
    print(f"After changes - {cube.GetDirty(c4d.DIRTYFLAGS_DATA) = }")   # +3 
    print(f"After changes - {cube.GetDirty(c4d.DIRTYFLAGS_MATRIX) = }\n") # +1

    # And then there are deep dirtiness checks, which consider not only the object itself but also 
    # its descendants (get) or ancestors (set). These also categorize the dirtiness in a different
    # way than the shallow dirtiness checks. I.e., although these two methods are very similarly
    # named, they do entirely different things under the hood.

    # Get the animation and tag dirty flags for the cube.
    print(f"{cube.GetHDirty(c4d.HDIRTYFLAGS_ANIMATION) = }")
    print(f"{cube.GetHDirty(c4d.HDIRTYFLAGS_TAG) = }")

    # Now add a tag to the cube and give the tag a new track.
    tag: c4d.BaseTag = mxutils.CheckType(cube.MakeTag(c4d.Tvibrate))
    track = c4d.CTrack(tag, c4d.DescID(c4d.DescLevel(c4d.VIBRATEEXPRESSION_POS_ENABLE)))
    tag.InsertTrackSorted(track)

    # And now check the updated dirty counts for the animation and tag flags. We do this again on
    # the cube. The tag change propagates up to the cube, and so did the track change which went
    # track -> tag -> cube. This will also work for much more complex nested relationships.
    print(f"After changes - {cube.GetHDirty(c4d.HDIRTYFLAGS_ANIMATION) = }")
    print(f"After changes - {cube.GetHDirty(c4d.HDIRTYFLAGS_TAG) = }")

    print(f"\n--- Identity Checks and Lifetime -------------------------------------------------\n")

    # Another big part of atoms is that they provide indirect access to markers via FindUniqueID
    # and AddUniqueID which allows us to mark scene elements with unique identifiers for later 
    # retrieval.

    # Encode a marker into bytes and store it in the element. You need a unique plugin ID to do this.
    # Register your plugin ID under https://developers.maxon.net/forum/pid.
    pluginId: int = 1070290
    payload: bytes = b"bob is your uncle"
    cube.AddUniqueID(pluginId, payload)

    # And get it back. Please understand that this is indeed a marker system and not a general-purpose 
    # storage system. You can mark an a scene element for example as being associated with the 
    # Vector(1, 2, 3) when this would be somehow important for scene evaluation. But you should not
    # use this to simply store the vector for convenience. I.e., markers are meant to identify scene 
    # elements uniquely.
    data: memoryview = cube.FindUniqueID(pluginId)
    print(f"Retrieved data - {data.tobytes() = }")

    # One of the most important markers is the marker with the ID MAXON_CREATOR_ID. Cinema 4D will
    # automatically assign such marker to each object when it is being created (which is different
    # from instantiation). This marker will stay the same over the whole lifetime of the object,
    # including scene save/load events, node re-instantiation, and more. The marker is also 
    # guaranteed to be unique within the entire scene.
    creatorId: memoryview = cube.FindUniqueID(c4d.MAXON_CREATOR_ID)
    print(f"Creator ID - {creatorId.tobytes() = }")

    # This is especially important in Python because scene element references (atoms) can become
    # dangling here, 'not alive' in the terms of the Python API. In a script like this, this will
    # usually not happen. But when you have some code which either holds long time references to 
    # scene elements or carries out operations which might invalidate them, the references can 
    # become dangling and you need to check their validity.

    if not cube.IsAlive():
        print("Cube reference is no longer valid.")

    # This is a common problem in Python which can be solved with markers such as MAXON_CREATOR_ID.
    # As we then can simply walk the scene to try to find the elements again. When it has been
    # reallocated by Cinema, i.e., the same data exists just in a different memory location, we will
    # find it again, otherwise the element has been deleted.

    # We lost #cube, but we have still stored its #creatorId. When #cube was dead at this point, we
    # could no longer call any methods on it, so the create ID must be stored beforehand. With it
    # and one of the traversal functions, we can find it again. Since we know it was an object, 
    # IterateTree will be enough, but we could also use IterateGraph if we did not even knew the 
    # type of the element.
    for obj in mxutils.IterateTree(doc.GetFirstObject(), yieldSiblings=True):
        if obj.FindUniqueID(c4d.MAXON_CREATOR_ID) == creatorId:
            print(f"\nFound cube again - {obj = }")

    # Please also note in this context that comparing two object references directly is not a 
    # reliable way to check if two elements are the same. You are comparing references, i.e., 
    # wrappers of the actual scene element and two different wrappers can point to the same 
    # underlying element.

    # A simpler interface to all this is C4DAtom.__hash__ which express MAXON_CREATOR_ID in a
    # Pythonic manner as an integer instead of the bytes representation via FindUniqueID.
    print(f"\n{hash(cube) = }")
    # Guaranteed to be True, even for two different references.
    print(f"{hash(cube) == hash(cube) = }")

    # This also means scene elements can be used in any anything hash based, such as dictionaries 
    # or sets.
    lookup: dict[int, any] = {}

    lookup[cube] = "Some data" # the more verbose form would be: lookup[hash(cube)] = "Some data"
    if hash(cube) in lookup:
        print(f"\nFound data for cube: {lookup[hash(cube)]}")

    # The two other big concepts in atoms, parameter and descriptions are handled in the examples:
    # scene/basics_parameters.py and data/_c4d_description.py respectively. Please read them to learn
    # more. about C4DAtom.GetDescription() and C4DAtom.Get/SetParameter() methods.

    c4d.EventAdd()

if __name__ == "__main__":
    c4d.ClearPythonConsole()
    main()
