# Description: Volume Export Settings

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/volumes/description/fvdbexport.res`
- **Symbol:** `Fvdbexport`
- **Category:** Files

Use parameter symbols to access parameters and cycle option symbols for cycle values, never their numeric IDs. Treat Min and Max as constraints and Default as the declared initial value; blank cells mean the resource does not declare that metadata, not that the value is zero. Base Description Parameters lists inherited fields from each base; All Parameters lists the effective parameter set for this description.

## Base Description Parameters

### Filter (`Fbase`)

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Presets | PRESET_OPTIONS_PRESETS | LONG |  |  | 0 | 
Save... | PRESET_OPTIONS_PRESETS_CUSTOM_SAVEBUTTON | BUTTON |  |  |  | 
Delete... | PRESET_OPTIONS_PRESETS_CUSTOM_DELETEBUTTON | BUTTON |  |  |  | 

## All Parameters

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Presets | PRESET_OPTIONS_PRESETS | LONG |  |  | 0 | 
Save... | PRESET_OPTIONS_PRESETS_CUSTOM_SAVEBUTTON | BUTTON |  |  |  | 
Delete... | PRESET_OPTIONS_PRESETS_CUSTOM_DELETEBUTTON | BUTTON |  |  |  | 
Scale | VDBEXPORT_UNIT_SCALE | UNITSCALE |  |  |  | 
Animation | VDBEXPORT_ANIMATION | BOOL |  |  |  | 
Name | VDBEXPORT_NAMEFORMAT | LONG |  |  |  | VDBEXPORT_NAMEFORMAT_0; VDBEXPORT_NAMEFORMAT_1; VDBEXPORT_NAMEFORMAT_2; VDBEXPORT_NAMEFORMAT_3; VDBEXPORT_NAMEFORMAT_4; VDBEXPORT_NAMEFORMAT_5
From | VDBEXPORT_FRAME_START | LONG | 0 |  |  | 
To | VDBEXPORT_FRAME_END | LONG | 0 |  |  | 
Selected Only | VDBEXPORT_SELECTED | BOOL |  |  |  | 
