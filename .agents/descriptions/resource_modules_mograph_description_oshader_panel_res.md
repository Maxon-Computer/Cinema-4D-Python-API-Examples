# Description: Shader Panel

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/mograph/description/oshader_panel.res`
- **Symbol:** `Oshader_panel`
- **Category:** Other

Use parameter symbols to access parameters and cycle option symbols for cycle values, never their numeric IDs. Treat Min and Max as constraints and Default as the declared initial value; blank cells mean the resource does not declare that metadata, not that the value is zero. Base Description Parameters lists inherited fields from each base; All Parameters lists the effective parameter set for this description.

## Base Description Parameters

No base descriptions.

## All Parameters

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Channel | ID_MG_SHADER_CHANNELSELECT | LONG |  |  |  | ID_MG_SHADER_CHANNELSELECT_COLOR; ID_MG_SHADER_CHANNELSELECT_LUMINANCE; ID_MG_SHADER_CHANNELSELECT_TRANSPARENCY; ID_MG_SHADER_CHANNELSELECT_ENVIRONMENT; ID_MG_SHADER_CHANNELSELECT_BUMP; ID_MG_SHADER_CHANNELSELECT_ALPHA; ID_MG_SHADER_CHANNELSELECT_SPECULAR; ID_MG_SHADER_CHANNELSELECT_DISPLACEMENT; ID_MG_SHADER_CHANNELSELECT_DIFFUSION; ID_MG_SHADER_CHANNELSELECT_NORMAL; ID_MG_SHADER_CHANNELSELECT_DIRECT
Edit | ID_MG_SHADER_EDIT_CHANNEL | BUTTON |  |  |  | 
Material Tag | ID_MG_SHADER_MATERIALTAG | LINK |  |  |  | 
Shader | ID_MG_SHADER_SHADER | SHADERLINK |  |  |  | 
Offset U | ID_MG_SHADER_TEXTAG_OFFSETX | REAL |  |  |  | 
Offset V | ID_MG_SHADER_TEXTAG_OFFSETY | REAL |  |  |  | 
Length U | ID_MG_SHADER_TEXTAG_LENGTHX | REAL |  |  |  | 
Length V | ID_MG_SHADER_TEXTAG_LENGTHY | REAL |  |  |  | 
Tile | ID_MG_SHADER_TEXTAG_TILE | BOOL |  |  |  | 
Use | ID_MG_SHADER_USE | LONG |  |  |  | ID_MG_SHADER_USE_ALPHA; ID_MG_SHADER_USE_GRAY; ID_MG_SHADER_USE_RED; ID_MG_SHADER_USE_GREEN; ID_MG_SHADER_USE_BLUE
Invert | ID_MG_SHADER_INVERTALPHA | BOOL |  |  |  | 
