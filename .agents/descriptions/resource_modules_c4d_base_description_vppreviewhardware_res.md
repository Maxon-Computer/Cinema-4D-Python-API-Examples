# Description: Viewport Renderer

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/c4d_base/description/vppreviewhardware.res`
- **Symbol:** `VPpreviewhardware`
- **Category:** Video Posts

Use parameter symbols to access parameters and cycle option symbols for cycle values, never their numeric IDs. Treat Min and Max as constraints and Default as the declared initial value; blank cells mean the resource does not declare that metadata, not that the value is zero. Base Description Parameters lists inherited fields from each base; All Parameters lists the effective parameter set for this description.

## Base Description Parameters

### Post Effect (`VPbase`)

No parameters.

## All Parameters

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Geometry Only | VP_PREVIEWHARDWARE_ONLY_GEOMETRY | BOOL |  |  |  | 
Workplane | VP_PREVIEWHARDWARE_DISPLAYFILTER_GRID | BOOL |  |  |  | 
World Grid | VP_PREVIEWHARDWARE_DISPLAYFILTER_BASEGRID | BOOL |  |  |  | 
World Axis | VP_PREVIEWHARDWARE_DISPLAYFILTER_WORLDAXIS | BOOL |  |  |  | 
Horizon | VP_PREVIEWHARDWARE_DISPLAYFILTER_HORIZON | BOOL |  |  |  | 
HUD | VP_PREVIEWHARDWARE_DISPLAYFILTER_HUD | BOOL |  |  |  | 
Null | VP_PREVIEWHARDWARE_DISPLAYFILTER_NULL | BOOL |  |  |  | 
Spline | VP_PREVIEWHARDWARE_DISPLAYFILTER_SPLINE | BOOL |  |  |  | 
Polygon | VP_PREVIEWHARDWARE_DISPLAYFILTER_POLYGON | BOOL |  |  |  | 
Generator | VP_PREVIEWHARDWARE_DISPLAYFILTER_GENERATOR | BOOL |  |  |  | 
Subdivision Surface | VP_PREVIEWHARDWARE_DISPLAYFILTER_HYPERNURBS | BOOL |  |  |  | 
Deformer | VP_PREVIEWHARDWARE_DISPLAYFILTER_DEFORMER | BOOL |  |  |  | 
Field | VP_PREVIEWHARDWARE_DISPLAYFILTER_FIELD | BOOL |  |  |  | 
Environment | VP_PREVIEWHARDWARE_DISPLAYFILTER_SCENE | BOOL |  |  |  | 
Camera | VP_PREVIEWHARDWARE_DISPLAYFILTER_CAMERA | BOOL |  |  |  | 
Light | VP_PREVIEWHARDWARE_DISPLAYFILTER_LIGHT | BOOL |  |  |  | 
Joint | VP_PREVIEWHARDWARE_DISPLAYFILTER_JOINT | BOOL |  |  |  | 
Particle | VP_PREVIEWHARDWARE_DISPLAYFILTER_PARTICLE | BOOL |  |  |  | 
Hair | VP_PREVIEWHARDWARE_DISPLAYFILTER_HAIR | BOOL |  |  |  | 
Guides | VP_PREVIEWHARDWARE_DISPLAYFILTER_GUIDELINES | BOOL |  |  |  | 
Other | VP_PREVIEWHARDWARE_DISPLAYFILTER_OTHER | BOOL |  |  |  | 
Axis | VP_PREVIEWHARDWARE_DISPLAYFILTER_OBJECTHANDLES | BOOL |  |  |  | 
Multi-Select Axes | VP_PREVIEWHARDWARE_DISPLAYFILTER_MULTIAXIS | BOOL |  |  |  | 
Handles | VP_PREVIEWHARDWARE_DISPLAYFILTER_HANDLES | BOOL |  |  |  | 
SDS Mesh | VP_PREVIEWHARDWARE_DISPLAYFILTER_SDS | BOOL |  |  |  | 
SDS Cage | VP_PREVIEWHARDWARE_DISPLAYFILTER_SDSCAGE | BOOL |  |  |  | 
N-gon Lines | VP_PREVIEWHARDWARE_DISPLAYFILTER_NGONLINES | BOOL |  |  |  | 
Animation Path | VP_PREVIEWHARDWARE_DATA_SHOWPATH | BOOL |  |  |  | 
Ghosting | VP_PREVIEWHARDWARE_DISPLAYFILTER_ONION | BOOL |  |  |  | 
Load Preset... | VP_PREVIEWHARDWARE_DISPLAYFILTER_PRESET_LOAD | BUTTON |  |  |  | 
Save Preset... | VP_PREVIEWHARDWARE_DISPLAYFILTER_PRESET_SAVE | BUTTON |  |  |  | 
Effects | VP_PREVIEWHARDWARE_ENHANCEDOPENGL | BOOL |  |  |  | 
HQ Noises | VP_PREVIEWHARDWARE_NOISE | BOOL |  |  |  | 
Transparency | VP_PREVIEWHARDWARE_TRANSPARENCY | BOOL |  |  |  | 
Shadows | VP_PREVIEWHARDWARE_SHADOW | BOOL |  |  |  | 
Shadowmap Size | VP_PREVIEWHARDWARE_SHADOW_MAP_SIZE | LONG | 32 | 4096 |  | 
Alternative Shadow Filtering | VP_PREVIEWHARDWARE_ALTERNATIVESHADOWMAPPING | BOOL |  |  |  | 
Reflections | VP_PREVIEWHARDWARE_REFLECTIONS | BOOL |  |  |  | 
Environment Override | VP_PREVIEWHARDWARE_REFLECTIONS_ENV_OVERRIDE | FILENAME |  |  |  | 
Rotation | VP_PREVIEWHARDWARE_REFLECTIONS_ENV_ROTATION | VECTOR |  |  |  | 
Screen-Space Local Reflections | VP_PREVIEWHARDWARE_REFLECTIONS_SSR | BOOL |  |  |  | 
Distance | VP_PREVIEWHARDWARE_REFLECTIONS_SSR_ITERATIONS | LONG | 1 | 1024 |  | 
Pixel Thickness | VP_PREVIEWHARDWARE_REFLECTIONS_SSR_GEOMETRY_THICKNESS | REAL | 0.02 | 100000 |  | 
Half Resolution | VP_PREVIEWHARDWARE_REFLECTIONS_SSR_HALF_RES | BOOL |  |  |  | 
Post Effects | VP_PREVIEWHARDWARE_POSTEFFECT | BOOL |  |  |  | 
Magic Bullet Looks | VP_PREVIEWHARDWARE_MAGICBULLETLOOKS | BOOL |  |  |  | 
SSAO | VP_PREVIEWHARDWARE_SSAO | BOOL |  |  |  | 
Tessellation | VP_PREVIEWHARDWARE_TESSELLATION | BOOL |  |  |  | 
Depth of Field | VP_PREVIEWHARDWARE_DEPTHOFFIELD | BOOL |  |  |  | 
Anti-Aliased DOF | VP_PREVIEWHARDWARE_DEPTHOFFIELD_ANTIALIASED | BOOL |  |  |  | 
Ignore Hidden Polygon Selections | VP_PREVIEWHARDWARE_IGNORE_HIDDEN_POLYGON_SELECTION | BOOL |  |  |  | 
32-bit Framebuffer | VP_PREVIEWHARDWARE_32BIT_DEPTH | BOOL |  |  |  | 
Anti-Aliasing | VP_PREVIEWHARDWARE_ANTIALIASING | LONG |  |  |  | 
Supersampling | VP_PREVIEWHARDWARE_SUPERSAMPLING | LONG |  |  |  | VP_PREVIEWHARDWARE_SUPERSAMPLING_NONE; VP_PREVIEWHARDWARE_SUPERSAMPLING_2; VP_PREVIEWHARDWARE_SUPERSAMPLING_3; VP_PREVIEWHARDWARE_SUPERSAMPLING_4; VP_PREVIEWHARDWARE_SUPERSAMPLING_5; VP_PREVIEWHARDWARE_SUPERSAMPLING_8; VP_PREVIEWHARDWARE_SUPERSAMPLING_16
Copy Effects from Viewport | VP_PREVIEWHARDWARE_COPY_VP_EFFECTS | BUTTON |  |  |  | 
