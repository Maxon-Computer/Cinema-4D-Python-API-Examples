# Description: Forger Export Settings

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/io_forger/description/fforgeriosaver.res`
- **Symbol:** `fforgeriosaver`
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
Scale | FORGERIO_SCALE_FACTOR_EXPORT | REAL |  |  |  | 
UVs | FORGERIO_EXPORT_UVW | BOOL |  |  |  | 
Vertex Colors | FORGERIO_EXPORT_POLYPAINT | BOOL |  |  |  | 
Polygon Groups | FORGERIO_EXPORT_POLYGROUP | BOOL |  |  |  | 
Connect With Children | FORGERIO_EXPORT_CONNECTWITHCHILDREN | BOOL |  |  |  | 
Materials | FORGERIO_EXPORT_MATERIALS | BOOL |  |  |  | 
No label | FORGERIO_EXPORT_WARNING | STRING |  |  |  | 
