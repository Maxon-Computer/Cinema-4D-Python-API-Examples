"""Checks the rotation tracks of the active object.

Topics:
    * BaseObject.FindBestEulerAngle()
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

    # Recalculates the existing keys to find the best angles
    op.FindBestEulerAngle(c4d.ID_BASEOBJECT_REL_ROTATION, True, False)

    # Animates the object so that it uses the new key values
    doc.AnimateObject(op, doc.GetTime(), c4d.ANIMATEFLAGS_0)

    # Pushes an update event to Cinema 4D
    c4d.EventAdd()


if __name__ == '__main__':
    main()
