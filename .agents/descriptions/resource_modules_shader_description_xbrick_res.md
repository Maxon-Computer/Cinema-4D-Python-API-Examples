# Description: Brick

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/shader/description/xbrick.res`
- **Symbol:** `xbrick`
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
Scale | BRICK_SCALE | REAL | 0.0 |  |  | 
Brick Width | BRICK_WIDTH | REAL | 0 |  |  | 
Brick Height | BRICK_HEIGHT | REAL | 0 |  |  | 
Shift | BRICK_SHIFT | REAL |  |  |  | 
Reset Every nth Row | BRICK_SHIFT_RESET | LONG | 0 |  |  | 
Half Width Every nth Row | BRICK_HALFWIDTH | LONG | 0 |  |  | 
Shift | BRICK_HALFWIDTH_SHIFT | REAL |  |  |  | 
Balance Alt. Color Period | BRICK_ALTCOL_BALANCE_HPERIOD | BOOL |  |  |  | 
Displacement Mode | BRICK_DISPLACEMENTMODE | SEPARATOR |  |  |  | 
Enable | BRICK_DISPLACEMENTMODE_ENABLE | BOOL |  |  |  | 
Height Variation | BRICK_DISPLACEMENTMODE_RANDOM_HEIGHT | REAL | 0.0 | 100.0 |  | 
Slope Intensity | BRICK_DISPLACEMENTMODE_RANDOM_SLOPE | REAL | 0.0 | 100.0 |  | 
Slope Direction | BRICK_DISPLACEMENTMODE_SLOPE_MODE | LONG |  |  |  | BRICK_DISPLACEMENTMODE_MODE_SLOPE_RANDOM; BRICK_DISPLACEMENTMODE_MODE_SLOPE_LEFT; BRICK_DISPLACEMENTMODE_MODE_SLOPE_RIGHT; BRICK_DISPLACEMENTMODE_MODE_SLOPE_UP; BRICK_DISPLACEMENTMODE_MODE_SLOPE_DOWN
Seed | BRICK_DISPLACEMENTMODE_SEED | LONG | 0 |  |  | 
Brick Color | BRICK_COL | GRADIENT |  |  |  | 
Texture | BRICK_TEX_LINK | SHADERLINK |  |  |  | 
Offset | BRICK_TEX_OFFSET | REAL |  |  |  | 
Random | BRICK_TEX_OFFSET_RANDOM | BOOL |  |  |  | 
Scale | BRICK_TEX_SCALE | REAL | 0.0 |  |  | 
Flip | BRICK_TEX_FLIP | BOOL |  |  |  | 
Opacity | BRICK_TEX_OPACITY | REAL | 0.0 | 100.0 |  | 
Blend Mode | BRICK_TEX_BLENDMODE | LONG |  |  |  | BRICK_BLENDMODE_NORMAL; BRICK_BLENDMODE_MULTIPLY; BRICK_BLENDMODE_OVERLAY; BRICK_BLENDMODE_DODGE; BRICK_BLENDMODE_BURN; BRICK_BLENDMODE_LIGHTEN; BRICK_BLENDMODE_DARKEN; BRICK_BLENDMODE_COLOR
Alt. Brick Color | BRICK_ALTCOL | GRADIENT |  |  |  | 
Texture | BRICK_ALTTEX_LINK | SHADERLINK |  |  |  | 
Offset | BRICK_ALTTEX_OFFSET | REAL |  |  |  | 
Random | BRICK_ALTTEX_OFFSET_RANDOM | BOOL |  |  |  | 
Scale | BRICK_ALTTEX_SCALE | REAL | 0.0 |  |  | 
Flip | BRICK_ALTTEX_FLIP | BOOL |  |  |  | 
Opacity | BRICK_ALTTEX_OPACITY | REAL | 0.0 | 100.0 |  | 
Blend Mode | BRICK_ALTTEX_BLENDMODE | LONG |  |  |  | BRICK_BLENDMODE_NORMAL; BRICK_BLENDMODE_MULTIPLY; BRICK_BLENDMODE_OVERLAY; BRICK_BLENDMODE_DODGE; BRICK_BLENDMODE_BURN; BRICK_BLENDMODE_LIGHTEN; BRICK_BLENDMODE_DARKEN; BRICK_BLENDMODE_COLOR
Alt. Color Every n Rows | BRICK_ALTCOL_VPERIOD | LONG | 0 |  |  | 
Alt. Color Every n Columns | BRICK_ALTCOL_HPERIOD | LONG | 0 |  |  | 
Brick Noise Scale | BRICK_COL_NOISE_SCALE | REAL |  |  |  | 
Detail | BRICK_COL_DETAILS_INTENSITY | REAL | 0.0 | 100.0 |  | 
Detail Scale | BRICK_COL_DETAILS_SCALE | REAL | 0.0 |  |  | 
Gap Color | BRICK_GAPCOL | GRADIENT |  |  |  | 
Texture | BRICK_GAPTEX_LINK | SHADERLINK |  |  |  | 
Scale | BRICK_GAPTEX_SCALE | REAL | 0.0 |  |  | 
Flip | BRICK_GAPTEX_FLIP | BOOL |  |  |  | 
Opacity | BRICK_GAPTEX_OPACITY | REAL | 0.0 | 100.0 |  | 
Blend Mode | BRICK_GAPTEX_BLENDMODE | LONG |  |  |  | BRICK_BLENDMODE_NORMAL; BRICK_BLENDMODE_MULTIPLY; BRICK_BLENDMODE_OVERLAY; BRICK_BLENDMODE_DODGE; BRICK_BLENDMODE_BURN; BRICK_BLENDMODE_LIGHTEN; BRICK_BLENDMODE_DARKEN; BRICK_BLENDMODE_COLOR
Gap Noise Scale | BRICK_GAPCOL_NOISE_SCALE | REAL |  |  |  | 
Depth | BRICK_DEPTH | REAL | 0.0 |  |  | 
Size | BRICK_GAPSIZE | REAL | 0.0 |  |  | 
Groove | BRICK_GAPNOTCH | REAL | -100.0 | 100.0 |  | 
Size Variation | BRICK_NOISE_INTENSITY | REAL | 0.0 | 100.0 |  | 
Size Variation Scale | BRICK_NOISE_SCALE | REAL | 0.0 |  |  | 
Enable | BRICK_DIRT_ENABLE | BOOL |  |  |  | 
Brick | BRICK_DIRT_ENABLE_BRICK | BOOL |  |  |  | 
Gap | BRICK_DIRT_ENABLE_GAP | BOOL |  |  |  | 
Opacity | BRICK_DIRT_OPACITY | REAL | 0 | 100.0 |  | 
Gap Blending | BRICK_DIRT_GAP_BLEND | REAL | -100.0 | 100.0 |  | 
Brick Blending | BRICK_DIRT_BRICK_BLEND | REAL | -100.0 | 100.0 |  | 
Color | BRICK_DIRT_COL | GRADIENT |  |  |  | 
Color Scale | BRICK_DIRT_COL_SCALE | REAL |  |  |  | 
Shift | BRICK_DIRT_ALPHA_SHIFT | VECTOR |  |  |  | 
Opacity Scale | BRICK_DIRT_ALPHA_SCALE | REAL |  |  |  | 
Octaves | BRICK_DIRT_ALPHA_OCT | REAL | 0 | 10 |  | 
Texture | BRICK_DIRTTEX_LINK | SHADERLINK |  |  |  | 
Color Texture | BRICK_DIRTTEX_COLOR_LINK | SHADERLINK |  |  |  | 
Shift | BRICK_DIRTTEX_SHIFT | VECTOR |  |  |  | 
Scale | BRICK_DIRTTEX_SCALE | REAL |  |  |  | 
Flip | BRICK_DIRTTEX_FLIP | BOOL |  |  |  | 
Multiply with Gradient | BRICK_DIRTTEX_MULTIPLYCOLOR | BOOL |  |  |  | 
Alpha Invert | BRICK_DIRTTEX_ALPHA_INVERT | BOOL |  |  |  | 
Alpha Contrast | BRICK_DIRTTEX_ALPHA_CONTRAST | REAL | 0.0 |  |  | 
Alpha Bias | BRICK_DIRTTEX_ALPHA_BIAS | REAL |  |  |  | 
Rain | BRICK_DIRTTEX_RAIN | REAL | 0.0 | 5000.0 |  | 
Samples | BRICK_DIRTTEX_RAIN_SAMPLES | LONG | 6 |  |  | 
Blur Color Texture | BRICK_DIRTTEX_RAIN_DOCOLOR | BOOL |  |  |  | 
