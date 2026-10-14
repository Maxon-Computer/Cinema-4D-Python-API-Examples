# Description: Seam Selection

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/c4d_objects/description/toolseamselection.res`
- **Symbol:** `ToolSeamSelection`
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
Loop Stop at Seams | MDATA_LOOP_SEL_STOP_AT_SELECTIONS | BOOL |  |  |  | 
Loop Stop at Non-Quads | MDATA_LOOP_SEL_STOP_AT_NON_QUADS | BOOL |  |  |  | 
Loop Stop at Poles | MDATA_LOOP_SEL_STOP_AT_POLES | BOOL |  |  |  | 
Mode | MDATA_MWS_EDGEMODE | LONG |  |  |  | MDATA_MWS_EDGEMODE_LINE2; MDATA_MWS_EDGEMODE_GUIDED; MDATA_MWS_EDGEMODE_LINE
Clear Seams | TOOL_SEAM_CLEAR_SEAMS | BUTTON |  |  |  | 
