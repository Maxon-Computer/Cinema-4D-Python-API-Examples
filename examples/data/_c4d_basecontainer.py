"""Demonstrates the usage of the fundamental container type in the Cinema API.

Run this example in the Cinema 4D Script Manager.

Topics:
    - Copying containers
    - Iterating over containers
    - Nested containers
    - Container IDs
    - Using containers in message and callback contexts
"""
__author__ = "Ferdinand Hoppe"
__copyright__ = "Copyright (C) 2026 MAXON Computer GmbH"
__license__ = "Apache-2.0 License"
__version__ = "2027"

import c4d
import mxutils

doc: c4d.documents.BaseDocument # The active document.


def main() -> None:
    """Demonstrates the usage of the fundamental container type in the Cinema API.
    """
    # BaseContainer is the type which holds most bundles of scene data. Each BaseList2D, i.e.,
    # scene element, has a container which holds most, but not all, of its data. There are two
    # ways to get the data container of a scene element.

    # Create a new scene element, a cube.
    cube: c4d.BaseObject = mxutils.CheckType(c4d.BaseObject(c4d.Ocube))
    doc.InsertObject(cube)

    # BaseList2D.GetData() returns a COPY of the data container, so that modifications to the 
    # returned container do not affect the scene element. It is not recommend to use GetData() 
    # for modifying scene elements, as reading and writing the full container is quite expensive.
    dataCopy: c4d.BaseContainer = cube.GetData()

    # BaseList2D.GetContainerInstance() returns a reference to the data container, so that
    # modifications to the returned container do affect the scene element.
    dataRef: c4d.BaseContainer = cube.GetDataInstance()

    # Set the size of the cube by writing to its data container.
    dataRef[c4d.PRIM_CUBE_LEN] = c4d.Vector(200.0, 200.0, 200.0)

    # We can also iterate over the container, which yields key-value pairs. Note that symbols, e.g.,
    # c4d.PRIM_CUBE_LEN, are just integer constants, so the keys are integers. 
    for key, value in dataRef:
        print(f"Key: {key}, Value: {value}")

    # We can also construct containers ourself and containers can be nested.
    myContainer: c4d.BaseContainer = c4d.BaseContainer()
    myContainer[1000] = "Hello World"
    myContainer[1001] = 42
    subContainer: c4d.BaseContainer = c4d.BaseContainer()
    subContainer[2000] = c4d.Vector(1.0, 2.0, 3.0)
    myContainer[1002] = subContainer

    # There are also specific functions to get and set values of a specific type, but we usually do 
    # not need them in Python, there are just a reflection of the C++ API.
    subContainer.SetInt32(2001, 42)
    value: int = subContainer.GetInt32(2001)

    # Besides atomic types such as int, float, bool, str, and vectors, BaseContainer can also hold 
    # more complex types. In Python we do not have all the options of the C++ API, but we can for 
    # example store a BaseLink or BaseTime in a container.
    subContainer[2002] = c4d.BaseTime(1.0)
    subContainer[2003] = cube

    # Now we can retrieve the values we stored in the container. Note that we stored a LINK to the 
    # cube in the container, not the object itself. For retrieving the linked object, it can be 
    # useful to use the dedicated GetLink() function, as we can specify there in which document we 
    # want to look for the linked object.
    time: c4d.BaseTime = subContainer[2002]
    linkedObject: c4d.BaseObject = subContainer[2003]

    # Container can be copied with GetClone().
    containerCopy: c4d.BaseContainer = myContainer.GetClone(c4d.COPYFLAGS_NONE)
    # And we can copy one container into another with CopyTo().
    containerCopy.CopyTo(myContainer, c4d.COPYFLAGS_NONE)
    # And we can flush a container with FlushAll(), which removes all key-value pairs.
    containerCopy.FlushAll()

    # Containers can have an ID. By default it is 0, but in a message context, this is sometimes set 
    # to the message ID. We can also specify an ID when constructing a container.
    myContainerWithID: c4d.BaseContainer = c4d.BaseContainer(42)
    myContainerWithID.SetId(24)
    cid: int = myContainerWithID.GetId()

    # Finally, we often encounter containers in message and callback contexts. Here we get for 
    # example the state of the mouse.
    state: c4d.BaseContainer = c4d.BaseContainer()
    c4d.gui.GetInputState(c4d.BFM_INPUT_MOUSE, 0, state)

    # A useful tool when dealing with containers can be the function GetContainerTreeString(), which 
    # returns a string representation of the container and its contents. It also has builtin symbol 
    # translation for the Cinema 4D symbols, so that we can see the symbol names instead of just the 
    # integer values. See the documentation of GetContainerTreeString() for more information.
    print(f"\nMouse Input State:\n\n{mxutils.GetContainerTreeString(state, '^BFM_')}")

    c4d.EventAdd()


if __name__ == "__main__":
    main()
