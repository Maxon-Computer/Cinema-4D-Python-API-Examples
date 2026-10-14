# Description: Thin Film Shader

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/shader/description/xthinfilm.res`
- **Symbol:** `Xthinfilm`
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
Color | THINFILMSHADER_LAYERCOLOR | COLOR |  |  |  | 
Texture | THINFILMSHADER_LAYERCOLOR_TEX_LINK | SHADERLINK |  |  |  | 
Mix Strength | THINFILMSHADER_LAYERMIXSTRENGTH | REAL | 0.0 | 100.0 |  | 
Thickness (nm) | THINFILMSHADER_AVERAGETHICKNESS | REAL | 0.0 | 5000.0 |  | 
Variation (nm) | THINFILMSHADER_RELATIVETHICKNESS | REAL | 0.0 | 5000.0 |  | 
Texture | THINFILMSHADER_RELATIVECHANGE_TEX_LINK | SHADERLINK |  |  |  | 
IOR Preset | THINFILMSHADER_IOR_PRESET | LONG |  |  |  | THINFILMSHADER_IOR_PRESET_CUSTOM; THINFILMSHADER_IOR_PRESET_BEER; THINFILMSHADER_IOR_PRESET_DIAMOND; THINFILMSHADER_IOR_PRESET_EMERALD; THINFILMSHADER_IOR_PRESET_ETHANOL; THINFILMSHADER_IOR_PRESET_GLASS; THINFILMSHADER_IOR_PRESET_JADE; THINFILMSHADER_IOR_PRESET_MILK; THINFILMSHADER_IOR_PRESET_OIL_VEGETABLE; THINFILMSHADER_IOR_PRESET_PEARL; THINFILMSHADER_IOR_PRESET_PET; THINFILMSHADER_IOR_PRESET_PLEXIGLASS; THINFILMSHADER_IOR_PRESET_RUBY; THINFILMSHADER_IOR_PRESET_SAPPHIRE; THINFILMSHADER_IOR_PRESET_WATER; THINFILMSHADER_IOR_PRESET_WATER_ICE; THINFILMSHADER_IOR_PRESET_WHISKEY
IOR | THINFILMSHADER_IOR | REAL | 1.0 | 10.0 |  | 
Spectral Samples | THINFILMSHADER_NUMSPECTRALSAMPLE | LONG | 1 | 100 |  | 
