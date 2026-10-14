# Description: Doodle

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/c4d_objects/description/tooldoodle.res`
- **Symbol:** `ToolDoodle`
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
Color | MDATA_DOODLE_COLOR | COLOR |  |  |  | 
Opacity | MDATA_DOODLE_OPACITY | REAL | 0.0 | 100.0 |  | 
Pressure | MDATA_DOODLE_OPPRESSURE | BOOL |  |  |  | 
Size | MDATA_DOODLE_SIZE | REAL | 0.0 |  |  | 
Pressure | MDATA_DOODLE_SIPRESSURE | BOOL |  |  |  | 
Hardness | MDATA_DOODLE_HARDNESS | REAL | 0.0 | 100.0 |  | 
Pressure | MDATA_DOODLE_HAPRESSURE | BOOL |  |  |  | 
Spacing | MDATA_DOODLE_SPACING | REAL | 0.0 | 100.0 |  | 
Auto-Add Frames | MDATA_DOODLE_AUTOFRAME | BOOL |  |  |  | 
