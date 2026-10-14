# Description: Get Nearest Point on Spline Operator

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/xpressocore/description/gvnearestpointonspline.res`
- **Symbol:** `GVnearestpointonspline`
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
Spline Object | GV_NEARESTPOINTONSPLINE_INPUT_SPLINEOBJECT | GVGENERALOBJECT |  |  |  | 
Global Position | GV_NEARESTPOINTONSPLINE_INPUT_GLOBALPOSITION | VECTOR |  |  |  | 
Precision | GV_NEARESTPOINTONSPLINE_INPUT_PRECISION | REAL |  |  |  | 
Spline Segment | GV_NEARESTPOINTONSPLINE_INPUT_SPLINESEGMENT | LONG |  |  |  | 
All Segments | GV_NEARESTPOINTONSPLINE_INPUT_ALLSEGMENTS | BOOL |  |  |  | 
Spline Position | GV_NEARESTPOINTONSPLINE_OUTPUT_SPLINEPOSITION | REAL |  |  |  | 
Nearest Point | GV_NEARESTPOINTONSPLINE_OUTPUT_NEARESTPOINT | VECTOR |  |  |  | 
Nearest Segment | GV_NEARESTPOINTONSPLINE_OUTPUT_NEARESTSEGMENT | LONG |  |  |  | 
Tangent | GV_NEARESTPOINTONSPLINE_OUTPUT_TANGENT | VECTOR |  |  |  | 
