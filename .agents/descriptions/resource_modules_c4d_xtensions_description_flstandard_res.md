# Description: Field Layer

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/c4d_xtensions/description/flstandard.res`
- **Symbol:** `FLStandard`
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
Field | ID_FIELDLAYER_LINK | LINK |  |  |  | 
