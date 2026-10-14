# Description: Spline Arc

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/c4d_objects/description/toolsplinearc.res`
- **Symbol:** `ToolSplineArc`
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
Middle Point | MDATA_SPLINEARC_MIDPOINT | VECTOR |  |  |  | 
End Point | MDATA_SPLINEARC_ENDPOINT | VECTOR |  |  |  | 
First Point | MDATA_SPLINEARC_FIRSTPOINT | VECTOR |  |  |  | 
Center | MDATA_SPLINEARC_CENTER | VECTOR |  |  |  | 
Radius | MDATA_SPLINEARC_RADIUS | REAL | 0.0 |  |  | 
Angle | MDATA_SPLINEARC_ANGLE | REAL | -360.0 | 360.0 |  | 
First Insert Spline Point Index | MDATA_SPLINEARC_POINTINDEX1 | LONG | 0 |  |  | 
Second Insert Spline Point Index | MDATA_SPLINEARC_POINTINDEX2 | LONG | 0 |  |  | 
Object First Insert Spline Point Index Belongs To | MDATA_SPLINEARC_OBJECT1 | LINK |  |  |  | 
Object Second Insert Spline Point Index Belongs To | MDATA_SPLINEARC_OBJECT2 | LINK |  |  |  | 
