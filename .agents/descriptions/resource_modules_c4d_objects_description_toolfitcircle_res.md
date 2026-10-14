# Description: Fit Circle

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/c4d_objects/description/toolfitcircle.res`
- **Symbol:** `ToolFitCircle`
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
Strength | MDATA_FITCIRCLE_WEIGHT | REAL | 0.0 | 100.0 |  | 
Roundness | MDATA_FITCIRCLE_ROUNDNESS | REAL | 0.0 | 100.0 |  | 
Exact Radius | MDATA_FITCIRCLE_ABSOLUTERADIUS | BOOL |  |  |  | 
Scale | MDATA_FITCIRCLE_SCALE | REAL | 0.0 |  |  | 
Radius | MDATA_FITCIRCLE_RADIUS | REAL | 0.0 |  |  | 
Angle | MDATA_FITCIRCLE_ANGLE | REAL |  |  |  | 
Adjust Inner Points | MDATA_FITCIRCLE_ADJUSTINNERPOINTS | BOOL |  |  |  | 
Project To Surface | MDATA_FITCIRCLE_PROJECTTOSURFACE | BOOL |  |  |  | 
Equal Spacing | MDATA_FITCIRCLE_PROJECTREGULAR | BOOL |  |  |  | 
Select Outline | MDATA_FITCIRCLE_SELECTOUTLINE | BOOL |  |  |  | 
