# Description: Morph Brush

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/ca/description/toolbrushmorph.res`
- **Symbol:** `toolbrushmorph`
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
Morph Tag | MORPHBRUSHTOOL_MORPHTAG | LINK |  |  |  | 
Morph Target | MORPHBRUSHTOOL_MORPH | LONG |  |  |  | MORPHBRUSHTOOL_MORPH_NONE
