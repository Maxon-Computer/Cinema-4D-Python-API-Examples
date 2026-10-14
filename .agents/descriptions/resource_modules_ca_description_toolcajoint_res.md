# Description: Joint

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/ca/description/toolcajoint.res`
- **Symbol:** `Toolcajoint`
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
Bone | ID_CA_JOINT_TOOL_CREATE | LONG |  |  |  | ID_CA_JOINT_TOOL_CREATE_AXIS; ID_CA_JOINT_TOOL_CREATE_FROMPARENT; ID_CA_JOINT_TOOL_CREATE_TOCHILD
IK Chain | ID_CA_JOINT_TOOL_IK_CHAIN | LONG |  |  |  | ID_CA_JOINT_TOOL_IK_CHAIN_NONE; ID_CA_JOINT_TOOL_IK_CHAIN_2D; ID_CA_JOINT_TOOL_IK_CHAIN_3D; ID_CA_JOINT_TOOL_IK_CHAIN_SPLINE
Size | ID_CA_JOINT_TOOL_SIZE | LONG |  |  |  | ID_CA_JOINT_TOOL_SIZE_LENGTH; ID_CA_JOINT_TOOL_SIZE_CUSTOM
Custom | ID_CA_JOINT_TOOL_SIZE_USER | REAL | 0.0 |  |  | 
Root Null | ID_CA_JOINT_TOOL_CREATE_ROOT | BOOL |  |  |  | 
Pole Null | ID_CA_JOINT_TOOL_CREATE_POLE | BOOL |  |  |  | 
Align Axis | ID_CA_JOINT_TOOL_ALIGN_AXIS | BOOL |  |  |  | 
Projection | ID_CA_JOINT_TOOL_PROJECTION | BOOL |  |  |  | 
Highlight | ID_CA_JOINT_TOOL_HIGHLIGHT | BOOL |  |  |  | 
Bounding Box | ID_CA_JOINT_TOOL_BOUNDING_BOX | BOOL |  |  |  | 
Symmetry | ID_CA_JOINT_TOOL_SYMMETRY | LONG |  |  |  | ID_CA_JOINT_TOOL_SYMMETRY_NONE; ID_CA_JOINT_TOOL_SYMMETRY_DRAW; ID_CA_JOINT_TOOL_SYMMETRY_LINKED
Plane | ID_CA_JOINT_TOOL_MIRROR_PLANE | LONG |  |  |  | ID_CA_JOINT_TOOL_MIRROR_WORLD_XY; ID_CA_JOINT_TOOL_MIRROR_WORLD_XZ; ID_CA_JOINT_TOOL_MIRROR_WORLD_YZ; ID_CA_JOINT_TOOL_MIRROR_LOCAL_XY; ID_CA_JOINT_TOOL_MIRROR_LOCAL_XZ; ID_CA_JOINT_TOOL_MIRROR_LOCAL_YZ
Origin | ID_CA_JOINT_TOOL_MIRROR_ORIGIN | LONG |  |  |  | ID_CA_JOINT_TOOL_MIRROR_ORIGIN_WORLD; ID_CA_JOINT_TOOL_MIRROR_ORIGIN_ROOT; ID_CA_JOINT_TOOL_MIRROR_ORIGIN_HUB; ID_CA_JOINT_TOOL_MIRROR_ORIGIN_PARENT; ID_CA_JOINT_TOOL_MIRROR_ORIGIN_OBJECT
Object | ID_CA_JOINT_TOOL_MIRROR_ORIGIN_LINK | LINK |  |  |  | 
Default | ID_CA_JOINT_TOOL_MODIFIER_DEFAULT | LONG |  |  |  | ID_CA_JOINT_TOOL_MODIFIER_DRAW; ID_CA_JOINT_TOOL_MODIFIER_MOVE_JOINT; ID_CA_JOINT_TOOL_MODIFIER_MOVE_CHAIN; ID_CA_JOINT_TOOL_MODIFIER_SPLIT; ID_CA_JOINT_TOOL_MODIFIER_ALIGN; ID_CA_JOINT_TOOL_MODIFIER_SNAP
Control | ID_CA_JOINT_TOOL_MODIFIER_CTRL | LONG |  |  |  | ID_CA_JOINT_TOOL_MODIFIER_DRAW; ID_CA_JOINT_TOOL_MODIFIER_MOVE_JOINT; ID_CA_JOINT_TOOL_MODIFIER_MOVE_CHAIN; ID_CA_JOINT_TOOL_MODIFIER_SPLIT; ID_CA_JOINT_TOOL_MODIFIER_ALIGN; ID_CA_JOINT_TOOL_MODIFIER_SNAP
Shift | ID_CA_JOINT_TOOL_MODIFIER_SHIFT | LONG |  |  |  | ID_CA_JOINT_TOOL_MODIFIER_DRAW; ID_CA_JOINT_TOOL_MODIFIER_MOVE_JOINT; ID_CA_JOINT_TOOL_MODIFIER_MOVE_CHAIN; ID_CA_JOINT_TOOL_MODIFIER_SPLIT; ID_CA_JOINT_TOOL_MODIFIER_ALIGN; ID_CA_JOINT_TOOL_MODIFIER_SNAP
