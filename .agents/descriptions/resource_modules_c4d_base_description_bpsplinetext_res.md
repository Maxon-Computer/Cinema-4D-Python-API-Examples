# Description: Path Text

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/c4d_base/description/bpsplinetext.res`
- **Symbol:** `BPsplinetext`
- **Category:** Other

Use parameter symbols to access parameters and cycle option symbols for cycle values, never their numeric IDs. Treat Min and Max as constraints and Default as the declared initial value; blank cells mean the resource does not declare that metadata, not that the value is zero. Base Description Parameters lists inherited fields from each base; All Parameters lists the effective parameter set for this description.

## Base Description Parameters

### Path (`BPspline`)

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Preview | ID_PAINTSPLINE_PREVIEW | BITMAPBUTTON |  |  |  | 
Position | ID_PAINTSPLINE_POSITION | VECTOR |  |  |  | 
Scale | ID_PAINTSPLINE_SCALE | VECTOR |  |  |  | 
Rotation | ID_PAINTSPLINE_ROTATION | VECTOR |  |  |  | 
Segments:  | ID_PAINTSPLINE_SEGMENTS | STATICTEXT |  |  |  | 
Point Count:  | ID_PAINTSPLINE_POINTS | STATICTEXT |  |  |  | 

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
Preview | ID_PAINTSPLINE_PREVIEW | BITMAPBUTTON |  |  |  | 
Position | ID_PAINTSPLINE_POSITION | VECTOR |  |  |  | 
Scale | ID_PAINTSPLINE_SCALE | VECTOR |  |  |  | 
Rotation | ID_PAINTSPLINE_ROTATION | VECTOR |  |  |  | 
Segments:  | ID_PAINTSPLINE_SEGMENTS | STATICTEXT |  |  |  | 
Point Count:  | ID_PAINTSPLINE_POINTS | STATICTEXT |  |  |  | 
Text | ID_PAINTSPLINETEXT_TEXT | STRING |  |  |  | 
Font | ID_PAINTSPLINETEXT_FONT | FONT |  |  |  | 
Align | ID_PAINTSPLINETEXT_ALIGN | LONG |  |  |  | 0,PAINTSPLINETEXT_ALIGN_LEFT; 1,PAINTSPLINETEXT_ALIGN_CENTER; 2,PAINTSPLINETEXT_ALIGN_RIGHT
Size | ID_PAINTSPLINETEXT_SIZE | REAL | 0 |  |  | 
Horizontal Spacing | ID_PAINTSPLINETEXT_SPACE_H | REAL |  |  |  | 
Vertical Spacing | ID_PAINTSPLINETEXT_SPACE_V | REAL |  |  |  | 
Separate Letters | ID_PAINTSPLINETEXT_SEPARATE | BOOL |  |  |  | 
