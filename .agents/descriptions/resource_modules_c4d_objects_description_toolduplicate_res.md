# Description: Duplicate

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/c4d_objects/description/toolduplicate.res`
- **Symbol:** `ToolDuplicate`
- **Category:** Other

Use parameter symbols to access parameters and cycle option symbols for cycle values, never their numeric IDs. Treat Min and Max as constraints and Default as the declared initial value; blank cells mean the resource does not declare that metadata, not that the value is zero. Base Description Parameters lists inherited fields from each base; All Parameters lists the effective parameter set for this description.

## Base Description Parameters

### Arrange (`ToolArrange`)

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Mode | MDATA_ARRANGE_MODE | LONG |  |  |  | MDATA_ARRANGE_MODE_SELECTMODE; MDATA_ARRANGE_MODE_LINEAR; MDATA_ARRANGE_MODE_CIRCLE; MDATA_ARRANGE_MODE_ALONGSPLINE
Per Step | MDATA_ARRANGE_LINEAR_PERSTEP | BOOL |  |  |  | 
Per Step | MDATA_ARRANGE_CIRCLE_PERSTEP | BOOL |  |  |  | 
Per Step | MDATA_ARRANGE_SPLINE_PERSTEP | BOOL |  |  |  | 
Enable Move | MDATA_ARRANGE_LINEAR_USE_MOVE | BOOL |  |  |  | 
Enable Move | MDATA_ARRANGE_CIRCLE_USE_MOVE | BOOL |  |  |  | 
Enable Move | MDATA_ARRANGE_SPLINE_USE_MOVE | BOOL |  |  |  | 
Enable Move X | MDATA_ARRANGE_LINEAR_USE_MOVE_X | BOOL |  |  |  | 
Enable Move X | MDATA_ARRANGE_CIRCLE_USE_MOVE_X | BOOL |  |  |  | 
Enable Move X | MDATA_ARRANGE_SPLINE_USE_MOVE_X | BOOL |  |  |  | 
Enable Move Y | MDATA_ARRANGE_LINEAR_USE_MOVE_Y | BOOL |  |  |  | 
Enable Move Y | MDATA_ARRANGE_CIRCLE_USE_MOVE_Y | BOOL |  |  |  | 
Enable Move Y | MDATA_ARRANGE_SPLINE_USE_MOVE_Y | BOOL |  |  |  | 
Enable Move Z | MDATA_ARRANGE_LINEAR_USE_MOVE_Z | BOOL |  |  |  | 
Enable Move Z | MDATA_ARRANGE_CIRCLE_USE_MOVE_Z | BOOL |  |  |  | 
Enable Move Z | MDATA_ARRANGE_SPLINE_USE_MOVE_Z | BOOL |  |  |  | 
Spline | MDATA_ARRANGE_SPLINE_LINK | LINK |  |  |  | 
Start Pos. | MDATA_ARRANGE_SPLINE_STARTPOS | REAL |  |  |  | 
End Pos. | MDATA_ARRANGE_SPLINE_ENDPOS | REAL |  |  |  | 
Radius | MDATA_ARRANGE_CIRCLE_RADIUS | REAL |  |  |  | 
Start | MDATA_ARRANGE_CIRCLE_START | REAL |  |  |  | 
End | MDATA_ARRANGE_CIRCLE_END | REAL |  |  |  | 
Move | MDATA_ARRANGE_LINEAR_MOVE | VECTOR |  |  |  | 
Move | MDATA_ARRANGE_CIRCLE_MOVE | VECTOR |  |  |  | 
Enable Scale | MDATA_ARRANGE_LINEAR_USE_SCALE | BOOL |  |  |  | 
Enable Scale | MDATA_ARRANGE_CIRCLE_USE_SCALE | BOOL |  |  |  | 
Enable Scale | MDATA_ARRANGE_SPLINE_USE_SCALE | BOOL |  |  |  | 
Scale | MDATA_ARRANGE_LINEAR_SCALE | VECTOR |  |  |  | 
Scale | MDATA_ARRANGE_CIRCLE_SCALE | VECTOR |  |  |  | 
Scale | MDATA_ARRANGE_SPLINE_SCALE | VECTOR |  |  |  | 
Enable Rotation | MDATA_ARRANGE_LINEAR_USE_ROTATION | BOOL |  |  |  | 
Enable Rotation | MDATA_ARRANGE_CIRCLE_USE_ROTATION | BOOL |  |  |  | 
Enable Rotation | MDATA_ARRANGE_SPLINE_USE_ROTATION | BOOL |  |  |  | 
Align Tangential | MDATA_ARRANGE_CIRCLE_ALIGNTANGENTIAL | BOOL |  |  |  | 
Rail Spline | MDATA_ARRANGE_SPLINE_RAIL | LINK |  |  |  | 
Align Tangential | MDATA_ARRANGE_SPLINE_ALIGNTANGENTIAL | LONG |  |  |  | MDATA_ARRANGE_SPLINE_ALIGNTANGENTIAL_X; MDATA_ARRANGE_SPLINE_ALIGNTANGENTIAL_XN; MDATA_ARRANGE_SPLINE_ALIGNTANGENTIAL_Y; MDATA_ARRANGE_SPLINE_ALIGNTANGENTIAL_YN; MDATA_ARRANGE_SPLINE_ALIGNTANGENTIAL_Z; MDATA_ARRANGE_SPLINE_ALIGNTANGENTIAL_ZN
Bank | MDATA_ARRANGE_SPLINE_FLIP | REAL |  |  |  | 
Rotate | MDATA_ARRANGE_LINEAR_ROTATION | VECTOR |  |  |  | 
Rotate | MDATA_ARRANGE_CIRCLE_ROTATION | VECTOR |  |  |  | 
Rotate | MDATA_ARRANGE_SPLINE_ROTATION | VECTOR |  |  |  | 

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
Copies | MDATA_DUPLICATE_COPIES | LONG | 1 |  |  | 
Clone Mode | MDATA_DUPLICATE_INSTANCES | LONG |  |  |  | MDATA_DUPLICATE_INSTANCES_OFF; MDATA_DUPLICATE_INSTANCES_INSTANCE; MDATA_DUPLICATE_INSTANCES_VOLUMEINSTANCE
Realtime Update | MDATA_INTERACTIVE | BOOL |  |  |  | 
    Apply     | MDATA_APPLY | BUTTON |  |  |  | 
New Transform | MDATA_NEWTRANSFORM | BUTTON |  |  |  | 
No label | ID_SNAPSETTINGS | SUBCONTAINER |  |  |  | 
Mode | MDATA_ARRANGE_MODE | LONG |  |  |  | MDATA_ARRANGE_MODE_SELECTMODE; MDATA_ARRANGE_MODE_LINEAR; MDATA_ARRANGE_MODE_CIRCLE; MDATA_ARRANGE_MODE_ALONGSPLINE
Per Step | MDATA_ARRANGE_LINEAR_PERSTEP | BOOL |  |  |  | 
Per Step | MDATA_ARRANGE_CIRCLE_PERSTEP | BOOL |  |  |  | 
Per Step | MDATA_ARRANGE_SPLINE_PERSTEP | BOOL |  |  |  | 
Enable Move | MDATA_ARRANGE_LINEAR_USE_MOVE | BOOL |  |  |  | 
Enable Move | MDATA_ARRANGE_CIRCLE_USE_MOVE | BOOL |  |  |  | 
Enable Move | MDATA_ARRANGE_SPLINE_USE_MOVE | BOOL |  |  |  | 
Enable Move X | MDATA_ARRANGE_LINEAR_USE_MOVE_X | BOOL |  |  |  | 
Enable Move X | MDATA_ARRANGE_CIRCLE_USE_MOVE_X | BOOL |  |  |  | 
Enable Move X | MDATA_ARRANGE_SPLINE_USE_MOVE_X | BOOL |  |  |  | 
Enable Move Y | MDATA_ARRANGE_LINEAR_USE_MOVE_Y | BOOL |  |  |  | 
Enable Move Y | MDATA_ARRANGE_CIRCLE_USE_MOVE_Y | BOOL |  |  |  | 
Enable Move Y | MDATA_ARRANGE_SPLINE_USE_MOVE_Y | BOOL |  |  |  | 
Enable Move Z | MDATA_ARRANGE_LINEAR_USE_MOVE_Z | BOOL |  |  |  | 
Enable Move Z | MDATA_ARRANGE_CIRCLE_USE_MOVE_Z | BOOL |  |  |  | 
Enable Move Z | MDATA_ARRANGE_SPLINE_USE_MOVE_Z | BOOL |  |  |  | 
Spline | MDATA_ARRANGE_SPLINE_LINK | LINK |  |  |  | 
Start Pos. | MDATA_ARRANGE_SPLINE_STARTPOS | REAL |  |  |  | 
End Pos. | MDATA_ARRANGE_SPLINE_ENDPOS | REAL |  |  |  | 
Radius | MDATA_ARRANGE_CIRCLE_RADIUS | REAL |  |  |  | 
Start | MDATA_ARRANGE_CIRCLE_START | REAL |  |  |  | 
End | MDATA_ARRANGE_CIRCLE_END | REAL |  |  |  | 
Move | MDATA_ARRANGE_LINEAR_MOVE | VECTOR |  |  |  | 
Move | MDATA_ARRANGE_CIRCLE_MOVE | VECTOR |  |  |  | 
Enable Scale | MDATA_ARRANGE_LINEAR_USE_SCALE | BOOL |  |  |  | 
Enable Scale | MDATA_ARRANGE_CIRCLE_USE_SCALE | BOOL |  |  |  | 
Enable Scale | MDATA_ARRANGE_SPLINE_USE_SCALE | BOOL |  |  |  | 
Scale | MDATA_ARRANGE_LINEAR_SCALE | VECTOR |  |  |  | 
Scale | MDATA_ARRANGE_CIRCLE_SCALE | VECTOR |  |  |  | 
Scale | MDATA_ARRANGE_SPLINE_SCALE | VECTOR |  |  |  | 
Enable Rotation | MDATA_ARRANGE_LINEAR_USE_ROTATION | BOOL |  |  |  | 
Enable Rotation | MDATA_ARRANGE_CIRCLE_USE_ROTATION | BOOL |  |  |  | 
Enable Rotation | MDATA_ARRANGE_SPLINE_USE_ROTATION | BOOL |  |  |  | 
Align Tangential | MDATA_ARRANGE_CIRCLE_ALIGNTANGENTIAL | BOOL |  |  |  | 
Rail Spline | MDATA_ARRANGE_SPLINE_RAIL | LINK |  |  |  | 
Align Tangential | MDATA_ARRANGE_SPLINE_ALIGNTANGENTIAL | LONG |  |  |  | MDATA_ARRANGE_SPLINE_ALIGNTANGENTIAL_X; MDATA_ARRANGE_SPLINE_ALIGNTANGENTIAL_XN; MDATA_ARRANGE_SPLINE_ALIGNTANGENTIAL_Y; MDATA_ARRANGE_SPLINE_ALIGNTANGENTIAL_YN; MDATA_ARRANGE_SPLINE_ALIGNTANGENTIAL_Z; MDATA_ARRANGE_SPLINE_ALIGNTANGENTIAL_ZN
Bank | MDATA_ARRANGE_SPLINE_FLIP | REAL |  |  |  | 
Rotate | MDATA_ARRANGE_LINEAR_ROTATION | VECTOR |  |  |  | 
Rotate | MDATA_ARRANGE_CIRCLE_ROTATION | VECTOR |  |  |  | 
Rotate | MDATA_ARRANGE_SPLINE_ROTATION | VECTOR |  |  |  | 
