# Description: SketchUp Importer Settings

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/io_skp/description/fskpimport.res`
- **Symbol:** `Fskpimport`
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
Daylight System / Physical Sky | SKPIMPORT_DAYLIGHT_SYSTEM_PHYSICAL_SKY | BOOL |  |  | 0 | 
Camera | SKPIMPORT_CAMERA | BOOL |  |  | 0 | 
Skip Hidden Objects | SKPIMPORT_SKIP_HIDDEN_OBJECTS | BOOL |  |  | 0 | 
Split Objects by Layer | SKPIMPORT_SPLIT_OBJECTS_BY_LAYER | BOOL |  |  | 0 | 
Show Statistics in Console | SKPIMPORT_SHOW_STATISTICS_IN_CONSOLE | BOOL |  |  | 0 | 
