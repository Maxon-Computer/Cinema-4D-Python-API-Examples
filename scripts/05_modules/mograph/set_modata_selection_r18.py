"""
Copyright: MAXON Computer GmbH

Description:
    - Selects all clones of the active Cloner object.

Class/method highlighted:
    - c4d.modules.mograph.GeSetMoDataSelection()

"""
import c4d


def main():
    # Checks if there is an active object
    if op is None:
        raise ValueError("op is None, please select one object.")

    # Checks if the active object is a MoGraph Cloner Object
    if not op.CheckType(1018544):
        raise TypeError("Selected object is not a Mograph Cloner Object.")

    # Builds list for clones selection states
    states = [1] * op[c4d.MG_LINEAR_COUNT]

    # Create MoGraph Selection Tag on the cloner to store the selection
    tag = op.MakeTag(c4d.Tmgselection)
    if tag is None:
        raise RuntimeError("Failed to create a MoGraph Selection Tag on the selected object.")
        
    # Creates new BaseSelect and sets it to states list
    selection = c4d.BaseSelect()
    selection.SetAll(states)

    # Sets clones selection states
    c4d.modules.mograph.GeSetMoDataSelection(op, selection)

    # Pushes an update event to Cinema 4D
    c4d.EventAdd()


if __name__ == '__main__':
    main()
