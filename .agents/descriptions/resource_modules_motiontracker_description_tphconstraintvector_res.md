# Description: Vector Constraint

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/motiontracker/description/tphconstraintvector.res`
- **Symbol:** `Tphconstraintvector`
- **Category:** Tags

Use parameter symbols to access parameters and cycle option symbols for cycle values, never their numeric IDs. Treat Min and Max as constraints and Default as the declared initial value; blank cells mean the resource does not declare that metadata, not that the value is zero. Base Description Parameters lists inherited fields from each base; All Parameters lists the effective parameter set for this description.

## Base Description Parameters

### Base Tag (`Tbase`)

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Expose on Object | ID_EXPOSETAB | BOOL |  |  |  | 

### Basic Properties (`Obaselist`)

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Icon File / ID | ID_BASELIST_ICON_FILE | TEXTURE |  |  |  | 
Icon Color | ID_BASELIST_ICON_COLORIZE_MODE | BOOL |  |  |  | 
Color | ID_BASELIST_ICON_COLOR | COLOR |  |  | 1.0 0.9 0.4 | 
No label | ID_BASELIST_ICON_PRESET_BUTTONS | ICONCHOOSER |  |  |  | 
Name | ID_BASELIST_NAME | STRING |  |  |  | 
Layer | ID_LAYER_LINK | LINK |  |  |  | 
No label | ID_BASELIST_NODESPACE_ADD_REMOVE_BUTTONS | NODESPACE_ADD_REMOVE |  |  |  | 

## All Parameters

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Icon File / ID | ID_BASELIST_ICON_FILE | TEXTURE |  |  |  | 
Icon Color | ID_BASELIST_ICON_COLORIZE_MODE | BOOL |  |  |  | 
Color | ID_BASELIST_ICON_COLOR | COLOR |  |  | 1.0 0.9 0.4 | 
No label | ID_BASELIST_ICON_PRESET_BUTTONS | ICONCHOOSER |  |  |  | 
Name | ID_BASELIST_NAME | STRING |  |  |  | 
Layer | ID_LAYER_LINK | LINK |  |  |  | 
No label | ID_BASELIST_NODESPACE_ADD_REMOVE_BUTTONS | NODESPACE_ADD_REMOVE |  |  |  | 
Expose on Object | ID_EXPOSETAB | BOOL |  |  |  | 
Mode | PH_SCENE_CAL_VECTOR_MODE | LONG |  |  |  | PH_SCENE_CAL_VECTOR_MODE_CAMTRACK; PH_SCENE_CAL_VECTOR_MODE_SELECT
Axis | PH_SCENE_CAL_VECTOR_AXIS | LONG |  |  |  | PH_SCENE_CAL_VECTOR_AXIS_NONE; PH_SCENE_CAL_VECTOR_AXIS_X; PH_SCENE_CAL_VECTOR_AXIS_Y; PH_SCENE_CAL_VECTOR_AXIS_Z
Reverse Axis | PH_SCENE_CAL_VECTOR_FLIP_AXIS | BOOL |  |  |  | 
Length | PH_SCENE_CAL_VECTOR_HAS_MEASUREMENT | LONG |  |  |  | PH_SCENE_CAL_VECTOR_WORLD_LENGTH_UNKNOWN; PH_SCENE_CAL_VECTOR_WORLD_LENGTH_KNOWN
No label | PH_SCENE_CAL_VECTOR_WORLD_LENGTH | REAL | 0.0 |  |  | 
Target | PH_SCENE_CAL_VECTOR_TARGET_0 | LINK |  |  |  | 
Target | PH_SCENE_CAL_VECTOR_TARGET_1 | LINK |  |  |  | 
Update Calibration | PH_SCENE_CAL_VECTOR_FORCE_EXPORT | BUTTON |  |  |  | 
