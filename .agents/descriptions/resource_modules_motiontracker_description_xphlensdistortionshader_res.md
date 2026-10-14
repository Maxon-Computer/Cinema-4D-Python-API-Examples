# Description: Lens Distortion

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/motiontracker/description/xphlensdistortionshader.res`
- **Symbol:** `Xphlensdistortionshader`
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
Lens Profile Filename | PH_LENS_PROFILE_FILENAME | FILENAME |  |  |  | 
No label | PH_LENS_PROFILE_TYPE | STATICTEXT |  |  |  | 
No label | PH_LENS_PARAM_RC_00 | STATICTEXT |  |  |  | 
No label | PH_LENS_PARAM_RC_01 | STATICTEXT |  |  |  | 
No label | PH_LENS_PARAM_RC_02 | STATICTEXT |  |  |  | 
No label | PH_LENS_PARAM_RC_03 | STATICTEXT |  |  |  | 
No label | PH_LENS_PARAM_RC_04 | STATICTEXT |  |  |  | 
No label | PH_LENS_PARAM_RC_05 | STATICTEXT |  |  |  | 
No label | PH_LENS_PARAM_RC_10 | STATICTEXT |  |  |  | 
No label | PH_LENS_PARAM_RC_11 | STATICTEXT |  |  |  | 
No label | PH_LENS_PARAM_RC_12 | STATICTEXT |  |  |  | 
No label | PH_LENS_PARAM_RC_13 | STATICTEXT |  |  |  | 
No label | PH_LENS_PARAM_RC_14 | STATICTEXT |  |  |  | 
No label | PH_LENS_PARAM_RC_15 | STATICTEXT |  |  |  | 
No label | PH_LENS_PARAM_RC_20 | STATICTEXT |  |  |  | 
No label | PH_LENS_PARAM_RC_21 | STATICTEXT |  |  |  | 
No label | PH_LENS_PARAM_RC_22 | STATICTEXT |  |  |  | 
No label | PH_LENS_PARAM_RC_23 | STATICTEXT |  |  |  | 
No label | PH_LENS_PARAM_RC_24 | STATICTEXT |  |  |  | 
No label | PH_LENS_PARAM_RC_25 | STATICTEXT |  |  |  | 
No label | PH_LENS_PARAM_RC_30 | STATICTEXT |  |  |  | 
No label | PH_LENS_PARAM_RC_31 | STATICTEXT |  |  |  | 
No label | PH_LENS_PARAM_RC_32 | STATICTEXT |  |  |  | 
No label | PH_LENS_PARAM_RC_33 | STATICTEXT |  |  |  | 
No label | PH_LENS_PARAM_RC_34 | STATICTEXT |  |  |  | 
No label | PH_LENS_PARAM_RC_35 | STATICTEXT |  |  |  | 
No label | PH_LENS_PARAM_RC_40 | STATICTEXT |  |  |  | 
No label | PH_LENS_PARAM_RC_41 | STATICTEXT |  |  |  | 
No label | PH_LENS_PARAM_RC_42 | STATICTEXT |  |  |  | 
No label | PH_LENS_PARAM_RC_43 | STATICTEXT |  |  |  | 
No label | PH_LENS_PARAM_RC_44 | STATICTEXT |  |  |  | 
No label | PH_LENS_PARAM_RC_45 | STATICTEXT |  |  |  | 
Image Scale | PH_IMAGE_VIEW_SCALE | REAL | 1.0 | 10000.0 |  | 
Image Offset X | PH_IMAGE_VIEW_OFFSET_X | REAL | -500.0 | 500.0 |  | 
Image Offset Y | PH_IMAGE_VIEW_OFFSET_Y | REAL | -500.0 | 500.0 |  | 
Texture | LENSDISTORTIONSHADER_TEXTURE | SHADERLINK |  |  |  | 
