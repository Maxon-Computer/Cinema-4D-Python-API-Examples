# Example py_tool_sculpt_pull_brush

Demonstrates how to implement a brush tool that modifies a BaseObject by pulling all points under the brush.

## DETAILS

The brush finds points under the cursor and displaces them according to the pull interaction, illustrating the SculptBrushToolData callbacks.

To run this example, place the file in the Cinema 4D plugins folder and restart Cinema 4D.

Topics:
- Finding points under a sculpt brush
- Displacing points with a pull interaction

## FILES

| File | Description |
| --- | --- |
| [py_tool_sculpt_pull_brush.pyp](py_tool_sculpt_pull_brush.pyp) | Demonstrates how to implement a brush tool that modifies a BaseObject by pulling all points under the brush. |
| [README.md](README.md) | This file. |
| [res/c4d_symbols.h](res/c4d_symbols.h) | Global symbols and identifiers used by the plugin. |
| [res/description/pythonpullbrush.h](res/description/pythonpullbrush.h) | Description symbols for the pythonpullbrush tool. |
| [res/description/pythonpullbrush.res](res/description/pythonpullbrush.res) | Description definition for the pythonpullbrush tool. |
| [res/strings_us/c4d_strings.str](res/strings_us/c4d_strings.str) | The global English language string table used by the plugin. |
| [res/strings_us/description/pythonpullbrush.str](res/strings_us/description/pythonpullbrush.str) | The English language string table by the pythonpullbrush description. |
