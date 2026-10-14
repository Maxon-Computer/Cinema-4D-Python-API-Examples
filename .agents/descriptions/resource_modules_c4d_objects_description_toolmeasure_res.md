# Description: Measure Tool

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/c4d_objects/description/toolmeasure.res`
- **Symbol:** `ToolMeasure`
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
Selection | MDATA_MEASURE_SELECTION | LONG |  |  |  | 
Show | MDATA_MEASURE_VISIBLE | BOOL |  |  |  | 
New Measure | MDATA_MEASURE_NEW | BUTTON |  |  |  | 
Delete Measure | MDATA_MEASURE_DELETE | BUTTON |  |  |  | 
Create Object | MDATA_MEASURE_CREATEOBJECT | BUTTON |  |  |  | 
3rd Point | MDATA_MEASURE_3RD_POINT | BOOL |  |  |  | 
Measure Distance 1 | MDATA_MEASURE_SHOWDIST1 | BOOL |  |  |  | 
Distance 1 | MDATA_MEASURE_DIST1 | REAL |  |  |  | 
Revert Direction | MDATA_MEASURE_DIR1 | BOOL |  |  |  | 
Measure Distance 2 | MDATA_MEASURE_SHOWDIST2 | BOOL |  |  |  | 
Distance 2 | MDATA_MEASURE_DIST2 | REAL |  |  |  | 
Revert Direction | MDATA_MEASURE_DIR2 | BOOL |  |  |  | 
Measure Angle | MDATA_MEASURE_SHOWANGLE | BOOL |  |  |  | 
Angle | MDATA_MEASURE_ANGLE | REAL |  |  |  | 
Revert Axis | MDATA_MEASURE_FIXROT | BOOL |  |  |  | 
Colors | MDATA_MEASUREGROUP_COLORS | SEPARATOR |  |  |  | 
Point Color | MDATA_MEASURE_COLORP | COLOR |  |  |  | 
Color 1 | MDATA_MEASURE_COLOR1 | COLOR |  |  |  | 
Color 2 | MDATA_MEASURE_COLOR2 | COLOR |  |  |  | 
Point1 | MDATA_MEASUREGROUP_P1 | SEPARATOR |  |  |  | 
Point 1 Object | MDATA_MEASURE_PNT1_LINK | LINK |  |  |  | 
Point 1 Mode | MDATA_MEASURE_PNT1_MODE | LONG |  |  |  | MDATA_MEASURE_PNT_MODE_FREE; MDATA_MEASURE_PNT_MODE_POINT; MDATA_MEASURE_PNT_MODE_EDGE; MDATA_MEASURE_PNT_MODE_POLY
Point 1 Index | MDATA_MEASURE_PNT1_IDX | LONG |  |  |  | 
Point 1 Position | MDATA_MEASURE_PNT1_VECTOR | VECTOR |  |  |  | 
Point2 | MDATA_MEASUREGROUP_P2 | SEPARATOR |  |  |  | 
Point 2 Object | MDATA_MEASURE_PNT2_LINK | LINK |  |  |  | 
Point 2 Mode | MDATA_MEASURE_PNT2_MODE | LONG |  |  |  | MDATA_MEASURE_PNT_MODE_FREE; MDATA_MEASURE_PNT_MODE_POINT; MDATA_MEASURE_PNT_MODE_EDGE; MDATA_MEASURE_PNT_MODE_POLY
Point 2 Index | MDATA_MEASURE_PNT2_IDX | LONG |  |  |  | 
Point 2 Position | MDATA_MEASURE_PNT2_VECTOR | VECTOR |  |  |  | 
Point3 | MDATA_MEASUREGROUP_P3 | SEPARATOR |  |  |  | 
Point 3 Object | MDATA_MEASURE_PNT3_LINK | LINK |  |  |  | 
Point 3 Mode | MDATA_MEASURE_PNT3_MODE | LONG |  |  |  | MDATA_MEASURE_PNT_MODE_FREE; MDATA_MEASURE_PNT_MODE_POINT; MDATA_MEASURE_PNT_MODE_EDGE; MDATA_MEASURE_PNT_MODE_POLY
Point 3 Index | MDATA_MEASURE_PNT3_IDX | LONG |  |  |  | 
Point 3 Position | MDATA_MEASURE_PNT3_VECTOR | VECTOR |  |  |  | 
