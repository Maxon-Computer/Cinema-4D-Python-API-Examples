# Description: Bevel Tool

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/c4d_objects/description/xbeveltool.res`
- **Symbol:** `xbeveltool`
- **Category:** Other

Use parameter symbols to access parameters and cycle option symbols for cycle values, never their numeric IDs. Treat Min and Max as constraints and Default as the declared initial value; blank cells mean the resource does not declare that metadata, not that the value is zero. Base Description Parameters lists inherited fields from each base; All Parameters lists the effective parameter set for this description.

## Base Description Parameters

### Base Tool (`ToolBase`)

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Realtime Update | MDATA_INTERACTIVE | BOOL |  |  |  | 
    Apply     | MDATA_APPLY | BUTTON |  |  |  | 
New Transform | MDATA_NEWTRANSFORM | BUTTON |  |  |  | 
No label | ID_SNAPSETTINGS | SUBCONTAINER |  |  |  | 

## All Parameters

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Bevel Mode | MDATA_BEVEL_MASTER_MODE | LONG |  |  |  | MDATA_BEVEL_MASTER_MODE_CHAMFER; MDATA_BEVEL_MASTER_MODE_SOLID
Offset Mode | MDATA_BEVEL_OFFSET_MODE | LONG |  |  |  | MDATA_BEVEL_OFFSET_MODE_FIXED; MDATA_BEVEL_OFFSET_MODE_RADIAL; MDATA_BEVEL_OFFSET_MODE_PROPORTIONAL
Offset | MDATA_BEVEL_RADIUS | REAL |  |  |  | 
Subdivision | MDATA_BEVEL_SUB | REAL | 0 |  |  | 
Depth | MDATA_BEVEL_DEPTH | REAL |  |  |  | 
Depth | MDATA_BEVEL_SHAPING_EXTR | REAL |  |  |  | 
Limit | MDATA_BEVEL_LIMIT | BOOL |  |  |  | 
Extrusion | MDATA_BEVEL_EXTRUSION | REAL |  |  |  | 
Max Angle | MDATA_BEVEL_POLY_ANGLE | REAL | 0 |  |  | 
Preserve Groups | MDATA_BEVEL_GROUP | BOOL |  |  |  | 
Shape | MDATA_BEVEL_SHAPING_MODE | LONG |  |  |  | MDATA_BEVEL_SHAPING_MODE_ROUND; MDATA_BEVEL_SHAPING_MODE_USER; MDATA_BEVEL_SHAPING_MODE_PROFILE
Tension | MDATA_BEVEL_SHAPING_TENSION | REAL |  |  |  | 
User Shape | MDATA_BEVEL_SHAPING_SPLINE | SPLINE |  |  |  | 
Profile Spline | MDATA_BEVEL_SHAPING_SPLINE_LINK | LINK |  |  |  | 
Profile Plane | MDATA_BEVEL_SHAPING_SPLINE_PLANE | LONG |  |  |  | MDATA_BEVEL_SHAPING_SPLINE_PLANE_XY; MDATA_BEVEL_SHAPING_SPLINE_PLANE_XZ; MDATA_BEVEL_SHAPING_SPLINE_PLANE_ZY
Symmetry | MDATA_BEVEL_SHAPING_SYMMETRY | BOOL |  |  |  | 
Constant Cross Section | MDATA_BEVELL_SHAPING_CONSTANT | BOOL |  |  |  | 
Mitering | MDATA_BEVEL_MITERING | LONG |  |  |  | MDATA_BEVEL_MITERING_DEFAULT; MDATA_BEVEL_MITERING_UNIFORM; MDATA_BEVEL_MITERING_RADIAL; MDATA_BEVEL_MITERING_PATCH
Ending | MDATA_BEVEL_CORNER_ENDING | LONG |  |  |  | MDATA_BEVEL_CORNER_ENDING_DEFAULT; MDATA_BEVEL_CORNER_ENDING_EXTEND; MDATA_BEVEL_CORNER_ENDING_INSET
Partial Rounding | MDATA_BEVEL_PROUNDING_TYPE | LONG |  |  |  | MDATA_BEVEL_PROUNDING_TYPE_FLAT; MDATA_BEVEL_PROUNDING_TYPE_FULL; MDATA_BEVEL_PROUNDING_TYPE_CONVEX
Corner N-gons | MDATA_BEVEL_CORNER_NGON | BOOL |  |  |  | 
Rounding N-gons | MDATA_BEVEL_ROUNDING_NGON | BOOL |  |  |  | 
Phong Break Rounding | MDATA_BEVEL_SELECTION_PHONG_BREAK | BOOL |  |  |  | 
Phong Break Miters | MDATA_BEVEL_SELECTION_PHONG_BREAK_M | BOOL |  |  |  | 
Realtime Update | MDATA_INTERACTIVE | BOOL |  |  |  | 
    Apply     | MDATA_APPLY | BUTTON |  |  |  | 
New Transform | MDATA_NEWTRANSFORM | BUTTON |  |  |  | 
No label | ID_SNAPSETTINGS | SUBCONTAINER |  |  |  | 
