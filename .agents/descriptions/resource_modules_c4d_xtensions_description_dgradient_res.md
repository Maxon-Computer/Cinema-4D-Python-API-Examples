# Description: Gradient Datatype

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/c4d_xtensions/description/dgradient.res`
- **Symbol:** `Dgradient`
- **Category:** Other

Use parameter symbols to access parameters and cycle option symbols for cycle values, never their numeric IDs. Treat Min and Max as constraints and Default as the declared initial value; blank cells mean the resource does not declare that metadata, not that the value is zero. Base Description Parameters lists inherited fields from each base; All Parameters lists the effective parameter set for this description.

## Base Description Parameters

No base descriptions.

## All Parameters

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Interpolation | GRADIENTSUBCHANNEL_INTERPOLATION | LONG |  |  |  | GRADIENTSUBCHANNEL_INTERPOLATION_SMOOTHKNOT; GRADIENTSUBCHANNEL_INTERPOLATION_CUBICKNOT; GRADIENTSUBCHANNEL_INTERPOLATION_LINEARKNOT; GRADIENTSUBCHANNEL_INTERPOLATION_NONE; GRADIENTSUBCHANNEL_INTERPOLATION_BLEND; GRADIENTSUBCHANNEL_INTERPOLATION_EXP_UP; GRADIENTSUBCHANNEL_INTERPOLATION_EXP_DOWN
