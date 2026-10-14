# Description: Python Operator

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/python/description/gvpython.res`
- **Symbol:** `GVpython`
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
Frame Dependent | GV_PYTHON_FRAME | BOOL |  |  |  | 
Reset on Frame 0 | GV_PYTHON_RESET | BOOL |  |  |  | 
Code | GV_PYTHON_CODE | STRING |  |  |  | 
Open Python Editor | GV_PYTHON_OPENEDITOR | BUTTON |  |  |  | 
On | GV_PYTHON_ON | BOOL |  |  |  | 
Integer | IN_LONG | LONG |  |  |  | 
Integer | OUT_LONG | LONG |  |  |  | 
String | IN_STRING | STRING |  |  |  | 
String | OUT_STRING | STRING |  |  |  | 
Float | IN_REAL | REAL |  |  |  | 
Float | OUT_REAL | REAL |  |  |  | 
Vector | IN_VECTOR | VECTOR |  |  |  | 
Vector | OUT_VECTOR | VECTOR |  |  |  | 
Matrix | IN_MATRIX | MATRIX |  |  |  | 
Matrix | OUT_MATRIX | MATRIX |  |  |  | 
Time | IN_BASETIME | BASETIME |  |  |  | 
Time | OUT_BASETIME | BASETIME |  |  |  | 
Bool | IN_BOOL | BOOL |  |  |  | 
Bool | OUT_BOOL | BOOL |  |  |  | 
Link | IN_LINK | LINK |  |  |  | 
Link | OUT_LINK | LINK |  |  |  | 
Filename | IN_FILENAME | FILENAME |  |  |  | 
Filename | OUT_FILENAME | FILENAME |  |  |  | 
Particle ID | IN_TP | TP_PARTICLE |  |  |  | 
Particle ID | OUT_TP | TP_PARTICLE |  |  |  | 
Gradient | IN_GRADIENT | GRADIENT |  |  |  | 
Gradient | OUT_GRADIENT | GRADIENT |  |  |  | 
InExcludeList | IN_INEXCLUDELIST | IN_EXCLUDE |  |  |  | 
InExcludeList | OUT_INEXCLUDELIST | IN_EXCLUDE |  |  |  | 
SplineData | IN_SPLINEDATA | SPLINE |  |  |  | 
SplineData | OUT_SPLINEDATA | SPLINE |  |  |  | 
SoundData | IN_SOUNDDATA | SOUNDDATA |  |  |  | 
SoundData | OUT_SOUNDDATA | SOUNDDATA |  |  |  | 
