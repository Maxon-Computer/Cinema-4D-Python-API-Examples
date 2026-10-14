"""Demonstrates creating and configuring LOD objects.

Topics:
    * c4d.LodObject
    * LodObject.GetLevelCount()
    * LodObject.GetCurrentLevel()
    * LodObject.GetDisplayBFCDescID()
    * LodObject.GetManualModeObjectListDescID()
    * LodObject.GetSimplifyModeDescID()
"""
__author__ = "Yannick Puech"
__copyright__ = "Copyright (C) 2026 MAXON Computer GmbH"
__license__ = "Apache-2.0 License"
__version__ = "R19"

import c4d


def CreateLodObject(doc: c4d.documents.BaseDocument) -> None:
    """Creates a new LOD object and adds it to a document."""
    lodObject = c4d.LodObject()
    lodObject.SetName("New LOD Object")
    doc.InsertObject(lodObject)
    c4d.EventAdd()


def SetCurrentLevelToMaximum(op: c4d.BaseObject) -> None:
    """Sets the current level to the maximum level in User LOD Level mode."""
    if op is None:
        raise RuntimeError("Failed to retrieve the active object.")
    if not op.IsInstanceOf(c4d.Olod):
        raise TypeError("op is not a Lod Object.")

    if op[c4d.LOD_CRITERIA] == c4d.LOD_CRITERIA_MANUAL:
        op[c4d.LOD_CURRENT_LEVEL] = op.GetLevelCount() - 1
        c4d.EventAdd()


def HideCurrentLevel(op: c4d.BaseObject) -> None:
    """Hides the objects of the active LOD object's current level."""
    if op is None:
        raise RuntimeError("Failed to retrieve the active object.")
    if not op.IsInstanceOf(c4d.Olod):
        raise TypeError("op is not a Lod Object.")

    showControlID = op.GetShowControlDescID(op.GetCurrentLevel())
    if showControlID is not None:
        op[showControlID] = False
        c4d.EventAdd()


def ConfigureDisplay(op: c4d.BaseObject) -> None:
    """Configures the display settings for each level of an LOD object."""
    if op is None:
        raise RuntimeError("Failed to retrieve the active object.")
    if not op.IsInstanceOf(c4d.Olod):
        raise TypeError("op is not a Lod Object.")

    for level in range(op.GetLevelCount()):
        descID = op.GetDisplayBFCDescID(level)
        if descID is not None:
            op[descID] = True

        descID = op.GetDisplayStModeDescID(level)
        if descID is not None:
            op[descID] = c4d.DISPLAYTAG_WDISPLAY_WIREFRAME

        descID = op.GetDisplayShModeDescID(level)
        if descID is not None:
            op[descID] = c4d.DISPLAYTAG_SDISPLAY_NOSHADING

    c4d.EventAdd()


def ConfigureManualGroups(doc: c4d.documents.BaseDocument) -> None:
    """Configures the selected objects as manual LOD groups."""
    activeObjects = doc.GetActiveObjects(c4d.GETACTIVEOBJECTFLAGS_0)
    if not activeObjects:
        raise RuntimeError("Failed to retrieve selected objects.")

    lodObject = doc.GetTargetObject()
    if lodObject is None or not lodObject.IsInstanceOf(c4d.Olod):
        raise TypeError("The last selected object is not a Lod Object.")

    lodObject[c4d.LOD_MODE] = c4d.LOD_MODE_MANUAL_GROUPS
    lodObject[c4d.LOD_CRITERIA] = c4d.LOD_CRITERIA_MANUAL
    lodObject[c4d.LOD_LEVEL_COUNT_DYN] = len(activeObjects) - 1

    level = 0
    for obj in activeObjects:
        if obj == lodObject:
            continue

        obj.Remove()
        doc.InsertObject(obj, lodObject)

        listID = lodObject.GetManualModeObjectListDescID(level)
        if listID is None:
            continue

        inExData = c4d.InExcludeData()
        inExData.InsertObject(obj, 1)
        lodObject[listID] = inExData
        level += 1

    c4d.EventAdd()


def ConfigureSimplify(op: c4d.BaseObject) -> None:
    """Configures two levels in Simplify mode."""
    if op is None:
        raise RuntimeError("Failed to retrieve the active object.")
    if not op.IsInstanceOf(c4d.Olod):
        raise TypeError("op is not a Lod Object.")

    op[c4d.LOD_MODE] = c4d.LOD_MODE_SIMPLIFY
    op[c4d.LOD_CRITERIA] = c4d.LOD_CRITERIA_MANUAL
    op[c4d.LOD_LEVEL_COUNT_DYN] = 2
    op[c4d.LOD_CURRENT_LEVEL] = 0

    descID = op.GetSimplifyModeDescID(0)
    if descID is not None:
        op[descID] = c4d.LOD_SIMPLIFY_CONVEXHULL
        descID = op.GetPerObjectControlDescID(0)
        if descID is not None:
            op[descID] = True

    descID = op.GetSimplifyModeDescID(1)
    if descID is not None:
        op[descID] = c4d.LOD_SIMPLIFY_NULL
        descID = op.GetNullDisplayDescID(1)
        if descID is not None:
            op[descID] = c4d.NULLOBJECT_DISPLAY_CIRCLE

    c4d.EventAdd()