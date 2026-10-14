# Description: Adobe PDF Illustrator Import Settings

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/mograph/description/faipdfimport.res`
- **Symbol:** `Faipdfimport`
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
Scale | AIIMPORTFILTER_SCALE | UNITSCALE |  |  |  | 
Create Vector Object | AIIMPORTFILTER_CREATE_VECTOROBJECT | BOOL |  |  | 1 | 
Force PDF | AIIMPORTFILTER_FORCE_PDF | BOOL |  |  | 0 | 
Greedy Fill | AIIMPORTFILTER_GREEDY_FILL | BOOL |  |  | 0 | 
