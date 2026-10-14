# Description: Field Entry

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/c4d_xtensions/description/desc_fieldentry.res`
- **Symbol:** `Desc_fieldentry`
- **Category:** Other

Use parameter symbols to access parameters and cycle option symbols for cycle values, never their numeric IDs. Treat Min and Max as constraints and Default as the declared initial value; blank cells mean the resource does not declare that metadata, not that the value is zero. Base Description Parameters lists inherited fields from each base; All Parameters lists the effective parameter set for this description.

## Base Description Parameters

No base descriptions.

## All Parameters

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Enabled | FIELDENTRY_ENABLED | BOOL |  |  |  | 
Falloff | FIELDENTRY_LINK | LINK |  |  |  | 
Strength | FIELDENTRY_STRENGTH | REAL |  |  |  | 
Blend Mode | FIELDENTRY_MODE | LONG |  |  |  | FIELDENTRY_MODE_NORMAL; FIELDENTRY_MODE_ADD; FIELDENTRY_MODE_LIGHTEN; FIELDENTRY_MODE_MULTIPLY; FIELDENTRY_MODE_COLORDODGE; FIELDENTRY_MODE_LINEARDODGE; FIELDENTRY_MODE_SUBTRACT; FIELDENTRY_MODE_DARKEN; FIELDENTRY_MODE_SCREEN; FIELDENTRY_MODE_COLORBURN; FIELDENTRY_MODE_LINEARBURN; FIELDENTRY_MODE_OVERLAY; FIELDENTRY_MODE_SOFTLIGHT; FIELDENTRY_MODE_HARDLIGHT; FIELDENTRY_MODE_LINEARLIGHT; FIELDENTRY_MODE_VIVIDLIGHT; FIELDENTRY_MODE_PINLIGHT; FIELDENTRY_MODE_GLOW; FIELDENTRY_MODE_AVERAGE; FIELDENTRY_MODE_DIFFERENCE; FIELDENTRY_MODE_NEGATION; FIELDENTRY_MODE_EXCLUSION; FIELDENTRY_MODE_PHOENIX; FIELDENTRY_MODE_REFLECT; FIELDENTRY_MODE_HARDMIX; FIELDENTRY_MODE_LEVR; FIELDENTRY_MODE_COLOR; FIELDENTRY_MODE_COLOR_INV
Color Mode | FIELDENTRY_COLORMODE | LONG |  |  |  | FIELDENTRY_COLORMODE_PASS; FIELDENTRY_COLORMODE_COLOR; FIELDENTRY_COLORMODE_GRADIENT
Color | FIELDENTRY_COLOR | COLOR |  |  |  | 
Gradient | FIELDENTRY_GRADIENT | GRADIENT |  |  |  | 
