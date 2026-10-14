# Description: Soft Selection

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/hair/description/toolhairsoftselection.res`
- **Symbol:** `ToolHairSoftSelection`
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
Soft Selection | HAIR_SOFTSELECTION | BOOL |  |  |  | 
Preview | HAIR_SOFTSELECTION_PREVIEW | BOOL |  |  |  | 
Tweak | HAIR_SOFTSELECTION_TWEAK | BOOL |  |  |  | 
Visible | HAIR_SOFTSELECTION_VISIBLE | BOOL |  |  |  | 
Type | HAIR_SOFTSELECTION_TYPE | LONG |  |  |  | HAIR_SOFTSELECTION_TYPE_SINGLE; HAIR_SOFTSELECTION_TYPE_VOLUME; HAIR_SOFTSELECTION_TYPE_ROOT
Coords | HAIR_SOFTSELECTION_SPACE | LONG |  |  |  | HAIR_SOFTSELECTION_SPACE_WORLD; HAIR_SOFTSELECTION_SPACE_SCREEN
Radius | HAIR_SOFTSELECTION_RADIUS | REAL | 0.0 |  |  | 
Strength | HAIR_SOFTSELECTION_STRENGTH | REAL | 0.0 | 100.0 |  | 
Clip | HAIR_SOFTSELECTION_CLIP | BOOL |  |  |  | 
Falloff | HAIR_SOFTSELECTION_FALLOFF | LONG |  |  |  | HAIR_SOFTSELECTION_FALLOFF_NONE; HAIR_SOFTSELECTION_FALLOFF_LINEAR; HAIR_SOFTSELECTION_FALLOFF_DOME; HAIR_SOFTSELECTION_FALLOFF_BELL; HAIR_SOFTSELECTION_FALLOFF_CIRCLE; HAIR_SOFTSELECTION_FALLOFF_NEEDLE; HAIR_SOFTSELECTION_FALLOFF_SPLINE
Width | HAIR_SOFTSELECTION_WIDTH | REAL | 0.0 | 100.0 |  | 
Falloff Curve | HAIR_SOFTSELECTION_FALLOFF_CURVE | SPLINE |  |  |  | 
