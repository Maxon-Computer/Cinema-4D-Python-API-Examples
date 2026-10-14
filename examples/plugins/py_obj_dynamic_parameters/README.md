# Example py_obj_dynamic_parameters

Demonstrates how to implement a node (at the example of an object) that dynamically updates its parameters.

## DETAILS

The generator builds parameters at runtime and links one of them to the angle of the first Phong tag. It highlights how dynamic descriptions, parameter translation, and enabling work together.

To run this example, place the file in the Cinema 4D plugins folder and restart Cinema 4D.

Topics:
- Building dynamic object descriptions at runtime
- Translating and enabling generated parameters
- Linking generated parameters to existing object data

## FILES

| File | Description |
| --- | --- |
| [py_obj_dynamic_parameters.pyp](py_obj_dynamic_parameters.pyp) | Demonstrates how to implement a node (at the example of an object) that dynamically updates its parameters. |
| [README.md](README.md) | This file. |
| [res/c4d_symbols.h](res/c4d_symbols.h) | Global symbols and identifiers used by the plugin. |
| [res/description/opydynamicparametersobject.h](res/description/opydynamicparametersobject.h) | Description symbols for the opydynamicparametersobject object. |
| [res/description/opydynamicparametersobject.res](res/description/opydynamicparametersobject.res) | Description definition for the opydynamicparametersobject object. |
| [res/strings_us/description/opydynamicparametersobject.str](res/strings_us/description/opydynamicparametersobject.str) | The English language string table by the opydynamicparametersobject description. |
