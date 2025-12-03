"""Demonstrates simple licensing workflow for Python plugins in Cinema 4D.

This example plugin module implements a simple licensing scheme for Python plugins in Cinema 4D. A
command (the licensed plugin) is only registered when a valid license is found. 

Demonstrated features:
  - Simple file based license storage in the user's preferences folder.
  - Restart based activation workflow.
  - Simple hashing scheme for license keys.

Warning:

    This example does not implement a license manager, to generate a valid license key, you have to
    run the more advanced example `py-licensing_2026.pyp` which contains a license manager dialog.
    File based licenses generated with that manager dialog will also apply to this simple example.

See `py-licensing_2026.pyp` for a more advanced licensing example that discusses multiple licensing
concepts in more detail.
"""
__copyright__ = "Copyright 2025, MAXON Computer"
__author__ = "Ferdinand Hoppe"
__date__ = "28/11/2025"
__license__ = "Apache-2.0 license"

import json
import os
import re
import hashlib

import c4d
import maxon
import mxutils

# Import all symbol IDs from the symbols file "res/c4d_symbols.h". The full version has a license
# management dialog that uses these symbols, we use them here to generate and validate license keys.
mxutils.ImportSymbols(os.path.join(os.path.dirname(__file__), "res", "c4d_symbols.h"))

# Because linters such as mypy or pyright (pylance uses pyright) cannot see the imported symbols 
# from the symbols file, we disable undefined variable reporting for this file. We could also do
# this more selectively around the usages of such symbols, see linter documentation for details.
# pyright: reportUndefinedVariable=false

class LicenseType:
    """Represents the different license types that a plugin can have.

    Only used to generate and validate license keys in this simple licensing example.
    """
    UNLICENSED: int = -1
    COMMERCIAL: int = 0
    DEMO: int = 1
    EDUCATIONAL: int = 2
    NFR: int = 3

# --- Start of example plugin implementations ------------------------------------------------------

class SimpleLicensableCommand(c4d.plugins.CommandData):
    """Implements a command that is either being registered or not, depending on the license state.

    This class does not contain any license management logic itself, all is handled in the boot phase
    in this simple version of licensing.
    """
    # Plugin IDs must be unique and obtained from https://developers.maxon.net/.
    ID_PLUGIN: int = 1066956

    def Execute(self, doc: c4d.documents.BaseDocument) -> bool:
        """Called by Cinema 4D when the command is executed.

        Args:
            doc: (c4d.documents.BaseDocument): The current document.

        Returns:
            bool: True on success, otherwise False.
        """
        c4d.gui.MessageDialog("Hello! This command is licensed and working!")
        return True

# --- Start of license management code -------------------------------------------------------------
class LicenseManager(object):
    """Implements a collections of functions to read, write, generate, and validate license keys
    for a plugin.

    This is a boiled down version of a license manager dialog in the more advanced example.
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

    # Local file path for a license within a user's preferences folder.
    LICENSE_FILE_PATH: str = os.path.join("plugins", "py-licensing_2026", "license.key")
    
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
        data: str = c4d.ExportLicenses()
        if not isinstance(data, str) or data.strip() == "":
            raise RuntimeError("Failed to retrieve user license information.")
        
        info: dict = json.loads(data)
        for key in ["name", "surname", "userid", "systemid", "version", "currentproduct", 
                    "accountlicenses"]:
            if key not in info:
                info[key] = LicenseManager.DEFAULT_USER_DATA

        return info
    
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
        serial = serial[:LicenseManager.SERIAL_KEY_LENGTH]
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
    def ValidateSerial(cls, serial: str) -> bool:
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
        
        # Try to read and decrypt the license from a license file. Since this is a simple example, 
        # we do not handle the case of storing the license inside of Cinema 4D itself.
        filePath: str | None = cls.GetLicenseFilePath(writeMode=False)
        data: bytes | None = None
        if filePath:
            os.chmod(filePath, 0o400)
            with open(filePath, "rb") as file:
                data = file.read()
            
            data = cls.EncryptOrDecryptData(data, cls.FILE_ENCRYPTION_KEY.encode("utf-8"))
        else:
            return None
        
        # Validate and return the decrypted license serial.
        serial: str = data.decode("utf-8")
        return serial if cls.ValidateSerial(serial) else None

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
    

# --- Plugin Registration --------------------------------------------------------------------------

def RegisterPlugins() -> bool:
    """Registers the plugin suite and handles licensing in the boot phase.
    """
    # !!! IMPORTANT: We must avoid doing GUI operations in the boot phase, so we should NOT open 
    # a licensing dialog here. Also things such as web requests, loading/running complex libraries, 
    # spawning new threads (or even worse - processes), etc. should be absolutely avoided here. Just 
    # because it works on your machine does not mean it will work for all users in all environments.
    # The earliest point where we can do such things is in the C4DPL_STARTACTIVITY plugin message
    # handled in PluginMessage() above.

    # Check for a valid license by reading any stored license serial and validating it.
    serial: str | None = LicenseManager.ReadLicense()
    isValidLicense: bool = serial is not None

    # Only register the licensed command plugin when we have a valid license. The more advanced
    # workflow would be to always register the plugin, but disable its functionality when no valid
    # license is present. See py-licensing_2026.pyp for such an example.
    if isValidLicense:
        cmdIcon: c4d.bitmaps.BaseBitmap = c4d.bitmaps.InitResourceBitmap(c4d.RESOURCEIMAGE_ARROWLEFT)
        if not c4d.plugins.RegisterCommandPlugin(
            SimpleLicensableCommand.ID_PLUGIN, "Py-SimpleLicensed Command", 0, cmdIcon, 
            "A simple command that requires licensing", SimpleLicensableCommand()):
            raise RuntimeError(f"Failed to register {SimpleLicensableCommand.__class__.__name__} plugin.")

    print(f"Py-Licensing_Simple_2026: {'Valid' if isValidLicense else 'No valid'} license found.")

if __name__ == "__main__":
    # Entry point when Cinema 4D loads the plugin module in the boot phase.
    RegisterPlugins()