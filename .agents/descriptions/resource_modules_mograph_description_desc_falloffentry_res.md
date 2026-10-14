# Description: MoGraph Falloff Shader

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/mograph/description/desc_falloffentry.res`
- **Symbol:** `Desc_falloffentry`
- **Category:** Other

Use parameter symbols to access parameters and cycle option symbols for cycle values, never their numeric IDs. Treat Min and Max as constraints and Default as the declared initial value; blank cells mean the resource does not declare that metadata, not that the value is zero. Base Description Parameters lists inherited fields from each base; All Parameters lists the effective parameter set for this description.

## Base Description Parameters

No base descriptions.

## All Parameters

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Enabled | FALLOFFENTRY_ENABLED | BOOL |  |  |  | 
Falloff | FALLOFFENTRY_LINK | LINK |  |  |  | 
Strength | FALLOFFENTRY_STRENGTH | REAL |  |  |  | 
Blend Mode | FALLOFFENTRY_MODE | LONG |  |  |  | FALLOFFENTRY_MODE_NORMAL; FALLOFFENTRY_MODE_ADD; FALLOFFENTRY_MODE_LIGHTEN; FALLOFFENTRY_MODE_MULTIPLY; FALLOFFENTRY_MODE_COLORDODGE; FALLOFFENTRY_MODE_LINEARDODGE; FALLOFFENTRY_MODE_SUBTRACT; FALLOFFENTRY_MODE_DARKEN; FALLOFFENTRY_MODE_SCREEN; FALLOFFENTRY_MODE_COLORBURN; FALLOFFENTRY_MODE_LINEARBURN; FALLOFFENTRY_MODE_OVERLAY; FALLOFFENTRY_MODE_SOFTLIGHT; FALLOFFENTRY_MODE_HARDLIGHT; FALLOFFENTRY_MODE_LINEARLIGHT; FALLOFFENTRY_MODE_VIVIDLIGHT; FALLOFFENTRY_MODE_PINLIGHT; FALLOFFENTRY_MODE_GLOW; FALLOFFENTRY_MODE_AVERAGE; FALLOFFENTRY_MODE_DIFFERENCE; FALLOFFENTRY_MODE_NEGATION; FALLOFFENTRY_MODE_EXCLUSION; FALLOFFENTRY_MODE_PHOENIX; FALLOFFENTRY_MODE_REFLECT; FALLOFFENTRY_MODE_HARDMIX; FALLOFFENTRY_MODE_LEVR; FALLOFFENTRY_MODE_COLOR; FALLOFFENTRY_MODE_COLOR_INV
Color Mode | FALLOFFENTRY_COLORMODE | LONG |  |  |  | FALLOFFENTRY_COLORMODE_PASS; FALLOFFENTRY_COLORMODE_COLOR; FALLOFFENTRY_COLORMODE_GRADIENT
Color | FALLOFFENTRY_COLOR | COLOR |  |  |  | 
Gradient | FALLOFFENTRY_GRADIENT | GRADIENT |  |  |  | 
