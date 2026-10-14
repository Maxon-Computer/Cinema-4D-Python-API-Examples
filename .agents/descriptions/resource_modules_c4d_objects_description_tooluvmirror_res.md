# Description: UV Mirror Tool

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/c4d_objects/description/tooluvmirror.res`
- **Symbol:** `ToolUvMirror`
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
Per Island | TOOL_UVMIRROR_PERISLAND | BOOL |  |  |  | 
Center Position | TOOL_UVMIRROR_CENTER | LONG |  |  |  | TOOL_UVMIRROR_CENTER_TILE; TOOL_UVMIRROR_CENTER_MIDBOX; TOOL_UVMIRROR_CENTER_CUSTOM; TOOL_UVMIRROR_CENTER_MODELINGAXIS
Custom Position | TOOL_UVMIRROR_CENTER_CUSTOM_POSITION | VECTOR |  |  |  | 
Mirror U | TOOL_UVMIRROR_MIRRORU | BOOL |  |  |  | 
Mirror V | TOOL_UVMIRROR_MIRRORV | BOOL |  |  |  | 
