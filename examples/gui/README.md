# gui

User interface elements, dialogs, and user areas.

## Files
| File | Description |
| --- | --- |
| [README.md](README.md) | This file. |
| [dialog_ask_number.py](dialog_ask_number.py) | Creates a Modal Dialog asking for an integer or a float. Retrieves the entered value, once the user exit the Dialog. |
| [dialog_menu_hide_content.py](dialog_menu_hide_content.py) | Creates an async Dialog with a top menu. Defines an icon in the menu to toggle group visibility. |
| [dialog_modal.py](dialog_modal.py) | Creates a basic Modal Dialog. |
| [dialog_quick_tab.py](dialog_quick_tab.py) | Creates a Modal Dialog displaying a different SubDialog according to the selected entry of the QuickTab. Demonstrates how to add, flushes, remove tab interactively. |
| [dialog_subdialog.py](dialog_subdialog.py) | Creates and attaches a SubDialog to a Dialog. Switch the displayed SubDialog after a click on a button. |
| [script_custom_icon.tif](script_custom_icon.tif) | No short description provided. |
| [script_icon.py](script_icon.py) | Example to customize the icon used for a script. The icon should be named like the .py file. Should be a TIF with a size of 32x32. |
| [script_name_description.py](script_name_description.py) | Example to customize the name and the description in the script manager. Name-en-US defines the displayed name. Description-en-US defines the description of the script. As long as Name-en-US (Prior R20 it was Name-US) and Description-en-US (Prior R20 it was Description-US) are in the first comment bloc, c4d will extract them. |
| [user_area_basic.py](user_area_basic.py) | Creates and attaches a GeUserArea to a Dialog. Interacts from the GeDialog to the GeUserArea and vice-versa. |
| [user_area_drag.py](user_area_drag.py) | Creates and attaches a GeUserArea to a Dialog. Creates a series of aligned squares, that can be dragged and swapped together. |

## Related Examples

| Type | Example | Description |
| --- | --- | --- |
| Plugin | [py_cmd_gui_simple](../plugins/py_cmd_gui_simple/py_cmd_gui_simple.pyp) | Demonstrates a simple dialog with two number input fields, a combo box and a button to carry out numeric operations on the two numbers. |
