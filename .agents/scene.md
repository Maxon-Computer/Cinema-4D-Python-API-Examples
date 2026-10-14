# Scene Documentation

A Cinema 4D scene is a `c4d.documents.BaseDocument` that stores objects, materials, render settings, layers, takes, scene hooks, and, attached to the objects themselves, tags and animation tracks. This document describes how a scene is organized, how to read and change it safely, and when code may touch it. For current API details, start at <https://developers.maxon.net/docs/py> and search for the `Scene Structure` and `Scene Execution` manuals.

# TOC

- [Concepts](#concepts): Describes nodes, hierarchies, branches, caches and the update cycle.
- [Rules](#rules): Hard rules for writing scene code.
- [Threading](#threading): Which operations are allowed where, and how to defer work to the main thread.
- [Recipes](#recipes): Short patterns for the most common tasks.
- [Examples](#examples): Runnable examples for scene topics.

# Concepts

- **Nodes**: `c4d.GeListNode` is the base type of almost everything a scene consists of: documents, objects, tags, materials, shaders, tracks and more. `c4d.BaseList2D` extends it with names, parameters, tags and tracks. `c4d.BaseObject`, `c4d.BaseTag`, `c4d.BaseMaterial` and `c4d.BaseShader` derive from `BaseList2D`.
- **Hierarchies**: Nodes are linked as lists and trees: `GetUp()` (parent), `GetDown()` (first child), `GetNext()`, `GetPred()`. A node is part of exactly one hierarchy, and a hierarchy only holds nodes of one kind.
- **Branches**: A node can expose additional hierarchies of other nodes, rooted in a `c4d.GeListHead`. The node that owns the heads is the *owner* (`GetMain()`), e.g., the document owns the branches Objects (`Obase`), Materials (`Mbase`), Render Settings (`Rbase`), Layers (`Olayer`) and Scene Hooks (`SHplugin`), and an object owns Tags (`Tbase`) and Tracks (`CTbase`). The parent of a node and its owner are different things. `node.GetBranchInfo(c4d.GETBRANCHINFO_NONE)` lists the branches of a node. Most owners offer shortcuts: `doc.GetFirstObject()`, `doc.GetFirstMaterial()`, `doc.GetFirstRenderData()`, `doc.GetLayerObjectRoot()`, `obj.GetFirstTag()`, `obj.GetTags()`, `node.GetCTracks()`, `mat.GetFirstShader()`.
- **Caches**: A generator, such as a Cube, an Array or a Cloner, does not contain polygons itself. When the scene is executed, it builds its output and stores it as its cache (`GetCache()`). A cache is neither a child nor in a branch of the generator, `GetUp()` of a cache returns `None`, the way back is `GetCacheParent()`. The cache of a generator with multiple outputs is a Null object with a hierarchy below it, and clones in that hierarchy can have caches themselves. Deformers do not change the cache, they store their result in the *deform cache* (`GetDeformCache()`) of the deformed object. Caches are read-only, and a generator has no cache before the document has been executed once.
- **Scene Graph**: Hierarchies, branches and caches together form the scene graph, a tree of trees. A new empty document already contains dozens of nodes, most of them scene hooks. What the user sees in the managers is only a small part of it.
- **Update Cycle**: Updates are requested and run later. `c4d.EventAdd()` only sets a flag that the main thread handles after the calling function has returned, multiple calls merge into one update. A new update cancels a running one. The execution runs elements by *priority* (stages Initial, Animation, Expression, Dynamics, Generators), with ties broken by Object Manager order, and **an element only sees the results of the stages that ran before it**. A tag at the default Expression stage that reads `GetCache()` sees the generator output of the *previous* update.
- **Entry points and callbacks**: Python code is either an *entry point* (script, command, dialog) that runs on the main thread between updates, or a *callback* (`Execute` of a tag, `GetVirtualObjects` of a generator, all `Draw` methods, Python Generator and Python Tag `main()`) that Cinema 4D calls during an update on a thread of its choosing. Callbacks run in a *threaded context*. Of all node methods, only `Message` is usually called on the main thread.

# Rules

- IMPORTANT: Never assume that code runs on the main thread, except in a Script Manager script. Guard everything that is main thread only with `c4d.threading.GeIsMainThreadAndNoDrawThread()`, even in methods documented to run on the main thread. See [Threading](#threading).
- NodeData evaluation callbacks such as `TagData.Execute`, `ObjectData.GetVirtualObjects`, `ObjectData.ModifyObject` and `ShaderData.Output` run in threaded contexts. They cannot structurally modify the active document, create undo steps, show UI, or run modeling commands against source scene data. `TagData.Execute` has a narrow exception: it may modify parameters and matrices of other scene nodes, but not their geometry/topology or document structure, and must not modify its own tag in a way that creates an update feedback loop. Use a guarded node `Message` callback for button-triggered main-thread operations. `ObjectData.GetVirtualObjects` builds and returns generated cache content; `ObjectData.ModifyObject` may change only the geometry it is specifically asked to deform. These are evaluated outputs, not destructive edits to source scene objects.
- In Script Manager scripts use the predefined `doc` and `op` attributes, do not call `c4d.documents.GetActiveDocument()` or `doc.GetActiveObject()`. In other contexts use the document that is passed to you, or `node.GetDocument()`.
- Guard allocations with `mxutils.CheckType(...)`, e.g., `mxutils.CheckType(c4d.BaseObject(c4d.Ocube))`. A failed allocation returns `None`.
- Call `c4d.EventAdd()` once at the end of the function that modified the scene, never in a loop. To get up-to-date caches immediately, or to update a document that is not the active one, call `doc.ExecutePasses(None, animation, expression, caches, c4d.BUILDFLAGS_NONE)` instead.
- Treat caches as read-only. Do not rely on the existence of a cache before the document has been executed.
- Setting global matrices (`SetMg`, `GetMg` on deep hierarchies) is more expensive than local ones (`SetMl`, `GetMl`). Prefer local matrices.
- Do not walk hierarchies recursively with hand written code. Use `mxutils.IterateTree` and `mxutils.IterateGraph`, they avoid recursion limits and `None` pitfalls.
- Add undo steps for modifications done by commands and tools, not for modifications done by generators, tags or scripts that run on every update. Undo steps must never be created in a threaded context.
  - Wrap changes in `doc.StartUndo()` / `doc.EndUndo()`.
  - `c4d.UNDOTYPE_NEW`: call `doc.AddUndo` **after** inserting the element.
  - `c4d.UNDOTYPE_CHANGE`, `c4d.UNDOTYPE_DELETE` and all other types: call `doc.AddUndo` **before** modifying or removing the element.
- Parameters are accessed with the bracket operator, `node[c4d.PRIM_CUBE_LEN] = c4d.Vector(200)`. Use `SetParameter`/`GetParameter` when you need flags such as `c4d.DESCFLAGS_SET_USERINTERACTION`, and the data container (`node.GetDataInstance()`) only when you need to read many values of the node itself or copy settings (`SetData`). To find the symbol of a parameter, print it with `mxutils.DebugPrint.PrintParameters` (see `.agents/debug.md`) and search the current docs at <https://developers.maxon.net/docs/py> for `Resource Index`.
- Parameters that use units store base units: an angle parameter shown in degrees is stored in radians (`c4d.utils.DegToRad`).
- Takes override parameters through `c4d.DescID`s, which must be precise (include data types), see `scene/takes.py`.
- Do not use `threading` or `multiprocessing` to access scene data. The only accepted use of the `threading` module is a `threading.Lock` that protects your own storage, never held while calling into the Cinema API. For long computations use `c4d.threading.C4DThread`.
- Callbacks are called often (every update, every dragged slider value, every rendered frame). Keep them fast, do not use the number of calls as a clock, depend on document time and parameters. Long callbacks must check for cancellation, e.g., `hh.GetThread().TestBreak()`.
- Do not store references to nodes in global storage that outlives a callback, the scene can have changed by the time the data is used. Store names, ids or plain values.

# Threading

| Operation | Main thread | Threaded context |
| --- | --- | --- |
| Insert, move, remove nodes of a document (`InsertObject`, `InsertUnder`, `Remove`) | Allowed | **Forbidden** |
| Create or modify nodes that are not attached to a document (e.g., the output of a generator) | Allowed | Allowed |
| Modify parameters or matrices of other nodes in a document | Allowed | Tags only |
| Modify geometry/topology of source nodes in a document, or run a modeling command on them | Allowed | **Forbidden** |
| Build generated cache output or modify designated deformation output | Allowed | Allowed only in its owning `ObjectData` callback |
| Modify parameters or matrices of the own node | Allowed | **Forbidden** |
| Create or modify materials | Allowed | **Forbidden** |
| Create undo steps | Allowed | **Forbidden** |
| Use the interface (dialogs, messages) | Allowed | **Forbidden** |
| Access files | Allowed | Allowed, but not while drawing |
| Read scene data | Allowed | Allowed |

Tags are the exception only for changing parameters and matrices of other nodes because they run after animation has written parameters and before generators consume them. This does not permit geometry/topology edits or modeling commands in `Execute`. A callback that changes its own node creates a feedback loop, because changing a node marks it dirty and triggers another update. `GetVirtualObjects` can construct and return geometry in its generated cache, and `ModifyObject` can change the designated deform output; neither operation destructively edits the source scene object.

## Deferring work to the main thread

When a threaded callback finds that the document must change, it cannot do that itself. Two options exist:

1. **Core message**: Send `c4d.SpecialEventAdd(ID_PLUGIN_REQUEST, key)` from the callback and handle `c4d.plugins.MessageData.CoreMessage` on the main thread. The message only carries integers, so the data goes through a lock protected global storage keyed by `key`. Start keys at 1, a message parameter of 0 cannot be read in Python. Store plain data, not node references.
2. **Node message**: Tie the work to `NodeData.Message`, e.g., to a button click (`c4d.MSG_DESCRIPTION_COMMAND`) of a tag or object, and verify the thread before doing it:

```python
def Message(self, node: c4d.BaseTag, msgId: int, data: object) -> bool:
    if msgId == c4d.MSG_DESCRIPTION_COMMAND and c4d.threading.GeIsMainThreadAndNoDrawThread():
        doc: c4d.documents.BaseDocument = node.GetDocument()
        # Modify the document here, e.g., insert objects.
    return True
```

The full core message pattern, including the `ctypes` code to read a core message parameter, is described in the current docs. Start at <https://developers.maxon.net/docs/py> and search for `Scene Execution` and `Deferring Workloads`. To debug threading violations, see `.agents/debug.md`.

# Recipes

## Create and insert objects

```python
# Create a cube with a phong tag and insert it under a null object, which is then inserted into
# the scene.
cube: c4d.BaseObject = mxutils.CheckType(c4d.BaseObject(c4d.Ocube))
phongTag: c4d.BaseTag = mxutils.CheckType(cube.MakeTag(c4d.Tphong))
null: c4d.BaseObject = mxutils.CheckType(c4d.BaseObject(c4d.Onull))
cube.InsertUnder(null)
doc.InsertObject(null)
c4d.EventAdd()
```

## Navigate and traverse

```python
a: c4d.BaseObject = doc.GetFirstObject()
children: list[c4d.BaseObject] = a.GetChildren()

# Depth-first over a node, its descendants and its following siblings.
for node in mxutils.IterateTree(a, yieldSiblings=True):
    print(node.GetName())

# A path of navigation characters: d(own), u(p), n(ext), p(revious), f(irst sibling), r(oot).
e: c4d.BaseObject | None = mxutils.GetNodeFromPath(a, "ddnd")
```

`mxutils.IterateTree` also supports `mxutils.TRAVERSAL_INVERSE_DEPTH_FIRST` (children before parents, useful for deleting or flattening) and `mxutils.TRAVERSAL_BREADTH_FIRST`. `mxutils.IterateGraph` additionally follows branches and caches, each of which must be enabled explicitly. See [traversal.py](../examples/scene/traversal.py).

## Iterate a branch

```python
# Branch heads are nodes, start at the first child of the head. All materials of a document:
for material in mxutils.IterateTree(doc.GetFirstMaterial(), yieldSiblings=True):
    print(material.GetName())
```

## Build caches and read them

```python
doc.ExecutePasses(None, False, False, True, c4d.BUILDFLAGS_NONE)
cache: c4d.BaseObject | None = cube.GetCache()
```

## Undo

```python
doc.StartUndo()

cube: c4d.BaseObject = mxutils.CheckType(c4d.BaseObject(c4d.Ocube))
doc.InsertObject(cube)
doc.AddUndo(c4d.UNDOTYPE_NEW, cube) # After the insertion.

doc.AddUndo(c4d.UNDOTYPE_CHANGE, cube) # Before the modification.
cube.SetMg(c4d.utils.MatrixMove(c4d.Vector(100, 0, 0)))

doc.EndUndo()
c4d.EventAdd()
```

## Documents

```python
newDoc: c4d.documents.BaseDocument = mxutils.CheckType(c4d.documents.BaseDocument())
c4d.documents.InsertBaseDocument(newDoc)
c4d.documents.SetActiveDocument(newDoc)

loadedDoc: c4d.documents.BaseDocument | None = c4d.documents.LoadDocument(
    "C:/Users/username/Desktop/scene.c4d", c4d.SCENEFILTER_OBJECTS | c4d.SCENEFILTER_MATERIALS)
```

`MergeDocument`, `SaveDocument`, `LoadFile` and `KillDocument` cover merging, saving, loading as an active document and closing. See [documents.py](../examples/scene/documents.py).

## Layers

Get the layer root with `doc.GetLayerObjectRoot()`, create layers with `c4d.documents.LayerObject()` and `root.InsertLast(layer)`, and assign a node with `node.SetLayerObject(layer)`.

## User data

```python
angle: c4d.BaseContainer = c4d.GetCustomDataTypeDefault(c4d.DTYPE_REAL)
angle[c4d.DESC_NAME] = "Angle"
angle[c4d.DESC_UNIT] = c4d.DESC_UNIT_DEGREE
angle[c4d.DESC_CUSTOMGUI] = c4d.CUSTOMGUI_REALSLIDER
didAngle: c4d.DescID = null.AddUserData(angle)
null[didAngle] = c4d.utils.DegToRad(45)
```

See [userdata.py](../examples/scene/userdata.py) for dropdowns, iteration and removal.

## Takes

Take overrides are created with `takeData.AddTake`, `BaseTake.FindOrAddOverrideParam` followed by `BaseOverride.UpdateSceneNode`, and override groups with `BaseTake.AddOverrideGroup`. See [takes.py](../examples/scene/takes.py).

## Scripting elements

Python Generator, Python Tag, Python Effector and Python Field scripts live in [scripting-elements](../examples/scene/scripting-elements/README.md). They run in a threaded context, so the threading rules apply.

# Examples

- [Documents](../examples/scene/documents.py): Accessing and instantiating documents, loading, saving, merging, modes.
- [Objects](../examples/scene/objects.py): Instantiating, inserting, transforms, bounding boxes, visibility, caches.
- [Parameters](../examples/scene/parameters.py): Atomic, bracket operator and data container access.
- [Traversal](../examples/scene/traversal.py): Navigating hierarchies, traversal orders, graph traversal over hierarchies, caches and branches.
- [Undos](../examples/scene/undos.py): Undo steps for insertions, modifications and removals.
- [Layers](../examples/scene/layers.py): Creating layers and assigning scene elements to them.
- [Takes](../examples/scene/takes.py): The Take System, overrides and override groups.
- [User Data](../examples/scene/userdata.py): Defining, setting, iterating and removing user data.
- [Scripting Elements](../examples/scene/scripting-elements/README.md): Python Generator, Tag, Effector and Field.
- [Modeling](../examples/modeling/README.md): Geometry, caches, modeling commands, UVs, volumes and snapping.
- [Animation](../examples/animation/README.md): Tracks, keys, curves, motion tracking and simulation.
