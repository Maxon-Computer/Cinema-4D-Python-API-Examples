# Description: Banzi Shader

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/sla/description/xslabanzi.res`
- **Symbol:** `XSLABanzi`
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
Wood | SLA_BANZI_WOOD | BOOL |  |  |  | 
Diffuse | SLA_BANZI_DIFFUSE | BOOL |  |  |  | 
Specular 1 | SLA_BANZI_SPECULAR1 | BOOL |  |  |  | 
Specular 2 | SLA_BANZI_SPECULAR2 | BOOL |  |  |  | 
Specular 3 | SLA_BANZI_SPECULAR3 | BOOL |  |  |  | 
Reflection | SLA_BANZI_REFLECTION | BOOL |  |  |  | 
Environment | SLA_BANZI_ENVIRONMENT | BOOL |  |  |  | 
Ambient | SLA_BANZI_AMBIENT | BOOL |  |  |  | 
Roughness | SLA_BANZI_ROUGHNESS | BOOL |  |  |  | 
Anisotropy | SLA_BANZI_ANISOTROPY | BOOL |  |  |  | 
Color | SLA_BANZI_WOOD_GRADIENT | GRADIENT |  |  |  | 
Ring intensity | SLA_BANZI_WOOD_RING_INTENSITY | REAL |  |  |  | 
Ring Scale | SLA_BANZI_WOOD_RING_SCALE | REAL | 0 |  |  | 
Ring Turbulence | SLA_BANZI_WOOD_RING_TURBULENCE | REAL | 0 |  |  | 
Turbulence Scale | SLA_BANZI_WOOD_TURBULENCE_SCALE | REAL | 0 |  |  | 
Ring Variance | SLA_BANZI_WOOD_RING_VARIANCE | REAL | 0 |  |  | 
Core Variance | SLA_BANZI_WOOD_CORE_VARIANCE | REAL | 0 |  |  | 
Variance Scale | SLA_BANZI_WOOD_VARIANCE_SCALE | REAL | 0 |  |  | 
Radial Variance | SLA_BANZI_WOOD_RADIAL_VARIANCE | REAL | 0 |  |  | 
Variance Scale | SLA_BANZI_WOOD_RADIAL_VARIANCE_SCALE | REAL | 0 |  |  | 
Grain Intensity | SLA_BANZI_WOOD_GRAIN_INTENSITY | REAL |  |  |  | 
Grain Scale | SLA_BANZI_WOOD_GRAIN_SCALE | REAL | 0 |  |  | 
Attenuation | SLA_BANZI_WOOD_ATTENUATION | REAL | 0 |  |  | 
Surface Color | SLA_BANZI_DIFFUSE_SURF_COLOR | COLOR |  |  |  | 
Algorithm | SLA_BANZI_DIFFUSE_ALGORITHM | LONG |  |  |  | SLA_BANZI_DIFFUSE_ALGORITHM_INTERNAL; SLA_BANZI_DIFFUSE_ALGORITHM_OREN_NAYAR
Roughness | SLA_BANZI_DIFFUSE_ROUGHNESS | REAL | 0 | 200 |  | 
Surface Illumination | SLA_BANZI_DIFFUSE_SURF_ILLUMINATION | REAL | 0 | 1000 |  | 
Contrast | SLA_BANZI_DIFFUSE_CONTRAST | REAL | -1000 | 1000 |  | 
Color | SLA_BANZI_SPEC1_COLOR | COLOR |  |  |  | 
Intensity | SLA_BANZI_SPEC1_INTENSITY | REAL | 0 | 1000 |  | 
Size | SLA_BANZI_SPEC1_SIZE | REAL | 0 | 200 |  | 
Contrast | SLA_BANZI_SPEC1_CONTRAST | REAL | 0 | 100 |  | 
Glare | SLA_BANZI_SPEC1_GLARE | REAL | 0 | 1000 |  | 
Falloff | SLA_BANZI_SPEC1_FALLOFF | REAL | 0 |  |  | 
Color | SLA_BANZI_SPEC2_COLOR | COLOR |  |  |  | 
Intensity | SLA_BANZI_SPEC2_INTENSITY | REAL | 0 | 1000 |  | 
Size | SLA_BANZI_SPEC2_SIZE | REAL | 0 | 200 |  | 
Contrast | SLA_BANZI_SPEC2_CONTRAST | REAL | 0 | 100 |  | 
Glare | SLA_BANZI_SPEC2_GLARE | REAL | 0 | 1000 |  | 
Falloff | SLA_BANZI_SPEC2_FALLOFF | REAL | 0 |  |  | 
Color | SLA_BANZI_SPEC3_COLOR | COLOR |  |  |  | 
Intensity | SLA_BANZI_SPEC3_INTENSITY | REAL | 0 | 1000 |  | 
Size | SLA_BANZI_SPEC3_SIZE | REAL | 0 | 200 |  | 
Contrast | SLA_BANZI_SPEC3_CONTRAST | REAL | 0 | 100 |  | 
Glare | SLA_BANZI_SPEC3_GLARE | REAL | 0 | 1000 |  | 
Falloff | SLA_BANZI_SPEC3_FALLOFF | REAL | 0 |  |  | 
Intensity | SLA_BANZI_REFLECTION_INTENSITY | REAL | 0 | 1000 |  | 
Edge Intensity | SLA_BANZI_REFLECTION_EDGE_INTENSITY | REAL | 0 | 1000 |  | 
Falloff | SLA_BANZI_REFLECTION_FALLOFF | REAL | 0 |  |  | 
Reflection Color | SLA_BANZI_REFLECTION_REFLECTION_COLOR | COLOR |  |  |  | 
Reflection Edge Color | SLA_BANZI_REFLECTION_EDGE_COLOR | COLOR |  |  |  | 
Image | SLA_BANZI_ENVIRONMENT_IMAGE | SHADERLINK |  |  |  | 
Intensity | SLA_BANZI_ENVIRONMENT_INTENSITY | REAL | 0 | 1000 |  | 
Glare | SLA_BANZI_ENVIRONMENT_GLARE | REAL | 0 | 1000 |  | 
Falloff | SLA_BANZI_ENVIRONMENT_FALLOFF | REAL | 0 |  |  | 
Utilize Anisotropic Scratches | SLA_BANZI_ENVIRONMENT_UTILIZE_ANISO_SCRATCHES | BOOL |  |  |  | 
Blur | SLA_BANZI_ENVIRONMENT_BLUR | REAL | 0 | 100 |  | 
Samples | SLA_BANZI_ENVIRONMENT_SAMPLES | LONG | 1 |  |  | 
Jitter | SLA_BANZI_ENVIRONMENT_JITTER | REAL | 0 | 1000 |  | 
Environment Color | SLA_BANZI_ENVIRONMENT_ENVIRONMENT_COLOR | COLOR |  |  |  | 
Edge Color | SLA_BANZI_ENVIRONMENT_EDGE_COLOR | COLOR |  |  |  | 
Color | SLA_BANZI_AMBIENT_COLOR | COLOR |  |  |  | 
Intensity | SLA_BANZI_AMBIENT_INTENSITY | REAL | 0 | 1000 |  | 
Edge Intensity | SLA_BANZI_AMBIENT_EDGE_INTENSITY | REAL | 0 | 1000 |  | 
Falloff | SLA_BANZI_AMBIENT_FALLOFF | REAL | 0 |  |  | 
Amplitude | SLA_BANZI_ROUGHNESS_AMPLITUDE | REAL | -1000 | 1000 |  | 
Delta | SLA_BANZI_ROUGHNESS_DELTA | REAL | 0 |  |  | 
Low Clip | SLA_BANZI_ROUGHNESS_LOW_CLIP | REAL | 0 | 100 |  | 
High Clip | SLA_BANZI_ROUGHNESS_HIGH_CLIP | REAL | 0 | 100 |  | 
Grit Color | SLA_BANZI_ROUGHNESS_GRIT_COLOR | COLOR |  |  |  | 
Grit Intensity | SLA_BANZI_ROUGHNESS_GRIT_INTENSITY | REAL | -200 | 200 |  | 
Grit Low Clip | SLA_BANZI_ROUGHNESS_GRIT_LOW_CLIP | REAL | 0 | 100 |  | 
Grit High Clip | SLA_BANZI_ROUGHNESS_GRIT_HIGH_CLIP | REAL | 0 | 100 |  | 
Projection | SLA_BANZI_ANISOTROPY_PROJECTION | LONG |  |  |  | SLA_BANZI_ANISOTROPY_PROJECTION_PLANAR; SLA_BANZI_ANISOTROPY_PROJECTION_AUTO_PLANAR; SLA_BANZI_ANISOTROPY_PROJECTION_SHRINK_WRAP; SLA_BANZI_ANISOTROPY_PROJECTION_RADIAL_AUTO_PLANAR; SLA_BANZI_ANISOTROPY_PROJECTION_RAD_PATTERN_AUTO_PLANAR; SLA_BANZI_ANISOTROPY_PROJECTION_RADIAL_PLANAR; SLA_BANZI_ANISOTROPY_PROJECTION_RAD_PATTERN_PLANAR
Projection Scale | SLA_BANZI_ANISOTROPY_PROJ_SCALE | REAL | 0 | 1000 |  | 
Roughness X | SLA_BANZI_ANISOTROPY_X_ROUGH | REAL | 0 |  |  | 
Roughness Y | SLA_BANZI_ANISOTROPY_Y_ROUGH | REAL | 0 |  |  | 
Amplitude | SLA_BANZI_ANISOTROPY_AMPL | REAL | 0 | 100 |  | 
Scale | SLA_BANZI_ANISOTROPY_SCALE | REAL | 0 |  |  | 
Length | SLA_BANZI_ANISOTROPY_LENGTH | REAL | 0 |  |  | 
Attenuation | SLA_BANZI_ANISOTROPY_ATT | REAL | 0 |  |  | 
Specular 1 | SLA_BANZI_ANISOTROPY_CHANNEL1 | BOOL |  |  |  | 
Specular 2 | SLA_BANZI_ANISOTROPY_CHANNEL2 | BOOL |  |  |  | 
Specular 3 | SLA_BANZI_ANISOTROPY_CHANNEL3 | BOOL |  |  |  | 
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
Assignment | MATERIAL_PAGE_ASSIGNMENT | BOOL |  |  |  | 
No label | ID_MATERIALASSIGNMENTS | MATASSIGN |  |  |  | 
