# BitmapSaverData Scaffold

Scaffolds an image export plugin (`c4d.plugins.BitmapSaverData`) for a simple binary format. Read [scaffolds.md](../scaffolds.md) first, it describes the workflow, the common questions, the placeholders and the rules that apply to all scaffolds.

Folder prefix: `py_io_`, with the suffix `_saver`: `{{Folder}}` is `py_io_{{SlugSnake}}_saver`. Registered with: `c4d.plugins.RegisterBitmapSaverPlugin` (with an *instance*). The scaffold needs no resource files.

# Questions

Ask the common questions (`name`, `description`, `pluginId`) and these:

| Key | Question | Options | Default |
| --- | --- | --- | --- |
| `suffix` | What is the file extension of the format, without the dot? | Free text. | `{{Slug}}` |

`suffix` must consist of lowercase letters and digits only. `{{SUFFIX}}` is its uppercase form.

## The format

The format is the one of the [BitmapLoaderData scaffold](bitmaploaderdata.md): the magic bytes `{{SUFFIX}}`, the width and height as 4 byte little endian integers, then the pixels as 8 bit RGB triplets. When the user wants a loader and a saver, scaffold both with the same `suffix` and two different plugin IDs.

# Files

```text
projects/{{Folder}}/
└── {{Folder}}.pyp
```

# Templates

## {{Folder}}.pyp

```python
"""{{Description}}

Save a *.{{suffix}} image with File > Save As, in the Picture Viewer, or as a render output. To
run this plugin, add its folder to the plugin paths of Cinema 4D and restart Cinema 4D.

Format: The magic bytes "{{SUFFIX}}", the width and height as 4 byte little endian integers, then
the pixels as 8 bit RGB triplets.

Topics:
    - Writing an image with BitmapSaverData.Save()
    - Registering a bitmap saver plugin
"""
__author__ = "{{ModelName}}"
__version__ = "{{Version}}"

import c4d

PLUGIN_ID: int = {{PluginId}}

# The first bytes of each file of the format.
MAGIC: bytes = b"{{SUFFIX}}"


class {{ClassName}}Saver(c4d.plugins.BitmapSaverData):
    """Implements the {{Name}} image exporter.
    """

    def Save(self, fn: str, bm: c4d.bitmaps.BaseBitmap, data: c4d.BaseContainer,
             savebits: int) -> int:
        """Called by Cinema 4D when a bitmap is saved in this format.
        """
        width: int = bm.GetBw()
        height: int = bm.GetBh()

        content: bytearray = bytearray(MAGIC)
        content += width.to_bytes(4, "little")
        content += height.to_bytes(4, "little")
        for y in range(height):
            for x in range(width):
                content += bytes(bm.GetPixel(x, y))

        try:
            with open(fn, "wb") as file:
                file.write(content)
        except OSError:
            return c4d.IMAGERESULT_FILEERROR

        return c4d.IMAGERESULT_OK


# Called by Cinema 4D when this plugin module is loaded.
if __name__ == "__main__":
    # Bitmap savers are registered with an instance which lives for the whole session.
    c4d.plugins.RegisterBitmapSaverPlugin(
        id=PLUGIN_ID, str="{{Name}}", info=c4d.PLUGINFLAG_BITMAPSAVER_SUPPORT_8BIT |
        c4d.PLUGINFLAG_BITMAPSAVER_FORCESUFFIX, dat={{ClassName}}Saver(), suffix="{{suffix}}")
```

# After Scaffolding

- Tell the user that the format appears in the file format lists of the save dialogs and the render settings.
- Mention that the saver is 8 bit only, and that other bit depths need the matching `PLUGINFLAG_BITMAPSAVER_SUPPORT_*` flags and different pixel access.
- Mention that format options need `PLUGINFLAG_BITMAPSAVER_ALLOWOPTIONS` and an `Edit` method, see the XAMPLE Saver example.

# References

- [XAMPLE Saver](../../examples/plugins/py_io_xample_saver/py_io_xample_saver.pyp): A saver with an options dialog and compression.
