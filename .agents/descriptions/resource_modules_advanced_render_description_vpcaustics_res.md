# Description: Caustics

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/advanced_render/description/vpcaustics.res`
- **Symbol:** `VPcaustics`
- **Category:** Video Posts

Use parameter symbols to access parameters and cycle option symbols for cycle values, never their numeric IDs. Treat Min and Max as constraints and Default as the declared initial value; blank cells mean the resource does not declare that metadata, not that the value is zero. Base Description Parameters lists inherited fields from each base; All Parameters lists the effective parameter set for this description.

## Base Description Parameters

### Post Effect (`VPbase`)

No parameters.

## All Parameters

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Surface Caustics | VPCAUSTICS_ENABLEDIFFUSE | BOOL |  |  |  | 
Volume Caustics | VPCAUSTICS_ENABLEVOLUME | BOOL |  |  |  | 
Strength | VPCAUSTICS_STRENGTH | REAL | 0.0 | 100000 |  | 
Step Size | VPCAUSTICS_STEPSIZE | REAL | 0.001 |  |  | 
Sample Radius | VPCAUSTICS_SAMPLERADIUS | REAL | 0.001 |  |  | 
Samples | VPCAUSTICS_SAMPLES | LONG | 1 | 10000 |  | 
Recompute | VPCAUSTICS_RECOMPUTE | LONG |  |  |  | VPCAUSTICS_RECOMPUTE_FIRSTTIME; VPCAUSTICS_RECOMPUTE_ALWAYS; VPCAUSTICS_RECOMPUTE_NEVER
Save Solution | VPCAUSTICS_SAVESOLUTION | BOOL |  |  |  | 
Single Animation Solution | VPCAUSTICS_CAMERASOLUTION | BOOL |  |  |  | 
