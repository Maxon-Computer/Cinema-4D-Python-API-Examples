# Description: Hair

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/hair/description/xhair.res`
- **Symbol:** `Xhair`
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
Color | HAIR_SHADER_COLOR | GRADIENT |  |  |  | 
Diffuse | HAIR_SHADER_DIFFUSE_STRENGTH | REAL | 0.0 | 10000.0 |  | 
Texture | HAIR_SHADER_DIFFUSE_SHADER | SHADERLINK |  |  |  | 
Specular | HAIR_SHADER_SPECULAR_STRENGTH | REAL | 0.0 | 10000.0 |  | 
Sharpness | HAIR_SHADER_SPECULAR_POWER | REAL | 0.0 |  |  | 
Texture | HAIR_SHADER_SPECULAR_SHADER | SHADERLINK |  |  |  | 
Strength | HAIR_SHADER_ISPECULAR_STRENGTH | REAL | 0.0 | 10000.0 |  | 
Sharpness | HAIR_SHADER_ISPECULAR_POWER | REAL | 0.0 |  |  | 
Texture | HAIR_SHADER_ISPECULAR_SHADER | SHADERLINK |  |  |  | 
Roughness | HAIR_SHADER_ROUGHNESS | REAL | 0.0 | 100.0 |  | 
Variation | HAIR_SHADER_ROUGHNESS_VAR | REAL | 0.0 | 100.0 |  | 
Reflectiveness | HAIR_SHADER_REFLECT | REAL | 0.0 | 100.0 |  | 
Translucence | HAIR_SHADER_TRANSMIT | REAL | 0.0 | 100.0 |  | 
Shadow | HAIR_SHADER_SHADOW | REAL | 0.0 | 100.0 |  | 
Alpha Depth | HAIR_SHADER_ALPHA_DEPTH | LONG | 1 |  |  | 
Shadow Transparency | HAIR_SHADER_SHADOW_TRANSPARENCY | REAL | 0.0 | 100.0 |  | 
From Hair Materials | HAIR_SHADER_FROM_MATERIAL | BOOL |  |  |  | 
