# modeling

Modeling, meshes, splines, and UVs.

## Files
| File | Description |
| --- | --- |
| [README.md](README.md) | This file. |
| [geometry_cache.py](geometry_cache.py) | Explains the geometry model of the Cinema API in Cinema 4D. |
| [geometry_edges.py](geometry_edges.py) | Demonstrates handling edges in polygon objects at the example of splitting edges. |
| [geometry_extrude.py](geometry_extrude.py) | Demonstrates how to modify polygonal geometry at the example of extruding polygons. |
| [geometry_flatten.py](geometry_flatten.py) | Demonstrates how to deform points of a point object at the example of 'flattening' the selected polygons in a polygon object. |
| [geometry_polygon_object.py](geometry_polygon_object.py) | Explains the user-editable polygon object model of the Cinema API. |
| [geometry_sds_weights.py](geometry_sds_weights.py) | Demonstrates how to read and write data of an SDS weight tag. |
| [geometry_spline_object.py](geometry_spline_object.py) | Explains the user-editable spline object model of the Cinema API. |
| [geometry_transfer_axis.py](geometry_transfer_axis.py) | Demonstrates how to 'transfer' the axis of a point object to another object while keeping its vertices in place. |
| [lod.py](lod.py) | Demonstrates creating and configuring LOD objects. |
| [modeling_command_bridge.c4d](modeling_command_bridge.c4d) | No short description provided. |
| [modeling_command_bridge.png](modeling_command_bridge.png) | No short description provided. |
| [modeling_command_bridge.py](modeling_command_bridge.py) | Demonstrates how to execute the 'Bridge' tool. |
| [modeling_command_current_state.py](modeling_command_current_state.py) | Demonstrates how to execute the 'Current State to Object' tool. |
| [modeling_command_edge_smooth.py](modeling_command_edge_smooth.py) | Demonstrates how to execute the 'Edge Smooth' tool. |
| [modeling_command_extrude.py](modeling_command_extrude.py) | Demonstrates how to use the `SendModelingCommand` (SMC) function in general at the example of the 'Extrude' tool. |
| [modeling_command_flatten.py](modeling_command_flatten.py) | Demonstrates how to execute the 'Flatten' tool. |
| [modeling_command_join.py](modeling_command_join.py) | Demonstrates how to execute the 'Join' tool. |
| [normal_tag.py](normal_tag.py) | Script creates a NormalTag for a selected polygon object with a phong tag where the normals have been rotated by 45° around the world z-axis. Showcases read and write operations for the normals of a NormalTag. Normals are stored for each vertex of each polygon. Raw data normal structure for one polygon is 12 int16 value (4 vectors for each vertex of a Cpolygon * 3 components for each vector), even if the Cpolygon is a triangle. |
| [reduction_create.py](reduction_create.py) | Creates a new PolygonReduction object. |
| [reduction_edge_level.py](reduction_edge_level.py) | Reduces the active PolygonObject to the given edge count. |
| [reduction_preprocess.py](reduction_preprocess.py) | Configures the given PolygonReduction object. Reduces the given PolygonObject to 25%. |
| [reduction_triangle_level.py](reduction_triangle_level.py) | Copyright: MAXON Computer GmbH Author: Yannick Puech |
| [reduction_vertex_level.py](reduction_vertex_level.py) | Reduces the active PolygonObject to the given vertex count. |
| [snap_3d_point.py](snap_3d_point.py) | Enables the snap if it's not already the case. Sets it to 3D Type and also to Point mode. |
| [snap_quantize.py](snap_quantize.py) | Enables the quantize if it's not already the case. Defines quantize Move and Scale step. |
| [snap_workplane.py](snap_workplane.py) | Retrieves the current workplane position and object. Locks this workplane so it can't be edited. |
| [uv_command.py](uv_command.py) | Calls BodyPaint 3D UV commands. |
| [uv_geometry.py](uv_geometry.py) | Explains how to generate UVW data for polygon objects. |
| [uv_pin_deselect.py](uv_pin_deselect.py) | Removes the polygon point selection to the uv points pinned. |
| [uv_pin_points.py](uv_pin_points.py) | Sets the polygon point selection to the uv points pinned. |
| [uv_pin_select.py](uv_pin_select.py) | Adds the polygon point selection to the uv points pinned. |
| [uv_seams.py](uv_seams.py) | Copies the UV seams to the edge polygon selection. |
| [vertex_color_points.py](vertex_color_points.py) | Gets and Sets Vertex Colors in Point mode: Changes all black Vertex Colors to red. |
| [vertex_color_polygons.py](vertex_color_polygons.py) | Gets and Sets Vertex Colors in Polygon mode: Changes all vertex colors to red. |
| [volume_boolean_mesh.py](volume_boolean_mesh.py) | Converts a Polygon Object to a Volume. Does a boolean operation over two Volume objects. Converts the resulting volume into a Polygon Object. |
| [volume_builder_access.py](volume_builder_access.py) | Retrieves a volume object from a volume builder. |
| [volume_builder_add_object.py](volume_builder_add_object.py) | Creates a volume builder and adds a cube object to it. Configures cube's object settings. |
| [volume_builder_create.py](volume_builder_create.py) | Creates a volume builder and inserts it into the active document. |
| [volume_builder_inputs.py](volume_builder_inputs.py) | Iterates over all input of a Volume Builder. |
| [volume_command_sphere.py](volume_command_sphere.py) | Creates a sphere volume with the corresponding command. |
| [volume_command_spline.py](volume_command_spline.py) | Creates a volume from the selected spline object. |
| [volume_curl.py](volume_curl.py) | Creates a new vector volume object with a curl filter applied from an existing Volume Builder set as vector mode. |
| [volume_export_mesh.py](volume_export_mesh.py) | Convert a Polygon Object to a Volume and save this volume to a VDB File Save a VDB file. |
| [volume_gradient_sphere.py](volume_gradient_sphere.py) | Create a Spherical Volume filled with gradient data. |
| [volume_grid_read.py](volume_grid_read.py) | Reads the Float value of the first channel available from a Volume stored in a Volume Builder. |
| [volume_grid_write.py](volume_grid_write.py) | Create a volume from scratch and assign values to voxels. |
| [volume_import_vdb.py](volume_import_vdb.py) | Loads a VDB file to a c4d.VolumeObject. |
| [volume_mesh_conversion.py](volume_mesh_conversion.py) | Convert a Polygon Object to a Volume and convert it back to a Polygon Object |
| [volume_mix_meshes.py](volume_mix_meshes.py) | Converts a Polygon Object to a FOG Volume. Does a mix operation over two FOG Volume objects. Converts the resulting FOG volume into a Polygon Object. |
| [volume_mix_vectors.py](volume_mix_vectors.py) | Creates 2 vector volume from scratch. Mixes both vector volumes with a cross product to produce a third vector volume. Inserts all 3 volumes into the scene. |
| [volume_vdb_import.py](volume_vdb_import.py) | Asks for a VDB file to load into a VolumeRef (a VolumeInterface Reference). Insert this VolumeRef into a VolumeObject. Inserts this VolumeObject into the current scene. |
| [volume_vector_to_fog.py](volume_vector_to_fog.py) | Creates a vector volume from scratch. Converts this vector volume to a fog volume. Inserts this fog volume as a child of a volume mesher. |

## Related Examples

| Type | Example | Description |
| --- | --- | --- |
| Script | [objects](../scene/objects.py) | Demonstrates basic operations on objects. |
| Script | [voronoi_fracture](../animation/simulation/voronoi_fracture.py) | Creates and define a noise shader as an input of a Voronoi Fracture object. |
