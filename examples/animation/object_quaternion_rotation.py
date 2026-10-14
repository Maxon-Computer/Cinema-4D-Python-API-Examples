"""Checks if the active object uses quaternion interpolation.

Topics:
    * BaseObject.IsQuaternionRotationMode()
    * BaseObject.SetQuaternionRotationMode()
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

    # Check if the object uses quaternion interpolation
    if not op.IsQuaternionRotationMode():
        # Enable quaternion interpolation
        # This will update the object's rotation animation tracks
        op.SetQuaternionRotationMode(True, False)
        c4d. EventAdd()


if __name__ == '__main__':
    main()
