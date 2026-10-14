# Description: Volume Import Settings

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/volumes/description/fvdbimport.res`
- **Symbol:** `Fvdbimport`
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
Volume Grids | VDBIMPORT_GRIDS_LISTVIEW | LISTVIEW |  |  |  | 
Scale | VDBIMPORT_UNIT_SCALE | UNITSCALE |  |  |  | 
Animation | VDBIMPORT_ANIMATION | BOOL |  |  |  | 
From | VDBIMPORT_FRAME_START | LONG | 0 |  |  | 
To | VDBIMPORT_FRAME_END | LONG | 0 |  |  | 
Group Objects | VDBIMPORT_GROUP_OBJECTS | BOOL |  |  |  | 
Import to Project Location | VDBIMPORT_RELATIVE | BOOL |  |  |  | 
