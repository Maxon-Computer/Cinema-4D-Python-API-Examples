# Description: Push

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/hair/description/toolhairpush.res`
- **Symbol:** `ToolHairPush`
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
Select Pushed | HAIR_TOOL_PUSH_SELECT | BOOL |  |  |  | 
Surface | HAIR_TOOL_PUSH_SURFACE | BOOL |  |  |  | 
Use Normal | HAIR_TOOL_PUSH_USE_NORMAL | BOOL |  |  |  | 
Distance | HAIR_TOOL_PUSH_DISTANCE | REAL | 0.0 |  |  | 
Strength | HAIR_TOOL_PUSH_CURVE | SPLINE |  |  |  | 
Guides | HAIR_TOOL_PUSH_GUIDES | BOOL |  |  |  | 
Distance | HAIR_TOOL_PUSH_GUIDES_DISTANCE | REAL | 0.0 |  |  | 
Relaxation | HAIR_TOOL_PUSH_GUIDES_RELAX | REAL | 4 | 1000 |  | 
Strength | HAIR_TOOL_PUSH_GUIDES_CURVE | SPLINE |  |  |  | 
