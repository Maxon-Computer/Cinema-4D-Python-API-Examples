# Description: Waypoint

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/c4d_manager/description/twaypoint.res`
- **Symbol:** `Twaypoint`
- **Category:** Other

Use parameter symbols to access parameters and cycle option symbols for cycle values, never their numeric IDs. Treat Min and Max as constraints and Default as the declared initial value; blank cells mean the resource does not declare that metadata, not that the value is zero. Base Description Parameters lists inherited fields from each base; All Parameters lists the effective parameter set for this description.

## Base Description Parameters

No base descriptions.

## All Parameters

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Weight | ID_ANIM_OWAYPOINT_SETTINGS_WEIGHT | REAL | 0.0 |  |  | 
Freedom | ID_ANIM_OWAYPOINT_SETTINGS_FREEDOM | REAL | 0.0 | 150.0 |  | 
Freedom Overwrite | ID_ANIM_OWAYPOINT_SETTINGS_FREEDOM_OVERWRITE | BOOL |  |  |  | 
Freedom In | ID_ANIM_OWAYPOINT_SETTINGS_FREEDOMIN | REAL | 0.0 | 150.0 |  | 
Freedom Out | ID_ANIM_OWAYPOINT_SETTINGS_FREEDOMOUT | REAL | 0.0 | 150.0 |  | 
Rest | ID_ANIM_OWAYPOINT_SETTINGS_WAITTIME | REAL | 0.0 |  |  | 
Move In | ID_ANIM_OWAYPOINT_SETTINGS_MOVEIN | REAL | 0.0 |  |  | 
Move Out | ID_ANIM_OWAYPOINT_SETTINGS_MOVEOUT | REAL | 0.0 |  |  | 
Timing | ID_ANIM_OWAYPOINT_SETTINGS_TIME_INTERPOLATION | LONG |  |  |  | ID_ANIM_OWAYPOINT_SETTINGS_TIME_INTERPOLATION_DEFAULT; ID_ANIM_OWAYPOINT_SETTINGS_TIME_INTERPOLATION_EASYEASE; ID_ANIM_OWAYPOINT_SETTINGS_TIME_INTERPOLATION_EASEIN; ID_ANIM_OWAYPOINT_SETTINGS_TIME_INTERPOLATION_EASEOUT
Timing Influence | ID_ANIM_OWAYPOINT_SETTINGS_TIME_INTERPOLATION_FACTOR | REAL |  |  | 1 | 
