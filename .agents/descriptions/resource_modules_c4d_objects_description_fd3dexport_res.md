# Description: Direct 3D Export Settings

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/c4d_objects/description/fd3dexport.res`
- **Symbol:** `Fd3dexport`
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
Scale | D3DEXPORTFILTER_SCALE | UNITSCALE |  |  |  | 
Format | D3DEXPORTFILTER_FORMAT | BOOL |  |  | 1 | 
Save Templates | D3DEXPORTFILTER_TEMPLATES | BOOL |  |  | 1 | 
Export Textures | D3DEXPORTFILTER_TEXTURES | BOOL |  |  | 1 | 
Save Normals | D3DEXPORTFILTER_NORMALS | BOOL |  |  | 1 | 
Generate Mesh | D3DEXPORTFILTER_SAVEMESH | BOOL |  |  | 1 | 
Adapt Textures | D3DEXPORTFILTER_CONVERTTEXTURENAME | BOOL |  |  | 1 | 
Suffix | D3DEXPORTFILTER_TEXTURESUFFIX | STRING |  |  |  | 
