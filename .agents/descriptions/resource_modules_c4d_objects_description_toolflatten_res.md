# Description: Flatten

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/c4d_objects/description/toolflatten.res`
- **Symbol:** `ToolFlatten`
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
Strength | MDATA_FLATTEN_WEIGHT | REAL | 0.0 | 100.0 |  | 
Mode | MDATA_FLATTEN_METHOD | LONG |  |  |  | MDATA_FLATTEN_METHOD_BESTFIT; MDATA_FLATTEN_METHOD_VIEW; MDATA_FLATTEN_METHOD_NORMAL; MDATA_FLATTEN_METHOD_AXIS; MDATA_FLATTEN_METHOD_WORLD
Axis | MDATA_FLATTEN_AXIS | LONG |  |  |  | MDATA_FLATTEN_AXIS_X; MDATA_FLATTEN_AXIS_Y; MDATA_FLATTEN_AXIS_Z
Use Axis Position | MDATA_FLATTEN_USEAXISPOSITION | BOOL |  |  |  | 
Position | MDATA_FLATTEN_PLANEPOSITION | REAL |  |  |  | 
Individual Islands | MDATA_FLATTEN_INDIVIDUALISLANDS | BOOL |  |  |  | 
Outline Only | MDATA_FLATTEN_OUTLINEONLY | BOOL |  |  |  | 
