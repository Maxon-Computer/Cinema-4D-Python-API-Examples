# Description: Delta Mush Tag

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/c4d_objects/description/tdeltamush.res`
- **Symbol:** `tdeltamush`
- **Category:** Tags

Use parameter symbols to access parameters and cycle option symbols for cycle values, never their numeric IDs. Treat Min and Max as constraints and Default as the declared initial value; blank cells mean the resource does not declare that metadata, not that the value is zero. Base Description Parameters lists inherited fields from each base; All Parameters lists the effective parameter set for this description.

## Base Description Parameters

### Expression (`Texpression`)

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Priority | EXPRESSION_PRIORITY | PRIORITY |  |  |  | 
Enable | EXPRESSION_ENABLE | BOOL |  |  |  | 

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
Priority | EXPRESSION_PRIORITY | PRIORITY |  |  |  | 
Enable | EXPRESSION_ENABLE | BOOL |  |  |  | 
Strength | ID_TDELTAMUSH_WEIGHT | REAL |  |  |  | 
Iterations | ID_TDELTAMUSH_SMOOTH_ITERATION | LONG | 0 |  |  | 
Smooth View | ID_TDELTAMUSH_PREV_SMOOTH | REAL |  |  |  | 
Tangent Mode | ID_TDELTAMUSH_TANGENT_TYPE | LONG |  |  |  | ID_TDELTAMUSH_TANGENT_A; ID_TDELTAMUSH_TANGENT_B; ID_TDELTAMUSH_TANGENT_C; ID_TDELTAMUSH_TANGENT_UV
Smooth Type | ID_TDELTAMUSH_WEIGHT_TYPE | LONG |  |  |  | ID_TDELTAMUSH_WEIGHT_FIX; ID_TDELTAMUSH_WEIGHT_PROPORTIONAL
Active | ID_TDELTAMUSH_WEIGHTMAP_ONOFF | BOOL |  |  |  | 
Strength Map | ID_TDELTAMUSH_WEIGHTMAP | LINK |  |  |  | 
Pin Border Points | ID_TDELTAMUSH_PIN_CORNER | BOOL |  |  |  | 
Affect Morphs | ID_TDELTAMUSH_AFFECTMORPH | BOOL |  |  |  | 
Initialize | ID_TDELTAMUSH_OBJECT_INITIAL | BUTTON |  |  |  | 
Release | ID_TDELTAMUSH_OBJECT_RESTORE | BUTTON |  |  |  | 
No label | ID_TDELTAMUSH_OBJECT_MEM | STATICTEXT |  |  |  | 
