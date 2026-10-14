# Description: Sound Probe

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/c4d_xtensions/description/dsoundprobe.res`
- **Symbol:** `Dsoundprobe`
- **Category:** Other

Use parameter symbols to access parameters and cycle option symbols for cycle values, never their numeric IDs. Treat Min and Max as constraints and Default as the declared initial value; blank cells mean the resource does not declare that metadata, not that the value is zero. Base Description Parameters lists inherited fields from each base; All Parameters lists the effective parameter set for this description.

## Base Description Parameters

No base descriptions.

## All Parameters

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Lower Hz | SOUNDPROBESUBCHANNEL_LEFT | REAL | 0.0 | 22050.0 |  | 
Upper Hz | SOUNDPROBESUBCHANNEL_RIGHT | REAL | 0.0 | 22050.0 |  | 
Max Volume | SOUNDPROBESUBCHANNEL_TOP | REAL | 0.0 | 100.0 |  | 
Min Volume | SOUNDPROBESUBCHANNEL_BOTTOM | REAL | 0.0 | 100.0 |  | 
Color Mode | SOUNDPROBESUBCHANNEL_COLOR_MODE | LONG |  |  |  | SOUNDPROBESUBCHANNEL_COLOR_MODE_OFF; SOUNDPROBESUBCHANNEL_COLOR_MODE_SOLID; SOUNDPROBESUBCHANNEL_COLOR_MODE_HORIZONTAL; SOUNDPROBESUBCHANNEL_COLOR_MODE_VERTICAL
Color | SOUNDPROBESUBCHANNEL_COLOR | COLOR |  |  |  | 
Gradient | SOUNDPROBESUBCHANNEL_GRADIENT | GRADIENT |  |  |  | 
Hold | SOUNDPROBESUBCHANNEL_HOLD | BOOL |  |  |  | 
