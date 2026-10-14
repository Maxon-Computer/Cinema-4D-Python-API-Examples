# Description: glTF Export Settings

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/io_gltf/description/fgltfexporter.res`
- **Symbol:** `fgltfexporter`
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
File Format | GLTFEXPORTER_FILEFORMAT | LONG |  |  | GLTFEXPORTER_FILEFORMAT_GLTF | GLTFEXPORTER_FILEFORMAT_GLTF; GLTFEXPORTER_FILEFORMAT_GLB
Scale | GLTFEXPORTER_UNITSCALE | UNITSCALE |  |  |  | 
Current Frame | GLTFEXPORTER_CURRENTFRAME | BOOL |  |  | 1 | 
Custom Frame | GLTFEXPORTER_CUSTOMFRAME | LONG |  |  | 0 | 
Transform | GLTFEXPORTER_PSRANIMATIONS | BOOL |  |  | 1 | 
Morph | GLTFEXPORTER_MORPHANIMATIONS | BOOL |  |  | 1 | 
Skin | GLTFEXPORTER_SKINANIMATIONS | BOOL |  |  | 0 | 
Bake Animation | GLTFEXPORTER_BAKEANIMATIONS | BOOL |  |  | 0 | 
Textures | GLTFEXPORTER_TEXTURES | BOOL |  |  | 1 | 
Width | GLTFEXPORTER_TEXTURES_WIDTH | LONG | 1 | 128000 | 1024 | 
Height | GLTFEXPORTER_TEXTURES_HEIGHT | LONG | 1 | 128000 | 1024 | 
Resize Textures | GLTFEXPORTER_TEXTURES_RESIZE | LONG |  |  | GLTFEXPORTER_TEXTURES_RESIZE_OFF | GLTFEXPORTER_TEXTURES_RESIZE_OFF; GLTFEXPORTER_TEXTURES_RESIZE_DONTENLARGE; GLTFEXPORTER_TEXTURES_RESIZE_ALWAYS
Double Sided | GLTFEXPORTER_DOUBLESIDED | BOOL |  |  | 0 | 
Cameras | GLTFEXPORTER_CAMERAS | BOOL |  |  | 1 | 
Instances | GLTFEXPORTER_INSTANCES | BOOL |  |  | 1 | 
Normals | GLTFEXPORTER_NORMALS | BOOL |  |  | 1 | 
UVs | GLTFEXPORTER_UVS | BOOL |  |  | 1 | 
Flip Z | GLTFEXPORTER_FLIPZ | BOOL |  |  | 1 | 
