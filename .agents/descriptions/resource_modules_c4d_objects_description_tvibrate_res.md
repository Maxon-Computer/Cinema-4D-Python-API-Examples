# Description: Vibrate Expression

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/c4d_objects/description/tvibrate.res`
- **Symbol:** `Tvibrate`
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
Regular Pulse | VIBRATEEXPRESSION_REGULAR | BOOL |  |  |  | 
Relative | VIBRATEEXPRESSION_RELATIVE | BOOL |  |  |  | 
Seed | VIBRATEEXPRESSION_SEED | REAL |  |  |  | 
Enable Position | VIBRATEEXPRESSION_POS_ENABLE | BOOL |  |  |  | 
Position Amplitude | VIBRATEEXPRESSION_POS_AMPLITUDE | VECTOR |  |  |  | 
Position Frequency | VIBRATEEXPRESSION_POS_FREQUENCY | REAL | 0.0 |  |  | 
Enable Rotation | VIBRATEEXPRESSION_ROT_ENABLE | BOOL |  |  |  | 
Rotation Amplitude | VIBRATEEXPRESSION_ROT_AMPLITUDE | VECTOR |  |  |  | 
Rotation Frequency | VIBRATEEXPRESSION_ROT_FREQUENCY | REAL | 0.0 |  |  | 
Enable Scale | VIBRATEEXPRESSION_SCL_ENABLE | BOOL |  |  |  | 
Uniform Scale | VIBRATEEXPRESSION_SCL_UNIFORM | BOOL |  |  |  | 
Scale Amplitude | VIBRATEEXPRESSION_SCL_AMPLITUDE | VECTOR | 0.01 |  |  | 
Scale Frequency | VIBRATEEXPRESSION_SCL_FREQUENCY | REAL | 0.0 |  |  | 
