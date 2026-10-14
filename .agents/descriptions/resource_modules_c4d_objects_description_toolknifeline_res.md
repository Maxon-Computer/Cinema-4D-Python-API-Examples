# Description: Line Cut

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/c4d_objects/description/toolknifeline.res`
- **Symbol:** `ToolKnifeLine`
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
Visible Only | MDATA_KNIFELINE_VISIBLE_ONLY | BOOL |  |  |  | 
Slice Mode | MDATA_KNIFELINE_SPLIT_MODE | LONG |  |  |  | MDATA_KNIFELINE_SPLIT_MODE_NOSPLIT; MDATA_KNIFELINE_SPLIT_MODE_SPLIT; MDATA_KNIFELINE_SPLIT_MODE_REGION_A; MDATA_KNIFELINE_SPLIT_MODE_REGION_B
Single Line | MDATA_KNIFELINE_SINGLE | BOOL |  |  |  | 
Infinite Cut | MDATA_KNIFELINE_INFINITE | BOOL |  |  |  | 
Restrict to Selection | MDATA_KNIFELINE_SELECTED | BOOL |  |  |  | 
Select Cuts | MDATA_KNIFELINE_SELECT_CUT | BOOL |  |  |  | 
Connect Cut Edges | MDATA_KNIFELINE_CUTPOLYS | BOOL |  |  |  | 
Preserve N-gon Curvature | MDATA_KNIFELINE_NGON_CURVATURE | BOOL |  |  |  | 
Auto Snap | MDATA_KNIFELINE_AUTOSNAP | BOOL |  |  |  | 
Angle Constrain | MDATA_KNIFELINE_ANGLE_CONSTRAINT | BOOL |  |  |  | 
Angle | MDATA_KNIFELINE_ANGLE_CONSTRAINT_VALUE | REAL | 0.1 | 180 |  | 
Realtime Cut | MDATA_KNIFELINE_REALTIME | BOOL |  |  |  | 
