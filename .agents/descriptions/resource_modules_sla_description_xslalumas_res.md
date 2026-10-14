# Description: Lumas Shader

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/sla/description/xslalumas.res`
- **Symbol:** `XSLALumas`
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
Active | SLA_LUMAS_DIFFUSE_ACTIVE | BOOL |  |  |  | 
Color | SLA_LUMAS_DIFFUSE_COLOR | COLOR |  |  |  | 
Algorithm | SLA_LUMAS_DIFFUSE_ALGORITHM | LONG |  |  |  | SLA_LUMAS_DIFFUSE_ALGO_INTERNAL; SLA_LUMAS_DIFFUSE_ALGO_ORENNAYAR
Roughness | SLA_LUMAS_DIFFUSE_ROUGHNESS | REAL | 0 | 200 |  | 
Illumination | SLA_LUMAS_DIFFUSE_ILLUMINATION | REAL | 0 | 1000 |  | 
Contrast | SLA_LUMAS_DIFFUSE_CONTRAST | REAL | -1000 | 1000 |  | 
Active | SLA_LUMAS_SPECULAR1_ACTIVE | BOOL |  |  |  | 
Color | SLA_LUMAS_SPECULAR1_COLOR | COLOR |  |  |  | 
Intensity | SLA_LUMAS_SPECULAR1_INTENSITY | REAL | 0 | 1000 |  | 
Size | SLA_LUMAS_SPECULAR1_SIZE | REAL | 0 | 200 |  | 
Contrast | SLA_LUMAS_SPECULAR1_CONTRAST | REAL | 0 | 100 |  | 
Glare | SLA_LUMAS_SPECULAR1_GLARE | REAL | 0 | 1000 |  | 
Falloff | SLA_LUMAS_SPECULAR1_FALLOFF | REAL | 0 |  |  | 
Active | SLA_LUMAS_SPECULAR2_ACTIVE | BOOL |  |  |  | 
Color | SLA_LUMAS_SPECULAR2_COLOR | COLOR |  |  |  | 
Intensity | SLA_LUMAS_SPECULAR2_INTENSITY | REAL | 0 | 1000 |  | 
Size | SLA_LUMAS_SPECULAR2_SIZE | REAL | 0 | 200 |  | 
Contrast | SLA_LUMAS_SPECULAR2_CONTRAST | REAL | 0 | 100 |  | 
Glare | SLA_LUMAS_SPECULAR2_GLARE | REAL | 0 | 1000 |  | 
Falloff | SLA_LUMAS_SPECULAR2_FALLOFF | REAL | 0 |  |  | 
Active | SLA_LUMAS_SPECULAR3_ACTIVE | BOOL |  |  |  | 
Color | SLA_LUMAS_SPECULAR3_COLOR | COLOR |  |  |  | 
Intensity | SLA_LUMAS_SPECULAR3_INTENSITY | REAL | 0 | 1000 |  | 
Size | SLA_LUMAS_SPECULAR3_SIZE | REAL | 0.01 | 200 |  | 
Contrast | SLA_LUMAS_SPECULAR3_CONTRAST | REAL | 0 | 100 |  | 
Glare | SLA_LUMAS_SPECULAR3_GLARE | REAL | 0 | 1000 |  | 
Falloff | SLA_LUMAS_SPECULAR3_FALLOFF | REAL | 0 |  |  | 
Active | SLA_LUMAS_ANISO_ACTIVE | BOOL |  |  |  | 
Projection | SLA_LUMAS_ANISO_PROJECTION | LONG |  |  |  | SLA_LUMAS_ANISO_PROJECTION_PLANAR; SLA_LUMAS_ANISO_PROJECTION_AUTO_PLANAR; SLA_LUMAS_ANISO_PROJECTION_SHRINK_WRAP; SLA_LUMAS_ANISO_PROJECTION_RAD_AUTO_PLANAR; SLA_LUMAS_ANISO_PROJECTION_RAD_PAT_AUTO_PLANAR; SLA_LUMAS_ANISO_PROJECTION_RAD_PLANAR; SLA_LUMAS_ANISO_PROJECTION_RAD_PATTERN_PLANAR
Projection Scale | SLA_LUMAS_ANISO_PROJ_SCALE | REAL | 0 | 1000 |  | 
X Roughness | SLA_LUMAS_ANISO_X_ROUGH | REAL | 0 |  |  | 
Y Roughness | SLA_LUMAS_ANISO_Y_ROUGH | REAL | 0 |  |  | 
Specular 1 | SLA_LUMAS_ANISO_SPEC_CHANNEL_SPEC1 | BOOL |  |  |  | 
Specular 2 | SLA_LUMAS_ANISO_SPEC_CHANNEL_SPEC2 | BOOL |  |  |  | 
Specular 3 | SLA_LUMAS_ANISO_SPEC_CHANNEL_SPEC3 | BOOL |  |  |  | 
Amplitude | SLA_LUMAS_ANISO_AMPLITUDE | REAL | 0 | 100 |  | 
Scale | SLA_LUMAS_ANISO_SCALE | REAL | 0 |  |  | 
Length | SLA_LUMAS_ANISO_LENGTH | REAL | 0 |  |  | 
Attenuation | SLA_LUMAS_ANISO_ATTENUATION | REAL | 0 |  |  | 
Specular 1 | SLA_LUMAS_ANISO_SCRATCH_CHANNEL_SPEC1 | BOOL |  |  |  | 
Specular 2 | SLA_LUMAS_ANISO_SCRATCH_CHANNEL_SPEC2 | BOOL |  |  |  | 
Specular 3 | SLA_LUMAS_ANISO_SCRATCH_CHANNEL_SPEC3 | BOOL |  |  |  | 
