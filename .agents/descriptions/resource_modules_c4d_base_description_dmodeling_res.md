# Description: Modeling Settings

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/c4d_base/description/dmodeling.res`
- **Symbol:** `dmodeling`
- **Category:** Other

Use parameter symbols to access parameters and cycle option symbols for cycle values, never their numeric IDs. Treat Min and Max as constraints and Default as the declared initial value; blank cells mean the resource does not declare that metadata, not that the value is zero. Base Description Parameters lists inherited fields from each base; All Parameters lists the effective parameter set for this description.

## Base Description Parameters

No base descriptions.

## All Parameters

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Snap | SNAP_SETTINGS_ENABLED | BOOL |  |  |  | 
Tool Specific | SNAP_SETTINGS_TOOL | BOOL |  |  |  | 
No label | SNAPMODE_COMBO | LONG |  |  |  | 
Snap Radius | SNAP_SETTINGS_RADIUS | REAL | 0.1 | 100 |  | 
Point | SNAPMODE_POINT | BOOL |  |  |  | 
Edge | SNAPMODE_EDGE | BOOL |  |  |  | 
Polygon | SNAPMODE_POLYGON | BOOL |  |  |  | 
Spline | SNAPMODE_SPLINE | BOOL |  |  |  | 
Axis | SNAPMODE_AXIS | BOOL |  |  |  | 
Intersections | SNAPMODE_INTERSECTION | BOOL |  |  |  | 
Mid Point | SNAPMODE_MIDPOINT | BOOL |  |  |  | 
Grid/Workplane | SNAPMODE_WORKPLANE | BOOL |  |  |  | 
Grid Point | SNAPMODE_GRIDPOINT | BOOL |  |  |  | 
Grid Line | SNAPMODE_GRIDLINE | BOOL |  |  |  | 
Guides | SNAPMODE_GUIDE | BOOL |  |  |  | 
Dynamic Guides | SNAPMODE_DYNAMICGUIDE | BOOL |  |  |  | 
Perpendicular | SNAPMODE_ORTHO | BOOL |  |  |  | 
Pixel | SNAPMODE_PIXEL | BOOL |  |  |  | 
Pixel Position | SNAP_SETTINGS_PIXELMODE | LONG |  |  |  | SNAP_SETTINGS_PIXELMODE_EDGE; SNAP_SETTINGS_PIXELMODE_CENTER
Quantize | QUANTIZE_ENABLED | BOOL |  |  |  | 
Move | QUANTIZE_MOVE | REAL | 0.001 |  |  | 
Rotate | QUANTIZE_ROTATE | REAL | 0.1 | 180.0 |  | 
Scale | QUANTIZE_SCALE | REAL | 0.01 |  |  | 
Move (UV) | QUANTIZE_TEXTURE | REAL | 0.01 | 1.0 |  | 
Guide Angle | SNAP_SETTINGS_GUIDEANGLE | REAL | 0.1 | 180.0 |  | 
Check Mesh | MESH_CHECK_ENABLED | BOOL |  |  |  | 
Isolated Points | MESH_CHECK_POINT | BOOL |  |  |  | 
Color | MESH_CHECK_POINT_COLOR | COLOR |  |  |  | 
&gt;&gt; | MESH_CHECK_POINT_SELECT | BUTTON |  |  |  | 
No label | MESH_CHECK_POINT_TEXT | STATICTEXT |  |  |  | 
Edge Points | MESH_CHECK_EDGEPOINT | BOOL |  |  |  | 
Color | MESH_CHECK_EDGEPOINT_COLOR | COLOR |  |  |  | 
&gt;&gt; | MESH_CHECK_EDGEPOINT_SELECT | BUTTON |  |  |  | 
No label | MESH_CHECK_EDGEPOINT_TEXT | STATICTEXT |  |  |  | 
Edge Points Angle Threshold | MESH_CHECK_EDGEPOINT_THRESHOLD | REAL | 0.0 | 180.0 |  | 
Complex Poles | MESH_CHECK_POLEPOINT | BOOL |  |  |  | 
Color | MESH_CHECK_POLEPOINT_COLOR | COLOR |  |  |  | 
&gt;&gt; | MESH_CHECK_POLEPOINT_SELECT | BUTTON |  |  |  | 
No label | MESH_CHECK_POLEPOINT_TEXT | STATICTEXT |  |  |  | 
Edge Count | MESH_CHECK_POLE_MIN | LONG | 3 |  |  | 
Non-Manifold | MESH_CHECK_MANIFOLD | BOOL |  |  |  | 
Color | MESH_CHECK_MANIFOLD_COLOR | COLOR |  |  |  | 
&gt;&gt; | MESH_CHECK_MANIFOLD_SELECT | BUTTON |  |  |  | 
No label | MESH_CHECK_MANIFOLD_TEXT | STATICTEXT |  |  |  | 
Boundary Edges | MESH_CHECK_BOUNDARY | BOOL |  |  |  | 
Color | MESH_CHECK_BOUNDARY_COLOR | COLOR |  |  |  | 
&gt;&gt; | MESH_CHECK_BOUNDARY_SELECT | BUTTON |  |  |  | 
No label | MESH_CHECK_BOUNDARY_TEXT | STATICTEXT |  |  |  | 
Bad Polygons | MESH_CHECK_POLY | BOOL |  |  |  | 
Color | MESH_CHECK_POLY_COLOR | COLOR |  |  |  | 
&gt;&gt; | MESH_CHECK_POLY_SELECT | BUTTON |  |  |  | 
No label | MESH_CHECK_POLY_TEXT | STATICTEXT |  |  |  | 
Not Planar Polygons | MESH_CHECK_NORMAL | BOOL |  |  |  | 
Color | MESH_CHECK_NORMAL_COLOR | COLOR |  |  |  | 
&gt;&gt; | MESH_CHECK_NORMAL_SELECT | BUTTON |  |  |  | 
No label | MESH_CHECK_NORMAL_TEXT | STATICTEXT |  |  |  | 
Planarity Threshold | MESH_CHECK_NORMAL_THRESHOLD | REAL | 0.0 | 180.0 |  | 
Triangles | MESH_CHECK_TRIANGLE | BOOL |  |  |  | 
Color | MESH_CHECK_TRIANGLE_COLOR | COLOR |  |  |  | 
&gt;&gt; | MESH_CHECK_TRIANGLE_SELECT | BUTTON |  |  |  | 
No label | MESH_CHECK_TRIANGLE_TEXT | STATICTEXT |  |  |  | 
Ngons | MESH_CHECK_NGON | BOOL |  |  |  | 
Color | MESH_CHECK_NGON_COLOR | COLOR |  |  |  | 
&gt;&gt; | MESH_CHECK_NGON_SELECT | BUTTON |  |  |  | 
No label | MESH_CHECK_NGON_TEXT | STATICTEXT |  |  |  | 
Solo | MODELING_OPTION_SOLO | BOOL |  |  |  | 
Preserve UV | MODELING_MODIFIERS_PRESERVE_UV | BOOL |  |  |  | 
