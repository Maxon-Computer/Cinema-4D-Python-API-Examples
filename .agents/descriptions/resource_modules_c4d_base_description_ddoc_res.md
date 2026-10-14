# Description: Scene

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/c4d_base/description/ddoc.res`
- **Symbol:** `Ddoc`
- **Category:** Other

Use parameter symbols to access parameters and cycle option symbols for cycle values, never their numeric IDs. Treat Min and Max as constraints and Default as the declared initial value; blank cells mean the resource does not declare that metadata, not that the value is zero. Base Description Parameters lists inherited fields from each base; All Parameters lists the effective parameter set for this description.

## Base Description Parameters

No base descriptions.

## All Parameters

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Project Scale | DOCUMENT_DOCUNIT | UNITSCALE |  |  |  | 
Scale Project... | DOCUMENT_SCALEDOCUMENT | BUTTON |  |  |  | 
FPS | DOCUMENT_FPS | LONG | 1 | 2500 |  | 
Project Time | DOCUMENT_TIME | BASETIME |  |  |  | 
Time Min | DOCUMENT_MINTIME | BASETIME |  |  |  | 
Time Max  | DOCUMENT_MAXTIME | BASETIME |  |  |  | 
Preview Min | DOCUMENT_LOOPMINTIME | BASETIME |  |  |  | 
Preview Max | DOCUMENT_LOOPMAXTIME | BASETIME |  |  |  | 
Animation | DOCUMENT_USEANIMATION | BOOL |  |  |  | 
Expression | DOCUMENT_USEEXPRESSIONS | BOOL |  |  |  | 
Generators | DOCUMENT_USEGENERATORS | BOOL |  |  |  | 
Deformers | DOCUMENT_USEDEFORMERS | BOOL |  |  |  | 
Motion System | DOCUMENT_USEMOTIONSYSTEM | BOOL |  |  |  | 
Connect Watch Folder | DOCUMENT_MOUNTWATCHFOLDER | BOOL |  |  | 1 | 
Relative Path | DOCUMENT_RELATIVEWATCHFOLDER | FILENAME |  |  |  | 
Color | DOCUMENT_DEFAULTMATERIAL_COLOR | COLOR |  |  |  | 
View Clipping | DOCUMENT_CLIPPING_PRESET | LONG |  |  |  | DOCUMENT_CLIPPING_PRESET_TINY; DOCUMENT_CLIPPING_PRESET_SMALL; DOCUMENT_CLIPPING_PRESET_MEDIUM; DOCUMENT_CLIPPING_PRESET_LARGE; DOCUMENT_CLIPPING_PRESET_HUGE; DOCUMENT_CLIPPING_PRESET_CUSTOM
Near | DOCUMENT_CLIPPING_PRESET_NEAR | REAL | 0 |  |  | 
Far | DOCUMENT_CLIPPING_PRESET_FAR | REAL | 0 |  |  | 
Level of Detail | DOCUMENT_LOD | REAL | 0.0 | 100.0 |  | 
Use Render LOD for Viewport Rendering | DOCUMENT_RENDERLOD | BOOL |  |  |  | 
Change Render Space... | DOCUMENT_CHANGE_RENDER_COLORSPACE | BUTTON |  |  |  | 
No label | DOCUMENT_CURRENT_RENDER_COLORSPACE | STATICTEXT |  |  |  | 
Color Management | DOCUMENT_COLOR_MANAGEMENT | LONG |  |  |  | 
Render Space | DOCUMENT_OCIO_RENDER_COLORSPACE | LONG |  |  |  | 
View Transform (Project) | DOCUMENT_OCIO_VIEW_TRANSFORM | LONG |  |  |  | 
View Transform (Thumbnails) | DOCUMENT_OCIO_VIEW_TRANSFORM_THUMBNAILS | LONG |  |  |  | 
Display Space | DOCUMENT_OCIO_DISPLAY_COLORSPACE | LONG |  |  |  | 
OpenColorIO Config | DOCUMENT_OCIO_CONFIG | FILENAME |  |  |  | 
OpenColorIO File Rules | DOCUMENT_OCIO_FILE_RULES | BOOL |  |  |  | 
Linear Workflow | DOCUMENT_LINEARWORKFLOW | BOOL |  |  |  | 
Input Color Profile | DOCUMENT_COLORPROFILE | LONG |  |  |  | DOCUMENT_COLORPROFILE_DISABLED; DOCUMENT_COLORPROFILE_SRGB; DOCUMENT_COLORPROFILE_LINEAR
No label | DOCUMENT_COLORINFO | STRING |  |  |  | 
No label | DOCUMENT_OCIO_INFOSTRING | STRING |  |  |  | 
Author | DOCUMENT_INFO_AUTHOR | STRING |  |  |  | 
Copyright | DOCUMENT_INFO_COPYRIGHT | STRING |  |  |  | 
Info | DOCUMENT_INFO_README | STRING |  |  |  | 
File Format | DOCUMENT_INFO_FILEFORMAT | STATICTEXT |  |  |  | 
File Version | DOCUMENT_INFO_FILEVERSION | STATICTEXT |  |  |  | 
Created by (Software) | DOCUMENT_INFO_PRGCREATOR_STRING | STATICTEXT |  |  |  | 
Created by (Software) | DOCUMENT_INFO_PRGCREATOR_NAME | STRING |  |  |  | 
Created by (Software) | DOCUMENT_INFO_PRGCREATOR_ID | LONG |  |  |  | 
Date Created | DOCUMENT_INFO_DATECREATED_STRING | STATICTEXT |  |  |  | 
Saved by (Software) | DOCUMENT_INFO_PRGWRITER_STRING | STATICTEXT |  |  |  | 
Saved by (Software) | DOCUMENT_INFO_PRGWRITER_NAME | STRING |  |  |  | 
Saved by (Software) | DOCUMENT_INFO_PRGWRITER_ID | LONG |  |  |  | 
Last Save Date | DOCUMENT_INFO_DATESAVED_STRING | STATICTEXT |  |  |  | 
Project Path | DOCUMENT_PATH | FILENAME |  |  |  | 
Project Name | DOCUMENT_NAME | FILENAME |  |  |  | 
File Path | DOCUMENT_FILEPATH | FILENAME |  |  |  | 
Preview Image | DOCUMENT_PREVIEW_IMAGE | BITMAPBUTTON |  |  |  | 
Preview Command | DOCUMENT_PREVIEW_COMMAND | LONG |  |  |  | DOCUMENT_PREVIEW_COMMAND_AUTO; DOCUMENT_PREVIEW_COMMAND_PASTE; DOCUMENT_PREVIEW_COMMAND_FROMEDITOR; DOCUMENT_PREVIEW_COMMAND_LOAD
Save Polygon Cache | DOCUMENT_CINEWARE_POLYGON_CACHE | BOOL |  |  |  | 
Save Animation Cache | DOCUMENT_CINEWARE_ANIMATION_CACHE | BOOL |  |  |  | 
Save Material Cache | DOCUMENT_CINEWARE_MATERIAL_CACHE | BOOL |  |  |  | 
Width | DOCUMENT_CINEWARE_MATERIAL_WIDTH | LONG | 0 | 128000 |  | 
Height | DOCUMENT_CINEWARE_MATERIAL_HEIGHT | LONG | 0 | 128000 |  | 
Format | DOCUMENT_CINEWARE_MATERIAL_FORMAT | LONG |  |  |  | 
Depth | DOCUMENT_CINEWARE_MATERIAL_DEPTH | LONG |  |  |  | 
