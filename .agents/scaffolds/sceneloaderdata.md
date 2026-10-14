# SceneLoaderData Scaffold

Scaffolds a scene import plugin (`c4d.plugins.SceneLoaderData`) for a simple text format. Read [scaffolds.md](../scaffolds.md) first, it describes the workflow, the common questions, the placeholders and the rules that apply to all scaffolds.

Folder prefix: `py_io_`, with the suffix `_loader`: `{{Folder}}` is `py_io_{{SlugSnake}}_loader`. Registered with: `c4d.plugins.RegisterSceneLoaderPlugin` (with the *class*). The scaffold needs no resource files.

# Questions

Ask the common questions (`name`, `description`, `pluginId`) and these:

| Key | Question | Options | Default |
| --- | --- | --- | --- |
| `suffix` | What is the file extension of the format, without the dot? | Free text. | `{{Slug}}` |

`suffix` must consist of lowercase letters and digits only. `{{SUFFIX}}` is its uppercase form, it is used as the first line of the file, which makes the format recognizable.

## The format

A text file. The first line is `{{SUFFIX}}`, each following line is `<name> <x> <y> <z>` and describes a null object with a position. Names must not contain spaces.

```text
{{SUFFIX}}
Start 0 0 0
End 500 0 0
```

The matching exporter is the [SceneSaverData scaffold](scenesaverdata.md), which uses the same format. When the user wants an importer and an exporter, scaffold both with the same `suffix` and two different plugin IDs.

# Files

```text
projects/{{Folder}}/
└── {{Folder}}.pyp
```

# Templates

## {{Folder}}.pyp

```python
"""{{Description}}

Import a *.{{suffix}} file with File > Open, or File > Merge. To run this plugin, add its folder
to the plugin paths of Cinema 4D and restart Cinema 4D.

Format: The first line is "{{SUFFIX}}", each following line is "<name> <x> <y> <z>" and creates
a null object.

Topics:
    - Recognizing a file with SceneLoaderData.Identify()
    - Importing a scene with SceneLoaderData.Load()
    - Registering a scene loader plugin
"""
__author__ = "{{ModelName}}"
__version__ = "{{Version}}"

import c4d
import mxutils

PLUGIN_ID: int = {{PluginId}}

# The first line of each file of the format.
HEADER: str = "{{SUFFIX}}"


class {{ClassName}}Loader(c4d.plugins.SceneLoaderData):
    """Implements the {{Name}} importer.
    """

    def Identify(self, node: c4d.BaseList2D, name: str, probe: memoryview, size: int) -> bool:
        """Called by Cinema 4D for every file to find out if this plugin can load it.
        """
        # Never use the probe outside of this method.
        return name.lower().endswith(".{{suffix}}") and bytes(probe[:len(HEADER)]).decode(
            "ascii", errors="ignore") == HEADER

    def Load(self, node: c4d.BaseList2D, name: str, doc: c4d.documents.BaseDocument,
             filterflags: int, error: object, bt: c4d.threading.BaseThread) -> int:
        """Called by Cinema 4D to load the file into #doc.
        """
        with open(name, "r", encoding="utf-8") as file:
            lines: list[str] = file.read().splitlines()

        if not lines or lines[0].strip() != HEADER:
            return c4d.FILEERROR_UNKNOWN_VALUE

        # Each line becomes a null object at the given position.
        for line in lines[1:]:
            parts: list[str] = line.split()
            if len(parts) != 4:
                continue

            try:
                position: c4d.Vector = c4d.Vector(float(parts[1]), float(parts[2]), float(parts[3]))
            except ValueError:
                return c4d.FILEERROR_WRONG_VALUE

            null: c4d.BaseObject = mxutils.CheckType(c4d.BaseObject(c4d.Onull))
            null.SetName(parts[0])
            null.SetRelPos(position)
            doc.InsertObject(null)

        return c4d.FILEERROR_NONE


# Called by Cinema 4D when this plugin module is loaded.
if __name__ == "__main__":
    c4d.plugins.RegisterSceneLoaderPlugin(
        id=PLUGIN_ID, str="{{Name}} (*.{{suffix}})", info=0, g={{ClassName}}Loader,
        description="")
```

# After Scaffolding

- Tell the user to test the plugin with the example file above saved as `test.{{suffix}}`.
- Mention that loaders run in a context where dialogs are only allowed on the main thread when the flag `c4d.SCENEFILTER_DIALOGSALLOWED` is set in `filterflags`, see the IES Meta example.
- Mention that import options need a description resource, see the IES Meta example.

# References

- [IES Meta Loader](../../examples/plugins/py_io_ies_meta/py_io_ies_meta_loader.pyp): A loader with import options defined in a description resource.
