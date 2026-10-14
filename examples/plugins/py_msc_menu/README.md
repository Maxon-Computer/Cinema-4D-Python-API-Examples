# Example py_msc_menu

Demonstrates how to build custom menus for your plugins.

## DETAILS

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

## FILES

| File | Description |
| --- | --- |
| [py_msc_menu.pyp](py_msc_menu.pyp) | Demonstrates how to build custom menus for your plugins. |
| [README.md](README.md) | This file. |
| [res/c4d_symbols.h](res/c4d_symbols.h) | Global symbols and identifiers used by the plugin. |
| [res/strings_us/c4d_strings.str](res/strings_us/c4d_strings.str) | The global English language string table used by the plugin. |
