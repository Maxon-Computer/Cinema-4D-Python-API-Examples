# Description: RangeMapper Operator

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/xpressocore/description/gvrangemapper.res`
- **Symbol:** `GVrangemapper`
- **Category:** Graph View

Use parameter symbols to access parameters and cycle option symbols for cycle values, never their numeric IDs. Treat Min and Max as constraints and Default as the declared initial value; blank cells mean the resource does not declare that metadata, not that the value is zero. Base Description Parameters lists inherited fields from each base; All Parameters lists the effective parameter set for this description.

## Base Description Parameters

### Dynamic DataType Operator (`GVdynamic`)

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Data Type | GV_DYNAMIC_DATATYPE | LONG |  |  |  | 

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
Data Type | GV_DYNAMIC_DATATYPE | LONG |  |  |  | 
Input Range | GV_RANGEMAPPER_INPUT_DEFS | LONG |  |  |  | GV_RANGEMAPPER_INPUT_USER; GV_RANGEMAPPER_INPUT_DEGREE; GV_RANGEMAPPER_INPUT_RADIANS; GV_RANGEMAPPER_INPUT_PERCENT; GV_RANGEMAPPER_INPUT_ZERO_TO_ONE; GV_RANGEMAPPER_INPUT_ZERO_TO_HUNDRED; GV_RANGEMAPPER_INPUT_ZERO_TO_THOUSAND
Output Range | GV_RANGEMAPPER_OUTPUT_DEFS | LONG |  |  |  | GV_RANGEMAPPER_OUTPUT_USER; GV_RANGEMAPPER_OUTPUT_DEGREE; GV_RANGEMAPPER_OUTPUT_RADIANS; GV_RANGEMAPPER_OUTPUT_PERCENT; GV_RANGEMAPPER_OUTPUT_ZERO_TO_ONE; GV_RANGEMAPPER_OUTPUT_ZERO_TO_HUNDRED; GV_RANGEMAPPER_OUTPUT_ZERO_TO_THOUSAND
Clamp Lower | GV_RANGEMAPPER_CLAMP_LOWER | BOOL |  |  |  | 
Clamp Upper | GV_RANGEMAPPER_CLAMP_UPPER | BOOL |  |  |  | 
Modulo | GV_RANGEMAPPER_MODULO | BOOL |  |  |  | 
Reverse | GV_RANGEMAPPER_REVERSE | BOOL |  |  |  | 
Use Spline | GV_RANGEMAPPER_USE_SPLINE | BOOL |  |  |  | 
Input | GV_RANGEMAPPER_INPUT | DYNAMIC |  |  |  | 
Input Lower | GV_RANGEMAPPER_RANGE11 | DYNAMIC |  |  |  | 
Input Upper | GV_RANGEMAPPER_RANGE12 | DYNAMIC |  |  |  | 
Output Lower | GV_RANGEMAPPER_RANGE21 | DYNAMIC |  |  |  | 
Output Upper | GV_RANGEMAPPER_RANGE22 | DYNAMIC |  |  |  | 
Spline | GV_RANGEMAPPER_SPLINE | SPLINE |  |  |  | 
Output | GV_RANGEMAPPER_OUTPUT | DYNAMIC |  |  |  | 
