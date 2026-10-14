# Description: FBX Export Settings

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/io_fbx/description/Ffbxexport.res`
- **Symbol:** `Ffbxexport`
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
File Format | FBXEXPORT_FBX_VERSION | LONG |  |  | FBX_EXPORTVERSION_NATIVE | FBX_EXPORTVERSION_NATIVE; FBX_EXPORTVERSION_7_5_0; FBX_EXPORTVERSION_7_4_0; FBX_EXPORTVERSION_7_3_0; FBX_EXPORTVERSION_7_2_0; FBX_EXPORTVERSION_7_1_0; FBX_EXPORTVERSION_6_1_0
As Text File | FBXEXPORT_ASCII | BOOL |  |  | 0 | 
Cameras | FBXEXPORT_CAMERAS | BOOL |  |  | 1 | 
Lights | FBXEXPORT_LIGHTS | BOOL |  |  | 1 | 
Splines | FBXEXPORT_SPLINES | BOOL |  |  | 1 | 
Instances | FBXEXPORT_INSTANCES | BOOL |  |  | 1 | 
Selection Only | FBXEXPORT_SELECTION_ONLY | BOOL |  |  | 0 | 
Global Coordinates | FBXEXPORT_GLOBAL_MATRIX | BOOL |  |  | 0 | 
Subdivision Surface | FBXEXPORT_SDS | LONG |  |  | FBXEXPORT_SDS_GENERATOR | FBXEXPORT_SDS_CAGE; FBXEXPORT_SDS_GENERATOR; FBXEXPORT_SDS_BAKED
Triangulate | FBXEXPORT_TRIANGULATE | BOOL |  |  | 0 | 
Normals | FBXEXPORT_SAVE_NORMALS | BOOL |  |  | 1 | 
Vertex Colors | FBXEXPORT_SAVE_VERTEX_COLORS | BOOL |  |  | 0 | 
Vertex Maps to Vertex Colors | FBXEXPORT_SAVE_VERTEX_MAPS_AS_COLORS | BOOL |  |  | 0 | 
Up Axis | FBXEXPORT_UP_AXIS | LONG |  |  | FBXEXPORT_UP_AXIS_Y | FBXEXPORT_UP_AXIS_Y; FBXEXPORT_UP_AXIS_MINUS_Y; FBXEXPORT_UP_AXIS_X; FBXEXPORT_UP_AXIS_MINUS_X; FBXEXPORT_UP_AXIS_Z; FBXEXPORT_UP_AXIS_MINUS_Z
Flip Z Axis | FBXEXPORT_FLIP_Z_AXIS | BOOL |  |  | 0 | 
Tracks | FBXEXPORT_TRACKS | BOOL |  |  | 1 | 
Bake All Frames | FBXEXPORT_BAKE_ALL_FRAMES | BOOL |  |  | 0 | 
PLA to Vertex Cache | FBXEXPORT_PLA_TO_VERTEXCACHE | BOOL |  |  | 0 | 
Bound Joints Only | FBXEXPORT_BOUND_JOINTS_ONLY | BOOL |  |  | 0 | 
Takes | FBXEXPORT_TAKE_MODE | LONG |  |  | FBXEXPORT_TAKE_TAKES | FBXEXPORT_TAKE_NONE; FBXEXPORT_TAKE_TAKES; FBXEXPORT_TAKE_MARKERS
Material | FBXEXPORT_MATERIALS | BOOL |  |  | 1 | 
Embed Textures | FBXEXPORT_EMBED_TEXTURES | BOOL |  |  | 1 | 
Substances | FBXEXPORT_SUBSTANCES | BOOL |  |  | 1 | 
Bake Materials | FBXEXPORT_BAKE_MATERIALS | BOOL |  |  | 1 | 
Width | FBXEXPORT_BAKEDTEXTURE_WIDTH | LONG | 0 | 128000 |  | 
Height | FBXEXPORT_BAKEDTEXTURE_HEIGHT | LONG | 0 | 128000 |  | 
Resize Textures | FBXEXPORT_BAKEDTEXTURE_RESIZE | LONG |  |  | FBXEXPORT_BAKEDTEXTURE_RESIZE_OFF | FBXEXPORT_BAKEDTEXTURE_RESIZE_OFF; FBXEXPORT_BAKEDTEXTURE_RESIZE_DONT_ENLARGE; FBXEXPORT_BAKEDTEXTURE_RESIZE_ALWAYS
Format | FBXEXPORT_BAKEDTEXTURE_FORMAT | LONG |  |  |  | 
Depth | FBXEXPORT_BAKEDTEXTURE_DEPTH | LONG |  |  | FBXEXPORT_BAKEDTEXTURE_DEPTH_8 | FBXEXPORT_BAKEDTEXTURE_DEPTH_8; FBXEXPORT_BAKEDTEXTURE_DEPTH_16; FBXEXPORT_BAKEDTEXTURE_DEPTH_32
LOD Name Suffix | FBXEXPORT_LOD_SUFFIX | BOOL |  |  | 0 | 
