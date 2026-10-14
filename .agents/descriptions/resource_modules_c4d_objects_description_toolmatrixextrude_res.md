# Description: Matrix Extrude

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/c4d_objects/description/toolmatrixextrude.res`
- **Symbol:** `ToolMatrixExtrude`
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
Steps | MDATA_MATRIXEXTRUDE_STEPS | LONG | 0 |  |  | 
Polygon Coordinates | MDATA_MATRIXEXTRUDE_POLYGONCOORDS | BOOL |  |  |  | 
Move | MDATA_MATRIXEXTRUDE_MOVE | VECTOR |  |  |  | 
Rotate | MDATA_MATRIXEXTRUDE_ROTATE | VECTOR |  |  |  | 
Scale | MDATA_MATRIXEXTRUDE_SCALE | VECTOR |  |  |  | 
Variation | MDATA_MATRIXEXTRUDE_VARIANCE | LONG |  |  |  | MDATA_MATRIXEXTRUDE_VARIANCE_NONE; MDATA_MATRIXEXTRUDE_VARIANCE_INITIAL; MDATA_MATRIXEXTRUDE_VARIANCE_PERSTEP
Move Min. | MDATA_MATRIXEXTRUDE_MOVEFROM | REAL |  |  |  | 
Move Max. | MDATA_MATRIXEXTRUDE_MOVETO | REAL |  |  |  | 
Rotate Min. | MDATA_MATRIXEXTRUDE_ROTATEFROM | REAL |  |  |  | 
Rotate Max | MDATA_MATRIXEXTRUDE_ROTATETO | REAL |  |  |  | 
Scale Min. | MDATA_MATRIXEXTRUDE_SCALEFROM | REAL |  |  |  | 
Scale Max. | MDATA_MATRIXEXTRUDE_SCALETO | REAL |  |  |  | 
