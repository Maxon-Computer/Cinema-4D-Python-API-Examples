# Description: Spots Shader

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/sketch/description/xspotshader.res`
- **Symbol:** `Xspotshader`
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
Shape | SPOTSHADER_GAP_SHAPE | LONG |  |  | 1 | SPOTSHADER_GAP_SHAPE_CIRCLE; SPOTSHADER_GAP_SHAPE_DIAMOND; SPOTSHADER_GAP_SHAPE_CHECKER; SPOTSHADER_GAP_SHAPE_SQUARE; SPOTSHADER_GAP_SHAPE_ULINES; SPOTSHADER_GAP_SHAPE_VLINES; SPOTSHADER_GAP_SHAPE_GRID; SPOTSHADER_GAP_SHAPE_TEXTURE
Texture | SPOTSHADER_GAP_TEXTURE | SHADERLINK |  |  |  | 
Gap Color | SPOTSHADER_GAP_COLOR | COLOR |  |  |  | 
Spot Color | SPOTSHADER_CIRCLE_COLOR | COLOR |  |  |  | 
Scale | SPOTSHADER_SCALE | REAL | 0.0 |  |  | 
U | SPOTSHADER_SCALE_U | REAL | 0.0 |  |  | 
V | SPOTSHADER_SCALE_V | REAL | 0.0 |  |  | 
Rotate | SPOTSHADER_ROTATE | REAL | 0.0 | 360.0 |  | 
Shadow | SPOTSHADER_SHADOW | GRADIENT |  |  |  | 
Diffuse | SPOTSHADER_DIFFUSE | GRADIENT |  |  |  | 
Specular | SPOTSHADER_SPEC | GRADIENT |  |  |  | 
Illumination | SPOTSHADER_ILLUM | GRADIENT |  |  |  | 
Camera | SPOTSHADER_CAMERA | BOOL |  |  |  | 
Lights | SPOTSHADER_LIGHTS | BOOL |  |  |  | 
Specular | SPOTSHADER_SPECULAR | BOOL |  |  |  | 
Illumination | SPOTSHADER_ILLUMINATION | BOOL |  |  |  | 
Shadows | SPOTSHADER_SHADOWS | BOOL |  |  |  | 
Invert | SPOTSHADER_INVERT | BOOL |  |  |  | 
Use Lights | SPOTSHADER_INCEXC | LONG |  |  |  | SPOTSHADER_INCEXC_INCLUDE; SPOTSHADER_INCEXC_EXCLUDE
Lights | SPOTSHADER_INCEXC_LIGHTS | IN_EXCLUDE |  |  |  | 
