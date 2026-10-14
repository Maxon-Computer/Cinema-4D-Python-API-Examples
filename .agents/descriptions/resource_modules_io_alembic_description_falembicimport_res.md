# Description: Alembic Import Settings

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/io_alembic/description/Falembicimport.res`
- **Symbol:** `Falembicimport`
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
Scale | ABCIMPORT_SCALE | UNITSCALE |  |  |  | 
SubD | ABCIMPORT_SUBD | LONG |  |  |  | ABCIMPORT_SUBD_NO_SDS; ABCIMPORT_SUBD_NO_WEIGHTS; ABCIMPORT_SUBD_BOTH_WEIGHTS
Curves | ABCIMPORT_CURVES | LONG |  |  |  | ABCIMPORT_CURVES_NONE; ABCIMPORT_CURVES_SPLINES; ABCIMPORT_CURVES_HAIR
Points | ABCIMPORT_POINTS | LONG |  |  |  | ABCIMPORT_POINTS_NONE; ABCIMPORT_POINTS_TPARTICLES; ABCIMPORT_POINTS_GEOMETRY; ABCIMPORT_POINTS_PARTICLEGROUP
Instances | ABCIMPORT_INSTANCES | LONG |  |  | ABCIMPORT_INSTANCES_RENDERINSTANCE | ABCIMPORT_INSTANCES_NONE; ABCIMPORT_INSTANCES_INSTANCE; ABCIMPORT_INSTANCES_RENDERINSTANCE
Cameras | ABCIMPORT_CAMERAS | BOOL |  |  | 1 | 
Original | ABCIMPORT_NOSTARTFRAME | BOOL |  |  | 1 | 
Start Frame | ABCIMPORT_STARTFRAME | LONG | -300000 | 300000 | 0 | 
Frame Rate | ABCIMPORT_FPS | LONG | 1 | 500 | 30 | 
Interpolation | ABCIMPORT_INTERPOLATION | BOOL |  |  | 1 | 
Visibility | ABCIMPORT_VISIBILITY | BOOL |  |  | 0 | 
Normals | ABCIMPORT_NORMALS | BOOL |  |  | 1 | 
UVs | ABCIMPORT_UVS | BOOL |  |  | 1 | 
Face Sets | ABCIMPORT_FACESETS | BOOL |  |  | 1 | 
Color Maps | ABCIMPORT_COLORMAPS | BOOL |  |  | 0 | 
Other Attributes | ABCIMPORT_OTHERATTR | BOOL |  |  | 0 | 
