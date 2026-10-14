# Description: Edge Cut

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/c4d_objects/description/tooledgecut.res`
- **Symbol:** `ToolEdgeCut`
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
Offset | MDATA_EDGECUT_OFFSET | REAL | 0.0 | 100.0 |  | 
Scale | MDATA_EDGECUT_SCALE | REAL | 0.0 |  |  | 
Subdivision | MDATA_EDGECUT_SUBDIV | REAL | 1 |  |  | 
Create N-gons | MDATA_EDGECUT_CREATENGONS | BOOL |  |  |  | 
N-gons | MDATA_EDGECUT_NGONMODE | LONG |  |  |  | MDATA_EDGECUT_NGONMODE_NONE; MDATA_EDGECUT_NGONMODE_ALL; MDATA_EDGECUT_NGONMODE_CORNER
