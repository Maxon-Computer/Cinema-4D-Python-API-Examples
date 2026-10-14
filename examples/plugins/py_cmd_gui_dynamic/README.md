# Example py_cmd_gui_dynamic

Demonstrates a dialog with dynamic content, where the content changes based on user input.

![Preview](preview.png)

## DETAILS

Open this dialog example by running the command "Py - Dynamic Gui" in the Commander (Shift + C).
The user can add and remove 'items' to the dialog, which are represented by link boxes. Dragging a
scene element such as an object, material, or tag into the link box will then update the label of
that previously empty or otherwise linked link box to the type name of the dragged item, e.g.,
"BaseObject". So, the two dynamic aspects are adding and removing items from the dialog and the
labels updating when the user drags an item into a link box.

Also shown here is the idea of an abstraction layer, which is not strictly necessary, but can be
useful when one wants to have a more structured way of dealing with the data in a dialog.
This is realized as the property `Items` of the `DynamicGuiDialog` class, which allows us to
just invoke `myDynamicGuiDialog.Items = [a, b, c]` for the dialog to rebuild its UI and
show the items `a`, `b`, and `c` in three link boxes.

To run this example, place the file in the Cinema 4D plugins folder and restart Cinema 4D.

Topics:
- Using GeDialog to create a dialog with dynamic content.
- Using a simple data model abstraction layer to simplify interaction with the dialog. Here
we realize DynamicGuiDialog.Items as a property that can be set and get, and upon
setting the property, the dialog will rebuild its UI.
- Using GeDialog.LayoutFlushGroup() to clear a group of gadgets and LayoutChanged() to notify
Cinema 4D that the layout has changed.
- Using GeDialog.AddCustomGui() to add custom GUI elements (here link boxes).

## FILES

| File | Description |
| --- | --- |
| [py_cmd_gui_dynamic.pyp](py_cmd_gui_dynamic.pyp) | Demonstrates a dialog with dynamic content, where the content changes based on user input. |
| [README.md](README.md) | This file. |
| [preview.png](preview.png) | Preview image for the plugin. |
