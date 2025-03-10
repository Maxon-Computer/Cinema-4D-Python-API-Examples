"""
Copyright: MAXON Computer GmbH
Author: Manuel Magalhaes

Description:
    - Copies the position, rotation and animation Tracks (so all Keyframes) from obj1 to obj2.

Notes:
    - If obj2 already have some animation data for its position, rotation, and animation these data will be lost.

Class/method highlighted:
    - BaseObject.GetCTracks()
    - CTracks.GetDescriptionID()
    - CTracks.FindCTrack()
    - C4DAtom.GetClone()
    - CTracks.InsertTrackSorted()
    - BaseDocument.AnimateObject()

"""
import c4d


def main():
    # Retrieves the object called obj1 from the active document.
    animatedBox = doc.SearchObject("obj1")
    if animatedBox is None:
        raise RuntimeError("Failed to retrieve obj1 in document.")

    # Retrieves the object called obj2 from the active document.
    fixedBox = doc.SearchObject("obj2")
    if fixedBox is None:
        raise RuntimeError("Failed to retrieve obj2 in document.")

    # Retrieves all the CTrack of obj1. CTracks contains all keyframes information of a parameter.
    tracks = animatedBox.GetCTracks()
    if not tracks:
        raise ValueError("Failed to retrieve animated tracks information for obj1.")

    # Defines a list that will contains the ID of parameters we want to copy.
    # Such ID can be found by drag-and-drop a parameter into the python console.
    trackListToCopy = [c4d.ID_BASEOBJECT_REL_POSITION, c4d.ID_BASEOBJECT_REL_ROTATION, c4d.ID_BASEOBJECT_REL_SCALE]

    # Start the Undo process.
    doc.StartUndo()

    # Iterates overs the CTracks of obj1.
    for track in tracks:
        # Retrieves the full parameter ID (DescID) describing a parameter.
        did = track.GetDescriptionID()

        # If the Parameter ID of the current CTracks is not on the trackListToCopy we go to the next one.
        if not did[0].id in trackListToCopy:
            continue

        # Find if our static object already got an animation track for this parameter ID.
        foundTrack = fixedBox.FindCTrack(did)
        if foundTrack:
            # Removes the track if found.
            doc.AddUndo(c4d.UNDOTYPE_DELETEOBJ, foundTrack)
            foundTrack.Remove()

        # Copies the initial CTrack in memory. All CCurve and CKey are kept in this CTrack.
        clone = track.GetClone()

        # Inserts the copied CTrack to the static object.
        fixedBox.InsertTrackSorted(clone)
        doc.AddUndo(c4d.UNDOTYPE_NEWOBJ, clone)

    # Ends the Undo Process.
    doc.EndUndo()

    # Updates fixedBox Geometry taking in account previously created keyframes
    animateFlag = c4d.ANIMATEFLAGS_NONE if c4d.GetC4DVersion() > 20000 else c4d.ANIMATEFLAGS_0
    doc.AnimateObject(fixedBox, doc.GetTime(), animateFlag)

    # Pushes an update event to Cinema 4D
    c4d.EventAdd()


if __name__ == "__main__":
    main()
