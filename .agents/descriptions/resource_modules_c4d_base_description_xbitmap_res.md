# Description: Bitmap Shader

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/c4d_base/description/xbitmap.res`
- **Symbol:** `Xbitmap`
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
Reload Image... | BITMAPSHADER_RELOADIMAGE | BUTTON |  |  |  | 
Edit Image... | BITMAPSHADER_EDITIMAGE | BUTTON |  |  |  | 
Locate Image... | BITMAPSHADER_LOCATEIMAGE | BUTTON |  |  |  | 
Find Similar (AI)... | BITMAPSHADER_FINDSIMILAR | BUTTON |  |  |  | 
Sampling | BITMAPSHADER_INTERPOLATION | LONG |  |  |  | BITMAPSHADER_INTERPOLATION_NONE; BITMAPSHADER_INTERPOLATION_CIRCLE; BITMAPSHADER_INTERPOLATION_SQUARE; BITMAPSHADER_INTERPOLATION_ALIAS1; BITMAPSHADER_INTERPOLATION_ALIAS2; BITMAPSHADER_INTERPOLATION_ALIAS3; BITMAPSHADER_INTERPOLATION_MIP; BITMAPSHADER_INTERPOLATION_SAT
File | BITMAPSHADER_FILENAME | FILENAME |  |  |  | 
Layer Set | BITMAPSHADER_LAYERSET | LAYERSET |  |  |  | 
Color Profile | BITMAPSHADER_COLORPROFILE | LONG |  |  |  | BITMAPSHADER_COLORPROFILE_EMBEDDED; BITMAPSHADER_COLORPROFILE_LINEAR; BITMAPSHADER_COLORPROFILE_SRGB; BITMAPSHADER_COLORPROFILE_CUSTOM
Custom Color Profile | BITMAPSHADER_CUSTOMCOLORPROFILE | COLORPROFILE |  |  |  | 
Color Space | BITMAPSHADER_OCIO_INPUT_COLORSPACE | LONG |  |  |  | 
Exposure | BITMAPSHADER_EXPOSURE | REAL | -25.0 | 25.0 |  | 
HDR Gamma | BITMAPSHADER_GAMMA | REAL | 0.0 | 100.0 |  | 
Black Point | BITMAPSHADER_BLACKPOINT | REAL | 0.0 | 100.0 |  | 
White Point | BITMAPSHADER_WHITEPOINT | REAL | 0.0 | 100.0 |  | 
Reset | BITMAPSHADER_RESETVALUES | BUTTON |  |  |  | 
Mode | BITMAPSHADER_TIMING_MODE | LONG |  |  |  | BITMAPSHADER_TIMING_MODE_SIMPLE; BITMAPSHADER_TIMING_MODE_LOOP; BITMAPSHADER_TIMING_MODE_PINGPONG
Timing | BITMAPSHADER_TIMING_TIMING | LONG |  |  |  | BITMAPSHADER_TIMING_TIMING_FRAME; BITMAPSHADER_TIMING_TIMING_SECOND; BITMAPSHADER_TIMING_TIMING_AREA
Range Start | BITMAPSHADER_TIMING_RANGEFROM | BASETIME | 0.0 | 999999999.0 |  | 
Range End | BITMAPSHADER_TIMING_RANGETO | BASETIME | 0.0 | 999999999.0 |  | 
Loops | BITMAPSHADER_TIMING_LOOPS | LONG | 0 | 1000 |  | 
Movie Start Frame | BITMAPSHADER_TIMING_FROM | LONG | 0 | 999999999 |  | 
Movie End Frame | BITMAPSHADER_TIMING_TO | LONG | 0 | 999999999 |  | 
Movie Frame Rate | BITMAPSHADER_TIMING_FPS | REAL | 1 | 100 |  | 
Calculate | BITMAPSHADER_CALCULATE | BUTTON |  |  |  | 
