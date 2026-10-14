# Description: Hair Points

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/hair/description/gvhair_point.res`
- **Symbol:** `GVhair_point`
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
Reference | GV_HAIR_POINT_OBJECT | LINK |  |  |  | 
Mode | GV_HAIR_POINT_MODE | LONG |  |  |  | GV_HAIR_POINT_MODE_GUIDE; GV_HAIR_POINT_MODE_DYNAMIC_GUIDE; GV_HAIR_POINT_MODE_HAIR
Object | GV_HAIR_POINT_INPUT_OBJECT | GVGENERALOBJECT |  |  |  | 
On | GV_HAIR_POINT_INPUT_ON | BOOL |  |  |  | 
Guide | GV_HAIR_POINT_INPUT_GUIDE | LONG |  |  |  | 
Index | GV_HAIR_POINT_INPUT_POINT | LONG |  |  |  | 
Segment | GV_HAIR_POINT_INPUT_SEGMENT | LONG |  |  |  | 
Segment Delta | GV_HAIR_POINT_INPUT_T | REAL |  |  |  | 
Position | GV_HAIR_POINT_INPUT_SET_POS | VECTOR |  |  |  | 
Dynamic Position | GV_HAIR_POINT_INPUT_SET_DYN_POS | VECTOR |  |  |  | 
Velocity | GV_HAIR_POINT_INPUT_SET_VELOCITY | VECTOR |  |  |  | 
Mass | GV_HAIR_POINT_INPUT_SET_MASS | REAL |  |  |  | 
Add Force | GV_HAIR_POINT_INPUT_ADD_FORCE | VECTOR |  |  |  | 
Position | GV_HAIR_POINT_POINT_VEC | VECTOR |  |  |  | 
Tangent | GV_HAIR_POINT_POINT_TANGENT | VECTOR |  |  |  | 
Velocity | GV_HAIR_POINT_POINT_VELOCITY | VECTOR |  |  |  | 
Mass | GV_HAIR_POINT_POINT_MASS | REAL |  |  |  | 
Force | GV_HAIR_POINT_POINT_FORCE | VECTOR |  |  |  | 
