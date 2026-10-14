# RenderToken Scaffold

Scaffolds a render token, a `$`-style placeholder that Cinema 4D replaces with a string in render and save paths. Read [scaffolds.md](../scaffolds.md) first, it describes the workflow, the common questions, the placeholders and the rules that apply to all scaffolds.

Folder prefix: `py_msc_`. Registered with: `c4d.plugins.RegisterToken` or `c4d.plugins.RegisterHiddenToken`. **Tokens have no plugin ID, do not ask for one.** The scaffold needs no resource files.

# Questions

Ask the common questions `name` and `description` (not `pluginId`) and these:

| Key | Question | Options | Default |
| --- | --- | --- | --- |
| `token` | What is the name of the token? | Free text, lowercase letters and digits only. | `{{Slug}}` |
| `visibility` | Should the token be listed in the render settings? | `Visible`, `Hidden` | `Visible` |

When the token name is already registered, the plugin does not register it a second time, so also check `projects/` and `examples/plugins/` for the name with grep and ask again when it is taken.

# Files

```text
projects/{{Folder}}/
└── {{Folder}}.pyp
```

# Templates

## {{Folder}}.pyp

```python
"""{{Description}}

Use the token "{{token}}" in the paths of the render settings, where it is replaced by the
string that the token function returns. To run this plugin, add its folder to the plugin paths of
Cinema 4D and restart Cinema 4D.

Topics:
    - Registering a render token
    - Replacing a token with an evaluated string
"""
__author__ = "{{ModelName}}"
__version__ = "{{Version}}"

import c4d

TOKEN: str = "{{token}}"


def Evaluate{{ClassName}}(data: c4d.BaseContainer) -> str:
    """Called by Cinema 4D to get the string that replaces the token.

    The container holds the document (index 0), the render data (1), the take (3) and the frame
    (4) of the render, among other values.
    """
    return str(data[4])


# Called by Cinema 4D when this plugin module is loaded.
if __name__ == "__main__":
    # Registering a token twice fails, e.g., when the plugins are reloaded.
    isRegistered: bool = any(
        entry.get("_token") == TOKEN for entry in c4d.modules.tokensystem.GetAllTokenEntries())
    if not isRegistered:
        c4d.plugins.<RegisterFunction>(TOKEN, "{{Name}}", "001", Evaluate{{ClassName}})
```

`<RegisterFunction>`: `RegisterToken` for `Visible`, `RegisterHiddenToken` for `Hidden`.

# After Scaffolding

- Tell the user how to use the token (in the output paths of the render settings, in the notation of the other tokens) and that the example returns the frame number.
- Mention that the token function runs while paths are evaluated, possibly in a threaded context, so it must not modify the scene or use the interface.

# References

- [Render Token](../../examples/plugins/py_msc_render_token/py_msc_render_token.pyp): A visible and a hidden token, with the full list of the values in the data container.
