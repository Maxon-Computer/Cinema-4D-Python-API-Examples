# Description: Spline Operator

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/xpressocore/description/gvspline.res`
- **Symbol:** `GVspline`
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
Matrix Mode | GV_SPLINE_MODE | LONG |  |  |  | GV_SPLINE_OPERATOR_MODE_GLOBAL; GV_SPLINE_OPERATOR_MODE_LOCAL
Use Uniform Distribution | GV_SPLINE_USE_NATURAL | BOOL |  |  |  | 
Use All Segments | GV_SPLINE_ALL_SEGMENTS | BOOL |  |  |  | 
Object | GV_SPLINE_INPUT_OBJECT | GVGENERALOBJECT |  |  |  | 
Offset | GV_SPLINE_INPUT_POINT | REAL | 0 | 100 |  | 
Segment | GV_SPLINE_INPUT_SEGMENT | LONG | 0 |  |  | 
Position | GV_SPLINE_OUTPUT_POSITION | VECTOR |  |  |  | 
Tangent | GV_SPLINE_OUTPUT_TANGENT | VECTOR |  |  |  | 
Length | GV_SPLINE_OUTPUT_LENGTH | REAL |  |  |  | 
Closed | GV_SPLINE_OUTPUT_IS_CLOSED | BOOL |  |  |  | 
Segments | GV_SPLINE_OUTPUT_SEGMENTS | LONG |  |  |  | 
