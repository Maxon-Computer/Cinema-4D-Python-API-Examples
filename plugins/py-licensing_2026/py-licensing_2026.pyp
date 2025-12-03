"""Demonstrates multiple licensing workflows for Python plugins in Cinema 4D.

This example plugin module implements two licensable plugins: an object plugin and a command
plugin. Both plugins can be licensed using a license manager dialog that is also implemented
in this module.

Demonstrated features:
  - Internalized license storage.
  - File based license storage.
  - Restart based activation workflow.
  - No-restart based activation workflow.
  - Simple hashing scheme for license keys.
  - Dynamic enabling/disabling of plugin functionality based on licensing state.
  - GUI based license manager dialog.
"""
__copyright__ = "Copyright 2025, MAXON Computer"
__author__ = "Ferdinand Hoppe"
__date__ = "28/11/2025"
__license__ = "Apache-2.0 license"

import hashlib
import json
import os
import re

import c4d
import maxon
import mxutils

# Import all symbol IDs from the symbols file "res/c4d_symbols.h" - which are primarily used by
# the License Manager dialog implementation below.
mxutils.ImportSymbols(os.path.join(os.path.dirname(__file__), "res", "c4d_symbols.h"))

# Because linters such as mypy or pyright (pylance uses pyright) cannot see the imported symbols 
# from the symbols file, we disable undefined variable reporting for this file. We could also do
# this more selectively around the usages of such symbols, see linter documentation for details.
# pyright: reportUndefinedVariable=false

class LicenseType:
    """Represents the different license types that a plugin can have.
    """
    UNLICENSED: int = -1
    COMMERCIAL: int = 0
    DEMO: int = 1
    EDUCATIONAL: int = 2
    NFR: int = 3

# --- Start of example plugin implementations ------------------------------------------------------

# Below you find two minimal plugin implementations that integrate within a licensing workflow;
# which is then implemented in the second section of this file.

class LicensableCubeObject(c4d.plugins.ObjectData):
    """Implements an object that can either be licensed (useable) or unlicensed (not usable) for a
    user, based on a license state.
    
    This example can be applied to all other NodeData derived plugin hooks as well, such as TagData, 
    ShaderData, etc. One must only adapt where the main check is done. Here, in an ObjectData plugin,
    it is done in GetVirtualObjects, whereas in a TagData plugin it would be done in Execute, in a
    ShaderData plugin it would be done in Output, etc.
    """
    # Plugin IDs must be unique and obtained from https://developers.maxon.net/.
    ID_PLUGIN: int = 10803

    # The license type of this object plugin.
    LICENSE_TYPE: int = LicenseType.UNLICENSED

    # An icon representing this object in the object manager when it is unlicensed. We initialize it
    # here once so that we can use it over and over again without reloading it each time.
    ICN_LOCK: c4d.bitmaps.BaseBitmap = c4d.bitmaps.InitResourceBitmap(c4d.RESOURCEIMAGE_UNLOCKED)

    @classmethod
    def IsLicensed(cls) -> bool:
        """Helper method to determine if this plugin is licensed or not.
        """
        return cls.LICENSE_TYPE != LicenseType.UNLICENSED

    def Init(self, op: c4d.GeListNode, isCloneInit: bool) -> bool:
        """Called by Cinema 4D when a new LicensableCube object has been instantiated.
        """
        # Initialize the attributes with their data type each.
        self.InitAttr(op, float, c4d.PY_LICENSABLE_CUBE_HEIGHT)
        self.InitAttr(op, float, c4d.PY_LICENSABLE_CUBE_WIDTH)
        self.InitAttr(op, float, c4d.PY_LICENSABLE_CUBE_DEPTH)

        # Only set the defaults when this is not a clone initialization (as the clone will have its
        # values initialized from the source instance).
        if not isCloneInit:
            op[c4d.PY_LICENSABLE_CUBE_HEIGHT] = 200.0
            op[c4d.PY_LICENSABLE_CUBE_WIDTH] = 200.0
            op[c4d.PY_LICENSABLE_CUBE_DEPTH] = 200.0

        # We cache the last known licensed state so that we can bust our cache when the license 
        # state changes. The better approach would be send messages to all node instances when the
        # license state has changed in LicenseManagerDialog.ActivateLicense. But this would require
        # more complex code, so I went with this simpler approach here.
        self._lastLicensedState: bool = LicensableCubeObject.LICENSE_TYPE
        
        return True

    def GetVirtualObjects(self, op: c4d.BaseObject, hierarchyHelp: object) -> c4d.BaseObject:
        """Called by Cinema 4D to obtain the generated geometry of this object.
        """
        # Check if we need to update the cache or if we can just fall back to the last cache. We 
        # also make our dirty check dependent on the last known licensed state, so that we can
        # bust the cache when the license state changes.
        isDirty: bool = (op.CheckCache(hierarchyHelp) or 
                         op.IsDirty(c4d.DIRTYFLAGS_DATA) or
                         (self._lastLicensedState != LicensableCubeObject.LICENSE_TYPE))
        if not isDirty:
            return op.GetCache()
        
        # Update the last known licensed state.
        self._lastLicensedState = LicensableCubeObject.LICENSE_TYPE

        # Create the root of our cache hierarchy, a null object and a text object with which we
        # indicate the license state
        null: c4d.BaseObject | None = c4d.BaseObject(c4d.Onull)
        text: c4d.BaseObject | None = c4d.BaseObject(c4d.Omgtext)
        if not null or not text:
            return None # Allocation failed, we return None to indicate a memory error.
        
        text.InsertUnder(null)
        text.SetRelPos(c4d.Vector(op[c4d.PY_LICENSABLE_CUBE_WIDTH] + 50, -50, 0))
        
        # Now we return the payload of this plugin, depending on the license state. This could be
        # done analogously for other plugin types as well, such as TagData, ShaderData, etc. We just
        # refuse to do what we are supposed to do when unlicensed. 

        # Our plugin is not licensed, we just return the text object, and not the cube object - our
        # main functionality is disabled in this state.
        if not LicensableCubeObject.IsLicensed():
            text[c4d.PRIM_TEXT_TEXT] = "Unlicensed"
        # The plugin is licensed, we return the cube object as expected.
        else:
            cube: c4d.BaseObject | None = c4d.BaseObject(c4d.Ocube)
            if not cube:
                return None
            
            cube[c4d.PRIM_CUBE_LEN] = c4d.Vector(op[c4d.PY_LICENSABLE_CUBE_WIDTH],
                                                 op[c4d.PY_LICENSABLE_CUBE_HEIGHT],
                                                 op[c4d.PY_LICENSABLE_CUBE_DEPTH])
            cube.InsertUnder(null)

            if text and LicensableCubeObject.LICENSE_TYPE == LicenseType.COMMERCIAL:
                text[c4d.PRIM_TEXT_TEXT] = "Commercial"
            elif text and LicensableCubeObject.LICENSE_TYPE == LicenseType.DEMO:
                text[c4d.PRIM_TEXT_TEXT] = "Demo"
            elif text and LicensableCubeObject.LICENSE_TYPE == LicenseType.EDUCATIONAL:
                text[c4d.PRIM_TEXT_TEXT] = "Educational"
            elif text and LicensableCubeObject.LICENSE_TYPE == LicenseType.NFR:
                text[c4d.PRIM_TEXT_TEXT] = "NFR"
        
        return null
    
    # Now follow multiple approaches to signaling that the plugin is unlicensed or licensed. We 
    # change the icon, the name in the object manager, disable/enable parameters in the attribute
    # manager, and handle the license button. Doing all of these at once is absolute overkill, and
    # in fact you need none of them. But one or two of these techniques can improve the user 
    # experience of your plugins, as the user more clearly understands that the plugin is not usable
    # in its current state.
    def GetDEnabling(self, node: c4d.GeListNode, eid: c4d.DescID, t_data: object, flags: int, 
                     itemdesc: c4d.BaseContainer) -> bool:
        """Called by Cinema 4D to determine if a given parameter should be enabled or disabled,
        i.e., is editable or not, in the attribute manager.
        """
        # Disable all parameters except for the license button when the plugin is not licensed. The
        # user will not be able to change any parameters until the plugin is licensed.
        if not LicensableCubeObject.IsLicensed() and eid[0].id != c4d.PY_LICENSABLE_GET_LICENSE:
            return False
        # Otherwise, enable everything except for the license button.
        elif LicensableCubeObject.IsLicensed() and eid[0].id == c4d.PY_LICENSABLE_GET_LICENSE:
            return False
        
        return True
    
    def Message(self, node: c4d.GeListNode, mid: int, data: object) -> bool:
        """Called by Cinema 4D to notify this plugin about various events.
        """
        # Name addition (not required): A name addition is the muted grey text that is shown behind
        # some object names in the object manager. Here we add "Unlicensed" as name addition when
        # the object is not licensed.
        if mid == c4d.MSG_GETCUSTOM_NAME_ADDITION and not LicensableCubeObject.IsLicensed():
            data["res"] = "Unlicensed"

        # Custom icon (not required): Here we provide a custom icon (a lock) to be shown in the object
        # manager when the object is not licensed. In a real world scenario, it would be better to
        # superimpose a lock icon over the regular icon instead of this a bit brutish replacement.
        elif mid == c4d.MSG_GETCUSTOMICON and not LicensableCubeObject.IsLicensed():
            data["bmp"] = LicensableCubeObject.ICN_LOCK # The new icon for the node instance.
            data["flags"] = c4d.ICONDATAFLAGS_NONE
            data["x"] = 0
            data["y"] = 0
            data["w"] = LicensableCubeObject.ICN_LOCK.GetBw()
            data["h"] = LicensableCubeObject.ICN_LOCK.GetBh()
            data["filled"] = True # must be True to use custom icon
        # Required (at least when you have a license button in the description): We handle the user
        # clicking the "Get License" button in an unlicensed state.
        elif mid == c4d.MSG_DESCRIPTION_COMMAND:
            if data["id"][0].id == c4d.PY_LICENSABLE_GET_LICENSE and c4d.threading.GeIsMainThread():
                LicenseManagerDialog.Run()

        return True
    
# --------------------------------------------------------------------------------------------------

class LicensableCommand(c4d.plugins.CommandData):
    """Implements a command that can either be licensed (useable) or unlicensed (not usable) for a
    user, based on a license state.

    Similar patterns could also be applied to other non NodeData based plugins, such as tools,
    message hooks, bitmap savers, bitmap loaders, scene savers, scene loaders, etc.
    """
    # Plugin IDs must be unique and obtained from https://developers.maxon.net/.
    ID_PLUGIN: int = 1066806

    # The license type of this command plugin.
    LICENSE_TYPE: int = LicenseType.UNLICENSED

    @classmethod
    def IsLicensed(cls) -> bool:
        """Helper method to determine if this plugin is licensed or not.
        """
        return cls.LICENSE_TYPE != LicenseType.UNLICENSED

    def Execute(self, doc: c4d.documents.BaseDocument) -> bool:
        """Called by Cinema 4D when the command is executed.

        Args:
            doc: (c4d.documents.BaseDocument): The current document.

        Returns:
            bool: True on success, otherwise False.
        """
        # This command is not licensed, we do nothing. Because we grey out the command in the menu
        # the user cannot execute it, but sneaky users could invoke the command via a CallCommand.
        # So, it is absolutely necessary to actually check the licensing before performing the 
        # command's action.
        if not LicensableCommand.IsLicensed():
            c4d.gui.MessageDialog("Please license this command to be able to use it.")
            return False

        msg: str = "Running this command in "
        if LicensableCommand.LICENSE_TYPE == LicenseType.COMMERCIAL:
            msg += "Commercial licensed mode."
        elif LicensableCommand.LICENSE_TYPE == LicenseType.DEMO:
            msg += "Demo licensed mode."
        elif LicensableCommand.LICENSE_TYPE == LicenseType.EDUCATIONAL:
            msg += "Educational licensed mode."
        elif LicensableCommand.LICENSE_TYPE == LicenseType.NFR:
            msg += "NFR licensed mode."

        c4d.gui.MessageDialog(msg)
        return True
    
    def GetState(self, doc: c4d.documents.BaseDocument) -> int:
        """Called by Cinema 4D to determine the state of the command.
        """
        # We disable the command in the menus if it is not licensed.
        if not LicensableCommand.IsLicensed():
            return 0 # Disabled state
        
        return c4d.CMD_ENABLED

# --- Start of license management code -------------------------------------------------------------

# Below you will find the code that implements the license handling. I have attached all the logic 
# to the license manager dialog, but you could also abstract this more. Below you can also find
# the command with which the license manager dialog is opened (but it contains nothing special).

class LicenseManagerDialog(c4d.gui.GeDialog):
    """Implements a dialog and the logic that is used by plugins to manage their licensing.

    To exact details of such dialog and logic depend entirely on the plugin and its licensing 
    scheme. This example is more a collection of different concepts where you can pick and choose
    what to implement for your plugins and what not. It is of course also not good for the security
    of your licensing scheme when you follow a public code example to the letter. So, mix up things
    a little!

    The primary things this dialog implements are:

    - Displaying license information to the user (and all the other GUI stuff around that).
    - Accepting a license key from the user and validating it.
    - Retrieving system and user information to bind licenses to.
    - Activating and deactivating licenses.
    - Store licenses both as a file or in the storage of Cinema 4D.
    - A restart and a restart-free license activation workflow.
    - Storing license management settings.
    """
    # A default value used for user data fields when no real user data is available.
    DEFAULT_USER_DATA: str = ""

    # The two secrets for this license manager solution: the salt to hash license keys with, and the
    # file encryption key. THESE MUST BE KEPT A SECRET. I.e., the file which contains this code must
    # be an encrypted .pyp file when you deploy your plugin.
    PLUGIN_SALT: str = "6c336037482b3b0bf3d031f7c38b4b6d"
    FILE_ENCRYPTION_KEY: str = "2899b177e09cfea0482f75237d924772"

    # The number of characters a license key should have. Cannot be larger than 64 characters due 
    # to the SHA-256 hash length and should be at least be 16 characters for collision resistances. 
    # This value expresses the raw number of characters, not including dashes and the prefix.
    SERIAL_KEY_LENGTH: int = 24

    # Local file path for a license within a user's preferences folder (only used when using file
    # based license storage).
    LICENSE_FILE_PATH: str = os.path.join("plugins", "py-licensing_2026", "license.key")

    # Calling c4d.ExportLicenses is somewhat expensive, so we cache the results here since this
    # dialog is modal anyway, so the license state cannot change while the dialog is open.
    EXPORT_LICENSES_CACHE: dict[str, str] = {}

    # The dummy data that is used for displaying (but not calculation) purposes that is used when 
    # USE_DUMMY_DATA is enabled. This primarily exists so that this code example can be documented
    # in screenshots without exposing any real user data. When this is enabled, the solution will
    # still use the real user data for license key calculation, but display the dummy data in the UI.
    USE_DUMMY_DATA: bool = False
    DUMMY_DATA: dict[str, str] = {
        "userid":"e3a1c2d4-7f8b-4a6e-9d2c-3f5b8e1a2c4d",
        "systemid":"QwErTyUiOpAsDfGhJkLzXcVbNm1234567890abCDt",
        "name": "Bobby",
        "surname":"Tables",
        "currentproduct":"net.maxon.license.app.cinema4d-release~commercial",
        "accountlicenses":{
            "net.maxon.license.app.cinema4d-release~commandline-floating": 10,
            "net.maxon.license.app.teamrender-release~commercial-floating": 10,
            "net.maxon.license.app.cinema4d-release~commercial-floating": 10,
            "net.maxon.license.app.cinema4d-release~education-floating": 10,
            "net.maxon.license.app.teamrender-release~education-floating": 10,
            "net.maxon.license.app.teamrender-release~commercial": 5,
            "net.maxon.license.app.cinema4d-release~commercial": 5
        }
    }
    
    # --- Ui Logic ---------------------------------------------------------------------------------

    # This is mostly UI fluff. When you want to read the 'real' license management logic, skip to
    # License Logic ~300 lines below.

    # --- GeDialog Overrides

    def __init__(self) -> None:
        """Initializes the license manager dialog.
        """
        # Used to store the ui values of the data tab, so that we can prevent the user from editing them.
        self._dataTabUiValues: dict[int, str] = {}

    def AskClose(self)-> bool:
        """Called by Cinema 4D when the user tries to close the dialog.
        """
        c4d.gui.StatusClear()
        self.EXPORT_LICENSES_CACHE.clear() # Flush the cache when closing the dialog.
        return False # False means "close the dialog".

    def CreateLayout(self) -> bool:
        """Called by Cinema 4D to populate the UI of the dialog with gadgets.
        """
        # We load our dialog layout entirely from a resource file to keep this example clean. See
        # res/dialogs/dlg_license_manager.res for the layout definition.
        if not self.LoadDialogResource(DLG_LICENSE_MANAGER):
            raise RuntimeError("Failed to load license manager dialog resource.")
        return True

    def InitValues(self) -> bool:
        """Called by Cinema 4D to initialize the dialog once its layout has been created.
        """
        # Get the currently active plugin license, and license management settings as we base some
        # UI states on them.
        license: str | None = self.ReadLicense()
        storageMode, activationMode = self.GetLicenseManagementSettings()

        # Set default values and states.
        self.SetInt32(ID_CMB_LICENSE_TYPE, ID_CMB_LICENSE_TYPE_COMMERCIAL)
        self.SetInt32(ID_CMB_LICENSE_STORAGE_MODE, storageMode)
        self.SetInt32(ID_CMB_LICENSE_ACTIVATION_MODE, activationMode)
        self.Enable(ID_BTN_LICENSE_DEACTIVATE, license is not None)

        # Select the currently active license type when a license is active.
        if license:
            if license.startswith("C"):
                self.SetInt32(ID_CMB_LICENSE_TYPE, ID_CMB_LICENSE_TYPE_COMMERCIAL)
            elif license.startswith("D"):
                self.SetInt32(ID_CMB_LICENSE_TYPE, ID_CMB_LICENSE_TYPE_DEMO)
            elif license.startswith("E"):
                self.SetInt32(ID_CMB_LICENSE_TYPE, ID_CMB_LICENSE_TYPE_EDUCATIONAL)
            elif license.startswith("N"):
                self.SetInt32(ID_CMB_LICENSE_TYPE, ID_CMB_LICENSE_TYPE_NFR)

        # Get the Cinema 4D licensing information (i.e., the license of Cinema 4D itself) and 
        # populate the data tab with it.
        info: dict = self.GetCinemaLicensingData().copy()
        if LicenseManagerDialog.USE_DUMMY_DATA: # Use dummy data for screenshots and documentation.
            info.update(LicenseManagerDialog.DUMMY_DATA)

        if isinstance(info.get("accountlicenses", None), dict):
            licenses: str = "\n".join([f"{key}: {value}" 
                                       for key, value in info["accountlicenses"].items()])
            info["accountlicenses"] = licenses.strip()

        # Set the UI values in the data tab.
        self.SetString(ID_EDT_DATA_SALT, LicenseManagerDialog.PLUGIN_SALT)
        self.SetString(ID_EDT_DATA_FILE_KEY, LicenseManagerDialog.FILE_ENCRYPTION_KEY)
        self.SetString(ID_EDT_DATA_ACCOUNT_LICENSES, info["accountlicenses"])
        self.SetString(ID_EDT_DATA_PRODUCT_ID, info["currentproduct"])
        self.SetString(ID_EDT_DATA_PRODUCT_VERSION, info["version"])
        self.SetString(ID_EDT_DATA_SYSTEM_ID, info["systemid"])
        self.SetString(ID_EDT_DATA_USER_ID, info["userid"])
        self.SetString(ID_EDT_DATA_USER_NAME, info["name"])
        self.SetString(ID_EDT_DATA_USER_SURNAME, info["surname"])

        # Store the ui data, so that we can use it later for preventing the user from editing it.
        self._dataTabUiValues = {
            ID_EDT_DATA_SALT: LicenseManagerDialog.PLUGIN_SALT,
            ID_EDT_DATA_FILE_KEY: LicenseManagerDialog.FILE_ENCRYPTION_KEY,
            ID_EDT_DATA_ACCOUNT_LICENSES: info["accountlicenses"],
            ID_EDT_DATA_PRODUCT_ID: info["currentproduct"],
            ID_EDT_DATA_PRODUCT_VERSION: info["version"],
            ID_EDT_DATA_SYSTEM_ID: info["systemid"],
            ID_EDT_DATA_USER_ID: info["userid"],
            ID_EDT_DATA_USER_NAME: info["name"],
            ID_EDT_DATA_USER_SURNAME: info["surname"]
        }

        # Switch to the license tab by default and set the help text.
        self.SetInt32(ID_TAB_GROUPS, ID_GRP_LICENSE)
        self.UpdateHelpText()

        # Generate and validate the first license key in the dialog (i.e., the active key when there
        # is an active license).
        self.UpdateLicenseKeyInUi()
        self.ValidateLicenseKeyInUi()

        return True
    
    def Message(self, msg: c4d.BaseContainer, result: c4d.BaseContainer) -> int:
        """Called by Cinema 4D to notify this dialog about various events.
        """
        # The user interacted with a gadget in the dialog.
        if msg.GetId() == c4d.BFM_ACTION:
            aid: int = msg.GetInt32(c4d.BFM_ACTION_ID)
            # The user tried to change a data tab value, revert it. This is a bit crude way to 
            # implement a read-only EDITTEXT. We could also use a MULTILINEEDIT which has a read-only
            # mode or a STATICTEXT, but both look a bit odd for what we want to achieve here. The
            # premium solution would be to implement a custom GUI for this.
            if aid in self._dataTabUiValues:
                self.SetString(aid, self._dataTabUiValues[aid])
            # The user switched a tab group, update the help text.
            elif aid == ID_TAB_GROUPS:
                self.UpdateHelpText()
            # The user changed a license generation parameter, update the generated license key and 
            # then run the ui validation right after (changing the check icon accordingly).
            elif aid in (ID_CMB_LICENSE_TYPE, ID_CHK_LICENSE_USE_SYSTEM_ID, 
                         ID_CHK_LICENSE_USE_PRODUCT_ID, ID_BTN_LICENSE_GENERATE):
                self.UpdateLicenseKeyInUi()
                self.ValidateLicenseKeyInUi()
            # The user updated the license key in the activate tab, update
            elif aid == ID_EDT_LICENSE_KEY:
                self.ValidateLicenseKeyInUi()
            # The user changed one of the settings that define how licenses are stored and activated,
            # save the new settings so that they persist over Cinema 4D sessions.
            elif aid in (ID_CMB_LICENSE_STORAGE_MODE, ID_CMB_LICENSE_ACTIVATION_MODE):
                self.SetLicenseManagementSettings()
            # The user either wants either to activate or deactivate a license.
            elif aid == ID_BTN_LICENSE_ACTIVATE:
                self.ActivateLicense()
            elif aid == ID_BTN_LICENSE_DEACTIVATE:
                self.DeactivateLicense()
            
        return super().Message(msg, result)
    
    # --- Custom UI logic

    def UpdateLicenseKeyInUi(self) -> None:
        """Updates the dialog UI to reflect the current license key based on the current generation
        parameters.
        """
        license: str = self.GetSerialFromUi()
        self.SetString(ID_EDT_LICENSE_KEY, license)

    def UpdateHelpText(self) -> None:
        """Updates the help text in the dialog based on the currently selected tab.

        """
        tid: int = self.GetInt32(ID_TAB_GROUPS)
        if tid == ID_GRP_DATA:
            self.SetString(ID_EDT_HELP, c4d.plugins.GeLoadString(IDS_HLP_DATA))
        elif tid == ID_GRP_LICENSE:
            self.SetString(ID_EDT_HELP, c4d.plugins.GeLoadString(IDS_HLP_LICENSE))
    
    def GetSerialFromUi(self) -> str:
        """Generates a license key based on the current dialog UI values.
        """
        # Get the base data and then get all the generation settings.
        info: dict = self.GetCinemaLicensingData()

        # Update the base data with the ui values. Be careful with #ID_CMB_LICENSE_TYPE
        # we encode here directly parameters ID into the license key. I.e., changing any of the
        # #ID_CMB_LICENSE_TYPE enum values would invalidate all previously generated 
        # license keys. The symbol file specifically assigns fixed values to these enum values but
        # when you are squeamish you could also map the symbols to hardcoded values here.
        info["license_type"] = self.GetInt32(ID_CMB_LICENSE_TYPE)
        info["use_system_id"] = self.GetBool(ID_CHK_LICENSE_USE_SYSTEM_ID)
        info["use_product_id"] = self.GetBool(ID_CHK_LICENSE_USE_PRODUCT_ID)

        return self.GenerateSerial(info)

    def ValidateLicenseKeyInUi(self) -> bool:
        """Validates the license key currently shown in the dialog UI by displaying the appropriate 
        icon next to it.
        """
        isValid: bool = self.ValidateSerial(self.GetString(ID_EDT_LICENSE_KEY))

        btn: c4d.gui.BitmapButtonCustomGui | None = self.FindCustomGui(
            ID_ICN_LICENSE_KEY_VALID, c4d.CUSTOMGUI_BITMAPBUTTON)
        
        # The icon to display based on the validation result.
        bmp: c4d.bitmaps.BaseBitmap | None = c4d.bitmaps.InitResourceBitmap(
            c4d.RESOURCEIMAGE_OBJECTMANAGER_STATE2
            if isValid else 
            c4d.RESOURCEIMAGE_OBJECTMANAGER_STATE1)
        
        if None in (btn, bmp):
            raise RuntimeError("Failed to get license validation icon bitmap button or bitmap.")
        if not btn.SetImage(bmp):
            raise RuntimeError("Failed to set license validation icon bitmap.")
        
        self.Enable(ID_BTN_LICENSE_ACTIVATE, isValid)
        btn.Redraw()

    def ActivateLicense(self) -> None:
        """Activates the license key currently shown in the dialog UI.
        """
        if not c4d.threading.GeIsMainThread():
            raise RuntimeError("License activation can only be performed from the main thread.")
        
        # Get and validate the license key from the UI.
        serial: str = self.GetString(ID_EDT_LICENSE_KEY)
        if not self.ValidateSerial(serial):
            raise ValueError("Cannot activate an invalid license key.")
        
        # Get the storage and activation modes from the UI and store the license.
        storageMode: int = self.GetInt32(ID_CMB_LICENSE_STORAGE_MODE)
        activationMode: int = self.GetInt32(ID_CMB_LICENSE_ACTIVATION_MODE)
        self.StoreLicense(serial, storageMode)
        self.Enable(ID_BTN_LICENSE_DEACTIVATE, True) # Enable the deactivate button.

        # Either update the plugins or restart Cinema 4D based on the activation mode; in both cases
        # we close the dialog afterwards.
        if activationMode == ID_CMB_LICENSE_ACTIVATION_MODE_NO_RESTART:
            self.UpdateLicensedPlugins(serial)
            c4d.gui.MessageDialog("License activated.")
            self.Close()
            c4d.EventAdd()
        else:
            if c4d.gui.QuestionDialog(c4d.plugins.GeLoadString(IDS_DLG_RESTART_REQUIRED)):
                self.Close()
                c4d.RestartMe()

    def DeactivateLicense(self) -> None:
        """Deactivates all currently stored licenses.
        """
        if not c4d.threading.GeIsMainThread():
            raise RuntimeError("License deactivation can only be performed from the main thread.")
        
        # Remove the stored license and update the plugins to unlicensed state.
        self.DeleteLicense()
        self.Enable(ID_BTN_LICENSE_DEACTIVATE, False) # Disable the deactivate button.

        # Either update the plugins or restart Cinema 4D based on the activation mode.
        activationMode: int = self.GetInt32(ID_CMB_LICENSE_ACTIVATION_MODE)
        if activationMode == ID_CMB_LICENSE_ACTIVATION_MODE_NO_RESTART:
            self.UpdateLicensedPlugins(None)
            c4d.gui.MessageDialog("License deactivated.")
            self.Close()
            c4d.EventAdd()
        else:
            if c4d.gui.QuestionDialog(c4d.plugins.GeLoadString(IDS_DLG_RESTART_REQUIRED)):
                self.Close()
                c4d.RestartMe()
    
    def SetLicenseManagementSettings(self) -> None:
        """Stores the current license management settings for this plugin.

        When you implement a plugin, you would likely not need this method, as you would just choose
        one of the licensing workflows implemented in this dialog, and hardcode it.
        """
        if not c4d.threading.GeIsMainThread():
            raise RuntimeError("License management settings can only be changed from the main thread.")
        
        # Get the old and new data to determine if anything changed and bail when not.
        oldStorageMode, oldActivationMode = self.GetLicenseManagementSettings()
        newStorageMode: int = self.GetInt32(ID_CMB_LICENSE_STORAGE_MODE)
        newActivationMode: str = self.GetInt32(ID_CMB_LICENSE_ACTIVATION_MODE)
        if (oldStorageMode == newStorageMode and oldActivationMode == newActivationMode):
            return
        
        # Write the new data, we use the plugin ID of our license manager command to store the data
        # under. We could also register a dedicated world plugin for this purpose but this MUST be
        # a registered plugin ID.
        data: c4d.BaseContainer = c4d.BaseContainer()
        data.SetInt32(ID_CMB_LICENSE_STORAGE_MODE, newStorageMode)
        data.SetInt32(ID_CMB_LICENSE_ACTIVATION_MODE, newActivationMode)
        if not c4d.plugins.SetWorldPluginData(LicenseManagerCommand.ID_PLUGIN, data, False):
            raise RuntimeError("Failed to store license management settings.")
        
        # When a restart is required because the activation mode change, ask the user if he/she 
        # wants to restart now.
        if (newActivationMode != oldActivationMode and
            c4d.gui.QuestionDialog(c4d.plugins.GeLoadString(IDS_DLG_RESTART_REQUIRED))):
            self.Close()
            c4d.RestartMe()

    @classmethod
    def GetLicenseManagementSettings(cls) -> tuple[int, int]:
        """Returns the current license management settings for this plugin.

        When you implement a plugin, you would likely not need this method, as you would just choose
        one of the licensing workflows implemented in this dialog, and hardcode it.
        """
        if not c4d.threading.GeIsMainThread():
            raise RuntimeError("License management settings can only be changed from the main thread.")
        
        # Get the plugin data container for our license manager plugin or create a new one when none
        # has been stored yet.
        pid: int = LicenseManagerCommand.ID_PLUGIN
        data: c4d.BaseContainer = c4d.plugins.GetWorldPluginData(pid) or c4d.BaseContainer()
        storageDefault: int = ID_CMB_LICENSE_STORAGE_MODE_FILE
        activationDefault: int = ID_CMB_LICENSE_ACTIVATION_MODE_RESTART
        
        # Validate the entries in the data container, either for a new container or when the 
        # container somehow got corrupted. This might seem a bit paranoid, but for complex plugins
        # it is generally a good idea to validate any BaseContainer data you read from disk or
        # internal Cinema 4D storage. As there might be multiple versions of your plugin and 
        # changing for example #ID_CMB_LICENSE_STORAGE_MODE from a LONG in V1 to a STRING in V2
        # might not fail as obviously as you might think, and you then have a very hard to track 
        # down bug on your hands.
        didUpdate: bool = False
        if (data.FindIndex(ID_CMB_LICENSE_STORAGE_MODE) == c4d.NOTOK or
            data.GetType(ID_CMB_LICENSE_STORAGE_MODE) != c4d.DTYPE_LONG or
            data.GetInt32(ID_CMB_LICENSE_STORAGE_MODE) not in (
                ID_CMB_LICENSE_STORAGE_MODE_FILE,
                ID_CMB_LICENSE_STORAGE_MODE_SYSTEM)):
            data.SetInt32(ID_CMB_LICENSE_STORAGE_MODE, storageDefault)
            didUpdate = True
        if (data.FindIndex(ID_CMB_LICENSE_ACTIVATION_MODE) == c4d.NOTOK or
            data.GetType(ID_CMB_LICENSE_ACTIVATION_MODE) != c4d.DTYPE_LONG or
            data.GetInt32(ID_CMB_LICENSE_ACTIVATION_MODE) not in (
                ID_CMB_LICENSE_ACTIVATION_MODE_RESTART,
                ID_CMB_LICENSE_ACTIVATION_MODE_NO_RESTART)):
            data.SetInt32(ID_CMB_LICENSE_ACTIVATION_MODE, activationDefault)
            didUpdate = True

        if didUpdate:
            if not c4d.plugins.SetWorldPluginData(pid, data, False):
                raise RuntimeError("Failed to store default license management settings.")
            c4d.gui.StatusSetText("Wrote default license management settings.")
        
        storageMode: int = data.GetInt32(ID_CMB_LICENSE_STORAGE_MODE, storageDefault)
        activationMode: int = data.GetInt32(ID_CMB_LICENSE_ACTIVATION_MODE, activationDefault)
        return storageMode, activationMode

    @classmethod
    def Run(cls) -> None:
        """Opens a modal instance of the license manager dialog.
        """
        dlg: LicenseManagerDialog = cls()
        dlg.Open(c4d.DLG_TYPE_MODAL_RESIZEABLE, defaultw=800)
    
    # --- Licensing Logic --------------------------------------------------------------------------

    # Below you will find the actual license management logic. These functions all do not access
    # dialog instance data and could therefore also be abstracted into a separate license manager
    # class if you wanted to. The three primary things which are realized here are: Generating a
    # license key, validating a license key, and storing/retrieving/deleting licenses.

    @classmethod
    def GetCinemaLicensingData(cls) -> dict[str, str]:
        """Returns the current user license information provided by Cinema 4D.

        This is not about the license information of your plugin, but about the license information
        of Cinema 4D itself, which you can use to bind your plugin licenses to.

        Technically, you could also replace this method with your own user management system, e.g.,
        a web service which returns user information based on a login, or just a simple MAC address
        retrieval function. The primary purpose of this method is to retrieve user and system
        information that can be used to bind licenses to.
        """
        # Build the Cinema 4D user information cache when not existing yet. We avoid calling 
        # c4d.ExportLicenses multiple times as it is somewhat expensive to call (as it can involve 
        # web requests). c4d.ExportLicenses will return license information for the current user of 
        # Cinema 4D as a json string, containing data such as the user ID, system ID, product ID,
        # license type, etc.
        if not cls.EXPORT_LICENSES_CACHE:
            data: str = c4d.ExportLicenses()
            if not isinstance(data, str) or data.strip() == "":
                raise RuntimeError("Failed to retrieve user license information.")
            
            info: dict = json.loads(data)
            for key in ["name", "surname", "userid", "systemid", "version", "currentproduct", 
                        "accountlicenses"]:
                if key not in info:
                    info[key] = LicenseManagerDialog.DEFAULT_USER_DATA
            
            cls.EXPORT_LICENSES_CACHE = info
        
        # Return the cached data.
        return cls.EXPORT_LICENSES_CACHE

    @classmethod
    def GenerateSerial(cls, data: dict) -> str:
        """Generates a license key hash from the given license data dictionary.

        What you hash your license keys with is entirely up to you. This code example uses a SHA-256
        hash of a payload string that contains user ID, system ID, product ID, license type, and
        a plugin salt. You could also add more data to the payload, such as an expiry date, or
        custom user data.
        """
        # Validate the data, this is not a place where we want to be loose. A hidden bug could be
        # catastrophic for the licensing scheme.
        userId: str = mxutils.CheckType(data.get("userid"), str)
        systemId: str = mxutils.CheckType(data.get("systemid"), str)
        productId: str = mxutils.CheckType(data.get("currentproduct"), str)
        licenseType: int = mxutils.CheckType(data.get("license_type"), int)
        useSystemId: bool = mxutils.CheckType(data.get("use_system_id"), bool)
        useProductId: bool = mxutils.CheckType(data.get("use_product_id"), bool)
        if "" in (userId.strip(), systemId.strip(), productId.strip()):
            raise ValueError("User ID, System ID, and Product ID must not be empty.")
        
        # ABSOLUTELY NECESSARY: When we would just encode our #licenseType value directly, adding
        # and removing values in the c4d_symbols.h file would change the integer values of the 
        # license type enum and therefore brick all previously generated license keys. To avoid 
        # this, we map the enum values to our class LicenseType values here. Or in less fancy words:
        # You must be sure that the things you encode into the license key do not (accidentally) 
        # change over time.

        # Map the license type values used by the GUI combobox to our internal LicenseType values.
        if licenseType == ID_CMB_LICENSE_TYPE_COMMERCIAL:
            licenseType = LicenseType.COMMERCIAL
        elif licenseType == ID_CMB_LICENSE_TYPE_DEMO:
            licenseType = LicenseType.DEMO
        elif licenseType == ID_CMB_LICENSE_TYPE_EDUCATIONAL:
            licenseType = LicenseType.EDUCATIONAL
        elif licenseType == ID_CMB_LICENSE_TYPE_NFR:
            licenseType = LicenseType.NFR

        if licenseType not in (
            LicenseType.COMMERCIAL, 
            LicenseType.DEMO,
            LicenseType.EDUCATIONAL,
            LicenseType.NFR):
            raise ValueError("Invalid license type.")
        
        # print(f"Generating license key with: \nuserId={userId}\nsystemId={systemId}, "
        #         f"productId={productId}\nlicenseType={licenseType}\n"
        #         f"useSystemId={useSystemId}\nuseProductId={useProductId}")
        
        # Build the payload string that is used to hash the license key.
        payload: str = f"{cls.PLUGIN_SALT}:{userId}:{licenseType}"

        # Bind the license to the system ID, i.e., it will only be valid on the system with this ID.
        if useSystemId: 
            payload += f":{systemId}" 
        # Bind the license to the product ID, i.e., it will only be valid for this product. This is
        # only very rarely sensible as things like a Teams Render client have a different product ID
        # than Cinema 4D application instance.
        if useProductId:
            payload += f":{productId}"

        # Hash the payload to generate the license key and then format it with dashes and the 
        # unencrypted prefixes. The unencrypted prefix allows us to store decoding information in
        # the serial itself. But since this information is also encoded in the hash, changing it
        # cannot be used to tamper with the license key (e.g., change a demo license into a
        # commercial license), it would just invalidate the license key. Alternatives could be to 
        # (a) store that data somewhere else next to the license key (e.g., in the license file 
        # header), or (b) to brute force all possible combinations when validating a license key.
        serial: str = hashlib.sha256(payload.encode("utf-8")).hexdigest().upper()
        serial = serial[:LicenseManagerDialog.SERIAL_KEY_LENGTH]
        serial = "-".join([serial[i:i+4] for i in range(0, len(serial), 4)])

        # Build the plain text prefix that encodes decoding information.
        prefix: str = "C"
        if licenseType == LicenseType.DEMO:
            prefix = "D"
        elif licenseType == LicenseType.EDUCATIONAL:
            prefix = "E"
        elif licenseType == LicenseType.NFR:
            prefix = "N"

        prefix += "1" if useSystemId else "0"
        prefix += "1" if useProductId else "0"
        prefix += "0" # Reserved for future use, one could encode an expiry byte here for 
                      # example. Mostly added so that the prefix has also a fixed length of 4 
                      # characters.

        # When you want to embed an expiry date into the license key, there are multiple ways to do 
        # so. But one could be a 'expiry bins' approach. I.e., you place an expiry byte in the
        # plain text prefix which encodes a fixed length of a license, the 'bin'. E.g., A = 365 
        # days, B = 730 days, D= 14 days, etc. Then, when generating the license key, you just 
        # encode the current date and that expiry byte into the payload. When validating the license 
        # key, you extract the expiry byte from the prefix, and then brute force the key by walking 
        # expiry byte count days backwards from the current date until you either find a matching 
        # license key or run out of days.

        # Return the final license key.
        return f"{prefix}-{serial}"
    
    @classmethod
    def ValidateSerial(cls, serial: str | None) -> bool:
        """Validates the given license key against this running instance of Cinema 4D.
        """
        if not isinstance(serial, str) or serial.strip() == "":
            return False
        
        # Validate the license key format, not really necessary but good to fail fast and makes it
        # easier to access the parts.
        match: re.Match | None = re.match(r"^(C|D|E|N)([0-1]{3})-([A-F0-9]{4}-){5,}[A-F0-9]{1,4}$", 
                                         serial)
        if not match:
            if c4d.threading.GeIsMainThread():
                c4d.gui.StatusSetText("License key format is invalid.")
            return False
        
        # Extract the prefix information from the license key.
        licenseTypeChar: str = match.group(1)
        useSystemId: bool = match.group(2)[0] == "1"
        useProductId: bool = match.group(2)[1] == "1"

        # Map the license type character to our internal LicenseType values.
        licenseType: int = LicenseType.COMMERCIAL
        if licenseTypeChar == "D":
            licenseType = LicenseType.DEMO
        elif licenseTypeChar == "E":
            licenseType = LicenseType.EDUCATIONAL
        elif licenseTypeChar == "N":
            licenseType = LicenseType.NFR

        # Get the current user data from Cinema 4D.
        info: dict = cls.GetCinemaLicensingData()

        # Build the data dictionary required for serial generation.
        data: dict = {
            "userid": info["userid"],
            "systemid": info["systemid"],
            "currentproduct": info["currentproduct"],
            "license_type": licenseType,
            "use_system_id": useSystemId,
            "use_product_id": useProductId
        }

        # Generate the license key from the current data and compare it to the given license key.
        res: bool = cls.GenerateSerial(data) == serial
        if c4d.threading.GeIsMainThread() and not res:
            c4d.gui.StatusSetText("License key is invalid.")

        return res
    
    @classmethod
    def ReadLicense(cls) -> str | None:
        """Returns and validates a stored license serial, or None when no license has been stored.
        """
        # We are doing file operations, ensure we are on the main thread.
        if not c4d.threading.GeIsMainThread():
            raise RuntimeError("License key can only be retrieved from the main thread.")
        
        # Try to read and decrypt the license from a license file.
        filePath: str | None = cls.GetLicenseFilePath(writeMode=False)
        data: bytes | None = None
        if filePath:
            os.chmod(filePath, 0o400)
            with open(filePath, "rb") as file:
                data = file.read()
            
            data = cls.EncryptOrDecryptData(data, cls.FILE_ENCRYPTION_KEY.encode("utf-8"))
        # Try to read the license from the internal Cinema 4D storage instead.
        else:
            data = c4d.plugins.ReadPluginInfo(
                LicenseManagerCommand.ID_PLUGIN, cls.GetLicenseByteSize())
            
            # This is an empty license or no license stored.
            if data is None or data == cls.GetEmptyLicense():
                return None
        
        # Validate and return the decrypted license serial.
        serial: str = data.decode("utf-8")
        return serial if cls.ValidateSerial(serial) else None
    
    @classmethod
    def StoreLicense(cls, licenseKey: str, storageMode: int) -> None:
        """Activates the given license key by storing it in the appropriate location.
        """
        if not c4d.threading.GeIsMainThread():
            raise RuntimeError("License key can only be stored from the main thread.")
        
        # First validate the license key and delete any existing license.
        if not cls.ValidateSerial(licenseKey):
            raise ValueError("Cannot store an invalid license key.")
        
        cls.DeleteLicense()
        
        # Store the license as a file. Here we encrypt the data before writing it to disk, so that
        # it is not stored in plain text.
        if storageMode == ID_CMB_LICENSE_STORAGE_MODE_FILE:
            filePath: str = cls.GetLicenseFilePath(writeMode=True)
            try:
                # Ensure we can write to an already existing file.
                if os.path.isfile(filePath):
                    os.chmod(filePath, 0o600)

                with open(filePath, "wb") as f:
                    data: bytes = cls.EncryptOrDecryptData(
                        licenseKey.encode("utf-8"), cls.FILE_ENCRYPTION_KEY.encode("utf-8"))
                    f.write(data)

                os.chmod(filePath, 0o400) # Ensure only the user can read the file.
            except Exception as e:
                raise RuntimeError(f"Failed to write license file: {e}") from e
        # Store the license in the encrypted Cinema 4D plugin storage. This is a different storage
        # than we used to store the license management settings in above. We also use here the plugin
        # ID of the license manager command to store the data under. For slightly improved security, 
        # it would be better to register a dedicated world plugin for this purpose, but this MUST also
        # be in any case a registered plugin ID.
        #
        # WARNING: While this data is stored encrypted by Cinema 4D, it can be read by anyone who
        # knows the plugin ID used to store it (and the makeup of the data). Therefore, do NOT 
        # store here data that is not otherwise verified. I.e., when you would store here if the 
        # license is a demo or not, and do not verify that in the serial itself, a user could just 
        # change that data and turn a demo license into a commercial license. You could also - other
        # than I did - encrypt the data before storing it here (so that it is double-encrypted).
        elif storageMode == ID_CMB_LICENSE_STORAGE_MODE_SYSTEM:
            data: bytes = licenseKey.encode("utf-8")
            c4d.plugins.WritePluginInfo(LicenseManagerCommand.ID_PLUGIN, data)
        else:
            raise NotImplementedError(f"Unknown license storage mode: {storageMode}")
        
    @classmethod
    def DeleteLicense(cls) -> int:
        """Removes all stored licenses for this plugin and returns the number of removed stored
        licenses.
        """
        if not c4d.threading.GeIsMainThread():
            raise RuntimeError("License key can only be deleted from the main thread.")
        
        # Delete all license files we can find.
        count: int = 0
        preferencesDir: str = maxon.Application.GetUrl(
            maxon.APPLICATION_URLTYPE.PREFS_DIR).GetSystemPath()
        
        # See #GetLicenseFilePath for an explanation of the different preference directories.
        baseDir: str = re.sub(r"(_[pxcsw])$", "", preferencesDir)
        for suffix in ["", "_p", "_x", "_c", "_s", "_w"]:
            dirToCheck: str = baseDir + suffix
            filePath: str = os.path.normpath(os.path.join(dirToCheck, cls.LICENSE_FILE_PATH))
            if os.path.isfile(filePath):
                try:
                    os.chmod(filePath, 0o600) # Ensure we can delete the file.
                    os.remove(filePath)
                    count += 1
                except Exception as e:
                    raise RuntimeError(f"Failed to delete license file: {e}") from e
        # Delete a license stored in Cinema 4D. There is no direct way to delete data stored via
        # WritePluginInfo, so we just overwrite it with an empty license.
        existingLicense: bytes = c4d.plugins.ReadPluginInfo(
                LicenseManagerCommand.ID_PLUGIN, cls.GetLicenseByteSize())
        if existingLicense and existingLicense != cls.GetEmptyLicense():
            c4d.plugins.WritePluginInfo(
                LicenseManagerCommand.ID_PLUGIN, cls.GetEmptyLicense())
            count += 1

        return count

    @classmethod
    def GetLicenseFilePath(cls, writeMode: bool = False) -> str | None:
        """Returns the path to a license file in the user preferences directory.

        This is the file where we store the license when using file-based license storage. There is
        some complexity to this as Cinema 4D has different preference directories for different
        derivates (e.g., Commandline, Teams Render, etc.). And one usually wants some cleverness in
        how a license registered for the main Cinema 4D application is also found when running a
        derivate.
        """
        # We are doing file operations, ensure we are in the main thread.
        if not c4d.threading.GeIsMainThread():
            raise RuntimeError("License file path can only be retrieved from the main thread.")
        
        # Get the user preferences path and build the full path to our license file. We get
        # here the path of the user preferences directory for this specific version of Cinema 
        # 4D which is running. We could also use #GLOBALPREFS_DIR to get the global preferences 
        # directory, i.e., store a license that would apply for multiple versions of Cinema 4D.
        pref: str = maxon.Application.GetUrl(maxon.APPLICATION_URLTYPE.PREFS_DIR).GetSystemPath()

        # Join the prefs path with our local license file path. Please store data at least in the
        # 'plugins' subfolder of the preferences directory, better in a dedicated subfolder for your
        # plugin. When you do what I did here with LICENSE_FILE_PATH, i.e., match the folder name
        # of your plugin, the license file would be placed inside the plugin folder itself when the
        # user uses the preferences to install your plugin.
        filePath: str = os.path.normpath(os.path.join(pref, cls.LICENSE_FILE_PATH))

        # When we are in write mode, i.e., we are about to write to the license file, we can just
        # return the file path directly. We do not care if the file exists or not in this case. We
        # just write a license file specifically for this Cinema 4D derivate that is running.
        if writeMode:
            os.makedirs(os.path.dirname(filePath), exist_ok=True) # Make sure the directory exists.
            return os.path.join(pref, filePath)
        
        # When we are in read mode, i.e., we are about to read the license file, we have to check
        # if the file actually exists and might have to check multiple locations. This is because
        # there exist different preference directories for different Cinema 4D derivates (e.g.,
        # Commandline, Teams Render, etc.). And the user might have only installed the license for 
        # the main Cinema 4D application. We could also fashion this so that writing a license 
        # always writes to all possible derivate preference directories, and this is probably
        # better, but I went with this simpler approach.

        # A license file for this running executable exists, we can just return it.
        if os.path.isfile(filePath):
            return filePath
        
        # Such file does not exist, we try to find a license file for the main Cinema 4D app. The
        # preferences directory paths follow the pattern that all derivates of an installation have
        # the form base[_n] where 'base' is a shared hash and '_n' is an optional suffix for a
        # derivate. E.g., Cinema 4D's main app uses just the base, whereas the Commandline derivate
        # uses "base_x". See the 'Python Libraries Manual' in the docs for more information on this
        # subject.
        match: re.Match | None = re.match(r"^(.*)(_[pxcsw])$", pref)
        if match:
            mainPrefs: str = match.group(1) # The base preference directory without derivate suffix.
            mainLicenseFilePath: str = os.path.normpath(os.path.join(mainPrefs, cls.LICENSE_FILE_PATH))
            if os.path.isfile(mainLicenseFilePath):
                return mainLicenseFilePath
        
        # No license file found.
        return None

    @classmethod
    def UpdateLicensedPlugins(cls, license: str | None) -> None:
        """Updates the license state of all plugins with the passed license serial.

        In a pure restart-only activation mode, you would not need this method, as the plugins would
        only load when licensed (and possibly modified) on startup of Cinema 4D.
        """
        # The approach shown here to update the license state of plugins is simple but requires
        # the license manager and the licensable plugins to be in the same Python module (i.e., 
        # 'pyp' file).

        # Alternative workflows could be plugin messages (sent via c4d.GePluginMessage and received
        # via PluginMessage()) or atom messages (sent via c4d.C4DAtom.Message and received via
        # c4d.NodeData.Message() in your NodeData derived plugin hook).

        # The issue with both message approaches is that that none of these message streams is 
        # sealed. I.e., someone could just listen to these message streams and then replicate for
        # example sending an 'activate all products' message to your plugins without having a valid 
        # license. One could argue that in a 'keep honest users honest' approach this is irrelevant,
        # but it still would be a big flaw. It is best to ship your plugin (suite) in a single 'pyp' 
        # file for robust licensing. Because here you can directly set class variables in your 
        # plugins to enable or disable them, and attackers cannot tamper with these so easily.

        # You could also open an encrypted local socket connection to your licensable plugins
        # and send license updates that way (and with that use multiple pyp files for your license
        # manager and plugins). This would be more robust against tampering, but also more complex 
        # to implement.

        if not c4d.threading.GeIsMainThread():
            raise RuntimeError("License states can only be set from the main thread.")
        
        if license is None: # No license, set unlicensed state.
            LicensableCubeObject.LICENSE_TYPE = LicenseType.UNLICENSED
            LicensableCommand.LICENSE_TYPE = LicenseType.UNLICENSED
        elif not isinstance(license, str) or license.strip() == "":
            raise ValueError("License serial must be a non-empty string.")
        elif license.startswith("C"): # Commercial license.
            LicensableCubeObject.LICENSE_TYPE = LicenseType.COMMERCIAL
            LicensableCommand.LICENSE_TYPE = LicenseType.COMMERCIAL
        elif license.startswith("D"): # Demo license.
            LicensableCubeObject.LICENSE_TYPE = LicenseType.DEMO
            LicensableCommand.LICENSE_TYPE = LicenseType.DEMO
        elif license.startswith("E"): # Educational license.
            LicensableCubeObject.LICENSE_TYPE = LicenseType.EDUCATIONAL
            LicensableCommand.LICENSE_TYPE = LicenseType.EDUCATIONAL
        elif license.startswith("N"): # NFR license.
            LicensableCubeObject.LICENSE_TYPE = LicenseType.NFR
            LicensableCommand.LICENSE_TYPE = LicenseType.NFR
    
    @classmethod
    def EncryptOrDecryptData(cls, data: bytes, secret: bytes) -> bytes:
        """Encrypts or decrypts the given data using the given secret.

        This is used by the file-based license storage to avoid storing the license key in plain text.
        Used is a simple and not secure at all XOR cipher for demonstration purposes. In a real 
        world scenario, you would likely want to use a more robust encryption scheme, possibly using 
        a third party library.
        """
        return bytes([b ^ secret[i % len(secret)] for i, b in enumerate(data)])
    
    @classmethod
    def GetLicenseByteSize(cls) -> int:
        """Returns the expected size of a license key in bytes when stored.
        """
        # A license key is a string of length SERIAL_KEY_LENGTH + a prefix of 4 characters + dashes
        # each 4 characters. 
        digits: int = cls.SERIAL_KEY_LENGTH + 4
        return digits + (digits // 4) - 1
    
    @classmethod
    def GetEmptyLicense(cls) -> bytes:
        """Returns an empty license used to clear any stored license in Cinema 4D.
        """
        return b"0" * cls.GetLicenseByteSize()
    

# --------------------------------------------------------------------------------------------------
    
class LicenseManagerCommand(c4d.plugins.CommandData):
    """Implements the license manager command plugin.

    It is just used to open the license manager dialog from the Cinema 4D menu.
    """
    # Plugin IDs must be unique and obtained from https://developers.maxon.net/.
    ID_PLUGIN: int = 1066811

    def Execute(self, doc: c4d.documents.BaseDocument) -> bool:
        """Called by Cinema 4D when the command is executed.
        """
        LicenseManagerDialog.Run()
        c4d.EventAdd()
        return True

# --- Plugin Messages and Registration -------------------------------------------------------------

# Below you can find the code that registers the plugins and hooks into the plugin message system of
# Cinema 4D. Here is all the code that runs in the boot phase of Cinema 4D or shortly afterwards.

def PluginMessage(mid: int, mdata: object) -> bool:
    """Called by Cinema 4D to notify plugins about stages in the lifecycle of a Cinema 4D session.
    """
    # Cinema 4D has fully booted, C4DPL_STARTACTIVITY is the earliest point where we can do whatever 
    # want want in the API (GUI operations, threading, file I/O, web requests, etc.).
    if mid == c4d.C4DPL_STARTACTIVITY:
        
        # Optionally we can open the license manager dialog automatically when no valid license
        # is found. But be careful with this, as it can be annoying for users if they
        # constantly get prompted to activate a license.
        # if license is None and c4d.gui.QuestionDialog(
        #     "No valid license found for Py-Licensable Plugins. Do you want to open the "
        #     "License Manager now to activate a license?"):
        #     LicenseManagerDialog.Run()

        # What could also be done at this point is to validate a license with a web service to
        # implement online licensing. But this should then be done asynchronously in a separate
        # thread as we are currently on the main thread. Cinema 4D has finished booting but we 
        # should still not let the user wait here for too long.
        
        return True # consume the start activity event.
    
    return False # do not consume other events we do not handle.


def RegisterPlugins() -> bool:
    """Registers the plugin suite and handles licensing in the boot phase.
    """
    # Create the icons for our plugins: a cube, a command icon, and the license manager. 
    cubeIcn: c4d.bitmaps.BaseBitmap = c4d.bitmaps.InitResourceBitmap(c4d.Ocube)
    cmdIcon: c4d.bitmaps.BaseBitmap = c4d.bitmaps.InitResourceBitmap(c4d.RESOURCEIMAGE_ARROWRIGHT)
    licenseIcn: c4d.bitmaps.BaseBitmap = c4d.bitmaps.InitResourceBitmap(13680)

    # Always register the license manager command plugin, so that the user can activate a license.
    if not c4d.plugins.RegisterCommandPlugin(
        LicenseManagerCommand.ID_PLUGIN, "Py-License Manager", 0, licenseIcn, 
        "A dummy license manager command", LicenseManagerCommand()):
        raise RuntimeError(f"Failed to register {LicenseManagerCommand.__class__.__name__} plugin.")

    # !!! IMPORTANT: We must avoid doing GUI operations in the boot phase, so we should NOT open 
    # the licensing dialog here. Also things such as web requests, loading/running complex libraries, 
    # spawning new threads (or even worse - processes), etc. should be absolutely avoided here. Just 
    # because it works on your machine does not mean it will work for all users in all environments.
    # The earliest point where we can do such things is in the C4DPL_STARTACTIVITY plugin message
    # handled in PluginMessage() above.

    # Determine if we should register the plugins or not based on the current license state and
    # activation mode. In a real world scenario, we would not need the GetLicenseManagementSettings() 
    # call as we would just hardcode one desired workflow.
    activationMode: int = LicenseManagerDialog.GetLicenseManagementSettings()[1]
    license: str | None = LicenseManagerDialog.ReadLicense()
    isValidLicense: bool = license is not None

    # Register the licensed plugins either when there is a valid license, or when we are in
    # no-restart activation mode (so that the user can activate a license without restarting).
    if isValidLicense or activationMode == ID_CMB_LICENSE_ACTIVATION_MODE_NO_RESTART:
        # Register the LicensableCube plugin.
        if not c4d.plugins.RegisterObjectPlugin(
            LicensableCubeObject.ID_PLUGIN, "Py-Licensable Cube", LicensableCubeObject, 
            "Olicenseablecube", c4d.OBJECT_GENERATOR|c4d.OBJECT_CUSTOM_NAME_ADDITION, cubeIcn):
            raise RuntimeError(f"Failed to register {LicensableCubeObject.__class__.__name__} plugin.")
        
        # Register the LicensedCommandData plugin.
        if not c4d.plugins.RegisterCommandPlugin(
            LicensableCommand.ID_PLUGIN, "Py-Licensed Command", 0, cmdIcon, 
            "A command that requires licensing", LicensableCommand()):
            raise RuntimeError(f"Failed to register {LicensableCommand.__class__.__name__} plugin.")
    
    # Finally, update the licensed plugins with the current license state. When you would implement
    # your plugin as restart activation only, this would not be necessary.
    LicenseManagerDialog.UpdateLicensedPlugins(license)

    print(f"Py-Licensing_2026: {'Valid' if isValidLicense else 'No valid'} license found.")
    if not isValidLicense:
        print("Py-Licensing_2026: You can activate a license via the 'Py-License Manager' command "
              "in the Plugins menu.")
    
if __name__ == "__main__":
    # Entry point when Cinema 4D loads the plugin module in the boot phase.
    RegisterPlugins()