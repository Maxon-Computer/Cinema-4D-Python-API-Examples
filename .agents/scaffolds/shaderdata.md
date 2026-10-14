# ShaderData Scaffold

Scaffolds a Cinema 4D classic material shader plugin (`c4d.plugins.ShaderData`) with a description resource for its parameters. Read [scaffolds.md](../scaffolds.md) first, it describes the workflow, the common questions, the placeholders and the rules that apply to all scaffolds.

Folder prefix: `py_sha_`. Resource name prefix: `X`. Registered with: `c4d.plugins.RegisterShaderPlugin` (with the *class*).

# Questions

Ask the common questions (`name`, `description`, `pluginId`) and these:

| Key | Question | Options | Default |
| --- | --- | --- | --- |
| `parameters` | Which parameters should the shader have? | See [Parameters](../scaffolds.md#parameters). | `Color, color, (1.0, 0.5, 0.0)` and `Strength, float, 1.0` |

The demo logic returns the first `color` parameter multiplied by the first `float` or `length` parameter (when there is one). When the user defines no `color` parameter, add `Color, color` and tell the user.

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

`{{ResName}}` is `X` followed by `py{{Slug}}`, e.g., `Xpyfresnel`.

# Templates

## {{Folder}}.pyp

```python
"""{{Description}}

Use the shader in a channel of a material, e.g., in the color channel, with the shader menu of
the channel. To run this plugin, add its folder to the plugin paths of Cinema 4D and restart
Cinema 4D.

Topics:
    - Implementing a ShaderData with ShaderData.Output()
    - Caching parameters for rendering with ShaderData.InitRender()
    - Exposing parameters with a description resource
"""
__author__ = "{{ModelName}}"
__version__ = "{{Version}}"

import c4d

PLUGIN_ID: int = {{PluginId}}


class {{ClassName}}Data(c4d.plugins.ShaderData):
    """Implements the {{Name}} shader.
    """

    def Init(self, node: c4d.BaseShader, isCloneInit: bool = False) -> bool:
        """Called by Cinema 4D to initialize the parameters of #node.
        """
        # Parameters must be initialized with their type before they can be used.
        <InitAttrLines>

        # Clones copy the values of the original, so only set defaults for new shaders.
        if not isCloneInit:
            <DefaultLines>

        return True

    def InitRender(self, sh: c4d.BaseShader, irs: c4d.modules.render.InitRenderStruct) -> int:
        """Called by Cinema 4D before rendering, parameters are cached here for Output().
        """
        self.values: dict[int, object] = {
            <ValueEntries>
        }
        return c4d.INITRENDERRESULT_OK

    def Output(self, sh: c4d.BaseShader, cd: c4d.modules.render.ChannelData) -> c4d.Vector:
        """Called by Cinema 4D for each shaded point, possibly on many threads at once.

        Do not access the scene or the operating system in here, and do not read parameters from
        the shader, use the values cached in InitRender().
        """
        <OutputLines>


# Called by Cinema 4D when this plugin module is loaded.
if __name__ == "__main__":
    c4d.plugins.RegisterShaderPlugin(
        PLUGIN_ID, "{{Name}}", 0, {{ClassName}}Data, "{{ResName}}", 0)
```

- `<InitAttrLines>`, `<DefaultLines>`: As for the [ObjectData scaffold](objectdata.md#templates), with `node` being the shader.
- `<ValueEntries>`: One line per parameter that is not a button, `c4d.{{SLUG}}_<PARAM>: sh[c4d.{{SLUG}}_<PARAM>],`.
- `<OutputLines>`:

```python
        color: c4d.Vector = self.values[c4d.{{SLUG}}_<COLORPARAM>]
        strength: float = self.values[c4d.{{SLUG}}_<FLOATPARAM>]
        return color * strength
```

  Without a `float` or `length` parameter, return `color` only.

## res/c4d_symbols.h

Same as for the [ObjectData scaffold](objectdata.md#resc4d_symbolsh).

## res/description/{{resname}}.h

Same structure and rules as for the [ObjectData scaffold](objectdata.md#resdescriptionresnameh).

## res/description/{{resname}}.res

```text
CONTAINER {{ResName}}
{
    NAME {{ResName}};
    INCLUDE Xbase;

    GROUP ID_SHADERPROPERTIES
    {
        <ParameterLines>
    }
}
```

`<ParameterLines>`: As for the [ObjectData scaffold](objectdata.md#resdescriptionresnameres).

## res/strings_en-US/description/{{resname}}.str

Same structure as for the [ObjectData scaffold](objectdata.md#resstrings_en-usdescriptionresnamestr).

# After Scaffolding

- Tell the user how to use the shader (shader menu of a material channel) and that resource changes require a restart.
- Mention that `Output` is called in a multi-threaded render context, and that all scene and OS access is forbidden there. Parameters are cached in `InitRender`.
- Mention that the shader returns a flat color and where to replace it with real logic, e.g., with the 3D position in `cd.vd`, see the Fresnel example.

# References

- [Fresnel](../../examples/plugins/py_sha_fresnel/py_sha_fresnel.pyp): A shader that computes a Fresnel response and reports an exception color.
- For current resource details, start at <https://developers.maxon.net/docs/py> and search for `Resource Files`.
