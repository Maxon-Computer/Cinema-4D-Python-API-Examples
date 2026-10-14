"""Demonstrates ray casting.

This example demonstrates how to use the GeRayCollider to perform ray casting against a polygon object.
You can run the example multiple times in a row, it will generate different rays each time.

Topics:
    - Initializing and using the GeRayCollider
    - Generating rays and checking for intersections
    - Visualizing ray intersections in the scene

Related:
    math/_c4d_matrix.py
"""
__author__ = "Ferdinand Hoppe"
__copyright__ = "Copyright (C) 2026 MAXON Computer GmbH"
__license__ = "Apache-2.0 License"
__version__ = "2027.0.0"
__date__ = "07/09/2026"

import c4d
import mxutils
import pprint


doc: c4d.documents.BaseDocument # The active Cinema 4D document.
op: c4d.BaseObject | None # The currently selected object in the Cinema 4D document, can be None.


def main() -> None:
    """Runs the example.
    """
    # --- Setup ------------------------------------------------------------------------------------

    # Flush the scene, and create a tours object at origin. Also give the tours a Phong and display
    # tag to make it more clear which faces are hit by the ray collider.
    doc.Flush()
    torus: c4d.BaseObject = mxutils.CheckType(c4d.BaseObject(c4d.Otorus))
    torus[c4d.ID_BASEOBJECT_XRAY] = True
    doc.InsertObject(torus)

    mxutils.CheckType(torus.MakeTag(c4d.Tphong))
    tag: c4d.BaseTag = mxutils.CheckType(torus.MakeTag(c4d.Tdisplay))
    tag[c4d.DISPLAYTAG_AFFECT_DISPLAYMODE] = True
    tag[c4d.DISPLAYTAG_SDISPLAYMODE] = c4d.DISPLAYTAG_SDISPLAY_GOURAUD_WIRE

    # Create a helper null object to organize the generated ray visualizations.
    root: c4d.BaseObject = mxutils.CheckType(c4d.BaseObject(c4d.Onull))
    root.SetName("rays")
    root.ChangeNBit(c4d.NBIT_OM1_FOLD, c4d.NBITCONTROL_SET)
    doc.InsertObject(root)

    # We need a polygon object to raycast against. Our torus is a generator and has no cache yet, as
    # we just inserted it into the scene. So, we have to evaluate the document state ('execute the
    # passes') to build the cache.
    if not doc.ExecutePasses(
        bt=None, animation=False, expressions=False, caches=True, flags=c4d.BUILDFLAGS_NONE):
        raise RuntimeError("Failed to execute passes on the document.")

    # Now we can get the cache of the object which is a polygon object in this case. Note that not
    # all generators necessarily directly produce a polygon object cache, and instead might also
    # return complex hierarchies of objects instead. You can then also use a modelling command 
    # such as current state to object to collapse the whole cache into a singular polygon object
    # (instead of getting the cache directly).
    cache: c4d.PolygonObject = mxutils.CheckType(torus.GetCache(), c4d.PolygonObject)

    # --- Ray Casting ------------------------------------------------------------------------------

    # Now we can initialize our ray collider and then construct a base vector for generating multiple 
    # rays. We make the base vector 50% larger than the largest dimension of the bounding box.
    caster: c4d.utils.GeRayCollider = c4d.utils.GeRayCollider()
    caster.Init(cache)

    bbox: c4d.Vector = cache.GetRad()
    base: c4d.Vector = c4d.Vector(max(bbox.x, bbox.y, bbox.z) * 1.5, 0, 0)

    # Now we construct multiple rays and directions based on the base ray.
    count: int = 5
    rays: list[tuple[c4d.Vector, c4d.Vector]] = []
    for _ in range(count):
        r1: c4d.Matrix = mxutils.g_random.RandomMatrix(
            rotationInterval=(c4d.Vector(), c4d.Vector(c4d.utils.DegToRad(360))))
        r2: c4d.Matrix = mxutils.g_random.RandomMatrix(
            rotationInterval=(c4d.Vector(), c4d.Vector(c4d.utils.DegToRad(25))))

        # Append the ray start and direction. The start is the base ray rotated by a matrix in the
        # rotation interval [0°, 360°]. The direction is the inverse of the start vector rotated 
        # by a matrix in the rotation interval [0°, 25°] (so that the example is more interesting
        # and we can also have misses).
        rays.append((r1 * base , r2 * -(r1 * base)))

    # Carry out the intersections for all the rays we generated.
    maxDistance: float = base.GetLength() * 2
    for i, (start, direction) in enumerate(rays):
        # This generates the the intersections for the i-th ray.
        caster.Intersect(start, direction, maxDistance)

        # Retrieve all intersections for the i-th ray.
        intersections: list[dict] = [
            caster.GetIntersection(j) for j in range(caster.GetIntersectionCount())]

        ExampleHelper.VisualizeRay(start, direction, maxDistance, intersections, root, 
                                   f"Ray.{i}", i / count) 

    # Print one example intersection set.
    # {
    #   'backface': True,                                    // True if backface hit
    #   'barrycoords': Vector(0.038, 0.542, 0.42),           // Barycentric coordinates of hit
    #   'distance': 1.601394977155644,                       // Distance from ray origin to hit
    #   'f_normal': Vector(356.937, 111.378, 434.929),       // Face normal (Not normalized)
    #   'face_id': 64,                                       // Face ID of hit
    #   'hitpos': Vector(92.81, 0.723, 116.76),              // Hit position in ray space
    #   's_normal': Vector(356.937, 111.378, 434.929),       // Phong normal of hit or f_normal
    #   'tri_face_id': -65                                   // If first half of quad or triangle 
    #                                                        // face_id + 1, else -(face_id + 1)
    # }
    pprint.pprint(intersections)

    c4d.EventAdd()

class ExampleHelper:
    """Provides helper function to generate ray visualizations.
    """
    @staticmethod
    def VisualizeRay(r: c4d.Vector, dir: c4d.Vector, maxDistance: float, intersections: list[dict], 
                     root: c4d.BaseObject, name: str, t: float) -> None:
        """Visualize a ray with its intersections.
        """
        # Compute the start, end, and midpoint of the ray.
        start: c4d.Vector = r
        end: c4d.Vector =  start + dir.GetNormalized() * maxDistance
        mid: c4d.Vector = (start + end) * 0.5

        # Build a frame for the ray direction. See math/_c4d_vector.py when you are lost as to what
        # is being done here.
        epsilon: float = 1e-6
        up: c4d.Vector = c4d.Vector(0, 1, 0) 
        up = up if 1. - abs(dir * c4d.Vector(0, 1, 0)) > epsilon else c4d.Vector(epsilon, 1, 0)
        fz: c4d.Vector = dir.GetNormalized()
        fx: c4d.Vector = up.Cross(fz).GetNormalized()
        fy: c4d.Vector = fz.Cross(fx).GetNormalized()

        # Build the cylinder representing the ray.
        color: c4d.Vector = c4d.utils.MixVec(c4d.Vector(1, 0, 0), c4d.Vector(0, 1, 0), t)
        cyliner: c4d.BaseObject = mxutils.CheckType(c4d.BaseObject(c4d.Ocylinder))
        cyliner[c4d.PRIM_CYLINDER_RADIUS] = 1
        cyliner[c4d.PRIM_CYLINDER_HEIGHT] = maxDistance
        cyliner[c4d.PRIM_AXIS] = c4d.PRIM_AXIS_ZP
        cyliner[c4d.ID_BASEOBJECT_COLOR] = color
        cyliner[c4d.ID_BASEOBJECT_USECOLOR] = c4d.ID_BASEOBJECT_USECOLOR_ALWAYS
        cyliner.SetMg(c4d.Matrix(off=mid, v1=fx, v2=fy, v3=fz))
        cyliner.SetName(name)
        cyliner.InsertUnderLast(root)

        # Build the cone representing the ray's endpoint.
        cone: c4d.BaseObject = mxutils.CheckType(c4d.BaseObject(c4d.Ocone))
        cone[c4d.PRIM_CONE_BRAD] = 5
        cone[c4d.PRIM_CONE_HEIGHT] = 10
        cone[c4d.PRIM_AXIS] = c4d.PRIM_AXIS_ZP
        cone[c4d.ID_BASEOBJECT_COLOR] = color * 0.5
        cone[c4d.ID_BASEOBJECT_USECOLOR] = c4d.ID_BASEOBJECT_USECOLOR_ALWAYS
        cone.InsertUnderLast(cyliner)
        cone.SetName(name + ".direction")
        cone.SetMg(c4d.Matrix(off=end, v1=fx, v2=fy, v3=fz))

        # Build spheres at the intersection points.
        for data in intersections:
            isBackFace: bool = data.get("backface", False)
            hitPos: c4d.Vector = data.get("hitpos", c4d.Vector())
            sphere: c4d.BaseObject = mxutils.CheckType(c4d.BaseObject(c4d.Osphere))
            sphere[c4d.PRIM_SPHERE_RAD] = 5
            sphere[c4d.ID_BASEOBJECT_COLOR] = color * 0.5 * (0.25 if isBackFace else 1.0)
            sphere[c4d.ID_BASEOBJECT_USECOLOR] = c4d.ID_BASEOBJECT_USECOLOR_ALWAYS
            sphere.InsertUnderLast(cyliner)
            sphere.SetName(name + ".hit" + (".in" if isBackFace else ".out"))
            sphere.SetMg(c4d.Matrix(off=hitPos, v1=fx, v2=fy, v3=fz))


if __name__ == "__main__":
    c4d.ClearPythonConsole()
    main()
