"""Demonstrates the most basic command/dialog plugin possible.

Note:
    This is not only a command hello world example, but generally a plugin hello world example. See
    the py-cmd_gui_simple example for a slightly more complex case that is also commented more
    verbosely.

Open this dialog example by running the command "Py - Hello World Gui" in the Commander (Shift + C).
This is a very simple dialog example, which demonstrates how to create a dialog with three buttons
that display a message when clicked.

Subjects:
    - GeDialog.CreateLayout() and its most basic usage to build a GUI.
    - GeDialog.Command() to handle user input.
    - CommandData.Execute() to open the dialog.
    - Registering a command plugin that manages a dialog.
"""
__copyright__ = "Copyright 2025, MAXON Computer"
__author__ = "Ferdinand Hoppe"
__date__ = "06/06/2025"
__license__ = "Apache-2.0 license"

import c4d
import typing


class HelloWorldGuiDialog(c4d.gui.GeDialog):
    """Realizes the most basic dialog possible.
    """
    # Define the button IDs.
    ID_BTN_RED: int = 1000
    ID_BTN_GREEN: int = 1001
    ID_BTN_BLUE: int = 1002

    def CreateLayout(self) -> bool:
        """Called by Cinema 4D when the GUI of the dialog is being built.
        """
        # Define the title of the dialog.
        self.SetTitle("Py - Hello World Gui")

        # Set the spacing of the implicit outermost group of the dialog.
        self.GroupBorderSpace(5, 5, 5, 5)  # A 5px border around the dialog.
        self.GroupSpace(5, 5)  # A 5px space between the elements in the dialog.

        # Add the three buttons. Gadgets are identified by their ID, which is an integer. We make
        # all buttons consume the full width of the dialog (BFH = horizontal, SCALEFIT = consume
        # all space on that axis). BFV_SCALEFIT would make the buttons consume all vertical space.
        self.AddButton(self.ID_BTN_RED, c4d.BFH_SCALEFIT, name="Red")
        self.AddButton(self.ID_BTN_GREEN, c4d.BFH_SCALEFIT, name="Green")
        self.AddButton(self.ID_BTN_BLUE, c4d.BFH_SCALEFIT, name="Blue")

        # All the elements we add in this most simple manner will be stacked vertically. See
        # py-cmd_gui_simple for a more complex example of how to build a dialog with a more complex
        # layout.

        return True

    def Command(self, mid: int, data: c4d.BaseContainer) -> bool:
        """Called by Cinema 4D when the user clicks a gadget in the dialog.
        """
        # Here we react to our buttons being clicked.
        if mid == self.ID_BTN_RED:
            c4d.gui.MessageDialog("You clicked the Red button!")
        elif mid == self.ID_BTN_GREEN:
            c4d.gui.MessageDialog("You clicked the Green button!")
        elif mid == self.ID_BTN_BLUE:
            c4d.gui.MessageDialog("You clicked the Blue button!")

        return True


class HelloWorldGuiCommand(c4d.plugins.CommandData):
    """Realizes the common implementation for a command that opens a foldable dialog.

    This example also reduces the CommandData implementation to its bare minimum, but it is
    strongly recommended to follow the more complete pattern shown in other examples, such as
    py-cmd_gui_simple.
    """
    # The dialog hosted by the plugin.
    REF_DIALOG: HelloWorldGuiDialog | None = None

    def Execute(self, doc: c4d.documents.BaseDocument) -> bool:
        """Opens the dialog when the command is executed.
        """
        # Instantiate the dialog if it does not exist yet.
        if HelloWorldGuiCommand.REF_DIALOG is None:
            HelloWorldGuiCommand.REF_DIALOG = HelloWorldGuiDialog()

        # Open the dialog when it is not yet open. We could also implement closing the dialog; see
        # one of the more complex examples for this, such as py-cmd_gui_simple. We open the dialog
        # asynchronously, i.e., the user can continue working in Cinema 4D while the dialog is open.
        if not HelloWorldGuiCommand.REF_DIALOG.IsOpen():
            HelloWorldGuiCommand.REF_DIALOG.Open(
                c4d.DLG_TYPE_ASYNC, self.ID_PLUGIN, defaultw=300, defaulth=0)

        return True

    # The unique ID of the plugin, it must be obtained from developers.maxon.net.
    ID_PLUGIN: int = 1065651

    # The name and help text of the plugin.
    STR_NAME: str = "Py - Hello World Gui"
    STR_HELP: str = "Opens a bare-bones dialog with three buttons that display a message when clicked."

    @classmethod
    def Register(cls: typing.Type, iconId: int) -> None:
        """Registers the command plugin.

        This is a custom method and not part of the CommandData interface.
        """
        # Load one of the built-in icons of Cinema 4D as the icon of the plugin. Then instantiate the
        # command plugin that will be registered. And finally register the command plugin with that
        # command instance and icon.
        bitmap: c4d.bitmaps.BaseBitmap = c4d.bitmaps.InitResourceBitmap(iconId)
        command: object = cls()
        c4d.plugins.RegisterCommandPlugin(
            id=cls.ID_PLUGIN, str=cls.STR_NAME, info=0, icon=bitmap, help=cls.STR_HELP, dat=command)


# Called by Cinema 4D when this plugin module is loaded.
if __name__ == '__main__':
    HelloWorldGuiCommand.Register(iconId=465001193)
