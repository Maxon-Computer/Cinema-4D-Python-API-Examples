# Description: Freeze

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/mograph/description/flproximity.res`
- **Symbol:** `FLproximity`
- **Category:** Other

Use parameter symbols to access parameters and cycle option symbols for cycle values, never their numeric IDs. Treat Min and Max as constraints and Default as the declared initial value; blank cells mean the resource does not declare that metadata, not that the value is zero. Base Description Parameters lists inherited fields from each base; All Parameters lists the effective parameter set for this description.

## Base Description Parameters

### Layer Controls (`FLbase`)

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Enabled | ID_FIELDLAYER_ENABLED | BOOL |  |  |  | 
Value | ID_FIELDLAYER_ENABLE_VALUE | BOOL |  |  |  | 
Color | ID_FIELDLAYER_ENABLE_COLOR | BOOL |  |  |  | 
Direction | ID_FIELDLAYER_ENABLE_DIRECTION | BOOL |  |  |  | 
Rotation | ID_FIELDLAYER_ENABLE_ROTATION | BOOL |  |  |  | 
Layer Opacity | ID_FIELDLAYER_STRENGTH | REAL | 0.0 | 100.0 |  | 
Layer Blending | ID_FIELDLAYER_BLENDINGMODE | LONG |  |  |  | ID_FIELDLAYER_BLENDINGMODE_NORMAL; ID_FIELDLAYER_BLENDINGMODE_DARKEN; ID_FIELDLAYER_BLENDINGMODE_TRUESUBTRACT; ID_FIELDLAYER_BLENDINGMODE_MULTIPLY; ID_FIELDLAYER_BLENDINGMODE_OVERLAY; ID_FIELDLAYER_BLENDINGMODE_LIGHTEN; ID_FIELDLAYER_BLENDINGMODE_ADD; ID_FIELDLAYER_BLENDINGMODE_SCREEN; ID_FIELDLAYER_BLENDINGMODE_LAYERMASK

## All Parameters

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Enabled | ID_FIELDLAYER_ENABLED | BOOL |  |  |  | 
Value | ID_FIELDLAYER_ENABLE_VALUE | BOOL |  |  |  | 
Color | ID_FIELDLAYER_ENABLE_COLOR | BOOL |  |  |  | 
Direction | ID_FIELDLAYER_ENABLE_DIRECTION | BOOL |  |  |  | 
Rotation | ID_FIELDLAYER_ENABLE_ROTATION | BOOL |  |  |  | 
Layer Opacity | ID_FIELDLAYER_STRENGTH | REAL | 0.0 | 100.0 |  | 
Layer Blending | ID_FIELDLAYER_BLENDINGMODE | LONG |  |  |  | ID_FIELDLAYER_BLENDINGMODE_NORMAL; ID_FIELDLAYER_BLENDINGMODE_DARKEN; ID_FIELDLAYER_BLENDINGMODE_TRUESUBTRACT; ID_FIELDLAYER_BLENDINGMODE_MULTIPLY; ID_FIELDLAYER_BLENDINGMODE_OVERLAY; ID_FIELDLAYER_BLENDINGMODE_LIGHTEN; ID_FIELDLAYER_BLENDINGMODE_ADD; ID_FIELDLAYER_BLENDINGMODE_SCREEN; ID_FIELDLAYER_BLENDINGMODE_LAYERMASK
Freeze | FIELDLAYER_PROXIMITY_FORCE_SAVE | BUTTON |  |  |  | 
Clear | FIELDLAYER_PROXIMITY_FORCE_CLEAR | BUTTON |  |  |  | 
Mode | FIELDLAYER_PROXIMITY_MODE | LONG |  |  |  | FIELDLAYER_PROXIMITY_MODE_NONE; FIELDLAYER_PROXIMITY_MODE_MAX; FIELDLAYER_PROXIMITY_MODE_MIN; FIELDLAYER_PROXIMITY_MODE_AVG; FIELDLAYER_PROXIMITY_MODE_GROW
Auto-Update | FIELDLAYER_PROXIMITY_DYNAMIC_UPDATE | BOOL |  |  |  | 
Subfields Only | FIELDLAYER_PROXIMITY_SELF_AGGREGATE | BOOL |  |  |  | 
Optimize Search Tree | FIELDLAYER_PROXIMITY_USE_INPUT_CRC | BOOL |  |  |  | 
Radius | FIELDLAYER_PROXIMITY_RADIUS | REAL | 0.0 |  |  | 
Effect Strength | FIELDLAYER_PROXIMITY_EFFECT_RATIO | REAL | 0.0 |  |  | 
Radius | FIELDLAYER_PROXIMITY_FIELDS | FIELDLIST |  |  |  | 
