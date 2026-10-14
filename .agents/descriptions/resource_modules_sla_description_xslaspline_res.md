# Description: Spline Shader

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/sla/description/xslaspline.res`
- **Symbol:** `XSLASpline`
- **Category:** Shaders

Use parameter symbols to access parameters and cycle option symbols for cycle values, never their numeric IDs. Treat Min and Max as constraints and Default as the declared initial value; blank cells mean the resource does not declare that metadata, not that the value is zero. Base Description Parameters lists inherited fields from each base; All Parameters lists the effective parameter set for this description.

## Base Description Parameters

### No label (`Mpreview`)

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
No label | MATERIAL_PREVIEW | MATPREVIEW |  |  |  | 

### Shader (`Xbase`)

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Blur Offset | SHADER_MIPOFFSET | REAL | 0.0 | 100.0 |  | 
Blur Scale | SHADER_MIPSCALE | REAL | -100.0 | 100.0 |  | 

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
No label | MATERIAL_PREVIEW | MATPREVIEW |  |  |  | 
Icon File / ID | ID_BASELIST_ICON_FILE | TEXTURE |  |  |  | 
Icon Color | ID_BASELIST_ICON_COLORIZE_MODE | BOOL |  |  |  | 
Color | ID_BASELIST_ICON_COLOR | COLOR |  |  | 1.0 0.9 0.4 | 
No label | ID_BASELIST_ICON_PRESET_BUTTONS | ICONCHOOSER |  |  |  | 
Name | ID_BASELIST_NAME | STRING |  |  |  | 
Layer | ID_LAYER_LINK | LINK |  |  |  | 
No label | ID_BASELIST_NODESPACE_ADD_REMOVE_BUTTONS | NODESPACE_ADD_REMOVE |  |  |  | 
Blur Offset | SHADER_MIPOFFSET | REAL | 0.0 | 100.0 |  | 
Blur Scale | SHADER_MIPSCALE | REAL | -100.0 | 100.0 |  | 
Spline | SLA_SPLINE_OBJECT | LINK |  |  |  | 
Background Texture | SLA_SPLINE_BACKGROUND_COLOR | SHADERLINK |  |  |  | 
Line Texture | SLA_SPLINE_LINE_COLOR | SHADERLINK |  |  |  | 
Fill Texture | SLA_SPLINE_FILLET_COLOR | SHADERLINK |  |  |  | 
X Offset | SLA_SPLINE_X_OFFSET | REAL | -100000 | 100000 |  | 
Y Offset | SLA_SPLINE_Y_OFFSET | REAL | -100000 | 100000 |  | 
X Scale | SLA_SPLINE_X_SCALE | REAL | -100000 | 100000 |  | 
Y Scale | SLA_SPLINE_Y_SCALE | REAL | -100000 | 100000 |  | 
Plane | SLA_SPLINE_USE_PLANE | LONG |  |  |  | SLA_SPLINE_USE_PLANE_XY; SLA_SPLINE_USE_PLANE_XZ; SLA_SPLINE_USE_PLANE_YZ
Single Pixel | SLA_SPLINE_SINGLE_PIXEL_WIDTH | BOOL |  |  |  | 
Line Width | SLA_SPLINE_LINE_WIDTH | REAL | 0 | 10000 |  | 
Smooth Width | SLA_SPLINE_SMOOTH_WIDTH | REAL | 0 | 10000 |  | 
Caps | SLA_SPLINE_HAS_CAPS | BOOL |  |  |  | 
Fill | SLA_SPLINE_FILL | BOOL |  |  |  | 
Use Fill Color | SLA_SPLINE_FILL_COLOR | BOOL |  |  |  | 
Bump Width | SLA_SPLINE_BUMP_WIDTH | REAL | 0 | 10000 |  | 
Text Spline | SLA_SPLINE_TEXT | BOOL |  |  |  | 
Text | SLA_SPLINE_TEXT_TEXT | STRING |  |  |  | 
Font | SLA_SPLINE_TEXT_FONT | FONT |  |  |  | 
Align | SLA_SPLINE_TEXT_ALIGN | LONG |  |  |  | SLA_SPLINE_TEXT_ALIGN_LEFT; SLA_SPLINE_TEXT_ALIGN_MIDDLE; SLA_SPLINE_TEXT_ALIGN_RIGHT
Height | SLA_SPLINE_TEXT_HEIGHT | REAL |  |  |  | 
H Spacing | SLA_SPLINE_TEXT_HSPACING | REAL |  |  |  | 
V Spacing | SLA_SPLINE_TEXT_VSPACING | REAL |  |  |  | 
