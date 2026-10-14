# Description: Hatch Shader

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/sketch/description/xhatchingshader.res`
- **Symbol:** `Xhatchingshader`
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
Texture | HATCHINGSHADER_TEXTURE | SHADERLINK |  |  |  | 
Tile UV | HATCHINGSHADER_TILE | BOOL |  |  |  | 
Rotational UV | HATCHINGSHADER_ROTATIONAL | BOOL |  |  |  | 
Scale | HATCHINGSHADER_SCALE | REAL | 0.0 |  |  | 
Rotate UV | HATCHINGSHADER_ROTATE | REAL | -360.0 | 360.0 |  | 
Offset U | HATCHINGSHADER_OFFSET_U | REAL |  |  |  | 
Offset V | HATCHINGSHADER_OFFSET_V | REAL |  |  |  | 
Density | HATCHINGSHADER_DENSITY | REAL | 0.0 | 10000.0 |  | 
Density U | HATCHINGSHADER_DENSITY_U | REAL | 0.0 | 100.0 |  | 
Density V | HATCHINGSHADER_DENSITY_V | REAL | 0.0 | 100.0 |  | 
Scatter U | HATCHINGSHADER_SCATTER_U | REAL | 0.0 |  |  | 
Scatter V | HATCHINGSHADER_SCATTER_V | REAL | 0.0 |  |  | 
Spacing U | HATCHINGSHADER_SPACE_U | REAL | -100.0 |  |  | 
Variation | HATCHINGSHADER_SPACE_U_VAR | REAL | 0.0 |  |  | 
Spacing V | HATCHINGSHADER_SPACE_V | REAL | -100.0 |  |  | 
Variation | HATCHINGSHADER_SPACE_V_VAR | REAL | 0.0 |  |  | 
Scale U | HATCHINGSHADER_SCALE_U | REAL | 0.0 |  |  | 
Variation | HATCHINGSHADER_SCALE_U_VAR | REAL | 0.0 |  |  | 
Scale V | HATCHINGSHADER_SCALE_V | REAL | 0.0 |  |  | 
Variation | HATCHINGSHADER_SCALE_V_VAR | REAL | 0.0 |  |  | 
Rotate | HATCHINGSHADER_STOKE_ROTATE | REAL | 0.0 | 360.0 |  | 
Crosses | HATCHINGSHADER_CROSSED | BOOL |  |  |  | 
Cross Rotation | HATCHINGSHADER_CROSS_ROTATE | REAL | -360.0 | 360.0 |  | 
Dark Stroke Color | HATCHINGSHADER_STROKE_COLOR | COLOR |  |  |  | 
Light Stroke Color | HATCHINGSHADER_STROKELIGHT_COLOR | COLOR |  |  |  | 
Background Color | HATCHINGSHADER_BACK_COLOR | COLOR |  |  |  | 
Show Dark Strokes | HATCHINGSHADER_DARK_STROKES | BOOL |  |  |  | 
Show Light Strokes | HATCHINGSHADER_LIGHT_STROKES | BOOL |  |  |  | 
Shade Levels | HATCHINGSHADER_LEVELS | LONG | 1 | 20 |  | 
Threshold | HATCHINGSHADER_THRESHOLD | REAL | 0.0 | 100.0 |  | 
Shadows | HATCHINGSHADER_SHADOW | GRADIENT |  |  |  | 
Diffuse | HATCHINGSHADER_DIFFUSE | GRADIENT |  |  |  | 
Specular | HATCHINGSHADER_SPEC | GRADIENT |  |  |  | 
Illumination | HATCHINGSHADER_ILLUM | GRADIENT |  |  |  | 
Use Bump | HATCHINGSHADER_BUMP | BOOL |  |  |  | 
Camera | HATCHINGSHADER_CAMERA | BOOL |  |  |  | 
Lights | HATCHINGSHADER_LIGHTS | BOOL |  |  |  | 
Specular | HATCHINGSHADER_SPECULAR | BOOL |  |  |  | 
Illumination | HATCHINGSHADER_ILLUMINATION | BOOL |  |  |  | 
Shadow | HATCHINGSHADER_SHADOWS | BOOL |  |  |  | 
Modifies Contrast | HATCHINGSHADER_CONTRAST | BOOL |  |  |  | 
Use Lights | HATCHINGSHADER_INCEXC | LONG |  |  |  | HATCHINGSHADER_INCEXC_INCLUDE; HATCHINGSHADER_INCEXC_EXCLUDE
Lights | HATCHINGSHADER_INCEXC_LIGHTS | IN_EXCLUDE |  |  |  | 
