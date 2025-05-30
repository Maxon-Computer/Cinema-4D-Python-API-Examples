#coding: utf-8
"""Explains the geometry model of the Cinema API in Cinema 4D.

The script either evaluates the caches of the currently selected object or when there is no
object selection, or inserts the following object hierarchy into the active document and evaluates 
the cache of "Array Object".

    Array Object
    +- Cylinder Object
        +- Bend Object

Topics:
    * The geometry model of the Cinema API
    * The purpose and structure of generator and deform caches
    * c4d.BaseObject
    * c4d.PointObject
    * c4d.PolygonObject
    * c4d.SplineObject
    * c4d.LineObject

Examples:
    * GetCaches(): Demonstrates retrieving and building caches for BaseObject instances.
    * PrintCacheTree(): Prints out the cache-tree of the passed object.

Overview:
    All geometry in the Cinema 4D Cinema API is represented as `BaseObject` instances. `BaseObject` 
    instances can also express non-geometry entities as light objects or cameras, but they are being 
    ignored in this context. There are two fundamental types of geometry representations in the 
    Cinema API:

        * Generator objects
        * Non-generator objects

    Generator objects are objects which generate some form of geometry over their parameters exposed
    in the Attribute Manager of Cinema 4D. Generators objects can generate both polygon and curve 
    geometry.An example would be the Cube generator object which has parameters for its size, 
    segments and fillets. Changing the parameters of the Cube generator object will then regenerate
    its underlying cache which represents the generator in the viewport and renderings. Generator 
    objects do not allow users to modify their underlying cache manually which also applies to 
    programmatic access.

    There are two types of geometry caches in the Cinema API. Caches for internal representations 
    of generator objects, they are plainly referred to as *caches*, and *deform caches*; which can
    only be found on non-generator objects. The latter represents the state of a generator, as 
    expressed by its parameters, as a (more) discrete form. In most simple cases this means
    that the cache is a `LineObject` or `PolygonObject`, but generator caches can also be more
    complex and can contain caches themselves when a generator returns a generator as its cache
    output. Deform caches represent the state of an object when it is being affected by a deformer
    as for example the bend object. Deform caches are only attached to `LineObject` or 
    `PolygonObject` instances, and are often buried deep inside the cache of generators.
"""
__author__ = "Ferdinand Hoppe"
__copyright__ = "Copyright (C) 2022 MAXON Computer GmbH"
__date__ = "08/04/2022"
__license__ = "Apache-2.0 License"
__version__ = "S26"

import c4d
import typing

doc: c4d.documents.BaseDocument  # The currently active document.
op: typing.Optional[c4d.BaseObject]  # The selected object within that active document. Can be None.


def PrintCacheTree(obj: c4d.BaseObject, indent: int = 0, prefix: str = "") -> None:
    """Prints out the cache-tree of the passed object.

    Since this script can also be used to evaluate the caches of existing objects, it is encouraged
    to try out the script with different objects selected in different scenes, to understand how
    their caches look like.

    Args:
        obj: The starting object to print the cache tree for.
        indent: The indentation level to start printing with. Defaults to 0.
        prefix: A prefix for the object label. Defaults to the empty string.

    Example:
        The following simple object hierarchy.

            Array (Array generator object with two clones)
                Cylinder (Cylinder generator object)
                    Bend (Bend deformer object)

        Will be printed as the following cache hierarchy for #Array as the input object.

            Array(Array)                                                                         [1]
                [cache] Array(Null)                                                              [4]
                    [child] Cylinder.2(Cylinder)                                                 [5]
                        [cache] Cylinder.2(Polygon)                                              [6]
                            [deform cache] Cylinder.2(Polygon)                                   [7]
                        [child] Bend(Bend)                                                       [8]
                    [child] Cylinder.1(Cylinder)                                                 [9]
                        [cache] Cylinder.1(Polygon)                                                 
                            [deform cache] Cylinder.1(Polygon)                                      
                        [child] Bend(Bend)                                                          
                [child] Cylinder(Cylinder)                                                       [2]
                    [child] Bend(Bend)                                                           [3]

            [1] The actual Array generator object as seen in the Object Manger.
            [2] The actual Cylinder generator object as seen in the Object Manger. Its caches are
                muted because it is an input object for [1].
            [3] The actual Bend deformer object as seen in the Object Manger.
            [4] The cache of the Array generator object is a Null object.
            [5] This Null object has a child which is the second Cylinder generator object clone of 
                the Array generator object.
            [6] This second Cylinder generator object has a cache itself because it is a generator 
                itself. The cache is here directly a polygon object. 
            [7] The deform cache of this polygon object. It will contain [6] as deformed by [8].
            [8] The bend deformer object deforming [6] as part of the cache of the Array generator
                object.
            [9] The first clone of the Array generator object, repeating the structure [5]-[8].

    Note:
        Caches can also be explored with the Active Object Plugin in the Cinema 4D C++ SDK.
    """
    if not isinstance(obj, c4d.BaseObject):
        return

    # Print the current node.
    tab = "\t" * indent
    print(f"{tab}{prefix} {obj.GetName()}({obj.GetTypeName()})")

    # Get the caches of the node and recurse for each of them.
    for prefix, cache in (("[cache]", obj.GetCache()),
                          ("[deform cache]", obj.GetDeformCache())):
        if cache:
            PrintCacheTree(cache, indent + 1, prefix)

    # Traverse the children of the node.
    for child in obj.GetChildren():
        PrintCacheTree(child, indent + 1, "[child]")


def GetCaches(node: c4d.BaseObject) -> None:
    """Demonstrates retrieving and building caches for BaseObject instances.

    Args:
        node: A node with pre-built caches for the example.
    """
    # --- Retrieving caches ------------------------------------------------------------------------

    print("Retrieving Caches:\n")

    # All BaseObject instances CAN carry two types of caches: A non-deformed cache and a deformed
    # cache. There is no guarantee that any of these caches is populated at any time.

    # The non-deformed cache of the node. This will only be populated for generator objects.
    cache = node.GetCache()

    # The deformed cache of the same node. Deformation refers here to modifiers such as the Bend
    # object. Deformed caches can only exist on non-generator objects. But since generator objects
    # will contain non-generator objects in their caches, deform caches are often contained within
    # the caches of generator objects.
    deformedCache = node.GetDeformCache()

    # When it is unclear if a passed node is a generator or not, the cache can also be determined in
    # this "fall-through" fashion.
    cache = node.GetDeformCache() or node.GetCache()

    # The return value of a cache function will always be a single node or None. Since #node will
    # be in this example a generator, GetCache() will return a cache, while GetDeformCache() will
    # return None (at least when the script is run with the example rig).
    print(f"{node.GetName()}.GetCache() = {node.GetCache()}")
    print(f"{node.GetName()}.GetDeformCache() = {node.GetDeformCache()}")

    # Prints the cache of #node as tree into the console. Depending on what #node is, its cache
    # can be a very complex hierarchical structure when fully resolved.
    print(f"\nCache Tree of '{node.GetName()}':\n")
    PrintCacheTree(node)

    # --- Building caches --------------------------------------------------------------------------

    print("\nBuilding Caches:\n")

    # A newly allocated generator object does not have any cashes.
    cube = c4d.BaseObject(c4d.Ocube)
    print(f"Cache for newly allocated object: {cube.GetCache()}")

    # To build the caches for a generator, it must be inserted into a document on which then the
    # cache pass must be executed. This can either be a 'real' document as the active document or a
    # dummy document as shown here.
    tempDoc = c4d.documents.BaseDocument()
    tempDoc.InsertObject(cube)

    # Passes can evaluate more than just caches, as for example expressions, i.e., tags, and 
    # animations. In complex cases it might be necessary to also evaluate expressions and 
    # animations as both can have an impact on the (deformed) geometry of an object. In complex 
    # cases where multiple objects do interact, it might also be necessary to execute the passes
    # multiple times. But in this case evaluating the cache pass once alone will be enough.
    if not tempDoc.ExecutePasses(
            bt=None, animation=False, expressions=False, caches=True, flags=c4d.BUILDFLAGS_NONE):
        raise RuntimeError(f"Could not evaluate caches for {tempDoc}.")

    # Although evaluated by documents, caches are not bound to them. A BaseObject will keep its
    # caches even after it has been removed from a document.
    cube.Remove()
    print(f"Cache after executing the cache pass: {cube.GetCache()}")


def BuildSetup(doc: c4d.documents.BaseDocument) -> c4d.BaseObject:
    """Builds the inputs for the examples.
    """
    def AssertType(item: any, t: typing.Type) -> any:
        """Asserts that #item is of type #t.
        """
        if not isinstance(item, t):
            raise MemoryError(f"Could not allocate {t}.")
        return item

    # Create the setup.
    array = AssertType(c4d.BaseObject(c4d.Oarray), c4d.BaseObject)
    cylinder = AssertType(c4d.BaseObject(c4d.Ocylinder), c4d.BaseObject)
    bend = AssertType(c4d.BaseObject(c4d.Obend), c4d.BaseObject)
    tag = AssertType(cylinder.MakeTag(c4d.Tphong), c4d.BaseTag)

    array[c4d.ARRAYOBJECT_COPIES] = 1
    array.SetMg(c4d.utils.MatrixMove(c4d.Vector(-500, 0, 0)))
    cylinder[c4d.PRIM_CYLINDER_HSUB] = 24
    tag[c4d.PHONGTAG_PHONG_ANGLELIMIT] = True
    bend[c4d.BENDOBJECT_STRENGTH] = c4d.utils.DegToRad(90.0)

    bend.InsertUnder(cylinder)
    cylinder.InsertUnder(array)

    # Build the caches for the setup.
    doc.InsertObject(array)
    if not doc.ExecutePasses(None, False, False, True, c4d.BUILDFLAGS_NONE):
        raise RuntimeError("Could not build caches for example rig.")

    return array


def main(doc: c4d.documents.BaseDocument, op: typing.Optional[c4d.BaseObject]) -> None:
    """Runs the example.

    Args:
        doc: The active document.
        op: The selected object in #doc. Can be #None.
    """
    # When there is no selected object, insert an example geometry into #doc instead.
    node = op if isinstance(op, c4d.BaseObject) else BuildSetup(doc)

    # Run the example evaluating the caches of #node.
    GetCaches(node)

    # Inform Cinema 4D that the document has been modified (this is required for the case when
    # the execution did insert the example geometry).
    c4d.EventAdd()


if __name__ == '__main__':
    c4d.CallCommand(13957)  # Clear the console.
    # #doc and #op are predefined module attributes as defined at the top of the file.
    main(doc, op)
