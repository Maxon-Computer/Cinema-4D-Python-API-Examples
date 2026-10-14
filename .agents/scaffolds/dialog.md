# Dialog Scaffold

Scaffolds a command that opens a dockable, asynchronous dialog (`c4d.gui.GeDialog`). The dialog is laid out either in code or with resource files. Read [scaffolds.md](../scaffolds.md) first, it describes the workflow, the common questions, the placeholders and the rules that apply to all scaffolds.

Folder prefix: `py_cmd_gui_`. Registered with: `c4d.plugins.RegisterCommandPlugin` (with an *instance*). The command hosts one dialog, the dialog holds all logic.

# Questions

Ask the common questions (`name`, `description`, `pluginId`) and these:

| Key | Question | Options | Default |
| --- | --- | --- | --- |
| `layout` | How should the dialog be laid out? | `In code` (everything in one `.pyp` file), `With resource files` (dialog markup and string tables in `res/`, enables translations) | `In code` |
| `gadgets` | Which gadgets should the dialog contain? (multi select) | `Number field`, `Text field`, `Combo box`, `Checkbox`, `Button`, `Multi-line output` | `Number field`, `Button`, `Multi-line output` |

The gadgets are placed in this order: a two column group with label and field for each of `Number field`, `Text field` and `Combo box`, then the `Checkbox`, then the `Button`, then the `Multi-line output` that takes all remaining space. When `Button` is selected, clicking it reads all other input gadgets and writes their values to the `Multi-line output`, or to a message dialog when there is no output. Without a `Button` the dialog has no `Command` method.

# Files

In code:

```text
projects/{{Folder}}/
└── {{Folder}}.pyp
```

With resource files:

```text
projects/{{Folder}}/
├── {{Folder}}.pyp
└── res/
    ├── c4d_symbols.h
    ├── dialogs/
    │   └── idd_main.res
    └── strings_en-US/
        ├── c4d_strings.str
        └── dialogs/
            └── idd_main.str
```

# Templates: In Code

## {{Folder}}.pyp

```python
"""{{Description}}

Open the dialog by running the command "{{Name}}" in the Commander (Shift + C) or from the
Extensions menu. To run this plugin, add its folder to the plugin paths of Cinema 4D and restart
Cinema 4D.

Topics:
    - GeDialog.CreateLayout() to build a GUI in code
    - GeDialog.InitValues() to set initial values of the dialog
    - GeDialog.Command() to handle user input
    - The pattern for a command plugin that manages a dockable dialog
"""
__author__ = "{{ModelName}}"
__version__ = "{{Version}}"

import c4d

PLUGIN_ID: int = {{PluginId}}

# The ID of a built-in icon, replace it with an own icon when releasing the plugin.
ICON_ID: int = 465001193


class {{ClassName}}Dialog(c4d.gui.GeDialog):
    """Realizes the dialog of the {{Name}} plugin.
    """
    # Gadget IDs must be unique within the dialog and should start at 1000 or above. Gaps between
    # logical blocks make it easy to add gadgets later.
    ID_GRP_MAIN: int = 1000
    ID_GRP_FIELDS: int = 1001

    <IdLines>

    def CreateLayout(self) -> bool:
        """Called by Cinema 4D once, when the GUI of the dialog is built.
        """
        self.SetTitle("{{Name}}")

        # The outermost group stacks all content in a single column and consumes all space.
        self.GroupBegin(self.ID_GRP_MAIN, c4d.BFH_SCALEFIT | c4d.BFV_SCALEFIT, cols=1, rows=0)
        self.GroupBorderSpace(5, 5, 5, 5)
        self.GroupSpace(5, 5)

        <LayoutBlocks>

        self.GroupEnd() # ID_GRP_MAIN
        return True

    def InitValues(self) -> bool:
        """Called by Cinema 4D after the layout has been built, to set the initial values.
        """
        <InitLines>
        return True

    <CommandMethod>


class {{ClassName}}Command(c4d.plugins.CommandData):
    """Realizes the command that opens, folds and restores the dialog.
    """
    # The dialog hosted by the command.
    REF_DIALOG: {{ClassName}}Dialog | None = None

    @property
    def Dialog(self) -> {{ClassName}}Dialog:
        """Returns the dialog of the command, and creates it when it does not exist yet.
        """
        if self.REF_DIALOG is None:
            self.REF_DIALOG = {{ClassName}}Dialog()

        return self.REF_DIALOG

    def Execute(self, doc: c4d.documents.BaseDocument) -> bool:
        """Folds the dialog when it is open, otherwise opens or unfolds it.
        """
        if self.Dialog.IsOpen() and not self.Dialog.GetFolding():
            self.Dialog.SetFolding(True)
        else:
            # An asynchronous dialog does not block Cinema 4D and can be docked.
            self.Dialog.Open(c4d.DLG_TYPE_ASYNC, PLUGIN_ID, defaultw=400, defaulth=300)

        return True

    def RestoreLayout(self, secret: object) -> bool:
        """Called by Cinema 4D to restore the dialog when the layout changes, this is mandatory.
        """
        return self.Dialog.Restore(PLUGIN_ID, secret)

    def GetState(self, doc: c4d.documents.BaseDocument) -> int:
        """Called by Cinema 4D to get the state of the command, the icon is blue while it is open.
        """
        if self.Dialog.IsOpen() and not self.Dialog.GetFolding():
            return c4d.CMD_ENABLED | c4d.CMD_VALUE

        return c4d.CMD_ENABLED


# Called by Cinema 4D when this plugin module is loaded.
if __name__ == "__main__":
    icon: c4d.bitmaps.BaseBitmap = c4d.bitmaps.InitResourceBitmap(ICON_ID)

    # Commands are registered with an instance which lives for the whole Cinema 4D session.
    c4d.plugins.RegisterCommandPlugin(
        id=PLUGIN_ID, str="{{Name}}", info=0, icon=icon, help="{{Description}}",
        dat={{ClassName}}Command())
```

## Gadget snippets

Insert the snippets of the selected gadgets into the placeholders of the template. Keep the order of the table.

| Gadget | `<IdLines>` | `<LayoutBlocks>` | `<InitLines>` | Run line (`Command`) |
| --- | --- | --- | --- | --- |
| Number field | `ID_LBL_NUMBER: int = 2000`, `ID_NUMBER: int = 2001` | In the field group: `self.AddStaticText(self.ID_LBL_NUMBER, c4d.BFH_LEFT, name="Number:")`, `self.AddEditNumberArrows(self.ID_NUMBER, c4d.BFH_SCALEFIT)` | `self.SetFloat(self.ID_NUMBER, 0.0)` | `f"Number: {self.GetFloat(self.ID_NUMBER)}"` |
| Text field | `ID_LBL_TEXT: int = 2002`, `ID_TEXT: int = 2003` | In the field group: `self.AddStaticText(self.ID_LBL_TEXT, c4d.BFH_LEFT, name="Text:")`, `self.AddEditText(self.ID_TEXT, c4d.BFH_SCALEFIT)` | `self.SetString(self.ID_TEXT, "")` | `f"Text: {self.GetString(self.ID_TEXT)}"` |
| Combo box | `ID_LBL_COMBO: int = 2004`, `ID_COMBO: int = 2005`, `ID_OPTION_A: int = 0`, `ID_OPTION_B: int = 1` (the item IDs only need to be unique within the combo box) | In the field group: `self.AddStaticText(self.ID_LBL_COMBO, c4d.BFH_LEFT, name="Option:")`, `self.AddComboBox(self.ID_COMBO, c4d.BFH_SCALEFIT)`, then `self.AddChild(self.ID_COMBO, self.ID_OPTION_A, "Option A")` and the same for `ID_OPTION_B` | `self.SetInt32(self.ID_COMBO, self.ID_OPTION_A)` | `f"Option: {self.GetInt32(self.ID_COMBO)}"` |
| Checkbox | `ID_CHECK: int = 2006` | After the field group: `self.AddCheckbox(self.ID_CHECK, c4d.BFH_LEFT, 0, 0, "Enabled")` | `self.SetBool(self.ID_CHECK, True)` | `f"Enabled: {self.GetBool(self.ID_CHECK)}"` |
| Button | `ID_BTN_RUN: int = 2007` | `self.AddButton(self.ID_BTN_RUN, c4d.BFH_SCALEFIT, name="Run")` | none | none |
| Multi-line output | `ID_OUTPUT: int = 2008` | After the button: `self.AddMultiLineEditText(self.ID_OUTPUT, c4d.BFH_SCALEFIT \| c4d.BFV_SCALEFIT, style=c4d.DR_MULTILINE_READONLY)` | `self.SetString(self.ID_OUTPUT, "")` | none |

Wrap the field gadgets (number, text, combo box) in one group, which is omitted when none of them is selected:

```python
        # Labels and fields are placed in two columns, the fields scale to the remaining width.
        self.GroupBegin(self.ID_GRP_FIELDS, c4d.BFH_SCALEFIT, cols=2, rows=0)
        self.GroupSpace(5, 5)
        <the labels and fields>
        self.GroupEnd() # ID_GRP_FIELDS
```

Also omit `ID_GRP_FIELDS` from the template when the group is omitted. When there are no init lines, `InitValues` is `return True` only.

## Command method

Only when `Button` is selected. `<Lines>` are the run lines of the selected input gadgets, one list entry each.

```python
    def Command(self, mid: int, data: c4d.BaseContainer) -> bool:
        """Called by Cinema 4D when the user interacts with a gadget.
        """
        if mid == self.ID_BTN_RUN:
            lines: list[str] = [
                <Lines>
            ]
            self.SetString(self.ID_OUTPUT, "\n".join(lines))

        return True
```

When there is no `Multi-line output`, replace the `SetString` line with `c4d.gui.MessageDialog("\n".join(lines))`. When there are no input gadgets, use `lines = ["{{Name}}"]`.

# Templates: With Resource Files

The `.pyp` file is the one of the in code variant with these differences:

- Add the imports and the symbol import after the plugin constants, the `PLUGIN_ID` and `ICON_ID` constants are replaced by the symbols of the resources (`ID_PLUGIN` is defined in `c4d_symbols.h`):

```python
import os

import c4d
import mxutils

# Makes the symbols of res/c4d_symbols.h available as attributes of this module, e.g., ID_PLUGIN.
mxutils.ImportSymbols(os.path.join(os.path.dirname(__file__), "res"))

# The ID of a built-in icon, replace it with an own icon when releasing the plugin.
ICON_ID: int = 465001193
```

- Use `ID_PLUGIN` instead of `PLUGIN_ID` everywhere. The dialog has no `ID_GRP_*` and gadget ID constants, it uses the `IDC_*` symbols of the resource.
- `CreateLayout` loads the resource, the title comes from the strings:

```python
    def CreateLayout(self) -> bool:
        """Called by Cinema 4D once, when the GUI of the dialog is built.
        """
        self.SetTitle(c4d.plugins.GeLoadString(IDS_PLUGIN_NAME))
        return self.LoadDialogResource(IDD_MAIN)
```

- `InitValues` and `Command` use `IDC_NUMBER`, `IDC_TEXT`, `IDC_COMBO`, `IDC_COMBO_A`, `IDC_CHECK`, `IDC_RUN` and `IDC_OUTPUT` without `self.`, and `Command` reads `IDC_RUN` instead of `self.ID_BTN_RUN`. Combo box items are selected with `self.SetInt32(IDC_COMBO, IDC_COMBO_A)`.
- The registration loads name and help from the strings and makes sure that the resources are initialized:

```python
# Called by Cinema 4D when this plugin module is loaded.
if __name__ == "__main__":
    # Cinema 4D usually exposes the resources of a plugin as __res__, make sure that it exists.
    res: c4d.plugins.GeResource | None = globals().get("__res__", None)
    if not isinstance(res, c4d.plugins.GeResource):
        res = c4d.plugins.GeResource()
        if not res.Init(os.path.join(os.path.dirname(__file__), "res")):
            raise RuntimeError("Failed to initialize the plugin resources.")

        __res__ = res

    icon: c4d.bitmaps.BaseBitmap = c4d.bitmaps.InitResourceBitmap(ICON_ID)
    c4d.plugins.RegisterCommandPlugin(
        id=ID_PLUGIN, str=c4d.plugins.GeLoadString(IDS_PLUGIN_NAME), info=0, icon=icon,
        help=c4d.plugins.GeLoadString(IDS_PLUGIN_HELP), dat={{ClassName}}Command())
```

## res/c4d_symbols.h

```cpp
#ifndef C4D_SYMBOLS_H__
#define C4D_SYMBOLS_H__

enum
{
    ID_PLUGIN = {{PluginId}},

    // The name and help text of the plugin, defined in strings_en-US/c4d_strings.str.
    IDS_PLUGIN_NAME = 1000,
    IDS_PLUGIN_HELP,

    // The dialog and its gadgets, the strings are defined in strings_en-US/dialogs/idd_main.str.
    IDD_MAIN = 1100,
    <SymbolLines>

    __DUMMY__
};

#endif
```

`<SymbolLines>` per selected gadget, in this order (one `IDC_` gadget symbol and one `IDS_` string symbol per label or caption):

| Gadget | Symbols |
| --- | --- |
| Number field | `IDC_NUMBER,` `IDS_NUMBER,` |
| Text field | `IDC_TEXT,` `IDS_TEXT,` |
| Combo box | `IDC_COMBO,` `IDS_COMBO,` `IDC_COMBO_A,` `IDS_COMBO_A,` `IDC_COMBO_B,` `IDS_COMBO_B,` |
| Checkbox | `IDC_CHECK,` `IDS_CHECK,` |
| Button | `IDC_RUN,` `IDS_RUN,` |
| Multi-line output | `IDC_OUTPUT,` |

## res/dialogs/idd_main.res

```text
DIALOG IDD_MAIN
{
    SCALE_H; SCALE_V;

    GROUP
    {
        COLUMNS 1;
        SPACE 5, 5;
        BORDERSIZE 5, 5, 5, 5;
        SCALE_H; SCALE_V;

        <GadgetBlocks>
    }
}
```

`<GadgetBlocks>`: Same order as in code. The field gadgets share one group:

```text
        GROUP
        {
            COLUMNS 2;
            SPACE 5, 5;
            SCALE_H;

            STATICTEXT { NAME IDS_NUMBER; CENTER_V; ALIGN_LEFT; }
            EDITNUMBERARROWS IDC_NUMBER { SCALE_H; }

            STATICTEXT { NAME IDS_TEXT; CENTER_V; ALIGN_LEFT; }
            EDITTEXT IDC_TEXT { SCALE_H; }

            STATICTEXT { NAME IDS_COMBO; CENTER_V; ALIGN_LEFT; }
            COMBOBOX IDC_COMBO
            {
                SCALE_H;
                CHILDS
                {
                    IDC_COMBO_A, IDS_COMBO_A;
                    IDC_COMBO_B, IDS_COMBO_B;
                }
            }
        }
```

followed by the remaining gadgets of the column:

```text
        CHECKBOX IDC_CHECK { NAME IDS_CHECK; }
        BUTTON IDC_RUN { NAME IDS_RUN; SCALE_H; }
        MULTILINEEDIT IDC_OUTPUT { SCALE_H; SCALE_V; }
```

Only include the blocks of the selected gadgets.

## res/strings_en-US/c4d_strings.str

```text
STRINGTABLE
{
    IDS_PLUGIN_NAME "{{Name}}";
    IDS_PLUGIN_HELP "{{Description}}";
}
```

## res/strings_en-US/dialogs/idd_main.str

```text
DIALOGSTRINGS IDD_MAIN
{
    <StringLines>
}
```

`<StringLines>`: One line per `IDS_` symbol of the selected gadgets, `IDS_NUMBER "Number:";`, `IDS_TEXT "Text:";`, `IDS_COMBO "Option:";`, `IDS_COMBO_A "Option A";`, `IDS_COMBO_B "Option B";`, `IDS_CHECK "Enabled";`, `IDS_RUN "Run";`.

# After Scaffolding

- Tell the user that the command is found in the Extensions menu and by name in the Commander (Shift + C), and that the dialog can be docked in the layout.
- Mention that `RestoreLayout` is mandatory, without it the dialog does not come back when the user changes the layout.
- Mention that dialog callbacks run on the main thread, but that long running work should not block it (see `.agents/scene.md`).
- For the resource variant mention that changes of resource files require a restart, and that other languages are added by copying the `strings_en-US` folder. For current details, start at <https://developers.maxon.net/docs/py> and search for `Implementing Plugins` and `resource strings`.
- Offer to implement the logic behind the button, or to extend the layout with user areas, tabs, or dynamic content (see the references).

# References

- [Hello World GUI](../../examples/plugins/py_cmd_gui_hello_world/py_cmd_gui_hello_world.pyp): The smallest command with a dialog.
- [Simple GUI](../../examples/plugins/py_cmd_gui_simple/py_cmd_gui_simple.pyp): Groups, labelled fields, a combo box, a button, and a multi-line output.
- [Persistent GUI](../../examples/plugins/py_cmd_gui_persistent/py_cmd_gui_persistent.pyp): The fold, restore and state pattern of the command, and saving dialog data.
- [Dynamic GUI](../../examples/plugins/py_cmd_gui_dynamic/py_cmd_gui_dynamic.pyp): Dialogs with content that changes at runtime.
- [Resource GUI](../../examples/plugins/py_cmd_gui_resources/py_cmd_gui_resources.pyp): Dialog resources and translations.
- For current resource details, start at <https://developers.maxon.net/docs/py> and search for `Resource Files`.
