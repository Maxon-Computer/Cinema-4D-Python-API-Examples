"""Demonstrates a dialog with dynamically addable and removable GUI elements.

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

Subjects:
    - Using GeDialog to create a dialog with dynamic content.
    - Using a simple data model abstraction layer to simplify interaction with the dialog. Here
      we realize DynamicGuiDialog.Items as a property that can be set and get, and upon
      setting the property, the dialog will rebuild its UI.
    - Using GeDialog.LayoutFlushGroup() to clear a group of gadgets and LayoutChanged() to notify
      Cinema 4D that the layout has changed.
    - Using GeDialog.AddCustomGui() to add custom GUI elements (here link boxes).
"""
__copyright__ = "Copyright 2025, MAXON Computer"
__author__ = "Ferdinand Hoppe"
__date__ = "06/06/2025"
__license__ = "Apache-2.0 license"

import c4d
import typing


class DynamicGuiDialog(c4d.gui.GeDialog):
    """Implements a dialog with link box gadgets which can be dynamically added and removed at
    runtime.

    This also demonstrates how one can put a data model abstraction layer (or however one wants
    to call such thing) on top of a couple of gadgets, here the link box GUIs.
    """
    # The gadget IDs of the dialog.

    # The three groups.
    ID_GRP_MAIN: int = 1000
    ID_GRP_ELEMENTS: int = 1001
    ID_GRP_BUTTONS: int = 1002

    # The three buttons at the bottom.
    ID_BTN_ADD: int = 2000
    ID_BTN_REMOVE: int = 2001

    # The dynamic elements. They start at 3000 and then go NAME, LINK, NAME, LINK, ...
    ID_ELEMENTS_START: int = 3000
    ID_ELEMENT_NAME: int = 0
    ID_ELEMENT_LINK: int = 1

    # A default layout flag for GUI gadgets and a default gadget spacing.
    DEFAULT_FLAGS: int = c4d.BFH_SCALEFIT | c4d.BFV_SCALEFIT
    DEFAULT_SPACE: tuple[int] = (5, 5, 5, 5)

    # A settings container for a LinkBoxGui instance, these are all default settings, so we could
    # pass the empty BaseContainer instead with the same effect. But here you can tweak the settings
    # of a custom GUI. Since we want all link boxes to look same, this is done as a class constant.
    LINKBOX_SETTINGS: c4d.BaseContainer = c4d.BaseContainer()
    LINKBOX_SETTINGS.SetBool(c4d.LINKBOX_HIDE_ICON, False)
    LINKBOX_SETTINGS.SetBool(c4d.LINKBOX_LAYERMODE, False)
    LINKBOX_SETTINGS.SetBool(c4d.LINKBOX_NO_PICKER, False)
    LINKBOX_SETTINGS.SetBool(c4d.LINKBOX_NODE_MODE, False)

    def __init__(self) -> None:
        """Initializes a DynamicGuiDialog instance.

        Args:
            items (list[c4d.BaseList2D]): The items to init the dialog with.
        """
        super().__init__()

        # The items linked in the dialog.
        self._items: list[c4d.BaseList2D] = []
        # The document of the dialog.
        self._doc: typing.Optional[c4d.documents.BaseDocument] = None
        # If CrateLayout() has run for the dialog or not.
        self._hasCreateLayout: bool = False

    # Our data model, we expose _items as a property, so that we can read and write items from
    # the outside. For basic type gadgets, e.g., string, bool, int, float, etc., there are
    # convenience methods attached to GeDialog like Get/SetString. But there is no GetLink() method.
    # So one must do one of two things:
    #
    #   1. Store all custom GUI gadgets in a list and manually interact with them.
    #   2. Put a little abstraction layer on top of things as I did here. In this case this also
    #      means that the GUI is being rebuilt when the property is set.
    #
    # Calling DynamicGuiDialogInstance.Items will always yield all items in the order as shown in
    # the GUI, and calling myDynamicGuiDialogInstance.Items = [a, b, c] will then show the items
    # [a, b, c] in three link boxes in the dialog. No method is really intrinsically better, but I
    # prefer it like this.
    @property
    def Items(self) -> list[c4d.BaseList2D]:
        """gets all items linked in the link boxes.
        """
        return self._items

    @Items.setter
    def Items(self, value: list[c4d.BaseList2D]) -> None:
        """Sets all items linked in link boxes.
        """
        if not isinstance(value, list):
            raise TypeError(f"Items: {value}")

        # Set the items and get the associated document from the first item.
        self._items = value
        self._doc = value[0].GetDocument() if len(self._items) > 0 else None

        # Update the GUI when this setter is being called after CreateLayout() has already run.
        if self._hasCreateLayout:
            self.PopulateDynamicGroup(isUpdate=True)

    def InitValues(self) -> bool:
        """Called by Cinema 4D once CreateLayout() has ran.

        Not needed in this case.
        """
        return super().InitValues()

    def CreateLayout(self) -> bool:
        """Called once by Cinema 4D when a dialog opens to populate the dialog with gadgets.

        But one is not bound to adding only items from this method; a dialog can be repopulated
        dynamically.
        """
        self._hasCreateLayout = True
        self.SetTitle("Py - Dynamic Gui")

        # Add the static text at the top of the dialog, that explains what the dialog does. This is
        # formally not part of the example and can be ignored.
        self.GroupBorderSpace(*self.DEFAULT_SPACE)
        self.AddMultiLineEditText(
            999, c4d.BFH_SCALEFIT, inith=50,
            style=c4d.DR_MULTILINE_READONLY | c4d.DR_MULTILINE_WORDWRAP | 
                  c4d.DR_MULTILINE_NO_DARK_BACKGROUND | c4d.DR_MULTILINE_NO_BORDER)
        self.SetString(999, "Demonstrates a dialog with a dynamic layout driven by user interaction. "
                       "Press the 'Add' and 'Remove Item' buttons to add and remove items from the "
                       "dialog. Dragging a scene element, e.g., an object, material, or tag into a "
                       "link box will update the label of the link box.")
        # end of helper text

        # Start of the main layout of the dialog.

        # The outmost layout group of the dialog. It has one column and we will only place other
        # groups in it. Items are placed like this:
        #
        #   Main {
        #       a,
        #       b,
        #       c,
        #       ...
        #   }
        #
        self.GroupBegin(id=self.ID_GRP_MAIN,
                        flags=c4d.BFH_SCALEFIT | c4d.BFV_SCALEFIT, cols=1)
        # Set the group spacing of ID_GRP_MAIN to (5, 5, 5, 5)
        self.GroupBorderSpace(*self.DEFAULT_SPACE)

        # An layout group inside #ID_GRP_MAIN, it has two columns and we will place pairs of
        # labels and link boxes in it. The layout is now:
        #
        #   Main {
        #       Elements {
        #           a, b,
        #           c, d,
        #           ... }
        #       b,
        #       c,
        #       ...
        #   }
        #
        self.GroupBegin(id=self.ID_GRP_ELEMENTS,
                        flags=c4d.BFH_SCALEFIT | c4d.BFV_SCALEFIT, cols=2)
        # Set the group spacing of ID_GRP_ELEMENTS to (5, 5, 5, 5).
        self.GroupBorderSpace(*self.DEFAULT_SPACE)
        # Call our PopulateDynamicGroup() method, here with isUpdate=False, so that group
        # ID_GRP_ELEMENTS won't be flushed the first time it is being built. Doing this is the same
        # as moving all the code from PopulateDynamicGroup() to the line below.
        self.PopulateDynamicGroup(isUpdate=False)
        self.GroupEnd()  # ID_GRP_ELEMENTS

        # A second layout group inside ID_GRP_MAIN, it has three columns and will place our buttons
        # in it. The layout is now:
        #
        #   Main {
        #       Elements {
        #           a, b,
        #           c, d,
        #           ... }
        #       Buttons {
        #           a, b, c,
        #           e, f, g,
        #           ...},
        #       c,
        #       ...
        #   }
        #
        self.GroupBegin(id=self.ID_GRP_BUTTONS, flags=c4d.BFH_SCALEFIT, cols=3)
        self.GroupBorderSpace(*self.DEFAULT_SPACE)
        # The two buttons.
        self.AddButton(id=self.ID_BTN_ADD,
                       flags=c4d.BFH_SCALEFIT, name="Add Item")
        self.AddButton(id=self.ID_BTN_REMOVE,
                       flags=c4d.BFH_SCALEFIT, name="Remove Item")
        self.GroupEnd()  # end of ID_GRP_BUTTONS

        self.GroupEnd()  # end of ID_GRP_MAIN

        return super().CreateLayout()

    def PopulateDynamicGroup(self, isUpdate: bool = False):
        """Builds the dynamic part of the GUI.

        This is a custom method that is not a member of GeDialog.

        Args:
            isUpdate (bool, optional): If this is a GUI update event. Defaults to False.

        Raises:
            MemoryError: On gadget allocation failure.
            RuntimeError: On linking objects failure.
        """
        # When this is an update event, i.e., the group #ID_GRP_ELEMENTS has been populated before,
        # flush the items in the group and set the gadget insertion pointer of this dialog to
        # the start of #ID_GRP_ELEMENTS. Everything else done in CreateLayout(), the groups, the
        # buttons, the spacings, remains intact.
        if isUpdate:
            self.LayoutFlushGroup(self.ID_GRP_ELEMENTS)

        # For each item in self._items ...
        for i, item in enumerate(self.Items):
            # Define the current starting id: 3000, 3002, 3004, 3006, ...
            offset: int = self.ID_ELEMENTS_START + (i * 2)

            # Add a static text element containing the class name of #item or "Empty" when the
            # item is None.
            self.AddStaticText(id=offset + self.ID_ELEMENT_NAME,
                               flags=c4d.BFH_LEFT,
                               name=item.__class__.__name__ if item else "Empty")

            # Add a link box GUI, a custom GUI is added by its gadget ID, its plugin ID, here
            # CUSTOMGUI_LINKBOX, and additionally a settings container, here the constant
            # self.LINKBOX_SETTINGS.
            gui: c4d.gui.LinkBoxGui = self.AddCustomGui(
                id=offset + self.ID_ELEMENT_LINK,
                pluginid=c4d.CUSTOMGUI_LINKBOX,
                name="",
                flags=c4d.BFH_SCALEFIT,
                minw=0,
                minh=0,
                customdata=self.LINKBOX_SETTINGS)
            if not isinstance(gui, c4d.gui.LinkBoxGui):
                raise MemoryError("Could not allocate custom GUI.")

            # When item is not a BaseList2D, i.e., None, we do not have to set the link.
            if not isinstance(item, c4d.BaseList2D):
                continue

            # Otherwise try to link #item in the link box GUI.
            if not gui.SetLink(item):
                raise RuntimeError("Failed to set node link from data.")

        if isUpdate:
            self.LayoutChanged(self.ID_GRP_ELEMENTS)

    def AddEmptyItem(self) -> None:
        """Adds a new empty item to the data model and updates the GUI.

        This is a custom method that is not a member of GeDialog.
        """
        self._items.append(None)
        self.PopulateDynamicGroup(isUpdate=True)

    def RemoveLastItem(self) -> None:
        """Removes the last item from the data model and updates the GUI.

        This is a custom method that is not a member of GeDialog.
        """
        if len(self._items) > 0:
            self._items.pop()
            self.PopulateDynamicGroup(isUpdate=True)

    def UpdateItem(self, cid: int):
        """Updates an item in the list of link boxes.

        This is a custom method that is not a member of GeDialog.

        Args:
            cid (int): The gadget ID for which this event was fired (guaranteed to be a link box
                GUI gadget ID unless I screwed up somewhere :D).
        """
        # The index of the link box and therefore index in self._items, e.g., the 0, 1, 2, 3, ...
        # link box GUI / item.
        index: int = int((cid - self.ID_ELEMENTS_START) * 0.5)

        # Get the LinkBoxGui associated with the ID #cid.
        gui: c4d.gui.LinkBoxGui = self.FindCustomGui(
            id=cid, pluginid=c4d.CUSTOMGUI_LINKBOX)
        if not isinstance(gui, c4d.gui.LinkBoxGui):
            raise RuntimeError(
                f"Could not access link box GUI for gadget id: {cid}")

        # Retrieve the item in the link box gui. This can return None, but in this case we are
        # okay with that, as we actually want to reflect in our data model self._items when
        # link box is empty. The second argument to GetLink() is a type filter. We pass here
        # #Tbaselist2d to indicate that we are interested in anything that is a BaseList2D. When
        # would pass Obase (any object), and the user linked a material, the method would return
        # None. If we would pass Ocube, only cube objects would be retrieved.
        item: typing.Optional[c4d.BaseList2D] = gui.GetLink(
            self._doc, c4d.Tbaselist2d)

        # Write the item into our data model and update the GUI.
        self.Items[index] = item
        self.PopulateDynamicGroup(isUpdate=True)

    def Command(self, cid: int, msg: c4d.BaseContainer) -> bool:
        """Called by Cinema 4D when the user interacts with a gadget.

        Args:
            cid (int): The id of the gadget which has been interacted with.
            msg (c4d.BaseContainer): The command data, not used here.

        Returns:
            bool: Success of the command.
        """
        # You could also put a lot of logic into this method, but for an example it might be better
        # to separate out the actual logic into methods to make things more clear.

        # The "Add Item" button has been clicked.
        if cid == self.ID_BTN_ADD:
            self.AddEmptyItem()
        # The "Remove Item" button has been clicked.
        elif cid == self.ID_BTN_REMOVE:
            self.RemoveLastItem()
        # One of the link boxes has received an interaction.
        elif (cid >= self.ID_ELEMENTS_START and 
              (cid - self.ID_ELEMENTS_START) % 2 == self.ID_ELEMENT_LINK):
            self.UpdateItem(cid)

        return super().Command(cid, msg)

    def CoreMessage(self, cid: int, msg: c4d.BaseContainer) -> bool:
        """Called by Cinema 4D when a core event occurs.

        You could use this to automatically update the dialog when the selection state in the 
        document has changed. I did not flesh this one out.
        """
        # When "something" has happened in the, e.g., the selection has changed ...
        # if cid == c4d.EVMSG_CHANGE:
        # items: list[c4d.BaseList2D] = (
        #     self._doc.GetSelection() + self._doc.GetActiveMaterials() if self._doc else [])

        # newItems: list[c4d.BaseList2D] = list(n for n in items if n not in self._items)
        # self.Items = self.Items + newItems

        return super().CoreMessage(cid, msg)


class DynamicGuiCommand (c4d.plugins.CommandData):
    """Realizes the common implementation for a command that opens a foldable dialog.

    It effectively realizes the button to be found in menus, palettes, and the command manager 
    that opens our dialog. Technically, this is the concrete plugin we implement. But it here
    only plays a secondary role to the dialog, where all the logic is implemented.
    """
    # The dialog hosted by the plugin.
    REF_DIALOG: DynamicGuiDialog | None = None

    def GetDialog(self) -> DynamicGuiDialog:
        """Returns the class bound dialog instance.
        """
        # Instantiate a new dialog when there is none.
        if self.REF_DIALOG is None:
            self.REF_DIALOG = DynamicGuiDialog()

        # Return the dialog instance.
        return self.REF_DIALOG

    def Execute(self, doc: c4d.documents.BaseDocument) -> bool:
        """Folds or unfolds the dialog.
        """
        # Get the dialog bound to this command data plugin type.
        dlg: DynamicGuiDialog = self.GetDialog()
        # Fold the dialog, i.e., hide it if it is open and unfolded.
        if dlg.IsOpen() and not dlg.GetFolding():
            dlg.SetFolding(True)
        # Open or unfold the dialog. When we open the dialog, we do it asynchronously, i.e., the
        # user can unfocus the dialog and continue working in Cinema 4D, while the dialog is open.
        # The alternative would be to open a modal dialog, which would force the user to focus the
        # dialog until it is closed. Modal can be useful but cannot be docked in the layout.
        else:
            dlg.Open(c4d.DLG_TYPE_ASYNC, self.ID_PLUGIN, defaultw=300, defaulth=300)
            # When the dialog does not yet have any items, i.e., has never been opened before, we
            # add the currently selected items in the document to the dialog. Due to our abstraction,
            # this will add the necessary GUI gadgets and link the set items in the link boxes.
            if dlg.Items == []:
                dlg.Items = doc.GetSelection()

        return True

    def RestoreLayout(self, secret: any) -> bool:
        """Restores the dialog on layout changes.
        """
        return self.GetDialog().Restore(self.ID_PLUGIN, secret)

    def GetState(self, doc: c4d.documents.BaseDocument) -> int:
        """Sets the command icon state of the plugin.

        With this you can tint the command icon blue when the dialog is open or grey it out when
        some condition is not met (not done here). You could for example disable the plugin when
        there is nothing selected in a scene, when document is not in polygon editing mode, etc.
        """
        # The icon is never greyed out, the button can always be clicked.
        result: int = c4d.CMD_ENABLED

        # Tint the icon blue when the dialog is already open.
        dlg: DynamicGuiDialog = self.GetDialog()
        if dlg.IsOpen() and not dlg.GetFolding():
            result |= c4d.CMD_VALUE

        return result
    
    # The unique ID of the plugin, it must be obtained from developers.maxon.net.
    ID_PLUGIN: int = 1065633

    # The name and help text of the plugin.
    STR_NAME: str = "Py - Dynamic Gui"
    STR_HELP: str = "Opens a dialog whose content a user can change by interacting with it."

    @classmethod
    def Register(cls: typing.Type, iconId: int) -> None:
        """Registers the command plugin.

        This is a custom method and not part of the CommandData interface.
        """
        # Load one of the builtin icons of Cinema 4D as the icon of the plugin, you can browse the
        # builtin icons under:
        #
        #   https://developers.maxon.net/docs/py/2023_2/modules/c4d.bitmaps/RESOURCEIMAGE.html
        #
        # You could also load your own icon file here.
        bitmap: c4d.bitmaps.BaseBitmap = c4d.bitmaps.InitResourceBitmap(iconId)

        # The instance of the command that will is registered and will live throughout the whole
        # lifetime of the Cinema 4D session. I.e., commands are effectively singletons (although
        # not formally implemented as such).
        command: object = cls()

        # Register the command, a registration can fail, for example when the ID is already taken.
        # But if this happens, Cinema 4D will print an error message to the console on its own. When
        # we register multiple plugins, it can make sense to stop registering plugins, when one of
        # them fails. But we do not need this here, so we just ignore the return value of the
        # RegisterCommandPlugin() function.
        c4d.plugins.RegisterCommandPlugin(
            id=cls.ID_PLUGIN, str=cls.STR_NAME, info=0, icon=bitmap, help=cls.STR_HELP, dat=command)

# Called by Cinema 4D when this plugin module is loaded.
if __name__ == '__main__':
    DynamicGuiCommand.Register(iconId=465001193)