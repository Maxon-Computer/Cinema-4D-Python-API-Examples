# Description: Lighting Tool

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/c4d_objects/description/toollightplacer.res`
- **Symbol:** `ToolLightPlacer`
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
Mode | MDATA_LIGHTPLACER_MODE | LONG |  |  |  | MDATA_LIGHTPLACER_MODE_TRACKBALL; MDATA_LIGHTPLACER_MODE_SURFACE; MDATA_LIGHTPLACER_MODE_DIFFUSE; MDATA_LIGHTPLACER_MODE_SPECULAR; MDATA_LIGHTPLACER_MODE_TARGET; MDATA_LIGHTPLACER_MODE_PIVOT
Selection Method | MDATA_LIGHTPLACER_SELMODE | LONG |  |  |  | MDATA_LIGHTPLACER_SELMODE_ANGLE; MDATA_LIGHTPLACER_SELMODE_LIGHT
Modify Lights Only | MDATA_LIGHTPLACER_LIGHTONLY | BOOL |  |  |  | 
Highlighting | MDATA_LIGHTPLACER_HIGHLIGHTING | BOOL |  |  |  | 
Pivot | MDATA_LIGHTPLACER_PIVOT | VECTOR |  |  |  | 
Place Pivot | MDATA_LIGHTPLACER_PLACEPIVOT | BUTTON |  |  |  | 
Add Light | MDATA_LIGHTPLACER_ADDLIGHT | BUTTON |  |  |  | 
