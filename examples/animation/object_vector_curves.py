"""Reads the vector components curves of the active object's rotation track curve.

Topics:
    * BaseObject.FindBestEulerAngle()
    * BaseObject.GetVectorCurves()
"""
__author__ = "Yannick Puech"
__copyright__ = "Copyright (C) 2026 MAXON Computer GmbH"
__license__ = "Apache-2.0 License"
__version__ = "R18"

import c4d


def main():
    # Checks if selected object is valid
    if op is None:
        raise ValueError("op is none, please select one object.")

    # Searches object's rotation track
    trackID = c4d.DescID(c4d.DescLevel(c4d.ID_BASEOBJECT_REL_ROTATION, c4d.DTYPE_VECTOR, op.GetType()))
    track = op.FindCTrack(trackID)
    if track is None:
        raise RuntimeError("Failed to retrieve the track, Object may not have track.")

    # Gets the curve for the track
    curve = track.GetCurve()
    if curve is None:
        raise RuntimeError("Failed to retrieve the curves, Object may not have curves.")

    # Gets the X,Y,Z curves from a Vector curve
    ret, curveX, curveY, curveZ = op.GetVectorCurves(curve)
    if not ret:
        raise RuntimeError("Failed to retrieve the vector curve.")

    print("c4d.ID_BASEOBJECT_REL_ROTATION curves:")
    print("Curve H: {0}".format(curveX))
    print("Curve P: {0}".format(curveY))
    print("Curve B: {0}".format(curveZ))


if __name__ == '__main__':
    main()
