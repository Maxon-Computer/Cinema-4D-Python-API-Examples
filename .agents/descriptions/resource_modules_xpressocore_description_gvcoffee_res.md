# Description: C.O.F.F.E.E. Operator

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/xpressocore/description/gvcoffee.res`
- **Symbol:** `GVcoffee`
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
Script | GV_COFFEE_CODE | STRING |  |  |  | 
Unprotect... | GV_COFFEE_UNLOCK | BUTTON |  |  |  | 
On | GV_COFFEE_ON | BOOL |  |  |  | 
Bool | GV_COFFEE_BOOL_INPUT | BOOL |  |  |  | 
Bool | GV_COFFEE_BOOL_OUTPUT | BOOL |  |  |  | 
Integer | GV_COFFEE_LONG_INPUT | LONG |  |  |  | 
Integer | GV_COFFEE_LONG_OUTPUT | LONG |  |  |  | 
Real | GV_COFFEE_REAL_INPUT | REAL |  |  |  | 
Real | GV_COFFEE_REAL_OUTPUT | REAL |  |  |  | 
Time | GV_COFFEE_TIME_INPUT | BASETIME |  |  |  | 
Time | GV_COFFEE_TIME_OUTPUT | BASETIME |  |  |  | 
Vector | GV_COFFEE_VECTOR_INPUT | VECTOR |  |  |  | 
Vector | GV_COFFEE_VECTOR_OUTPUT | VECTOR |  |  |  | 
Matrix | GV_COFFEE_MATRIX_INPUT | MATRIX |  |  |  | 
Matrix | GV_COFFEE_MATRIX_OUTPUT | MATRIX |  |  |  | 
String | GV_COFFEE_STRING_INPUT | STRING |  |  |  | 
String | GV_COFFEE_STRING_OUTPUT | STRING |  |  |  | 
Filename | GV_COFFEE_FILENAME_INPUT | FILENAME |  |  |  | 
Filename | GV_COFFEE_FILENAME_OUTPUT | FILENAME |  |  |  | 
Link | GV_COFFEE_LINK_INPUT | LINK |  |  |  | 
Link | GV_COFFEE_LINK_OUTPUT | LINK |  |  |  | 
