# Description: Mirror

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/ca/description/toolcamirror.res`
- **Symbol:** `Toolcamirror`
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

### Mirror Base (`ToolMirrorBase`)

No parameters.

## All Parameters

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Realtime Update | MDATA_INTERACTIVE | BOOL |  |  |  | 
    Apply     | MDATA_APPLY | BUTTON |  |  |  | 
New Transform | MDATA_NEWTRANSFORM | BUTTON |  |  |  | 
No label | ID_SNAPSETTINGS | SUBCONTAINER |  |  |  | 
Origin | ID_CA_MIRROR_TOOL_ORIGIN | LONG |  |  |  | ID_CA_TOOL_MIRROR_BASE_ORIGIN_SELECTED; ID_CA_TOOL_MIRROR_BASE_ORIGIN_ROOT; ID_CA_TOOL_MIRROR_BASE_ORIGIN_PARENT; ID_CA_TOOL_MIRROR_BASE_ORIGIN_HUB; ID_CA_TOOL_MIRROR_BASE_ORIGIN_OBJECT; ID_CA_TOOL_MIRROR_BASE_ORIGIN_WORLD; ID_CA_TOOL_MIRROR_BASE_ORIGIN_MESH
Coords | ID_CA_MIRROR_TOOL_COORDS | LONG |  |  |  | ID_CA_TOOL_MIRROR_BASE_COORDS_WORLD; ID_CA_TOOL_MIRROR_BASE_COORDS_LOCAL; ID_CA_TOOL_MIRROR_BASE_COORDS_VIEW
Axis | ID_CA_MIRROR_TOOL_DIRECTION | LONG |  |  |  | ID_CA_TOOL_MIRROR_BASE_DIRECTION_X; ID_CA_TOOL_MIRROR_BASE_DIRECTION_Y; ID_CA_TOOL_MIRROR_BASE_DIRECTION_Z
Mirroring | ID_CA_MIRROR_TOOL_TYPE | LONG |  |  |  | ID_CA_TOOL_MIRROR_BASE_TYPE_REFLECT; ID_CA_TOOL_MIRROR_BASE_TYPE_P2N; ID_CA_TOOL_MIRROR_BASE_TYPE_N2P
Object | ID_CA_MIRROR_TOOL_OBJECT_LINK | LINK |  |  |  | 
Target | ID_CA_MIRROR_TOOL_TARGET | LONG |  |  |  | ID_CA_MIRROR_TOOL_TARGET_CLONE; ID_CA_MIRROR_TOOL_TARGET_OBJECT; ID_CA_MIRROR_TOOL_TARGET_SELF
Object | ID_CA_MIRROR_TOOL_TARGET_LINK | LINK |  |  |  | 
Include Links | ID_CA_MIRROR_TOOL_AUTO_INCLUDE | BOOL |  |  |  | 
Link Joints | ID_CA_MIRROR_TOOL_SET_JOINT_LINK | BOOL |  |  |  | 
Freeze | ID_CA_MIRROR_TOOL_FREEZE_PSR | BOOL |  |  |  | 
Position | ID_CA_MIRROR_TOOL_PSR | BOOL |  |  |  | 
Axes | ID_CA_MIRROR_TOOL_AXIS | LONG |  |  |  | ID_CA_MIRROR_TOOL_AXIS_NONE; ID_CA_MIRROR_TOOL_AXIS_ROTATE; ID_CA_MIRROR_TOOL_AXIS_ALIGN_X; ID_CA_MIRROR_TOOL_AXIS_ALIGN_Y; ID_CA_MIRROR_TOOL_AXIS_ALIGN_Z
Weights | ID_CA_MIRROR_TOOL_WEIGHTS | BOOL |  |  |  | 
Points | ID_CA_MIRROR_TOOL_POINTS | BOOL |  |  |  | 
Tags | ID_CA_MIRROR_TOOL_CLONE_TAGS | BOOL |  |  |  | 
Animation | ID_CA_MIRROR_TOOL_CLONE_ANIM | BOOL |  |  |  | 
Match Case | ID_CA_MIRROR_TOOL_CASE | BOOL |  |  |  | 
Prefix | ID_CA_MIRROR_TOOL_PRE | STRING |  |  |  | 
Suffix | ID_CA_MIRROR_TOOL_POST | STRING |  |  |  | 
Replace | ID_CA_MIRROR_TOOL_REPLACE | STRING |  |  |  | 
With | ID_CA_MIRROR_TOOL_WITH | STRING |  |  |  | 
Point Method | ID_CA_MIRROR_TOOL_SEARCH | LONG |  |  |  | ID_CA_TOOL_MIRROR_BASE_SEARCH_RADIUS; ID_CA_TOOL_MIRROR_BASE_SEARCH_NEAREST; ID_CA_TOOL_MIRROR_BASE_SEARCH_SURFACE; ID_CA_TOOL_MIRROR_BASE_SEARCH_NORMALS
Tolerance | ID_CA_MIRROR_TOOL_POINT_RADIUS | REAL | 0.00001 |  |  | 
Side Threshold | ID_CA_MIRROR_TOOL_SIDE_THRESHOLD | REAL | 0.000001 |  |  | 
Pass 1 | ID_CA_MIRROR_TOOL_JOINT_ALGO_PASS1 | LONG |  |  |  | ID_CA_TOOL_MIRROR_BASE_JOINT_MATCH_TOPO; ID_CA_TOOL_MIRROR_BASE_JOINT_MATCH_POS; ID_CA_TOOL_MIRROR_BASE_JOINT_MATCH_SPATIAL_PART; ID_CA_TOOL_MIRROR_BASE_JOINT_MATCH_NAME
Pass 2 | ID_CA_MIRROR_TOOL_JOINT_ALGO_PASS2 | LONG |  |  |  | ID_CA_TOOL_MIRROR_BASE_JOINT_MATCH_NONE; ID_CA_TOOL_MIRROR_BASE_JOINT_MATCH_TOPO; ID_CA_TOOL_MIRROR_BASE_JOINT_MATCH_POS; ID_CA_TOOL_MIRROR_BASE_JOINT_MATCH_SPATIAL_PART; ID_CA_TOOL_MIRROR_BASE_JOINT_MATCH_NAME
No label | ID_CA_MIRROR_TOOL_JOINT_ALGO_PASS_FINAL | BOOL |  |  |  | 
Adaptative | ID_CA_MIRROR_TOOL_SPATIAL_PART_ADAPTATIVE | BOOL |  |  |  | 
Partitioning Factor | ID_CA_MIRROR_TOOL_SPATIAL_PART_FACTOR | REAL | 1.0 | 200.0 |  | 
Tolerance | ID_CA_MIRROR_TOOL_JOINT_TOLERANCE | REAL | 0.00001 |  |  | 
Match Case | ID_CA_MIRROR_TOOL_JOINT_NAME_MATCH_CASE | BOOL |  |  |  | 
Left | ID_CA_MIRROR_TOOL_JOINT_NAME_NEG_PREFIX | STRING |  |  |  | 
Right | ID_CA_MIRROR_TOOL_JOINT_NAME_POS_PREFIX | STRING |  |  |  | 
Mirror Weights | ID_CA_MIRROR_TOOL_MIRROR_WEIGHTS | BUTTON |  |  |  | 
Children | ID_CA_MIRROR_TOOL_HIERARCHY | BOOL |  |  |  | 
Mirror | ID_CA_MIRROR_TOOL | BUTTON |  |  |  | 
