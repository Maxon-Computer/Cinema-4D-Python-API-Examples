# Description: Value Key

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/c4d_base/description/ckvalue.res`
- **Symbol:** `CKvalue`
- **Category:** Other

Use parameter symbols to access parameters and cycle option symbols for cycle values, never their numeric IDs. Treat Min and Max as constraints and Default as the declared initial value; blank cells mean the resource does not declare that metadata, not that the value is zero. Base Description Parameters lists inherited fields from each base; All Parameters lists the effective parameter set for this description.

## Base Description Parameters

No base descriptions.

## All Parameters

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Quaternion Interpolation | ID_CKEY_QUAT_INTER | LONG |  |  |  | ID_CKEY_QUAT_LINEAR; ID_CKEY_QUAT_CUBIC
Type | ID_CKEY_INTER | LONG |  |  |  | ID_CKEY_SPLINE; ID_CKEY_LINEAR; ID_CKEY_STEP
Mute | ID_VKEY_MUTE | BOOL |  |  |  | 
Key Time | ID_VKEY_TIME | BASETIME |  |  |  | 
Key Value | ID_CKEY_VALUE | REAL |  |  |  | 
No label | ID_CKEY_VALUE_TIME | BASETIME |  |  |  | 
Lock Time | ID_VKEY_LOCK_T | BOOL |  |  |  | 
Lock Value | ID_CKEY_LOCK_V | BOOL |  |  |  | 
Breakdown | ID_VKEY_BREAKDOWN | BOOL |  |  |  | 
Breakdown Color | ID_VKEY_BREAKDOWNCOLOR | BOOL |  |  |  | 
Tangent Preset | ID_CKEY_PRESET | LONG |  |  |  | ID_CKEY_PRESET_AUTO_CLAMP; ID_CKEY_PRESET_AUTO_OVERSHOOT; ID_CKEY_PRESET_AUTO_OVERSHOOTWEIGHTED; ID_CKEY_PRESET_FIXED_OVERSHOOTWEIGHTED; ID_CKEY_PRESET_CUSTOM
Auto Tangents | ID_CKEY_AUTO | BOOL |  |  |  | 
Clamp | ID_CKEY_CLAMP | BOOL |  |  |  | 
Angle | ID_CKEY_AUTOMODE | LONG |  |  |  | ID_CKEY_CLASSIC; ID_CKEY_FIXEDSLOPE
Remove Overshooting | ID_CKEY_REMOVEOVERSHOOT | BOOL |  |  |  | 
Weighted Tangent | ID_CKEY_WEIGHTEDTANGENT | BOOL |  |  |  | 
Automatic Weighting | ID_CKEY_AUTOWEIGHT | BOOL |  |  |  | 
Left  Time | ID_CKEY_TIME_LEFT | BASETIME |  | 0.0 |  | 
Right Time | ID_CKEY_TIME_RIGHT | BASETIME | 0.0 |  |  | 
Left  Value | ID_CKEY_VALUE_LEFT | REAL |  |  |  | 
Right Value | ID_CKEY_VALUE_RIGHT | REAL |  |  |  | 
Lock Tangent Angles | ID_CKEY_LOCK_O | BOOL |  |  |  | 
Lock Tangent Lengths | ID_CKEY_LOCK_L | BOOL |  |  |  | 
Break Tangents | ID_CKEY_BREAK | BOOL |  |  |  | 
Keep Visual Angle | ID_CKEY_KEEPVISUALANGLE | BOOL |  |  |  | 
