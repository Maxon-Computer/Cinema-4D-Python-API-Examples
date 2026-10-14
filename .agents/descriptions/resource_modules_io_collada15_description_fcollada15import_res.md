# Description: COLLADA 1.5 Import Settings

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/io_collada15/description/FCollada15Import.res`
- **Symbol:** `FCollada15Import`
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
Spline Subdivision Factor | COLLADA_IMPORT_SPLINE_SUBDIVISION_FACTOR | LONG | 1 |  |  | 
2D Geometry | COLLADA_IMPORT_2D_GEOMETRY | BOOL |  |  |  | 
Animation | COLLADA_IMPORT_ANIMATION | BOOL |  |  |  | 
Fix Transparency | COLLADA_IMPORT_FORCE_TRANSPARENCY_OPAQUE_MODE_TO_RGB_ZERO | BOOL |  |  |  | 
