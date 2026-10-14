# Example py_obj_ocio_node

Demonstrates how to implement a scene element respecting OpenColorIO color management.

## DETAILS

Since Cinema 4D 2025, OCIO has become the default color management system in Cinema 4D. This code
examples highlights how to write a scene element plugin, an object, deformer, tag, shader, etc.,
that is OCIO aware at the example of an generator object plugin. Highlighted in particular are the
color initlization behavior of NodeData.Init() and the color handling drawing methods such as
ObjectData.Draw().

Class or methods highlighted:
- c4d.plugins.NodeData.Init()
- c4d.plugins.NodeData.Message()
- c4d.plugins.ObjectData.Draw()
- c4d.BaseDraw.SetPen()

To run this example, place the file in the Cinema 4D plugins folder and restart Cinema 4D.

Topics:
- Respecting OpenColorIO scene color management
- Converting colors between scene and display spaces

## FILES

| File | Description |
| --- | --- |
| [py_obj_ocio_node.pyp](py_obj_ocio_node.pyp) | Demonstrates how to implement a scene element respecting OpenColorIO color management. |
| [README.md](README.md) | This file. |
| [res/c4d_symbols.h](res/c4d_symbols.h) | Global symbols and identifiers used by the plugin. |
| [res/description/opyocionode2025.h](res/description/opyocionode2025.h) | Description symbols for the opyocionode2025 object. |
| [res/description/opyocionode2025.res](res/description/opyocionode2025.res) | Description definition for the opyocionode2025 object. |
| [res/strings_en-US/c4d_strings.str](res/strings_en-US/c4d_strings.str) | The global English language string table used by the plugin. |
| [res/strings_en-US/description/opyocionode2025.str](res/strings_en-US/description/opyocionode2025.str) | The English language string table by the opyocionode2025 description. |
