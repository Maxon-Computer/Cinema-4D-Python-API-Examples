# Description: Noise Shader

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/sla/description/xslanoise.res`
- **Symbol:** `XSLANoise`
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
Color 1 | SLA_NOISE_COLOR1 | COLOR |  |  |  | 
Color 2 | SLA_NOISE_COLOR2 | COLOR |  |  |  | 
Seed | SLA_NOISE_SEED | LONG |  |  |  | 
Noise | SLA_NOISE_NOISE | LONG |  |  |  | 
Octaves | SLA_NOISE_OCTAVES | REAL | 0 | 20 |  | 
Space | SLA_NOISE_SPACE | LONG |  |  |  | SLA_NOISE_SPACE_UV; SLA_NOISE_SPACE_TEXTURE; SLA_NOISE_SPACE_OBJECT; SLA_NOISE_SPACE_WORLD; SLA_NOISE_SPACE_CAMERA; SLA_NOISE_SPACE_SCREEN; SLA_NOISE_SPACE_RASTER
Global Scale | SLA_NOISE_GLOBAL_SCALE | REAL | 0 |  |  | 
Relative Scale | SLA_NOISE_SCALE | VECTOR | 0 |  |  | 
Animation Speed | SLA_NOISE_ANI_SPEED | REAL | 0 |  |  | 
Loop Period | SLA_NOISE_TIMEPERIOD | REAL | 0 |  |  | 
Detail Attenuation | SLA_NOISE_DETAIL_ATT | REAL | 0 |  |  | 
Delta | SLA_NOISE_DELTA | REAL |  |  |  | 
Movement | SLA_NOISE_MOVEMENT | VECTOR |  |  |  | 
Speed | SLA_NOISE_SPEED | REAL |  |  |  | 
Absolute | SLA_NOISE_ABSOLUTE | BOOL |  |  |  | 
Cycles | SLA_NOISE_CYCLES | REAL | 0 |  |  | 
Low Clip | SLA_NOISE_LOW_CLIP | REAL | 0 | 100 |  | 
High Clip | SLA_NOISE_HIGH_CLIP | REAL | 0 | 100 |  | 
Brightness | SLA_NOISE_BRIGHTNESS | REAL | -100 | 100 |  | 
Contrast | SLA_NOISE_CONTRAST | REAL | -100 | 100 |  | 
Use as Environment | SLA_NOISE_USE_AS_ENV | BOOL |  |  |  | 
Project Environment | SLA_NOISE_PROJECT_ENV | BOOL |  |  |  | 
Compatibility | SLA_NOISE_COMPATIBILITY | BOOL |  |  |  | 
