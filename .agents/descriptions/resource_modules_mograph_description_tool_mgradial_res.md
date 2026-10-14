# Description: Radial Clone Tool

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/mograph/description/tool_mgradial.res`
- **Symbol:** `Tool_MGRadial`
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
Center | MDATA_MGRADIALTOOL_CENTER | VECTOR |  |  |  | 
Radius | MDATA_MGRADIALTOOL_RADIUS | REAL |  |  |  | 
Axis | MDATA_MGRADIALTOOL_AXIS | LONG |  |  |  | MDATA_MGRADIALTOOL_AXIS_XY; MDATA_MGRADIALTOOL_AXIS_YZ; MDATA_MGRADIALTOOL_AXIS_XZ
Clones Count | MDATA_MGRADIALTOOL_COUNT | LONG | 1 |  |  | 
Generate | MDATA_MGRADIALTOOL_MODE | LONG |  |  |  | MDATA_MGRADIALTOOL_MODE_CLONE; MDATA_MGRADIALTOOL_MODE_INSTANCE
