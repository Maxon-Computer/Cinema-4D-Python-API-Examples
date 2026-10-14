# Description: Cloth Cache Tool

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/clothilde/description/cachetool.res`
- **Symbol:** `CacheTool`
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
Realtime Update | MDATA_INTERACTIVE | BOOL |  |  |  | 
    Apply     | MDATA_APPLY | BUTTON |  |  |  | 
New Transform | MDATA_NEWTRANSFORM | BUTTON |  |  |  | 
No label | ID_SNAPSETTINGS | SUBCONTAINER |  |  |  | 
Mode | CACHE_TOOL_MODE | LONG |  |  |  | CACHE_TOOL_MODE_SMEAR; CACHE_TOOL_MODE_SMOOTH
Show +/- | CACHE_TOOL_SHOW_RADIUS | LONG | 1 |  |  | 
Frames +/- | CACHE_TOOL_FALLOFF_RADIUS | LONG | 0 |  |  | 
Strength | CACHE_TOOL_FALLOFF_STRENGTH | REAL |  |  |  | 
Falloff | CACHE_TOOL_FALLOFF_MODE | LONG |  |  |  | CACHE_TOOL_MODE_CONSTANT; CACHE_TOOL_MODE_LINEAR; CACHE_TOOL_MODE_DOME; CACHE_TOOL_MODE_BELL; CACHE_TOOL_MODE_CIRCLE; CACHE_TOOL_MODE_NEEDLE; CACHE_TOOL_MODE_USER
Width | CACHE_TOOL_FALLOFF_WIDTH | REAL | 0.0 |  |  | 
No label | CACHE_TOOL_FALLOFF | SPLINE |  |  |  | 
