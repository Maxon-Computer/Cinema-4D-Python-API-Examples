# Description: Project

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/c4d_objects/description/toolsplineproject.res`
- **Symbol:** `ToolSplineProject`
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
Mode | MDATA_SPLINE_PROJECT_MODE | LONG |  |  |  | MDATA_SPLINE_PROJECT_MODE_VIEW; MDATA_SPLINE_PROJECT_MODE_XY; MDATA_SPLINE_PROJECT_MODE_ZY; MDATA_SPLINE_PROJECT_MODE_XZ; MDATA_SPLINE_PROJECT_MODE_X_AXIS; MDATA_SPLINE_PROJECT_MODE_Y_AXIS; MDATA_SPLINE_PROJECT_MODE_Z_AXIS; MDATA_SPLINE_PROJECT_MODE_SPHERICAL
