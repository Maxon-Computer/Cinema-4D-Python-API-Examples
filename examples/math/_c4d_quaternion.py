"""Demonstrates working with quaternions.

Quaternions are used to represent rotations in 3D space. They can be especially helpful when 
interpolating between different orientations smoothly. As opposed to Euler angles, quaternions avoid 
gimbal lock and provide smooth rotational transitions.

Topics:
    - Linear and spherical interpolation of quaternions
    - Arithmetic operations with quaternions

Related:
    math/_c4d_matrix.py
"""
__author__ = "Ferdinand Hoppe"
__copyright__ = "Copyright (C) 2026 MAXON Computer GmbH"
__license__ = "Apache-2.0 License"
__version__ = "2027.0.0"
__date__ = "07/09/2026"

import c4d
import math
import mxutils


doc: c4d.documents.BaseDocument # The active Cinema 4D document.
op: c4d.BaseObject | None # The currently selected object in the Cinema 4D document, can be None.


def main() -> None:
    """Runs the example.
    """
    doc.Flush()

    # --- Setup ------------------------------------------------------------------------------------

    # Create two example setups of two null objects at a different orientation between we which
    # we will interpolate linearly and spherically.
    red: c4d.Vector = c4d.Vector(1, 0, 0)
    green: c4d.Vector = c4d.Vector(0, 1, 0)
    rootA: c4d.BaseObject = ExampleHelper.CreateAB("Lerp", 100, red, green, c4d.Vector(200, 0, 0))
    rootB: c4d.BaseObject = ExampleHelper.CreateAB("Slerp", 100, red, green, c4d.Vector(0, 0, 0))

    # The two nulls for linear interpolation are under rootA.
    a: c4d.BaseObject = mxutils.GetNodeFromPath(rootA, "d")
    b: c4d.BaseObject = mxutils.GetNodeFromPath(rootA, "dn")

    # The two nulls for spherical interpolation are under rootB.
    c: c4d.BaseObject = mxutils.GetNodeFromPath(rootB, "d")
    d: c4d.BaseObject = mxutils.GetNodeFromPath(rootB, "dn")

    # Number of step to interpolate between the quaternions and the size of the inserted step nulls.
    count: int = 10
    size: float = 50

    # --- Linear Interpolation ---------------------------------------------------------------------

    # Instantiate two quaternions and initialize them with the global matrices of objects A and B.
    # They now represent the orientations of objects A and B as quaternions.
    qa: c4d.Quaternion = c4d.Quaternion()
    qb: c4d.Quaternion = c4d.Quaternion()
    qa.SetMatrix(a.GetMg())
    qb.SetMatrix(b.GetMg())

    # Take #count steps between the two quaternions and linearly interpolate between them. Because
    # the rotation happens on an arc (a sphere), linear interpolation will not produce evenly spaced 
    # orientations. Samples will clump up towards the start and end of the interpolation.
    for i in range(1, count + 1):
        t: float = i / (count + 1)

        # Linearly interpolate between the two quaternions and the colors and create a null for the
        # orientation and color. QBlend is the function to linearly interpolate between two quaternions.
        q: c4d.Quaternion = c4d.utils.QBlend(qa, qb, t)
        color: c4d.Vector = c4d.utils.MixVec(red, green, t)
        ExampleHelper.CreateNull(f"A->B Lerp @ {t*100:.0f}%", size, q.GetMatrix(), color, b)

    # --- Spherically Linear Interpolation ---------------------------------------------------------

    # Do the same again, but for the second setup and use spherical interpolation. This will give
    # us even spacing between the orientations.
    qa: c4d.Quaternion = c4d.Quaternion()
    qb: c4d.Quaternion = c4d.Quaternion()
    qa.SetMatrix(c.GetMg())
    qb.SetMatrix(d.GetMg())

    for i in range(1, count + 1):
        t: float = i / (count + 1)

        # QSlerp is the function to spherically interpolate between two quaternions.
        q: c4d.Quaternion = c4d.utils.QSlerp(qa, qb, t)
        color: c4d.Vector = c4d.utils.MixVec(red, green, t)
        ExampleHelper.CreateNull(f"A->B Slerp @ {t*100:.0f}%", size, q.GetMatrix(), color, d)

    # There exist also other, more complex interpolation functions such as QSquad, QSmoothCubic,
    # and QSpline.

    print("--- Arithmetic Operations -----------------------------------------------------------\n")

    # There exist also arithmetic operations for quaternions, but they are implemented as functions,
    # not as operators. You will also only rarely need them.

    print(f"{qa = }")
    print(f"{qb = }")

    # Add, subtract, and multiply two quaternions.
    print(f"\n{c4d.utils.QAdd(qa, qb) = }")
    print(f"{c4d.utils.QSub(qa, qb) = }")
    print(f"{c4d.utils.QMul(qa, qb) = }")

    # Norm, invert, dot, and derivative.
    print(f"\n{c4d.utils.QNorm(qa) = }")
    print(f"{c4d.utils.QInvert(qa) = }")
    print(f"{c4d.utils.QDot(qa, qb) = }")

    c4d.EventAdd()

class ExampleHelper:
    """Provides helper functions to setup the null object for the example.

    This is just boilerplate code and you can ignore it.
    """
    @staticmethod
    def CreateAB(name: str, size: float,colorA: c4d.Vector, colorB: c4d.Vector, 
                             offset: c4d.Vector) -> c4d.BaseObject:
        """Creates the interpolation setup with two null objects under a parent null.
        """
        root: c4d.BaseObject = mxutils.CheckType(c4d.BaseObject(c4d.Onull))
        root.SetName(name)
        root.SetMg(c4d.utils.MatrixMove(offset))

        a: c4d.BaseObject = mxutils.CheckType(c4d.BaseObject(c4d.Onull))
        a.SetName("A")
        a[c4d.NULLOBJECT_DISPLAY] = c4d.NULLOBJECT_DISPLAY_AXIS
        a[c4d.NULLOBJECT_RADIUS] = size
        a[c4d.ID_BASEOBJECT_USECOLOR] = c4d.ID_BASEOBJECT_USECOLOR_ALWAYS
        a[c4d.ID_BASEOBJECT_COLOR] = colorA

        b: c4d.BaseObject = mxutils.CheckType(c4d.BaseObject(c4d.Onull))
        b.SetName("B")
        b[c4d.NULLOBJECT_DISPLAY] = c4d.NULLOBJECT_DISPLAY_AXIS
        b[c4d.NULLOBJECT_RADIUS] = size
        b[c4d.ID_BASEOBJECT_USECOLOR] = c4d.ID_BASEOBJECT_USECOLOR_ALWAYS
        b[c4d.ID_BASEOBJECT_COLOR] = colorB

        # Set the orientations of the null objects.
        a.SetMg(c4d.utils.MatrixRotX(math.pi / 4) * 
                c4d.utils.MatrixRotY(math.pi / 4))
        b.SetMg(c4d.utils.MatrixRotX(2 * math.pi / 3) * 
                c4d.utils.MatrixRotY(2 * math.pi / 3))

        a.InsertUnderLast(root)
        b.InsertUnderLast(root)

        text: c4d.BaseObject = mxutils.CheckType(c4d.BaseObject(c4d.Omgtext))
        text[c4d.PRIM_TEXT_TEXT] = name
        text[c4d.PRIM_TEXT_HEIGHT] = 30
        text[c4d.MGTEXTOBJECT_SPLINEMOVE] = 1
        text.InsertUnderLast(root)

        text.SetMl(c4d.Matrix(off=c4d.Vector(-30, -100, 0)))

        doc.InsertObject(root)

        return root

    @staticmethod
    def CreateNull(name: str, size: float, mg: c4d.Matrix, color: c4d.Vector, 
                   predecessor: c4d.BaseObject) -> None:
        """Creates a null object with the specified parameters, used for
        the inserted interpolation steps.
        """
        null: c4d.BaseObject = mxutils.CheckType(c4d.BaseObject(c4d.Onull))
        null.SetName(name)
        null.SetMg(mg)
        null[c4d.NULLOBJECT_DISPLAY] = c4d.NULLOBJECT_DISPLAY_AXIS
        null[c4d.NULLOBJECT_RADIUS] = size
        null[c4d.ID_BASEOBJECT_USECOLOR] = c4d.ID_BASEOBJECT_USECOLOR_ALWAYS
        null[c4d.ID_BASEOBJECT_COLOR] = color
        null.InsertBefore(predecessor)

if __name__ == "__main__":
    c4d.ClearPythonConsole()
    main()
