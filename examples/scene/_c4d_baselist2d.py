"""Demonstrates important functions for the type c4d.BaseList2D.

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
    - data/_c4d_basecontainer.py
    - data/_c4d_description.py
    - scene/basics_parameters.py
    - scene/layers.py
    - scene/userdata.py
    - animation/tracks.py

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
    print(f"\n--- Instantiation ----------------------------------------------------------------\n")

    # You can instantiate each scene element that derives from BaseList2D, such as documents,
    # objects, tags, etc. via the BaseList2D initialization. It is more common to use the derived 
    # class initialization methods instead due to better readability but the BaseList2D 
    # initialization is functionally equivalent. It can be useful when you do not know what kind of
    # scene element you are dealing with at runtime.

    # Instantiate a sphere via the BaseList2D initialization and BaseObject initialization. In both
    # cases, the result will be an Osphere BaseObject.
    sphereA: c4d.BaseObject = mxutils.CheckType(c4d.BaseList2D(c4d.Osphere))
    sphereB: c4d.BaseObject = mxutils.CheckType(c4d.BaseObject(c4d.Osphere))

    print(f"{sphereA = }")
    print(f"{sphereB = }")

    # The same for a tag ...
    tagA: c4d.BaseTag = mxutils.CheckType(c4d.BaseList2D(c4d.Tphong))
    tagB: c4d.BaseTag = mxutils.CheckType(c4d.BaseTag(c4d.Tphong))
    print(f"{tagA = }")
    print(f"{tagB = }")

    # ... or a document.
    docA: c4d.documents.BaseDocument = mxutils.CheckType(c4d.BaseList2D(c4d.Tbasedocument))
    docB: c4d.documents.BaseDocument = mxutils.CheckType(c4d.documents.BaseDocument())
    print(f"{docA = }")
    print(f"{docB = }")

    sphereA.InsertTag(tagA)
    sphereB.InsertTag(tagB)
    doc.InsertObject(sphereA)
    doc.InsertObject(sphereB)

    print(f"\n--- Flags ------------------------------------------------------------------------\n")

    # BaseList2D also provides a set flag functions, the BIT_ flags. These are not to be confused
    # with the GelistNode NBIT_ flags. Both flag sets serve different purposes, and generally, the
    # NBIT_ flags are more important.

    # Mark the two objects and their tags we added as active. They will appear as selected in the
    # Object Manger and show up in the Attribute Manager.
    sphereA.SetBit(c4d.BIT_ACTIVE)
    sphereB.SetBit(c4d.BIT_ACTIVE)
    tagA.SetBit(c4d.BIT_ACTIVE)
    tagB.SetBit(c4d.BIT_ACTIVE)

    # Get the selection state of sphereA.
    isSphereAActive: int = sphereA.GetBit(c4d.BIT_ACTIVE)
    print(f"{isSphereAActive = }")

    # Remove the active state from sphereA.
    sphereA.DelBit(c4d.BIT_ACTIVE)

    # Print the BIT_ flags of the sphereB object. Note: This function will also print internal flags
    # which might not be officially documented.
    mxutils.DebugPrint.PrintFlags(sphereB, showNBit=False)

    print(f"\n--- Names, Type Name, and Icons --------------------------------------------------\n")

    # Set and get the name of elements as it is shown in the Object, Material, Layer, etc. manager
    # or wherever the name is displayed in the Cinema 4D interface.
    sphereA.SetName("sphereA") # Same as sphereA[c4d.ID_BASELIST_NAME] = "sphereA"
    sphereB.SetName("sphereB")
    print(f"{sphereA.GetName() = }") # Same as sphereA[c4d.ID_BASELIST_NAME]
    print(f"{sphereB.GetName() = }")

    # You can also get the type name of an element, which can be helpful when an object has be renamed
    # but is generally a bit misleading. When you need a type identifier for an element, it is better 
    # to use the object's type ID.
    print(f"{sphereA.GetTypeName() = }")
    print(f"{sphereA.GetType() = }")

    # Finally, you can get the icon of a node via GetIcon(). This is quite similar to allocating a
    # a resource icon, but GetIcon() will reflect a element's customized icon such as tinting or
    # overlays, while the resource icon is just the base. But in most cases, both are the same.
    icon: dict = sphereA.GetIcon()
    bmp: c4d.BaseBitmap = icon.get("bmp")
    bmp2: c4d.BaseBitmap = c4d.bitmaps.InitResourceBitmap(sphereA.GetType())

    # Uncomment the following lines to display the bitmaps.
    # c4d.bitmaps.ShowBitmap(bmp, "element icon")
    # c4d.bitmaps.ShowBitmap(bmp2, "type resource icon")

    print(f"{icon = }")

    print(f"\n--- Data Container ---------------------------------------------------------------\n")

    # A BasesList2D also provides access to the data container of a node. This holds all parameter
    # values specific for this element (but not the ones shared via its base type). This is part
    # of the parameter model subject. For details, see the parameter model and BaseContainer 
    # examples referenced at the top of this file.

    # Get a reference to the data container of sphereA.
    data: c4d.BaseContainer = sphereA.GetDataInstance()
    print(f"{data = }")

    # Modify the sphere radius parameter in the data container. This will affect the node in the document
    # since we are working on the actual data instance of the node.
    data[c4d.PRIM_SPHERE_RAD] = 200.0

    # Sometimes we do not want to modify the actual data instance directly. In such cases, we can
    # work on a copy of the data container instead.

    dataCopy: c4d.BaseContainer = data.GetClone(c4d.COPYFLAGS_NONE)
    dataCopy[c4d.PRIM_SPHERE_RAD] = 100.0
    print(f"{dataCopy = }")

    # We can also overwrite the full container of an element. Here we write our copy into sphereB.
    # This is an easy way to copy most of the parameters from one object to another. Things such
    # as the object name or coordinates are not part of the container model since they are base
    # parameters of objects and therefore not expressed in the data container.
    sphereB.SetData(dataCopy)

    # With mxutils.DebugPrint and its PrintContainer and DiffContainer functions, we can print and
    # diff container contents for debugging purposes. The last call will print this, showing us that
    # these two sphere objects parameter wise only differ in their radius parameter.
    #
    #       --- first
    #       +++ second
    #       @@ -1,5 +1,5 @@
    #       Root (None , id = -1):
    #      -├── 1110 (DTYPE_REAL): 200.0
    #      +├── 1110 (DTYPE_REAL): 100.0
    #       ├── 1112 (DTYPE_LONG): 0
    #       ├── 1111 (DTYPE_LONG): 32
    #       ├── 1113 (DTYPE_LONG): 1
    #
    print("\nDebugPrint.PrintContainer(sphereA.GetDataInstance()):")
    mxutils.DebugPrint.PrintContainer(sphereA.GetDataInstance())
    print("DebugPrint.PrintContainer(sphereB.GetDataInstance()):")
    mxutils.DebugPrint.PrintContainer(sphereB.GetDataInstance())
    print("\nDebugPrint.DiffContainer(sphereA.GetDataInstance(), sphereB.GetDataInstance()):")
    print(mxutils.DebugPrint.DiffContainer(sphereA.GetDataInstance(), sphereB.GetDataInstance()))

    print(f"\n--- Owner and Implementation Access ----------------------------------------------\n")

    # With GetMain() you can access the branch owner of an element. The object for a tag, the 
    # material for a shader, the document for an object, and so on. See the _c4d_gelistnode.py
    # example for more details.
    owner: c4d.BaseList2D = sphereA.GetMain()
    print(f"{owner = }") # In this case the owner is the document.

    # You can also access the implementation of an element using GetNodeData(). But this of course
    # requires you having access to the implementation of the element, which will be only the case
    # for your own plugins. We use here the Rounded Tube object from the Python SDK as an example.
    pidRoundedTube: int = 1025250
    try:
        tube: c4d.BaseObject = c4d.BaseObject(pidRoundedTube)
        doc.InsertObject(tube)

        impl: c4d.plugins.NodeData = tube.GetNodeData()
        print(f"{impl = }")
    except BaseException as e:
        print(f"Exception: You likely do not have the Python SDK installed: {e}")

    # Somewhat related to this is that you can access the flags with which a NodeData hook has been
    # registered via GetInfo() (registered for example via RegisterObjectPlugin for an object). This
    # works for all elements, including native ones, not just your own plugins. In rare cases this can
    # be useful to classify an element.
    cube: c4d.BaseObject = mxutils.CheckType(c4d.BaseObject(c4d.Ocube))
    bend: c4d.BaseObject = mxutils.CheckType(c4d.BaseObject(c4d.Obend))

    # Check the type of the objects using their info flags. There is no central place to find all
    # these flags, you must look into the respective registration function for an element type to
    # find them. E.g., c4d.plugins.RegisterObjectPlugin for an object.
    print(f"{cube.GetInfo() & c4d.OBJECT_GENERATOR == c4d.OBJECT_GENERATOR = }") # A cube is a generator object.
    print(f"{bend.GetInfo() & c4d.OBJECT_MODIFIER == c4d.OBJECT_MODIFIER = }") # A bend is a modifier object.

    print(f"\n--- Tracks -----------------------------------------------------------------------\n")

    # Another component of BaseList2D is tracks, which are used for animation. Each BaseList2D
    # element can have multiple tracks associated with it.

    # Create a new position track for sphereA.
    posTrackId: c4d.DescID = c4d.DescID(c4d.DescLevel(c4d.ID_BASEOBJECT_POSITION, c4d.DTYPE_VECTOR, 0))
    track: c4d.CTrack = c4d.CTrack(sphereA, posTrackId)
    sphereA.InsertTrackSorted(track)

    # Find the post track on the sphereA object.
    posTrack: c4d.CTrack | None = sphereA.FindCTrack(posTrackId)

    # Iterate over all tracks on the sphereA object.
    for track in sphereA.GetCTracks():
        print(f"{track = }")

    # Note that we only created a position track for sphereA, but not a curve or keys. See the
    # animation/ examples in general and animation/tracks.py in particular for more details on the
    # tracks and animation system in Cinema 4D.

    c4d.EventAdd()

if __name__ == "__main__":
    c4d.ClearPythonConsole()
    doc.Flush()
    main()
