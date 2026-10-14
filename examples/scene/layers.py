"""Demonstrates how to assign a scene element to a layer.

Topics:
    - Accessing the layer hierarchy
    - Creating a layer
    - Assigning a scene element to a layer
"""
__author__ = "Ferdinand Hoppe"
__copyright__ = "Copyright (C) 2026 MAXON Computer GmbH"
__license__ = "Apache-2.0 License"
__version__ = "2027.0.0"
__date__ = "07/09/2026"

import c4d
import mxutils


doc: c4d.documents.BaseDocument # The active Cinema 4D document.
op: c4d.BaseObject | None # The currently selected object, can be None.


def main() -> None:
    """Runs the example.
    """
    sphere: c4d.BaseObject = mxutils.CheckType(c4d.BaseObject(c4d.Osphere))
    doc.InsertObject(sphere)

    # Get the layer head and then the first layer. If no layers exist, create one.
    root: c4d.GeListHead = doc.GetLayerObjectRoot()
    first: c4d.documents.LayerObject | None = root.GetDown()
    if not first:
        first = c4d.documents.LayerObject()
        first.SetName("New Layer")
        root.InsertLast(first)

    # Set the sphere's layer to the first layer.
    sphere.SetLayerObject(first)
    print(f"{first = }")

    # Rinse and repeat for a material and second layer.
    material: c4d.BaseMaterial = mxutils.CheckType(c4d.BaseMaterial(c4d.Mmaterial))
    doc.InsertMaterial(material)

    second: c4d.documents.LayerObject | None = first.GetNext()
    if not second:
        second = c4d.documents.LayerObject()
        second.SetName("Second Layer")
        root.InsertLast(second)

    material.SetLayerObject(second)
    print(f"{second = }")

    c4d.EventAdd()


if __name__ == "__main__":
    c4d.ClearPythonConsole()
    main()
