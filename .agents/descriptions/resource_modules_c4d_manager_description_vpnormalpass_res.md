# Description: Normal Pass

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/c4d_manager/description/vpnormalpass.res`
- **Symbol:** `vpnormalpass`
- **Category:** Video Posts

Use parameter symbols to access parameters and cycle option symbols for cycle values, never their numeric IDs. Treat Min and Max as constraints and Default as the declared initial value; blank cells mean the resource does not declare that metadata, not that the value is zero. Base Description Parameters lists inherited fields from each base; All Parameters lists the effective parameter set for this description.

## Base Description Parameters

### Post Effect (`VPbase`)

No parameters.

## All Parameters

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Space | VP_NORMALPASS_SPACE | LONG |  |  |  | VP_NORMALPASS_SPACE_WORLD; VP_NORMALPASS_SPACE_CAMERA; VP_NORMALPASS_SPACE_OBJECT
Channel Order | VP_NORMALPASS_FLIP | LONG |  |  |  | VP_NORMALPASS_FLIP_RGB; VP_NORMALPASS_FLIP_RBG; VP_NORMALPASS_FLIP_GBR; VP_NORMALPASS_FLIP_GRB; VP_NORMALPASS_FLIP_BGR; VP_NORMALPASS_FLIP_BRG
Invert Z | VP_NORMALPASS_INVERTZ | BOOL |  |  |  | 
