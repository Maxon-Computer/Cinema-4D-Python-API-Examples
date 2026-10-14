"""Retrieves the current workplane position and object. Locks this workplane so it can't be edited.

Topics:
    * c4d.modules.snap
    * c4d.modules.snap.GetWorkplaneObject()
    * c4d.modules.snap.GetWorkplaneMatrix()
    * c4d.modules.snap.IsWorkplaneLock()
    * c4d.modules.snap.SetWorkplaneLock()
"""
__author__ = "Ferdinand Hoppe"
__copyright__ = "Copyright (C) 2026 MAXON Computer GmbH"
__license__ = "Apache-2.0 License"
__version__ = "R14"

import c4d


def main():
    # Prints workplane object and matrix
    print("Workplane Object:", c4d.modules.snap.GetWorkplaneObject(doc))
    print("Workplane Matrix:", c4d.modules.snap.GetWorkplaneMatrix(doc, None))

    # Checks if workplane is locked
    if not c4d.modules.snap.IsWorkplaneLock(doc):
        # Locks workplane
        c4d.modules.snap.SetWorkplaneLock(doc.GetActiveBaseDraw(), True)
        print("Workplane Locked:", c4d.modules.snap.IsWorkplaneLock(doc))


if __name__ == '__main__':
    main()
