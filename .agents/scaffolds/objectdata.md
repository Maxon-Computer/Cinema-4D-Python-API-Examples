# ObjectData Scaffold

Scaffolds a Cinema 4D object plugin (`c4d.plugins.ObjectData`) with a description resource for its parameters. Read [scaffolds.md](../scaffolds.md) first, it describes the workflow, the common questions, the placeholders and the rules that apply to all scaffolds.

Folder prefix: `py_obj_`. Resource name prefix: `O`. Registered with: `c4d.plugins.RegisterObjectPlugin` (with the *class*).

`GetVirtualObjects` runs in a threaded context and returns the generator's cache. Build or extrude the output there without modifying the active source objects or document. `ModifyObject` may change only the geometry it is specifically asked to deform; this changes evaluated deformation output, not the source mesh destructively. Use a CommandData or ToolData operation for destructive edits to existing geometry.

# Questions

Ask the common questions (`name`, `description`, `pluginId`) and these:

| Key | Question | Options | Default |
| --- | --- | --- | --- |
| `kind` | What kind of object should it be? | `Generator` (builds polygon or generic geometry from parameters), `Spline generator` (builds a spline), `Deformer` (modifies the points of its parent or siblings) | `Generator` |
| `parameters` | Which parameters should the object have? | See [Parameters](../scaffolds.md#parameters). | Generator: `Size, length, 200`. Spline generator: `Size, length, 200`. Deformer: `Offset, length, 100`. |

The kind decides the registration flags and which methods are generated:

| Kind | Method | `info` flags | Output |
| --- | --- | --- | --- |
| `Generator` | `GetVirtualObjects` | `c4d.OBJECT_GENERATOR` | A sphere that stands in for your geometry. |
| `Spline generator` | `GetContour` | `c4d.OBJECT_GENERATOR \| c4d.OBJECT_ISSPLINE` | A closed square spline. |
| `Deformer` | `ModifyObject` | `c4d.OBJECT_MODIFIER` | Moves the points along the Y axis of the deformer. |

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

`{{ResName}}` is `O` followed by `py{{Slug}}`, e.g., `Opyroundedtube`.

# Templates

## {{Folder}}.pyp

Replace the parts in angle brackets as described below the template.

```python
"""{{Description}}

Create the object by searching for "{{Name}}" in the Commander (Shift + C) or in the Extensions
menu. To run this plugin, add its folder to the plugin paths of Cinema 4D and restart Cinema 4D.

Topics:
    - <TopicForKind>
    - Exposing parameters with a description resource
"""
__author__ = "{{ModelName}}"
__version__ = "{{Version}}"

import c4d
import mxutils

PLUGIN_ID: int = {{PluginId}}

# The ID of a built-in icon, replace it with an own icon when releasing the plugin.
ICON_ID: int = 465001193


class {{ClassName}}Data(c4d.plugins.ObjectData):
    """Implements the {{Name}} object.
    """

    def Init(self, node: c4d.BaseObject, isCloneInit: bool = False) -> bool:
        """Called by Cinema 4D to initialize the parameters of #node.
        """
        # Parameters must be initialized with their type before they can be used.
        <InitAttrLines>

        # Clones copy the values of the original, so only set defaults for new objects.
        if not isCloneInit:
            <DefaultLines>

        return True

    <KindMethod>

    <MessageMethod>


# Called by Cinema 4D when this plugin module is loaded.
if __name__ == "__main__":
    icon: c4d.bitmaps.BaseBitmap = c4d.bitmaps.InitResourceBitmap(ICON_ID)
    c4d.plugins.RegisterObjectPlugin(
        id=PLUGIN_ID, str="{{Name}}", g={{ClassName}}Data, description="{{ResName}}",
        icon=icon, info=<InfoFlags>)
```

- `<TopicForKind>`: `Generating geometry with GetVirtualObjects()`, `Generating a spline with GetContour()` or `Modifying points with ModifyObject()`.
- `<InitAttrLines>`: One line per parameter that is not a button: `self.InitAttr(node, <PythonType>, c4d.{{SLUG}}_<PARAM>)`.
- `<DefaultLines>`: One line per parameter that has a default: `node[c4d.{{SLUG}}_<PARAM>] = <default>`. When the object has no parameters, use `pass`.
- `<InfoFlags>`: From the table above.
- `<MessageMethod>`: Only when the object has `button` parameters, otherwise omit it. Use the button template below.
- Import `mxutils` only when it is used.

### Kind method: Generator

Use the first `float` or `length` parameter as the radius. When there is none, use the literal `100.0`.

```python
    def GetVirtualObjects(self, op: c4d.BaseObject, hh: object) -> c4d.BaseObject | None:
        """Called by Cinema 4D to build the output of the generator, in a threaded context.
        """
        # Reuse the cache when neither the parameters nor the inputs have changed.
        if not (op.CheckCache(hh) or op.IsDirty(c4d.DIRTYFLAGS_DATA)):
            return op.GetCache(hh)

        # A sphere stands in for the generated geometry, replace it with your own.
        sphere: c4d.BaseObject = mxutils.CheckType(c4d.BaseObject(c4d.Osphere))
        sphere[c4d.PRIM_SPHERE_RAD] = op[c4d.{{SLUG}}_<PARAM>]
        sphere.SetName(op.GetName())
        return sphere
```

### Kind method: Spline generator

```python
    def GetContour(self, op: c4d.BaseObject, doc: c4d.documents.BaseDocument, lod: float,
                   bt: c4d.threading.BaseThread) -> c4d.SplineObject | None:
        """Called by Cinema 4D to build the output spline, in a threaded context.
        """
        # A closed square stands in for the generated spline, replace it with your own.
        size: float = op[c4d.{{SLUG}}_<PARAM>]
        spline: c4d.SplineObject = mxutils.CheckType(c4d.SplineObject(4, c4d.SPLINETYPE_LINEAR))
        spline[c4d.SPLINEOBJECT_CLOSED] = True
        spline.SetAllPoints([c4d.Vector(-size, -size, 0), c4d.Vector(size, -size, 0),
                             c4d.Vector(size, size, 0), c4d.Vector(-size, size, 0)])
        spline.Message(c4d.MSG_UPDATE)
        return spline
```

### Kind method: Deformer

```python
    def ModifyObject(self, mod: c4d.BaseObject, doc: c4d.documents.BaseDocument,
                     op: c4d.BaseObject, opMg: c4d.Matrix, modMg: c4d.Matrix, lod: float,
                     flags: int, thread: c4d.threading.BaseThread) -> bool:
        """Called by Cinema 4D for each object that is deformed by #mod.
        """
        points: list[c4d.Vector] = op.GetAllPoints() if op.IsInstanceOf(c4d.Opoint) else []
        if not points:
            return True

        # Move the points in the space of the deformer, and then back into the space of the object.
        matrix: c4d.Matrix = ~modMg * opMg
        invMatrix: c4d.Matrix = ~matrix
        offset: c4d.Vector = c4d.Vector(0, mod[c4d.{{SLUG}}_<PARAM>], 0)
        for index, point in enumerate(points):
            op.SetPoint(index, ((matrix * point) + offset) * invMatrix)

        op.Message(c4d.MSG_UPDATE)
        return True
```

Add `GetDimension` or handles only when the user asks, see `examples/plugins/py_obj_sphere_deformer` and `py_obj_double_circle`.

### Message method for buttons

```python
    def Message(self, node: c4d.BaseObject, msgId: int, data: object) -> bool:
        """Called by Cinema 4D for messages sent to the node, e.g., button clicks.
        """
        # Guard main thread only work, even in a method that is usually called on the main thread.
        if msgId == c4d.MSG_DESCRIPTION_COMMAND and c4d.threading.GeIsMainThreadAndNoDrawThread():
            buttonId: int = data["id"][0].id
            <ButtonBranches>

        return True
```

`<ButtonBranches>`: One `if buttonId == c4d.{{SLUG}}_<BUTTON>:` per button, with `c4d.gui.MessageDialog("<Button name> has been clicked.")` as the body. A button named `Reset` instead resets the defaults: move the content of `<DefaultLines>` into a `SetDefaults(self, node)` method that `Init` and the button call.

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
    <SymbolLines>
    _DUMMY_ELEMENT_
};

#endif
```

`<SymbolLines>`: One line per parameter with an explicit value: `{{SLUG}}_<PARAM> = 10000,` for the first parameter, `{{SLUG}}_<PARAM> = 10001,` for the second and so on. Cycle entries are symbols with the explicit values of the cycle, `{{SLUG}}_<PARAM>_<ENTRY> = 0,`, `{{SLUG}}_<PARAM>_<ENTRY> = 1,`, ... and are written after their parameter. They do not take part in the numbering of the parameters.

## res/description/{{resname}}.res

```text
CONTAINER {{ResName}}
{
    NAME {{ResName}};
    INCLUDE Obase;

    GROUP ID_OBJECTPROPERTIES
    {
        <ParameterLines>
    }
}
```

`<ParameterLines>`: One line per parameter, `<RES_TYPE> {{SLUG}}_<PARAM> { <flags> }` with the data type and flags from the [parameter table](../scaffolds.md#parameters), e.g., `REAL ROUNDEDTUBE_SIZE { UNIT METER; MIN 0.0; }`. Add `INCLUDE Osplineprimitive;` after the group only when the user asks for the standard spline parameters, then the generator must also handle them.

## res/strings_en-US/description/{{resname}}.str

```text
STRINGTABLE {{ResName}}
{
    {{ResName}} "{{Name}}";

    <StringLines>
}
```

`<StringLines>`: `{{SLUG}}_<PARAM> "<Parameter name as entered>";` per parameter and one line per cycle entry.

# After Scaffolding

- Tell the user that the object is found by name in the Commander (Shift + C) and in the Extensions menu, and that resource changes require a restart.
- Mention that the generated geometry is a stand-in and where to replace it.
- Mention that generators, splines and deformers run in a threaded context (see `.agents/scene.md`), and that parameters of the own node must not be modified there.

# References

- [Double Circle](../../examples/plugins/py_obj_double_circle/py_obj_double_circle.pyp): A spline generator with handles.
- [Rounded Tube](../../examples/plugins/py_obj_rounded_tube/py_obj_rounded_tube.pyp): A polygon generator.
- [Sphere Deformer](../../examples/plugins/py_obj_sphere_deformer/py_obj_sphere_deformer.pyp): A deformer with weight map support.
- [Dynamic Parameters](../../examples/plugins/py_obj_dynamic_parameters/py_obj_dynamic_parameters.pyp): Parameters that change at runtime.
- For current resource details, start at <https://developers.maxon.net/docs/py> and search for `Resource Files`.
