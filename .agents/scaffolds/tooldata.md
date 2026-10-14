# ToolData Scaffold

Scaffolds a Cinema 4D viewport tool (`c4d.plugins.ToolData`). The tool inserts an object where the user clicks in the viewport. Read [scaffolds.md](../scaffolds.md) first, it describes the workflow, the common questions, the placeholders and the rules that apply to all scaffolds.

Folder prefix: `py_tool_`. Registered with: `c4d.plugins.RegisterToolPlugin` (with an *instance*). Tool plugins require a plugin resource folder containing the global symbols header and string table. For sculpting brushes (`SculptBrushToolData`) follow the `py_tool_sculpt_*` examples.

# Questions

Ask the common questions (`name`, `description`, `pluginId`) and these:

| Key | Question | Options | Default |
| --- | --- | --- | --- |
| `object` | Which object should the tool insert on a click? | `Null`, `Cube`, `Sphere` | `Null` |

The object maps to `c4d.Onull`, `c4d.Ocube` or `c4d.Osphere`.

# Files

```text
projects/{{Folder}}/
├── {{Folder}}.pyp
└── res/
    ├── c4d_symbols.h
    └── strings_en-US/
        └── c4d_strings.str
```

# Templates

## {{Folder}}.pyp

```python
"""{{Description}}

Activate the tool by searching for "{{Name}}" in the Commander (Shift + C), then click into a
viewport. To run this plugin, add its folder to the plugin paths of Cinema 4D and restart
Cinema 4D.

Topics:
    - Implementing a ToolData with ToolData.MouseInput()
    - Converting screen space to world space with BaseDraw.SW()
    - Registering a tool plugin
"""
__author__ = "{{ModelName}}"
__version__ = "{{Version}}"

import c4d
import mxutils

PLUGIN_ID: int = {{PluginId}}
IDS_PLUGIN_NAME: int = 50000
IDS_PLUGIN_HELP: int = 50001

# The ID of a built-in icon, replace it with an own icon when releasing the plugin.
ICON_ID: int = 465001193


class {{ClassName}}Tool(c4d.plugins.ToolData):
    """Implements the {{Name}} tool.
    """

    def GetState(self, doc: c4d.documents.BaseDocument) -> int:
        """Called by Cinema 4D to decide if the tool can be used currently.
        """
        return c4d.CMD_ENABLED

    def MouseInput(self, doc: c4d.documents.BaseDocument, data: c4d.BaseContainer,
                   bd: c4d.BaseDraw, win: c4d.gui.EditorWindow, msg: c4d.BaseContainer) -> bool:
        """Called by Cinema 4D when the user clicks into a viewport while the tool is active.
        """
        if msg[c4d.BFM_INPUT_CHANNEL] != c4d.BFM_INPUT_MOUSELEFT:
            return True

        # Insert the object at the click position, projected 500 units into the view. Cinema 4D
        # opens the undo step for a mouse input on its own, only AddUndo is needed.
        obj: c4d.BaseObject = mxutils.CheckType(c4d.BaseObject(c4d.<ObjectType>))
        obj.SetAbsPos(bd.SW(c4d.Vector(msg[c4d.BFM_INPUT_X], msg[c4d.BFM_INPUT_Y], 500.0)))
        doc.InsertObject(obj)
        doc.AddUndo(c4d.UNDOTYPE_NEWOBJ, obj)
        doc.SetActiveObject(obj)

        c4d.EventAdd()
        return True


# Called by Cinema 4D when this plugin module is loaded.
if __name__ == "__main__":
    icon: c4d.bitmaps.BaseBitmap = c4d.bitmaps.InitResourceBitmap(ICON_ID)

    # Tools are registered with an instance which lives for the whole Cinema 4D session.
    c4d.plugins.RegisterToolPlugin(
        id=PLUGIN_ID, str=c4d.plugins.GeLoadString(IDS_PLUGIN_NAME), info=0, icon=icon,
        help=c4d.plugins.GeLoadString(IDS_PLUGIN_HELP),
        dat={{ClassName}}Tool())
```

## res/c4d_symbols.h

```c
enum
{
	IDS_PLUGIN_NAME = 50000,
	IDS_PLUGIN_HELP = 50001,
	_DUMMY_ELEMENT_
};
```

## res/strings_en-US/c4d_strings.str

```text
STRINGTABLE
{
	IDS_PLUGIN_NAME "{{Name}}";
	IDS_PLUGIN_HELP "{{Description}}";
}
```

`<ObjectType>`: `Onull`, `Ocube` or `Osphere`.

# After Scaffolding

- Tell the user how to activate the tool (Commander, or by adding it to a palette) and what it does on a click.
- Offer the common extensions: an option dialog in the Attribute Manager with `AllocSubDialog` (see the `py_tool_ui` example), viewport drawing with `Draw`, and a cursor with `GetCursorInfo` (see `py_tool_liquid_painter`).

# References

- [Tool UI](../../examples/plugins/py_tool_ui/py_tool_ui.pyp): A tool with a `SubDialog` in the Attribute Manager.
- [Liquid Painter](../../examples/plugins/py_tool_liquid_painter/py_tool_liquid_painter.pyp): Mouse dragging, drawing and cursor handling.
