# Plugins

Contains code examples for implementing plugins using the Cinema 4D Python API


| Plugin Folder | Category | Description |
| ----------- | -------- | ----------- |
| py_cmd_gui_hello_world               | Command/Gui          | Demonstrates the most basic command/dialog plugin possible, this is not only a command hello world example, but generally a plugin hello world example. |
| py_cmd_gui_simple                    | Command/Gui          | Demonstrates a simple dialog with two number input fields, a combo box and a button to carry out numeric operations on the two numbers. |
| py_cmd_gui_dynamic                   | Command/Gui          | Demonstrates a dialog with dynamic content, where the content changes based on user input. |
| py_cmd_gui_persistent                | Command/Gui          | Demonstrates how to store dialog layout data and values persistently over dialog open/close and Cinema 4D restart boundaries. |
| py_cmd_gui_persistent_no_restart     | Command/Gui          | Demonstrates a simple way to store dialog layout data and values persistently over dialog open/close boundaries (but not over Cinema 4D restart boundaries). :warning: The no-restart version of this example is considerably less complex than the full version. It is recommend to start out with this version, when persistent layouts or values are a requirement. |
| py_cmd_gui_resources                 | Command/Gui          | Demonstrates a plugin that uses resources to define its dialog layout and string translations. |
| py_cmd_gui_html                      | Command/Gui          | Demonstrates how to implement a dialog that hosts an HTML viewer and can send and receive data to/from the displayed web page. Implements a simple light manager with bidirectional updates between the scene and the web page, including dynamic styling based on the Cinema 4D look and feel. |
| py_cmd_texture_baker                 | Command/Gui          | Demonstrates implementing a simple legacy texture baking dialog. |
| py_cmd_memory_viewer                 | Command/Gui          | Demonstrates implementing a simple legacy memory viewer dialog. |
| py_cmd_sculpt_save_mask              | Command              | Demonstrates the legacy Sculpting API; it is highly specialized and not that useful outside of sculpting. |
| py_cmd_tool_finalization             | Command              | Demonstrates a tool finalization workflow at the example of editing SDS weights. The pattern locks onto a snapshot of scene data, allows rolling interactive changes with viewport feedback, and only commits changes to the scene on explicit user confirmation. |
| py_obj_rounded_tube                  | ObjectData           | Demonstrates how to implement a polygonal object generator with handles to drive parameters. |
| py_obj_double_circle                 | ObjectData           | Demonstrates how to implement a spline object generator with handles to drive parameters. |
| py_obj_sphere_deformer               | ObjectData           | Demonstrates how to implement a deformer object that pushes the points of a point object to a spherical shape, driven by radius and strength parameters. |
| py_obj_assetcontainer                | ObjectData           | Demonstrates NodeData serialization and custom branching. Shows how to store, read, and copy extra node data by owning a custom GeListHead branch and implementing NodeData.GetBranchInfo(). |
| py_obj_buildflags                    | ObjectData           | Demonstrates how to react to build flags and level of detail (LOD) in an object plugin. Build flags signal the context in which an object is built (rendering, editing, export, etc.), and LOD controls the detail level from 0.0 to 1.0. |
| py_obj_custom_icon                   | ObjectData           | Demonstrates how to implement a scene element that dynamically updates its icon. |
| py_obj_ocio_node                     | ObjectData           | Demonstrates how to implement a scene element respecting OpenColorIO color management. |
| py_obj_offset_y_spline               | ObjectData           | Demonstrates a spline offset generator (very questionable design, should not be followed). |
| py_obj_gravitation                   | ObjectData           | Demonstrates how to implement a classic particle modifier object that applies a simple gravitation effect for each particle. |
| py_obj_skin_mesh                     | ObjectData           | Demonstrates Skin Joint and Skin Mesh object generators. Skin Mesh recursively skins its Skin Joint children and applies native modeling commands to the generated mesh. |
| py_obj_dynamic_parameters            | NodeData             | Demonstrates how to implement a node (at the example of an object) that dynamically updates its parameters. |
| py_tag_look_at_camera                | TagData              | Demonstrates how to implement a tag that forces the host object to look at the camera (like the Look At Camera Tag). |
| py_sha_fresnel                       | ShaderData           | Demonstrates how to implement a shader that computes a fresnel effect. |
| py_tool_liquid_painter               | ToolData             | Demonstrates how to implement a simple tool. |
| py_tool_ui                           | ToolData             | Demonstrates how to implement a ToolData with a linkBox where it's possible to drag and drop an object, which is then cloned and added to the document in a random position. |
| py_tool_sculpt_grab_brush            | SculptBrushToolData  | Demonstrates how to implement a brush tool that modifies a BaseObject by grabbing all points under the brush. |
| py_tool_sculpt_pull_brush            | SculptBrushToolData  | Demonstrates how to implement a brush tool that modifies a BaseObject by pulling all points under the brush. |
| py_tool_sculpt_twist_brush           | SculptBrushToolData  | Demonstrates how to implement a brush tool that modifies a BaseObject by twisting all points under the brush. |
| py_tool_sculpt_paint_brush           | SculptBrushToolData  | Demonstrates how to implement a brush tool that rasterizes the stencil onto the polygons touched by the brush, accessing the stencil and BodyPaint layer. |
| py_obj_sculpt_modifier_deformer      | ObjectData           | Demonstrates how to implement a modifier object that modifies a point object using the pull sculpting brush tool. |
| py_io_ies_meta                       | SceneSaverData       | Demonstrates how to implement a scene saver plugin that exports all IES Meta information from the current document to a txt file, iterating through all objects in the scene. |
| py_io_xample_loader                  | BitmapLoaderData     | Demonstrates how to implement a custom bitmap loader to import a custom picture format into Cinema 4D. |
| py_io_xample_saver                   | BitmapSaverData      | Demonstrates how to implement a custom bitmap saver to export a custom picture format into Cinema 4D. |
| py_prf_preference                    | PreferenceData       | Demonstrates how to implement a preference category in the Cinema 4D preference dialog, exposing parameters as global preferences. |
| py_msc_noise_falloff                 | Falloff              | Demonstrates legacy falloffs, a technology that has been replaced by fields in R20. |
| py_msc_render_token                  | Render Token         | Demonstrates how to register two Tokens, one visible in the render settings and the other not. A token is a string that will be replaced during the token evaluation time by a string representation. |
| py_msc_licensing                     | Licensing            | Demonstrates how to implement licensing checks in plugins. |