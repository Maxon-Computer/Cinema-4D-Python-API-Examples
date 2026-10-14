# CommandData Scaffold

Scaffolds a Cinema 4D command plugin (`c4d.plugins.CommandData`) that runs on demand from the Extensions menu, the Commander, palettes and shortcuts. Read [scaffolds.md](../scaffolds.md) first, it describes the workflow, the common questions, the placeholders and the rules that apply to all scaffolds. A command that opens a dialog is covered by the [Dialog scaffold](dialog.md).

Folder prefix: `py_cmd_`. Registered with: `c4d.plugins.RegisterCommandPlugin` (with an *instance*). The scaffold needs no resource files.

# Questions

Ask the common questions (`name`, `description`, `pluginId`) and these:

| Key | Question | Options | Default |
| --- | --- | --- | --- |
| `behavior` | What should the command do when it is executed? | `Process the selected objects`, `Create new objects`, `Run my own logic` | `Process the selected objects` |
| `needsSelection` | Should the command be greyed out when nothing is selected? | `Yes`, `No` | `Yes` when `behavior` is `Process the selected objects`, otherwise `No` |
| `undo` | Should the command be undoable? | `Yes`, `No` | `Yes` |

When the user wants an interface, redirect to the Dialog scaffold instead.

# Files

```text
projects/{{Folder}}/
└── {{Folder}}.pyp
```

# Templates

## {{Folder}}.pyp

```python
"""{{Description}}

Run the command by searching for "{{Name}}" in the Commander (Shift + C) or in the Extensions
menu. To run this plugin, add its folder to the plugin paths of Cinema 4D and restart Cinema 4D.

Topics:
    - Implementing a CommandData with CommandData.Execute()
    - Enabling and disabling a command with CommandData.GetState()
    - Registering a command plugin
"""
__author__ = "{{ModelName}}"
__version__ = "{{Version}}"

import c4d
import mxutils

PLUGIN_ID: int = {{PluginId}}

# The ID of a built-in icon, replace it with an own icon when releasing the plugin.
ICON_ID: int = 465001193


class {{ClassName}}Command(c4d.plugins.CommandData):
    """Implements the {{Name}} command.
    """

    def Execute(self, doc: c4d.documents.BaseDocument) -> bool:
        """Called by Cinema 4D when the command is executed, on the main thread.
        """
        <ExecuteBody>

    def GetState(self, doc: c4d.documents.BaseDocument) -> int:
        """Called by Cinema 4D to decide if the command is enabled.
        """
        <GetStateBody>


# Called by Cinema 4D when this plugin module is loaded.
if __name__ == "__main__":
    icon: c4d.bitmaps.BaseBitmap = c4d.bitmaps.InitResourceBitmap(ICON_ID)

    # Commands are registered with an instance which lives for the whole Cinema 4D session.
    c4d.plugins.RegisterCommandPlugin(
        id=PLUGIN_ID, str="{{Name}}", info=0, icon=icon, help="{{Description}}",
        dat={{ClassName}}Command())
```

- Import `mxutils` only when it is used.

### GetState body

When `needsSelection` is `Yes`:

```python
        # Grey out the command when no object is selected.
        if doc.GetActiveObject() is None:
            return 0

        return c4d.CMD_ENABLED
```

Otherwise:

```python
        return c4d.CMD_ENABLED
```

### Execute body: Process the selected objects

With `undo` set to `Yes`, keep the undo calls, otherwise remove them (including `StartUndo` and `EndUndo`).

```python
        objects: list[c4d.BaseObject] = doc.GetActiveObjects(c4d.GETACTIVEOBJECTFLAGS_NONE)
        if not objects:
            c4d.gui.MessageDialog("Select at least one object.")
            return True

        # Moves each selected object 100 units along its local Y axis, replace this with the
        # logic of the command. The undo step must be added BEFORE modifying an element.
        doc.StartUndo()
        for obj in objects:
            doc.AddUndo(c4d.UNDOTYPE_CHANGE, obj)
            position: c4d.Vector = obj.GetRelPos()
            position.y += 100.0
            obj.SetRelPos(position)

        doc.EndUndo()
        c4d.EventAdd()
        return True
```

### Execute body: Create new objects

```python
        # Creates a cube and selects it, replace this with the logic of the command. The undo step
        # must be added AFTER inserting an element.
        doc.StartUndo()
        cube: c4d.BaseObject = mxutils.CheckType(c4d.BaseObject(c4d.Ocube))
        cube.SetName("{{Name}}")
        doc.InsertObject(cube)
        doc.AddUndo(c4d.UNDOTYPE_NEW, cube)
        doc.SetActiveObject(cube, c4d.SELECTION_NEW)
        doc.EndUndo()

        c4d.EventAdd()
        return True
```

### Execute body: Run my own logic

```python
        # Replace this with the logic of the command.
        c4d.gui.MessageDialog("{{Name}} has been executed.")
        return True
```

# After Scaffolding

- Tell the user that the command is found in the Extensions menu and by name in the Commander (Shift + C), and how to add it to a palette or assign a shortcut with the Customize Commands manager.
- Mention that `Execute` runs on the main thread when invoked by the user, but that the main thread is not guaranteed in general. Main thread only work that is called from other callbacks must be guarded (see `.agents/scene.md`).
- Mention that the command is registered with an instance, so state kept on the instance lives for the whole session.
- Offer to add a dialog with the Dialog scaffold, or a custom menu entry with `PLUGINFLAG_HIDEPLUGINMENU` and a `PluginMessage` function. For current API details, start at <https://developers.maxon.net/docs/py> and search for `Implementing Plugins` and `PluginMessage`.

# References

- [Hello World GUI](../../examples/plugins/py_cmd_gui_hello_world/py_cmd_gui_hello_world.pyp): The smallest command that opens a dialog.
- [Tool Finalization](../../examples/plugins/py_cmd_tool_finalization/py_cmd_tool_finalization.pyp): A command that works on a snapshot of scene data with rolling changes.
- [Menu](../../examples/plugins/py_msc_menu/py_msc_menu.pyp): Placing commands in a custom menu.
