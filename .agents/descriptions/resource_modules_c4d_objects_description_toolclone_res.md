# Description: Clone

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/c4d_objects/description/toolclone.res`
- **Symbol:** `ToolClone`
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
Clones | MDATA_CLONE_CNT | LONG | 1 | 1000 |  | 
Offset | MDATA_CLONE_OFFSET | REAL |  |  |  | 
Holes | MDATA_CLONE_HOLES | REAL | 0 | 100 |  | 
Scale | MDATA_CLONE_SCALE | REAL | 0 | 100 |  | 
Axis | MDATA_CLONE_AXIS | LONG |  |  |  | MDATA_CLONE_AXIS_X; MDATA_CLONE_AXIS_Y; MDATA_CLONE_AXIS_Z
Rotation | MDATA_CLONE_ROTATION | REAL |  |  |  | 
Move Var. | MDATA_CLONE_LOCALMOVE | VECTOR |  |  |  | 
Scale Var. | MDATA_CLONE_LOCALSCALE | VECTOR | 0 | 100 |  | 
Rot. Var. | MDATA_CLONE_LOCALROTATE | VECTOR |  |  |  | 
Uniform Scale | MDATA_CLONE_KEEPFORM | BOOL |  |  |  | 
