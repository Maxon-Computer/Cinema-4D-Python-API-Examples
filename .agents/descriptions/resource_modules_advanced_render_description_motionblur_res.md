# Description: Vector Motion Blur

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/advanced_render/description/motionblur.res`
- **Symbol:** `MotionBlur`
- **Category:** Video Posts

Use parameter symbols to access parameters and cycle option symbols for cycle values, never their numeric IDs. Treat Min and Max as constraints and Default as the declared initial value; blank cells mean the resource does not declare that metadata, not that the value is zero. Base Description Parameters lists inherited fields from each base; All Parameters lists the effective parameter set for this description.

## Base Description Parameters

### Post Effect (`VPbase`)

No parameters.

## All Parameters

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Phase | MBLUR_PHASE | REAL | -100.0 | 100.0 |  | 
Density | MBLUR_DENSITY | REAL | 0.0 | 10000.0 |  | 
Samples | MBLUR_SAMPLES | LONG | 2 | 1000 |  | 
Sample Radius | MBLUR_BLUR | REAL | 0.0 | 10.0 |  | 
Weighted Trails | MBLUR_TRAILS | BOOL |  |  |  | 
Geometry Deformation | MBLUR_MESHTRACK | BOOL |  |  |  | 
