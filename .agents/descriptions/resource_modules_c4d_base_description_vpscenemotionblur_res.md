# Description: Sub-Frame Motion Blur

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/c4d_base/description/vpscenemotionblur.res`
- **Symbol:** `VPscenemotionblur`
- **Category:** Video Posts

Use parameter symbols to access parameters and cycle option symbols for cycle values, never their numeric IDs. Treat Min and Max as constraints and Default as the declared initial value; blank cells mean the resource does not declare that metadata, not that the value is zero. Base Description Parameters lists inherited fields from each base; All Parameters lists the effective parameter set for this description.

## Base Description Parameters

### Post Effect (`VPbase`)

No parameters.

## All Parameters

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Samples | VP_SMBSUB | LONG |  |  |  | VP_SMBSUB_5; VP_SMBSUB_9; VP_SMBSUB_16; VP_SMBSUB_25; VP_SMBSUB_36; VP_SMBSUB_49
Dithering | VP_SMBDITHER | REAL | 0.0 | 100.0 |  | 
Antialiasing Restriction | VP_SMBAARESTRICTION | BOOL |  |  |  | 
Camera Offset | VP_SMBCAMERAOFFSET | BOOL |  |  |  | 
