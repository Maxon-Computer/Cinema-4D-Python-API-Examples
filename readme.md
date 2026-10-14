# Cinema 4D Python SDK

Describes the content of the Cinema 4D Python SDK.

## Contents

- [SDK Layout](#sdk-layout)
- [Example Categories](#example-categories)
- [Example Index](#example-index)

  - [Plugins](#plugins)
    - [Command](#plugins-command)
    - [I/O](#plugins-i-o)
    - [Miscellaneous](#plugins-miscellaneous)
    - [Objects](#plugins-objects)
    - [Shaders](#plugins-shaders)
    - [Tags](#plugins-tags)
    - [Tools](#plugins-tools)
  - [Scripts](#scripts)
    - [Animation](#scripts-animation)
    - [Data](#scripts-data)
    - [Gui](#scripts-gui)
    - [I/O](#scripts-i-o)
    - [Math](#scripts-math)
    - [Misc](#scripts-misc)
    - [Modeling](#scripts-modeling)
    - [Nodes](#scripts-nodes)
    - [Plugins](#scripts-plugins)
    - [Rendering](#scripts-rendering)
    - [Scene](#scripts-scene)

## SDK Layout

| Path | Description |
| --- | --- |
| [examples](examples/) | Runnable Python examples demonstrating the Cinema 4D and Maxon APIs. |
| [projects](projects/) | Complete Python SDK project templates for building Cinema 4D extensions. |
| `AGENTS.md` | Agent instructions for the Cinema 4D Python SDK. |
| `LICENSE.md` | License information for the Cinema 4D Python SDK. |
| `sdk.code-workspace` | VS Code workspace configuration for the Python SDK. |

## Example Categories

| Path | Description |
| --- | --- |
| [animation/](examples/animation/) | Animation, keyframes, motion, and tracks. |
| [data/](examples/data/) | Basic data types and containers. |
| [gui/](examples/gui/) | User interface elements, dialogs, and user areas. |
| [io/](examples/io/) | Importing and exporting files, images, and assets. |
| [math/](examples/math/) | Vectors, random values, KD-trees, and related mathematical utilities. |
| [misc/](examples/misc/) | Miscellaneous tooling commonly used in scripts. |
| [modeling/](examples/modeling/) | Modeling, meshes, splines, and UVs. |
| [nodes/](examples/nodes/) | Node-based workflows, node graphs, and node materials. |
| [plugins/](examples/plugins/) | Creating plugins, commands, tools, and extensions. |
| [rendering/](examples/rendering/) | Rendering, materials, shaders, textures, and render settings. |
| [scene/](examples/scene/) | Scene files, documents, objects, tags, and takes. |

## Example Index

<table>
  <colgroup>
    <col width="35%">
    <col width="65%">
  </colgroup>
  <thead>
    <tr>
      <th align="left">File</th>
      <th align="left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th colspan="2" align="left"><h3><a id="plugins"></a>Plugins</h3></th>
    </tr>
    <tr>
      <th colspan="2" align="left"><h4><a id="plugins-command"></a>Command</h4></th>
    </tr>
    <tr>
      <td><a href="examples/plugins/py_cmd_gui_dynamic/">examples/plugins/py_cmd_gui_dynamic/</a></td>
      <td>Demonstrates a dialog with dynamic content, where the content changes based on user input.</td>
    </tr>
    <tr>
      <td><a href="examples/plugins/py_cmd_gui_hello_world/">examples/plugins/py_cmd_gui_hello_world/</a></td>
      <td>Demonstrates the most basic command/dialog plugin possible.</td>
    </tr>
    <tr>
      <td><a href="examples/plugins/py_cmd_gui_html/">examples/plugins/py_cmd_gui_html/</a></td>
      <td>Demonstrates how to implement a dialog that hosts an HTML viewer and can send and receive data to/from the displayed web page.</td>
    </tr>
    <tr>
      <td><a href="examples/plugins/py_cmd_gui_persistent/">examples/plugins/py_cmd_gui_persistent/</a></td>
      <td>Demonstrates how to store dialog layout data and values persistently over dialog open/close and Cinema 4D restart boundaries.</td>
    </tr>
    <tr>
      <td><a href="examples/plugins/py_cmd_gui_persistent_no_restart/">examples/plugins/py_cmd_gui_persistent_no_restart/</a></td>
      <td>Demonstrates a simple way to store dialog layout data and values persistently over dialog open/close boundaries (but not over Cinema 4D restart boundaries).</td>
    </tr>
    <tr>
      <td><a href="examples/plugins/py_cmd_gui_resources/">examples/plugins/py_cmd_gui_resources/</a></td>
      <td>Demonstrates a plugin that uses resources to define its dialog layout and string translations.</td>
    </tr>
    <tr>
      <td><a href="examples/plugins/py_cmd_gui_simple/">examples/plugins/py_cmd_gui_simple/</a></td>
      <td>Demonstrates a simple dialog with two number input fields, a combo box and a button to carry out numeric operations on the two numbers.</td>
    </tr>
    <tr>
      <td><a href="examples/plugins/py_cmd_memory_viewer/">examples/plugins/py_cmd_memory_viewer/</a></td>
      <td>Demonstrates implementing a simple legacy memory viewer dialog.</td>
    </tr>
    <tr>
      <td><a href="examples/plugins/py_cmd_sculpt_save_mask/">examples/plugins/py_cmd_sculpt_save_mask/</a></td>
      <td>Demonstrates the legacy Sculpting API; it is highly specialized and not that useful outside of sculpting.</td>
    </tr>
    <tr>
      <td><a href="examples/plugins/py_cmd_texture_baker/">examples/plugins/py_cmd_texture_baker/</a></td>
      <td>Demonstrates implementing a simple legacy texture baking dialog.</td>
    </tr>
    <tr>
      <td><a href="examples/plugins/py_cmd_tool_finalization/">examples/plugins/py_cmd_tool_finalization/</a></td>
      <td>Demonstrates a tool finalization workflow at the example of editing SDS weights.</td>
    </tr>
    <tr>
      <th colspan="2" align="left"><h4><a id="plugins-i-o"></a>I/O</h4></th>
    </tr>
    <tr>
      <td><a href="examples/plugins/py_io_ies_meta/">examples/plugins/py_io_ies_meta/</a></td>
      <td>Demonstrates how to implement a scene saver plugin that exports all IES Meta information from the current document to a txt file, iterating through all objects in the scene.</td>
    </tr>
    <tr>
      <td><a href="examples/plugins/py_io_xample_loader/">examples/plugins/py_io_xample_loader/</a></td>
      <td>Demonstrates how to implement a custom bitmap loader to import a custom picture format into Cinema 4D.</td>
    </tr>
    <tr>
      <td><a href="examples/plugins/py_io_xample_saver/">examples/plugins/py_io_xample_saver/</a></td>
      <td>Demonstrates how to implement a custom bitmap saver to export a custom picture format into Cinema 4D.</td>
    </tr>
    <tr>
      <th colspan="2" align="left"><h4><a id="plugins-miscellaneous"></a>Miscellaneous</h4></th>
    </tr>
    <tr>
      <td><a href="examples/plugins/py_msc_licensing/">examples/plugins/py_msc_licensing/</a></td>
      <td>Demonstrates how to implement licensing checks in plugins.</td>
    </tr>
    <tr>
      <td><a href="examples/plugins/py_msc_menu/">examples/plugins/py_msc_menu/</a></td>
      <td>Demonstrates how to build custom menus for your plugins.</td>
    </tr>
    <tr>
      <td><a href="examples/plugins/py_msc_noise_falloff/">examples/plugins/py_msc_noise_falloff/</a></td>
      <td>Demonstrates legacy falloffs, a technology that has been replaced by fields in R20.</td>
    </tr>
    <tr>
      <td><a href="examples/plugins/py_msc_preference/">examples/plugins/py_msc_preference/</a></td>
      <td>Demonstrates how to implement a preference category in the Cinema 4D preference dialog, exposing parameters as global preferences.</td>
    </tr>
    <tr>
      <td><a href="examples/plugins/py_msc_render_token/">examples/plugins/py_msc_render_token/</a></td>
      <td>Demonstrates how to register two Tokens, one visible in the render settings and the other not.</td>
    </tr>
    <tr>
      <th colspan="2" align="left"><h4><a id="plugins-objects"></a>Objects</h4></th>
    </tr>
    <tr>
      <td><a href="examples/plugins/py_obj_assetcontainer/">examples/plugins/py_obj_assetcontainer/</a></td>
      <td>Demonstrates NodeData serialization and custom branching.</td>
    </tr>
    <tr>
      <td><a href="examples/plugins/py_obj_custom_icon/">examples/plugins/py_obj_custom_icon/</a></td>
      <td>Demonstrates how to implement a scene element that dynamically updates its icon.</td>
    </tr>
    <tr>
      <td><a href="examples/plugins/py_obj_double_circle/">examples/plugins/py_obj_double_circle/</a></td>
      <td>Demonstrates how to implement a spline object generator with handles to drive parameters.</td>
    </tr>
    <tr>
      <td><a href="examples/plugins/py_obj_dynamic_parameters/">examples/plugins/py_obj_dynamic_parameters/</a></td>
      <td>Demonstrates how to implement a node (at the example of an object) that dynamically updates its parameters.</td>
    </tr>
    <tr>
      <td><a href="examples/plugins/py_obj_gravitation/">examples/plugins/py_obj_gravitation/</a></td>
      <td>Demonstrates how to implement a classic particle modifier object that applies a simple gravitation effect for each particle.</td>
    </tr>
    <tr>
      <td><a href="examples/plugins/py_obj_ocio_node/">examples/plugins/py_obj_ocio_node/</a></td>
      <td>Demonstrates how to implement a scene element respecting OpenColorIO color management.</td>
    </tr>
    <tr>
      <td><a href="examples/plugins/py_obj_offset_y_spline/">examples/plugins/py_obj_offset_y_spline/</a></td>
      <td>Demonstrates a spline offset generator (very questionable design, should not be followed).</td>
    </tr>
    <tr>
      <td><a href="examples/plugins/py_obj_rounded_tube/">examples/plugins/py_obj_rounded_tube/</a></td>
      <td>Demonstrates how to implement a polygonal object generator with handles to drive parameters.</td>
    </tr>
    <tr>
      <td><a href="examples/plugins/py_obj_sculpt_modifier_deformer/">examples/plugins/py_obj_sculpt_modifier_deformer/</a></td>
      <td>Demonstrates how to implement a modifier object that modifies a point object using the pull sculpting brush tool.</td>
    </tr>
    <tr>
      <td><a href="examples/plugins/py_obj_sphere_deformer/">examples/plugins/py_obj_sphere_deformer/</a></td>
      <td>Demonstrates how to implement a deformer object that pushes the points of a point object to a spherical shape, driven by radius and strength parameters.</td>
    </tr>
    <tr>
      <th colspan="2" align="left"><h4><a id="plugins-shaders"></a>Shaders</h4></th>
    </tr>
    <tr>
      <td><a href="examples/plugins/py_sha_fresnel/">examples/plugins/py_sha_fresnel/</a></td>
      <td>Demonstrates how to implement a shader that computes a fresnel effect.</td>
    </tr>
    <tr>
      <th colspan="2" align="left"><h4><a id="plugins-tags"></a>Tags</h4></th>
    </tr>
    <tr>
      <td><a href="examples/plugins/py_tag_look_at_camera/">examples/plugins/py_tag_look_at_camera/</a></td>
      <td>Demonstrates how to implement a tag that forces the host object to look at the camera (like the Look At Camera Tag).</td>
    </tr>
    <tr>
      <th colspan="2" align="left"><h4><a id="plugins-tools"></a>Tools</h4></th>
    </tr>
    <tr>
      <td><a href="examples/plugins/py_tool_liquid_painter/">examples/plugins/py_tool_liquid_painter/</a></td>
      <td>Demonstrates how to implement a simple tool.</td>
    </tr>
    <tr>
      <td><a href="examples/plugins/py_tool_sculpt_grab_brush/">examples/plugins/py_tool_sculpt_grab_brush/</a></td>
      <td>Demonstrates how to implement a brush tool that modifies a BaseObject by grabbing all points under the brush.</td>
    </tr>
    <tr>
      <td><a href="examples/plugins/py_tool_sculpt_paint_brush/">examples/plugins/py_tool_sculpt_paint_brush/</a></td>
      <td>Demonstrates how to implement a brush tool that rasterizes the stencil onto the polygons touched by the brush, accessing the stencil and BodyPaint layer.</td>
    </tr>
    <tr>
      <td><a href="examples/plugins/py_tool_sculpt_pull_brush/">examples/plugins/py_tool_sculpt_pull_brush/</a></td>
      <td>Demonstrates how to implement a brush tool that modifies a BaseObject by pulling all points under the brush.</td>
    </tr>
    <tr>
      <td><a href="examples/plugins/py_tool_sculpt_twist_brush/">examples/plugins/py_tool_sculpt_twist_brush/</a></td>
      <td>Demonstrates how to implement a brush tool that modifies a BaseObject by twisting all points under the brush.</td>
    </tr>
    <tr>
      <td><a href="examples/plugins/py_tool_ui/">examples/plugins/py_tool_ui/</a></td>
      <td>Demonstrates how to implement a ToolData with a linkBox where it&#x27;s possible to drag and drop an object, which is then cloned and added to the document in a random position.</td>
    </tr>
    <tr>
      <th colspan="2" align="left"><h3><a id="scripts"></a>Scripts</h3></th>
    </tr>
    <tr>
      <th colspan="2" align="left"><h4><a id="scripts-animation"></a>Animation</h4></th>
    </tr>
    <tr>
      <td><a href="examples/animation/key_quaternion_interpolation.py">examples/animation/key_quaternion_interpolation.py</a></td>
      <td>Checks the interpolation of the first key for an object&#x27;s rotation track. If the interpolation is linear (SLERP) it is changed to cubic.</td>
    </tr>
    <tr>
      <td><a href="examples/animation/motion_tracker_object_track.py">examples/animation/motion_tracker_object_track.py</a></td>
      <td>Loops through all the tracks of the active Motion Tracker object.</td>
    </tr>
    <tr>
      <td><a href="examples/animation/object_find_best_euler_angle.py">examples/animation/object_find_best_euler_angle.py</a></td>
      <td>Checks the rotation tracks of the active object.</td>
    </tr>
    <tr>
      <td><a href="examples/animation/object_quaternion_rotation.py">examples/animation/object_quaternion_rotation.py</a></td>
      <td>Checks if the active object uses quaternion interpolation.</td>
    </tr>
    <tr>
      <td><a href="examples/animation/object_sync_vector_keys.py">examples/animation/object_sync_vector_keys.py</a></td>
      <td>Synchronizes the keys for the tracks of the active cube&#x27;s &quot;Size&quot; parameter.</td>
    </tr>
    <tr>
      <td><a href="examples/animation/object_vector_curves.py">examples/animation/object_vector_curves.py</a></td>
      <td>Reads the vector components curves of the active object&#x27;s rotation track curve.</td>
    </tr>
    <tr>
      <td><a href="examples/animation/object_vector_tracks.py">examples/animation/object_vector_tracks.py</a></td>
      <td>Reads the vector components tracks of the active object&#x27;s position track curve.</td>
    </tr>
    <tr>
      <td><a href="examples/animation/simulation/field_list_add_mask.py">examples/animation/simulation/field_list_add_mask.py</a></td>
      <td>Creates a FieldList with a formula layer, a mask and another formula layer used as a mask of the first formula layer. Assigns this FieldList to the active object that have a c4d.FIELDS parameter e.g. all MoGraph effectors.</td>
    </tr>
    <tr>
      <td><a href="examples/animation/simulation/field_list_sampling.py">examples/animation/simulation/field_list_sampling.py</a></td>
      <td>Samples arbitrary points from multiple fields with c4d.FieldList and stores the result into a vertex color tag.</td>
    </tr>
    <tr>
      <td><a href="examples/animation/simulation/field_object_sampling.py">examples/animation/simulation/field_object_sampling.py</a></td>
      <td>Samples arbitrary points within a random field.</td>
    </tr>
    <tr>
      <td><a href="examples/animation/simulation/modata_get_selection.py">examples/animation/simulation/modata_get_selection.py</a></td>
      <td>Retrieves all selected clones of the active Cloner object.</td>
    </tr>
    <tr>
      <td><a href="examples/animation/simulation/modata_get_weights.py">examples/animation/simulation/modata_get_weights.py</a></td>
      <td>Retrieves the weights from all clones of the active Cloner object.</td>
    </tr>
    <tr>
      <td><a href="examples/animation/simulation/modata_read_color.py">examples/animation/simulation/modata_read_color.py</a></td>
      <td>Retrieves the color or each clone using two ways. First one by accessing directly the Mograph Data. Second one by accessing the polygon cache representation of the Mograph Cloner.</td>
    </tr>
    <tr>
      <td><a href="examples/animation/simulation/modata_set_selection.py">examples/animation/simulation/modata_set_selection.py</a></td>
      <td>Generates and sets a MoGraph selection tag on a MoGraph cloner object. Effectively, this will create a selection tag for all uneven clones in the cloner object. This script has no runtime requirements, as it creates its inputs itself.</td>
    </tr>
    <tr>
      <td><a href="examples/animation/simulation/modata_set_weights.py">examples/animation/simulation/modata_set_weights.py</a></td>
      <td>Sets a weight of 1.0 for all clones of the active Cloner object.</td>
    </tr>
    <tr>
      <td><a href="examples/animation/simulation/particle_group_object.py">examples/animation/simulation/particle_group_object.py</a></td>
      <td>Demonstrates how to read particle data from a ParticleGroupObject.</td>
    </tr>
    <tr>
      <td><a href="examples/animation/simulation/thinking_particles_creates.py">examples/animation/simulation/thinking_particles_creates.py</a></td>
      <td>Creates 90 Thinking Particles. Defines custom position and color for each particle.</td>
    </tr>
    <tr>
      <td><a href="examples/animation/simulation/voronoi_fracture.py">examples/animation/simulation/voronoi_fracture.py</a></td>
      <td>Creates and define a noise shader as an input of a Voronoi Fracture object.</td>
    </tr>
    <tr>
      <td><a href="examples/animation/track_copy.py">examples/animation/track_copy.py</a></td>
      <td>Copies the position, rotation and animation Tracks (so all Keyframes) from obj1 to obj2.</td>
    </tr>
    <tr>
      <td><a href="examples/animation/track_create_keys.py">examples/animation/track_create_keys.py</a></td>
      <td>Creates position Y tracks. Adds two keyframes. Sets their value and interpolation.</td>
    </tr>
    <tr>
      <td><a href="examples/animation/track_synchronized.py">examples/animation/track_synchronized.py</a></td>
      <td>Checks if the rotation track of an object is synchronized. If not, it will be synchronized.</td>
    </tr>
    <tr>
      <th colspan="2" align="left"><h4><a id="scripts-data"></a>Data</h4></th>
    </tr>
    <tr>
      <td><a href="examples/data/_c4d_basebitmap.py">examples/data/_c4d_basebitmap.py</a></td>
      <td>Demonstrates the usage of the central bitmap type.</td>
    </tr>
    <tr>
      <td><a href="examples/data/_c4d_basecontainer.py">examples/data/_c4d_basecontainer.py</a></td>
      <td>Demonstrates the usage of the fundamental container type in the Cinema API.</td>
    </tr>
    <tr>
      <td><a href="examples/data/_c4d_descid.py">examples/data/_c4d_descid.py</a></td>
      <td>Demonstrates important functions for the types c4d.DescID and c4d.DescLevel.</td>
    </tr>
    <tr>
      <td><a href="examples/data/_c4d_description.py">examples/data/_c4d_description.py</a></td>
      <td>Demonstrates important functions for the type c4d.Description.</td>
    </tr>
    <tr>
      <td><a href="examples/data/_maxon_basearray.py">examples/data/_maxon_basearray.py</a></td>
      <td>Demonstrates instantiation and usage of various Maxon data types.</td>
    </tr>
    <tr>
      <td><a href="examples/data/_maxon_datadictionary.py">examples/data/_maxon_datadictionary.py</a></td>
      <td>Demonstrates the key functionalities of maxon.DataDictionary.</td>
    </tr>
    <tr>
      <td><a href="examples/data/_maxon_tuple.py">examples/data/_maxon_tuple.py</a></td>
      <td>Creates a Maxon Tuple of 3 fields (any maxon type is working).</td>
    </tr>
    <tr>
      <th colspan="2" align="left"><h4><a id="scripts-gui"></a>Gui</h4></th>
    </tr>
    <tr>
      <td><a href="examples/gui/dialog_ask_number.py">examples/gui/dialog_ask_number.py</a></td>
      <td>Creates a Modal Dialog asking for an integer or a float. Retrieves the entered value, once the user exit the Dialog.</td>
    </tr>
    <tr>
      <td><a href="examples/gui/dialog_menu_hide_content.py">examples/gui/dialog_menu_hide_content.py</a></td>
      <td>Creates an async Dialog with a top menu. Defines an icon in the menu to toggle group visibility.</td>
    </tr>
    <tr>
      <td><a href="examples/gui/dialog_modal.py">examples/gui/dialog_modal.py</a></td>
      <td>Creates a basic Modal Dialog.</td>
    </tr>
    <tr>
      <td><a href="examples/gui/dialog_quick_tab.py">examples/gui/dialog_quick_tab.py</a></td>
      <td>Creates a Modal Dialog displaying a different SubDialog according to the selected entry of the QuickTab. Demonstrates how to add, flushes, remove tab interactively.</td>
    </tr>
    <tr>
      <td><a href="examples/gui/dialog_subdialog.py">examples/gui/dialog_subdialog.py</a></td>
      <td>Creates and attaches a SubDialog to a Dialog. Switch the displayed SubDialog after a click on a button.</td>
    </tr>
    <tr>
      <td><a href="examples/gui/script_icon.py">examples/gui/script_icon.py</a></td>
      <td>Example to customize the icon used for a script. The icon should be named like the .py file. Should be a TIF with a size of 32x32.</td>
    </tr>
    <tr>
      <td><a href="examples/gui/script_name_description.py">examples/gui/script_name_description.py</a></td>
      <td>Example to customize the name and the description in the script manager. Name-en-US defines the displayed name. Description-en-US defines the description of the script. As long as Name-en-US (Prior R20 it was Name-US) and Description-en-US (Prior R20 it was Description-US) are in the first comment bloc, c4d will extract them.</td>
    </tr>
    <tr>
      <td><a href="examples/gui/user_area_basic.py">examples/gui/user_area_basic.py</a></td>
      <td>Creates and attaches a GeUserArea to a Dialog. Interacts from the GeDialog to the GeUserArea and vice-versa.</td>
    </tr>
    <tr>
      <td><a href="examples/gui/user_area_drag.py">examples/gui/user_area_drag.py</a></td>
      <td>Creates and attaches a GeUserArea to a Dialog. Creates a series of aligned squares, that can be dragged and swapped together.</td>
    </tr>
    <tr>
      <th colspan="2" align="left"><h4><a id="scripts-i-o"></a>I/O</h4></th>
    </tr>
    <tr>
      <td><a href="examples/io/asset_databases.py">examples/io/asset_databases.py</a></td>
      <td>Provides examples for handling asset databases and repositories.</td>
    </tr>
    <tr>
      <td><a href="examples/io/asset_metadata.py">examples/io/asset_metadata.py</a></td>
      <td>Provides examples for reading and writing asset metadata.</td>
    </tr>
    <tr>
      <td><a href="examples/io/asset_types.py">examples/io/asset_types.py</a></td>
      <td>Provides examples for creating and loading different asset types.</td>
    </tr>
    <tr>
      <td><a href="examples/io/bitmap_fill_color.py">examples/io/bitmap_fill_color.py</a></td>
      <td>Adds an overlay color to a Picture.</td>
    </tr>
    <tr>
      <td><a href="examples/io/bitmap_init_vector_file.py">examples/io/bitmap_init_vector_file.py</a></td>
      <td>Initializes a bitmap from a vector image file.</td>
    </tr>
    <tr>
      <td><a href="examples/io/export_alembic.py">examples/io/export_alembic.py</a></td>
      <td>Exports Alembic with custom settings.</td>
    </tr>
    <tr>
      <td><a href="examples/io/export_obj.py">examples/io/export_obj.py</a></td>
      <td>Exports Obj with custom settings.</td>
    </tr>
    <tr>
      <td><a href="examples/io/image_copy_32bit.py">examples/io/image_copy_32bit.py</a></td>
      <td>Copies the internal data of a 32 bit per-channel image to a new one.</td>
    </tr>
    <tr>
      <td><a href="examples/io/import_obj.py">examples/io/import_obj.py</a></td>
      <td>Imports Obj with custom settings.</td>
    </tr>
    <tr>
      <td><a href="examples/io/import_sketchup.py">examples/io/import_sketchup.py</a></td>
      <td>Imports Sketchup File with custom settings.</td>
    </tr>
    <tr>
      <td><a href="examples/io/import_step.py">examples/io/import_step.py</a></td>
      <td>Imports STP/STEP with custom settings.</td>
    </tr>
    <tr>
      <td><a href="examples/io/memory_file_bitmap.py">examples/io/memory_file_bitmap.py</a></td>
      <td>Writes/Reads a bitmap to/from memory.</td>
    </tr>
    <tr>
      <td><a href="examples/io/memory_file_data.py">examples/io/memory_file_data.py</a></td>
      <td>Writes/Reads simple data to/from memory.</td>
    </tr>
    <tr>
      <td><a href="examples/io/texture_paths.py">examples/io/texture_paths.py</a></td>
      <td>Sets and gets global texture paths (Preferences-&gt;Files-&gt;Paths).</td>
    </tr>
    <tr>
      <th colspan="2" align="left"><h4><a id="scripts-math"></a>Math</h4></th>
    </tr>
    <tr>
      <td><a href="examples/math/_c4d_geraycollider.py">examples/math/_c4d_geraycollider.py</a></td>
      <td>Demonstrates ray casting.</td>
    </tr>
    <tr>
      <td><a href="examples/math/_c4d_kdtree.py">examples/math/_c4d_kdtree.py</a></td>
      <td>Demonstrates how to use KDTree to find neighboring points in a mesh.</td>
    </tr>
    <tr>
      <td><a href="examples/math/_c4d_matrix.py">examples/math/_c4d_matrix.py</a></td>
      <td>Demonstrates working with matrices.</td>
    </tr>
    <tr>
      <td><a href="examples/math/_c4d_noise.py">examples/math/_c4d_noise.py</a></td>
      <td>Demonstrates working with noise functions.</td>
    </tr>
    <tr>
      <td><a href="examples/math/_c4d_quaternion.py">examples/math/_c4d_quaternion.py</a></td>
      <td>Demonstrates working with quaternions.</td>
    </tr>
    <tr>
      <td><a href="examples/math/_c4d_vector.py">examples/math/_c4d_vector.py</a></td>
      <td>Demonstrates working with vectors.</td>
    </tr>
    <tr>
      <td><a href="examples/math/_mxutils_random.py">examples/math/_mxutils_random.py</a></td>
      <td>Demonstrates deterministic random values with mxutils.Random.</td>
    </tr>
    <tr>
      <th colspan="2" align="left"><h4><a id="scripts-misc"></a>Misc</h4></th>
    </tr>
    <tr>
      <td><a href="examples/misc/mxutils_checktype.py">examples/misc/mxutils_checktype.py</a></td>
      <td>Demonstrates type and iterable validation with mxutils.</td>
    </tr>
    <tr>
      <td><a href="examples/misc/mxutils_debugprint.py">examples/misc/mxutils_debugprint.py</a></td>
      <td>Demonstrates mxutils helpers for diagnosing Cinema 4D scene data.</td>
    </tr>
    <tr>
      <td><a href="examples/misc/mxutils_decorators.py">examples/misc/mxutils_decorators.py</a></td>
      <td>Demonstrates mxutils helpers for diagnosing Cinema 4D scene data.</td>
    </tr>
    <tr>
      <td><a href="examples/misc/mxutils_localimportpath.py">examples/misc/mxutils_localimportpath.py</a></td>
      <td>Demonstrates importing a package relative to a saved Python script.</td>
    </tr>
    <tr>
      <td><a href="examples/misc/mxutils_symboltranslationcache.py">examples/misc/mxutils_symboltranslationcache.py</a></td>
      <td>Demonstrates translating Cinema 4D symbols with SymbolTranslationCache.</td>
    </tr>
    <tr>
      <td><a href="examples/misc/script_load.py">examples/misc/script_load.py</a></td>
      <td>Create a new temporary script. Load an existing Python file into the Script Manager. Retrieve the first script not active in the Script Manager and make it active.</td>
    </tr>
    <tr>
      <th colspan="2" align="left"><h4><a id="scripts-modeling"></a>Modeling</h4></th>
    </tr>
    <tr>
      <td><a href="examples/modeling/geometry_cache.py">examples/modeling/geometry_cache.py</a></td>
      <td>Explains the geometry model of the Cinema API in Cinema 4D.</td>
    </tr>
    <tr>
      <td><a href="examples/modeling/geometry_edges.py">examples/modeling/geometry_edges.py</a></td>
      <td>Demonstrates handling edges in polygon objects at the example of splitting edges.</td>
    </tr>
    <tr>
      <td><a href="examples/modeling/geometry_extrude.py">examples/modeling/geometry_extrude.py</a></td>
      <td>Demonstrates how to modify polygonal geometry at the example of extruding polygons.</td>
    </tr>
    <tr>
      <td><a href="examples/modeling/geometry_flatten.py">examples/modeling/geometry_flatten.py</a></td>
      <td>Demonstrates how to deform points of a point object at the example of &#x27;flattening&#x27; the selected polygons in a polygon object.</td>
    </tr>
    <tr>
      <td><a href="examples/modeling/geometry_polygon_object.py">examples/modeling/geometry_polygon_object.py</a></td>
      <td>Explains the user-editable polygon object model of the Cinema API.</td>
    </tr>
    <tr>
      <td><a href="examples/modeling/geometry_sds_weights.py">examples/modeling/geometry_sds_weights.py</a></td>
      <td>Demonstrates how to read and write data of an SDS weight tag.</td>
    </tr>
    <tr>
      <td><a href="examples/modeling/geometry_spline_object.py">examples/modeling/geometry_spline_object.py</a></td>
      <td>Explains the user-editable spline object model of the Cinema API.</td>
    </tr>
    <tr>
      <td><a href="examples/modeling/geometry_transfer_axis.py">examples/modeling/geometry_transfer_axis.py</a></td>
      <td>Demonstrates how to &#x27;transfer&#x27; the axis of a point object to another object while keeping its vertices in place.</td>
    </tr>
    <tr>
      <td><a href="examples/modeling/lod.py">examples/modeling/lod.py</a></td>
      <td>Demonstrates creating and configuring LOD objects.</td>
    </tr>
    <tr>
      <td><a href="examples/modeling/modeling_command_bridge.py">examples/modeling/modeling_command_bridge.py</a></td>
      <td>Demonstrates how to execute the &#x27;Bridge&#x27; tool.</td>
    </tr>
    <tr>
      <td><a href="examples/modeling/modeling_command_current_state.py">examples/modeling/modeling_command_current_state.py</a></td>
      <td>Demonstrates how to execute the &#x27;Current State to Object&#x27; tool.</td>
    </tr>
    <tr>
      <td><a href="examples/modeling/modeling_command_edge_smooth.py">examples/modeling/modeling_command_edge_smooth.py</a></td>
      <td>Demonstrates how to execute the &#x27;Edge Smooth&#x27; tool.</td>
    </tr>
    <tr>
      <td><a href="examples/modeling/modeling_command_extrude.py">examples/modeling/modeling_command_extrude.py</a></td>
      <td>Demonstrates how to use the <code>SendModelingCommand</code> (SMC) function in general at the example of the &#x27;Extrude&#x27; tool.</td>
    </tr>
    <tr>
      <td><a href="examples/modeling/modeling_command_flatten.py">examples/modeling/modeling_command_flatten.py</a></td>
      <td>Demonstrates how to execute the &#x27;Flatten&#x27; tool.</td>
    </tr>
    <tr>
      <td><a href="examples/modeling/modeling_command_join.py">examples/modeling/modeling_command_join.py</a></td>
      <td>Demonstrates how to execute the &#x27;Join&#x27; tool.</td>
    </tr>
    <tr>
      <td><a href="examples/modeling/normal_tag.py">examples/modeling/normal_tag.py</a></td>
      <td>Script creates a NormalTag for a selected polygon object with a phong tag where the normals have been rotated by 45° around the world z-axis. Showcases read and write operations for the normals of a NormalTag. Normals are stored for each vertex of each polygon. Raw data normal structure for one polygon is 12 int16 value (4 vectors for each vertex of a Cpolygon * 3 components for each vector), even if the Cpolygon is a triangle.</td>
    </tr>
    <tr>
      <td><a href="examples/modeling/reduction_create.py">examples/modeling/reduction_create.py</a></td>
      <td>Creates a new PolygonReduction object.</td>
    </tr>
    <tr>
      <td><a href="examples/modeling/reduction_edge_level.py">examples/modeling/reduction_edge_level.py</a></td>
      <td>Reduces the active PolygonObject to the given edge count.</td>
    </tr>
    <tr>
      <td><a href="examples/modeling/reduction_preprocess.py">examples/modeling/reduction_preprocess.py</a></td>
      <td>Configures the given PolygonReduction object. Reduces the given PolygonObject to 25%.</td>
    </tr>
    <tr>
      <td><a href="examples/modeling/reduction_triangle_level.py">examples/modeling/reduction_triangle_level.py</a></td>
      <td>Copyright: MAXON Computer GmbH Author: Yannick Puech</td>
    </tr>
    <tr>
      <td><a href="examples/modeling/reduction_vertex_level.py">examples/modeling/reduction_vertex_level.py</a></td>
      <td>Reduces the active PolygonObject to the given vertex count.</td>
    </tr>
    <tr>
      <td><a href="examples/modeling/snap_3d_point.py">examples/modeling/snap_3d_point.py</a></td>
      <td>Enables the snap if it&#x27;s not already the case. Sets it to 3D Type and also to Point mode.</td>
    </tr>
    <tr>
      <td><a href="examples/modeling/snap_quantize.py">examples/modeling/snap_quantize.py</a></td>
      <td>Enables the quantize if it&#x27;s not already the case. Defines quantize Move and Scale step.</td>
    </tr>
    <tr>
      <td><a href="examples/modeling/snap_workplane.py">examples/modeling/snap_workplane.py</a></td>
      <td>Retrieves the current workplane position and object. Locks this workplane so it can&#x27;t be edited.</td>
    </tr>
    <tr>
      <td><a href="examples/modeling/uv_command.py">examples/modeling/uv_command.py</a></td>
      <td>Calls BodyPaint 3D UV commands.</td>
    </tr>
    <tr>
      <td><a href="examples/modeling/uv_geometry.py">examples/modeling/uv_geometry.py</a></td>
      <td>Explains how to generate UVW data for polygon objects.</td>
    </tr>
    <tr>
      <td><a href="examples/modeling/uv_pin_deselect.py">examples/modeling/uv_pin_deselect.py</a></td>
      <td>Removes the polygon point selection to the uv points pinned.</td>
    </tr>
    <tr>
      <td><a href="examples/modeling/uv_pin_points.py">examples/modeling/uv_pin_points.py</a></td>
      <td>Sets the polygon point selection to the uv points pinned.</td>
    </tr>
    <tr>
      <td><a href="examples/modeling/uv_pin_select.py">examples/modeling/uv_pin_select.py</a></td>
      <td>Adds the polygon point selection to the uv points pinned.</td>
    </tr>
    <tr>
      <td><a href="examples/modeling/uv_seams.py">examples/modeling/uv_seams.py</a></td>
      <td>Copies the UV seams to the edge polygon selection.</td>
    </tr>
    <tr>
      <td><a href="examples/modeling/vertex_color_points.py">examples/modeling/vertex_color_points.py</a></td>
      <td>Gets and Sets Vertex Colors in Point mode: Changes all black Vertex Colors to red.</td>
    </tr>
    <tr>
      <td><a href="examples/modeling/vertex_color_polygons.py">examples/modeling/vertex_color_polygons.py</a></td>
      <td>Gets and Sets Vertex Colors in Polygon mode: Changes all vertex colors to red.</td>
    </tr>
    <tr>
      <td><a href="examples/modeling/volume_boolean_mesh.py">examples/modeling/volume_boolean_mesh.py</a></td>
      <td>Converts a Polygon Object to a Volume. Does a boolean operation over two Volume objects. Converts the resulting volume into a Polygon Object.</td>
    </tr>
    <tr>
      <td><a href="examples/modeling/volume_builder_access.py">examples/modeling/volume_builder_access.py</a></td>
      <td>Retrieves a volume object from a volume builder.</td>
    </tr>
    <tr>
      <td><a href="examples/modeling/volume_builder_add_object.py">examples/modeling/volume_builder_add_object.py</a></td>
      <td>Creates a volume builder and adds a cube object to it. Configures cube&#x27;s object settings.</td>
    </tr>
    <tr>
      <td><a href="examples/modeling/volume_builder_create.py">examples/modeling/volume_builder_create.py</a></td>
      <td>Creates a volume builder and inserts it into the active document.</td>
    </tr>
    <tr>
      <td><a href="examples/modeling/volume_builder_inputs.py">examples/modeling/volume_builder_inputs.py</a></td>
      <td>Iterates over all input of a Volume Builder.</td>
    </tr>
    <tr>
      <td><a href="examples/modeling/volume_command_sphere.py">examples/modeling/volume_command_sphere.py</a></td>
      <td>Creates a sphere volume with the corresponding command.</td>
    </tr>
    <tr>
      <td><a href="examples/modeling/volume_command_spline.py">examples/modeling/volume_command_spline.py</a></td>
      <td>Creates a volume from the selected spline object.</td>
    </tr>
    <tr>
      <td><a href="examples/modeling/volume_curl.py">examples/modeling/volume_curl.py</a></td>
      <td>Creates a new vector volume object with a curl filter applied from an existing Volume Builder set as vector mode.</td>
    </tr>
    <tr>
      <td><a href="examples/modeling/volume_export_mesh.py">examples/modeling/volume_export_mesh.py</a></td>
      <td>Convert a Polygon Object to a Volume and save this volume to a VDB File Save a VDB file.</td>
    </tr>
    <tr>
      <td><a href="examples/modeling/volume_gradient_sphere.py">examples/modeling/volume_gradient_sphere.py</a></td>
      <td>Create a Spherical Volume filled with gradient data.</td>
    </tr>
    <tr>
      <td><a href="examples/modeling/volume_grid_read.py">examples/modeling/volume_grid_read.py</a></td>
      <td>Reads the Float value of the first channel available from a Volume stored in a Volume Builder.</td>
    </tr>
    <tr>
      <td><a href="examples/modeling/volume_grid_write.py">examples/modeling/volume_grid_write.py</a></td>
      <td>Create a volume from scratch and assign values to voxels.</td>
    </tr>
    <tr>
      <td><a href="examples/modeling/volume_import_vdb.py">examples/modeling/volume_import_vdb.py</a></td>
      <td>Loads a VDB file to a c4d.VolumeObject.</td>
    </tr>
    <tr>
      <td><a href="examples/modeling/volume_mesh_conversion.py">examples/modeling/volume_mesh_conversion.py</a></td>
      <td>Convert a Polygon Object to a Volume and convert it back to a Polygon Object</td>
    </tr>
    <tr>
      <td><a href="examples/modeling/volume_mix_meshes.py">examples/modeling/volume_mix_meshes.py</a></td>
      <td>Converts a Polygon Object to a FOG Volume. Does a mix operation over two FOG Volume objects. Converts the resulting FOG volume into a Polygon Object.</td>
    </tr>
    <tr>
      <td><a href="examples/modeling/volume_mix_vectors.py">examples/modeling/volume_mix_vectors.py</a></td>
      <td>Creates 2 vector volume from scratch. Mixes both vector volumes with a cross product to produce a third vector volume. Inserts all 3 volumes into the scene.</td>
    </tr>
    <tr>
      <td><a href="examples/modeling/volume_vdb_import.py">examples/modeling/volume_vdb_import.py</a></td>
      <td>Asks for a VDB file to load into a VolumeRef (a VolumeInterface Reference). Insert this VolumeRef into a VolumeObject. Inserts this VolumeObject into the current scene.</td>
    </tr>
    <tr>
      <td><a href="examples/modeling/volume_vector_to_fog.py">examples/modeling/volume_vector_to_fog.py</a></td>
      <td>Creates a vector volume from scratch. Converts this vector volume to a fog volume. Inserts this fog volume as a child of a volume mesher.</td>
    </tr>
    <tr>
      <th colspan="2" align="left"><h4><a id="scripts-nodes"></a>Nodes</h4></th>
    </tr>
    <tr>
      <td><a href="examples/nodes/graph_descriptions_basics.py">examples/nodes/graph_descriptions_basics.py</a></td>
      <td>Demonstrates how graph descriptions create and modify node graphs.</td>
    </tr>
    <tr>
      <td><a href="examples/nodes/graph_descriptions_commands.py">examples/nodes/graph_descriptions_commands.py</a></td>
      <td>Demonstrates graph description commands.</td>
    </tr>
    <tr>
      <td><a href="examples/nodes/graph_descriptions_queries.py">examples/nodes/graph_descriptions_queries.py</a></td>
      <td>Demonstrates graph description queries, including lazy color and vector literals.</td>
    </tr>
    <tr>
      <td><a href="examples/nodes/graph_descriptions_references.py">examples/nodes/graph_descriptions_references.py</a></td>
      <td>Demonstrates graph description references together with lazy color and URL literals.</td>
    </tr>
    <tr>
      <td><a href="examples/nodes/nodes_associate_nodes.py">examples/nodes/nodes_associate_nodes.py</a></td>
      <td>Demonstrates how to associate nodes in a Maxon API graph with their corresponding Cinema 4D API surrogate elements.</td>
    </tr>
    <tr>
      <td><a href="examples/nodes/nodes_create_or_get_graphs.py">examples/nodes/nodes_create_or_get_graphs.py</a></td>
      <td>Demonstrates creating or getting node graphs in a scene.</td>
    </tr>
    <tr>
      <td><a href="examples/nodes/nodes_graph_entities.py">examples/nodes/nodes_graph_entities.py</a></td>
      <td>Demonstrates the inner structure of node graphs and how to find entities in them.</td>
    </tr>
    <tr>
      <td><a href="examples/nodes/nodes_group.py">examples/nodes/nodes_group.py</a></td>
      <td>Retrieve the selected node material and group the node that are selected.</td>
    </tr>
    <tr>
      <td><a href="examples/nodes/nodes_info.py">examples/nodes/nodes_info.py</a></td>
      <td>Retrieve information about the selected port of a selected material.</td>
    </tr>
    <tr>
      <td><a href="examples/nodes/nodes_material_access.py">examples/nodes/nodes_material_access.py</a></td>
      <td>Demonstrates accessing node materials and their graph contents in a scene.</td>
    </tr>
    <tr>
      <td><a href="examples/nodes/nodes_material_create_redshift.py">examples/nodes/nodes_material_create_redshift.py</a></td>
      <td>Demonstrates setting up a Redshift node material composed out of multiple nodes.</td>
    </tr>
    <tr>
      <td><a href="examples/nodes/nodes_material_standard.py">examples/nodes/nodes_material_standard.py</a></td>
      <td>Demonstrates setting up a Standard renderer node material composed out of multiple nodes.</td>
    </tr>
    <tr>
      <td><a href="examples/nodes/nodes_modify_port.py">examples/nodes/nodes_modify_port.py</a></td>
      <td>Create a material for the standard node space and modify the value of the BDSF color port.</td>
    </tr>
    <tr>
      <td><a href="examples/nodes/nodes_selection.py">examples/nodes/nodes_selection.py</a></td>
      <td>This example shows how to select different elements on a node graph. It creates a node material, select ports, print connections and select wires.</td>
    </tr>
    <tr>
      <td><a href="examples/nodes/nodes_solo.py">examples/nodes/nodes_solo.py</a></td>
      <td>This example shows how to solo a node. It creates a material and solo&#x27;s the end node in this material.</td>
    </tr>
    <tr>
      <td><a href="examples/nodes/nodes_wire_mute.py">examples/nodes/nodes_wire_mute.py</a></td>
      <td>Retrieve the selected node material and toggle-mute the selected connection, i.e., if the connection is muted, it will be unmuted or vice-versa. A connection is composed out of eight wires, to mute the connection, one must set the INHIBIT wire to WIRE_MODE.NORMAL. To unmute the connection, one must set the INHIBIT wire to WIRE_MODE.REMOVE.</td>
    </tr>
    <tr>
      <td><a href="examples/nodes/xpresso_create_connect.py">examples/nodes/xpresso_create_connect.py</a></td>
      <td>Creates a Constants and Results node in the Xpresso Tag of the selected object. Connects both Nodes together.</td>
    </tr>
    <tr>
      <td><a href="examples/nodes/xpresso_delete.py">examples/nodes/xpresso_delete.py</a></td>
      <td>Deletes the first node created from the Xpresso Tag of the selected object.</td>
    </tr>
    <tr>
      <td><a href="examples/nodes/xpresso_from_tag.py">examples/nodes/xpresso_from_tag.py</a></td>
      <td>Retrieves the Node Master (The BaseList2D object that holds all nodes) from an Xpresso Tag.</td>
    </tr>
    <tr>
      <td><a href="examples/nodes/xpresso_iterate.py">examples/nodes/xpresso_iterate.py</a></td>
      <td>Loops through all nodes from the Xpresso Tag of the selected object. Checks if it&#x27;s a Constant Node.</td>
    </tr>
    <tr>
      <td><a href="examples/nodes/xpresso_move.py">examples/nodes/xpresso_move.py</a></td>
      <td>Moves the first node in the Graph View created from the Xpresso Tag of the selected object.</td>
    </tr>
    <tr>
      <th colspan="2" align="left"><h4><a id="scripts-plugins"></a>Plugins</h4></th>
    </tr>
    <tr>
      <td><a href="examples/plugins/py_cmd_gui_resources/unicode_encode_strings.py">examples/plugins/py_cmd_gui_resources/unicode_encode_strings.py</a></td>
      <td>Provides an example for how one could realize a string encoding pipeline for plugin resources.</td>
    </tr>
    <tr>
      <th colspan="2" align="left"><h4><a id="scripts-rendering"></a>Rendering</h4></th>
    </tr>
    <tr>
      <td><a href="examples/rendering/_c4d_renderdata.py">examples/rendering/_c4d_renderdata.py</a></td>
      <td>No short description provided.</td>
    </tr>
    <tr>
      <td><a href="examples/rendering/batch_render_postprocess.py">examples/rendering/batch_render_postprocess.py</a></td>
      <td>Demonstrates to manipulate the file outputs of a batch render post process once the rendering has finished.</td>
    </tr>
    <tr>
      <td><a href="examples/rendering/batch_render_preprocess.py">examples/rendering/batch_render_preprocess.py</a></td>
      <td>Demonstrates how to pre-process multiple documents before adding them to the batch renderer for rendering.</td>
    </tr>
    <tr>
      <td><a href="examples/rendering/ocio.py">examples/rendering/ocio.py</a></td>
      <td>Demonstrates how to read, write, and convert colors in an OpenColorIO (OCIO) color-managed document in Cinema 4D.</td>
    </tr>
    <tr>
      <td><a href="examples/rendering/render_complex.py">examples/rendering/render_complex.py</a></td>
      <td>Demonstrates the details and manual handling of a programmatic rendering process.</td>
    </tr>
    <tr>
      <td><a href="examples/rendering/render_hardware.py">examples/rendering/render_hardware.py</a></td>
      <td>Demonstrates how carry out a &#x27;hardware preview&#x27; rendering, i.e., a rendering of what is shown in the viewport using the hardware renderer.</td>
    </tr>
    <tr>
      <td><a href="examples/rendering/render_openexr.py">examples/rendering/render_openexr.py</a></td>
      <td>Configures OpenEXR output render format with SetImageSettingsDictionary() then reads these with GetImageSettingsDictionary().</td>
    </tr>
    <tr>
      <td><a href="examples/rendering/render_preroll.py">examples/rendering/render_preroll.py</a></td>
      <td>Demonstrates how to render document from or at a given frame after prerolling it.</td>
    </tr>
    <tr>
      <td><a href="examples/rendering/render_set_engine.py">examples/rendering/render_set_engine.py</a></td>
      <td>Demonstrates how to manipulate the render settings of a rendering, specifically also the used render engine.</td>
    </tr>
    <tr>
      <td><a href="examples/rendering/render_simple.py">examples/rendering/render_simple.py</a></td>
      <td>Demonstrates a simple way to programmatically render a document to either memory or disk.</td>
    </tr>
    <tr>
      <td><a href="examples/rendering/render_tiles.py">examples/rendering/render_tiles.py</a></td>
      <td>Demonstrates how to render a document split into tiles which can be composited back together to a full image.</td>
    </tr>
    <tr>
      <td><a href="examples/rendering/render_token.py">examples/rendering/render_token.py</a></td>
      <td>Renders a BaseDocument and saves the resulting image using a filename handling tokens.</td>
    </tr>
    <tr>
      <th colspan="2" align="left"><h4><a id="scripts-scene"></a>Scene</h4></th>
    </tr>
    <tr>
      <td><a href="examples/scene/_c4d_atom.py">examples/scene/_c4d_atom.py</a></td>
      <td>Demonstrates important functions for the type c4d.C4DAtom.</td>
    </tr>
    <tr>
      <td><a href="examples/scene/_c4d_baselist2d.py">examples/scene/_c4d_baselist2d.py</a></td>
      <td>Demonstrates important functions for the type c4d.BaseList2D.</td>
    </tr>
    <tr>
      <td><a href="examples/scene/_c4d_gelistnode.py">examples/scene/_c4d_gelistnode.py</a></td>
      <td>Demonstrates important functions for the type c4d.GeListNode.</td>
    </tr>
    <tr>
      <td><a href="examples/scene/documents.py">examples/scene/documents.py</a></td>
      <td>Demonstrates basic document operations.</td>
    </tr>
    <tr>
      <td><a href="examples/scene/layers.py">examples/scene/layers.py</a></td>
      <td>Demonstrates how to assign a scene element to a layer.</td>
    </tr>
    <tr>
      <td><a href="examples/scene/objects.py">examples/scene/objects.py</a></td>
      <td>Demonstrates basic operations on objects.</td>
    </tr>
    <tr>
      <td><a href="examples/scene/parameters.py">examples/scene/parameters.py</a></td>
      <td>Demonstrates different ways to access and modify parameters of Cinema 4D scene elements.</td>
    </tr>
    <tr>
      <td><a href="examples/scene/takes.py">examples/scene/takes.py</a></td>
      <td>Demonstrates the fundamental operations of the Take System.</td>
    </tr>
    <tr>
      <td><a href="examples/scene/traversal.py">examples/scene/traversal.py</a></td>
      <td>Demonstrates scene traversal.</td>
    </tr>
    <tr>
      <td><a href="examples/scene/undos.py">examples/scene/undos.py</a></td>
      <td>Demonstrates adding undo steps for document modifications.</td>
    </tr>
    <tr>
      <td><a href="examples/scene/userdata.py">examples/scene/userdata.py</a></td>
      <td>Demonstrates how to work with user data parameters.</td>
    </tr>
  </tbody>
</table>
