# Description: Collision Operator

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/xpressocore/description/gvcollision.res`
- **Symbol:** `GVcollision`
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
Collision Type | GV_COLLISION_TYPE | LONG |  |  |  | GV_COLLISION_OPERATOR_TYPE_CUBE; GV_COLLISION_OPERATOR_TYPE_SPHERE; GV_COLLISION_OPERATOR_TYPE_POLYGON; GV_COLLISION_OPERATOR_TYPE_DISTANCE; GV_COLLISION_OPERATOR_TYPE_TOLERANCE
Use Deformed Points | GV_COLLISION_USE_DEFORMED | BOOL |  |  |  | 
Matrix Mode | GV_COLLISION_MODE | LONG |  |  |  | GV_COLLISION_OPERATOR_MODE_GLOBAL; GV_COLLISION_OPERATOR_MODE_LOCAL
Include Children | GV_COLLISION_USE_HIERARCHY | BOOL |  |  |  | 
Selection Tag 1 | GV_COLLISION_SELECTION1 | LINK |  |  |  | 
Selection Tag 2 | GV_COLLISION_SELECTION2 | LINK |  |  |  | 
Object 1 | GV_COLLISION_INPUT_OBJECT1 | GVGENERALOBJECT |  |  |  | 
Object 2 | GV_COLLISION_INPUT_OBJECT2 | GVGENERALOBJECT |  |  |  | 
Tolerance | GV_COLLISION_INPUT_TOLERANCE | REAL | 0 |  |  | 
Collision | GV_COLLISION_OUTPUT | BOOL |  |  |  | 
Distance | GV_COLLISION_OUTPUT_DISTANCE | REAL |  |  |  | 
Polygon Index 1 | GV_COLLISION_OUTPUT_INDEX1 | LONG |  |  |  | 
Polygon Index 2 | GV_COLLISION_OUTPUT_INDEX2 | LONG |  |  |  | 
Point 1 | GV_COLLISION_OUTPUT_POINT1 | VECTOR |  |  |  | 
Point 2 | GV_COLLISION_OUTPUT_POINT2 | VECTOR |  |  |  | 
