"""Synchronizes the keys for the tracks of the active cube's "Size" parameter.

Topics:
    * BaseObject.SynchronizeVectorTrackKeys()

Note:
- If a track has a key at a certain time, keys for the other synchronized tracks will be created.
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

    # Synchronizes keys
    op.SynchronizeVectorTrackKeys(c4d.PRIM_CUBE_LEN, False)

    # Pushes an update event to Cinema 4D
    c4d.EventAdd()


if __name__ == '__main__':
    main()
