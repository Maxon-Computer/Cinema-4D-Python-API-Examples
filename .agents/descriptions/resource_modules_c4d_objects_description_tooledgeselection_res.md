# Description: Path Selection

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/c4d_objects/description/tooledgeselection.res`
- **Symbol:** `ToolEdgeSelection`
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
Mode | MDATA_MWS_EDGEMODE | LONG |  |  |  | MDATA_MWS_EDGEMODE_LINE2; MDATA_MWS_EDGEMODE_GUIDED; MDATA_MWS_EDGEMODE_LINE; MDATA_MWS_EDGEMODE_LOOP
Add to Selection | MDATA_MWS_ADD_TO_SEL | BOOL |  |  |  | 
Tag Name | MWS_TAG_LINK | STRING |  |  |  | 
Auto Set Selection | MWS_TAG_AUTO_SET_SEL | BOOL |  |  |  | 
Set Selection | MWS_TAG_SET_SEL | BUTTON |  |  |  | 
Add Selection | MWS_TAG_ADD_SEL | BUTTON |  |  |  | 
Subtract Selection | MWS_TAG_REM_SEL | BUTTON |  |  |  | 
