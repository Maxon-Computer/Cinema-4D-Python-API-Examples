"""Demonstrates the fundamental operations of the Take System.

Run this example in the Script Manager. It creates a cube, a material, and a small Take
hierarchy, then uses these elements to demonstrate overrides and override groups.

Topics:
    - Managing Takes
    - Creating and updating parameter overrides
    - Creating and configuring override groups

Related:
    - data/_c4d_descid.py
    - scene/_c4d_gelistnode.py
"""
__author__ = "Ferdinand Hoppe"
__copyright__ = "Copyright (C) 2026 MAXON Computer GmbH"
__license__ = "Apache-2.0 License"
__version__ = "2027.0.0"

import c4d
import mxutils
from c4d.modules import takesystem


doc: c4d.documents.BaseDocument  # The active Cinema 4D document.
op: c4d.BaseObject | None  # The currently selected object, can be None.


def main() -> None:
    """Creates a scene and demonstrates the Take System on its elements.
    """
    # Create one object and material which are used throughout the example.
    doc.Flush()
    cube: c4d.BaseObject = mxutils.CheckType(c4d.BaseObject(c4d.Ocube))
    cube.SetName("Take Cube")
    doc.InsertObject(cube)

    material: c4d.BaseMaterial = mxutils.CheckType(c4d.BaseMaterial(c4d.Mmaterial))
    material.SetName("Take Material")
    doc.InsertMaterial(material)
    textureTag: c4d.BaseTag = mxutils.CheckType(cube.MakeTag(c4d.Ttexture))
    textureTag[c4d.TEXTURETAG_MATERIAL] = material

    takeData: takesystem.TakeData = mxutils.CheckType(doc.GetTakeData())
    mainTake: takesystem.BaseTake = mxutils.CheckType(takeData.GetMainTake())

    print("\n--- Managing Takes ----------------------------------------------------------------\n")

    # Create the following take hierarchy. The Main Take is the root and will always exist and
    # cannot be deleted or modified.
    # 
    #     Main Take
    #     ├── Geometry
    #     │   └── Material
    #     └── Temporary
    #
    geometryTake: takesystem.BaseTake = mxutils.CheckType(takeData.AddTake("Geometry", mainTake, None))
    materialTake: takesystem.BaseTake = mxutils.CheckType(takeData.AddTake("Material", geometryTake, None))
    temporaryTake: takesystem.BaseTake = mxutils.CheckType(takeData.AddTake("Temporary", mainTake, None))

    # Remove the temporary Take again.
    takeData.DeleteTake(temporaryTake)

    # Takes are nodes such as objects, tags, materials, etc., and therefore can be traversed like a tree.
    for take in mxutils.IterateTree(mainTake):
        print(f"{take = }")

    # The active take can be set with SetCurrentTake().
    if not takeData.SetCurrentTake(geometryTake):
        raise RuntimeError("Failed to set the current take to Geometry Take.")
    
    print("\n--- Parameter Overrides ----------------------------------------------------------\n")

    # Takes fundamentally rely on DescID to identify the parameters they override. This is also one
    # of the cases where we have to be precise in our ID definition. See the data/_c4d_descid.py
    # example for more information.

    # Define the DescID for the x component of the cube size.
    didCubeSizeX: c4d.DescID = c4d.DescID(
        c4d.DescLevel(c4d.PRIM_CUBE_LEN, c4d.DTYPE_VECTOR, c4d.Ocube),
        c4d.DescLevel(c4d.VECTOR_X, c4d.DTYPE_REAL, 0))

    # Create an override for the x component of the cube size, this will automatically apply to
    # the active take in #takeData. Finally make the changes propagate to the scene node.
    cubeOverride: takesystem.BaseOverride = mxutils.CheckType(
        geometryTake.FindOrAddOverrideParam(takeData, cube, didCubeSizeX, 300.0))
    cubeOverride.UpdateSceneNode(takeData, didCubeSizeX)

    # The same thing, but this time for the color and brightness of the material.
    didMatColor: c4d.DescID = c4d.DescID(c4d.DescLevel(c4d.MATERIAL_COLOR_COLOR, c4d.DTYPE_COLOR, 0))
    didMatBrightness: c4d.DescID = c4d.DescID(c4d.DescLevel(c4d.MATERIAL_COLOR_BRIGHTNESS, c4d.DTYPE_REAL, 0))

    materialOverride: takesystem.BaseOverride = mxutils.CheckType(
        materialTake.FindOrAddOverrideParam(takeData, material, didMatColor, c4d.Vector(1.0, 0.0, 0.0)))
    materialOverride.UpdateSceneNode(takeData, didMatColor)

    materialOverride = mxutils.CheckType(
        materialTake.FindOrAddOverrideParam(takeData, material, didMatBrightness, 0.8))
    materialOverride.UpdateSceneNode(takeData, didMatBrightness)

    # Find the override for the material in the current take and find all overridden parameters.
    override: takesystem.BaseOverride = materialTake.FindOverride(takeData, material)
    for did in override.GetAllOverrideDescID():
        print(f"Overridden Parameter: {did}")

    print("\n--- Override Groups --------------------------------------------------------------\n")

    # An override group applies common visibility and tags to a set of scene nodes.
    group: takesystem.BaseOverrideGroup = mxutils.CheckType(geometryTake.AddOverrideGroup())
    group.SetName("Cube Group")
    group.SetEditorMode(c4d.MODE_OFF)
    group.SetRenderMode(c4d.MODE_ON)
    group.AddToGroup(takeData, cube)
    group.AddTag(takeData, c4d.Ttexture, material)

    for currentGroup in geometryTake.GetOverrideGroups():
        print(f"Override Group: {currentGroup.GetName()}")

    takeData.SetCurrentTake(mainTake)
    c4d.EventAdd()


if __name__ == "__main__":
    c4d.ClearPythonConsole()
    main()
