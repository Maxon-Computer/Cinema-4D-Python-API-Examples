# Description: Pavement Shader

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/shader/description/xpavement.res`
- **Symbol:** `xpavement`
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
Scale | PAVEMENT_SCALE | REAL | 0.0 |  |  | 
Seed | PAVEMENT_SEED | LONG | 0 |  |  | 
Width | PAVEMENT_GAP_SIZE | REAL | 1.0 | 100.0 |  | 
Soft | PAVEMENT_GAP_BLUR | REAL | 0.0 | 200.0 |  | 
Crookedness | PAVEMENT_GAP_CROOKED_INTENSITY | REAL | 0.0 |  |  | 
Crookedness Scale | PAVEMENT_GAP_CROOKED_SCALE | REAL | 0.0 |  |  | 
Stone Color | PAVEMENT_COL_STONE | GRADIENT |  |  |  | 
Rough Structure | PAVEMENT_COL_STONE_STRUCT1 | REAL | 0.0 | 100.0 |  | 
Fine Structure | PAVEMENT_COL_STONE_STRUCT2 | REAL | 0.0 | 100.0 |  | 
Gap Color | PAVEMENT_COL_GAP | GRADIENT |  |  |  | 
Grainy Gaps | PAVEMENT_COL_GRAINYGAPS | REAL | 0.0 | 100.0 |  | 
Contrast Grain | PAVEMENT_COL_GRAINYGAPS_MODE | BOOL |  |  |  | 
Smudgy Color | PAVEMENT_COL_SMUDGE | GRADIENT |  |  |  | 
Smudgy Edges | PAVEMENT_COL_SMUDGYEDGES | REAL | 0.0 | 100.0 |  | 
Smudgy Edges Size | PAVEMENT_COL_SMUDGYEDGES_SIZE | REAL | 0.0 | 100.0 |  | 
