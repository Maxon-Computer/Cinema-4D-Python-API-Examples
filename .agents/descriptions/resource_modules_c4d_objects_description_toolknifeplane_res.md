# Description: Plane Cut

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/c4d_objects/description/toolknifeplane.res`
- **Symbol:** `ToolKnifePlane`
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
Mode | MDATA_KNIFEPLANE_MODE | LONG |  |  |  | MDATA_KNIFEPLANE_MODE_ALL; MDATA_KNIFEPLANE_MODE_SPLIT; MDATA_KNIFEPLANE_MODE_REGION_A; MDATA_KNIFEPLANE_MODE_REGION_B
Plane Mode | MDATA_KNIFEPLANE_PLANE_MODE | LONG |  |  |  | MDATA_KNIFEPLANE_PLANE_MODE_FREE; MDATA_KNIFEPLANE_PLANE_MODE_LOCAL; MDATA_KNIFEPLANE_PLANE_MODE_WORLD; MDATA_KNIFEPLANE_PLANE_MODE_CAMERA
Plane | MDATA_KNIFEPLANE_PLANE | LONG |  |  |  | MDATA_KNIFEPLANE_PLANE_XY; MDATA_KNIFEPLANE_PLANE_YZ; MDATA_KNIFEPLANE_PLANE_XZ
Plane Position | MDATA_KNIFEPLANE_PIVOT_POSITION | VECTOR |  |  |  | 
Plane Rotation | MDATA_KNIFEPLANE_PIVOT_ROTATION | VECTOR |  |  |  | 
No label | MDATA_KNIFEPLANE_PLANE_PRESET | LONG |  |  |  | MDATA_KNIFEPLANE_PLANE_PRESET_X; MDATA_KNIFEPLANE_PLANE_PRESET_X2; MDATA_KNIFEPLANE_PLANE_PRESET_Y; MDATA_KNIFEPLANE_PLANE_PRESET_Y2; MDATA_KNIFEPLANE_PLANE_PRESET_Z; MDATA_KNIFEPLANE_PLANE_PRESET_Z2; MDATA_KNIFEPLANE_PLANE_PRESET_CUSTOM
Offset | MDATA_KNIFEPLANE_OFFSET | REAL |  |  |  | 
Number of Cuts | MDATA_KNIFEPLANE_CONUT | LONG | 1 |  |  | 
Spacing | MDATA_KNIFEPLANE_DIST | REAL |  |  |  | 
Restrict To Selection | MDATA_KNIFEPLANE_SELECTED | BOOL |  |  |  | 
Select Cuts | MDATA_KNIFEPLANE_SELECT_CUT | BOOL |  |  |  | 
Connect Cut Edges | MDATA_KNIFEPLANE_CUTPOLYS | BOOL |  |  |  | 
Preserve N-gon Curvature | MDATA_KNIFEPLANE_NGON_CURVATURE | BOOL |  |  |  | 
Auto Snap | MDATA_KNIFEPLANE_AUTOSNAP | BOOL |  |  |  | 
Regular Slice | MDATA_KNIFEPLANE_REGULARSLICE | BOOL |  |  |  | 
Angle Constrain | MDATA_KNIFEPLANE_ANGLE_CONSTRAINT | BOOL |  |  |  | 
Angle | MDATA_KNIFEPLANE_ANGLE_CONSTRAINT_VALUE | REAL | 0.1 | 180 |  | 
Realtime Cut | MDATA_KNIFEPLANE_REALTIME | BOOL |  |  |  | 
