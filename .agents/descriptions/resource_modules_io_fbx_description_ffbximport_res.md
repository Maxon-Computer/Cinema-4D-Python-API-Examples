# Description: FBX Import Settings

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/io_fbx/description/Ffbximport.res`
- **Symbol:** `Ffbximport`
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
Geometry | FBXIMPORT_GEOMETRY | BOOL |  |  | 1 | 
Curves | FBXIMPORT_CURVES | BOOL |  |  | 1 | 
Cameras | FBXIMPORT_CAMERAS | BOOL |  |  | 1 | 
Lights | FBXIMPORT_LIGHTS | BOOL |  |  | 1 | 
Instances | FBXIMPORT_INSTANCES | BOOL |  |  | 1 | 
Markers | FBXIMPORT_MARKERS | BOOL |  |  | 1 | 
Subdivision Surface | FBXIMPORT_SDS | BOOL |  |  | 1 | 
Deformation | FBXIMPORT_ACTIVATE_JOINTS | BOOL |  |  | 1 | 
Normals | FBXIMPORT_NORMALS | LONG |  |  | FBXIMPORT_NORMALS_EDGE_BREAKS | FBXIMPORT_NORMALS_NONE; FBXIMPORT_NORMALS_NORMALTAGS; FBXIMPORT_NORMALS_EDGE_BREAKS
Vertex Colors | FBXIMPORT_COLORS | BOOL |  |  | 0 | 
Grayscale to Vertex Maps | FBXIMPORT_COLORS_AS_VERTEX_MAPS | BOOL |  |  | 0 | 
Up Axis | FBXIMPORT_UP_AXIS | LONG |  |  | FBXIMPORT_UP_AXIS_DEFAULT | FBXIMPORT_UP_AXIS_DEFAULT; FBXIMPORT_UP_AXIS_X; FBXIMPORT_UP_AXIS_MINUS_X; FBXIMPORT_UP_AXIS_Y; FBXIMPORT_UP_AXIS_MINUS_Y; FBXIMPORT_UP_AXIS_Z; FBXIMPORT_UP_AXIS_MINUS_Z
Flip Z Axis | FBXIMPORT_FLIP_Z_AXIS | BOOL |  |  | 0 | 
Tracks | FBXIMPORT_TRACKS | BOOL |  |  | 1 | 
Clean Tracks | FBXIMPORT_CLEAN_TRACKS | BOOL |  |  | 0 | 
Vertex Cache to PLA | FBXIMPORT_VERTEXCACHE_TO_PLA | BOOL |  |  | 0 | 
Poses | FBXIMPORT_SHAPES | BOOL |  |  | 1 | 
Materials | FBXIMPORT_MATERIALS | BOOL |  |  | 1 | 
Substances | FBXIMPORT_SUBSTANCES | BOOL |  |  | 1 | 
Single Material Selection Sets | FBXIMPORT_SINGLE_MAT_SELECTIONTAGS | BOOL |  |  | 0 | 
