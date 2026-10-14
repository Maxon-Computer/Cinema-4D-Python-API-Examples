# Description: Spline Smooth

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/c4d_objects/description/toolsplinesmooth.res`
- **Symbol:** `ToolSplineSmooth`
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
Radius | MDATA_SPLINESMOOTH_RADIUS | REAL | 0.0 |  |  | 
Strength | MDATA_SPLINESMOOTH_STRENGTH | REAL | 0.0 | 100.0 |  | 
No label | MDATA_SPLINESMOOTH_SMOOTH_ON | BOOL |  |  |  | 
Smooth | MDATA_SPLINESMOOTH_SMOOTH | REAL | 0.0 | 100.0 |  | 
No label | MDATA_SPLINESMOOTH_FLATTEN_ON | BOOL |  |  |  | 
Flatten | MDATA_SPLINESMOOTH_FLATTEN | REAL | 0.0 | 100.0 |  | 
No label | MDATA_SPLINESMOOTH_RANDOM_ON | BOOL |  |  |  | 
Random | MDATA_SPLINESMOOTH_RANDOM | REAL | 0.0 | 100.0 |  | 
No label | MDATA_SPLINESMOOTH_PULL_ON | BOOL |  |  |  | 
Pull | MDATA_SPLINESMOOTH_PULL | REAL | 0.0 | 100.0 |  | 
No label | MDATA_SPLINESMOOTH_SPIRAL_ON | BOOL |  |  |  | 
Spiral | MDATA_SPLINESMOOTH_SPIRAL | REAL | -100.0 | 100.0 |  | 
No label | MDATA_SPLINESMOOTH_INFLATE_ON | BOOL |  |  |  | 
Inflate | MDATA_SPLINESMOOTH_INFLATE | REAL | -100.0 | 100.0 |  | 
No label | MDATA_SPLINESMOOTH_PROJECT_ON | BOOL |  |  |  | 
Project | MDATA_SPLINESMOOTH_PROJECT | REAL | -100.0 | 100.0 |  | 
