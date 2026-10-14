# Description: Illustrator

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/sketch/description/faiexport.res`
- **Symbol:** `Faiexport`
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
Output | TUAIEXPORT_OUTPUTSIZE | LONG |  |  | TUAIEXPORT_OUTPUTSIZE_RENDER | TUAIEXPORT_OUTPUTSIZE_RENDER; TUAIEXPORT_OUTPUTSIZE_EDITOR; TUAIEXPORT_OUTPUTSIZE_CUSTOM
Width | TUAIEXPORT_OUTPUTSIZE_WIDTH | LONG | 8 |  | 640 | 
Height | TUAIEXPORT_OUTPUTSIZE_HEIGHT | LONG | 8 |  | 480 | 
Z Order | TUAIEXPORT_ZSORT | LONG |  |  | TUAIEXPORT_ZSORT_BACK | TUAIEXPORT_ZSORT_BACK; TUAIEXPORT_ZSORT_CENTER; TUAIEXPORT_ZSORT_FRONT
Scale | TUAIEXPORT_SCALE | REAL | 0.0 | 1000 | 100 | 
Layers | TUAIEXPORT_LAYERS | BOOL |  |  | 1 | 
Export | TUAIEXPORT_EXPORTLINES | BOOL |  |  | 1 | 
Opacity | TUAIEXPORT_LINEOPACITY | BOOL |  |  | 1 | 
Thickness | TUAIEXPORT_LINETHICKNESS | BOOL |  |  | 1 | 
Patterns | TUAIEXPORT_LINEPATTERNS | BOOL |  |  | 1 | 
Connections | TUAIEXPORT_LINECONNECTIONS | BOOL |  |  | 1 | 
Export | TUAIEXPORT_EXPORTSURFACE | BOOL |  |  | 1 | 
Subdivide Polygons | TUAIEXPORT_POLYSUBDIV | BOOL |  |  | 0 | 
Divisions | TUAIEXPORT_POLYSUBDIV_LEVEL | LONG | 1 | 8 | 2 | 
Backface Cull | TUAIEXPORT_BACKFACECULL | BOOL |  |  | 1 | 
Overfill | TUAIEXPORT_OVERFILL | BOOL |  |  | 1 | 
Shading | TUAIEXPORT_SHADING | LONG |  |  | TUAIEXPORT_SHADING_FACETTED | TUAIEXPORT_SHADING_OBJECTCOL; TUAIEXPORT_SHADING_UNIFORM; TUAIEXPORT_SHADING_FACETTED
Export | TUAIEXPORT_ANIMATION | BOOL |  |  |  | 
Output As | TUAIEXPORT_ANIMTYPE | LONG |  |  | TUAIEXPORT_ANIMTYPE_FILES | TUAIEXPORT_ANIMTYPE_FILES; TUAIEXPORT_ANIMTYPE_LAYERS
Frames | TUAIEXPORT_FRAMES | LONG |  |  | TUAIEXPORT_FRAMES_RENDER | TUAIEXPORT_FRAMES_ALL; TUAIEXPORT_FRAMES_RENDER; TUAIEXPORT_FRAMES_MANUAL
Start | TUAIEXPORT_FRAME_START | BASETIME |  |  | 0 | 
End | TUAIEXPORT_FRAME_END | BASETIME |  |  | 3 | 
Frame Rate | TUAIEXPORT_FRAME_RATE | LONG | 1 |  | 30 | 
