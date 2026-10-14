# Description: Color Correction

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/c4d_manager/description/pvfilter.res`
- **Symbol:** `pvfilter`
- **Category:** Video Posts

Use parameter symbols to access parameters and cycle option symbols for cycle values, never their numeric IDs. Treat Min and Max as constraints and Default as the declared initial value; blank cells mean the resource does not declare that metadata, not that the value is zero. Base Description Parameters lists inherited fields from each base; All Parameters lists the effective parameter set for this description.

## Base Description Parameters

### Post Effect (`VPbase`)

No parameters.

## All Parameters

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Tone Mapping | ID_PV_FILTER_TONEMAPPING | REAL | 0.0 |  |  | 
Saturation | ID_PV_FILTER_SATURATION | REAL | -100.0 | 100.0 |  | 
Brightness | ID_PV_FILTER_BRIGHTNESS | REAL | -100.0 | 100.0 |  | 
Contrast | ID_PV_FILTER_CONTRAST | REAL | -100.0 | 100.0 |  | 
Exposure | ID_PV_FILTER_EXPOSURE | REAL | -10.0 | 10.0 |  | 
Gamma | ID_PV_FILTER_GAMMA | REAL | 0.1 | 10.0 |  | 
Red | ID_PV_FILTER_RED | BOOL |  |  |  | 
Green | ID_PV_FILTER_GREEN | BOOL |  |  |  | 
Blue | ID_PV_FILTER_BLUE | BOOL |  |  |  | 
Invert | ID_PV_FILTER_INVERT | BOOL |  |  |  | 
Black Point | ID_PV_FILTER_BLACKPOINT | REAL | 0.0 | 100.0 |  | 
White Point | ID_PV_FILTER_WHITEPOINT | REAL | 0.0 | 100.0 |  | 
Grading Intensity | ID_PV_FILTER_GRAD_INTENSITY | REAL | 0.0 | 100.0 |  | 
Curve Min | ID_PV_FILTER_GRAD_MIN | REAL |  |  |  | 
Curve Max | ID_PV_FILTER_GRAD_MAX | REAL |  |  |  | 
Curve | ID_PV_FILTER_GRAD_SPLINE_RGB | SPLINE |  |  |  | 
Red | ID_PV_FILTER_GRAD_SPLINE_R | SPLINE |  |  |  | 
Green | ID_PV_FILTER_GRAD_SPLINE_G | SPLINE |  |  |  | 
Blue | ID_PV_FILTER_GRAD_SPLINE_B | SPLINE |  |  |  | 
Reset Values | ID_PV_FILTER_RESET | BUTTON |  |  |  | 
