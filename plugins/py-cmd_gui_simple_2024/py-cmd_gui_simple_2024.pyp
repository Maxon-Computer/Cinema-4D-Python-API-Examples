"""Demonstrates a simple dialog with two number input fields, a combo box and a button to
carry out numeric operations on the two numbers.

Open this dialog example by running the command "Py - Simple Gui" in the Commander (Shift + C). This
is a very simple dialog example, which demonstrates how to create a dialog with a few gadgets, how 
to handle user input, and how to display results in a multi-line edit text field.

Subjects:
    - GeDialog.CreateLayout() and how to use it build a GUI.
    - GeDialog.InitValues() to set initial values of the dialog.
    - GeDialog.Command() to handle user input.
    - Using a custom GUI.
    - Implementing a very simple gui-value abstraction.
    - The pattern for implementing a command plugin that manages a dialog.
"""
__copyright__ = "Copyright 2025, MAXON Computer"
__author__ = "Ferdinand Hoppe"
__date__ = "06/06/2025"
__license__ = "Apache-2.0 license"

import c4d
import typing


class SimpleGuiDialog(c4d.gui.GeDialog):
    """Realizes a very simple dialog with two number input fields, a combo box and a button, to
    carry out numeric operations on the two numbers.
    """
    # Dialogs, as most things in Cinema 4D, are driven by messages and symbols, i.e., numeric
    # identifiers for entities. These symbols and the layout of a dialog can be defined in a
    # resource (file), but a common approach is also to define everything in code, as we do here.

    # It is ABSOLUTELY necessary to define unique IDs for the dialog. Because when we use the same
    # ID twice, we will be able to add the two gadgets to the dialog, but when we try to interact
    # with them, we cannot distinguish them, as they have the same ID.

    # Groups in the dialog, we use them to structure the placement of gadgets in the dialog. It is
    # common practice and in some cases also a necessity to define IDs starting out from the value
    # 1000 (as Cinema 4D sometimes defines ID below 1000 for its own purposes).
    ID_GRP_MAIN: int      = 1000
    ID_GRP_NUMBERS: int   = 1001
    ID_GRP_OPERATION: int = 1002

    # Not necessary, but good practice it is to leave gaps between logical blocks of IDed entities,
    # here for example between the group IDs and the IDs of the actual gadgets. This way, we can
    # easily add new groups or gadgets without having to change the IDs of the existing ones.

    # The IDs for the actual gadgets.
    ID_BTN_CLEAR: int     = 2000 # The button to clear the result.
    ID_LBL_NUM_A: int     = 2001 # The static text label for the first number.
    ID_NUM_A: int         = 2002 # The first number input field.
    ID_LBL_NUM_B: int     = 2003 # The static text label for the second number.
    ID_NUM_B: int         = 2004 # The second number input field.
    ID_LBL_OPERATION: int = 2005 # The static text label for the operation.
    ID_CMB_OPERATION: int = 2006 # The combo box to select the operation.
    ID_BTN_CALCULATE: int = 2007 # The button to calculate the result.
    ID_MLE_RESULT: int    = 2008 # The static text label for the result.
    
    # The IDs for the operations in the combo box. These do not refer to gadgets, but to items in
    # the combo box. So, we do not have to avoid conflicts for these IDs with other IDs they must
    # be unique only within the combo box.
    ID_OP_ADD: int        = 0 # The ID of the "Add" operation in the combo box.
    ID_OP_SUBTRACT: int   = 1 # The ID of the "Subtract" operation in the combo box.
    ID_OP_MULTIPLY: int   = 2 # The ID of the "Multiply" operation in the combo box.
    ID_OP_DIVIDE: int     = 3 # The ID of the "Divide" operation in the combo box.

    def __init__(self):
        """Initializes the dialog.
        """
        # Stores the result-expression pairs for all the past calculations. See AddResult() for 
        # details.
        self._history: list[tuple[float, str]] = []
        
    def CreateLayout(self) -> bool:
        """Called by Cinema 4D when the GUI of the dialog is being built.

        This method is called exactly once for the lifetime of a dialog, i.e., the GUI defined here 
        is static/persistent. See py-cmd_gui_dynamic for a dialog that can change its GUI dynamically
        at runtime based on user inputs.

        Returns:
            bool: True if the layout was created successfully, otherwise False.
        """
        # Defines the title of the Dialog
        self.SetTitle("Py - Simple Gui")

        # Dialogs have by default an implicit outmost group, for which we can set things like the
        # border and the padding. I.e., the calls below would be absolutely legal.
        # self.GroupBorderSpace(*self.PAD_BORDER_SPACE)
        # self.GroupSpace(*self.PAD_ELEMENT_SPACE) 

        # But for the implicit outmost group, we cannot set the row and column count (which we do
        # not need here), but for the sake of clarity, we define our own outmost group (which will
        # be inside the implicit outmost group) and verbosely set its row and column count.

        # Defines the group of the dialog which holds all its content. A column count of 1 and a row
        # count of 0 means that the group will expand vertically to stack all its children. I.e., we
        # currently have a layout such as:
        #
        #   +-- GRP_MAIN ----------------+
        #   |                            |
        #   |  [Element_0]               |
        #   |  [Element_1]               |
        #   |  ...                       |
        #   |  [Element_N]               |
        #   |                            |
        #   +----------------------------+
        self.GroupBegin(self.ID_GRP_MAIN, c4d.BFH_SCALEFIT | c4d.BFV_SCALEFIT, cols=1, rows=0)
        self.GroupBorderSpace(5, 5, 5, 5) # Sets the border space of the group.
        self.GroupSpace(5, 5) # Sets the space between the elements in the group.

        # Into this group we will stack five elements, two groups, a button, a separator, and a
        # multi-line edit text field. Lets start with the first group:

        # We add a new group that has a column count of 4 and a row count of 0, which means that the
        # group will put four elements in a single row, before breaking to the next row. I.e., our
        # layout will look like this:
        #
        #   +-- GRP_MAIN ----------------+
        #   |  +-- GRP_NUMBERS --------+ |
        #   |  |                       | |
        #   |  |  [A], [B], [C], [D],  | |
        #   |  |  [E], [F], [G], [H],  | |
        #   |  |  ...                  | |
        #   |  +-----------------------+ |
        #   |  ...                       |
        #   

        # Add the group for the numbers, the group consumes the full width of the parent group
        # (BFH_SCALEFIT) and will fit its height to the content (BFV_FIT). 
        self.GroupBegin(self.ID_GRP_NUMBERS, c4d.BFH_SCALEFIT | c4d.BFV_FIT, cols=4, rows=0)
        self.GroupSpace(5, 5) # Sets the space between the elements in the group.

        # Effectively we will use this group to populate a singular row with four elements, two 
        # pairs of a static text label and an edit number field, i.e., the layout will look like this:
        #
        #   +-- GRP_NUMBERS ------------------------------+
        #   | Lbl_A: [EditNumber_A] Lbl_B: [EditNumber_B] |
        #   +---------------------------------------------+

        # Add labels which are horizontally left aligned, i.e., only consume the space they need
        # to display their text, and add edit number fields that will scale to fill the remaining
        # space in the row.
        self.AddStaticText(self.ID_LBL_NUM_A, c4d.BFH_LEFT, name="A:")
        self.AddEditNumberArrows(self.ID_NUM_A, c4d.BFH_SCALEFIT)
        self.AddStaticText(self.ID_LBL_NUM_B, c4d.BFH_LEFT, name="B:")
        self.AddEditNumberArrows(self.ID_NUM_B, c4d.BFH_SCALEFIT)
        self.GroupEnd() # end of ID_GRP_NUMBERS

        # Now we add the second group, which will hold the operation selection and its label. One 
        # might ask why we do not add these controls to former group, as we could have a row with 
        # four elements and then break to the next row with two elements.
        #
        # Cinema 4D's groups act more like a table and not like a stack panel, so when we have a
        # four column group, and four elements, in one row, and two elements in the next row, where
        # one element is very long, the layout will look like this:
        #
        #   +--------------------------+
        #   |  A B                 C D |
        #   |  E VERY_VERY_LONG_F      |
        #   +--------------------------+
        #
        # I.e., the largest element in a column will determine the width of the whole column.

        # Add a two column group that will hold the operation selection and its label. We could 
        # stack multiple label-value pairs in this group to get the typical label aligned look of
        # the Cinema 4D UI.
        self.GroupBegin(self.ID_GRP_OPERATION, c4d.BFH_SCALEFIT | c4d.BFV_FIT, cols=2, rows=0)
        self.GroupSpace(5, 5)
        self.AddStaticText(self.ID_LBL_OPERATION, c4d.BFH_LEFT, name="Operation:")
        self.AddComboBox(self.ID_CMB_OPERATION, c4d.BFH_SCALEFIT)
        # Add the children of the combo box, i.e., the items that will be displayed in the 
        # drop-down, the operations that can be performed on the two numbers.
        self.AddChild(self.ID_CMB_OPERATION, self.ID_OP_ADD, "Add")
        self.AddChild(self.ID_CMB_OPERATION, self.ID_OP_SUBTRACT, "Subtract")
        self.AddChild(self.ID_CMB_OPERATION, self.ID_OP_MULTIPLY, "Multiply")
        self.AddChild(self.ID_CMB_OPERATION, self.ID_OP_DIVIDE, "Divide")
        self.GroupEnd() # end of ID_GRP_OPERATION

        # At this point, our layout looks like this:
        #
        #   +-- GRP_MAIN --------------------+
        #   |  +-- GRP_NUMBERS ------------+ |
        #   |  | A: [NumEdit] B: [NumEdit] | |
        #   |  +---------------------------+ |
        #   |  +-- GRP_OPERATION ---------+  |
        #   |  | Operation: [ComboBox    ]|  |
        #   |  +---------------------------+ |
        #   |  ...                           |

        # Now we add a button in the outmost single column group, and make it scale over the full
        # width of the group. After that we add a horizontal separator (which have no ID).
        self.AddButton(self.ID_BTN_CALCULATE, c4d.BFH_SCALEFIT, name="Calculate")
        self.AddSeparatorH(1)
        
        # Last but not least, we add a multi-line edit text field that will display the results and
        # stretches the full width and height of the remaining space. Multi-line edits are example
        # of more complex controls which allow for styling, we just make it read-only here, so that
        # it acts as the console output of the dialog.
        self.AddMultiLineEditText(self.ID_MLE_RESULT, c4d.BFH_SCALEFIT | c4d.BFV_SCALEFIT, 
                                  style=c4d.DR_MULTILINE_READONLY)
        
        # Our dialog now looks like this:
        #
        #   +-- GRP_MAIN --------------------+
        #   |  +-- GRP_NUMBERS ------------+ |
        #   |  | A: [NumEdit] B: [NumEdit] | |
        #   |  +---------------------------+ |
        #   |  +-- GRP_OPERATION ----------+ |
        #   |  | Operation: [ComboBox   ]  | |
        #   |  +---------------------------+ |
        #   |  [Calculate Button           ] |
        #   |  ----------------------------- |
        #   |  [MultiLineEdit              ] |
        #   +--------------------------------+

        # The last thing we will do, which we would conventionally do as the first thing, is place
        # controls in the menu of the dialog. We saved this for last, as this entails two more
        # advanced concepts, namely menu controls and custom GUIs.
        # 
        # A menu control is a control placed on the right side of the menu bar of the dialog,
        # Cinema puts here often things like buttons or combo boxes, which provide often used
        # functionality for their dialog. We could also implement a traditional text menu, but
        # this is for another example.

        # A menu group has no ID and rows or columns. When we want more layout control, we have to
        # add a sub-group.
        self.GroupBeginInMenuLine()
        self.GroupBorderSpace(5, 5, 5, 5)
        self.GroupSpace(5, 5)

        # We could add here just a normal button as we did above, but we will do something a bit
        # fancier, we will use a custom GUI. Dialogs have methods for a handful of standard GUIs
        # for certain data types, such as edit fields, check boxes, combo boxes, etc. But Cinema
        # 4D offers also many, many, many more more GUI gadgets called custom GUIs. These actually
        # also can come with a custom data type, for example the spline or gradient GUI do that. To
        # be able to properly use a custom GUI, you often need access to the custom GUI class. 
        # 
        # We will add here a very commonly used custom GUI, a BitmapButtonCustomGui, which as its
        # name implies, is a button that displays a bitmap. Since we will use it as a simple action
        # button, we will not have to deal with the custom gui class, but we can learn how to add
        # a custom GUI to a dialog.

        # Custom GUIs always have a settings container which defines how the custom GUI looks and
        # behaves. They are documented in c4d.gui module alongside their custom GUI classes.
        settings: c4d.BaseContainer = c4d.BaseContainer()
        # Enable button behavior, i.e., the button will be clickable.
        settings[c4d.BITMAPBUTTON_BUTTON] = True
        # The icon of the button. Icons are often referenced by their registered icon ID. We use a 
        # built-in icon, see the Icon Index in the documentation for details.
        settings[c4d.BITMAPBUTTON_ICONID1] = c4d.RESOURCEIMAGE_CLEARSELECTION
        # The tooltip of the button which is displayed when the user hovers over the button.
        settings[c4d.BITMAPBUTTON_TOOLTIP] = "Clears the results"

        # Add the custom GUI to the dialog, i.e., we place an bitmap in the top-right corner of
        # the dialog, which will clear the results when clicked.
        self.AddCustomGui(
            self.ID_BTN_CLEAR, c4d.CUSTOMGUI_BITMAPBUTTON, "", c4d.BFH_LEFT, 0, 0, settings)

        self.GroupEnd() # end of menu group
        self.GroupEnd() # end of ID_GRP_MAIN

        return True
    
    def InitValues(self) -> bool:
        """Called by Cinema 4D after the layout has been created.

        Returns:
            bool: True if the initial values were set successfully, otherwise False.
        """
        # Set the initial values of the edit number fields.
        self.SetFloat(self.ID_NUM_A, 42.0)
        self.SetFloat(self.ID_NUM_B, 3.14159)

        # Set the initial value of the combo box to the "Multiply" operation.
        self.SetInt32(self.ID_CMB_OPERATION, self.ID_OP_MULTIPLY)

        # Set our history of results to the empty string.
        self.SetString(self.ID_MLE_RESULT, "")

        return True

    def Command(self, mid: int, data: c4d.BaseContainer) -> bool:
        """Called by Cinema 4D when the user clicked a gadget in the dialog.

        This is just a specialization of GeDialog.Message() which among other things, conveys a
        broader stream of input events such as mouse and keyboard events. But this method is good 
        way to implement simple click events, as we do not have to deal with the message data in 
        detail.

        Args:
            mid (int): The ID of the gadget that was clicked.
            data (c4d.BaseContainer): The message data for the click event.

        Returns:
            bool: True if the click event was consumed, False otherwise.
        """
        # The user clicked the clear button. Despite this being a custom GUI, on this very simple
        # level, we can interact with it just via its ID, and do not have to sue the full custom 
        # GUI class.
        if mid == self.ID_BTN_CLEAR:
            return self.ClearResults()
        # The user clicked the calculate button, which is a 'normal' button.
        elif mid == self.ID_BTN_CALCULATE:
            return self.Calculate()

        return True
    
    # --- Custom methods ---------------------------------------------------------------------------

    def Calculate(self) -> None:
        """Calculates the result based on the input values and the selected operation.

        This is the primary logic of the dialog.
        """
        # Get the values of the two input fields.
        num_a: float = self.GetFloat(self.ID_NUM_A)
        num_b: float = self.GetFloat(self.ID_NUM_B)

        # Get the selected operation from the combo box.
        operation: int = self.GetInt32(self.ID_CMB_OPERATION)

        # Perform the calculation based on the selected operation.
        if operation == self.ID_OP_ADD:
            result: float = num_a + num_b
            expression: str = f"{num_a} + {num_b}"
        elif operation == self.ID_OP_SUBTRACT:
            result: float = num_a - num_b
            expression: str = f"{num_a} - {num_b}"
        elif operation == self.ID_OP_MULTIPLY:
            result: float = num_a * num_b
            expression: str = f"{num_a} * {num_b}"
        elif operation == self.ID_OP_DIVIDE:
            if num_b != 0:
                result: float = num_a / num_b
                expression: str = f"{num_a} / {num_b}"
            else:
                result = 0.0
                expression = f"{num_a} / {num_b} (Division by zero)"
        else: # Should never happen, but we handle it gracefully.
            return self.AddResult(0.0, "Error: Unknown operation")
        
        # Add the result to the history and update the result label.
        return self.AddResult(result, expression)

    def AddResult(self, result: float, expression: str) -> bool:
        """Adds a result to the history and updates the result label.

        It is often beneficial to add abstractions for certain aspects of a dialog, which hide away
        implementation details of a dialog. In this very simple example, we add the AddResult()
        and ClearResults() methods to the dialog. 

        The abstraction is here very simple, but we hide away that there is a #self._history which
        is a list of tuples that holds the results and their expressions. When a new result is
        added, we append it to the history and then build a string from the history to display it in
        the multi-line edit text field.

        The non-abstracted way to do this would be to directly manipulate the multi-line edit text 
        field in Command(). But without the attribute self._history, it would for example be harder
        to always display the sum of all results in the result label, as we have to insert the 
        current result before that sum and also have to keep track of the history of results.

        See py-cmd_gui_dynamic for a more complex example of how to builds abstractions around a
        a GUI.

        Args:
            result (float): The result of the calculation.
            expression (str): The expression that was calculated.
        """
        # Adds the result and expression to the history.
        self._history.append((result, expression))

        # Build the output string from the history, which will be displayed in the result label.
        output: str = "\n".join(f"{expr} = {res:.2f}" for res, expr in self._history)
        # Add the total sum of the results to the output.
        total: float = sum(res for res, _ in self._history)
        output += "\n" + "-" * 80
        output += f"\nSum of results: {total:.2f}"

        # Update the result multi-line edit text field with the output string.
        self.SetString(self.ID_MLE_RESULT, output)

        return True

    def ClearResults(self) -> bool:
        """Clears the results and the result label.

        This is the other part of the very simple abstraction. It just clears #self._history and
        sets the result label to an empty string.

        This method is called when the user clicks the clear button in the dialog.
        """
        # Clear the history of results.
        self._history.clear()
        # Clear the result label.
        self.SetString(self.ID_MLE_RESULT, "")
        
        return True 
    
class SimpleGuiCommand (c4d.plugins.CommandData):
    """Realizes the common implementation for a command that opens a foldable dialog.

    It effectively realizes the button to be found in menus, palettes, and the command manager 
    that opens our dialog. Technically, this is the concrete plugin we implement. But it here
    only plays a secondary role to the dialog, where all the logic is implemented.
    """
    # The dialog hosted by the plugin.
    REF_DIALOG: SimpleGuiDialog | None = None

    @property
    def Dialog(self) -> SimpleGuiDialog:
        """Returns the class bound dialog instance.
        """
        if self.REF_DIALOG is None:
            self.REF_DIALOG = SimpleGuiDialog()

        return self.REF_DIALOG

    def Execute(self, doc: c4d.documents.BaseDocument) -> bool:
        """Folds or unfolds the dialog.
        """
        # Fold the dialog, i.e., hide it if it is open and unfolded.
        if self.Dialog.IsOpen() and not self.Dialog.GetFolding():
            self.Dialog.SetFolding(True)
        # Open or unfold the dialog. When we open the dialog, we do it asynchronously, i.e., the
        # user can unfocus the dialog and continue working in Cinema 4D, while the dialog is open.
        # The alternative would be to open a modal dialog, which would force the user to focus the
        # dialog until it is closed. Modal can be useful but cannot be docked in the layout.
        else:
            self.Dialog.Open(c4d.DLG_TYPE_ASYNC, self.ID_PLUGIN, defaultw=300, defaulth=300)

        return True

    def RestoreLayout(self, secret: any) -> bool:
        """Restores the dialog on layout changes.

        Implementing this is absolutely necessary, as otherwise the dialog will not be
        restored when the user changes the layout of Cinema 4D.
        """
        return self.Dialog.Restore(self.ID_PLUGIN, secret)

    def GetState(self, doc: c4d.documents.BaseDocument) -> int:
        """Sets the command icon state of the plugin.

        With this you can tint the command icon blue when the dialog is open or grey it out when
        some condition is not met (not done here). You could for example disable the plugin when
        there is nothing selected in a scene, when document is not in polygon editing mode, etc.
        """
        # The icon is never greyed out, the button can always be clicked.
        result: int = c4d.CMD_ENABLED

        # Tint the icon blue when the dialog is already open.
        if self.Dialog.IsOpen() and not self.Dialog.GetFolding():
            result |= c4d.CMD_VALUE

        return result
    
    # The unique ID of the plugin, it must be obtained from developers.maxon.net.
    ID_PLUGIN: int = 1065652

    # The name and help text of the plugin.
    STR_NAME: str = "Py - Simple Gui"
    STR_HELP: str = "Opens a dialog that uses a simple GUI to perform calculations on two numbers."

    @classmethod
    def Register(cls: typing.Type, iconId: int) -> None:
        """Registers the command plugin.

        This is a custom method and not part of the CommandData interface.
        """
        # Load one of the built-in icons of Cinema 4D as the icon of the plugin. You can browse the
        # built-in icons under:
        #
        #   https://developers.maxon.net/docs/py/2023_2/modules/c4d.bitmaps/RESOURCEIMAGE.html
        #
        # You could also load your own icon file here.
        bitmap: c4d.bitmaps.BaseBitmap = c4d.bitmaps.InitResourceBitmap(iconId)

        # The instance of the command that will be registered and will live throughout the whole
        # lifetime of the Cinema 4D session. I.e., commands are effectively singletons (although
        # not formally implemented as such).
        command: object = cls()

        # Register the command. A registration can fail, for example when the ID is already taken.
        # But if this happens, Cinema 4D will print an error message to the console on its own. When
        # we register multiple plugins, it can make sense to stop registering plugins when one of
        # them fails. But we do not need this here, so we just ignore the return value of the
        # RegisterCommandPlugin() function.
        c4d.plugins.RegisterCommandPlugin(
            id=cls.ID_PLUGIN, str=cls.STR_NAME, info=0, icon=bitmap, help=cls.STR_HELP, dat=command)


# Called by Cinema 4D when this plugin module is loaded.
if __name__ == '__main__':
    SimpleGuiCommand.Register(iconId=465001193)
