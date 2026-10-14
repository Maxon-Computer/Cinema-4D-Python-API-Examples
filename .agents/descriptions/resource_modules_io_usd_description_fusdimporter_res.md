# Description: USD Import Settings

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/io_usd/description/fusdimporter.res`
- **Symbol:** `fusdimporter`
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
Keep Bridge Open | USDIMPORTER_KEEPBRIDGEOPEN | BOOL |  |  | 0 | 
Cameras | USDIMPORTER_CAMERAS | BOOL |  |  | 1 | 
Geometry | USDIMPORTER_GEOMETRY | BOOL |  |  | 1 | 
Materials | USDIMPORTER_MATERIALS | BOOL |  |  | 1 | 
Instances | USDIMPORTER_INSTANCES | BOOL |  |  | 0 | 
Lights | USDIMPORTER_LIGHTUNITS | LONG |  |  | USDIMPORTER_LIGHTUNITS_NIT | USDIMPORTER_LIGHTUNITS_NONE; USDIMPORTER_LIGHTUNITS_NIT; USDIMPORTER_LIGHTUNITS_CANDELA; USDIMPORTER_LIGHTUNITS_PERCENT
Normals | USDIMPORTER_GEOMETRY_NORMALS | LONG |  |  | USDIMPORTER_GEOMETRY_NORMALS_VERTEX | USDIMPORTER_GEOMETRY_NORMALS_NONE; USDIMPORTER_GEOMETRY_NORMALS_VERTEX; USDIMPORTER_GEOMETRY_NORMALS_PHONG
Phong Angle | USDIMPORTER_GEOMETRY_PHONG_ANGLE | REAL | 0 | 180 | 40 | 
UVs | USDIMPORTER_GEOMETRY_UV | BOOL |  |  | 1 | 
Display Color | USDIMPORTER_GEOMETRY_DISPLAYCOLOR | BOOL |  |  | 1 | 
Tracks | USDIMPORTER_ANIMATION_TRS | BOOL |  |  | 1 | 
Clean Tracks | USDIMPORTER_ANIMATION_CLEANTRACKS | BOOL |  |  | 0 | 
Skin | USDIMPORTER_ANIMATION_SKELETAL | BOOL |  |  | 1 | 
