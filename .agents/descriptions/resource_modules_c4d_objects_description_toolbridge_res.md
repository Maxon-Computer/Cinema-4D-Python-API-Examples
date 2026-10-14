# Description: Bridge

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/c4d_objects/description/toolbridge.res`
- **Symbol:** `ToolBridge`
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
Subdivision | MDATA_BRIDGE_SUBDIVISION | LONG | 0 |  |  | 
Tension | MDATA_BRIDGE_TENSION | REAL | -100.0 | 100.0 |  | 
Separate Controls | MDATA_BRIDGE_SEPARATE_CONTROLS | BOOL |  |  |  | 
Mode Start | MDATA_BRIDGE_FIRST_MODE | LONG |  |  |  | MDATA_BRIDGE_MODE_SURFACE; MDATA_BRIDGE_MODE_NORMAL; MDATA_BRIDGE_MODE_SURFACE_AVERAGE; MDATA_BRIDGE_MODE_NORMAL_AVERAGE
Mode End | MDATA_BRIDGE_SECOND_MODE | LONG |  |  |  | MDATA_BRIDGE_MODE_SURFACE; MDATA_BRIDGE_MODE_NORMAL; MDATA_BRIDGE_MODE_SURFACE_AVERAGE; MDATA_BRIDGE_MODE_NORMAL_AVERAGE
Flip Start | MDATA_BRIDGE_FIRST_FLIP | BOOL |  |  |  | 
Flip End | MDATA_BRIDGE_SECOND_FLIP | BOOL |  |  |  | 
Mode | MDATA_BRIDGE_BOTH_MODE | LONG |  |  |  | MDATA_BRIDGE_MODE_SURFACE; MDATA_BRIDGE_MODE_NORMAL; MDATA_BRIDGE_MODE_SURFACE_AVERAGE; MDATA_BRIDGE_MODE_NORMAL_AVERAGE
Flip | MDATA_BRIDGE_BOTH_FLIP | BOOL |  |  |  | 
Spin Steps | MDATA_BRIDGE_SPIN_STEPS | LONG | -2147483647 |  |  | 
Reverse | MDATA_BRIDGE_REVERSE | BOOL |  |  |  | 
Restrict to Selection | MDATA_BRIDGE_RESTRICT | BOOL |  |  |  | 
Patch Mode | MDATA_BRIDGE_USE_SMART_BRIDGE | BOOL |  |  |  | 
One Sided Patch | MDATA_BRIDGE_ONE_SIDED_PATCH | BOOL |  |  |  | 
Keep Original | MDATA_BRIDGE_KEEP_POLYGONS | BOOL |  |  |  | 
