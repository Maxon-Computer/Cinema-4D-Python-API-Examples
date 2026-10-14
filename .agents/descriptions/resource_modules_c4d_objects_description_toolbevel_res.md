# Description: Bevel

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/c4d_objects/description/toolbevel.res`
- **Symbol:** `ToolBevel`
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
Maximum Angle | MDATA_BEVEL_ANGLE | REAL |  |  |  | 
Extrusion | MDATA_BEVEL_OFFSET1 | REAL |  |  |  | 
Extrusion Variance | MDATA_BEVEL_VARIANCE1 | REAL | 0 | 200 |  | 
Inner Offset | MDATA_BEVEL_OFFSET2 | REAL |  |  |  | 
Inner Variance | MDATA_BEVEL_VARIANCE2 | REAL | 0 | 200 |  | 
Subdivision | MDATA_BEVEL_SUBDIVISION | LONG | 0 |  |  | 
Create N-gons | MDATA_BEVEL_CREATENGONS | BOOL |  |  |  | 
Type | MDATA_BEVEL_MODE | LONG |  |  |  | MDATA_BEVEL_MODE_LINEAR; MDATA_BEVEL_MODE_OUTER_CIRCLE; MDATA_BEVEL_MODE_INNER_CIRCLE; MDATA_BEVEL_MODE_BEZIER; MDATA_BEVEL_MODE_USER
Path | MDATA_BEVEL_PATH | SPLINE |  |  |  | 
Preserve Groups | MDATA_BEVEL_PRESERVEGROUPS | BOOL |  |  |  | 
