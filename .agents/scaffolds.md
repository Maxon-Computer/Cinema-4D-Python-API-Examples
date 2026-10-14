# Scaffolds Documentation

Scaffolds are templates and reusable structures for building plugins. A scaffold tells you which questions to ask the user, which files to generate, and which code to put into them. The result is a ready to load plugin in the `projects/` folder of the SDK, which the user (or you) then extends.

# TOC

- [Available Scaffolds](#available-scaffolds): The scaffolds and when to use which.
- [Workflow](#workflow): The steps to follow for every scaffold.
- [Common Questions](#common-questions): The questions that every scaffold asks.
- [Placeholders](#placeholders): The values that are substituted into templates.
- [Parameters](#parameters): How user defined parameters map to resources and code.
- [Resource Rules](#resource-rules): Rules for `.res`, `.h` and `.str` files.
- [Rules](#rules): Hard rules for scaffolding.

# Available Scaffolds

| Scaffold | Use it for | Hook | Folder prefix |
| --- | --- | --- | --- |
| [Dialog](scaffolds/dialog.md) | A command that opens a dockable dialog (`GeDialog`), laid out in code or with resource files. | `CommandData` + `GeDialog` | `py_cmd_gui_` |
| [CommandData](scaffolds/commanddata.md) | A command that runs on demand from menus, palettes and shortcuts, without an interface. | `CommandData` | `py_cmd_` |
| [ObjectData](scaffolds/objectdata.md) | A generator, spline generator or deformer object with parameters. | `ObjectData` | `py_obj_` |
| [TagData](scaffolds/tagdata.md) | A tag that runs on every scene update and has parameters. | `TagData` | `py_tag_` |
| [PreferenceData](scaffolds/preferencedata.md) | A page in the Cinema 4D preferences that stores global settings. | `PreferenceData` | `py_msc_` |
| [MessageData](scaffolds/messagedata.md) | A plugin that receives core messages of the application, or custom messages sent with `c4d.SpecialEventAdd`. | `MessageData` | `py_msc_` |
| [ShaderData](scaffolds/shaderdata.md) | A classic material shader with parameters. | `ShaderData` | `py_sha_` |
| [ToolData](scaffolds/tooldata.md) | A viewport tool that reacts to mouse input. | `ToolData` | `py_tool_` |
| [SceneLoaderData](scaffolds/sceneloaderdata.md) | An importer for a scene file format. | `SceneLoaderData` | `py_io_`, suffix `_loader` |
| [SceneSaverData](scaffolds/scenesaverdata.md) | An exporter for a scene file format. | `SceneSaverData` | `py_io_`, suffix `_saver` |
| [BitmapLoaderData](scaffolds/bitmaploaderdata.md) | An importer for an image file format. | `BitmapLoaderData` | `py_io_`, suffix `_loader` |
| [BitmapSaverData](scaffolds/bitmapsaverdata.md) | An exporter for an image file format. | `BitmapSaverData` | `py_io_`, suffix `_saver` |
| [RenderToken](scaffolds/rendertoken.md) | A token that is replaced by a string in render and save paths. Needs no plugin ID. | `RegisterToken` | `py_msc_` |

## Plugin Form Selection

Use this table to build the selection menu when the user asks for a plugin but has not specified its form. Offer only forms that can perform the requested behavior; do not include incompatible types just to list every scaffold. Preserve a form the user already specified; do not ask them to choose it again.

| Menu choice | Scaffold | Choose it when... | Do not choose it when... |
| --- | --- | --- | --- |
| Command | [CommandData](scaffolds/commanddata.md) | A user-invoked one-shot action should process a selection or scene. | The operation must continuously generate output or be controlled by viewport mouse gestures. |
| Dialog | [Dialog](scaffolds/dialog.md) | The user needs a dockable interface with controls and buttons. | The behavior is only a viewport gesture or must run on every scene update. |
| Generator object | [ObjectData](scaffolds/objectdata.md) | The plugin should procedurally create its own cache from object parameters; `GetVirtualObjects` can return an extruded result as generated output. | The request is to destructively edit existing geometry in the active scene; use a command or tool instead. |
| Viewport tool | [ToolData](scaffolds/tooldata.md) | The user should activate the plugin and interact directly in the viewport with mouse input. | The operation is automatic, continuously evaluated, or has no viewport interaction. |
| Tag | [TagData](scaffolds/tagdata.md) | Lightweight per-update behavior; `Execute` may change parameters and matrices of other scene nodes. A button can trigger a guarded node `Message` callback for main-thread work. | The operation must directly change geometry/topology, run a modeling command, create undo, show UI, or change document structure from `Execute`. NodeData callbacks cannot edit the active scene this way; use a button `Message`, Command, Tool, or generated ObjectData cache as appropriate. |
| Shader | [ShaderData](scaffolds/shaderdata.md) | A material shader should compute color or shading output. | The plugin should perform general scene or geometry edits. |
| Preferences page | [PreferenceData](scaffolds/preferencedata.md) | The user needs persistent application-wide settings. | The values belong to a scene object or the plugin is an operation. |
| Message handler | [MessageData](scaffolds/messagedata.md) | The plugin should react to application or custom messages, including deferring work to a safe context. | The user needs a directly invoked command or interactive viewport tool. |
| Scene importer / exporter | [SceneLoaderData](scaffolds/sceneloaderdata.md) / [SceneSaverData](scaffolds/scenesaverdata.md) | The plugin should read or write a scene file format. | The request is a general modeling action unrelated to file I/O. Ask which direction when unclear. |
| Image importer / exporter | [BitmapLoaderData](scaffolds/bitmaploaderdata.md) / [BitmapSaverData](scaffolds/bitmapsaverdata.md) | The plugin should read or write an image file format. | The request is a general image operation unrelated to file I/O. Ask which direction when unclear. |
| Render token | [RenderToken](scaffolds/rendertoken.md) | A path token should evaluate to a string for render or save paths. | The request is an operation that changes a scene or image. |
| Other / custom | No matching scaffold | The requested plugin hook has no matching scaffold. Consult examples as references and create under `projects/`. | A listed scaffold can safely implement the requested behavior. |

When the intended interaction is ambiguous, ask which compatible form fits instead of silently choosing. For polygon extrusion, offer Command for a one-shot operation on the current selection and Viewport tool for mouse-driven extrusion. Do not offer TagData `Execute` for extrusion: no NodeData evaluation callback can run a modeling command against the active scene. A TagData button can dispatch through its guarded `Message` callback for main-thread work. Offer a Generator only when the user wants a non-destructive, continuously evaluated result returned as the ObjectData cache, not an edit to the active polygon object.

Use a scaffold first for any request to create, build, or implement a new plugin or tool, including informal requests such as "create a plugin" or "create a tool." Do this even when the user has not used the word "scaffold." When a request needs a command that opens a dialog, use the Dialog scaffold.

For hooks without a scaffold (sculpt brushes, falloffs, generic nodes, menus and `PluginMessage`), consult examples in `examples/plugins/` as references. For current API guidance, start at <https://developers.maxon.net/docs/py> and search for `Implementing Plugins`; then create the new implementation under `projects/`. Never use an example as the output target or modify anything under `examples/`.

# Workflow

1. **Read** this file and the scaffold file of the requested type. Read `AGENTS.md` for the code style, all generated code must follow it.
2. **Ask** the user for the values the scaffold needs, with a chat selection menu, see [Common Questions](#common-questions). Use the ask-questions or selection menu tool of your environment (e.g., `vscode_askQuestions` in VS Code Copilot Chat, `AskUserQuestion` in Claude Code). Whenever you can predict even one plausible answer, present it as a recommended choice and include `Other (enter a custom answer)` when custom answers are valid. Apply this to names, descriptions, behavior and technical choices; do not turn predictable answers into text-only fields. Use text-only input only when no plausible answer can be predicted or the value must be supplied exactly, such as a registered plugin ID. Do not offer `Other` for strict API enums. Ask all questions of the scaffold in one batch. When no such tool exists, ask in plain chat with numbered options. Never silently invent answers for questions that have no default, and never continue without a plugin ID (except for the RenderToken scaffold, which has none).
3. **Derive** the [placeholders](#placeholders) from the answers.
4. **Check the target.** The target folder is `projects/{{Folder}}/` in the SDK root (the folder that contains `AGENTS.md`). When it already exists, do not overwrite anything. Ask the user whether to choose another name or to cancel.
5. **Generate** the files of the scaffold, substituting all placeholders. Do not leave any `{{...}}` in the output, and do not leave TODO comments. Generate only the files the chosen options need.
6. **Validate**: Compile the `.pyp` file for syntax errors, e.g., `python -m py_compile projects/{{Folder}}/{{Folder}}.pyp` (the `c4d` module does not have to be importable for that), and delete the generated `__pycache__` folder afterwards. Cross check that every symbol used in the `.pyp` exists in a `.h` file, and every symbol of a `.res` file exists in a `.h` file and in the `.str` file.
7. **Report** briefly what has been created, and give the [load instructions](#loading-the-plugin). Mention that the plugin uses a built-in icon, which the user should replace before releasing the plugin.

All scaffold output belongs under `projects/`. The `examples/` tree is read-only: use it to learn from existing implementations, never as a place to create or modify code.

## Loading the Plugin

Cinema 4D only loads plugins from its plugin paths. Tell the user to add `projects/{{Folder}}` to the plugin search paths, e.g., with the command line argument `g_additionalModulePath=<path to projects/{{Folder}}>`, or to copy or link the folder into the `plugins` folder of the user preferences. Then:

- Restart Cinema 4D after adding or changing resource files (`.res`, `.h`, `.str`), they are parsed at startup.
- Code only changes of the `.pyp` file can be reloaded with the command *Reload Python Plugins*.
- Plugin messages, errors and registration failures are printed to the Python console.

# Common Questions

Every scaffold asks these questions first, followed by its own questions (the RenderToken scaffold skips `pluginId`, tokens have no ID). Infer a useful plugin name and one-sentence description from the request, present each as a recommended choice, and add `Other (enter a custom name/description)` so the user can override it. For each scaffold-specific question, present any predictable answer as a recommended selection and add `Other (enter a custom answer)` when the value supports customization. Keep text-only input for values that cannot be predicted and must be supplied exactly, such as plugin IDs. Strict API enums remain constrained to their valid choices.

| Key | Question | Options | Validation |
| --- | --- | --- | --- |
| `name` | What is the name of the plugin? | Suggested name inferred from the request (recommended); `Other (enter a custom name)`. | Not empty, ASCII only, letters, digits, spaces and dashes. This is the display name, e.g., `Rounded Tube`. |
| `description` | What one-sentence description should the plugin use? | Suggested description inferred from the request (recommended); `Other (enter a custom description)`. | One line, no quotes. |
| `pluginId` | What is your plugin ID? Request one at developers.maxon.net if you do not have one. | Free text input of the number only, no preset options, no default. | Positive integer, not used by another plugin in `projects/` or `examples/plugins/`. |

## Plugin IDs

- Every plugin ID must be globally unique. Two plugins with the same ID cannot both be loaded.
- IDs must be obtained from the plugin ID generator on [developers.maxon.net](https://developers.maxon.net/). **You cannot generate a valid ID yourself.** Never invent an ID, never use a placeholder or a "test" ID, and never reuse an ID from an example.
- Always ask the user for the ID. When the user has none, tell them to request one at developers.maxon.net and stop the scaffolding until they provide it. Do not generate any files without an ID.
- Some scaffolds need more than one ID (see the scaffold file). Ask for every ID separately.
- Reject an ID that is already used by a plugin in `projects/` or `examples/plugins/`, grep both for it, and ask again.

# Placeholders

All templates use `{{Placeholder}}` markers. Derive the values from the user input. The example input is the name `Rounded Tube`.

| Placeholder | Meaning | Example |
| --- | --- | --- |
| `{{Name}}` | The display name as entered. | `Rounded Tube` |
| `{{Description}}` | The one sentence description. | `Generates a rounded tube.` |
| `{{PluginId}}` | The main plugin ID, as given by the user. | `1234567` |
| `{{ClassName}}` | PascalCase of the name, no spaces. | `RoundedTube` |
| `{{SlugSnake}}` | Lowercase snake case of the name. | `rounded_tube` |
| `{{Slug}}` | Lowercase letters and digits only, no separators. | `roundedtube` |
| `{{SLUG}}` | Uppercase `Slug`. Used as the symbol prefix. | `ROUNDEDTUBE` |
| `{{Folder}}` | The plugin folder and `.pyp` file name: the folder prefix of the scaffold followed by `{{SlugSnake}}` (and the suffix of the scaffold, e.g., `_loader`, where it defines one). | `py_obj_rounded_tube` |
| `{{ResName}}` | The description resource name: the node prefix (`O` objects, `T` tags, `X` shaders) followed by `py{{Slug}}`. Preferences use `py{{Slug}}` without prefix. Used as the symbol, container name, `description` argument and as the lowercase base name of the files. | `Opyroundedtube` |
| `{{resname}}` | Lowercase `{{ResName}}`, used in file names. | `opyroundedtube` |
| `{{ModelName}}` | The name of the model that generates the plugin. | |
| `{{Year}}` | The current year. | `2026` |
| `{{Version}}` | The SDK version, i.e., the `__version__` used by the current examples, e.g., in `examples/scene/objects.py`. | `2027.0.0` |

When `{{Slug}}` would start with a digit, prefix it with `x`. When the name does not produce a usable slug, ask again.

# Parameters

Scaffolds for objects, tags and preferences let the user define parameters. Ask for them as one question `parameters`. Options: `Use the default parameters of the scaffold` (recommended), `Define my own`. For the second, ask for free text with one parameter per line in the form `Name, type, default`, e.g., `Radius, length, 200`. Supported types:

| Type | `.res` data type | `DTYPE_` | Python type for `InitAttr` | Python default | Extra `.res` flags |
| --- | --- | --- | --- | --- | --- |
| `bool` | `BOOL` | `DTYPE_BOOL` | `bool` | `True` | |
| `int` | `LONG` | `DTYPE_LONG` | `int` | `1` | `MIN 0; MAX 1000;` when the user gives a range |
| `float` | `REAL` | `DTYPE_REAL` | `float` | `1.0` | |
| `length` | `REAL` | `DTYPE_REAL` | `float` | `200.0` | `UNIT METER; MIN 0.0;` |
| `angle` | `REAL` | `DTYPE_REAL` | `float` | `c4d.utils.DegToRad(45.0)` | `UNIT DEGREE;` (stored in radians) |
| `string` | `STRING` | `DTYPE_STRING` | `str` | `""` | |
| `vector` | `VECTOR` | `DTYPE_VECTOR` | `c4d.Vector` | `c4d.Vector(0.0)` | |
| `color` | `COLOR` | `DTYPE_COLOR` | `c4d.Vector` | `c4d.Vector(1.0)` | |
| `link` | `LINK` | `DTYPE_BASELISTLINK` | `c4d.BaseList2D` | `None` (no default) | `ACCEPT { Obase; }` |
| `cycle` | `LONG` | `DTYPE_LONG` | `int` | `0` | `CYCLE { <SYMBOL>_<ENTRY>; ... }`, the entries must be defined as symbols and strings |
| `button` | `BUTTON` | none | none | none | Handled in `Message`, has no value |

Rules for generating from the parameters:

- Parameter symbols are `{{SLUG}}_<PARAMNAME>`, uppercase, e.g., `ROUNDEDTUBE_RADIUS`. They become attributes of the `c4d` module, so they must be unique across all plugins, which is why the prefix is mandatory.
- IDs start at `10000` (objects and tags) or `1000` (preferences) and increase by one in the order of the parameters. Always write explicit values (`= 10000`). Cycle entry symbols are written after their parameter with the explicit values of the cycle (`= 0`, `= 1`, ...) and do not take part in the numbering of parameters.
- Every parameter symbol appears in the `.h` file, the `.res` file and the `.str` file. Initialize each parameter with a value in `Init` (`InitAttr` + default).
- A `link` has no default. Only `InitAttr`, do not assign.
- When the user defines no parameters, use the default parameters given in the scaffold.

# Resource Rules

Description resources are needed by objects, tags, shaders and preferences; dialogs can optionally use dialog resources. Tool plugins also include a `res` folder with global symbols and strings. For current details, start at <https://developers.maxon.net/docs/py> and search for `Resource Files`. These are the rules that matter for scaffolding:

- Resources live in a `res` folder next to the `.pyp` file. Every scaffold that uses resources must include a `c4d_symbols.h` with an `enum` that ends with a dummy element, even when it holds no symbols. Keep each scaffold's `Files` tree and generated files in sync; when Cinema reports *Could not find required '__res__'*, check the generated resource files and their paths.
- A **description** with the resource name `{{ResName}}` consists of three files that must use the identical name: `res/description/{{resname}}.res` with `CONTAINER {{ResName}}`, `res/description/{{resname}}.h`, and `res/strings_en-US/description/{{resname}}.str` with `STRINGTABLE {{ResName}}`. The same name is passed as `description` to the registration function.
- Always `INCLUDE` the base description of the node type (`Obase` for objects, `Texpression` for tags, `Xbase` for shaders) and place the parameters in the properties group (`ID_OBJECTPROPERTIES` for objects, `ID_TAGPROPERTIES` for tags, `ID_SHADERPROPERTIES` for shaders). Preferences use their own group.
- The string table must contain the name of the description (`{{ResName}} "{{Name}}";`) and one string for each parameter and cycle entry.
- Only the language `strings_en-US` is generated. Mention that other languages are added by copying the folder. For current localization guidance, start at <https://developers.maxon.net/docs/py> and search for `Implementing Plugins` and `resource strings`. Non-ASCII characters in `.str` files must be written as `\uHHHH` escapes, so keep generated strings ASCII.
- Use tabs or four spaces consistently in resource files, and `//` for comments.
- Symbols in header files must not collide with Cinema 4D symbols. The prefix `{{SLUG}}_` and a `py` resource name make collisions unlikely.

# Rules

- IMPORTANT: Never overwrite existing files, and never delete anything in `projects/`. When the target exists, ask.
- IMPORTANT: Generated project code must follow `AGENTS.md`: camel case identifiers (`Execute`, `pluginId`, `PLUGIN_ID` for constants), type hints, `__author__` and `__version__` metadata, a module doc string with usage instructions and topics, and sparse analytical comments. Never add `__copyright__`, `__license__`, or claims of Maxon ownership to a project.
- Hook classes are registered inside an `if __name__ == "__main__":` block. Do not run work at module level besides imports, constants and the symbol import. The module level code runs in the restricted boot phase of Cinema 4D.
- Commands, message plugins, tools, bitmap loaders and savers are registered with an *instance*, objects, tags, shaders, preferences, scene loaders and scene savers with the *class*.
- Respect the threading rules in `.agents/scene.md` in all generated callbacks.
- Do not add features that were not asked for. The generated plugin should work as is, show a visible result, and be small enough to extend.
- Do not add `README.md` or `meta.json` files to the plugin folder.
- Locate files relative to `__file__` and not to the working directory.
- After scaffolding, do not start implementing the logic of the plugin unless the user asked for it. Offer it as a next step.
