# Description: Texture

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/c4d_base/description/bptexture.res`
- **Symbol:** `BPtexture`
- **Category:** Other

Use parameter symbols to access parameters and cycle option symbols for cycle values, never their numeric IDs. Treat Min and Max as constraints and Default as the declared initial value; blank cells mean the resource does not declare that metadata, not that the value is zero. Base Description Parameters lists inherited fields from each base; All Parameters lists the effective parameter set for this description.

## Base Description Parameters

### Base Bitmap (`BPbitmap`)

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Preview | ID_PAINTBITMAP_PREVIEW | BITMAPBUTTON |  |  |  | 
Width | ID_PAINTBITMAP_SIZE_X | STATICTEXT |  |  |  | 
Height | ID_PAINTBITMAP_SIZE_Y | STATICTEXT |  |  |  | 
Memory Usage | ID_PAINTBITMAP_MEMORY | STATICTEXT |  |  |  | 

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
Preview | ID_PAINTBITMAP_PREVIEW | BITMAPBUTTON |  |  |  | 
Width | ID_PAINTBITMAP_SIZE_X | STATICTEXT |  |  |  | 
Height | ID_PAINTBITMAP_SIZE_Y | STATICTEXT |  |  |  | 
Memory Usage | ID_PAINTBITMAP_MEMORY | STATICTEXT |  |  |  | 
File Format | ID_PAINTTEXTURE_SAVEFORMAT | LONG |  |  |  | 
Filename | ID_PAINTTEXTURE_FILENAME | FILENAME |  |  |  | 
Color Profile | ID_PAINTTEXTURE_ICCPROFILE | COLORPROFILE |  |  |  | 
DPI | ID_PAINTTEXTURE_DPI | REAL |  |  |  | 
Aspect Ratio | ID_PAINTTEXTURE_ASPECTRATIO | REAL |  |  |  | 
Mode | ID_PAINTTEXTURE_MODE | STATICTEXT |  |  |  | 
Paths | ID_PAINTTEXTURE_PATHS | STATICTEXT |  |  |  | 
