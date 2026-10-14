"""Demonstrates how to build custom menus for your plugins.

The example adds a new menu entry to the 'Extensions' menu and populates it with all Python SDK 
examples that would normally also show up in the 'Extensions' menu. This code would likely not be
a separate plugin in your own project, but rather part of some other plugin module.

The general structure is:

    py_msc_menu/
    ├── res/
    │   ├── strings_us/             # Defines the US English strings for this plugin resource.
    │   │   └── c4d_strings.str 
    │   ├── strings_<language>/     # Another language localization.
    │   │   └── c4d_strings.str      
    │   ├── ...
    │   └── c4d_symbols.h           # Declares resource symbols.
    └── py_msc_menu.pyp             # This plugin.

I.e., it is the normal localized plugin resource structure. See the py_cmd_gui_resources example for 
more details on plugin resources. In this case we use it to define menu section names. To express the
menu commands itself use the PLUGIN_CMD_{ID} structure, to describe a an executable plugin command.
These entries do not have to be localized manually, as Cinema will automatically use the localized 
name of the plugin with the given ID.

The 'trick' for all this to work, is to register the plugins which we want to move from their default
menu location to our own menu with the flag PLUGINFLAG_HIDEPLUGINMENU. This will hide the default 
menu entry of the plugin. We could also not do this, but would then have two menu entries for the 
same plugin, which is allowed, but not what we want in this case.

Registering a hook with a hidden menu entry. All register functions for hooks that have visible menu 
entries support this flag.

    c4d.plugins.RegisterCommandPlugin(
            id=cls.ID_PLUGIN, str=cls.STR_NAME, info=c4d.PLUGINFLAG_HIDEPLUGINMENU, icon=bitmap,
            help=cls.STR_HELP, dat=command)
"""
import os
import typing

import c4d
import mxutils

# Import the plugin resource symbols into the global scope. The if typing.TYPE_CHECKING only exists
# so that a type check does not complain about the symbols not being defined.
mxutils.ImportSymbols(os.path.join(os.path.dirname(__file__), "res"))
if typing.TYPE_CHECKING:
    IDS_PYTHON_SDK: int
    IDS_PYTHON_SDK_COMMANDS: int
    IDS_PYTHON_SDK_OBJECTS: int
    IDS_PYTHON_SDK_TOOLS: int
    IDS_PYTHON_SDK_LICENSING: int


# The menu data for our plugins. This is an entirely custom approach and you could also implement
# this in a different way. But Cinema itself uses fairly similar mechanism (which is not available
# for plugins, be it Python or C++).
MENUDATA: dict = {
    # IDS_PYTHON_SDK_COMMANDS is the label for a sub-menu. We could also place a string here, the
    # menu build below supports both. But by using #IDS_PYTHON_SDK_COMMANDS we tell the menu builder
    # the we want to use a string for this menu entry as defined in the c4d_symbols.h and 
    # c4d_strings.str files. I.e., this menu entry can be localized. See the py_cmd_gui_resources
    # example for more details on plugin resources.
    IDS_PYTHON_SDK_COMMANDS: {  
        # The content of this sub-menu.

        # The items to load. We make here use of the PLUGIN_CMD_{ID} structure, that Cinema's own
        # menu system is using. Cinema will load for such entry the plugin with the corresponding 
        # ID and display its name and icon in the menu. Clicking the item will invoke the plugin.
        "PLUGIN_CMD_1065651": None,   # Py SDK - Hello World Gui
        "PLUGIN_CMD_1065652": None,   # Py SDK - Simple Gui
        "PLUGIN_CMD_1065633": None,   # Py SDK - Dynamic Gui
        "PLUGIN_CMD_10656351": None,  # Py SDK - Persistent Gui
        "PLUGIN_CMD_1065679": None,   # Py SDK - Persistent Gui No Restart
        "PLUGIN_CMD_1065655": None,   # Py SDK - GUI Resources
        "PLUGIN_CMD_1069107": None,   # Py SDK - HTML Gui
        "PLUGIN_CMD_1025249": None,   # Py SDK - Memory Viewer
        "PLUGIN_CMD_1031644": None,   # Py SDK - Sculpt Save Mask
        "PLUGIN_CMD_1037872": None,   # Py SDK - Texture Baker
        "PLUGIN_CMD_1067508": None,   # Py SDK - SDS Weighting Tool
    },
    IDS_PYTHON_SDK_OBJECTS: {
        "PLUGIN_CMD_1025250": None,   # Py SDK - Rounded Tube
        "PLUGIN_CMD_1025245": None,   # Py SDK - Double Circle
        "PLUGIN_CMD_1025252": None,   # Py SDK - Sphere Deformer
        "PLUGIN_CMD_1069813": None,   # Py SDK - Asset Container
        "PLUGIN_CMD_1069202": None,   # Py SDK - Build Flags
        "PLUGIN_CMD_1053134": None,   # Py SDK - Custom Icon Object Data
        "PLUGIN_CMD_1064267": None,   # Py SDK - OCIO Node 2025
        "PLUGIN_CMD_98989801": None,  # Py SDK - Offset Y Spline
        "PLUGIN_CMD_1025246": None,   # Py SDK - Gravitation
        "PLUGIN_CMD_1037871": None,   # Py SDK - Dynamic Parameters Object
        "PLUGIN_CMD_1030505": None,   # Py SDK - Sculpt Modifier Deformer
        "PLUGIN_CMD_1031586": None,   # Py SDK - Serialize

        # An example for a sub-menu and a hardcoded title. 
        "Skin Mesh": {
            "PLUGIN_CMD_1069893": None,   # Py SDK - Skin Mesh
            "PLUGIN_CMD_1069892": None,   # Py SDK - Skin Joint
        },
    },
    IDS_PYTHON_SDK_TOOLS: {
        "PLUGIN_CMD_1025247": None,   # Py SDK - Liquid Painter
        "PLUGIN_CMD_1054512": None,   # Py SDK - ToolData With UI
        "PLUGIN_CMD_1031347": None,   # Py SDK - Grab Brush
        "PLUGIN_CMD_1031348": None,   # Py SDK - Paint Brush
        "PLUGIN_CMD_1031349": None,   # Py SDK - Pull Brush
        "PLUGIN_CMD_1031350": None,   # Py SDK - Twist Brush
    },
    # The licensing examples. This also demonstrates what happens when a plugin is not available which
    # we insert, as that is the case by default for the licensing examples. The menu entry simply will 
    # simply ignored by Cinema when it cannot find the plugin with the given ID. I.e., until the user 
    # ran the license manager and activated a license, three of the four menu entries will not be 
    # available.
    IDS_PYTHON_SDK_LICENSING: {
        "PLUGIN_CMD_1066811": None,   # Py SDK - License Manager
        "PLUGIN_CMD_1066956": None,   # Py SDK - Simple Licensable Command
        "PLUGIN_CMD_1066806": None,   # Py SDK - Licensable Command
        "PLUGIN_CMD_1069915": None,   # Py SDK - Licensable Cube
    },
}


def GetMenuTitle(title: str | int) -> str:
    """Resolves a hard-coded title or a localized plugin resource symbol.
    """
    if isinstance(title, int):
        return c4d.plugins.GeLoadString(title)
    return title


def InsertMenuData(root: c4d.BaseContainer, data: dict) -> None:
    """Recursively converts the menu dictionary #data into Cinema 4D menu resource containers.
    """
    title: int | str
    entries: None | dict
    for title, entries in data.items():
        if entries is None:
            root.InsData(c4d.MENURESOURCE_COMMAND, title)
            continue

        submenu: c4d.BaseContainer = c4d.BaseContainer()
        submenu.InsData(c4d.MENURESOURCE_SUBTITLE, GetMenuTitle(title))
        InsertMenuData(submenu, entries)
        root.InsData(c4d.MENURESOURCE_SUBMENU, submenu)


def ContainsMenu(root: c4d.BaseContainer, title: str) -> bool:
    """Returns whether root already contains a submenu with the given title.
    """
    for _, menuValue in root:
        if not isinstance(menuValue, c4d.BaseContainer):
            continue
        if menuValue.GetString(c4d.MENURESOURCE_SUBTITLE) == title:
            return True
    return False


def UpdateMenu(root: c4d.BaseContainer, data: dict) -> bool:
    """Adds the Python SDK menu once and preserves existing menu entries.
    """
    title: str = GetMenuTitle(IDS_PYTHON_SDK)
    if ContainsMenu(root, title):
        return False

    InsertMenuData(root, {title: data})
    return True


def PluginMessage(mid: int, data: object) -> bool:
    """Adds the Python SDK examples when Cinema 4D builds its menus.
    """
    if mid != c4d.C4DPL_BUILDMENU:
        return False

    # Cinema is asking us to extend the menus. This happens directly after booting or when the user
    # hits the 'Reload Python Plugins' button in the UI.

    # Get the 'Extensions' menu resource (whose symbol is IDS_EDITOR_PIPELINE) and add our menu 
    # entries to it.
    resource: object = c4d.gui.SearchPluginMenuResource("IDS_EDITOR_PIPELINE")
    extensions: c4d.BaseContainer | None = c4d.Cast(None, resource)
    if extensions is None:
        return False

    return UpdateMenu(extensions, MENUDATA)