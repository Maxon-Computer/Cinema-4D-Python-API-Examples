# Description: Tween Tool

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/ca/description/tooltween.res`
- **Symbol:** `Tooltween`
- **Category:** Other

Use parameter symbols to access parameters and cycle option symbols for cycle values, never their numeric IDs. Treat Min and Max as constraints and Default as the declared initial value; blank cells mean the resource does not declare that metadata, not that the value is zero. Base Description Parameters lists inherited fields from each base; All Parameters lists the effective parameter set for this description.

## Base Description Parameters

### Base Tool (`ToolBase`)

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Realtime Update | MDATA_INTERACTIVE | BOOL |  |  |  | 
    Apply     | MDATA_APPLY | BUTTON |  |  |  | 
New Transform | MDATA_NEWTRANSFORM | BUTTON |  |  |  | 
No label | ID_SNAPSETTINGS | SUBCONTAINER |  |  |  | 

## All Parameters

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Realtime Update | MDATA_INTERACTIVE | BOOL |  |  |  | 
    Apply     | MDATA_APPLY | BUTTON |  |  |  | 
New Transform | MDATA_NEWTRANSFORM | BUTTON |  |  |  | 
No label | ID_SNAPSETTINGS | SUBCONTAINER |  |  |  | 
Tween | ID_CA_TWEEN_VALUE | REAL | -100.0 | 100.0 |  | 
-90 % | ID_CA_TWEEN_STEPL3 | BUTTON |  |  |  | 
-75 % | ID_CA_TWEEN_STEPL2 | BUTTON |  |  |  | 
-50 % | ID_CA_TWEEN_STEPL1 | BUTTON |  |  |  | 
0 % | ID_CA_TWEEN_MID | BUTTON |  |  |  | 
+50 % | ID_CA_TWEEN_STEPR1 | BUTTON |  |  |  | 
+75 % | ID_CA_TWEEN_STEPR2 | BUTTON |  |  |  | 
+90 % | ID_CA_TWEEN_STEPR3 | BUTTON |  |  |  | 
Set n | ID_CA_RETIME_FRAME_AMOUNT | BASETIME | 0 |  |  | 
-n | ID_CA_RETIME_SUBSTRACT | BUTTON |  |  |  | 
-1 | ID_CA_RETIME_SUBSTRACT_ONE | BUTTON |  |  |  | 
+1 | ID_CA_RETIME_ADD_ONE | BUTTON |  |  |  | 
+n | ID_CA_RETIME_ADD | BUTTON |  |  |  | 
&#92;u2590 +n &#92;u2B05 | ID_CA_RETIME_SET | BUTTON |  |  |  | 
Position | ID_CA_TWEEN_POSITION | BOOL |  |  |  | 
Rotation | ID_CA_TWEEN_ROTATION | BOOL |  |  |  | 
Scale | ID_CA_TWEEN_SCALING | BOOL |  |  |  | 
Parameters | ID_CA_TWEEN_OTHERS | BOOL |  |  |  | 
User Data | ID_CA_TWEEN_USERDATA | BOOL |  |  |  | 
Tags | ID_CA_TWEEN_TAGS | BOOL |  |  |  | 
Selected Tracks | ID_CA_TWEEN_KEYFRAMESEL | BOOL |  |  |  | 
Linear | ID_CA_TWEEN_LINEAR | BOOL |  |  |  | 
HUD | ID_CA_TWEEN_ENABLE_VIEWPORT_BAR | BOOL |  |  |  | 
Global Space Mode | ID_CA_TWEEN_GLOBAL_MODE | BOOL |  |  |  | 
