# Description: Fusion Shader

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/sla/description/xslafusion.res`
- **Symbol:** `XSLAFusion`
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
Mode | SLA_FUSION_MODE | LONG |  |  |  | SLA_FUSION_MODE_NORMAL; SLA_FUSION_MODE_SEP_1; SLA_FUSION_MODE_MULTIPLY; SLA_FUSION_MODE_SCREEN; SLA_FUSION_MODE_OVERLAY; SLA_FUSION_MODE_HARD_LIGHT; SLA_FUSION_MODE_SOFT_LIGHT; SLA_FUSION_MODE_SEP_2; SLA_FUSION_MODE_DODGE; SLA_FUSION_MODE_BURN; SLA_FUSION_MODE_SEP_3; SLA_FUSION_MODE_DARKEN; SLA_FUSION_MODE_LIGHTEN; SLA_FUSION_MODE_ADD; SLA_FUSION_MODE_SUBTRACT; SLA_FUSION_MODE_DIFFERENCE; SLA_FUSION_MODE_EXCLUSION; SLA_FUSION_MODE_SEP_4; SLA_FUSION_MODE_HUE; SLA_FUSION_MODE_SAT; SLA_FUSION_MODE_COLOR; SLA_FUSION_MODE_LUMINANCE; SLA_FUSION_MODE_SEP_5; SLA_FUSION_MODE_LEVR
Blend | SLA_FUSION_BLEND | REAL | 0 | 100 |  | 
Use Mask | SLA_FUSION_USE_MASK | BOOL |  |  |  | 
Invert Mask | SLA_FUSION_INVERT_MASK | BOOL |  |  |  | 
Invert Output | SLA_FUSION_INVERT_OUTPUT | BOOL |  |  |  | 
Blend Channel | SLA_FUSION_BLEND_CHANNEL | SHADERLINK |  |  |  | 
Mask Channel | SLA_FUSION_MASK_CHANNEL | SHADERLINK |  |  |  | 
Base Channel | SLA_FUSION_BASE_CHANNEL | SHADERLINK |  |  |  | 
