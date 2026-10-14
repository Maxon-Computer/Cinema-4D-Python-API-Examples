# Description: USD Export Settings

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/io_usd/description/fusdexporter.res`
- **Symbol:** `fusdexporter`
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
Export to USD Layer | USDEXPORTER_EXPORT2LAYER | BOOL |  |  | 0 | 
File Format | USDEXPORTER_FILEFORMAT | LONG |  |  | USDEXPORTER_FILEFORMAT_USDC | USDEXPORTER_FILEFORMAT_USDA; USDEXPORTER_FILEFORMAT_USDC
Zipped (&#42;.usdz) | USDEXPORTER_ZIP | BOOL |  |  | 0 | 
Geometry | USDEXPORTER_GEOMETRY | BOOL |  |  | 1 | 
Cameras | USDEXPORTER_CAMERAS | BOOL |  |  | 1 | 
Instances | USDEXPORTER_INSTANCES | BOOL |  |  | 0 | 
Materials | USDEXPORTER_MATERIALS | LONG |  |  | USDEXPORTER_MATERIALS_EXPORT | USDEXPORTER_MATERIALS_NONE; USDEXPORTER_MATERIALS_EXPORT
No label | USDEXPORTER_MATERIALS_BRIDGE_INFO | STRING |  |  |  | 
Lights | USDEXPORTER_LIGHTUNITS | LONG |  |  | USDEXPORTER_LIGHTUNITS_NIT | USDEXPORTER_LIGHTUNITS_NONE; USDEXPORTER_LIGHTUNITS_NIT; USDEXPORTER_LIGHTUNITS_CANDELA
Normals | USDEXPORTER_GEOMETRY_NORMALS | BOOL |  |  | 1 | 
UV | USDEXPORTER_GEOMETRY_UV | BOOL |  |  | 1 | 
Vertex Color | USDEXPORTER_GEOMETRY_VERTEXCOLORS | BOOL |  |  | 1 | 
Display Color | USDEXPORTER_GEOMETRY_DISPLAYCOLOR | BOOL |  |  | 1 | 
Skin | USDEXPORTER_ANIMATION_SKELETON | BOOL |  |  | 1 | 
Animation Range | USDEXPORTER_ANIMATION_FRAMES | LONG |  |  | USDEXPORTER_ANIMATION_FRAMES_CURRENTFRAME | USDEXPORTER_ANIMATION_FRAMES_MANUAL; USDEXPORTER_ANIMATION_FRAMES_CURRENTFRAME; USDEXPORTER_ANIMATION_FRAMES_ALLFRAMES; USDEXPORTER_ANIMATION_FRAMES_ALLANIMATEDFRAMES; USDEXPORTER_ANIMATION_FRAMES_PREVIEWRANGE
From | USDEXPORTER_ANIMATION_TIMEFROM | BASETIME | 0 |  |  | 
To | USDEXPORTER_ANIMATION_TIMETO | BASETIME | 0 |  |  | 
Bake Materials | USDEXPORTER_MATERIALS_BAKETEXTURES | BOOL |  |  | 1 | 
Width | USDEXPORTER_MATERIALS_WIDTH | LONG | 1 | 128000 | 1024 | 
Height | USDEXPORTER_MATERIALS_HEIGHT | LONG | 1 | 128000 | 1024 | 
Resize Textures | USDEXPORTER_MATERIALS_RESIZE | LONG |  |  | USDEXPORTER_MATERIALS_RESIZE_OFF | USDEXPORTER_MATERIALS_RESIZE_OFF; USDEXPORTER_MATERIALS_RESIZE_DONT_ENLARGE; USDEXPORTER_MATERIALS_RESIZE_ALWAYS
Format | USDEXPORTER_MATERIALS_FORMAT | LONG |  |  |  | 
Format | USDEXPORTER_MATERIALS_FORMAT_USDZ | LONG |  |  |  | 
Depth | USDEXPORTER_MATERIALS_DEPTH | LONG |  |  | USDEXPORTER_MATERIALS_DEPTH_8 | USDEXPORTER_MATERIALS_DEPTH_8; USDEXPORTER_MATERIALS_DEPTH_16; USDEXPORTER_MATERIALS_DEPTH_32
Prevent Gprim Nesting | USDEXPORTER_VALIDITY_PREVENTGPRIMNESTING | BOOL |  |  |  | 
