# Description: Mabel Shader

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/sla/description/xslamabel.res`
- **Symbol:** `XSLAMabel`
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
Surface | SLA_MABEL_SURFACE | LONG |  |  |  | SLA_MABEL_SURFACE_1; SLA_MABEL_SURFACE_2; SLA_MABEL_SURFACE_BOTH
Veining | SLA_MABEL_VEINING | BOOL |  |  |  | 
Diffuse A | SLA_MABEL_DIFFUSE_A | BOOL |  |  |  | 
Specular 1 A | SLA_MABEL_SPECULAR1_A | BOOL |  |  |  | 
Specular 2 A | SLA_MABEL_SPECULAR2_A | BOOL |  |  |  | 
Specular 3 A | SLA_MABEL_SPECULAR3_A | BOOL |  |  |  | 
Reflection A | SLA_MABEL_REFLECTION_A | BOOL |  |  |  | 
Environment A | SLA_MABEL_ENVIRONMENT_A | BOOL |  |  |  | 
Ambient A | SLA_MABEL_AMBIENT_A | BOOL |  |  |  | 
Roughness A | SLA_MABEL_ROUGHNESS_A | BOOL |  |  |  | 
Anisotropy A | SLA_MABEL_ANISOTROPY_A | BOOL |  |  |  | 
Diffuse B | SLA_MABEL_DIFFUSE_B | BOOL |  |  |  | 
Specular 1 B | SLA_MABEL_SPECULAR1_B | BOOL |  |  |  | 
Specular 2 B | SLA_MABEL_SPECULAR2_B | BOOL |  |  |  | 
Specular 3 B | SLA_MABEL_SPECULAR3_B | BOOL |  |  |  | 
Reflection B | SLA_MABEL_REFLECTION_B | BOOL |  |  |  | 
Environment B | SLA_MABEL_ENVIRONMENT_B | BOOL |  |  |  | 
Ambient B | SLA_MABEL_AMBIENT_B | BOOL |  |  |  | 
Roughness B | SLA_MABEL_ROUGHNESS_B | BOOL |  |  |  | 
Anisotropy B | SLA_MABEL_ANISOTROPY_B | BOOL |  |  |  | 
Seed | SLA_MABEL_SEED | LONG |  |  |  | 
Veining Turbulence | SLA_MABEL_VEINING_TURBULENCE | LONG |  |  |  | 
Veining Stirring | SLA_MABEL_VEINING_STIRRING | REAL | 0 |  |  | 
Veining Scale | SLA_MABEL_VEINING_SCALE | REAL | 0 | 100 |  | 
Veining Octaves | SLA_MABEL_VEINING_OCTAVES | REAL | 0 | 20 |  | 
Veining Size | SLA_MABEL_VEINING_SIZE | REAL | 0 | 100 |  | 
Veining Contrast | SLA_MABEL_VEINING_CONTRAST | REAL | -100 | 100 |  | 
Variance Turbulence | SLA_MABEL_VARIANCE_TURBULENCE | LONG |  |  |  | 
Variance Amplitude | SLA_MABEL_VARIANCE_AMPLITUDE | REAL | 0 |  |  | 
Variance Octaves | SLA_MABEL_VARIANCE_OCTAVES | REAL | 0 | 20 |  | 
Variance Scale | SLA_MABEL_VARIANCE_SCALE | REAL | 0 | 100 |  | 
Variance Contrast | SLA_MABEL_VARIANCE_CONTRAST | REAL | -100 | 100 |  | 
Color | SLA_MABEL_DIFFUSE_COLOR_A | COLOR |  |  |  | 
Roughness | SLA_MABEL_DIFFUSE_ROUGHNESS_A | REAL | 0 | 200 |  | 
Illumination | SLA_MABEL_DIFFUSE_ILLUMINATION_A | REAL | 0 | 1000 |  | 
Contrast | SLA_MABEL_DIFFUSE_CONTRAST_A | REAL | -1000 | 1000 |  | 
Color | SLA_MABEL_SPEC1_COLOR_A | COLOR |  |  |  | 
Intensity | SLA_MABEL_SPEC1_INTENSITY_A | REAL | 0 | 1000 |  | 
Size | SLA_MABEL_SPEC1_SIZE_A | REAL | 0 | 200 |  | 
Contrast | SLA_MABEL_SPEC1_CONTRAST_A | REAL | 0 | 100 |  | 
Glare | SLA_MABEL_SPEC1_GLARE_A | REAL | 0 | 1000 |  | 
Falloff | SLA_MABEL_SPEC1_FALLOFF_A | REAL | 0 |  |  | 
Color | SLA_MABEL_SPEC2_COLOR_A | COLOR |  |  |  | 
Intensity | SLA_MABEL_SPEC2_INTENSITY_A | REAL | 0 | 1000 |  | 
Size | SLA_MABEL_SPEC2_SIZE_A | REAL | 0 | 200 |  | 
Contrast | SLA_MABEL_SPEC2_CONTRAST_A | REAL | 0 | 100 |  | 
Glare | SLA_MABEL_SPEC2_GLARE_A | REAL | 0 | 1000 |  | 
Falloff | SLA_MABEL_SPEC2_FALLOFF_A | REAL | 0 |  |  | 
Color | SLA_MABEL_SPEC3_COLOR_A | COLOR |  |  |  | 
Intensity | SLA_MABEL_SPEC3_INTENSITY_A | REAL | 0 | 1000 |  | 
Size | SLA_MABEL_SPEC3_SIZE_A | REAL | 0 | 200 |  | 
Contrast | SLA_MABEL_SPEC3_CONTRAST_A | REAL | 0 | 100 |  | 
Glare | SLA_MABEL_SPEC3_GLARE_A | REAL | 0 | 1000 |  | 
Falloff | SLA_MABEL_SPEC3_FALLOFF_A | REAL | 0 |  |  | 
Intensity | SLA_MABEL_REFLECTION_INTENSITY_A | REAL | 0 | 1000 |  | 
Edge Intensity | SLA_MABEL_REFLECTION_EDGE_INTENSITY_A | REAL | 0 | 1000 |  | 
Falloff | SLA_MABEL_REFLECTION_FALLOFF_A | REAL | 0 |  |  | 
Reflection Color | SLA_MABEL_REFLECTION_REFLECTION_COLOR_A | COLOR |  |  |  | 
Reflection Edge Color | SLA_MABEL_REFLECTION_EDGE_COLOR_A | COLOR |  |  |  | 
Intensity | SLA_MABEL_ENVIRONMENT_INTENSITY_A | REAL | 0 | 1000 |  | 
Glare | SLA_MABEL_ENVIRONMENT_GLARE_A | REAL | 0 | 1000 |  | 
Falloff | SLA_MABEL_ENVIRONMENT_FALLOFF_A | REAL | 0 |  |  | 
Utilize Anisotropic Scratches | SLA_MABEL_ENVIRONMENT_UTILIZE_ANISO_SCRATCHES_A | BOOL |  |  |  | 
Blur | SLA_MABEL_ENVIRONMENT_BLUR_A | REAL | 0 | 100 |  | 
Samples | SLA_MABEL_ENVIRONMENT_SAMPLES_A | LONG | 2 |  |  | 
Jitter | SLA_MABEL_ENVIRONMENT_JITTER_A | REAL | 0 | 1000 |  | 
Environment Color | SLA_MABEL_ENVIRONMENT_ENVIRONMENT_COLOR_A | COLOR |  |  |  | 
Edge Color | SLA_MABEL_ENVIRONMENT_EDGE_COLOR_A | COLOR |  |  |  | 
Color | SLA_MABEL_AMBIENT_COLOR_A | COLOR |  |  |  | 
Intensity | SLA_MABEL_AMBIENT_INTENSITY_A | REAL | 0 | 1000 |  | 
Edge Intensity | SLA_MABEL_AMBIENT_EDGE_INTENSITY_A | REAL | 0 | 1000 |  | 
Falloff | SLA_MABEL_AMBIENT_FALLOFF_A | REAL | 0 |  |  | 
Seed | SLA_MABEL_ROUGHNESS_SEED_A | LONG |  |  |  | 
Function | SLA_MABEL_ROUGHNESS_NOISE_A | LONG |  |  |  | 
Amplitude | SLA_MABEL_ROUGHNESS_AMPLITUDE_A | REAL | -1000 | 1000 |  | 
Octaves | SLA_MABEL_ROUGHNESS_OCTAVES_A | REAL | 0 | 20 |  | 
Scale | SLA_MABEL_ROUGHNESS_SCALE_A | REAL | 0 |  |  | 
Attenuation | SLA_MABEL_ROUGHNESS_ATTENUATION_A | REAL | 0 | 1000 |  | 
Delta | SLA_MABEL_ROUGHNESS_DELTA_A | REAL | 0 |  |  | 
Hard Bump | SLA_MABEL_ROUGHNESS_HARD_BUMP_A | BOOL |  |  |  | 
Absolute | SLA_MABEL_ROUGHNESS_ABSOLUTE_A | BOOL |  |  |  | 
Low Clip | SLA_MABEL_ROUGHNESS_LOW_CLIP_A | REAL | 0 | 100 |  | 
High Clip | SLA_MABEL_ROUGHNESS_HIGH_CLIP_A | REAL | 0 | 100 |  | 
Grit Color | SLA_MABEL_ROUGHNESS_GRIT_COLOR_A | COLOR |  |  |  | 
Grit Intensity | SLA_MABEL_ROUGHNESS_GRIT_INTENSITY_A | REAL | -200 | 200 |  | 
Grit Low Clip | SLA_MABEL_ROUGHNESS_GRIT_LOW_CLIP_A | REAL | 0 | 100 |  | 
Grit High Clip | SLA_MABEL_ROUGHNESS_GRIT_HIGH_CLIP_A | REAL | 0 | 100 |  | 
Projection | SLA_MABEL_ANISOTROPY_PROJECTION_A | LONG |  |  |  | SLA_MABEL_PROJECTION_PLANAR; SLA_MABEL_PROJECTION_AUTO_PLANAR; SLA_MABEL_PROJECTION_SHRINK_WRAP; SLA_MABEL_PROJECTION_RADIAL_AUTO_PLANAR; SLA_MABEL_PROJECTION_RAD_PATTERN_AUTO_PLANAR; SLA_MABEL_PROJECTION_RADIAL_PLANAR; SLA_MABEL_PROJECTION_RAD_PATTERN_PLANAR
Projection Scale | SLA_MABEL_ANISOTROPY_PROJ_SCALE_A | REAL | 0 | 1000 |  | 
Roughness X | SLA_MABEL_ANISOTROPY_X_ROUGH_A | REAL | 0 |  |  | 
Roughness Y | SLA_MABEL_ANISOTROPY_Y_ROUGH_A | REAL | 0 |  |  | 
Amplitude | SLA_MABEL_ANISOTROPY_AMPL_A | REAL | 0 | 100 |  | 
Scale | SLA_MABEL_ANISOTROPY_SCALE_A | REAL | 0 |  |  | 
Length | SLA_MABEL_ANISOTROPY_LENGTH_A | REAL | 0 |  |  | 
Attenuation | SLA_MABEL_ANISOTROPY_ATT_A | REAL | 0 |  |  | 
Specular 1 | SLA_MABEL_ANISOTROPY_CHANNEL1_A | BOOL |  |  |  | 
Specular 2 | SLA_MABEL_ANISOTROPY_CHANNEL2_A | BOOL |  |  |  | 
Specular 3 | SLA_MABEL_ANISOTROPY_CHANNEL3_A | BOOL |  |  |  | 
Color | SLA_MABEL_DIFFUSE_COLOR_B | COLOR |  |  |  | 
Algorithm | SLA_MABEL_DIFFUSE_ALGORITHM_A | LONG |  |  |  | SLA_MABEL_DIFFUSE_ALGORITHM_INTERNAL; SLA_MABEL_DIFFUSE_ALGORITHM_OREN_NAYAR
Roughness | SLA_MABEL_DIFFUSE_ROUGHNESS_B | REAL | 0 | 200 |  | 
Illumination | SLA_MABEL_DIFFUSE_ILLUMINATION_B | REAL | 0 | 1000 |  | 
Contrast | SLA_MABEL_DIFFUSE_CONTRAST_B | REAL | -1000 | 1000 |  | 
Color | SLA_MABEL_SPEC1_COLOR_B | COLOR |  |  |  | 
Intensity | SLA_MABEL_SPEC1_INTENSITY_B | REAL | 0 | 1000 |  | 
Size | SLA_MABEL_SPEC1_SIZE_B | REAL | 0 | 200 |  | 
Contrast | SLA_MABEL_SPEC1_CONTRAST_B | REAL | 0 | 100 |  | 
Glare | SLA_MABEL_SPEC1_GLARE_B | REAL | 0 | 1000 |  | 
Falloff | SLA_MABEL_SPEC1_FALLOFF_B | REAL | 0 |  |  | 
Color | SLA_MABEL_SPEC2_COLOR_B | COLOR |  |  |  | 
Intensity | SLA_MABEL_SPEC2_INTENSITY_B | REAL | 0 | 1000 |  | 
Size | SLA_MABEL_SPEC2_SIZE_B | REAL | 0 | 200 |  | 
Contrast | SLA_MABEL_SPEC2_CONTRAST_B | REAL | 0 | 100 |  | 
Glare | SLA_MABEL_SPEC2_GLARE_B | REAL | 0 | 1000 |  | 
Falloff | SLA_MABEL_SPEC2_FALLOFF_B | REAL | 0 |  |  | 
Color | SLA_MABEL_SPEC3_COLOR_B | COLOR |  |  |  | 
Intensity | SLA_MABEL_SPEC3_INTENSITY_B | REAL | 0 | 1000 |  | 
Size | SLA_MABEL_SPEC3_SIZE_B | REAL | 0 | 200 |  | 
Contrast | SLA_MABEL_SPEC3_CONTRAST_B | REAL | 0 | 100 |  | 
Glare | SLA_MABEL_SPEC3_GLARE_B | REAL | 0 | 1000 |  | 
Falloff | SLA_MABEL_SPEC3_FALLOFF_B | REAL | 0 |  |  | 
Intensity | SLA_MABEL_REFLECTION_INTENSITY_B | REAL | 0 | 1000 |  | 
Edge Intensity | SLA_MABEL_REFLECTION_EDGE_INTENSITY_B | REAL | 0 | 1000 |  | 
Falloff | SLA_MABEL_REFLECTION_FALLOFF_B | REAL | 0 |  |  | 
Reflection Color | SLA_MABEL_REFLECTION_REFLECTION_COLOR_B | COLOR |  |  |  | 
Reflection Edge Color | SLA_MABEL_REFLECTION_EDGE_COLOR_B | COLOR |  |  |  | 
Image | SLA_MABEL_ENVIRONMENT_IMAGE | SHADERLINK |  |  |  | 
Intensity | SLA_MABEL_ENVIRONMENT_INTENSITY_B | REAL | 0 | 1000 |  | 
Glare | SLA_MABEL_ENVIRONMENT_GLARE_B | REAL | 0 | 1000 |  | 
Falloff | SLA_MABEL_ENVIRONMENT_FALLOFF_B | REAL | 0 |  |  | 
Utilize Anisotropic Scratches | SLA_MABEL_ENVIRONMENT_UTILIZE_ANISO_SCRATCHES_B | BOOL |  |  |  | 
Blur | SLA_MABEL_ENVIRONMENT_BLUR_B | REAL | 0 | 100 |  | 
Samples | SLA_MABEL_ENVIRONMENT_SAMPLES_B | LONG | 2 |  |  | 
Jitter | SLA_MABEL_ENVIRONMENT_JITTER_B | REAL | 0 | 1000 |  | 
Environment Color | SLA_MABEL_ENVIRONMENT_ENVIRONMENT_COLOR_B | COLOR |  |  |  | 
Edge Color | SLA_MABEL_ENVIRONMENT_EDGE_COLOR_B | COLOR |  |  |  | 
Color | SLA_MABEL_AMBIENT_COLOR_B | COLOR |  |  |  | 
Intensity | SLA_MABEL_AMBIENT_INTENSITY_B | REAL | 0 | 1000 |  | 
Edge Intensity | SLA_MABEL_AMBIENT_EDGE_INTENSITY_B | REAL | 0 | 1000 |  | 
Falloff | SLA_MABEL_AMBIENT_FALLOFF_B | REAL | 0 |  |  | 
Seed | SLA_MABEL_ROUGHNESS_SEED_B | LONG |  |  |  | 
Function | SLA_MABEL_ROUGHNESS_NOISE_B | LONG |  |  |  | 
Amplitude | SLA_MABEL_ROUGHNESS_AMPLITUDE_B | REAL | -1000 | 1000 |  | 
Octaves | SLA_MABEL_ROUGHNESS_OCTAVES_B | REAL | 0 | 20 |  | 
Scale | SLA_MABEL_ROUGHNESS_SCALE_B | REAL | 0 |  |  | 
Attenuation | SLA_MABEL_ROUGHNESS_ATTENUATION_B | REAL | 0 | 1000 |  | 
Delta | SLA_MABEL_ROUGHNESS_DELTA_B | REAL | 0 |  |  | 
Hard Bump | SLA_MABEL_ROUGHNESS_HARD_BUMP_B | BOOL |  |  |  | 
Absolute | SLA_MABEL_ROUGHNESS_ABSOLUTE_B | BOOL |  |  |  | 
Low Clip | SLA_MABEL_ROUGHNESS_LOW_CLIP_B | REAL | 0 | 100 |  | 
High Clip | SLA_MABEL_ROUGHNESS_HIGH_CLIP_B | REAL | 0 | 100 |  | 
Grit Color | SLA_MABEL_ROUGHNESS_GRIT_COLOR_B | COLOR |  |  |  | 
Grit Intensity | SLA_MABEL_ROUGHNESS_GRIT_INTENSITY_B | REAL | -200 | 200 |  | 
Grit Low Clip | SLA_MABEL_ROUGHNESS_GRIT_LOW_CLIP_B | REAL | 0 | 100 |  | 
Grit High Clip | SLA_MABEL_ROUGHNESS_GRIT_HIGH_CLIP_B | REAL | 0 | 100 |  | 
Projection | SLA_MABEL_ANISOTROPY_PROJECTION_B | LONG |  |  |  | SLA_MABEL_PROJECTION_PLANAR; SLA_MABEL_PROJECTION_AUTO_PLANAR; SLA_MABEL_PROJECTION_SHRINK_WRAP; SLA_MABEL_PROJECTION_RADIAL_AUTO_PLANAR; SLA_MABEL_PROJECTION_RAD_PATTERN_AUTO_PLANAR; SLA_MABEL_PROJECTION_RADIAL_PLANAR; SLA_MABEL_PROJECTION_RAD_PATTERN_PLANAR
Projection Scale | SLA_MABEL_ANISOTROPY_PROJ_SCALE_B | REAL | 0 | 1000 |  | 
Roughness X | SLA_MABEL_ANISOTROPY_X_ROUGH_B | REAL | 0 |  |  | 
Roughness Y | SLA_MABEL_ANISOTROPY_Y_ROUGH_B | REAL | 0 |  |  | 
Amplitude | SLA_MABEL_ANISOTROPY_AMPL_B | REAL | 0 | 100 |  | 
Scale | SLA_MABEL_ANISOTROPY_SCALE_B | REAL | 0 |  |  | 
Length | SLA_MABEL_ANISOTROPY_LENGTH_B | REAL | 0 |  |  | 
Attenuation | SLA_MABEL_ANISOTROPY_ATT_B | REAL | 0 |  |  | 
Specular 1 | SLA_MABEL_ANISOTROPY_CHANNEL1_B | BOOL |  |  |  | 
Specular 2 | SLA_MABEL_ANISOTROPY_CHANNEL2_B | BOOL |  |  |  | 
Specular 3 | SLA_MABEL_ANISOTROPY_CHANNEL3_B | BOOL |  |  |  | 
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
