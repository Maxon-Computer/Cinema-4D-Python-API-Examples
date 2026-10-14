# Description: Rect Select

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/hair/description/toolhairrectselect.res`
- **Symbol:** `ToolHairRectSelect`
- **Category:** Other

Use parameter symbols to access parameters and cycle option symbols for cycle values, never their numeric IDs. Treat Min and Max as constraints and Default as the declared initial value; blank cells mean the resource does not declare that metadata, not that the value is zero. Base Description Parameters lists inherited fields from each base; All Parameters lists the effective parameter set for this description.

## Base Description Parameters

### Live Select (`ToolHairLiveSelect`)

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Radius | HAIR_LIVESELECT_RADIUS | REAL | 0.0 |  |  | 
Visible Only | HAIR_LIVESELECT_VISIBLE | BOOL |  |  |  | 
Restrict | HAIR_LIVESELECT_RESTRICT | BOOL |  |  |  | 
Select Locked | HAIR_LIVESELECT_LOCKED | BOOL |  |  |  | 
Shape | HAIR_LIVESELECT_SHAPE | LONG |  |  |  | HAIR_LIVESELECT_SHAPE_CIRCLE; HAIR_LIVESELECT_SHAPE_BOX; HAIR_LIVESELECT_SHAPE_DIAMOND
Pressure | HAIR_LIVESELECT_PEN | LONG |  |  |  | HAIR_LIVESELECT_PEN_NONE; HAIR_LIVESELECT_PEN_RADIUS; HAIR_LIVESELECT_PEN_STRENGTH
Aspect | HAIR_LIVESELECT_SHAPE_ASPECT | REAL | 0.0 | 10000.0 |  | 
Angle | HAIR_LIVESELECT_SHAPE_ANGLE | REAL |  |  |  | 

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
Radius | HAIR_LIVESELECT_RADIUS | REAL | 0.0 |  |  | 
Visible Only | HAIR_LIVESELECT_VISIBLE | BOOL |  |  |  | 
Restrict | HAIR_LIVESELECT_RESTRICT | BOOL |  |  |  | 
Select Locked | HAIR_LIVESELECT_LOCKED | BOOL |  |  |  | 
Shape | HAIR_LIVESELECT_SHAPE | LONG |  |  |  | HAIR_LIVESELECT_SHAPE_CIRCLE; HAIR_LIVESELECT_SHAPE_BOX; HAIR_LIVESELECT_SHAPE_DIAMOND
Pressure | HAIR_LIVESELECT_PEN | LONG |  |  |  | HAIR_LIVESELECT_PEN_NONE; HAIR_LIVESELECT_PEN_RADIUS; HAIR_LIVESELECT_PEN_STRENGTH
Aspect | HAIR_LIVESELECT_SHAPE_ASPECT | REAL | 0.0 | 10000.0 |  | 
Angle | HAIR_LIVESELECT_SHAPE_ANGLE | REAL |  |  |  | 
