# Description: Key Interpolation

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/c4d_manager/description/tlworld.res`
- **Symbol:** `TLWorld`
- **Category:** Other

Use parameter symbols to access parameters and cycle option symbols for cycle values, never their numeric IDs. Treat Min and Max as constraints and Default as the declared initial value; blank cells mean the resource does not declare that metadata, not that the value is zero. Base Description Parameters lists inherited fields from each base; All Parameters lists the effective parameter set for this description.

## Base Description Parameters

No base descriptions.

## All Parameters

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Overdub | TLWORLD_OVERDUB | BOOL |  |  |  | 
Type | TLWORLD_INTER | LONG |  |  |  | TLWORLD_INTER_SP; TLWORLD_INTER_LI; TLWORLD_INTER_ST
Quaternion Interpolation | TLWORLD_QUATINTER | LONG |  |  |  | TLWORLD_QUATINTER_LINEAR; TLWORLD_QUATINTER_CUBIC
Lock Time | TLWORLD_LOCKT | BOOL |  |  |  | 
Lock Value | TLWORLD_LOCKV | BOOL |  |  |  | 
Breakdown | TLWORLD_BREAKDOWN | BOOL |  |  |  | 
Breakdown Color | TLWORLD_BREAKDOWNCOLOR | BOOL |  |  |  | 
Tangent Preset | TLWORLD_PRESET | LONG |  |  |  | TLWORLD_PRESET_AUTO_CLAMP; TLWORLD_PRESET_AUTO_OVERSHOOT; TLWORLD_PRESET_AUTO_OVERSHOOTWEIGHTED; TLWORLD_PRESET_FIXED_OVERSHOOTWEIGHTED; TLWORLD_PRESET_CUSTOM
Auto Tangents | TLWORLD_AUTO | BOOL |  |  |  | 
Clamp | TLWORLD_CLAMP | BOOL |  |  |  | 
Angle | TLWORLD_AUTOTYPE | LONG |  |  |  | TLWORLD_AUTOTYPE_CLASSIC; TLWORLD_AUTOTYPE_FIXEDSLOPE
Remove Overshooting | TLWORLD_REMOVEOVERSHOOT | BOOL |  |  |  | 
Weighted Tangents | TLWORLD_WEIGHTEDTANGENT | BOOL |  |  |  | 
Automatic Weighting | TLWORLD_AUTOWEIGHT | BOOL |  |  |  | 
Lock Tangent Angles | TLWORLD_LOCKTA | BOOL |  |  |  | 
Lock Tangent Lengths | TLWORLD_LOCKTL | BOOL |  |  |  | 
Break Tangents | TLWORLD_BREAK | BOOL |  |  |  | 
Keep Visual Angle | TLWORLD_KEEPVISUALANGLE | BOOL |  |  |  | 
R23 Track Evaluation | TLWORLD_TRACKEVALMODE | BOOL |  |  |  | 
