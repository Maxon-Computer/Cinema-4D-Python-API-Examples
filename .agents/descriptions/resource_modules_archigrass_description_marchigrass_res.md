# Description: Architectural Grass

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/archigrass/description/marchigrass.res`
- **Symbol:** `Marchigrass`
- **Category:** Materials

Use parameter symbols to access parameters and cycle option symbols for cycle values, never their numeric IDs. Treat Min and Max as constraints and Default as the declared initial value; blank cells mean the resource does not declare that metadata, not that the value is zero. Base Description Parameters lists inherited fields from each base; All Parameters lists the effective parameter set for this description.

## Base Description Parameters

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

## All Parameters

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
No label | GRASS_MAT_PREVIEW | MATPREVIEW |  |  |  | 
Icon File / ID | ID_BASELIST_ICON_FILE | TEXTURE |  |  |  | 
Icon Color | ID_BASELIST_ICON_COLORIZE_MODE | BOOL |  |  |  | 
Color | ID_BASELIST_ICON_COLOR | COLOR |  |  | 1.0 0.9 0.4 | 
No label | ID_BASELIST_ICON_PRESET_BUTTONS | ICONCHOOSER |  |  |  | 
Name | ID_BASELIST_NAME | STRING |  |  |  | 
Layer | ID_LAYER_LINK | LINK |  |  |  | 
No label | ID_BASELIST_NODESPACE_ADD_REMOVE_BUTTONS | NODESPACE_ADD_REMOVE |  |  |  | 
No label | MATERIAL_PAGE_PROPERTIES | BOOL |  |  |  | 
Color | GRASS_COLOR | GRADIENT |  |  |  | 
Color Texture | GRASS_COLOR_VAR_SHD | SHADERLINK |  |  |  | 
Mix Strength | GRASS_INHERITCOL | REAL | 0.0 | 100.0 |  | 
Blade Length | GRASS_LENGTH | REAL | 0.0 |  |  | 
Blade Width | GRASS_WIDTH | REAL | 0.0 |  |  | 
Density | GRASS_DENSITY | REAL | 0.0 |  |  | 
Density Texture | GRASS_DENSITY_SHD | SHADERLINK |  |  |  | 
Segments | GRASS_SEGMENTS | LONG | 1 | 100 |  | 
Crinkle | GRASS_STYLE_1 | REAL | 0.0 | 100.0 |  | 
Bend | GRASS_STYLE_2 | REAL | 0.0 | 100.0 |  | 
Wetness | GRASS_SPECULAR | REAL | 0.0 | 100.0 |  | 
No label | GRASS_ASSIGN | MATASSIGN |  |  |  | 
