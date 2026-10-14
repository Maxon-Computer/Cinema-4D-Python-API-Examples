# Description: Spline Pen

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/c4d_objects/description/toolsplinepen.res`
- **Symbol:** `ToolSplinePen`
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
Type | MDATA_SPLINEPEN_MODE | LONG |  |  |  | MDATA_SPLINEPEN_MODE_LINEAR; MDATA_SPLINEPEN_MODE_CUBIC; MDATA_SPLINEPEN_MODE_AKIMA; MDATA_SPLINEPEN_MODE_BSPLINE; MDATA_SPLINEPEN_MODE_BEZIER
Edit Tangents Mode | MDATA_SPLINEPEN_TANGENT_MODE | BOOL |  |  |  | 
Lock Tangent Rotation | MDATA_SPLINEPEN_LOCK_ROTATION | BOOL |  |  |  | 
Lock Tangent Length | MDATA_SPLINEPEN_LOCK_SCALE | BOOL |  |  |  | 
Create New Splines | MDATA_SPLINEPEN_CREATE_SPLINES | BOOL |  |  |  | 
