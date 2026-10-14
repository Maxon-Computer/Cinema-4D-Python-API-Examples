# Description: Remap

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/c4d_xtensions/description/flremap.res`
- **Symbol:** `FLRemap`
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

### Field Remapper (`Fieldremapper`)

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Enable Remapping | FIELD_REMAP_ENABLE | BOOL |  |  |  | 
Mirror Graph | FIELD_REMAP_MIRROR | BOOL |  |  |  | 
No label | FIELD_PREVIEW | BITMAPBUTTON |  |  |  | 
Strength | FIELD_STRENGTH | REAL |  |  |  | 
Invert | FIELD_INVERT | BOOL |  |  |  | 
Inner Offset | FIELD_INNER_OFFSET | REAL | 0.0 | 100.0 |  | 
Min | FIELD_MIN | REAL |  |  |  | 
Clamp Min | FIELD_CLAMP_MIN | BOOL |  |  |  | 
Max | FIELD_MAX | REAL |  |  |  | 
Clamp Max | FIELD_CLAMP_MAX | BOOL |  |  |  | 
Multiplier | FIELD_MULTIPLIER | REAL |  |  |  | 
Contour Mode | FIELD_CONTOUR_MODE | LONG |  |  |  | FIELD_CONTOUR_MODE_NONE; FIELD_CONTOUR_MODE_QUAD; FIELD_CONTOUR_MODE_STEP; FIELD_CONTOUR_MODE_QUANTIZE; FIELD_CONTOUR_MODE_CURVE
Curve | FIELD_CONTOUR_CURVE | REAL | -100.0 | 100.0 |  | 
Steps | FIELD_CONTOUR_STEPS | LONG | 1 |  |  | 
Spline | FIELD_CONTOUR_SPLINE | SPLINE |  |  |  | 
Spline Animation Speed | FIELD_CONTOUR_ANIMATION_SPEED | BASETIME |  |  |  | 
Spline Offset | FIELD_CONTOUR_SPLINE_OFFSET | REAL |  |  |  | 
Spline Range | FIELD_CONTOUR_SPLINE_RANGE | REAL |  |  |  | 
Color Mode | FIELD_COLOR_MODE | LONG |  |  |  | FIELD_COLOR_MODE_OFF; FIELD_COLOR_MODE_COLOR; FIELD_COLOR_MODE_GRADIENT
Color | FIELD_COLOR | COLOR |  |  |  | 
Gradient | FIELD_GRADIENT | GRADIENT |  |  |  | 
Length | FIELD_DIRECTIONMODE | LONG |  |  |  | FIELD_DIRECTIONMODE_OFF; FIELD_DIRECTIONMODE_NORMALIZE; FIELD_DIRECTIONMODE_ATTENUATE; FIELD_DIRECTIONMODE_INVERSESQUARE
Scale | FIELD_DIRECTIONSCALE | REAL |  |  |  | 
Invert Direction | FIELD_DIRECTIONINVERT | BOOL |  |  |  | 
Strength | FIELD_ROTATIONMODE | LONG |  |  |  | FIELD_ROTATIONMODE_OFF; FIELD_ROTATIONMODE_NORMALIZE; FIELD_ROTATIONMODE_REMAP; FIELD_ROTATIONMODE_ATTENUATE; FIELD_ROTATIONMODE_INVERSESQUARE
Scale | FIELD_ROTATIONSCALE | REAL |  |  |  | 
Invert Rotations | FIELD_ROTATIONINVERT | BOOL |  |  |  | 

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
Enable Remapping | FIELD_REMAP_ENABLE | BOOL |  |  |  | 
Mirror Graph | FIELD_REMAP_MIRROR | BOOL |  |  |  | 
No label | FIELD_PREVIEW | BITMAPBUTTON |  |  |  | 
Strength | FIELD_STRENGTH | REAL |  |  |  | 
Invert | FIELD_INVERT | BOOL |  |  |  | 
Inner Offset | FIELD_INNER_OFFSET | REAL | 0.0 | 100.0 |  | 
Min | FIELD_MIN | REAL |  |  |  | 
Clamp Min | FIELD_CLAMP_MIN | BOOL |  |  |  | 
Max | FIELD_MAX | REAL |  |  |  | 
Clamp Max | FIELD_CLAMP_MAX | BOOL |  |  |  | 
Multiplier | FIELD_MULTIPLIER | REAL |  |  |  | 
Contour Mode | FIELD_CONTOUR_MODE | LONG |  |  |  | FIELD_CONTOUR_MODE_NONE; FIELD_CONTOUR_MODE_QUAD; FIELD_CONTOUR_MODE_STEP; FIELD_CONTOUR_MODE_QUANTIZE; FIELD_CONTOUR_MODE_CURVE
Curve | FIELD_CONTOUR_CURVE | REAL | -100.0 | 100.0 |  | 
Steps | FIELD_CONTOUR_STEPS | LONG | 1 |  |  | 
Spline | FIELD_CONTOUR_SPLINE | SPLINE |  |  |  | 
Spline Animation Speed | FIELD_CONTOUR_ANIMATION_SPEED | BASETIME |  |  |  | 
Spline Offset | FIELD_CONTOUR_SPLINE_OFFSET | REAL |  |  |  | 
Spline Range | FIELD_CONTOUR_SPLINE_RANGE | REAL |  |  |  | 
Color Mode | FIELD_COLOR_MODE | LONG |  |  |  | FIELD_COLOR_MODE_OFF; FIELD_COLOR_MODE_COLOR; FIELD_COLOR_MODE_GRADIENT
Color | FIELD_COLOR | COLOR |  |  |  | 
Gradient | FIELD_GRADIENT | GRADIENT |  |  |  | 
Length | FIELD_DIRECTIONMODE | LONG |  |  |  | FIELD_DIRECTIONMODE_OFF; FIELD_DIRECTIONMODE_NORMALIZE; FIELD_DIRECTIONMODE_ATTENUATE; FIELD_DIRECTIONMODE_INVERSESQUARE
Scale | FIELD_DIRECTIONSCALE | REAL |  |  |  | 
Invert Direction | FIELD_DIRECTIONINVERT | BOOL |  |  |  | 
Strength | FIELD_ROTATIONMODE | LONG |  |  |  | FIELD_ROTATIONMODE_OFF; FIELD_ROTATIONMODE_NORMALIZE; FIELD_ROTATIONMODE_REMAP; FIELD_ROTATIONMODE_ATTENUATE; FIELD_ROTATIONMODE_INVERSESQUARE
Scale | FIELD_ROTATIONSCALE | REAL |  |  |  | 
Invert Rotations | FIELD_ROTATIONINVERT | BOOL |  |  |  | 
