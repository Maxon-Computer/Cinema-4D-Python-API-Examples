# Description: Cheen Shader

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/sla/description/xslacheen.res`
- **Symbol:** `XSLACheen`
- **Category:** Materials

Use parameter symbols to access parameters and cycle option symbols for cycle values, never their numeric IDs. Treat Min and Max as constraints and Default as the declared initial value; blank cells mean the resource does not declare that metadata, not that the value is zero. Base Description Parameters lists inherited fields from each base; All Parameters lists the effective parameter set for this description.

## Base Description Parameters

### No label (`Mpreview`)

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
No label | MATERIAL_PREVIEW | MATPREVIEW |  |  |  | 

### Material (`Mbase`)

No parameters.

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

### No label (`Millum`)

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Illumination | MATERIAL_PAGE_ILLUMINATION | BOOL |  |  |  | 
Polygon Light | MATERIAL_GLOBALILLUM_AREA | BOOL |  |  |  | 
Portal | MATERIAL_GLOBALILLUM_PORTAL | BOOL |  |  |  | 
GI Generate | MATERIAL_GLOBALILLUM_GENERATE | BOOL |  |  |  | 
GI Generate Strength | MATERIAL_GLOBALILLUM_GENERATE_STRENGTH | REAL | 0.0 | 10000.0 |  | 
GI Generate Saturation | MATERIAL_GLOBALILLUM_GENERATE_SATURATION | REAL | 0.0 | 1000.0 |  | 
GI Receive | MATERIAL_GLOBALILLUM_RECEIVE | BOOL |  |  |  | 
GI Receive Strength | MATERIAL_GLOBALILLUM_RECEIVE_STRENGTH | REAL | 0.0 | 10000.0 |  | 
GI Receive Saturation | MATERIAL_GLOBALILLUM_SATURATION | REAL | 0.0 | 1000.0 |  | 
Caustics Generate | MATERIAL_CAUSTICS_GENERATE | BOOL |  |  |  | 
Caustics Generate Strength | MATERIAL_CAUSTICS_GENERATE_STRENGTH | REAL | 0.0 | 10000.0 |  | 
Caustics Receive | MATERIAL_CAUSTICS_RECEIVE | BOOL |  |  |  | 
Caustics Receive Strength | MATERIAL_CAUSTICS_RECEIVE_STRENGTH | REAL | 0.0 | 10000.0 |  | 
Caustics Sample Radius | MATERIAL_CAUSTICS_SAMPLERADIUS | REAL | 0.0 |  |  | 
Caustics Samples | MATERIAL_CAUSTICS_SAMPLES | LONG | 1 | 10000 |  | 

### Assignment (`Massign`)

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Assignment | MATERIAL_PAGE_ASSIGNMENT | BOOL |  |  |  | 
No label | ID_MATERIALASSIGNMENTS | MATASSIGN |  |  |  | 

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
Gradients | SLA_CHEEN_GRADIENTS | BOOL |  |  |  | 
Diffuse | SLA_CHEEN_DIFFUSE | BOOL |  |  |  | 
Specular 1 | SLA_CHEEN_SPECULAR1 | BOOL |  |  |  | 
Specular 2 | SLA_CHEEN_SPECULAR2 | BOOL |  |  |  | 
Specular 3 | SLA_CHEEN_SPECULAR3 | BOOL |  |  |  | 
Transparency | SLA_CHEEN_TRANSPARENCY | BOOL |  |  |  | 
Reflection | SLA_CHEEN_REFLECTION | BOOL |  |  |  | 
Environment | SLA_CHEEN_ENVIRONMENT | BOOL |  |  |  | 
Ambient | SLA_CHEEN_AMBIENT | BOOL |  |  |  | 
Roughness | SLA_CHEEN_ROUGHNESS | BOOL |  |  |  | 
Anisotropy | SLA_CHEEN_ANISOTROPY | BOOL |  |  |  | 
Esoterica | SLA_CHEEN_ESOTERICA | BOOL |  |  |  | 
Color | SLA_CHEEN_GRADIENTS_COLOR | GRADIENT |  |  |  | 
Opacity | SLA_CHEEN_GRADIENTS_OPACITY | GRADIENT |  |  |  | 
Surface Color | SLA_CHEEN_DIFFUSE_SURF_COLOR | COLOR |  |  |  | 
Algorithm | SLA_CHEEN_DIFFUSE_ALGORITHM | LONG |  |  |  | SLA_CHEEN_DIFFUSE_ALGORITHM_INTERNAL; SLA_CHEEN_DIFFUSE_ALGORITHM_OREN_NAYAR
Roughness | SLA_CHEEN_DIFFUSE_ROUGHNESS | REAL | 0 | 200 |  | 
Surface Illumination | SLA_CHEEN_DIFFUSE_SURF_ILLUMINATION | REAL | -1000 | 1000 |  | 
Contrast | SLA_CHEEN_DIFFUSE_CONTRAST | REAL | -1000 | 1000 |  | 
Color | SLA_CHEEN_SPEC1_COLOR | COLOR |  |  |  | 
Intensity | SLA_CHEEN_SPEC1_INTENSITY | REAL | 0 | 1000 |  | 
Size | SLA_CHEEN_SPEC1_SIZE | REAL | 0 | 200 |  | 
Contrast | SLA_CHEEN_SPEC1_CONTRAST | REAL | 0 | 100 |  | 
Glare | SLA_CHEEN_SPEC1_GLARE | REAL | 0 | 1000 |  | 
Falloff | SLA_CHEEN_SPEC1_FALLOFF | REAL | 0 |  |  | 
Color | SLA_CHEEN_SPEC2_COLOR | COLOR |  |  |  | 
Intensity | SLA_CHEEN_SPEC2_INTENSITY | REAL | 0 | 1000 |  | 
Size | SLA_CHEEN_SPEC2_SIZE | REAL | 0 | 200 |  | 
Contrast | SLA_CHEEN_SPEC2_CONTRAST | REAL | 0 | 100 |  | 
Glare | SLA_CHEEN_SPEC2_GLARE | REAL | 0 | 1000 |  | 
Falloff | SLA_CHEEN_SPEC2_FALLOFF | REAL | 0 |  |  | 
Color | SLA_CHEEN_SPEC3_COLOR | COLOR |  |  |  | 
Intensity | SLA_CHEEN_SPEC3_INTENSITY | REAL | 0 | 1000 |  | 
Size | SLA_CHEEN_SPEC3_SIZE | REAL | 0 | 200 |  | 
Contrast | SLA_CHEEN_SPEC3_CONTRAST | REAL | 0 | 100 |  | 
Glare | SLA_CHEEN_SPEC3_GLARE | REAL | 0 | 1000 |  | 
Falloff | SLA_CHEEN_SPEC3_FALLOFF | REAL | 0 |  |  | 
Refraction Index | SLA_CHEEN_TRANS_REFRACTION_INDEX | REAL | 0.25 | 4.0 |  | 
Internal Refraction | SLA_CHEEN_TRANS_INTERNAL_REFLECTION | BOOL |  |  |  | 
Solid Object | SLA_CHEEN_TRANS_SOLID_OBJECT | BOOL |  |  |  | 
Intensity | SLA_CHEEN_REFLECTION_INTENSITY | REAL | 0 | 1000 |  | 
Edge Intensity | SLA_CHEEN_REFLECTION_EDGE_INTENSITY | REAL | 0 | 1000 |  | 
Falloff | SLA_CHEEN_REFLECTION_FALLOFF | REAL | 0 |  |  | 
Reflection Color | SLA_CHEEN_REFLECTION_REFLECTION_COLOR | COLOR |  |  |  | 
Reflection Edge Color | SLA_CHEEN_REFLECTION_EDGE_COLOR | COLOR |  |  |  | 
Image | SLA_CHEEN_ENVIRONMENT_IMAGE | SHADERLINK |  |  |  | 
Intensity | SLA_CHEEN_ENVIRONMENT_INTENSITY | REAL | 0 | 1000 |  | 
Glare | SLA_CHEEN_ENVIRONMENT_GLARE | REAL | 0 | 1000 |  | 
Falloff | SLA_CHEEN_ENVIRONMENT_FALLOFF | REAL | 0 |  |  | 
Utilize Anisotropic Scratches | SLA_CHEEN_ENVIRONMENT_UTILIZE_ANISO_SCRATCHES | BOOL |  |  |  | 
Blur | SLA_CHEEN_ENVIRONMENT_BLUR | REAL | 0 | 100 |  | 
Samples | SLA_CHEEN_ENVIRONMENT_SAMPLES | LONG | 1 |  |  | 
Jitter | SLA_CHEEN_ENVIRONMENT_JITTER | REAL | 0 | 1000 |  | 
Environment Color | SLA_CHEEN_ENVIRONMENT_ENVIRONMENT_COLOR | COLOR |  |  |  | 
Edge Color | SLA_CHEEN_ENVIRONMENT_EDGE_COLOR | COLOR |  |  |  | 
Color | SLA_CHEEN_AMBIENT_COLOR | COLOR |  |  |  | 
Intensity | SLA_CHEEN_AMBIENT_INTENSITY | REAL | 0 | 1000 |  | 
Edge Intensity | SLA_CHEEN_AMBIENT_EDGE_INTENSITY | REAL | 0 | 1000 |  | 
Falloff | SLA_CHEEN_AMBIENT_FALLOFF | REAL | 0 |  |  | 
Seed | SLA_CHEEN_ROUGHNESS_SEED | LONG |  |  |  | 
Function | SLA_CHEEN_ROUGHNESS_NOISE | LONG |  |  |  | 
Amplitude | SLA_CHEEN_ROUGHNESS_AMPLITUDE | REAL | -1000 | 1000 |  | 
Octaves | SLA_CHEEN_ROUGHNESS_OCTAVES | REAL | 0 | 20 |  | 
Scale | SLA_CHEEN_ROUGHNESS_SCALE | REAL | 0 |  |  | 
Speed | SLA_CHEEN_ROUGHNESS_SPEED | REAL | -100 | 100 |  | 
Attenuation | SLA_CHEEN_ROUGHNESS_ATTENUATION | REAL | 0 | 1000 |  | 
Delta | SLA_CHEEN_ROUGHNESS_DELTA | REAL | 0 |  |  | 
Hard Bump | SLA_CHEEN_ROUGHNESS_HARD_BUMP | BOOL |  |  |  | 
Absolute | SLA_CHEEN_ROUGHNESS_ABSOLUTE | BOOL |  |  |  | 
Low Clip | SLA_CHEEN_ROUGHNESS_LOW_CLIP | REAL | 0 | 100 |  | 
High Clip | SLA_CHEEN_ROUGHNESS_HIGH_CLIP | REAL | 0 | 100 |  | 
Grit Color | SLA_CHEEN_ROUGHNESS_GRIT_COLOR | COLOR |  |  |  | 
Grit Intensity | SLA_CHEEN_ROUGHNESS_GRIT_INTENSITY | REAL | -200 | 200 |  | 
Grit Low Clip | SLA_CHEEN_ROUGHNESS_GRIT_LOW_CLIP | REAL | 0 | 100 |  | 
Grit High Clip | SLA_CHEEN_ROUGHNESS_GRIT_HIGH_CLIP | REAL | 0 | 100 |  | 
Projection | SLA_CHEEN_ANISOTROPY_PROJECTION | LONG |  |  |  | SLA_CHEEN_ANISOTROPY_PROJECTION_PLANAR; SLA_CHEEN_ANISOTROPY_PROJECTION_AUTO_PLANAR; SLA_CHEEN_ANISOTROPY_PROJECTION_SHRINK_WRAP; SLA_CHEEN_ANISOTROPY_PROJECTION_RADIAL_AUTO_PLANAR; SLA_CHEEN_ANISOTROPY_PROJECTION_RAD_PATTERN_AUTO_PLANAR; SLA_CHEEN_ANISOTROPY_PROJECTION_RADIAL_PLANAR; SLA_CHEEN_ANISOTROPY_PROJECTION_RAD_PATTERN_PLANAR
Projection Scale | SLA_CHEEN_ANISOTROPY_PROJ_SCALE | REAL | 0 | 1000 |  | 
Roughness X | SLA_CHEEN_ANISOTROPY_X_ROUGH | REAL | 0 |  |  | 
Roughness Y | SLA_CHEEN_ANISOTROPY_Y_ROUGH | REAL | 0 |  |  | 
Amplitude | SLA_CHEEN_ANISOTROPY_AMPL | REAL | 0 | 100 |  | 
Scale | SLA_CHEEN_ANISOTROPY_SCALE | REAL | 0 |  |  | 
Length | SLA_CHEEN_ANISOTROPY_LENGTH | REAL | 0 |  |  | 
Attenuation | SLA_CHEEN_ANISOTROPY_ATT | REAL | 0 |  |  | 
Specular 1 | SLA_CHEEN_ANISOTROPY_CHANNEL1 | BOOL |  |  |  | 
Specular 2 | SLA_CHEEN_ANISOTROPY_CHANNEL2 | BOOL |  |  |  | 
Specular 3 | SLA_CHEEN_ANISOTROPY_CHANNEL3 | BOOL |  |  |  | 
Illumination | MATERIAL_PAGE_ILLUMINATION | BOOL |  |  |  | 
Polygon Light | MATERIAL_GLOBALILLUM_AREA | BOOL |  |  |  | 
Portal | MATERIAL_GLOBALILLUM_PORTAL | BOOL |  |  |  | 
GI Generate | MATERIAL_GLOBALILLUM_GENERATE | BOOL |  |  |  | 
GI Generate Strength | MATERIAL_GLOBALILLUM_GENERATE_STRENGTH | REAL | 0.0 | 10000.0 |  | 
GI Generate Saturation | MATERIAL_GLOBALILLUM_GENERATE_SATURATION | REAL | 0.0 | 1000.0 |  | 
GI Receive | MATERIAL_GLOBALILLUM_RECEIVE | BOOL |  |  |  | 
GI Receive Strength | MATERIAL_GLOBALILLUM_RECEIVE_STRENGTH | REAL | 0.0 | 10000.0 |  | 
GI Receive Saturation | MATERIAL_GLOBALILLUM_SATURATION | REAL | 0.0 | 1000.0 |  | 
Caustics Generate | MATERIAL_CAUSTICS_GENERATE | BOOL |  |  |  | 
Caustics Generate Strength | MATERIAL_CAUSTICS_GENERATE_STRENGTH | REAL | 0.0 | 10000.0 |  | 
Caustics Receive | MATERIAL_CAUSTICS_RECEIVE | BOOL |  |  |  | 
Caustics Receive Strength | MATERIAL_CAUSTICS_RECEIVE_STRENGTH | REAL | 0.0 | 10000.0 |  | 
Caustics Sample Radius | MATERIAL_CAUSTICS_SAMPLERADIUS | REAL | 0.0 |  |  | 
Caustics Samples | MATERIAL_CAUSTICS_SAMPLES | LONG | 1 | 10000 |  | 
Global Shadow Opacity | SLA_CHEEN_ESOTERICA_OPACITY | REAL | 0 | 100 |  | 
Assignment | MATERIAL_PAGE_ASSIGNMENT | BOOL |  |  |  | 
No label | ID_MATERIALASSIGNMENTS | MATASSIGN |  |  |  | 
