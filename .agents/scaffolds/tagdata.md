# TagData Scaffold

Scaffolds a Cinema 4D tag plugin (`c4d.plugins.TagData`) with a description resource for its parameters. Read [scaffolds.md](../scaffolds.md) first, it describes the workflow, the common questions, the placeholders and the rules that apply to all scaffolds.

Folder prefix: `py_tag_`. Resource name prefix: `T`. Registered with: `c4d.plugins.RegisterTagPlugin` (with the *class*).

Important: `TagData.Execute` runs during scene evaluation in a threaded context. It may change parameters and matrices of other scene nodes, but it must not modify geometry/topology, run modeling commands such as `SendModelingCommand`, create undo steps, show UI, or insert, move, or remove document nodes. A button can perform a user-invoked operation through the node's `Message` method, guarded with `c4d.threading.GeIsMainThreadAndNoDrawThread()`. For polygon extrusion, use that button-message path or a CommandData/ToolData plugin; use ObjectData only when the extruded result is generated and returned as its cache.

# Questions

Ask the common questions (`name`, `description`, `pluginId`) and these:

| Key | Question | Options | Default |
| --- | --- | --- | --- |
| `stage` | In which execution stage should the tag run? | `Initial`, `Animation`, `Expression`, `Dynamics`, `Generators` | `Expression` |
| `parameters` | Which parameters should the tag have? | See [Parameters](../scaffolds.md#parameters). | `Offset, length, 100` |

Explain the stages in the question text: a tag only sees the results of the stages that ran before it. A tag that reads the cache of a generator must run in the `Generators` stage, with a priority value of `1`. The stage maps to the constants `c4d.CYCLE_INITIAL`, `c4d.CYCLE_ANIMATION`, `c4d.CYCLE_EXPRESSION`, `c4d.CYCLE_DYNAMICS` and `c4d.CYCLE_GENERATORS`.

The demo logic needs a `float` or `length` parameter. When the user defines none, add the parameter `Offset, length, 0` and tell the user.

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

`{{ResName}}` is `T` followed by `py{{Slug}}`, e.g., `Tpylookatcamera`.

# Templates

## {{Folder}}.pyp

```python
"""{{Description}}

Attach the tag to an object with the Tags menu of the Object Manager or by searching for
"{{Name}}" in the Commander (Shift + C). To run this plugin, add its folder to the plugin paths of
Cinema 4D and restart Cinema 4D.

Topics:
    - Implementing a TagData with TagData.Execute()
    - Defining the execution priority of a tag
    - Exposing parameters with a description resource
"""
__author__ = "{{ModelName}}"
__version__ = "{{Version}}"

import c4d
import mxutils

PLUGIN_ID: int = {{PluginId}}

# The ID of a built-in icon, replace it with an own icon when releasing the plugin.
ICON_ID: int = 465001193


class {{ClassName}}Data(c4d.plugins.TagData):
    """Implements the {{Name}} tag.
    """

    def Init(self, node: c4d.BaseTag, isCloneInit: bool = False) -> bool:
        """Called by Cinema 4D to initialize the parameters of #node.
        """
        # Parameters must be initialized with their type before they can be used.
        <InitAttrLines>

        # Clones copy the values of the original, so only set defaults for new tags.
        if not isCloneInit:
            <DefaultLines>

            # Run in the chosen execution stage, a tag only sees the results of earlier stages.
            priority: c4d.PriorityData = mxutils.CheckType(c4d.PriorityData())
            priority.SetPriorityValue(c4d.PRIORITYVALUE_MODE, c4d.CYCLE_<STAGE>)
            priority.SetPriorityValue(c4d.PRIORITYVALUE_PRIORITY, <PriorityValue>)
            node[c4d.EXPRESSION_PRIORITY] = priority

        return True

    def Execute(self, tag: c4d.BaseTag, doc: c4d.documents.BaseDocument, op: c4d.BaseObject,
                bt: c4d.threading.BaseThread, priority: int, flags: int) -> int:
        """Called by Cinema 4D on every scene update, in a threaded context.

        Tags may modify their host object, but must not insert or remove nodes in the document.
        """
        # Moves the host object along its Y axis to the value of the parameter, replace this with
        # the logic of the tag.
        position: c4d.Vector = op.GetRelPos()
        position.y = tag[c4d.{{SLUG}}_<PARAM>]
        op.SetRelPos(position)

        return c4d.EXECUTIONRESULT_OK

    <MessageMethod>


# Called by Cinema 4D when this plugin module is loaded.
if __name__ == "__main__":
    icon: c4d.bitmaps.BaseBitmap = c4d.bitmaps.InitResourceBitmap(ICON_ID)
    c4d.plugins.RegisterTagPlugin(
        id=PLUGIN_ID, str="{{Name}}", info=c4d.TAG_VISIBLE | c4d.TAG_EXPRESSION,
        g={{ClassName}}Data, description="{{ResName}}", icon=icon)
```

- `<InitAttrLines>`, `<DefaultLines>`: As for the [ObjectData scaffold](objectdata.md#templates), with `node` being the tag.
- `<STAGE>`: The chosen stage in uppercase, e.g., `EXPRESSION`. `<PriorityValue>`: `0`, or `1` for the `Generators` stage.
- `<PARAM>`: The first `float` or `length` parameter.
- `<MessageMethod>`: Only when the tag has `button` parameters, otherwise omit it. Use the `Message` template of the [ObjectData scaffold](objectdata.md#message-method-for-buttons) with `node: c4d.BaseTag`.
- Import `mxutils` only when it is used (it is used for the priority).

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

Same structure and rules as for the [ObjectData scaffold](objectdata.md#resdescriptionresnameh), with the include guard `_{{ResName}}_H_`.

## res/description/{{resname}}.res

```text
CONTAINER {{ResName}}
{
    NAME {{ResName}};
    INCLUDE Texpression;

    GROUP ID_TAGPROPERTIES
    {
        <ParameterLines>
    }
}
```

`<ParameterLines>`: As for the [ObjectData scaffold](objectdata.md#resdescriptionresnameres). `Texpression` provides the priority parameter, which is what makes the stage visible in the Attribute Manager.

## res/strings_en-US/description/{{resname}}.str

Same structure as for the [ObjectData scaffold](objectdata.md#resstrings_en-usdescriptionresnamestr).

# After Scaffolding

- Tell the user how to attach the tag (Tags menu of the Object Manager, or the Commander) and that resource changes require a restart.
- Mention the threading rules: `Execute` runs in a threaded context and may change parameters and matrices of other scene nodes, but not geometry/topology or document structure. Button-triggered scene edits belong in `Message`, guarded with `c4d.threading.GeIsMainThreadAndNoDrawThread()` (see `.agents/scene.md`).
- Mention that `Execute` is called on every update, so it should stay fast.

# References

- [Look At Camera](../../examples/plugins/py_tag_look_at_camera/py_tag_look_at_camera.pyp): A tag with a parameter that aligns its host to the camera.
- For execution stages and threading, start at <https://developers.maxon.net/docs/py> and search for `Scene Execution`.
- For current resource details, search the same documentation for `Resource Files`.
