# Description: Projection Shader

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/sla/description/xslaprojector.res`
- **Symbol:** `XSLAProjector`
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
Texture | SLA_PROJECTOR_TEXTURE | SHADERLINK |  |  |  | 
Projection | SLA_PROJECTOR_PROJECTION | LONG |  |  |  | SLA_PROJECTOR_PROJECTION_SPHERICAL; SLA_PROJECTOR_PROJECTION_CYLINDRICAL; SLA_PROJECTOR_PROJECTION_FLAT; SLA_PROJECTOR_PROJECTION_CUBIC; SLA_PROJECTOR_PROJECTION_FRONTAL; SLA_PROJECTOR_PROJECTION_SPATIAL; SLA_PROJECTOR_PROJECTION_UVW; SLA_PROJECTOR_PROJECTION_SHRINKWRAP
Offset X | SLA_PROJECTOR_OFFSET_X | REAL |  |  |  | 
Offset Y | SLA_PROJECTOR_OFFSET_Y | REAL |  |  |  | 
Length X | SLA_PROJECTOR_LENGTH_X | REAL |  |  |  | 
Length Y | SLA_PROJECTOR_LENGTH_Y | REAL |  |  |  | 
Tiles X | SLA_PROJECTOR_TILES_X | REAL |  |  |  | 
Tiles Y | SLA_PROJECTOR_TILES_Y | REAL |  |  |  | 
Tile | SLA_PROJECTOR_TILE | BOOL |  |  |  | 
Seamless | SLA_PROJECTOR_SEAMLESS | BOOL |  |  |  | 
Position | SLA_PROJECTOR_POSITION | VECTOR |  |  |  | 
Rotation | SLA_PROJECTOR_ROTATION | VECTOR |  |  |  | 
Scale | SLA_PROJECTOR_SIZE | VECTOR |  |  |  | 
Paste Tag | SLA_PROJECTOR_PASTE_TAG | BUTTON |  |  |  | 
