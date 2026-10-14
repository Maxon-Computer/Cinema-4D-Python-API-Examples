# Description: Set Point Value

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/c4d_objects/description/toolsetvalue.res`
- **Symbol:** `ToolSetValue`
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
All | TEMP_MDATA_SETVALUE_SETALL | LONG |  |  |  | MDATA_SETVALUE_SET_LEAVE; MDATA_SETVALUE_SET_SET; MDATA_SETVALUE_SET_CENTER; MDATA_SETVALUE_SET_QUANTIZE; MDATA_SETVALUE_CRUMPLE_ALONGNORMALS; MDATA_SETVALUE_CRUMPLE_AXIAL; MDATA_SETVALUE_CRUMPLE_RADIAL
X | MDATA_SETVALUE_SETX | LONG |  |  |  | MDATA_SETVALUE_SET_LEAVE; MDATA_SETVALUE_SET_SET; MDATA_SETVALUE_SET_CENTER; MDATA_SETVALUE_SET_QUANTIZE; MDATA_SETVALUE_CRUMPLE_ALONGNORMALS; MDATA_SETVALUE_CRUMPLE_AXIAL; MDATA_SETVALUE_CRUMPLE_RADIAL
X Value | TEMP_MDATA_SETVALUE_VAL_X | REAL |  |  |  | 
Y | MDATA_SETVALUE_SETY | LONG |  |  |  | MDATA_SETVALUE_SET_LEAVE; MDATA_SETVALUE_SET_SET; MDATA_SETVALUE_SET_CENTER; MDATA_SETVALUE_SET_QUANTIZE; MDATA_SETVALUE_CRUMPLE_ALONGNORMALS; MDATA_SETVALUE_CRUMPLE_AXIAL; MDATA_SETVALUE_CRUMPLE_RADIAL
Y Value | TEMP_MDATA_SETVALUE_VAL_Y | REAL |  |  |  | 
Z | MDATA_SETVALUE_SETZ | LONG |  |  |  | MDATA_SETVALUE_SET_LEAVE; MDATA_SETVALUE_SET_SET; MDATA_SETVALUE_SET_CENTER; MDATA_SETVALUE_SET_QUANTIZE; MDATA_SETVALUE_CRUMPLE_ALONGNORMALS; MDATA_SETVALUE_CRUMPLE_AXIAL; MDATA_SETVALUE_CRUMPLE_RADIAL
Z Value | TEMP_MDATA_SETVALUE_VAL_Z | REAL |  |  |  | 
Coordinate System | MDATA_SETVALUE_SYSTEM | LONG |  |  |  | MDATA_SETVALUE_SYSTEM_OBJECT; MDATA_SETVALUE_SYSTEM_WORLD; MDATA_SETVALUE_SYSTEM_SCREEN
In and Out | MDATA_SETVALUE_INOUT | BOOL |  |  |  | 
Seed | MDATA_SETVALUE_SEED | LONG |  |  |  | 
