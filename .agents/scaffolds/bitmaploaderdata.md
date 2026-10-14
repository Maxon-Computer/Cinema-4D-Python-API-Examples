# BitmapLoaderData Scaffold

Scaffolds an image import plugin (`c4d.plugins.BitmapLoaderData`) for a simple binary format. Read [scaffolds.md](../scaffolds.md) first, it describes the workflow, the common questions, the placeholders and the rules that apply to all scaffolds.

Folder prefix: `py_io_`, with the suffix `_loader`: `{{Folder}}` is `py_io_{{SlugSnake}}_loader`. Registered with: `c4d.plugins.RegisterBitmapLoaderPlugin` (with an *instance*). The scaffold needs no resource files.

# Questions

Ask the common questions (`name`, `description`, `pluginId`) and these:

| Key | Question | Options | Default |
| --- | --- | --- | --- |
| `suffix` | What is the file extension of the format, without the dot? | Free text. | `{{Slug}}` |

`suffix` must consist of lowercase letters and digits only. `{{SUFFIX}}` is its uppercase form, it is used as the magic bytes at the start of each file.

## The format

An uncompressed 8 bit RGB image:

| Offset | Size | Content |
| --- | --- | --- |
| 0 | `len({{SUFFIX}})` | The magic bytes, `{{SUFFIX}}` as ASCII. |
| after magic | 4 | The width, unsigned, little endian. |
| after width | 4 | The height, unsigned, little endian. |
| after height | `width * height * 3` | The pixels, row by row from the top left, three bytes (red, green, blue) each. |

The matching exporter is the [BitmapSaverData scaffold](bitmapsaverdata.md), which uses the same format. When the user wants a loader and a saver, scaffold both with the same `suffix` and two different plugin IDs.

# Files

```text
projects/{{Folder}}/
└── {{Folder}}.pyp
```

# Templates

## {{Folder}}.pyp

```python
"""{{Description}}

Load a *.{{suffix}} image with File > Open, in the Picture Viewer, or as a texture. To run this
plugin, add its folder to the plugin paths of Cinema 4D and restart Cinema 4D.

Format: The magic bytes "{{SUFFIX}}", the width and height as 4 byte little endian integers, then
the pixels as 8 bit RGB triplets.

Topics:
    - Recognizing a file with BitmapLoaderData.Identify()
    - Filling a BaseBitmap with BitmapLoaderData.Load()
    - Registering a bitmap loader plugin
"""
__author__ = "{{ModelName}}"
__version__ = "{{Version}}"

import c4d

PLUGIN_ID: int = {{PluginId}}

# The first bytes of each file of the format.
MAGIC: bytes = b"{{SUFFIX}}"


class {{ClassName}}Loader(c4d.plugins.BitmapLoaderData):
    """Implements the {{Name}} image importer.
    """

    def Identify(self, name: str, probe: memoryview, size: int) -> bool:
        """Called by Cinema 4D for every image file to find out if this plugin can load it.
        """
        return bytes(probe[:len(MAGIC)]) == MAGIC

    def Load(self, name: str, bm: c4d.bitmaps.BaseBitmap, frame: int) -> int:
        """Called by Cinema 4D to load the file into the bitmap #bm.
        """
        with open(name, "rb") as file:
            data: bytes = file.read()

        # Read the header, and make sure that the file holds all pixels it promises.
        offset: int = len(MAGIC)
        width: int = int.from_bytes(data[offset:offset + 4], "little")
        height: int = int.from_bytes(data[offset + 4:offset + 8], "little")
        offset += 8
        if width < 1 or height < 1 or len(data) < offset + width * height * 3:
            return c4d.IMAGERESULT_FILESTRUCTURE

        if bm.Init(width, height, 24) != c4d.IMAGERESULT_OK:
            return c4d.IMAGERESULT_OUTOFMEMORY

        for y in range(height):
            for x in range(width):
                bm.SetPixel(x, y, data[offset], data[offset + 1], data[offset + 2])
                offset += 3

        return c4d.IMAGERESULT_OK


# Called by Cinema 4D when this plugin module is loaded.
if __name__ == "__main__":
    # Bitmap loaders are registered with an instance which lives for the whole session.
    c4d.plugins.RegisterBitmapLoaderPlugin(
        id=PLUGIN_ID, str="{{Name}}", info=0, dat={{ClassName}}Loader())
```

# After Scaffolding

- Tell the user to test the plugin with a file written by the matching saver, or to produce a test file with a few lines of Python following the format table.
- Mention that the per-pixel loop is slow for large images, and that real formats should decode in bulk.

# References

- [XAMPLE Loader](../../examples/plugins/py_io_xample_loader/py_io_xample_loader.pyp): A loader for a compressed custom format.
