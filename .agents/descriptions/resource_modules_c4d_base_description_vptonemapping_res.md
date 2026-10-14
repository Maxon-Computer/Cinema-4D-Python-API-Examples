# Description: Tone Mapping

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/c4d_base/description/vptonemapping.res`
- **Symbol:** `VPtonemapping`
- **Category:** Video Posts

Use parameter symbols to access parameters and cycle option symbols for cycle values, never their numeric IDs. Treat Min and Max as constraints and Default as the declared initial value; blank cells mean the resource does not declare that metadata, not that the value is zero. Base Description Parameters lists inherited fields from each base; All Parameters lists the effective parameter set for this description.

## Base Description Parameters

### Post Effect (`VPbase`)

No parameters.

## All Parameters

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Operator | VP_TONEMAPPING_OPERATOR | LONG |  |  |  | VP_TONEMAPPING_LINEAR; VP_TONEMAPPING_PHOTOLINEAR; VP_TONEMAPPING_AUTOLINEAR; VP_TONEMAPPING_MAXWHITE; VP_TONEMAPPING_REINHARD02
Scale | VP_TONEMAPPING_SCALE | REAL | 0 |  |  | 
Exposure | VP_TONEMAPPING_EXPOSURE | REAL | 0 |  |  | 
ISO | VP_TONEMAPPING_SENSITIVITY | REAL | 0 |  |  | 
F-Stop | VP_TONEMAPPING_FSTOP | REAL | 0 |  |  | 
Gamma | VP_TONEMAPPING_GAMMA | REAL | 0 |  |  | 
Pre-Scale | VP_TONEMAPPING_PRESCALE | REAL | 0 |  |  | 
Post-Scale | VP_TONEMAPPING_POSTSCALE | REAL | 0 |  |  | 
Burn | VP_TONEMAPPING_BURN | REAL | 0 |  |  | 
To use Tone Mapping, please set the 'Depth' option to 32 Bit/Channel in the 'Save' tab. | VP_TONEMAPPING_INFO | STATICTEXT |  |  |  | 
