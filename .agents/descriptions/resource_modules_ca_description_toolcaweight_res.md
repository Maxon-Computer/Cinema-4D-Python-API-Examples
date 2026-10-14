# Description: Weight

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/ca/description/toolcaweight.res`
- **Symbol:** `Toolcaweight`
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

### Weight Base (`ToolWeightBase`)

No parameters.

## All Parameters

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Realtime Update | MDATA_INTERACTIVE | BOOL |  |  |  | 
    Apply     | MDATA_APPLY | BUTTON |  |  |  | 
New Transform | MDATA_NEWTRANSFORM | BUTTON |  |  |  | 
No label | ID_SNAPSETTINGS | SUBCONTAINER |  |  |  | 
Projection | ID_CA_WEIGHT_TOOL_PROJECTION | BOOL |  |  |  | 
Visible Only | ID_CA_WEIGHT_TOOL_VISIBLE_ONLY | BOOL |  |  |  | 
Selected Only | ID_CA_WEIGHT_TOOL_SELECTED | BOOL |  |  |  | 
Auto Normalize | ID_CA_WEIGHT_TOOL_NORMALIZE | BOOL |  |  |  | 
Mode | ID_CA_WEIGHT_TOOL_MODE | LONG |  |  |  | ID_CA_WEIGHT_BASE_MODE_ADD; ID_CA_WEIGHT_BASE_MODE_SPRAY; ID_CA_WEIGHT_BASE_MODE_SUBTRACT; ID_CA_WEIGHT_BASE_MODE_ABS; ID_CA_WEIGHT_BASE_MODE_SMOOTH; ID_CA_WEIGHT_BASE_MODE_BLEED; ID_CA_WEIGHT_BASE_MODE_INTENSITY; ID_CA_WEIGHT_BASE_MODE_REMAP; ID_CA_WEIGHT_BASE_MODE_PRUNE; ID_CA_WEIGHT_BASE_MODE_DROPPER; ID_CA_WEIGHT_BASE_MODE_HAMMER
Strength | ID_CA_WEIGHT_TOOL_STRENGTH | REAL | -100.0 | 100.0 |  | 
Curve | ID_CA_WEIGHT_TOOL_SPLINE | SPLINE |  |  |  | 
Falloff | ID_CA_WEIGHT_TOOL_FALLOFF | LONG |  |  |  | ID_CA_WEIGHT_TOOL_FALLOFF_NONE; ID_CA_WEIGHT_TOOL_FALLOFF_SIMPLE; ID_CA_WEIGHT_TOOL_FALLOFF_LINEAR; ID_CA_WEIGHT_TOOL_FALLOFF_DOME; ID_CA_WEIGHT_TOOL_FALLOFF_BELL; ID_CA_WEIGHT_TOOL_FALLOFF_CIRCLE; ID_CA_WEIGHT_TOOL_FALLOFF_NEEDLE; ID_CA_WEIGHT_TOOL_FALLOFF_SPLINE
Pressure | ID_CA_WEIGHT_TOOL_PEN | LONG |  |  |  | ID_CA_WEIGHT_TOOL_PEN_NONE; ID_CA_WEIGHT_TOOL_PEN_RADIUS; ID_CA_WEIGHT_TOOL_PEN_STRENGTH; ID_CA_WEIGHT_TOOL_PEN_HARDNESS
Radius | ID_CA_WEIGHT_TOOL_RADIUS | REAL | 0.0 |  |  | 
Width | ID_CA_WEIGHT_TOOL_WIDTH | REAL | 0.0 | 100.0 |  | 
Hardness | ID_CA_WEIGHT_TOOL_HARDNESS | REAL | 0.0 | 100.0 |  | 
Curve | ID_CA_WEIGHT_TOOL_FALLOFF_CURVE | SPLINE |  |  |  | 
Clamp | ID_CA_WEIGHT_TOOL_CLAMP_LOWER_ENABLE | BOOL |  |  |  | 
Lower | ID_CA_WEIGHT_TOOL_CLAMP_LOWER | REAL | 0.0 | 100.0 |  | 
Clamp | ID_CA_WEIGHT_TOOL_CLAMP_UPPER_ENABLE | BOOL |  |  |  | 
Upper | ID_CA_WEIGHT_TOOL_CLAMP_UPPER | REAL | 0.0 | 100.0 |  | 
Enable | ID_CA_WEIGHT_TOOL_SYMMETRY | BOOL |  |  |  | 
Mode | ID_CA_WEIGHT_TOOL_SYMMETRY_MODE | LONG |  |  |  | ID_CA_WEIGHT_TOOL_SYMMETRY_MODE_NONE; ID_CA_WEIGHT_TOOL_SYMMETRY_MODE_NAME; ID_CA_WEIGHT_TOOL_SYMMETRY_MODE_HIEARCHY
Search | ID_CA_WEIGHT_TOOL_SYMMETRY_RAD | REAL | 0.0 |  |  | 
Left | ID_CA_WEIGHT_TOOL_SYMMETRY_MODE_NAME_LEFT | STRING |  |  |  | 
Right | ID_CA_WEIGHT_TOOL_SYMMETRY_MODE_NAME_RIGHT | STRING |  |  |  | 
Coord | ID_CA_WEIGHT_TOOL_SYMMETRY_COORD | LONG |  |  |  | ID_CA_WEIGHT_TOOL_SYMMETRY_COORD_LOCAL; ID_CA_WEIGHT_TOOL_SYMMETRY_COORD_WORLD; ID_CA_WEIGHT_TOOL_SYMMETRY_COORD_CUSTOM
Mirror | ID_CA_WEIGHT_TOOL_SYMMETRY_MIRROR | LONG |  |  |  | ID_CA_WEIGHT_TOOL_SYMMETRY_MIRROR_XY; ID_CA_WEIGHT_TOOL_SYMMETRY_MIRROR_YZ; ID_CA_WEIGHT_TOOL_SYMMETRY_MIRROR_XZ
Object | ID_CA_WEIGHT_TOOL_SYMMETRY_COORD_CUSTOM_OBJECT | LINK |  |  |  | 
Display Weighting | ID_CA_WEIGHT_TOOL_ENABLE_DISPLAY | BOOL |  |  |  | 
Draw Falloff | ID_CA_WEIGHT_TOOL_DISPLAY_FALLOFF | BOOL |  |  |  | 
Draw Outline | ID_CA_WEIGHT_TOOL_DISPLAY_CURSOR | BOOL |  |  |  | 
Falloff While Painting | ID_CA_WEIGHT_TOOL_DISPLAY_MOUSEIN | BOOL |  |  |  | 
Cursor Color | ID_CA_WEIGHT_TOOL_DISPLAY_CURSOR_COLOR | COLOR |  |  |  | 
Falloff Color | ID_CA_WEIGHT_TOOL_DISPLAY_FALLOFF_COLOR | COLOR |  |  |  | 
Erase Color | ID_CA_WEIGHT_TOOL_DISPLAY_ERASE_COLOR | COLOR |  |  |  | 
