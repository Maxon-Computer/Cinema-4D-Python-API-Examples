# Description: Comb

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/hair/description/toolhaircomb.res`
- **Symbol:** `ToolHairComb`
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
Direction | HAIR_TOOL_COMB_DIRECTION | LONG |  |  |  | HAIR_TOOL_COMB_DIRECTION_CAMERA_X; HAIR_TOOL_COMB_DIRECTION_CAMERA_Y; HAIR_TOOL_COMB_DIRECTION_CAMERA_Z; HAIR_TOOL_COMB_DIRECTION_WORLD_X; HAIR_TOOL_COMB_DIRECTION_WORLD_Y; HAIR_TOOL_COMB_DIRECTION_WORLD_Z; HAIR_TOOL_COMB_DIRECTION_LOCAL_X; HAIR_TOOL_COMB_DIRECTION_LOCAL_Y; HAIR_TOOL_COMB_DIRECTION_LOCAL_Z; HAIR_TOOL_COMB_DIRECTION_SPLINE; HAIR_TOOL_COMB_DIRECTION_SHADER
Strength | HAIR_TOOL_COMB_STRENGTH | REAL | -100.0 | 100.0 |  | 
Spline | HAIR_TOOL_COMB_SPLINE | LINK |  |  |  | 
Texture | HAIR_TOOL_COMB_SHADER | TEXTURE |  |  |  | 
Curve | HAIR_TOOL_COMB_CURVE | SPLINE |  |  |  | 
From Root | HAIR_TOOL_COMB_FROMROOT | BOOL |  |  |  | 
Prevent Intersection | HAIR_TOOL_COMB_INTERSECT | BOOL |  |  |  | 
Geometry Weighting | HAIR_TOOL_COMB_WEIGHTED | BOOL |  |  |  | 
Weight | HAIR_TOOL_COMB_WEIGHT | REAL | 0.0 | 100.0 |  | 
Limit | HAIR_TOOL_COMB_LIMIT_DISTANCE | BOOL |  |  |  | 
Distance | HAIR_TOOL_COMB_DISTANCE | REAL | 0.0 |  |  | 
