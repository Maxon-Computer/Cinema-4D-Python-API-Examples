# Description: Protection Tag

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/c4d_base/description/tprotection.res`
- **Symbol:** `Tprotection`
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
Position | PROTECTION_P | LONG |  |  |  | PROTECTION_NONE; PROTECTION_LOCK; PROTECTION_LIMIT
X | PROTECTION_P_X | BOOL |  |  |  | 
Min | PROTECTION_P_MIN_X | REAL |  |  |  | 
Max | PROTECTION_P_MAX_X | REAL |  |  |  | 
Y | PROTECTION_P_Y | BOOL |  |  |  | 
Min | PROTECTION_P_MIN_Y | REAL |  |  |  | 
Max | PROTECTION_P_MAX_Y | REAL |  |  |  | 
Z | PROTECTION_P_Z | BOOL |  |  |  | 
Min | PROTECTION_P_MIN_Z | REAL |  |  |  | 
Max | PROTECTION_P_MAX_Z | REAL |  |  |  | 
Rotation | PROTECTION_R | LONG |  |  |  | PROTECTION_NONE; PROTECTION_LOCK; PROTECTION_LIMIT
H | PROTECTION_R_X | BOOL |  |  |  | 
Min | PROTECTION_R_MIN_X | REAL |  |  |  | 
Max | PROTECTION_R_MAX_X | REAL |  |  |  | 
P | PROTECTION_R_Y | BOOL |  |  |  | 
Min | PROTECTION_R_MIN_Y | REAL |  |  |  | 
Max | PROTECTION_R_MAX_Y | REAL |  |  |  | 
B | PROTECTION_R_Z | BOOL |  |  |  | 
Min | PROTECTION_R_MIN_Z | REAL |  |  |  | 
Max | PROTECTION_R_MAX_Z | REAL |  |  |  | 
Scale | PROTECTION_S | LONG |  |  |  | PROTECTION_NONE; PROTECTION_LOCK; PROTECTION_LIMIT
X | PROTECTION_S_X | BOOL |  |  |  | 
Min | PROTECTION_S_MIN_X | REAL |  |  |  | 
Max | PROTECTION_S_MAX_X | REAL |  |  |  | 
Y | PROTECTION_S_Y | BOOL |  |  |  | 
Min | PROTECTION_S_MIN_Y | REAL |  |  |  | 
Max | PROTECTION_S_MAX_Y | REAL |  |  |  | 
Z | PROTECTION_S_Z | BOOL |  |  |  | 
Min | PROTECTION_S_MIN_Z | REAL |  |  |  | 
Max | PROTECTION_S_MAX_Z | REAL |  |  |  | 
Allow Expressions | PROTECTION_ALLOW_EXPRESSIONS | BOOL |  |  |  | 
Allow Viewport Duplication | PROTECTION_ALLOW_DUPLICATION | BOOL |  |  |  | 
