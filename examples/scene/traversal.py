"""Demonstrates scene traversal.

Topics:
    * Safely navigating a node hierarchy
    * Traversing node trees in different orders
    * Traversing hierarchies, caches, and branches as a graph
    * Filtering graph traversal by branch and node type
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
    def Callback(node: c4d.BaseObject) -> None:
        """Unfolds the objects added by AddHierarchyFromString and adds tags to them.
        """
        node.ChangeNBit(c4d.NBIT_OM1_FOLD, c4d.NBITCONTROL_SET)
        node.MakeTag(c4d.Tdisplay)
        if node.GetType() in (c4d.Osphere, c4d.Ocone, c4d.Ocylinder):
            tag: c4d.BaseTag = mxutils.CheckType(node.MakeTag(c4d.Tphong))
            tag[c4d.PHONGTAG_PHONG_ANGLELIMIT] = True

    print("\n--- Setup -------------------------------------------------------------------------\n")

    # Build the hierarchy used by the traversal examples.
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

    # Add random layers, render data, materials, and tracks to the scene.
    mxutils.g_scene_faker.RandomizeTransform(
        objects, minPosition=c4d.Vector(-500), maxPosition=c4d.Vector(500))
    mxutils.g_scene_faker.AddRandomLayers(doc, minCount=2, maxCount=2)
    mxutils.g_scene_faker.AddRandomRenderData(doc, minCount=2, maxCount=2)
    mxutils.g_scene_faker.AddRandomMaterials(doc, minCount=5, maxCount=5, objects=objects)
    mxutils.g_scene_faker.AddRandomTracks(objects, minCount=2, maxCount=2, minKeys=2, maxKeys=2)

    rData: c4d.documents.RenderData = mxutils.CheckType(doc.GetActiveRenderData())
    rData[c4d.RDATA_RENDERENGINE] = c4d.RDATA_RENDERENGINE_STANDARD

    print("\n--- Getting Nodes -----------------------------------------------------------------\n")

    # GetNodeFromPath() is the recommend way to retrieve nodes by a hierarchical path which is deeper
    # than one level. Chaining multiple calls to GetDown(), GetNext(), etc., will otherwise lead to
    # cryptic runtime errors when a path does not exist.

    # Get the first object in the document, which is "A".
    a: c4d.BaseObject | None = mxutils.CheckType(doc.GetFirstObject())
    if a is None:
        raise ValueError("The first object in the document is not found.")

    # Get the node down from "A", which is "B". We could also simply write a.GetDown() in this case
    # and it would be functionally equivalent and also slightly faster.
    b: c4d.BaseObject | None = mxutils.GetNodeFromPath(a, "d")
    
    # Get the down, down, next, down node from "A", which is "E" (A -> B -> D -> E). For a failing
    # path the function will simply return None. You can also pass the last argument raisePathErrors
    # as True to raise an error if the path does not exist.
    e: c4d.BaseObject | None = mxutils.GetNodeFromPath(a, "ddnd") #

    # More of the same, they are needed for examples below.
    f: c4d.BaseObject | None = mxutils.GetNodeFromPath(a, "ddnn")
    h: c4d.BaseObject | None = mxutils.GetNodeFromPath(a, "nd")
    
    print(f"GetNodeFromPath(a, 'd') = {b}")
    print(f"GetNodeFromPath(a, 'ddnd') = {e}")
    print(f"GetNodeFromPath(a, 'ddnn') = {f}")
    print(f"GetNodeFromPath(a, 'nd') = {h}")

    # The function GetRootNode() retrieves the top-most ancestor of the given node (its root). You
    # can also use GetNodeFromPath(node, "r") to achieve the same result.
    rootE: c4d.BaseObject = mxutils.GetRootNode(e)
    rootH: c4d.BaseObject = mxutils.GetNodeFromPath(h, "r")
    print(f"GetRootNode(e) = {rootE}")
    print(f"GetNodeFromPath(h, 'r') = {rootH}")

    # The function GetFirstSiblingNode() retrieves the first sibling of the given node. I.e., the
    # first child of the parent of the given node (or the first node in the branch when there is no 
    # parent).
    firstSiblingF: c4d.BaseObject = mxutils.GetFirstSiblingNode(f)
    firstSiblingB: c4d.BaseObject = mxutils.GetNodeFromPath(b, "f")
    print(f"GetFirstSiblingNode(f) = {firstSiblingF}")
    print(f"GetNodeFromPath(b, 'f') = {firstSiblingB}")

    # GetNodeFromPath() supports the following traversal symbols:
    #
    #   "d" - down (first child)
    #   "u" - up (parent)
    #   "n" - next (next sibling)
    #   "p" - previous (previous sibling)
    #   "f" - first sibling
    #   "r" - root
    
    # A -> B -> C -> D -> F -> D -> B
    b: c4d.BaseObject | None = mxutils.GetNodeFromPath(a, "ddnnpu")
    print(f"GetNodeFromPath(a, 'ddnnpu') = {b}")

    print("\n--- Traversing Trees --------------------------------------------------------------\n")

    # With the function IterateTree(), we can walk arbitrary GeListNode trees. We do it here only 
    # with objects, but it would also work the same with documents, tags, materials, etc.

    # Walk over all objects in the local hierarchy of A. This will ignore G and H, as they are not
    # direct descendants of A.
    print("\nmxutils.IterateTree(a)")
    for item in mxutils.IterateTree(a):
        print(f"\t{item.GetName()}")

    # Walk over all objects starting from A, including those that come 'after' A (G and H).
    print("\nmxutils.IterateTree(a, yieldSiblings=True)")
    for item in mxutils.IterateTree(a, yieldSiblings=True):
        print(f"\t{item.GetName()}")

    # IterateTree offers also some of the rewinding functionality we have seen before which makes
    # it easier to traverse a tree when starting from an arbitrary node. This exact call below will
    # always yield the full tree, no matter from where we start. The rewinding is done before the
    # traversal begins and #rewindToRoot takes precedence over #rewindToFirstSibling.
    print("\nmxutils.IterateTree(h, yieldSiblings=True, rewindToFirstSibling=True, rewindToRoot=True)")
    for item in mxutils.IterateTree(h, yieldSiblings=True, rewindToFirstSibling=True, rewindToRoot=True):
        print(f"\t{item.GetName()}")

    # Finally, IterateTree offers three traversal modes. Our tree looks like this:
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
    # The traversal modes are:
    #
    #   1. Depth-First: This is the default and will yield nodes as a human would read them, top-down
    #      and left-to-right. I.e., A, B, C, D, E, F, G, H in this case.
    #
    #   2. Inverse Depth-First: In this mode, children are yielded before their parents. This can be 
    #      useful for operations where you have to work 'from the inside out', such as deleting 
    #      elements or flattening a hierarchy. Will yield in this case: C, E, D, F, B, A, H, G.
    #
    #   3. Breadth-First: This will yield all siblings of a node before descending into their 
    #      children. You can also think of this mode as yielding in columns, (A, G) is the first 
    #      column, (B, H) is the second column, (C, D, F) is the third column, and (E) is the fourth 
    #      column. This can be useful for operations that need to process all nodes at a given depth 
    #      before moving deeper into the hierarchy. Will yield A, G, B, H, C, D, F, E in this case.

    print("\nmxutils.IterateTree(a, yieldSiblings=True, traversalMode=mxutils.TRAVERSAL_DEPTH_FIRST)")
    for item in mxutils.IterateTree(a, yieldSiblings=True, traversalMode=mxutils.TRAVERSAL_DEPTH_FIRST):
        print(f"\t{item.GetName()}")

    print("\nmxutils.IterateTree(a, yieldSiblings=True, traversalMode=mxutils.TRAVERSAL_INVERSE_DEPTH_FIRST)")
    for item in mxutils.IterateTree(a, yieldSiblings=True, traversalMode=mxutils.TRAVERSAL_INVERSE_DEPTH_FIRST):
        print(f"\t{item.GetName()}")

    print("\nmxutils.IterateTree(a, yieldSiblings=True, traversalMode=mxutils.TRAVERSAL_BREADTH_FIRST)")
    for item in mxutils.IterateTree(a, yieldSiblings=True, traversalMode=mxutils.TRAVERSAL_BREADTH_FIRST):
        print(f"\t{item.GetName()}")

    print("\n--- Traversing Graphs -------------------------------------------------------------\n")

    # Until now we have only dealt with the main hierarchical structure of the document, i.e., the
    # parent-child relationships between nodes. But Cinema also provides two other types of 
    # relationships: caches and branches.
    #
    # What are Caches?
    #
    # Caches are a special type of relationship of generator objects. When you have for example a
    # Cube object generator in a scene, it will have a static cache which is the PolygonObject
    # representation of the generator's output. There are also deform caches which store the deformed 
    # state of an object. Caches can also consist out of multiple objects and contain caches 
    # themselves (a generator that returns another generator as its cache). See 
    # modeling/geometry_cache.py for more details.
    #
    # What are Branches?
    #
    # Branches are Cinema's twist on arbitrary relationships between nodes. Each GeListNode can have
    # in addition to its hierarchical relationships arbitrary relations to other nodes. A document
    # has for example an 'Objects' branch which holds the the hierarchy of all objects, and a 
    # 'Materials' branch which holds the hierarchy of all materials. An object in turn has for 
    # example a 'Tag' branch which holds all its tags and a 'Tracks' branch which holds all its 
    # tracks. And tracks have ten curve branches, etc. In this manner, Cinema 4D realizes what is
    # commonly referred to as a "scene graph".

    a: c4d.BaseObject | None = doc.GetFirstObject()

    # When we only pass a node to IterateGraph without any additional parameters, nothing will happen
    # because all traversal options are disabled by default.
    print("\nmxutils.IterateGraph(a):")
    for node in mxutils.IterateGraph(a):
        print(f"\t{node}")

    # This call will yield all hierarchically related nodes starting from 'a'. Note that other than in
    # IterateTree(), there is no option to also consume next siblings of the starting node. If we wanted
    # to yield all objects, we would have to start from the document instead.
    print("\nmxutils.IterateGraph(a, yieldHierarchy=True):")
    for node in mxutils.IterateGraph(a, yieldHierarchy=True):
        print(f"\t{node}")

    # But we can now also do something different and also yield the caches of our objects, i.e., the
    # internal state of generator objects, in this case the `PolygonObject` instances that the 
    # generators built we added to the scene.
    print("\nmxutils.IterateGraph(a, yieldHierarchy=True, yieldCaches=True):")
    for node in mxutils.IterateGraph(a, yieldHierarchy=True, yieldCaches=True):
        print(f"\t{node}")

    # And finally, we can also include branches in our traversal. Which means that we will also see
    # tags, tracks, curves , and possibly other node types being yielded, as they are in a branching
    # relation with our objects. Note that both caches and branches are internally also hierarchical.
    # So, unless we only want to see the first node of a brach or cache, we usually want to enable
    # both hierarchical traversal and branch/cache traversal. Caches and branches are mostly independent 
    # of each other but branches can contain caches and caches can contain branches. But usually cache
    # traversal is not so important and can be left disabled.
    print("\nmxutils.IterateGraph(a, yieldHierarchy=True, yieldCaches=True, yieldBranches=True):")
    for node in mxutils.IterateGraph(a, yieldHierarchy=True, yieldCaches=True, yieldBranches=True):
        print(f"\t{node}")

    # Besides the normal node-only yield type, mxutils.IterateGraph also has a complex yield type that
    # provides more information about the yielded node.
    print("\nmxutils.IterateGraph(a, yieldBranches=True, yieldHierarchy=True, complexYield=True):")
    for node, owner, depth, isBranch, isCache in mxutils.IterateGraph(
        a, yieldBranches=True, yieldHierarchy=True, complexYield=True):
        print(f"\t{node =}, {owner =}, {depth =}, {isBranch =}, {isCache =}")

    # As discussed before, documents are also nodes, so we can also start traversal from a document.
    # That is in fact one of the most common forms of traversal.

    # We collect literally ALL nodes in the document, this can be an expensive operation for very 
    # large scenes which might run for multiple milliseconds (e.g., a 5000 node scene takes on 
    # average 20ms on my machine).  Our scene will contain only 236 nodes (at the time of writing,
    # this can change).
    nodes: list[c4d.BaseList2D] = list(mxutils.IterateGraph(
        doc, yieldHierarchy=True, yieldCaches=True, yieldBranches=True))
    print(f"The document {doc} contains {len(nodes)} nodes.")

    # To sort out all this information, IterateGraph offers multiple filtering operations. See the
    # docs for in detail information on them. One of the most important filters is the branchFilter. 
    # It determines from which brach types the function will yield nodes. By default it DOES NOT 
    # mean that it will not step into other branches, it just does not yield from them.

    # Iterate over all nodes in the document, but only yield from Obase and Tbase branches, i.e.,
    # object and tag branches.
    print("\nmxutils.IterateGraph with branchFilter=[c4d.Obase, c4d.Tbase]:")
    for node in mxutils.IterateGraph(
        doc, yieldHierarchy=True, yieldBranches=True, branchFilter=[c4d.Obase, c4d.Tbase]):
        print(f"{node = }")

    # This is complemented by the argument stopBranchingEarly. This will cause branchFilter not only
    # to act as a yield but also traversal filter. The function will now only step into branches of
    # the given type. This can be a massive performance improvement for large scenes, but we must 
    # include all necessary branch types to reach our desired nodes. As an example, if we would only 
    # pass Tbase, and use a document as the starting node, we would never see any output, as tags 
    # live in objects, and to get there, the function would have to first step into the Obase branch 
    # of a document.
    
    # This cannot reach anything, as documents do not have tag branches.
    print("\nmxutils.IterateGraph with branchFilter=[c4d.Tbase] and stopBranchingEarly=True:")
    for node in mxutils.IterateGraph(
            doc, yieldHierarchy=True, yieldBranches=True, branchFilter=[c4d.Tbase], stopBranchingEarly=True):
            print(f"{node = }")

    # Another filter type is nodeFilter which lets us filter nodes based on type. We can either use
    # specific types such as Ocube or base types such as Obase (which would fit all objects).

    # Find all cube objects and any form of tags in the scene, restricted to the the branch path
    # (Obase, Tbase).
    print("\nmxutils.IterateGraph with branchFilter=[c4d.Obase, c4d.Tbase], "
          "stopBranchingEarly=True, and nodeFilter=[c4d.Ocube, c4d.Tbase]:")
    for node in mxutils.IterateGraph(
        doc, yieldHierarchy=True, yieldBranches=True, branchFilter=[c4d.Obase, c4d.Tbase], 
        stopBranchingEarly=True, nodeFilter=[c4d.Ocube, c4d.Tbase]):
        print(f"{node = }")

    # The last filter type is maxBranchingDepth, which allows us to limit how deep the traversal goes 
    # into the branch hierarchy. Just as with stopBranchingEarly, this can help optimize traversal by
    # avoiding unnecessary exploration of deep branches.

    # We look in a document for all nodes of type tag with a maximum branching depth of 1. As in the
    # previous example, this can never yield anything, because tags sit at least two branches levels
    # below a document (Objects > Tags).
    print("\nmxutils.IterateGraph with maxBranchingDepth=1 and nodeFilter=[c4d.Tbase]:")
    for node in mxutils.IterateGraph(
        doc, yieldHierarchy=True, nodeFilter=[c4d.Tbase], maxBranchingDepth=1):
        print(f"{node = }")

    print("\n--- Manual Branch Traversal ---------------------------------------------------------")

    # NOTE: The information provided below is expert knowledge and most users can ignore it. But
    # when you want to implement a plugin which holds custom branches (via NodeData::GetBranchInfo),
    # you should understand this.

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
    for node in mxutils.IterateTree(objectHead):
        print(f"{node = }")

    print(f"\nIterating over the material branch:")
    for node in mxutils.IterateTree(materialHead):
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

    c4d.EventAdd()


if __name__ == "__main__":
    c4d.ClearPythonConsole()
    main()