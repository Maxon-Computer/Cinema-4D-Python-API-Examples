# Description: Allplan Export Settings

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/interop_misc/description/allplan.res`
- **Symbol:** `Allplan`
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
Scale | ALLPLAN_SIZE | UNITSCALE |  |  |  | 
Save Selected | ALLPLAN_SELECTED | BOOL |  |  | 0 | 
Triangulate | ALLPLAN_TRI | BOOL |  |  | 0 | 
Optimize | ALLPLAN_OTPIMIZE | BOOL |  |  | 1 | 
Optimize Tolerance | ALLPLAN_OPTIMIZEVALUE | REAL | 0.0 |  | 0.01 | 
Clear Degenerated Polygons | ALLPLAN_COLLAPSED | BOOL |  |  | 1 | 
Color | ALLPLAN_COLOR | BOOL |  |  | 0 | 
Small Format | ALLPLAN_KOMPRIMIERT | BOOL |  |  | 1 | 
Create Log File | ALLPLAN_INFO | BOOL |  |  | 0 | 
