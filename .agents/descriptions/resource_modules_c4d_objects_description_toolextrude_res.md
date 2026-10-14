# Description: Extrude

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/c4d_objects/description/toolextrude.res`
- **Symbol:** `ToolExtrude`
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
Offset | MDATA_EXTRUDE_OFFSET | REAL |  |  |  | 
Offset Variation | MDATA_EXTRUDE_VARIANCE | REAL | 0 |  |  | 
Subdivision | MDATA_EXTRUDE_SUBDIVISION | REAL | 0 |  |  | 
Create N-gons | MDATA_EXTRUDE_CREATENGONS | BOOL |  |  |  | 
Preserve Groups | MDATA_EXTRUDE_PRESERVEGROUPS | BOOL |  |  |  | 
Create Caps | MDATA_EXTRUDE_CREATECAPS | BOOL |  |  |  | 
Maximum Angle | MDATA_EXTRUDE_ANGLE | REAL | 0 | 180 |  | 
Rotation | MDATA_EXTRUDE_EDGEANGLE | REAL |  |  |  | 
Quantize Rotation | MDATA_EXTRUDE_EDGESNAP | BOOL |  |  |  | 
Angle | MDATA_EXTRUDE_EDGESNAPVALUE | REAL | 0 | 180 |  | 
Bevel | MDATA_EXTRUDE_BEVEL | REAL |  |  |  | 
Bevel Variation | MDATA_EXTRUDE_BEVEL_VARIANCE | REAL | 0 |  |  | 
