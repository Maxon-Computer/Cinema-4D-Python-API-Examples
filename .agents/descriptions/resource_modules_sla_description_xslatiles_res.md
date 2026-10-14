# Description: Tile Shader

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/sla/description/xslatiles.res`
- **Symbol:** `XSLATiles`
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
Grout Color | SLA_TILES_GROUT_COLOR | COLOR |  |  |  | 
Tiles Color 1 | SLA_TILES_TILE_COLOR_1 | COLOR |  |  |  | 
Tiles Color 2 | SLA_TILES_TILE_COLOR_2 | COLOR |  |  |  | 
Tiles Color 3 | SLA_TILES_TILE_COLOR_3 | COLOR |  |  |  | 
Pattern | SLA_TILES_PATTERN | LONG |  |  |  | SLA_TILES_PATTERN_BRICK1; SLA_TILES_PATTERN_BRICK2; SLA_TILES_PATTERN_CIRCLES1; SLA_TILES_PATTERN_CIRCLES2; SLA_TILES_PATTERN_CIRCLES3; SLA_TILES_PATTERN_HEXAGONS; SLA_TILES_PATTERN_LINES1; SLA_TILES_PATTERN_LINES2; SLA_TILES_PATTERN_PARQUET; SLA_TILES_PATTERN_PLANKS; SLA_TILES_PATTERN_RADIAL_LINES1; SLA_TILES_PATTERN_RADIAL_LINES2; SLA_TILES_PATTERN_RANDOM; SLA_TILES_PATTERN_RINGS1; SLA_TILES_PATTERN_RINGS2; SLA_TILES_PATTERN_SAWTOOTH1; SLA_TILES_PATTERN_SAWTOOTH2; SLA_TILES_PATTERN_SCALES1; SLA_TILES_PATTERN_SCALES2; SLA_TILES_PATTERN_SPIRAL1; SLA_TILES_PATTERN_SPIRAL2; SLA_TILES_PATTERN_SQUARES; SLA_TILES_PATTERN_TRIANGLES1; SLA_TILES_PATTERN_TRIANGLES2; SLA_TILES_PATTERN_TRIANGLES3; SLA_TILES_PATTERN_WAVES1; SLA_TILES_PATTERN_WAVES2; SLA_TILES_PATTERN_WEAVE
Grout Width | SLA_TILES_GROUT_WIDTH | REAL | 0.0 | 100.0 |  | 
Bevel Width | SLA_TILES_BEVEL_WIDTH | REAL | 0.0 | 100.0 |  | 
Bevel | SLA_TILES_SMOOTH_BEVEL | BOOL |  |  |  | 
Randomize Color | SLA_TILES_RANDOMIZE_COLOR | BOOL |  |  |  | 
Orientation | SLA_TILES_ORIENTATION | LONG |  |  |  | SLA_TILES_ORIENTATION_U; SLA_TILES_ORIENTATION_V
Global Scale | SLA_TILES_GLOBAL_SCALE | REAL | 0.0 |  |  | 
U Scale | SLA_TILES_U_SCALE | REAL | 0.0 |  |  | 
V Scale | SLA_TILES_V_SCALE | REAL | 0.0 |  |  | 
Radial Scale | SLA_TILES_RADIAL_SCALE | REAL | 0.0 |  |  | 
Rotate | SLA_TILES_ROTATE | REAL |  |  |  | 
Delta | SLA_TILES_DELTA | REAL | 0.0 |  |  | 
Seed | SLA_TILES_SEED | LONG |  |  |  | 
