# Description: Terrain Mask

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/shader/description/xterrainmask.res`
- **Symbol:** `xTerrainmask`
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
Gradient | XTMASK_GRADIENT | GRADIENT |  |  |  | 
Enable Altitude Masking | XTMASK_ALTITUDE_ENABLE | BOOL |  |  |  | 
Min Altitude | XTMASK_ALTITUDE_MIN | REAL |  |  |  | 
Max Altitude | XTMASK_ALTITUDE_MAX | REAL |  |  |  | 
Soften Min | XTMASK_ALTITUDE_SOFTEN_MIN | REAL | 0.0 | 100.0 |  | 
Soften Max | XTMASK_ALTITUDE_SOFTEN_MAX | REAL | 0.0 | 100.0 |  | 
Noise Height | XTMASK_ALTITUDE_NOISE_HEIGHT | REAL |  |  |  | 
Scale | XTMASK_ALTITUDE_NOISE_SCALE | REAL |  |  |  | 
Enable Slope Masking | XTMASK_SLOPE_ENABLE | BOOL |  |  |  | 
Min Slope | XTMASK_SLOPE_MIN | REAL | 0.0 | 179.0 |  | 
Max Slope | XTMASK_SLOPE_MAX | REAL | 1.0 | 180.0 |  | 
Soften Min | XTMASK_SLOPE_SOFTEN_MIN | REAL | 0.0 | 100.0 |  | 
Soften Max | XTMASK_SLOPE_SOFTEN_MAX | REAL | 0.0 | 100.0 |  | 
Use Bump | XTMASK_SLOPE_USEBUMP | BOOL |  |  |  | 
Direction | XTMASK_SLOPE_DIRECTION | LONG |  |  |  | XTMASK_DIRECTION_X2; XTMASK_DIRECTION_X; XTMASK_DIRECTION_Y2; XTMASK_DIRECTION_Y; XTMASK_DIRECTION_Z2; XTMASK_DIRECTION_Z; XTMASK_DIRECTION_CUSTOM
Custom Direction | XTMASK_SLOPE_DIRECTION_CUSTOM | VECTOR |  |  |  | 
Alternative Blending | XTMASK_SLOPE_ALTERNATIVEBLENDING | BOOL |  |  |  | 
Hardness | XTMASK_SLOPE_ALTERNATIVEBLENDING_HARDNESS | REAL | 0.0 | 100.0 |  | 
Use Global Coordinates | XTMASK_GLOBAL | BOOL |  |  |  | 
Invert | XTMASK_INVERT | BOOL |  |  |  | 
