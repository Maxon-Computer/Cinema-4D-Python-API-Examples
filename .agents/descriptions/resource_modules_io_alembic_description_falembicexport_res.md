# Description: Alembic Export Settings

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/io_alembic/description/Falembicexport.res`
- **Symbol:** `Falembicexport`
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
Scale | ABCEXPORT_SCALE | UNITSCALE |  |  |  | 
Selection Only | ABCEXPORT_SELECTION_ONLY | BOOL |  |  | 0 | 
Global Coordinates | ABCEXPORT_GLOBAL_MATRIX | BOOL |  |  | 0 | 
Cameras | ABCEXPORT_CAMERAS | BOOL |  |  | 1 | 
XRefs | ABCEXPORT_XREFS | BOOL |  |  | 0 | 
Subdivision Surface | ABCEXPORT_HYPERNURBS | BOOL |  |  | 1 | 
Subdivision Surface Weights | ABCEXPORT_SDS_WEIGHTS | BOOL |  |  | 1 | 
Splines (Curves) | ABCEXPORT_SPLINES | BOOL |  |  | 1 | 
Hair (Curves) | ABCEXPORT_HAIR | BOOL |  |  | 0 | 
Particles | ABCEXPORT_PARTICLES | BOOL |  |  | 0 | 
Particles (Geometry) | ABCEXPORT_PARTICLE_GEOMETRY | BOOL |  |  | 0 | 
Start Frame | ABCEXPORT_FRAME_START | LONG | -18000 | 3240000 | 0 | 
End Frame | ABCEXPORT_FRAME_END | LONG | -18000 | 3240000 | 90 | 
Frame Step | ABCEXPORT_FRAME_STEP | LONG | 1 | 100 | 1 | 
Subframes | ABCEXPORT_SUBFRAMES | LONG | 1 | 100 | 1 | 
Visibility | ABCEXPORT_VISIBILITY | BOOL |  |  | 0 | 
Polygon Selections | ABCEXPORT_POLYGONSELECTIONS | BOOL |  |  | 1 | 
Normals | ABCEXPORT_NORMALS | BOOL |  |  | 1 | 
UVs | ABCEXPORT_UVS | BOOL |  |  | 1 | 
Vertex Colors | ABCEXPORT_VERTEX_COLORS | BOOL |  |  | 0 | 
Display Colors to Vertex Colors | ABCEXPORT_DISPLAY_COLORS | BOOL |  |  | 0 | 
Vertex Maps | ABCEXPORT_VERTEX_MAPS | BOOL |  |  | 0 | 
Points Only (Geometry) | ABCEXPORT_POINTS_ONLY | BOOL |  |  | 0 | 
Merge Generated | ABCEXPORT_MERGE_CACHE | BOOL |  |  | 0 | 
