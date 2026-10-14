# Description: Add Guides

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/hair/description/toolhairaddroot.res`
- **Symbol:** `ToolHairAddRoot`
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
Radius | HAIR_TOOL_ADDROOT_RADIUS | REAL | 0.0 |  |  | 
Step | HAIR_TOOL_ADDROOT_STEP | LONG | 0 |  |  | 
Count | HAIR_TOOL_ADDROOT_COUNT | LONG | 1 |  |  | 
Length | HAIR_TOOL_ADDROOT_LENGTH | REAL | 0.0 |  |  | 
Min Spacing | HAIR_TOOL_ADDROOT_MINSPACING | REAL | 0.0 |  |  | 
Pressure | HAIR_TOOL_ADDROOT_PEN | LONG |  |  |  | HAIR_TOOL_ADDROOT_PEN_NONE; HAIR_TOOL_ADDROOT_PEN_RADIUS; HAIR_TOOL_ADDROOT_PEN_LENGTH; HAIR_TOOL_ADDROOT_PEN_COUNT
Interpolated | HAIR_TOOL_ADDROOT_INTERPOLATE | BOOL |  |  |  | 
Strength | HAIR_TOOL_ADDROOT_INTERPOLATE_STRENGTH | REAL | 0.0 | 100.0 |  | 
