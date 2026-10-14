# Description: Spline Field Layer

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/mograph/description/flspline.res`
- **Symbol:** `FLspline`
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
Spline Object | FIELDLAYER_SPLINE_OBJECT | LINK |  |  |  | 
Spline Shape | FIELDLAYER_SPLINE_SHAPE | LONG |  |  |  | FIELDLAYER_SPLINE_SHAPE_CURVE; FIELDLAYER_SPLINE_SHAPE_MASK
Distance Mode | FIELDLAYER_SPLINE_DISTANCEMODE | LONG |  |  |  | FIELDLAYER_SPLINE_DISTANCEMODE_ALONG; FIELDLAYER_SPLINE_DISTANCEMODE_RADIUS; FIELDLAYER_SPLINE_DISTANCEMODE_BOTH
Radius | FIELDLAYER_SPLINE_DISTANCE | REAL | 0.0 |  |  | 
Clip to Shape | FIELDLAYER_SPLINE_CLIP | BOOL |  |  |  | 
Radius Falloff | FIELDLAYER_SPLINE_RADIUSCURVE | SPLINE |  |  |  | 
Segments | FIELDLAYER_SPLINE_ALONGMODE | LONG |  |  |  | FIELDLAYER_SPLINE_ALONGMODE_WHOLE; FIELDLAYER_SPLINE_ALONGMODE_PERSEGMENT
Range Start | FIELDLAYER_SPLINE_RANGE_START | REAL | 0.0 | 100.0 |  | 
Range End | FIELDLAYER_SPLINE_RANGE_END | REAL | 0.0 | 100.0 |  | 
Offset | FIELDLAYER_SPLINE_OFFSET | REAL |  |  |  | 
Along Curve Falloff | FIELDLAYER_SPLINE_ALONGCURVE | SPLINE |  |  |  | 
Cycle | FIELDLAYER_SPLINE_ALONGCURVECYCLE | BOOL |  |  |  | 
Mask Projection | FIELDLAYER_SPLINE_PROJECTION | LONG |  |  |  | FIELDLAYER_SPLINE_PROJECTION_X; FIELDLAYER_SPLINE_PROJECTION_Y; FIELDLAYER_SPLINE_PROJECTION_Z
Mask Falloff | FIELDLAYER_SPLINE_MASKFALLOFF | LONG |  |  |  | FIELDLAYER_SPLINE_MASKFALLOFF_INSIDE; FIELDLAYER_SPLINE_MASKFALLOFF_OUTSIDE
Distance | FIELDLAYER_SPLINE_MASK_DISTANCE | REAL | 0.0 |  |  | 
Clip to Shape | FIELDLAYER_SPLINE_MASK_CLIP | BOOL |  |  |  | 
