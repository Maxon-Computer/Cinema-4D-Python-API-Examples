# Description: PLA Track

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/c4d_manager/description/ctpla.res`
- **Symbol:** `CTpla`
- **Category:** Tracks

Use parameter symbols to access parameters and cycle option symbols for cycle values, never their numeric IDs. Treat Min and Max as constraints and Default as the declared initial value; blank cells mean the resource does not declare that metadata, not that the value is zero. Base Description Parameters lists inherited fields from each base; All Parameters lists the effective parameter set for this description.

## Base Description Parameters

### Track (`CTbase`)

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Animation | ID_CTRACK_ANIMOFF | BOOL |  |  |  | 
Solo Animation | ID_CTRACK_ANIMSOLO | BOOL |  |  |  | 
Constant Velocity | ID_CTRACK_CONSTANTVELOCITY_V | BOOL |  |  |  | 
Before | ID_CTRACK_BEFORE | LONG |  |  |  | ID_CTRACK_OFF; ID_CTRACK_CONSTANT; ID_CTRACK_CONTINUE; ID_CTRACK_REPEAT; ID_CTRACK_OFFSETREPEAT; ID_CTRACK_OSCILLATE
Repetitions | ID_CTRACK_BEFORE_CNT | LONG | 0 |  |  | 
After | ID_CTRACK_AFTER | LONG |  |  |  | ID_CTRACK_OFF; ID_CTRACK_CONSTANT; ID_CTRACK_CONTINUE; ID_CTRACK_REPEAT; ID_CTRACK_OFFSETREPEAT; ID_CTRACK_OSCILLATE; ID_CTRACK_LOOP
Repetitions | ID_CTRACK_AFTER_CNT | LONG | 0 |  |  | 
Loop End | ID_CTRACK_TIME_LOOP_END | BASETIME |  |  |  | 
Time Track | ID_CTRACK_TIME | LINK |  |  |  | 
Relative Mapping | ID_CTRACK_TIME_RELATIVE | BOOL |  |  |  | 
Color from Preferences | ID_CTRACK_USE_PREF | BOOL |  |  |  | 
Color | ID_CTRACK_FCURVE_COLOR | COLOR |  |  |  | 
F-Curve Offset | ID_CTRACK_FCURVE_OFFSET | REAL |  |  |  | 
F-Curve Scale | ID_CTRACK_FCURVE_SCALE | REAL |  |  |  | 
R23 Evaluation | ID_CTRACK_EVALUATION_MODE | BOOL |  |  |  | 

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
Animation | ID_CTRACK_ANIMOFF | BOOL |  |  |  | 
Solo Animation | ID_CTRACK_ANIMSOLO | BOOL |  |  |  | 
Constant Velocity | ID_CTRACK_CONSTANTVELOCITY_V | BOOL |  |  |  | 
Before | ID_CTRACK_BEFORE | LONG |  |  |  | ID_CTRACK_OFF; ID_CTRACK_CONSTANT; ID_CTRACK_CONTINUE; ID_CTRACK_REPEAT; ID_CTRACK_OFFSETREPEAT; ID_CTRACK_OSCILLATE
Repetitions | ID_CTRACK_BEFORE_CNT | LONG | 0 |  |  | 
After | ID_CTRACK_AFTER | LONG |  |  |  | ID_CTRACK_OFF; ID_CTRACK_CONSTANT; ID_CTRACK_CONTINUE; ID_CTRACK_REPEAT; ID_CTRACK_OFFSETREPEAT; ID_CTRACK_OSCILLATE; ID_CTRACK_LOOP
Repetitions | ID_CTRACK_AFTER_CNT | LONG | 0 |  |  | 
Loop End | ID_CTRACK_TIME_LOOP_END | BASETIME |  |  |  | 
Time Track | ID_CTRACK_TIME | LINK |  |  |  | 
Relative Mapping | ID_CTRACK_TIME_RELATIVE | BOOL |  |  |  | 
Color from Preferences | ID_CTRACK_USE_PREF | BOOL |  |  |  | 
Color | ID_CTRACK_FCURVE_COLOR | COLOR |  |  |  | 
F-Curve Offset | ID_CTRACK_FCURVE_OFFSET | REAL |  |  |  | 
F-Curve Scale | ID_CTRACK_FCURVE_SCALE | REAL |  |  |  | 
R23 Evaluation | ID_CTRACK_EVALUATION_MODE | BOOL |  |  |  | 
