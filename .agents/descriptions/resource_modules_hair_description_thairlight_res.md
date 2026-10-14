# Description: Light

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/hair/description/thairlight.res`
- **Symbol:** `Thairlight`
- **Category:** Tags

Use parameter symbols to access parameters and cycle option symbols for cycle values, never their numeric IDs. Treat Min and Max as constraints and Default as the declared initial value; blank cells mean the resource does not declare that metadata, not that the value is zero. Base Description Parameters lists inherited fields from each base; All Parameters lists the effective parameter set for this description.

## Base Description Parameters

### Base Tag (`Tbase`)

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Expose on Object | ID_EXPOSETAB | BOOL |  |  |  | 

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
Icon File / ID | ID_BASELIST_ICON_FILE | TEXTURE |  |  |  | 
Icon Color | ID_BASELIST_ICON_COLORIZE_MODE | BOOL |  |  |  | 
Color | ID_BASELIST_ICON_COLOR | COLOR |  |  | 1.0 0.9 0.4 | 
No label | ID_BASELIST_ICON_PRESET_BUTTONS | ICONCHOOSER |  |  |  | 
Name | ID_BASELIST_NAME | STRING |  |  |  | 
Layer | ID_LAYER_LINK | LINK |  |  |  | 
No label | ID_BASELIST_NODESPACE_ADD_REMOVE_BUTTONS | NODESPACE_ADD_REMOVE |  |  |  | 
Expose on Object | ID_EXPOSETAB | BOOL |  |  |  | 
Include | HAIR_LIGHT_TAG_INCLUDE | BOOL |  |  |  | 
Shadows | HAIR_LIGHT_TAG_SHADOWS | LONG |  |  |  | HAIR_LIGHT_TAG_SHADOWS_NONE; HAIR_LIGHT_TAG_SHADOWS_SOFT
Trans. Threshold | HAIR_LIGHT_TAG_SHADOW_TRANS_ACCURACY | REAL | 0.0 | 100.0 |  | 
Depth Threshold | HAIR_LIGHT_TAG_SHADOW_DIST_ACCURACY | REAL | 0.0 |  |  | 
Antialiasing | HAIR_LIGHT_TAG_SHADOW_AA_LEVEL | LONG |  |  |  | HAIR_LIGHT_TAG_SHADOW_AA_NONE; HAIR_LIGHT_TAG_SHADOW_AA_LOW; HAIR_LIGHT_TAG_SHADOW_AA_MED; HAIR_LIGHT_TAG_SHADOW_AA_HIGH; HAIR_LIGHT_TAG_SHADOW_AA_BEST; HAIR_LIGHT_TAG_SHADOW_AA_USER
Filter | HAIR_LIGHT_TAG_SHADOW_AA_USER_LEVEL | REAL | 0.0 |  |  | 
Density | HAIR_LIGHT_TAG_SHADOW_DENSITY | REAL | 0.0 |  |  | 
Cast Density | HAIR_LIGHT_TAG_CAST_SHADOW | REAL | 0.0 |  |  | 
Sample Size | HAIR_LIGHT_TAG_SHADOW_SAMPLE_SIZE | LONG | 0 | 512 |  | 
Shadow Map | HAIR_LIGHT_TAG_SHADOWS_MAP | LONG |  |  |  | HAIR_LIGHT_TAG_SHADOWS_MAP_250; HAIR_LIGHT_TAG_SHADOWS_MAP_500; HAIR_LIGHT_TAG_SHADOWS_MAP_750; HAIR_LIGHT_TAG_SHADOWS_MAP_1000; HAIR_LIGHT_TAG_SHADOWS_MAP_1250; HAIR_LIGHT_TAG_SHADOWS_MAP_1500; HAIR_LIGHT_TAG_SHADOWS_MAP_1750; HAIR_LIGHT_TAG_SHADOWS_MAP_2000; HAIR_LIGHT_TAG_SHADOWS_MAP_CUSTOM
Resolution | HAIR_LIGHT_TAG_MAP_SIZE | LONG | 64 | 16384 |  | 
Traced Width | HAIR_LIGHT_TAG_SHADOW_WIDTH | REAL | 0.0 | 89.0 |  | 
