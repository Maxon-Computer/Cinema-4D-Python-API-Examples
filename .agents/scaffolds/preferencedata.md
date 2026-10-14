# PreferenceData Scaffold

Scaffolds a page in the Cinema 4D preferences (`c4d.plugins.PreferenceData`) whose values are stored globally in the world container. Read [scaffolds.md](../scaffolds.md) first, it describes the workflow, the common questions, the placeholders and the rules that apply to all scaffolds.

Folder prefix: `py_msc_`. Resource name: `py{{Slug}}` without a node prefix, e.g., `pypreference`. Registered with: `c4d.plugins.RegisterPreferencePlugin` (with the *class*).

# Questions

Ask the common questions (`name`, `description`, `pluginId`) and these:

| Key | Question | Options | Default |
| --- | --- | --- | --- |
| `containerId` | What is your second plugin ID, for the world container that stores the values? Request it at developers.maxon.net. | Free text input of the number only, no preset options, no default. | None |
| `parameters` | Which preferences should the page have? | See [Parameters](../scaffolds.md#parameters). Only `bool`, `int`, `float`, `length` and `string` are supported. | `Enabled, bool, True` and `Count, int, 10` |

The container ID is a second ID in the same ID space as plugin IDs. It must be unique as well, and must differ from `pluginId`. See [Plugin IDs](../scaffolds.md#plugin-ids). Filename parameters are not supported in preference pages, do not offer them.

# Files

```text
projects/{{Folder}}/
├── {{Folder}}.pyp
└── res/
    ├── c4d_symbols.h
    ├── description/
    │   ├── {{resname}}.h
    │   └── {{resname}}.res
    └── strings_en-US/
        └── description/
            └── {{resname}}.str
```

`{{ResName}}` is `py{{Slug}}` and `{{resname}}` is identical to it.

# Templates

## {{Folder}}.pyp

```python
"""{{Description}}

Open the page in the Preferences of Cinema 4D (Edit > Preferences) under "{{Name}}". To run this
plugin, add its folder to the plugin paths of Cinema 4D and restart Cinema 4D.

The values are stored in the world container, so that other code can read them, e.g., with
`c4d.GetWorldContainerInstance().GetContainerInstance(WORLD_CONTAINER_ID)`.

Topics:
    - Registering a custom preference page with PreferenceData
    - Sharing preference values through the world container
"""
__author__ = "{{ModelName}}"
__version__ = "{{Version}}"

import c4d
import mxutils

PLUGIN_ID: int = {{PluginId}}

# The ID of the world container in which the values of the preferences are stored.
WORLD_CONTAINER_ID: int = {{ContainerId}}


class {{ClassName}}Preference(c4d.plugins.PreferenceData):
    """Implements the {{Name}} preference page.
    """

    @staticmethod
    def GetDefaults() -> dict[int, tuple[int, object]]:
        """Returns the data type and the default value of each preference, by parameter ID.
        """
        # The symbols are attributes of the c4d module, once Cinema 4D has parsed the resources.
        return {
            <DefaultEntries>
        }

    @staticmethod
    def GetValues() -> c4d.BaseContainer:
        """Returns the container in the world container that stores the values of the preferences.
        """
        world: c4d.BaseContainer = c4d.GetWorldContainerInstance()
        values: c4d.BaseContainer | None = world.GetContainerInstance(WORLD_CONTAINER_ID)
        if values is None:
            world.SetContainer(WORLD_CONTAINER_ID, c4d.BaseContainer())
            values = world.GetContainerInstance(WORLD_CONTAINER_ID)

        return mxutils.CheckType(values)

    def InitValue(self, paramId: int, description: c4d.Description | None = None) -> None:
        """Defines the type and default value of the preference #paramId.
        """
        dataType, default = self.GetDefaults()[paramId]
        descId: c4d.DescID = c4d.DescID(c4d.DescLevel(paramId, dataType, 0))
        self.InitPreferenceValue(paramId, default, description, descId, self.GetValues())

    def Init(self, node: c4d.GeListNode, isCloneInit: bool = False) -> bool:
        """Called by Cinema 4D to initialize the preference data.
        """
        for paramId in self.GetDefaults():
            self.InitValue(paramId)

        return True

    def GetDDescription(self, node: c4d.GeListNode, description: c4d.Description,
                        flags: int) -> bool | tuple[bool, int]:
        """Called by Cinema 4D when the description, i.e., the interface, is requested.
        """
        if not description.LoadDescription("{{ResName}}"):
            return False

        # Cinema 4D asks for the default values, e.g., when the user resets a preference.
        if flags & c4d.DESCFLAGS_DESC_NEEDDEFAULTVALUE:
            for paramId in self.GetDefaults():
                self.InitValue(paramId, description)

        return True, flags | c4d.DESCFLAGS_DESC_LOADED

    def GetDParameter(self, node: c4d.GeListNode, id: c4d.DescID,
                      flags: int) -> bool | tuple[bool, object, int]:
        """Called by Cinema 4D to read a preference, the value comes from the world container.
        """
        paramId: int = id[0].id
        if paramId not in self.GetDefaults():
            return False

        return True, self.GetValues()[paramId], flags | c4d.DESCFLAGS_GET_PARAM_GET

    def SetDParameter(self, node: c4d.GeListNode, id: c4d.DescID, data: object,
                      flags: int) -> bool | tuple[bool, int]:
        """Called by Cinema 4D to write a preference, the value goes to the world container.
        """
        paramId: int = id[0].id
        if paramId not in self.GetDefaults():
            return False

        # Store the value with the Python type of the default, e.g., bool, int, float or str.
        self.GetValues()[paramId] = type(self.GetDefaults()[paramId][1])(data)
        return True, flags | c4d.DESCFLAGS_SET_PARAM_SET


# Called by Cinema 4D when this plugin module is loaded.
if __name__ == "__main__":
    c4d.plugins.RegisterPreferencePlugin(
        id=PLUGIN_ID, g={{ClassName}}Preference, name="{{Name}}", description="{{ResName}}",
        parentid=0, sortid=0)
```

`<DefaultEntries>`: One line per parameter, `c4d.{{SLUG}}_<PARAM>: (c4d.<DTYPE>, <default>),` with the data type and Python default from the [parameter table](../scaffolds.md#parameters), e.g., `c4d.PYPREFERENCE_ENABLED: (c4d.DTYPE_BOOL, True),`. `length` and `float` preferences use `c4d.DTYPE_REAL`.

## res/c4d_symbols.h

```cpp
#ifndef C4D_SYMBOLS_H__
#define C4D_SYMBOLS_H__

enum
{
    // The global symbols of the plugin, this plugin does not need any.
    _DUMMY_ELEMENT_
};

#endif
```

## res/description/{{resname}}.h

```cpp
#ifndef _{{ResName}}_H_
#define _{{ResName}}_H_

enum
{
    {{SLUG}}_MAIN_GROUP = 999,
    <SymbolLines>
    _DUMMY_ELEMENT_
};

#endif
```

`<SymbolLines>`: As for the [ObjectData scaffold](objectdata.md#resdescriptionresnameh), but numbered from `1000` instead of `10000`. Preferences do not support cycle or button parameters in this scaffold.

## res/description/{{resname}}.res

```text
CONTAINER {{ResName}}
{
    NAME {{ResName}};

    GROUP {{SLUG}}_MAIN_GROUP
    {
        DEFAULT 1;
        COLUMNS 1;

        <ParameterLines>
    }
}
```

`<ParameterLines>`: As for the [ObjectData scaffold](objectdata.md#resdescriptionresnameres), with `ANIM OFF;` added to the flags of every parameter, preferences cannot be animated, e.g., `BOOL PYPREFERENCE_ENABLED { ANIM OFF; }`.

## res/strings_en-US/description/{{resname}}.str

```text
STRINGTABLE {{ResName}}
{
    {{ResName}} "{{Name}}";

    <StringLines>
}
```

`<StringLines>`: `{{SLUG}}_<PARAM> "<Parameter name as entered>";` per parameter.

# After Scaffolding

- Tell the user where the page appears (Edit > Preferences, page `{{Name}}`) and that resource changes require a restart.
- Show how other code reads a value: `c4d.GetWorldContainerInstance().GetContainerInstance(WORLD_CONTAINER_ID)[c4d.{{SLUG}}_<PARAM>]`, and that code outside the plugin must use the container ID, which is the second ID of the plugin.
- Mention that the values live in the world container and not in scene files.
- Offer to enable or disable parameters depending on other parameters by implementing `GetDEnabling`, see the example.

# References

- [Preference](../../examples/plugins/py_msc_preference/py_msc_preference.pyp): A preference page with a checkbox and a number that is enabled by the checkbox.
- For current resource details, start at <https://developers.maxon.net/docs/py> and search for `Resource Files`.
