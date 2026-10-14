# SceneSaverData Scaffold

Scaffolds a scene export plugin (`c4d.plugins.SceneSaverData`) for a simple text format. Read [scaffolds.md](../scaffolds.md) first, it describes the workflow, the common questions, the placeholders and the rules that apply to all scaffolds.

Folder prefix: `py_io_`, with the suffix `_saver`: `{{Folder}}` is `py_io_{{SlugSnake}}_saver`. Registered with: `c4d.plugins.RegisterSceneSaverPlugin` (with the *class*). The scaffold needs no resource files.

# Questions

Ask the common questions (`name`, `description`, `pluginId`) and these:

| Key | Question | Options | Default |
| --- | --- | --- | --- |
| `suffix` | What is the file extension of the format, without the dot? | Free text. | `{{Slug}}` |

`suffix` must consist of lowercase letters and digits only. `{{SUFFIX}}` is its uppercase form.

## The format

The format is the one of the [SceneLoaderData scaffold](sceneloaderdata.md): the first line is `{{SUFFIX}}`, each following line is `<name> <x> <y> <z>`. The exporter writes one line for each top-level object of the document, with spaces in names replaced by underscores. When the user wants an importer and an exporter, scaffold both with the same `suffix` and two different plugin IDs.

# Files

```text
projects/{{Folder}}/
└── {{Folder}}.pyp
```

# Templates

## {{Folder}}.pyp

```python
"""{{Description}}

Export a *.{{suffix}} file with File > Save As, and the format "{{Name}}". To run this plugin, add
its folder to the plugin paths of Cinema 4D and restart Cinema 4D.

Format: The first line is "{{SUFFIX}}", each following line is "<name> <x> <y> <z>" and describes
a top-level object with its position.

Topics:
    - Exporting a scene with SceneSaverData.Save()
    - Registering a scene saver plugin
"""
__author__ = "{{ModelName}}"
__version__ = "{{Version}}"

import c4d

PLUGIN_ID: int = {{PluginId}}

# The first line of each file of the format.
HEADER: str = "{{SUFFIX}}"


class {{ClassName}}Saver(c4d.plugins.SceneSaverData):
    """Implements the {{Name}} exporter.
    """

    def Save(self, node: c4d.BaseList2D, name: str, doc: c4d.documents.BaseDocument,
             filterflags: int) -> int:
        """Called by Cinema 4D when the document is saved in this format.
        """
        # Names must not contain spaces, they separate the fields of a line.
        lines: list[str] = [HEADER]
        for obj in doc.GetObjects():
            position: c4d.Vector = obj.GetRelPos()
            lines.append(f"{obj.GetName().replace(' ', '_')} {position.x} {position.y} {position.z}")

        with open(name, "w", encoding="utf-8") as file:
            file.write("\n".join(lines) + "\n")

        return c4d.FILEERROR_NONE


# Called by Cinema 4D when this plugin module is loaded.
if __name__ == "__main__":
    c4d.plugins.RegisterSceneSaverPlugin(
        id=PLUGIN_ID, str="{{Name}} (*.{{suffix}})", info=0, g={{ClassName}}Saver,
        description="", suffix="{{suffix}}")
```

# After Scaffolding

- Tell the user that the format appears in the file format list of File > Save As.
- Mention that the exporter only writes top-level objects and their relative positions, and that generators and caches need to be traversed explicitly for real exporters, see the IES Meta example and `.agents/scene.md`.
- Mention that dialogs may only be opened when `c4d.SCENEFILTER_DIALOGSALLOWED` is set in `filterflags`.

# References

- [IES Meta Saver](../../examples/plugins/py_io_ies_meta/py_io_ies_meta.pyp): An exporter that traverses objects and caches.
