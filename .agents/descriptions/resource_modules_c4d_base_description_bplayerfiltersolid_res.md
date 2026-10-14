# Description: Fill Solid Color Layer

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/c4d_base/description/bplayerfiltersolid.res`
- **Symbol:** `BPlayerfiltersolid`
- **Category:** Other

Use parameter symbols to access parameters and cycle option symbols for cycle values, never their numeric IDs. Treat Min and Max as constraints and Default as the declared initial value; blank cells mean the resource does not declare that metadata, not that the value is zero. Base Description Parameters lists inherited fields from each base; All Parameters lists the effective parameter set for this description.

## Base Description Parameters

### Filter Layer (`BPlayerfilterbase`)

No parameters.

### Base Layer (`BPlayer`)

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Visible | ID_PAINTLAYER_SHOW | BOOL |  |  |  | 
Blend Mode | ID_PAINTLAYER_BLEND | LONG |  |  |  | LAYER_PASSFOLDER; LAYER_NORMAL; LAYER_DISSOLVE; 0; LAYER_DARKEN; LAYER_MULTIPLY; LAYER_COLORBURN; LAYER_LINEARBURN; 0; LAYER_LIGHTEN; LAYER_SCREEN; LAYER_COLORDODGE; LAYER_LINEARDODGE; LAYER_ADD; 0; LAYER_OVERLAY; LAYER_SOFTLIGHT; LAYER_HARDLIGHT; LAYER_STAMP; LAYER_PINLIGHT; LAYER_HARDMIX; 0; LAYER_DIFFERENCE; LAYER_EXCLUSION; LAYER_REFLECT; LAYER_NEGATION; LAYER_GLOW; LAYER_AVERAGE; LAYER_FREEZE; LAYER_HEAT
Opacity | ID_PAINTLAYER_OPACITY | REAL | 0.0 | 100.0 |  | 
Texture Profile | ID_PAINTLAYER_TEXPROFILE | COLORPROFILE |  |  |  | 
Texture Link | ID_PAINTLAYER_TEXTURE_LINK | LINK |  |  |  | 
Texture Name | ID_PAINTLAYER_TEXTURE_NAME | STATICTEXT |  |  |  | 

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
Visible | ID_PAINTLAYER_SHOW | BOOL |  |  |  | 
Blend Mode | ID_PAINTLAYER_BLEND | LONG |  |  |  | LAYER_PASSFOLDER; LAYER_NORMAL; LAYER_DISSOLVE; 0; LAYER_DARKEN; LAYER_MULTIPLY; LAYER_COLORBURN; LAYER_LINEARBURN; 0; LAYER_LIGHTEN; LAYER_SCREEN; LAYER_COLORDODGE; LAYER_LINEARDODGE; LAYER_ADD; 0; LAYER_OVERLAY; LAYER_SOFTLIGHT; LAYER_HARDLIGHT; LAYER_STAMP; LAYER_PINLIGHT; LAYER_HARDMIX; 0; LAYER_DIFFERENCE; LAYER_EXCLUSION; LAYER_REFLECT; LAYER_NEGATION; LAYER_GLOW; LAYER_AVERAGE; LAYER_FREEZE; LAYER_HEAT
Opacity | ID_PAINTLAYER_OPACITY | REAL | 0.0 | 100.0 |  | 
Texture Profile | ID_PAINTLAYER_TEXPROFILE | COLORPROFILE |  |  |  | 
Texture Link | ID_PAINTLAYER_TEXTURE_LINK | LINK |  |  |  | 
Texture Name | ID_PAINTLAYER_TEXTURE_NAME | STATICTEXT |  |  |  | 
Fill Color | ID_PAINTLAYERFILTERSOLID_COLOR | COLOR |  |  |  | 
