# Description: Linear Clone Tool

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/mograph/description/tool_mglinear.res`
- **Symbol:** `Tool_MGLinear`
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
Start Position | MDATA_MGLINEARTOOL_START | VECTOR |  |  |  | 
End Position | MDATA_MGLINEARTOOL_END | VECTOR |  |  |  | 
Clones Count | MDATA_MGLINEARTOOL_COUNT | LONG | 1 |  |  | 
Generate | MDATA_MGLINEARTOOL_MODE | LONG |  |  |  | MDATA_MGLINEARTOOL_MODE_CLONE; MDATA_MGLINEARTOOL_MODE_INSTANCE
