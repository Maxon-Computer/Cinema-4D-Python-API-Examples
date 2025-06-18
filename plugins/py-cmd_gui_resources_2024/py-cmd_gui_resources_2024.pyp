"""Demonstrates a plugin that uses resources to define its dialog layout and string translations.

Open this dialog example by running the command "Py - Resource Gui" in the Commander (Shift + C). 
The dialog itself is not very complex, but it demonstrates how to use resources to define the layout
of a dialog.

Plugins store their resources in a folder named "res" next to the plugin module (the pyp file in
Python). Such a resource folder can contain a wide variety of resources, but one important aspect
are *.res, *.str, and *.h files, defining description resources (the UI types used by scene elements 
such as materials, objects, and tags), and dialog resources. This example focuses on dialog
resources. A res folder for a plugin using dialog resources could look like this:

    myPlugin/                               # The plugin folder.
    ├── myPlugin.pyp                        # The plugin module.
    └── res/                                # The resources of the plugin.    
        ├── c4d_symbols.h                   # The global symbols of the plugin; here are all non-
        │                                     description, i.e., dialog, IDs defined.
        ├── dialogs/                        # The dialog resources of the plugin; here we can find
        │   |                               # the markup that defines dialogs.
        │   ├── idd_values.res              # A dialog GUI markup file.
        │   └── idd_buttons.res             # Another dialog GUI markup file.
        ├── strings_en-US/                  # The English strings for the plugin used by resources.
        │   ├── dialogs/                    # The English dialog strings for the plugin.  
        │   │   ├── idd_values.str          # The strings for the IDD_VALUES dialog.
        │   │   └── idd_buttons.str         # The strings for the IDD_BUTTONS dialog.
        │   └── c4d_strings.str             # Generic English strings for the plugin.
        └── strings_de-DE/                  # The German strings for the plugin used by resources.
             ...

Cinema 4D currently supports the following languages:

    - en-US: English (default language, fallback when no translation is available; all plugins must
                      have this language defined)
    - ar-AR: Arabic
    - cs-CZ: Czech
    - de-DE: German
    - es-ES: Spanish
    - fr-FR: French
    - it-IT: Italian
    - ja-JP: Japanese
    - ko-KR: Korean
    - pl-PL: Polish
    - pt-BR: Brazilian Portuguese
    - zh-CN: Simplified Chinese

Warning:

    All languages that use non-ASCII characters, such as Chinese, French, and German, require their
    special Unicode characters to be encoded as ASCII escape sequences in the *.str files. E.g.,
    an '品' must become '\u54c1', an 'é' must become '\u00e9', "ä" must become "\u00e4", and so
    on. Cinema 4D offers no built-in tool to do this, but the example script `unicode_encode_strings.py`
    shipped next to this example can be a starting point for a conversion pipeline.

Subjects:

    - Defining dialog resources in a resource file.
    - Loading dialog resources with GeDialog.LoadDialogResource().
    - Loading string translations with c4d.plugins.GeLoadString().
    - Purpose of __res__ in a plugin module and how to manually load a resource.
"""
__copyright__ = "Copyright 2025, MAXON Computer"
__author__ = "Ferdinand Hoppe"
__date__ = "06/06/2025"
__license__ = "Apache-2.0 license"

import os
import typing

import c4d
import mxutils

# There are two ways how we can deal with symbols inside resources (defined for example in a 
# symbols.h file). One way to is to automatically import them like this:

# Import all symbols inside the res folder of this plugin module. E.g., `ID_PLUGIN` in the
# `c4d_symbols.h` file will be available as a global attribute of this module, i.e., you can
# just write `print(ID_PLUGIN)` to print the ID of this plugin. The other way would be to redefine
# the symbols in this module, e.g., `ID_PLUGIN = 1065655`. The advantage of the first way is that
# it automatically updates the symbols when the resource files change, while the second way works 
# better with auto-completion in IDE and linters, since they have no idea about these symbols being
# defined in a resource file.
mxutils.ImportSymbols(os.path.join(os.path.dirname(__file__), "res"))

class ResourceGuiDialog(c4d.gui.GeDialog):
    """Realizes the most basic dialog possible.
    """
    # Define the button IDs.


    def CreateLayout(self) -> bool:
        """Called by Cinema 4D when the GUI of the dialog is being built.
        """
        self.GroupBorderSpace(5, 5, 5, 5)  # A 5px border around the dialog. 

        # Load the dialog resource #IDD_VALUES exposed in the resources of this plugin module.
        # By default, a __res__ resource is exposed in a plugin module, which is uses when
        # resource bound methods such as LoadDialogResource() are called. But these methods
        # usually also accept a manually allocated GeResource object. Referenced insides 
        # resources are then entities via their symbol/ID, i.e., here the IDD_VALUES we imported
        # above with mxutils.ImportSymbols.
        self.LoadDialogResource(IDD_VALUES)

        # The cool thing about LoadDialogResource() is that this does not finalize the dialog, it 
        # just loads the resource and leaves us with the gadget pointer advanced to the last 
        # element in loaded in by the dialog resource. We can now continue with manual in code
        # methods to add gadgets to the dialog, or even call LoadDialogResource() again to
        # load another dialog resource, which will then be appended to the current dialog.

        # Add a horizontal separator to the dialog, and then load the IDD_BUTTONS dialog resource
        # which contains the three buttons we want to add to the dialog. This is a common pattern
        # used internally, that dialogs are split into components which are then mixed and matched
        # at runtime to create the final dialog.

        self.AddSeparatorH(1)
        self.LoadDialogResource(IDD_BUTTONS)

        # When we manually add gadgets or just define strings, we can still use the values defined
        # in a resource. We load here the title of the dialog from the plugin resource. 
        # GeLoadString() will load a string in the current language, or fall back to en-US when 
        # the plugin has no resources defined for the current language of Cinema 4D.

        # We reuse the name of the plugin as the title of the dialog.
        self.SetTitle(c4d.plugins.GeLoadString(IDS_PLUGIN_NAME))

        return True
    
    def InitValues(self) -> bool:
        """Called by Cinema 4D to initialize the values dialog once its GUI has bee built.
        """
        # Set the initial values of the two input fields to 0.0, which are defined in the IDD_VALUES
        # dialog resource loaded above.
        self.SetFloat(IDC_VALUE_A, 42.0)
        self.SetFloat(IDC_VALUE_B, 3.14159)

        return True

    def Command(self, mid: int, data: c4d.BaseContainer) -> bool:
        """Called by Cinema 4D when the user clicked a gadget in the dialog.
        """
        # The "Add" and "Subtract" buttons have been clicked. To interact with the dialog, we
        # rely on the IDs defined in the resources, which are imported above with
        # mxutils.ImportSymbols().
        if mid in (IDC_ADD, IDC_SUBTRACT):
            a: float = self.GetFloat(IDC_VALUE_A)
            b: float = self.GetFloat(IDC_VALUE_B)
            res: float = a + b if mid == IDC_ADD else a - b
            c4d.gui.MessageDialog(
                f"{a} {'+' if mid == IDC_ADD else '-'} {b} = {res}")

        return True

    
class ResourceGuiCommand (c4d.plugins.CommandData):
    """Realizes the common implementation for a command that opens a foldable dialog.

    This example also reduces the CommandData implementation to its bare minimum, but it is 
    strongly recommend to follow the more complete pattern shown in other examples, such as
    py-cmd_gui_simple.
    """
    # The dialog hosted by the plugin.
    REF_DIALOG: ResourceGuiDialog | None = None

    def Execute(self, doc: c4d.documents.BaseDocument) -> bool:
        """Opens the dialog when the command is executed.
        """
        # Instantiate the dialog if it does not exist yet.
        if ResourceGuiCommand.REF_DIALOG is None:
            ResourceGuiCommand.REF_DIALOG = ResourceGuiDialog()

        # Open the dialog when it is not yet open. We could also implement closing the dialog, see
        # one of the more complex examples for this, such as py-cmd_gui_simple. We open the dialog
        # asynchronously, i.e., the user can continue working in Cinema 4D while the dialog is open.
        if not ResourceGuiCommand.REF_DIALOG.IsOpen():
            ResourceGuiCommand.REF_DIALOG.Open(
                c4d.DLG_TYPE_ASYNC, ID_PLUGIN, defaultw=1, defaulth=1)

        return True
    
    # Here we hardcode the plugin ID, name, and help text in other code examples, but when we use 
    # resources, we can also load these values from the plugin resources. So, we do not need
    # this section anymore, ID_PLUGIN is defined in the c4d_symbols.h file and imported
    # automatically by mxutils.ImportSymbols() above, and the name and help text are defined in
    # the plugin resources and can be loaded with c4d.plugins.GeLoadString().

    # ID_PLUGIN: int = ...
    # STR_NAME: str = ...
    # STR_HELP: str = ...

    @classmethod
    def Register(cls: typing.Type, iconId: int) -> None:
        """Registers the command plugin.

        This is a custom method and not part of the CommandData interface.
        """
        # Load one of the builtin icons of Cinema 4D as the icon of the plugin. Then instantiate the
        # command plugin that will be registered. And finally register the command plugin with that
        # command instance and icon.
        bitmap: c4d.bitmaps.BaseBitmap = c4d.bitmaps.InitResourceBitmap(iconId)
        command: object = cls()

        name: str = c4d.plugins.GeLoadString(IDS_PLUGIN_NAME)
        help: str = c4d.plugins.GeLoadString(IDS_PLUGIN_HELP)

        c4d.plugins.RegisterCommandPlugin(
            id=ID_PLUGIN, str=name, info=0, icon=bitmap, help=help, dat=command)


# Called by Cinema 4D when this plugin module is loaded.
if __name__ == '__main__':
    # When we use resources, we should make sure that the resource for our plugin is loaded before
    # we register and load the plugin. Cinema 4D will usually do this automatically, but it is
    # common practice to check as this can fail. What is shown here is also the pattern necessary 
    # to use resources in other modules (where Cinema 4D does not automatically expose it) or when
    # we specifically want to load resources from a different path than the default one. It is very
    # much recommended to not load the same resources multiple times. I.e., multiple plugin modules
    # working in tandem should share the same resource object.

    # Check if there is a GeResource object available in the global scope under the name `__res__`.
    res: c4d.plugins.GeResource | None = globals().get("__res__", None)
    if not isinstance(res, c4d.plugins.GeResource):
        # Attempt to initialize the resource object from the res folder of this plugin module.
        res = c4d.plugins.GeResource()
        if not res.Init(os.path.join(os.path.dirname(__file__), "res")):
            raise RuntimeError("Failed to initialize the plugin resources.")
        # Write to __res__ so that functions using this default resource can access it.
        __res__ = res

    # Register our plugin as usual.
    ResourceGuiCommand.Register(iconId=465001193)
