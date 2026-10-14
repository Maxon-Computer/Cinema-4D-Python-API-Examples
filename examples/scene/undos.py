"""Demonstrates adding undo steps for document modifications.

Topics:
    - Undo steps for insertions
    - Undo steps for modifications
    - Undo steps for removals
"""
__author__ = "Ferdinand Hoppe"
__copyright__ = "Copyright (C) 2026 MAXON Computer GmbH"
__license__ = "Apache-2.0 License"
__version__ = "2027.0.0"
__date__ = "07/09/2026"

import c4d
import mxutils


doc: c4d.documents.BaseDocument # The active Cinema 4D document.
op: c4d.BaseObject | None # The currently selected object in the Cinema 4D document, can be None.

def main() -> None:
    """Runs the example.
    """
    # Create a new document, so that we start with a clean slate.
    doc: c4d.documents.BaseDocument = mxutils.CheckType(c4d.documents.BaseDocument())
    doc.SetDocumentName("Undo Example")
    c4d.documents.InsertBaseDocument(doc)

    # You can write code without undo steps, but your scene modifications will then not be undoable.

    # Open a new undo step for the active document. All undo actions return a bool, but it is
    # uncommon to check for that, as most undo actions cannot fail. But when you want 'perfect'
    # code you can check. Although this 'perfection' can be cumbersome to read and write.
    if not doc.StartUndo():
        raise RuntimeError("Failed to start undo step.")

    # Or a bit shorter form of check.
    # mxutils.CheckType(doc.StartUndo())

    # Add a cube object to the document and add a an undo item. Adding elements requires the AddUndo 
    # call AFTER the action.
    cube: c4d.BaseObject = mxutils.CheckType(c4d.BaseObject(c4d.Ocube))
    doc.InsertObject(cube)
    doc.AddUndo(c4d.UNDOTYPE_NEW, cube)

    # Add a material to the document and add an undo item.
    material: c4d.BaseMaterial = mxutils.CheckType(c4d.BaseMaterial(c4d.Mmaterial))
    doc.InsertMaterial(material)
    doc.AddUndo(c4d.UNDOTYPE_NEW, material)

    # Add render data to the document and add an undo item.
    renderData: c4d.documents.RenderData = mxutils.CheckType(c4d.documents.RenderData())
    doc.InsertRenderData(renderData)
    doc.AddUndo(c4d.UNDOTYPE_NEW, renderData)

    # Close the undo step.
    doc.EndUndo()

    # Now we are going to modify a few parameters and properties, which all require the undo item
    # BEFORE making any modifications, we need to start a new undo step.
    doc.StartUndo()

    # Change the transform of the cube, the AddUndo call must come before the modification.
    doc.AddUndo(c4d.UNDOTYPE_CHANGE, cube)
    cube.SetMg(c4d.utils.MatrixMove(c4d.Vector(100, 0, 0)))

    # Change the color of the material and its brightness.
    doc.AddUndo(c4d.UNDOTYPE_CHANGE, material)
    material[c4d.MATERIAL_COLOR_COLOR] = c4d.Vector(1, 0, 0)
    material[c4d.MATERIAL_COLOR_BRIGHTNESS] = 0.5

    doc.EndUndo()
    c4d.EventAdd()

    # All other undo types follow the BEFORE principle, meaning you must call AddUndo before making 
    # any changes. Here we add an undo step for removing the cube from the scene.
    doc.StartUndo()
    doc.AddUndo(c4d.UNDOTYPE_DELETE, cube)
    cube.Remove()
    doc.EndUndo()

    print("Press undo once, to see the cube being undeleted, once more to undo the translation of "
          "the cube and the red color of the material, and once more to see the cube and material "
          "addition being undone.")

if __name__ == "__main__":
    c4d.ClearPythonConsole()
    main()
