# Description: Filter Shader

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/sla/description/xslafilter.res`
- **Symbol:** `XSLAFilter`
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
Texture | SLA_FILTER_TEXTURE | SHADERLINK |  |  |  | 
Hue | SLA_FILTER_HUE | REAL | 0 | 360 |  | 
Saturation | SLA_FILTER_SATURATION | REAL | -100 | 100 |  | 
Lightness | SLA_FILTER_LIGHTNESS | REAL | -100 | 100 |  | 
Colorize | SLA_FILTER_COLORIZE | BOOL |  |  |  | 
Brightness | SLA_FILTER_BRIGHNESS | REAL | -100 | 100 |  | 
Contrast | SLA_FILTER_CONTRAST | REAL | -100 | 100 |  | 
Gamma | SLA_FILTER_GAMMA | REAL | .1 | 100 |  | 
Enable Clipping | SLA_FILTER_CLIPPING | BOOL |  |  |  | 
Low Clip | SLA_FILTER_LOW_CLIP | REAL | 0 | 10000 |  | 
High Clip | SLA_FILTER_HIGH_CLIP | REAL | 0 | 10000 |  | 
Enabled | SLA_FILTER_GRADING_ENABLED | BOOL |  |  |  | 
Intensity | SLA_FILTER_GRADING_INTENSITY | REAL | 0.0 | 100.0 |  | 
RGB | SLA_FILTER_GRADING_CURVE_RGB | SPLINE |  |  |  | 
R | SLA_FILTER_GRADING_CURVE_R | SPLINE |  |  |  | 
G | SLA_FILTER_GRADING_CURVE_G | SPLINE |  |  |  | 
B | SLA_FILTER_GRADING_CURVE_B | SPLINE |  |  |  | 
