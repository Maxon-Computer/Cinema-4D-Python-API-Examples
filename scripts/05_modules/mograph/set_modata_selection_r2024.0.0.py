"""Generates and sets a MoGraph selection tag on a MoGraph cloner object.

Effectively, this will create a selection tag for all uneven clones in the cloner object. This script
has no runtime requirements, as it creates its inputs itself.

Class/method highlighted:
    - c4d.modules.mograph.GeSetMoDataSelection()

Note:

    This example has been updated as it was a bit thin-lipped in its old form, and uses now some 
    newer feature of the Python API, such as exposed symbols, type hinting, and streamlined type 
    validation. This script requires Cinema 4D R2024.0.0 or later due to that. The core functionality
    of setting a MoGraph selection is available from R18 out, just as its neighboring examples. See
    older releases of the Python SDK for an R18 version of this example.
"""
__author__ = "Maxime Adam, Ferdinand Hoppe"
__copyright__ = "Maxon Computer GmbH"
__version__ = "2024.0.0"

import c4d
import mxutils

doc: c4d.documents.BaseDocument # The active document.

def main() -> None:
    """Invoked by Cinema 4D when the script is run.
    """
    # Create a cloner object in linear mode with 10 clones, a cube object child, a MoGraph 
    # selection tag on it, and then insert it into the active document.
    count: int = 10
    cloner: c4d.BaseObject = mxutils.CheckType(c4d.BaseObject(c4d.Omgcloner))
    cloner[c4d.ID_MG_MOTIONGENERATOR_MODE] = c4d.ID_MG_MOTIONGENERATOR_MODE_LINEAR
    cloner[c4d.MG_LINEAR_COUNT] = count
    cube: c4d.BaseObject = mxutils.CheckType(c4d.BaseObject(c4d.Ocube))
    cube[c4d.PRIM_CUBE_LEN] = c4d.Vector(10)
    cube.InsertUnder(cloner)

    tag: c4d.BaseTag = mxutils.CheckType(cloner.MakeTag(c4d.Tmgselection))
    tag[c4d.MGSELECTIONTAG_NUMBERS] = True  # Enable displaying index numbers in the viewport.
    tag.SetBit(c4d.BIT_ACTIVE)  # Select the tag, so that the indices are drawn in the viewport.

    doc.InsertObject(cloner)

    # Selections in Cinema 4D are a list of states. When we want to create a selection that selects
    # all uneven elements, we have to go `False, True, False, True, ...` until we reach the last
    # element (because the first element is the element with index 0).
    states: list[bool] = [i % 2 == 1 for i in range(count)]
    print(f"{states = }")

    # Create a new selection, set our states for the clones, and finally write the selection
    # to the MoGraph selection tag.
    selection: c4d.BaseSelect = c4d.BaseSelect()
    selection.SetAll(states)
    c4d.modules.mograph.GeSetMoDataSelection(tag, selection)

    # Inform Cinema 4D that the UI should be updated.
    c4d.EventAdd()

if __name__ == '__main__':
    main()