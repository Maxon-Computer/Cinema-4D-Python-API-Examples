"""Demonstrates important functions for the type c4d.GeListNode.

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
    - Hierarchy functions
    - Branching functions
"""
__author__ = "Ferdinand Hoppe"
__copyright__ = "Copyright (C) 2026 MAXON Computer GmbH"
__license__ = "Apache-2.0 License"
__version__ = "2027.0.0"
__date__ = "07/09/2026"

import c4d
import mxutils
from collections.abc import Iterator


doc: c4d.documents.BaseDocument # The active Cinema 4D document.
op: c4d.BaseObject | None # The currently selected object in the Cinema 4D document, can be None.


def IterateTree(node: c4d.GeListNode | None) -> Iterator[c4d.GeListNode]:
    """Yields a node and its descendants using GeListNode navigation methods.
    """
    while node:
        yield node
        yield from IterateTree(node.GetDown())
        node = node.GetNext()


def main() -> None:
    """Runs the example.
    """
    def Callback(node: c4d.BaseObject) -> None:
        """Customizes the objects created by AddHierarchyFromString.
        """
        node.ChangeNBit(c4d.NBIT_OM1_FOLD, c4d.NBITCONTROL_SET)
        node.MakeTag(c4d.Tdisplay)
        if node.GetType() in (c4d.Osphere, c4d.Ocone, c4d.Ocylinder):
            tag: c4d.BaseTag = mxutils.CheckType(node.MakeTag(c4d.Tphong))
            tag[c4d.PHONGTAG_PHONG_ANGLELIMIT] = True

    print("\n--- Setup -------------------------------------------------------------------------\n")

    # Int this section we only create an 'interesting' scene to traverse.

    # Flush the document and create the following object hierarchy which we will use for the 
    # traversal examples.
    #
    #    A
    #    ├─ B
    #    │  ├─ C
    #    │  ├─ D
    #    │  │  └─ E
    #    │  └─ F
    #    G
    #    └─ H
    #
    doc.Flush()
    objects: list[c4d.BaseObject] = mxutils.g_scene_faker.AddHierarchyFromString(
        doc,
        f"""
        A
            B::{c4d.Ocube}
                C::{c4d.Osphere}
                D::{c4d.Ocone}
                    E::{c4d.Osphere}
                F::{c4d.Ocylinder}
        G
            H
        """,
        callback=Callback
    )

    # Add some random materials to the scene.
    mxutils.g_scene_faker.AddRandomMaterials(doc, minCount=5, maxCount=5, objects=objects)

    print("\n--- Hierarchy Functions -----------------------------------------------------------\n")

    # c4d.GeListNode is one of the fundamental building blocks of the Cinema API. It expresses 
    # hierarchical and branching relations, Cinema's take on a scene graph. Many types in the
    # Cinema API are derived from c4d.GeListNode, including documents, objects, tags, materials,
    # shaders, tracks, curves, and many more.

    # Get the first object in the document, the node "A" we created above.
    a: c4d.BaseObject | None = doc.GetFirstObject()
    print(f"{a = }")

    # Get the first child of "A", which is "B".
    aDown: c4d.BaseObject | None = a.GetDown() if a else None
    print(f"{aDown = }")

    # Get the parent of "B", which is "A".
    bParent: c4d.BaseObject | None = aDown.GetUp() if aDown else None
    print(f"{bParent = }")

    # Get the next sibling of "A", which is "G".
    aNext: c4d.BaseObject | None = a.GetNext() if a else None
    print(f"{aNext = }")

    # Get the previous sibling of "G", which is "A".
    prevG: c4d.BaseObject | None = aNext.GetPred() if aNext else None
    print(f"{prevG = }")

    # Since a document is also a c4d.GeListNode, we can for example also call GetNext() on it to
    # get the next document in the document list (if there is one). But a document will not have
    # children or a parent.
    nextDoc: c4d.documents.BaseDocument | None = doc.GetNext()
    print(f"{nextDoc = }")

    # Finally, the Python API (other than the C++ API) also has the convenience method GetChildren()
    # which returns a list of all DIRECT children of a node (i.e., not all descendants).
    childrenA: list[c4d.BaseObject] = a.GetChildren() if a else []
    print(f"{childrenA = }")

    # Last but not least, we can always get the document a node belongs with GetDocument().
    docOfA: c4d.documents.BaseDocument | None = a.GetDocument() if a else None
    print(f"{docOfA = }")

    # And finally, nodes have the function Remove() to remove a node from its tree, and the functions
    # InsertUnder() and InsertUnderLast() to insert a node under another node. Due to the concept of
    # branches, inserting a node not under another node but into a document requires specific insertion 
    # methods such as BaseDocument.InsertObject() which are demonstrated in the  node type specific 
    # examples.

    # Create four null object nodes.
    null1: c4d.BaseObject = c4d.BaseObject(c4d.Onull)
    null2: c4d.BaseObject = c4d.BaseObject(c4d.Onull)
    null3: c4d.BaseObject = c4d.BaseObject(c4d.Onull)
    null4: c4d.BaseObject = c4d.BaseObject(c4d.Onull)

    # Insert null2 under null1.
    null2.InsertUnder(null1)

    # If we would now call InsertUnder(null3) on null1 again, we would end up with:
    #
    #    null1
    #     ├── null3
    #     └── null2
    #
    # Because InsertUnder() would be more aptly named as InsertUnderFirst(), i.e., it inserts the
    # node as the first child of the specified parent. But since we usually want to append nodes 
    # as the last child, we should usually use InsertUnderLast() as our default method.
    null3.InsertUnderLast(null1)

    # A node can never be parented to more than one node (Cinema's graphs are mono-hierarchical).
    # The Python API already enforces this for us by calling #Remove on a node before it is being
    # inserted under another node. In C++ that is not the case.

    # null 2 has been removed from null1 as a parent and is now a child of null3.
    null2.InsertUnderLast(null3)

    # Manually remove null3 from null1 (and with that also null2 from null1).
    null3.Remove()

    # With the methods InsertBefore and InsertAfter we can insert a node relative to a sibling node.
    null2.InsertUnderLast(null1)   # Insert null2 under null1 as the last child.
    null3.InsertAfter(null2)       # Insert null3 after null2 in the hierarchy.
    null4.InsertBefore(null2)      # Insert null4 before null2 in the hierarchy.

    print("\n--- Branching Functions -------------------------------------------------------------")

    # What are Branches?
    #
    # Branches are Cinema's twist on arbitrary relationships between nodes. Each GeListNode can have
    # in addition to its hierarchical relationships arbitrary relations to other nodes. A document
    # has for example an 'Objects' branch which holds the the hierarchy of all objects, and a 
    # 'Materials' branch which holds the hierarchy of all materials. An object in turn has for 
    # example a 'Tag' branch which holds all its tags and a 'Tracks' branch which holds all its 
    # tracks. And tracks have ten curve branches, etc. In this manner, Cinema 4D realizes what is
    # commonly referred to as a "scene graph".

    # Branches are reachable via the function GetBranchInfo. Here we get the branches for a document.
    branches: list[dict[str, any]] = doc.GetBranchInfo(c4d.BRANCHINFOFLAGS_NONE) or []
    print(f"{branches = }")

    # Branches are practically realized with the type c4d.GeListHead (a subtype of GeListNode), which 
    # serves as the root for a branch. So, we have a tree GeListNode's (for example an object tree),
    # where each node points to a couple of GeListHeads (its branches), which then hold the hierarchy 
    # of nodes within that branch.

    # Get the the branch head for the branch with the id Obase in the document: The object branch.
    objectHead: c4d.GeListHead | None = next(
        (n.get("head") for n in branches if n.get("id") == c4d.Obase), None)

    # Get the the branch head for the branch with the id Mbase in the document: The material branch.
    materialHead: c4d.GeListHead | None = next(
        (n.get("head") for n in branches if n.get("id") == c4d.Mbase), None)

    # There also exists 'name' and 'flags' metadata for each branch, which is being ignored here.

    print(f"{objectHead = }")
    print(f"{materialHead = }")

    # Since branch heads are also c4d.GeListNode, we can use the traversal methods we already know.
    print(f"\nIterating over the object branch:")
    for node in IterateTree(objectHead.GetDown() if objectHead else None):
        print(f"{node = }")

    print(f"\nIterating over the material branch:")
    for node in IterateTree(materialHead.GetDown() if materialHead else None):
        print(f"{node = }")

    # You can get the GeListHead for given node with GetListHead.
    first: c4d.BaseObject | None = objectHead.GetDown()
    second: c4d.BaseObject | None = first.GetNext()

    firstHead: c4d.GeListHead | None = first.GetListHead()
    secondHead: c4d.GeListHead | None = second.GetListHead()
    print(f"\n{firstHead = }")
    print(f"{secondHead = }")
    print(f"{firstHead == secondHead}") # They are the same because both nodes belong to the same branch.

    # You can get the owner, i.e., the node that holds the branch of a given node, with GetMain().
    firstMain: c4d.GeListNode | None = first.GetMain() if first else None
    seconmdMain: c4d.GeListNode | None = second.GetMain() if second else None
    print(f"\n{firstMain = }")
    print(f"{seconmdMain = }")

    # Push an update event so that our scene changes are reflected in the Cinema 4D interface.
    c4d.EventAdd()

if __name__ == "__main__":
    c4d.ClearPythonConsole()
    main()
