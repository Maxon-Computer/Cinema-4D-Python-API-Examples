# Example py_io_ies_meta

Demonstrates how to implement a scene saver plugin that exports all IES Meta information from the current document to a txt file, iterating through all objects in the scene.

## DETAILS

The scene saver walks the document and its object caches to collect IES light data, then writes the result to a text file.

To run this example, place the file in the Cinema 4D plugins folder and restart Cinema 4D.

Topics:
- Traversing object caches to find IES lights
- Writing scene metadata with a SceneSaverData plugin

## FILES

| File | Description |
| --- | --- |
| [py_io_ies_meta.pyp](py_io_ies_meta.pyp) | Demonstrates how to implement a scene saver plugin that exports all IES Meta information from the current document to a txt file, iterating through all objects in the scene. |
| [py_io_ies_meta_loader.pyp](py_io_ies_meta_loader.pyp) | Demonstrates a scene loader plugin for IES Meta data. |
| [README.md](README.md) | This file. |
| [res/c4d_symbols.h](res/c4d_symbols.h) | Global symbols and identifiers used by the plugin. |
| [res/description/fies_loader.h](res/description/fies_loader.h) | Description symbols for the fies_loader plugin. |
| [res/description/fies_loader.res](res/description/fies_loader.res) | Description definition for the fies_loader plugin. |
| [res/strings_us/c4d_strings.str](res/strings_us/c4d_strings.str) | The global English language string table used by the plugin. |
| [res/strings_us/description/fies_loader.str](res/strings_us/description/fies_loader.str) | The English language string table by the fies_loader description. |
