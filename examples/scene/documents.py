"""Demonstrates basic document operations.

Topics:
    - Accessing or instantiating documents
    - Loading, saving, and merging documents
    - Document Modes
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
    print(f"\n--- Accessing or Instantiating Documents -----------------------------------------\n")

    # In many contexts, such as this script, you will either get a predefined module attribute #doc,
    # or a document argument to a function or method. If that is the a case, you should always use 
    # this attribute or argument.

    # Get the active document, i.e., the document that is currently in view in Cinema 4D. This is 
    # the same as the predefined module attribute #doc. Will never be None.
    activeDoc: c4d.documents.BaseDocument = c4d.documents.GetActiveDocument()
    print(f"{doc = }")
    print(f"{activeDoc = }")

    # Get the first document in the list of documents. Will never be None.
    firstDoc: c4d.documents.BaseDocument = c4d.documents.GetFirstDocument()

    # Since documents are nodes, just like any other scene elements, we can iterate over the list
    # of all opened documents with mxutils.IterateTree.
    for docNode in mxutils.IterateTree(firstDoc):
        print(f"{docNode = }")

    # Documents can also be instantiated like any other scene element. This can fail, we therefore
    # shield ourself against allocation failures by using mxutils.CheckType.
    newDoc: c4d.documents.BaseDocument = mxutils.CheckType(c4d.documents.BaseDocument())
    print(f"{newDoc = }")

    # Add the new document to the list of opened documents and make it the active document.
    c4d.documents.InsertBaseDocument(newDoc)
    c4d.documents.SetActiveDocument(newDoc)

    # Another method to get documents is from node via BaseList2D.GetDocument().

    # Add a cube to #newDoc and then get its document (which will be #newDoc).
    obj: c4d.BaseObject = mxutils.CheckType(c4d.BaseObject(c4d.Ocube))
    newDoc.InsertObject(obj)

    objDoc: c4d.documents.BaseDocument = obj.GetDocument()
    print(f"{objDoc = }")

    print(f"\n--- Loading, Saving, and Merging Documents ---------------------------------------\n")

    # Create a document with a cube, and a document with a sphere.
    docA: c4d.documents.BaseDocument = mxutils.CheckType(c4d.documents.BaseDocument())
    docA.SetDocumentName("Document A")
    cube: c4d.BaseObject = mxutils.CheckType(c4d.BaseObject(c4d.Ocube))
    docA.InsertObject(cube)

    docB: c4d.documents.BaseDocument = mxutils.CheckType(c4d.documents.BaseDocument())
    docB.SetDocumentName("Document B")
    sphere: c4d.BaseObject = mxutils.CheckType(c4d.BaseObject(c4d.Osphere))
    docB.InsertObject(sphere)

    # Insert docA and make it the active document.
    c4d.documents.InsertBaseDocument(docA)
    c4d.documents.SetActiveDocument(docA)
    print(f"{c4d.documents.GetActiveDocument() = }")

    # Save docB to the desktop.
    path: str = c4d.storage.GeGetC4DPath(c4d.C4D_PATH_DESKTOP) + "/scene.c4d"
    c4d.documents.SaveDocument(docB, path, c4d.SAVEDOCUMENTFLAGS_NONE, c4d.FORMAT_C4DEXPORT)

    # Merge the file on the desktop (docB) into the active document (docA). Our scene should now
    # contain both the cube from docA and the sphere from docB.
    c4d.documents.MergeDocument(c4d.documents.GetActiveDocument(), path, 
                                c4d.SCENEFILTER_OBJECTS | c4d.SCENEFILTER_MATERIALS)

    # And now also load the document from the desktop into a new BaseDocument. This will be just an
    # object in memory, not an inserted document. Vut before we do that we close the original
    # document, so that Cinema will not complain about having the same document open twice.
    c4d.documents.KillDocument(docB)
    loadedDoc: c4d.documents.BaseDocument | None = c4d.documents.LoadDocument(
        path, c4d.SCENEFILTER_OBJECTS | c4d.SCENEFILTER_MATERIALS)
    print(f"{loadedDoc = }")

    # Load the document from the desktop directly as the active document, adding a new document to the
    # opened documents.
    c4d.documents.LoadFile(path)

    # Close the active document again, so that the example is less confusing to follow.
    c4d.documents.KillDocument(c4d.documents.GetActiveDocument())

    print(f"\n--- Get/Set Document Name and Path -----------------------------------------------\n")

    # Print the name and path of docA (which we did not save yet, but we gave it a name)
    print(f"{docA.GetDocumentName() = }")
    print(f"{docA.GetDocumentPath() = }")

    docA.SetDocumentPath(c4d.storage.GeGetC4DPath(c4d.C4D_PATH_DESKTOP))
    print(f"{docA.GetDocumentPath() = }")

    print(f"\n--- Modes ------------------------------------------------------------------------\n")

    # Get the mode (as in model, polygons, edges, points, uv, etc.) the document is in, and 
    # translate it to a human-readable symbol.
    mode: int = docA.GetMode()
    symbol: str = mxutils.g_c4d_symbol_translation_cache.Get(mode, "^M[a-z]")
    print(f"{mode = } ({symbol = })")

    # Set the document to polygon mode.
    docA.SetMode(c4d.Mpolygons)


if __name__ == "__main__":
    c4d.ClearPythonConsole()
    main()
