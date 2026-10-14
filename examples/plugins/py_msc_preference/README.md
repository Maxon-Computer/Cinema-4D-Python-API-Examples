# Example py_msc_preference

Demonstrates how to implement a preference category in the Cinema 4D preference dialog, exposing
parameters as global preferences.

## DETAILS

The preference plugin exposes values globally through the world container so other parts of Cinema
4D can access them. Filename parameters are intentionally omitted because they are unsupported.

To run this example, place the file in the Cinema 4D plugins folder and restart Cinema 4D.

Topics:
- Registering a custom preference category
- Sharing preference values through the world container
- Handling unsupported filename preference parameters

## FILES

| File | Description |
| --- | --- |
| [py_msc_preference.pyp](py_msc_preference.pyp) | Demonstrates how to implement a preference category in the Cinema 4D preference dialog, exposing parameters as global preferences. |
| [README.md](README.md) | This file. |
| [res/c4d_symbols.h](res/c4d_symbols.h) | Global symbols and identifiers used by the plugin. |
| [res/description/pypreference.h](res/description/pypreference.h) | Description symbols for the pypreference plugin. |
| [res/description/pypreference.res](res/description/pypreference.res) | Description definition for the pypreference plugin. |
| [res/strings_us/description/pypreference.str](res/strings_us/description/pypreference.str) | The English language string table by the pypreference description. |
