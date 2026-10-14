# Example py_obj_sphere_deformer

Demonstrates how to implement a deformer object that pushes the points of a point object to a spherical shape, driven by radius and strength parameters.

## DETAILS

Implements a simple deformer that deforms a point object by pushing its points to a spherical shape.
The deformation is driven by two parameters, the radius of the sphere and the strength of the deformation.

To run this example, place the file in the Cinema 4D plugins folder and restart Cinema 4D.

Topics:
- Using ObjectData.ModifyObject() to modify an input object.
- Handle management with GetHandleCount(), GetHandle() and SetHandle() to drive parameters with handles.

## FILES

| File | Description |
| --- | --- |
| [py_obj_sphere_deformer.pyp](py_obj_sphere_deformer.pyp) | Demonstrates how to implement a deformer object that pushes the points of a point object to a spherical shape, driven by radius and strength parameters. |
| [README.md](README.md) | This file. |
| [res/c4d_symbols.h](res/c4d_symbols.h) | Global symbols and identifiers used by the plugin. |
| [res/description/opyspheredeformer.h](res/description/opyspheredeformer.h) | Description symbols for the opyspheredeformer object. |
| [res/description/opyspheredeformer.res](res/description/opyspheredeformer.res) | Description definition for the opyspheredeformer object. |
| [res/opyspheredeformer.tif](res/opyspheredeformer.tif) | Icon used by the sphere deformer object. |
| [res/strings_us/description/opyspheredeformer.str](res/strings_us/description/opyspheredeformer.str) | The English language string table by the opyspheredeformer description. |
