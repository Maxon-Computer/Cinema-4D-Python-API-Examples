# Description: Subsurface Scattering Shader

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/c4d_base/description/xxmbsubsurface.res`
- **Symbol:** `Xxmbsubsurface`
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
Preset | XMBSUBSURFACESHADER_PRESET | LONG |  |  |  | XMBSUBSURFACESHADER_PRESET_CUSTOM; XMBSUBSURFACESHADER_PRESET_APPLE; XMBSUBSURFACESHADER_PRESET_CHICKEN; XMBSUBSURFACESHADER_PRESET_CREAM; XMBSUBSURFACESHADER_PRESET_KETCHUP; XMBSUBSURFACESHADER_PRESET_MARBLE; XMBSUBSURFACESHADER_PRESET_MILK_SKIM; XMBSUBSURFACESHADER_PRESET_MILK_WHOLE; XMBSUBSURFACESHADER_PRESET_POTATO; XMBSUBSURFACESHADER_PRESET_SKIN_DARK; XMBSUBSURFACESHADER_PRESET_SKIN_LIGHT; XMBSUBSURFACESHADER_PRESET_SPECTRALON
Color | XMBSUBSURFACESHADER_DIFFUSE | COLOR |  |  |  | 
Strength | XMBSUBSURFACESHADER_STRENGTH | REAL | 0.0 | 10000.0 |  | 
Shader | XMBSUBSURFACESHADER_SHADER | SHADERLINK |  |  |  | 
Path Length | XMBSUBSURFACESHADER_LENGTH | REAL | 0.001 | 100000.0 |  | 
Red | XMBSUBSURFACESHADER_LENGTH_R | REAL | 0.01 | 10000.0 |  | 
Green | XMBSUBSURFACESHADER_LENGTH_G | REAL | 0.01 | 10000.0 |  | 
Blue | XMBSUBSURFACESHADER_LENGTH_B | REAL | 0.01 | 10000.0 |  | 
Mode | XMBSUBSURFACESHADER_MULTIPLE_MODE | LONG |  |  |  | XMBSUBSURFACESHADER_MULTIPLE_MODE_CACHE; XMBSUBSURFACESHADER_MULTIPLE_MODE_DIRECT
Enabled | XMBSUBSURFACESHADER_MULTIPLE_ENABLED | BOOL |  |  |  | 
Fast Evaluation | XMBSUBSURFACESHADER_CACHE_INTERPOLATION | BOOL |  |  |  | 
Sample Density | XMBSUBSURFACESHADER_CACHE_SAMPLE_DENSITY | REAL | 10.0 | 1000.0 |  | 
Smoothing | XMBSUBSURFACESHADER_CACHE_SMOOTHING | REAL | 0.0 | 1000.0 |  | 
Threshold | XMBSUBSURFACESHADER_CACHE_ERROR | REAL | 0.01 | 1.0 |  | 
Separate Color Channels | XMBSUBSURFACESHADER_DIRECT_SPLIT | BOOL |  |  |  | 
Minimum Threshold | XMBSUBSURFACESHADER_DIRECT_RATIO | REAL | 0.0 | 1.0 |  | 
Custom Sampling | XMBSUBSURFACESHADER_MULTIPLE_CUSTOM_ENABLED | BOOL |  |  |  | 
Sampling Subdivision | XMBSUBSURFACESHADER_MULTIPLE_CUSTOM_SAMPLING | REAL | 0.0 | 16.0 |  | 
Enabled | XMBSUBSURFACESHADER_SINGLE_ENABLED | BOOL |  |  |  | 
Separate Color Channels | XMBSUBSURFACESHADER_SINGLE_SPLIT | BOOL |  |  |  | 
Trace Shadow Rays | XMBSUBSURFACESHADER_SINGLE_TRACE | BOOL |  |  |  | 
Phase Function | XMBSUBSURFACESHADER_SINGLE_PHASE | REAL | -1.0 | 1.0 |  | 
Custom Sampling | XMBSUBSURFACESHADER_SINGLE_CUSTOM_ENABLED | BOOL |  |  |  | 
Sampling Subdivision | XMBSUBSURFACESHADER_SINGLE_CUSTOM_SAMPLING | REAL | 0.0 | 16.0 |  | 
Fresnel Reflectivity | XMBSUBSURFACESHADER_FRESNEL | REAL | 0.0 | 100.0 |  | 
Dithering | XMBSUBSURFACESHADER_DITHER | REAL | 0.0 | 500.0 |  | 
Index of Refraction | XMBSUBSURFACESHADER_IOR | REAL | 1.0 | 2.0 |  | 
Compute GI Contribution | XMBSUBSURFACESHADER_LIGHTS_GI | BOOL |  |  |  | 
Use Lights | XMBSUBSURFACESHADER_LIGHTS_MODE | LONG |  |  |  | XMBSUBSURFACESHADER_LIGHTS_MODE_INCLUDE; XMBSUBSURFACESHADER_LIGHTS_MODE_EXCLUDE
Lights | XMBSUBSURFACESHADER_LIGHTS | IN_EXCLUDE |  |  |  | 
