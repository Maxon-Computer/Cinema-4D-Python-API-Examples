# Description: Align

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/c4d_objects/description/toolcenter.res`
- **Symbol:** `ToolCenter`
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
X Axis | MDATA_CENTER_XAXIS | LONG |  |  |  | MDATA_CENTER_NONE; MDATA_CENTER_POS; MDATA_CENTER_CENTER; MDATA_CENTER_NEG
Y Axis | MDATA_CENTER_YAXIS | LONG |  |  |  | MDATA_CENTER_NONE; MDATA_CENTER_POS; MDATA_CENTER_CENTER; MDATA_CENTER_NEG
Z Axis | MDATA_CENTER_ZAXIS | LONG |  |  |  | MDATA_CENTER_NONE; MDATA_CENTER_POS; MDATA_CENTER_CENTER; MDATA_CENTER_NEG
