"""Demonstrates basic operations on objects.

Topics:
    - Instantiating and inserting objects into the document
    - Setting and getting local and global transforms
    - Accessing bounding boxes
    - Modifying editor and render visibility
    - Working with object caches

Related:
    - modeling/geometry_cache.py
    - modeling/geometry_polygon_object.py
    - modeling/geometry_spline_object.py
"""
__author__ = "Ferdinand Hoppe"
__copyright__ = "Copyright (C) 2026 MAXON Computer GmbH"
__license__ = "Apache-2.0 License"
__version__ = "2027.0.0"
__date__ = "07/09/2026"

import c4d
import mxutils


doc: c4d.documents.BaseDocument # The active Cinema 4D document.
op: c4d.BaseObject | None # The currently selected object, can be None.


def main() -> None:
    """Runs the example.
    """
    print("\n--- Instantiation -------------------------------------------------------------------")

    # Create a new SDS and cube object and insert them as a hierarchy into the document.
    sds: c4d.BaseObject = mxutils.CheckType(c4d.BaseObject(c4d.Osds))
    cube: c4d.BaseObject = mxutils.CheckType(c4d.BaseObject(c4d.Ocube))
    doc.InsertObject(sds)
    cube.InsertUnderLast(sds)

    # Add another null object as a child of the cube and directly remove it again.
    null: c4d.BaseObject = mxutils.CheckType(c4d.BaseObject(c4d.Onull))
    cube.InsertUnderLast(null)
    null.Remove()

    print("\n--- Transforms ----------------------------------------------------------------------")

    # Set the local transform of the cube object (in relation to its parent).
    cube.SetMl(c4d.utils.MatrixMove(c4d.Vector(100, 0, 0)))

    # Set the global transform of the cube object (in world space). This operation is more 
    # expensive than setting the local transform and should be avoided when possible. The
    # same applies to getting the transform.
    cube.SetMg(c4d.utils.MatrixMove(c4d.Vector(200, 0, 0)))

    print(f"{cube.GetMl() = }")
    print(f"{cube.GetMg() = }")

    # There also exists a lot of other transform-related functions, but I would recommend to ignore
    # them unless you have to specifically deal with frozen transformations.

    print("\n--- Bounding Box --------------------------------------------------------------------")

    # Get the computed bounding box for the object.
    center: c4d.Vector = cube.GetMp()
    radius: c4d.Vector = cube.GetRad()

    print(f"{center = }")
    print(f"{radius = }")

    print("\n--- Editor/Render Mode --------------------------------------------------------------")

    # Get/Set the Editor/Render mode of the object. I.e., if the object is visible in the editor or render.
    print(f"{cube.GetEditorMode() = }")
    print(f"{cube.GetRenderMode() = }")

    cube.SetEditorMode(c4d.MODE_ON)
    cube.SetRenderMode(c4d.MODE_OFF)

    # The same can also be done via parameter access with the symbols
    # c4d.ID_BASEOBJECT_VISIBILITY_EDITOR and c4d.ID_BASEOBJECT_VISIBILITY_RENDER.
    cube[c4d.ID_BASEOBJECT_VISIBILITY_EDITOR] = c4d.MODE_ON
    cube[c4d.ID_BASEOBJECT_VISIBILITY_RENDER] = c4d.MODE_OFF

    print("\n--- Caches --------------------------------------------------------------------------")

    # Parametric objects such as the SDS or cube have internal caches that store their polygonal 
    # state (the same also applies for splines which have an internal line object cache). But in
    # order to access caches, the cache must exist. Which is not the case for a newly instantiated
    # object as ours.
    
    # Execute the passes on the document, so that caches are generated.
    doc.ExecutePasses(bt=None, animation=False, expression=False, caches=True)

    # Now we can access the cache of the objects. Caches must be treated as read only.
    cubeCache: c4d.BaseObject = cube.GetCache()
    sdsCache: c4d.BaseObject = sds.GetCache()
    print(f"{cubeCache = }")
    print(f"{sdsCache = }")

    # To lean more about caches, see modeling/geometry_cache.py. In the modelling section you can
    # also learn more about sub-types of BaseObject such as PolygonObject and SplineObject.
    c4d.EventAdd()


if __name__ == "__main__":
    c4d.ClearPythonConsole()
    main()
