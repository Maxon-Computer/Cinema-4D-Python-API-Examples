# Description: Object Operator

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/xpressocore/description/gvobject.res`
- **Symbol:** `GVobject`
- **Category:** Graph View

Use parameter symbols to access parameters and cycle option symbols for cycle values, never their numeric IDs. Treat Min and Max as constraints and Default as the declared initial value; blank cells mean the resource does not declare that metadata, not that the value is zero. Base Description Parameters lists inherited fields from each base; All Parameters lists the effective parameter set for this description.

## Base Description Parameters

### Node (`GVbase`)

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Enabled | ID_GVBASE_ENABLE | BOOL |  |  |  | 
Title Color | ID_GVBASE_COLOR | COLOR |  |  |  | 
Remark | ID_GVBASE_REMARK | STRING |  |  |  | 

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
Enabled | ID_GVBASE_ENABLE | BOOL |  |  |  | 
Title Color | ID_GVBASE_COLOR | COLOR |  |  |  | 
Remark | ID_GVBASE_REMARK | STRING |  |  |  | 
Reference | GV_OBJECT_OBJECT_ID | LINK |  |  |  | 
Reference Mode | GV_OBJECT_PATH_TYPE | LONG |  |  |  | GV_OBJECT_PATH_TYPE_START; GV_OBJECT_PATH_TYPE_ABSOLUTE; GV_OBJECT_PATH_TYPE_RELATIVE
Start Position | GV_OBJECT_START_TYPE_ID | LONG |  |  |  | 
Start Distance | GV_OBJECT_DISTANCE_ID | LONG | 1 |  |  | 
History Depth | GV_OBJECT_HISTORY_DEPTH_ID | LONG | 1 |  |  | 
Path | GV_OBJECT_PATH_ID | STRING |  |  |  | 
Local Matrix | GV_OBJECT_OPERATOR_LOCAL_IN | MATRIX |  |  |  | 
Global Matrix | GV_OBJECT_OPERATOR_GLOBAL_IN | MATRIX |  |  |  | 
History level | GV_OBJECT_OPERATOR_HISTORY_IN | LONG |  |  |  | 
Object | GV_OBJECT_OPERATOR_OBJECT_IN | GVGENERALINSTANCE |  |  |  | 
On | GV_OBJECT_OPERATOR_ON | BOOL |  |  |  | 
Local Matrix | GV_OBJECT_OPERATOR_LOCAL_OUT | MATRIX |  |  |  | 
Global Matrix | GV_OBJECT_OPERATOR_GLOBAL_OUT | MATRIX |  |  |  | 
Object | GV_OBJECT_OPERATOR_OBJECT_OUT | GVGENERALINSTANCE |  |  |  | 
Previous position | GV_OBJECT_OPERATOR_OLD_POS_OUT | VECTOR |  |  |  | 
Previous rotation | GV_OBJECT_OPERATOR_OLD_ROT_OUT | VECTOR |  |  |  | 
Previous scale | GV_OBJECT_OPERATOR_OLD_SIZE_OUT | VECTOR |  |  |  | 
Previous global matrix | GV_OBJECT_OPERATOR_OLD_GLOBAL_OUT | MATRIX |  |  |  | 
Previous local matrix | GV_OBJECT_OPERATOR_OLD_LOCAL_OUT | MATRIX |  |  |  | 
Position velocity | GV_OBJECT_OPERATOR_VELOCITY_POS_OUT | VECTOR |  |  |  | 
Rotation velocity | GV_OBJECT_OPERATOR_VELOCITY_ROT_OUT | VECTOR |  |  |  | 
Scale velocity | GV_OBJECT_OPERATOR_VELOCITY_SIZE_OUT | VECTOR |  |  |  | 
