"""Retrieves all selected clones of the active Cloner object.

Topics:
    * c4d.modules.mograph.GeGetMoDataSelection()
"""
__author__ = "Ferdinand Hoppe"
__copyright__ = "Copyright (C) 2026 MAXON Computer GmbH"
__license__ = "Apache-2.0 License"
__version__ = "R18"

import c4d


def main():
    # Checks if there is an active object
    if op is None:
        raise ValueError("op is none, please select one object.")

    # Checks if the active object is a MoGraph Cloner Object
    if not op.IsInstanceOf(1018544):
        raise TypeError("Selected object is not a Mograph Cloner Object.")

    # Retrieves MoGraph Selection Tag from the cloner
    tag = op.GetTag(c4d.Tmgselection)
    if tag is None:
        raise RuntimeError("Failed to retrieve a MoGraph Selection Tag on the selected object.")

    # Retrieves the clones selection
    selection = c4d.modules.mograph.GeGetMoDataSelection(tag)

    # Retrieves selection list
    count = op[c4d.MG_LINEAR_COUNT]

    # Retrieves selected clones indices
    indices = []
    for index in range(count):
        if selection.IsSelected(index):
            indices.append(index)

    print("Clones selection indices:", indices)


if __name__ == '__main__':
    main()
