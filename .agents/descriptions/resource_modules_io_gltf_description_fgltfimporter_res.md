# Description: glTF Import Settings

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/io_gltf/description/fgltfimporter.res`
- **Symbol:** `fgltfimporter`
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
Scale | GLTFIMPORTER_UNITSCALE | UNITSCALE |  |  |  | 
Cameras | GLTFIMPORTER_CAMERAS | BOOL |  |  | 1 | 
Geometry | GLTFIMPORTER_GEOMETRY | BOOL |  |  | 1 | 
Materials | GLTFIMPORTER_MATERIALS | BOOL |  |  | 1 | 
Normals | GLTFIMPORTER_NORMALS | LONG |  |  | GLTFIMPORTER_NORMALS_PHONG | GLTFIMPORTER_NORMALS_NONE; GLTFIMPORTER_NORMALS_VERTEX; GLTFIMPORTER_NORMALS_PHONG
Phong Angle | GLTFIMPORTER_PHONGANGLE | REAL | 0 | 180 | 40 | 
Vertex Colors | GLTFIMPORTER_VERTEXCOLORS | BOOL |  |  | 1 | 
UVs | GLTFIMPORTER_UVS | BOOL |  |  | 1 | 
Flip Z | GLTFIMPORTER_FLIPZ | BOOL |  |  | 1 | 
Split Meshes | GLTFIMPORTER_GEOMETRY_SPLIT_MESHPRIMS | BOOL |  |  | 0 | 
Transform | GLTFIMPORTER_ANIMATION_TRS | BOOL |  |  | 1 | 
Pose Morphs | GLTFIMPORTER_ANIMATION_POSEMORPHS | BOOL |  |  | 1 | 
Pose Target Layer | GLTFIMPORTER_ANIMATION_POSEMORPHS_TARGETSLAYER | BOOL |  |  | 1 | 
Clean Tracks | GLTFIMPORTER_ANIMATION_CLEANTRACKS | BOOL |  |  | 1 | 
