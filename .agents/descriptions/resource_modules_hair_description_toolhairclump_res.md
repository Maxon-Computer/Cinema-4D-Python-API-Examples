# Description: Clump

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/hair/description/toolhairclump.res`
- **Symbol:** `ToolHairClump`
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
Towards | HAIR_TOOL_CLUMP_TO | LONG |  |  |  | HAIR_TOOL_CLUMP_TO_LINE; HAIR_TOOL_CLUMP_TO_CENTER; HAIR_TOOL_CLUMP_TO_AVERAGE
Keep Lengths | HAIR_TOOL_CLUMP_FIXED_LENGTH | BOOL |  |  |  | 
Strength | HAIR_TOOL_CLUMP_STRENGTH | REAL | -100.0 | 100.0 |  | 
Curve | HAIR_TOOL_CLUMP_CURVE | SPLINE |  |  |  | 
Rotate | HAIR_TOOL_CLUMP_ROTATE | BOOL |  |  |  | 
Rotation | HAIR_TOOL_CLUMP_FREQ | REAL |  |  |  | 
Curve | HAIR_TOOL_CLUMP_FREQ_CURVE | SPLINE |  |  |  | 
