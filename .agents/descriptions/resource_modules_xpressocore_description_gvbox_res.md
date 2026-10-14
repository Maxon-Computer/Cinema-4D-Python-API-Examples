# Description: Bounding Box Operator

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/xpressocore/description/gvbox.res`
- **Symbol:** `GVbox`
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
Matrix Mode | GV_BOX_MODE | LONG |  |  |  | GV_BOX_OPERATOR_MODE_GLOBAL; GV_BOX_OPERATOR_MODE_LOCAL
Use Deformed Points | GV_BOX_USE_DEFORMED | BOOL |  |  |  | 
Object | GV_BOX_INPUT_OBJECT | GVGENERALOBJECT |  |  |  | 
Box Minimum | GV_BOX_OUTPUT_POINT_MIN | VECTOR |  |  |  | 
Box Maximum | GV_BOX_OUTPUT_POINT_MAX | VECTOR |  |  |  | 
Box Size | GV_BOX_OUTPUT_POINT_SIZE | VECTOR |  |  |  | 
Box Point 1 | GV_BOX_OUTPUT_POINT1 | VECTOR |  |  |  | 
Box Point 2 | GV_BOX_OUTPUT_POINT2 | VECTOR |  |  |  | 
Box Point 3 | GV_BOX_OUTPUT_POINT3 | VECTOR |  |  |  | 
Box Point 4 | GV_BOX_OUTPUT_POINT4 | VECTOR |  |  |  | 
Box Point 5 | GV_BOX_OUTPUT_POINT5 | VECTOR |  |  |  | 
Box Point 6 | GV_BOX_OUTPUT_POINT6 | VECTOR |  |  |  | 
Box Point 7 | GV_BOX_OUTPUT_POINT7 | VECTOR |  |  |  | 
Box Point 8 | GV_BOX_OUTPUT_POINT8 | VECTOR |  |  |  | 
