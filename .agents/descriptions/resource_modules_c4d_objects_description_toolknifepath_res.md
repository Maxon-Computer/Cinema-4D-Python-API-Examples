# Description: Loop/Path Cut

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/c4d_objects/description/toolknifepath.res`
- **Symbol:** `ToolKnifePath`
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
Mode | MDATA_KNIFEPATH_MODE | LONG |  |  |  | MDATA_KNIFEPATH_MODE_LOOP; MDATA_KNIFEPATH_MODE_PATH
Offset Mode | MDATA_KNIFEPATH_OFFSET_MODE | LONG |  |  |  | MDATA_KNIFEPATH_OFFSET_MODE_PROPORTIONAL; MDATA_KNIFEPATH_OFFSET_MODE_EDGEDISTANCE
Offset | MDATA_KNIFEPATH_OFFSET | REAL | 0 | 100 |  | 
Distance | MDATA_KNIFEPATH_DISTANCE | REAL | 0 |  |  | 
Number of Cuts | MDATA_KNIFEPATH_CUT_NUMBER | LONG | 1 |  |  | 
Restrict To Selection | MDATA_KNIFEPATH_SELECTED | BOOL |  |  |  | 
Select Cuts | MDATA_KNIFEPATH_SELECT_CUT | BOOL |  |  |  | 
Connect Cut Edges | MDATA_KNIFEPATH_CUTPOLYS | BOOL |  |  |  | 
Reuse Cuts | MDATA_KNIFEPATH_INTERACTION_STORE_LAYOUT | BOOL |  |  |  | 
Bidirectional Cut | MDATA_KNIFEPATH_INTERACTION_BIDIRECTIONAL | BOOL |  |  |  | 
Symmetrical Cut | MDATA_KNIFEPATH_INTERACTION_SYMETRY | BOOL |  |  |  | 
Toggle Direction | MDATA_KNIFEPATH_INTERACTION_DIRECTION | BOOL |  |  |  | 
Stop Cut at N-gon | MDATA_KNIFEPATH_INTERACTION_STOP_AT_NGON | BOOL |  |  |  | 
Stop Cut at Pole | MDATA_KNIFEPATH_INTERACTION_STOP_AT_POLE | BOOL |  |  |  | 
Quantize Subdivision | MDATA_KNIFEPATH_QUANTIZE_EDGE_SUB | BOOL |  |  |  | 
Quantize Step | MDATA_KNIFEPATH_QUANTIZE_EDGE_SUB_NUMBER | LONG | 1 |  |  | 
Use Loop Range | MDATA_KNIFEPATH_LIMITED_RANGE | BOOL |  |  |  | 
Range | MDATA_KNIFEPATH_RANGE_NUMBER | LONG | 1 |  |  | 
Preserve Curvature | MDATA_KNIFEPATH_PRESERVE_CURVATURE | BOOL |  |  |  | 
Tension | MDATA_KNIFEPATH_PRESERVE_CURVATURE_TENSION | REAL | -5 | 5 |  | 
Profile | MDATA_KNIFEPATH_SPLINE_USE | BOOL |  |  |  | 
Depth | MDATA_KNIFEPATH_SPLINE_EXTRUSION | REAL |  |  |  | 
No label | MDATA_KNIFEPATH_SPLINE | SPLINE |  |  |  | 
