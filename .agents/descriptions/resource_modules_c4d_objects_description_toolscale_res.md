# Description: Scale

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/c4d_objects/description/toolscale.res`
- **Symbol:** `ToolScale`
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

### Modeling Axis (`ToolModelingAxis`)

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Position | MDATA_AXIS_MODE | LONG |  |  |  | MDATA_AXIS_MODE_WORLD; MDATA_AXIS_MODE_OBJECT; MDATA_AXIS_MODE_SELECTED; MDATA_AXIS_MODE_ROOT; MDATA_AXIS_MODE_PARENT; MDATA_AXIS_MODE_BOUNDS; MDATA_AXIS_MODE_POINTS; MDATA_AXIS_MODE_CAMERA; MDATA_AXIS_MODE_FREE; MDATA_AXIS_MODE_SELECTED_POINTS
Orientation | MDATA_AXIS_ROT | LONG |  |  |  | MDATA_AXIS_ROT_AXIS; MDATA_AXIS_ROT_WORLD; MDATA_AXIS_ROT_OBJECT; MDATA_AXIS_ROT_ROOT; MDATA_AXIS_ROT_PARENT; MDATA_AXIS_ROT_NORMALS; MDATA_AXIS_ROT_CAMERA
Retain Changes | MDATA_AXIS_FREE | BOOL |  |  |  | 
Along Normals | MDATA_AXIS_NORMAL_PSR | BOOL |  |  |  | 
Object | MDATA_AXIS_OBJECT_LINK | LINK |  |  |  | 
X | MDATA_AXIS_BOUNDS_X | REAL | -100.0 | 100.0 |  | 
Y | MDATA_AXIS_BOUNDS_Y | REAL | -100.0 | 100.0 |  | 
Z | MDATA_AXIS_BOUNDS_Z | REAL | -100.0 | 100.0 |  | 
No label | MDATA_AXIS_DIRTY | BOOL |  |  |  | 
Per-Object Transform | MDATA_AXIS_LOCALMANIPULATION | BOOL |  |  |  | 
Gimballing Rotation | MDATA_AXIS_GIMBALROTATION | BOOL |  |  |  | 

### Soft Selection (`ToolSoftSelection`)

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Enable | MDATA_SOFT_ENABLE | BOOL |  |  |  | 
Surface | MDATA_SOFT_SURFACE | BOOL |  |  |  | 
Rubber | MDATA_SOFT_RUBBER | BOOL |  |  |  | 
Restrict | MDATA_SOFT_RESTRICT | BOOL |  |  |  | 
Preview | MDATA_SOFT_PREVIEW | BOOL |  |  |  | 
Falloff | MDATA_SOFT_FALLOFF | LONG |  |  |  | MDATA_SOFT_FALLOFF_LINEAR; MDATA_SOFT_FALLOFF_DOME; MDATA_SOFT_FALLOFF_BELL; MDATA_SOFT_FALLOFF_CIRCLE; MDATA_SOFT_FALLOFF_NEEDLE; MDATA_SOFT_FALLOFF_VMAP; MDATA_SOFT_FALLOFF_SPLINE
Mode | MDATA_SOFT_MODE | LONG |  |  |  | MDATA_SOFT_MODE_GROUPS; MDATA_SOFT_MODE_CENTER; MDATA_SOFT_MODE_ALL
Radius | MDATA_SOFT_RADIUS | REAL | 0.0 |  |  | 
Radius (UV) | MDATA_SOFT_RADIUS_UV | REAL | 0.0 |  |  | 
Radius | MDATA_SOFT_RADIUS_3D | REAL | 0.0 |  |  | 
Strength | MDATA_SOFT_STRENGTH | REAL | 0.0 | 100.0 |  | 
Width | MDATA_SOFT_WIDTH | REAL | 0.0 | 100.0 |  | 
Spline | MDATA_SOFT_SPLINE | SPLINE |  |  |  | 

## All Parameters

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Realtime Update | MDATA_INTERACTIVE | BOOL |  |  |  | 
    Apply     | MDATA_APPLY | BUTTON |  |  |  | 
New Transform | MDATA_NEWTRANSFORM | BUTTON |  |  |  | 
No label | ID_SNAPSETTINGS | SUBCONTAINER |  |  |  | 
Position | MDATA_AXIS_MODE | LONG |  |  |  | MDATA_AXIS_MODE_WORLD; MDATA_AXIS_MODE_OBJECT; MDATA_AXIS_MODE_SELECTED; MDATA_AXIS_MODE_ROOT; MDATA_AXIS_MODE_PARENT; MDATA_AXIS_MODE_BOUNDS; MDATA_AXIS_MODE_POINTS; MDATA_AXIS_MODE_CAMERA; MDATA_AXIS_MODE_FREE; MDATA_AXIS_MODE_SELECTED_POINTS
Orientation | MDATA_AXIS_ROT | LONG |  |  |  | MDATA_AXIS_ROT_AXIS; MDATA_AXIS_ROT_WORLD; MDATA_AXIS_ROT_OBJECT; MDATA_AXIS_ROT_ROOT; MDATA_AXIS_ROT_PARENT; MDATA_AXIS_ROT_NORMALS; MDATA_AXIS_ROT_CAMERA
Retain Changes | MDATA_AXIS_FREE | BOOL |  |  |  | 
Along Normals | MDATA_AXIS_NORMAL_PSR | BOOL |  |  |  | 
Object | MDATA_AXIS_OBJECT_LINK | LINK |  |  |  | 
X | MDATA_AXIS_BOUNDS_X | REAL | -100.0 | 100.0 |  | 
Y | MDATA_AXIS_BOUNDS_Y | REAL | -100.0 | 100.0 |  | 
Z | MDATA_AXIS_BOUNDS_Z | REAL | -100.0 | 100.0 |  | 
No label | MDATA_AXIS_DIRTY | BOOL |  |  |  | 
Per-Object Transform | MDATA_AXIS_LOCALMANIPULATION | BOOL |  |  |  | 
Gimballing Rotation | MDATA_AXIS_GIMBALROTATION | BOOL |  |  |  | 
Enable | MDATA_SOFT_ENABLE | BOOL |  |  |  | 
Surface | MDATA_SOFT_SURFACE | BOOL |  |  |  | 
Rubber | MDATA_SOFT_RUBBER | BOOL |  |  |  | 
Restrict | MDATA_SOFT_RESTRICT | BOOL |  |  |  | 
Preview | MDATA_SOFT_PREVIEW | BOOL |  |  |  | 
Falloff | MDATA_SOFT_FALLOFF | LONG |  |  |  | MDATA_SOFT_FALLOFF_LINEAR; MDATA_SOFT_FALLOFF_DOME; MDATA_SOFT_FALLOFF_BELL; MDATA_SOFT_FALLOFF_CIRCLE; MDATA_SOFT_FALLOFF_NEEDLE; MDATA_SOFT_FALLOFF_VMAP; MDATA_SOFT_FALLOFF_SPLINE
Mode | MDATA_SOFT_MODE | LONG |  |  |  | MDATA_SOFT_MODE_GROUPS; MDATA_SOFT_MODE_CENTER; MDATA_SOFT_MODE_ALL
Radius | MDATA_SOFT_RADIUS | REAL | 0.0 |  |  | 
Radius (UV) | MDATA_SOFT_RADIUS_UV | REAL | 0.0 |  |  | 
Radius | MDATA_SOFT_RADIUS_3D | REAL | 0.0 |  |  | 
Strength | MDATA_SOFT_STRENGTH | REAL | 0.0 | 100.0 |  | 
Width | MDATA_SOFT_WIDTH | REAL | 0.0 | 100.0 |  | 
Spline | MDATA_SOFT_SPLINE | SPLINE |  |  |  | 
