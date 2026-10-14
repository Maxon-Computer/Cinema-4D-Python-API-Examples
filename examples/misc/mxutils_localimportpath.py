"""Demonstrates importing a package relative to a saved Python script.

Warning:
    This script must be run from a saved file, in a location where Cinema 4D has read and write access.
"""
__author__ = "Ferdinand Hoppe"
__copyright__ = "Copyright (C) 2026 MAXON Computer GmbH"
__license__ = "Apache-2.0 License"
__version__ = "2027.0"



# --- Boiler plate code to generate a dummy package next to this script ----------------------------

if not __file__:
    raise RuntimeError("This script must be run from a saved file.")

import os

directory: str = os.path.dirname(os.path.abspath(__file__))
package: str = os.path.join(directory, "dummy_package")
module: str = os.path.join(package, "__init__.py")

if not os.path.exists(package):
    os.makedirs(package)

with open(module, "w") as f:
    f.write("def GetMessage() -> str:\n")
    f.write("    return 'Hello from the dummy package!'\n")

# --- Example Start --------------------------------------------------------------------------------

import mxutils

# Cinema, unlike the native CPython interpreter, does not automatically include a script's directory 
# in the module search paths. This includes both myScript.py and myPoly.pyp files. Which in turn means 
# that sibling packages or modules located next to the script are not automatically discoverable. The
# reason why this is being done, is because unlike vanilla CPython, Cinema 4D is a multi user 
# environment, i.e., there can be multiple scripts and plugins (from different authors) running at 
# the same time. If they would all globally modify the module search paths, it could lead to conflicts 
# and unpredictable behavior.
#
# The class mxutils.LocalImportPath fixes this gap, by gracefully exposing a local directory to the 
# module search path, only for the time it is needed within a specific scope.

# Import from the directory containing this script. Instead of a file path, such as "__file__", you 
# could also provide a directory path directly. When a file path is given, it will be internally 
# converted to its containing directory.
with mxutils.LocalImportPath(__file__):
    # Within this scope, we can import modules from the local directory.
    from dummy_package import GetMessage

# And we can then still use them in the enclosing scope, or the entire script when the call was in
# the global scope.
print(GetMessage())

# LocalImportPath also has an #autoReload argument, which especially comes in handy during plugin 
# development. When you hit 'Reload Python' plugins in Cinema 4D, the module dependencies are reloaded 
# automatically if #autoReload is set to True. This feature can detect dependencies of your dependency
# on its own (you import moduleA, which imports moduleB and moduleB), but will try to reload them in
# order of discovery, not necessarily the order in which they are imported in your code. In case a
# specific order is required, you may need to manually reload certain modules to ensure the correct 
# behavior. You should tie the #autoReload argument to a debug flag or a development setting, so that 
# it is only enabled when needed.

# Import the dummy package again, this will entail a console message that it has been reloaded 
# because the module was already imported previously.
IS_DEBUG: bool = True
with mxutils.LocalImportPath(__file__, autoReload=IS_DEBUG):
    import dummy_package