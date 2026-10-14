# Description: Paint

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/ca/description/toolcapaint.res`
- **Symbol:** `Toolcapaint`
- **Category:** Other

Use parameter symbols to access parameters and cycle option symbols for cycle values, never their numeric IDs. Treat Min and Max as constraints and Default as the declared initial value; blank cells mean the resource does not declare that metadata, not that the value is zero. Base Description Parameters lists inherited fields from each base; All Parameters lists the effective parameter set for this description.

## Base Description Parameters

### Brush Base (`Toolbrushbase`)

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Strength | ID_BRUSH_BASE_TOOL_STRENGTH | REAL | 0.0 | 100.0 |  | 
Projection | ID_BRUSH_BASE_TOOL_PROJECTION | BOOL |  |  |  | 
Visible Only | ID_BRUSH_BASE_TOOL_VISIBLE_ONLY | BOOL |  |  |  | 
Selected Only | ID_BRUSH_BASE_TOOL_SELECTED | BOOL |  |  |  | 
Size | ID_BRUSH_BASE_TOOL_RADIUS | REAL | 0.0 |  |  | 
Step | ID_BRUSH_BASE_TOOL_STEP | LONG | 1 | 1000 |  | 
Falloff | ID_BRUSH_BASE_TOOL_FALLOFF | LONG |  |  |  | ID_BRUSH_BASE_TOOL_FALLOFF_NONE; ID_BRUSH_BASE_TOOL_FALLOFF_SIMPLE; ID_BRUSH_BASE_TOOL_FALLOFF_LINEAR; ID_BRUSH_BASE_TOOL_FALLOFF_DOME; ID_BRUSH_BASE_TOOL_FALLOFF_BELL; ID_BRUSH_BASE_TOOL_FALLOFF_CIRCLE; ID_BRUSH_BASE_TOOL_FALLOFF_NEEDLE; ID_BRUSH_BASE_TOOL_FALLOFF_SPLINE
Width | ID_BRUSH_BASE_TOOL_WIDTH | REAL | 0.0 | 100.0 |  | 
Hardness | ID_BRUSH_BASE_TOOL_HARDNESS | REAL | 0.0 | 100.0 |  | 
Curve | ID_BRUSH_BASE_TOOL_FALLOFF_CURVE | SPLINE |  |  |  | 
Pressure | ID_BRUSH_BASE_TOOL_PEN | LONG |  |  |  | ID_BRUSH_BASE_TOOL_PEN_NONE; ID_BRUSH_BASE_TOOL_PEN_RADIUS; ID_BRUSH_BASE_TOOL_PEN_STRENGTH; ID_BRUSH_BASE_TOOL_PEN_HARDNESS

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
Realtime Update | MDATA_INTERACTIVE | BOOL |  |  |  | 
    Apply     | MDATA_APPLY | BUTTON |  |  |  | 
New Transform | MDATA_NEWTRANSFORM | BUTTON |  |  |  | 
No label | ID_SNAPSETTINGS | SUBCONTAINER |  |  |  | 
Strength | ID_BRUSH_BASE_TOOL_STRENGTH | REAL | 0.0 | 100.0 |  | 
Projection | ID_BRUSH_BASE_TOOL_PROJECTION | BOOL |  |  |  | 
Visible Only | ID_BRUSH_BASE_TOOL_VISIBLE_ONLY | BOOL |  |  |  | 
Selected Only | ID_BRUSH_BASE_TOOL_SELECTED | BOOL |  |  |  | 
Size | ID_BRUSH_BASE_TOOL_RADIUS | REAL | 0.0 |  |  | 
Step | ID_BRUSH_BASE_TOOL_STEP | LONG | 1 | 1000 |  | 
Falloff | ID_BRUSH_BASE_TOOL_FALLOFF | LONG |  |  |  | ID_BRUSH_BASE_TOOL_FALLOFF_NONE; ID_BRUSH_BASE_TOOL_FALLOFF_SIMPLE; ID_BRUSH_BASE_TOOL_FALLOFF_LINEAR; ID_BRUSH_BASE_TOOL_FALLOFF_DOME; ID_BRUSH_BASE_TOOL_FALLOFF_BELL; ID_BRUSH_BASE_TOOL_FALLOFF_CIRCLE; ID_BRUSH_BASE_TOOL_FALLOFF_NEEDLE; ID_BRUSH_BASE_TOOL_FALLOFF_SPLINE
Width | ID_BRUSH_BASE_TOOL_WIDTH | REAL | 0.0 | 100.0 |  | 
Hardness | ID_BRUSH_BASE_TOOL_HARDNESS | REAL | 0.0 | 100.0 |  | 
Curve | ID_BRUSH_BASE_TOOL_FALLOFF_CURVE | SPLINE |  |  |  | 
Pressure | ID_BRUSH_BASE_TOOL_PEN | LONG |  |  |  | ID_BRUSH_BASE_TOOL_PEN_NONE; ID_BRUSH_BASE_TOOL_PEN_RADIUS; ID_BRUSH_BASE_TOOL_PEN_STRENGTH; ID_BRUSH_BASE_TOOL_PEN_HARDNESS
Paint Mode | ID_CA_PAINT_TOOL_MAINMODE | LONG |  |  |  | ID_CA_PAINT_TOOL_MAINMODE_VERTEXMAP; ID_CA_PAINT_TOOL_MAINMODE_VERTEXCOLOR; ID_CA_PAINT_TOOL_MAINMODE_VERTEXCOLOR_ALPHA; ID_CA_PAINT_TOOL_MAINMODE_VERTEXALPHA
Opacity | ID_CA_PAINT_TOOL_OPACITY | REAL | 0.0 | 100.0 |  | 
Mode | ID_CA_PAINT_TOOL_MODE | LONG |  |  |  | ID_CA_PAINT_TOOL_MODE_ADD; ID_CA_PAINT_TOOL_MODE_SUBTRACT; ID_CA_PAINT_TOOL_MODE_ABS; ID_CA_PAINT_TOOL_MODE_SMOOTH; ID_CA_PAINT_TOOL_MODE_AVERAGE; ID_CA_PAINT_TOOL_MODE_BLEED; ID_CA_PAINT_TOOL_MODE_INTENSITY; ID_CA_PAINT_TOOL_MODE_REMAP
Mode | ID_CA_PAINT_TOOL_COLORMODE | LONG |  |  |  | ID_CA_PAINT_TOOL_COLORMODE_NORMAL; ID_CA_PAINT_TOOL_COLORMODE_ADD; ID_CA_PAINT_TOOL_COLORMODE_SUB; ID_CA_PAINT_TOOL_COLORMODE_MUL; ID_CA_PAINT_TOOL_COLORMODE_LIG; ID_CA_PAINT_TOOL_COLORMODE_DARK; ID_CA_PAINT_TOOL_COLORMODE_SMOOTH; ID_CA_PAINT_TOOL_COLORMODE_AVERAGE; ID_CA_PAINT_TOOL_COLORMODE_BLEED; ID_CA_PAINT_TOOL_COLORMODE_INTENSITY; ID_CA_PAINT_TOOL_COLORMODE_REMAP
Smooth | ID_CA_PAINT_TOOL_SMOOTH | LONG | 1 | 1000 |  | 
Curve | ID_CA_PAINT_TOOL_SPLINE | SPLINE |  |  |  | 
Apply All | ID_CA_PAINT_TOOL_APPLY_ALL | BUTTON |  |  |  | 
Apply Selected | ID_CA_PAINT_TOOL_APPLY_SELECTED | BUTTON |  |  |  | 
Color | ID_CA_PAINT_TOOL_VERTEXCOLOR | COLOR |  |  |  | 
Alpha | ID_CA_PAINT_TOOL_VERTEXCOLOR_APLHAVALUE | REAL | 0.0 | 100.0 |  | 
Lower | ID_CA_PAINT_TOOL_DISPLAY_LOWER | REAL | 0.0 | 100.0 |  | 
Upper | ID_CA_PAINT_TOOL_DISPLAY_UPPER | REAL | 0.0 | 100.0 |  | 
Custom Color | ID_CA_PAINT_TOOL_DISPLAY_COLOR_CUSTOM | BOOL |  |  |  | 
Color | ID_CA_PAINT_TOOL_DISPLAY_COLOR | GRADIENT |  |  |  | 
Cursor | ID_CA_PAINT_TOOL_DISPLAY_CURSOR_COLOR | COLOR |  |  |  | 
