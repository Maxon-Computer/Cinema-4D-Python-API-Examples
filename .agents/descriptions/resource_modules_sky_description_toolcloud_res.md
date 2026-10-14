# Description: Cloud

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/sky/description/toolcloud.res`
- **Symbol:** `ToolCloud`
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
Radius | MDATA_CLOUD_CREATE_BRUSH_RAD | REAL | 1 |  |  | 
Density | MDATA_CLOUD_CREATE_DENSITY | REAL | 0 | 100 |  | 
Maximum Size | MDATA_CLOUD_CREATE_MAX_SIZE | VECTOR |  | 120000 |  | 
Threshold | MDATA_CLOUD_DRAW_THRESHOLD | REAL | 1 | 100 |  | 
Clear | MDATA_CLOUD_CLEAR | BUTTON |  |  |  | 
Fill Plane | MDATA_CLOUD_FILL_PLANE | BUTTON |  |  |  | 
Fill Sphere | MDATA_CLOUD_FILL_SPHERE | BUTTON |  |  |  | 
Distance | MDATA_CLOUD_SMOOTH_B_DIST | REAL | 0 |  |  | 
Variance | MDATA_CLOUD_SMOOTH_B_VAR | REAL | 0 | 100 |  | 
Shape | MDATA_CLOUD_SMOOTH_B_SPLINE | SPLINE |  |  |  | 
Smooth Borders | MDATA_CLOUD_SMOOTH_BORDERS | BUTTON |  |  |  | 
Strength | MDATA_CLOUD_SMOOTH_A_STR | REAL | 0 | 100 |  | 
Variance | MDATA_CLOUD_SMOOTH_A_VARIANCE | REAL | 0 | 100 |  | 
Smooth All | MDATA_CLOUD_SMOOTH_ALL | BUTTON |  |  |  | 
Remap | MDATA_CLOUD_REMAP_SPLINE | SPLINE |  |  |  | 
Remap | MDATA_CLOUD_REMAP | BUTTON |  |  |  | 
Quality | MDATA_CLOUD_DISPLAY_QUALITY | REAL | 0 | 100 |  | 
Render Preview | MDATA_RENDERPREVIEW_BTN | BUTTON |  |  |  | 
