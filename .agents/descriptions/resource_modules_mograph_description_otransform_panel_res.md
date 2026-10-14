# Description: Transfom Panel

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/mograph/description/otransform_panel.res`
- **Symbol:** `otransform_panel`
- **Category:** Other

Use parameter symbols to access parameters and cycle option symbols for cycle values, never their numeric IDs. Treat Min and Max as constraints and Default as the declared initial value; blank cells mean the resource does not declare that metadata, not that the value is zero. Base Description Parameters lists inherited fields from each base; All Parameters lists the effective parameter set for this description.

## Base Description Parameters

No base descriptions.

## All Parameters

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Display | ID_MG_TRANSFORM_DISPLAYMODE | LONG |  |  |  | ID_MG_TRANSFORM_DISPLAYMODE_OFF; ID_MG_TRANSFORM_DISPLAYMODE_WEIGHT; ID_MG_TRANSFORM_DISPLAYMODE_UV; ID_MG_TRANSFORM_DISPLAYMODE_COLOR; ID_MG_TRANSFORM_DISPLAYMODE_INDEX
P | ID_MG_TRANSFORM_POSITION | VECTOR |  |  |  | 
R | ID_MG_TRANSFORM_ROTATE | VECTOR |  |  |  | 
S | ID_MG_TRANSFORM_SCALE | VECTOR |  |  |  | 
Color | ID_MG_TRANSFORM_COLOR | COLOR |  |  | 0 | 
Weight | ID_MG_TRANSFORM_WEIGHT | REAL | 0.0 |  |  | 
Time | ID_MG_TRANSFORM_TIME | BASETIME |  |  |  | 
