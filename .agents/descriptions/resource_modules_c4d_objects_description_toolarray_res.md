# Description: Array

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/c4d_objects/description/toolarray.res`
- **Symbol:** `ToolArray`
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
Clones X | MDATA_ARRAY_XCNT | LONG | 1 | 1000 |  | 
Y | MDATA_ARRAY_YCNT | LONG | 1 | 1000 |  | 
Z | MDATA_ARRAY_ZCNT | LONG | 1 | 1000 |  | 
Offset | MDATA_ARRAY_OFFSET | VECTOR |  |  |  | 
Holes | MDATA_ARRAY_HOLES | REAL | 0 | 100 |  | 
Move Var. | MDATA_ARRAY_LOCALMOVE | VECTOR |  |  |  | 
Scale Var. | MDATA_ARRAY_LOCALSCALE | VECTOR | 0 | 100 |  | 
Rot. Var. | MDATA_ARRAY_LOCALROTATE | VECTOR |  |  |  | 
Uniform Scale | MDATA_ARRAY_KEEPFORM | BOOL |  |  |  | 
