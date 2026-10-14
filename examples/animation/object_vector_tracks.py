"""Reads the vector components tracks of the active object's position track curve.

Topics:
    * BaseObject.GetVectorTracks()
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

    # Creates ID_BASEOBJECT_REL_POSITION DescID
    trackID = c4d.DescID(c4d.DescLevel(c4d.ID_BASEOBJECT_REL_POSITION, c4d.DTYPE_VECTOR, op.GetType()))

    # Retrieves ID_BASEOBJECT_REL_POSITION vector tracks
    ret, trackX, trackY, trackZ = op.GetVectorTracks(trackID)
    if not ret:
        raise RuntimeError("Failed to retrieve the vector tracks.")

    print("c4d.ID_BASEOBJECT_REL_POSITION tracks:")
    print("Track X: {0}".format(trackX))
    print("Track Y: {0}".format(trackY))
    print("Track Z: {0}".format(trackZ))


if __name__ == '__main__':
    main()
