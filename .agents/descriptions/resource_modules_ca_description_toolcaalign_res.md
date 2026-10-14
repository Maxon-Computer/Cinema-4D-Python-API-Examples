# Description: Joint Align

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/ca/description/toolcaalign.res`
- **Symbol:** `Toolcaalign`
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
Axis | ID_CA_JOINT_ALIGN_PRIMARY_AXIS | LONG |  |  |  | ID_CA_JOINT_ALIGN_AXIS_FROMJOINT; ID_CA_JOINT_ALIGN_AXIS_X; ID_CA_JOINT_ALIGN_AXIS_Y; ID_CA_JOINT_ALIGN_AXIS_Z; ID_CA_JOINT_ALIGN_AXIS_NONE
Direction | ID_CA_JOINT_ALIGN_PRIMARY_DIRECTION | LONG |  |  |  | ID_CA_JOINT_ALIGN_DIRECTION_BONE; ID_CA_JOINT_ALIGN_DIRECTION_WORLD_AXIS; ID_CA_JOINT_ALIGN_DIRECTION_OBJECT_AXIS; ID_CA_JOINT_ALIGN_DIRECTION_OBJECT; ID_CA_JOINT_ALIGN_DIRECTION_ROOT_AXIS
Object | ID_CA_JOINT_ALIGN_PRIMARY_LINK | LINK |  |  |  | 
Up Axis | ID_CA_JOINT_ALIGN_UP_AXIS | LONG |  |  |  | ID_CA_JOINT_ALIGN_AXIS_X; ID_CA_JOINT_ALIGN_AXIS_Y; ID_CA_JOINT_ALIGN_AXIS_Z; ID_CA_JOINT_ALIGN_AXIS_NONE
Up Direction | ID_CA_JOINT_ALIGN_UP_DIRECTION | LONG |  |  |  | ID_CA_JOINT_ALIGN_DIRECTION_WORLD_AXIS; ID_CA_JOINT_ALIGN_DIRECTION_OBJECT_AXIS; ID_CA_JOINT_ALIGN_DIRECTION_OBJECT; ID_CA_JOINT_ALIGN_DIRECTION_ROOT_AXIS
Object | ID_CA_JOINT_ALIGN_UP_LINK | LINK |  |  |  | 
Align With Previous | ID_CA_JOINT_ALIGN_UP_FROMPREV | BOOL |  |  |  | 
Children | ID_CA_JOINT_ALIGN_CHILDREN | BOOL |  |  |  | 
Align | ID_CA_JOINT_ALIGN | BUTTON |  |  |  | 
