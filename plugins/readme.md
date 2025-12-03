# Plugins

Contains code examples for implementing plugins using the Cinema 4D Python API.

| Plugin Name | Category | Description |
| ----------- | -------- | ----------- |
| py-cmd_gui_hello_world       | Command/Gui         | Demonstrates the most basic command/dialog plugin possible, this is not only a command hello world example, but generally a plugin hello world example. |
| py-cmd_gui_simple            | Command/Gui         | Demonstrates a simple dialog with two number input fields, a combo box and a button to carry out numeric operations on the two numbers. |
| py-cmd_gui_dynamic           | Command/Gui         | Demonstrates a dialog with dynamic content, where the content changes based on user input. |
| py-cmd_gui_persistent        | Command/Gui         | Demonstrates how to store dialog layout data and values persistently over dialog open/close and Cinema 4D restart boundaries. |
| py-cmd_gui_persistent_no_restart | Command/Gui     | Demonstrates a simple way to store dialog layout data and values persistently over dialog open/close boundaries (but not over Cinema 4D restart boundaries). :warning: The no-restart version of this example is considerably less complex than the full version. It is recommend to start out with this version, when persistent layouts or values are a requirement. |
| py-cmd_gui_resources         | Command/Gui         | Demonstrates a plugin that uses resources to define its dialog layout and string translations. |
| py-texture_baker             | Command/Gui         | Legacy code example that demonstrates implementing a simple texture baking dialog. |
| py-memory_viewer             | Command/Gui         | Legacy code example that demonstrates implementing a memory viewer dialog. |
| py-sculpt_save_mask          | Command             | Legacy code example for the Sculpting API, highly specialized and not that useful outside of sculpting. |
| py-rounded_tube              | ObjectData          | Demonstrates how to implement a polygonal object generator with handles to drive parameters. |
| py-double_circle             | ObjectData          | Demonstrates how to implement a spline object generator with handles to drive parameters. |
| py-spherify_modifier         | ObjectData          | Demonstrates how to implement a modifier object that modifies a point object. |
| py-custom_icon               | ObjectData          | Demonstrates how to implement a scene element that dynamically updates its icon. |
| py-ocio_node                 | ObjectData          | Demonstrates how to implement a scene element respecting OpenColorIO color management. |
| py-offset_y_spline           | ObjectData          | Questionable design, should not be followed. |
| py-gravitation               | ObjectData          | Demonstrates how to implement a classic particle modifier object that applies a simple gravitation effect for each particle. |
| py-dynamic_parameters_object | NodeData            | Demonstrates how to implement a node (at the example of an object) that dynamically updates its parameters. |
| py-look_at_camera            | TagData             | Demonstrates how to implement a tag that forces the host object to look at the camera (like the Look At Camera Tag). |
| py-fresnel                   | ShaderData          | Demonstrates how to implement a shader that computes a fresnel effect. |
| py-liquid_painter            | ToolData            | Demonstrates how to implement a simple tool. |
| py-tooldata_ui               | ToolData            | Demonstrates how to implement a ToolData with a linkBox where it's possible to drag and drop an object, which is then cloned and added to the document in a random position. |
| py-sculpt_grab_brush         | SculptBrushToolData | Demonstrates how to implement a brush tool that modifies a BaseObject by grabbing all points under the brush. |
| py-sculpt_pull_brush         | SculptBrushToolData | Demonstrates how to implement a brush tool that modifies a BaseObject by pulling all points under the brush. |
| py-sculpt_twist_brush        | SculptBrushToolData | Demonstrates how to implement a brush tool that modifies a BaseObject by twisting all points under the brush. |
| py-sculpt_paint_brush        | SculptBrushToolData | Demonstrates how to implement a brush tool that rasterizes the stencil onto the polygons touched by the brush, accessing the stencil and BodyPaint layer. |
| py-ies_meta                  | SceneSaverData      | Demonstrates how to implement a scene saver plugin that exports all IES Meta information from the current document to a txt file, iterating through all objects in the scene. |
| py-xample_loader             | BitmapLoaderData    | Demonstrates how to implement a custom bitmap loader to import a custom picture format into Cinema 4D. |
| py-xample_saver              | BitmapSaverData     | Demonstrates how to implement a custom bitmap saver to export a custom picture format into Cinema 4D. |
| py-preference                | PreferenceData      | Demonstrates how to implement a preference category in the Cinema 4D preference dialog, exposing parameters as global preferences. |
| py-render_token              | Render Token        | Demonstrates how to register two Tokens, one visible in the render settings and the other not. A token is a string that will be replaced during the token evaluation time by a string representation. |
| py-licensing_2026         | Licensing           | Demonstrates how to implement licensing checks in plugins. |

`py-noise_falloff` is a legacy code example for falloffs, a technology that has been replaced by fields in R20. Falloffs are still supported for compatibility reasons, but new development should focus on fields instead.
