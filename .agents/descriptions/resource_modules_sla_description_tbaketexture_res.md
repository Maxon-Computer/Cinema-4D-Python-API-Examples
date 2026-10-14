# Description: Bake Material

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/sla/description/tbaketexture.res`
- **Symbol:** `TBakeTexture`
- **Category:** Tags

Use parameter symbols to access parameters and cycle option symbols for cycle values, never their numeric IDs. Treat Min and Max as constraints and Default as the declared initial value; blank cells mean the resource does not declare that metadata, not that the value is zero. Base Description Parameters lists inherited fields from each base; All Parameters lists the effective parameter set for this description.

## Base Description Parameters

### Base Tag (`Tbase`)

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Expose on Object | ID_EXPOSETAB | BOOL |  |  |  | 

### Basic Properties (`Obaselist`)

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Icon File / ID | ID_BASELIST_ICON_FILE | TEXTURE |  |  |  | 
Icon Color | ID_BASELIST_ICON_COLORIZE_MODE | BOOL |  |  |  | 
Color | ID_BASELIST_ICON_COLOR | COLOR |  |  | 1.0 0.9 0.4 | 
No label | ID_BASELIST_ICON_PRESET_BUTTONS | ICONCHOOSER |  |  |  | 
Name | ID_BASELIST_NAME | STRING |  |  |  | 
Layer | ID_LAYER_LINK | LINK |  |  |  | 
No label | ID_BASELIST_NODESPACE_ADD_REMOVE_BUTTONS | NODESPACE_ADD_REMOVE |  |  |  | 

## All Parameters

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Icon File / ID | ID_BASELIST_ICON_FILE | TEXTURE |  |  |  | 
Icon Color | ID_BASELIST_ICON_COLORIZE_MODE | BOOL |  |  |  | 
Color | ID_BASELIST_ICON_COLOR | COLOR |  |  | 1.0 0.9 0.4 | 
No label | ID_BASELIST_ICON_PRESET_BUTTONS | ICONCHOOSER |  |  |  | 
Name | ID_BASELIST_NAME | STRING |  |  |  | 
Layer | ID_LAYER_LINK | LINK |  |  |  | 
No label | ID_BASELIST_NODESPACE_ADD_REMOVE_BUTTONS | NODESPACE_ADD_REMOVE |  |  |  | 
Expose on Object | ID_EXPOSETAB | BOOL |  |  |  | 
Filename | BAKETEXTURE_NAME | FILENAME |  |  |  | 
Format | BAKETEXTURE_FORMAT | LONG |  |  |  | 
Options... | BAKETEXTURE_OPTIONS_BTN | BUTTON |  |  |  | 
Single File | BAKETEXTURE_SINGLEFILE | BOOL |  |  |  | 
Color Profile | BAKETEXTURE_COLORPROFILE | COLORPROFILE |  |  |  | 
Color Depth | BAKETEXTURE_COLOR_DEPTH | LONG |  |  |  | 
Automatic Size | BAKETEXTURE_AUTOSIZE | BOOL |  |  |  | 
Width | BAKETEXTURE_WIDTH | LONG | 16 | 16000 |  | 
Height | BAKETEXTURE_HEIGHT | LONG | 16 | 16000 |  | 
Minimal Size | BAKETEXTURE_AUTO_MIN | LONG | 16 | 16000 |  | 
Maximal Size | BAKETEXTURE_AUTO_MAX | LONG | 16 | 16000 |  | 
Pixel Size | BAKETEXTURE_AUTO_PIXEL_SIZE | REAL | 0.001 |  |  | 
Supersampling | BAKETEXTURE_SUPERSAMPLING | LONG | 0 | 10 |  | 
Pixel Border | BAKETEXTURE_PIXELBORDER | LONG | 0 | 20 |  | 
Continue UVs | BAKETEXTURE_CONTINUE_UV | BOOL |  |  |  | 
Background | BAKETEXTURE_BACKGROUND | COLOR |  |  |  | 
Use Polygon Selection | BAKETEXTURE_USE_POLYSELECTION | BOOL |  |  |  | 
Evaluate Bump | BAKETEXTURE_USE_BUMP | BOOL |  |  |  | 
Use Camera Vector | BAKETEXTURE_USE_CAMERA_VECTOR | BOOL |  |  |  | 
Color | BAKETEXTURE_CHANNEL_COLOR | BOOL |  |  |  | 
Luminance | BAKETEXTURE_CHANNEL_LUMINANCE | BOOL |  |  |  | 
Diffusion | BAKETEXTURE_CHANNEL_DIFFUSION | BOOL |  |  |  | 
Bump | BAKETEXTURE_CHANNEL_BUMP | BOOL |  |  |  | 
Alpha | BAKETEXTURE_CHANNEL_ALPHA | BOOL |  |  |  | 
Transparency | BAKETEXTURE_CHANNEL_TRANS | BOOL |  |  |  | 
Displacement | BAKETEXTURE_CHANNEL_DISPLACEMENT | BOOL |  |  |  | 
Surface Color | BAKETEXTURE_CHANNEL_S_COLOR | BOOL |  |  |  | 
Illumination | BAKETEXTURE_CHANNEL_ILLUMINATION | BOOL |  |  |  | 
Shadows | BAKETEXTURE_CHANNEL_SHADOWS | BOOL |  |  |  | 
Ambient Occlusion | BAKETEXTURE_CHANNEL_AO | BOOL |  |  |  | 
Normal | BAKETEXTURE_CHANNEL_NORMAL | BOOL |  |  |  | 
UV Map | BAKETEXTURE_CHANNEL_UVMAP | BOOL |  |  |  | 
Reflection | BAKETEXTURE_CHANNEL_REFLECTION | BOOL |  |  |  | 
Illumination | BAKETEXTURE_COLOR_ILLUM | BOOL |  |  |  | 
Shadows | BAKETEXTURE_COLOR_SHADOWS | BOOL |  |  |  | 
Luminance | BAKETEXTURE_COLOR_LUMINANCE | BOOL |  |  |  | 
Diffusion | BAKETEXTURE_COLOR_DIFFUSION | BOOL |  |  |  | 
Diffusion | BAKETEXTURE_LUMINANCE_DIFFUSION | BOOL |  |  |  | 
Shadows | BAKETEXTURE_ILLUMINATION_SHADOWS | BOOL |  |  |  | 
Source | BAKETEXTURE_NORMAL_SOURCE | LINK |  |  |  | 
Method | BAKETEXTURE_NORMAL_METHOD | LONG |  |  |  | BAKETEXTURE_NORMAL_METHOD_OBJECT; BAKETEXTURE_NORMAL_METHOD_TANGENT; BAKETEXTURE_NORMAL_METHOD_WORLD
Flip X | BAKETEXTURE_NORMAL_FLIP_X | BOOL |  |  |  | 
Flip Y | BAKETEXTURE_NORMAL_FLIP_Y | BOOL |  |  |  | 
Flip Z | BAKETEXTURE_NORMAL_FLIP_Z | BOOL |  |  |  | 
Swap Y &amp; Z | BAKETEXTURE_NORMAL_SWAP_YZ | BOOL |  |  |  | 
Self Shadowing Only | BAKETEXTURE_AO_SELFINTERSECTION | BOOL |  |  |  | 
To Vertex Map | BAKETEXTURE_AO_TO_VERTEX | BOOL |  |  |  | 
Source | BAKETEXTURE_DISPLACEMENT_SOURCE | LINK |  |  |  | 
Height | BAKETEXTURE_DISPLACEMENT_HEIGHT | REAL |  |  |  | 
Method | BAKETEXTURE_DISPLACEMENT_METHOD | LONG |  |  |  | BAKETEXTURE_DISPLACEMENT_METHOD_INTENSITY; BAKETEXTURE_DISPLACEMENT_METHOD_CENTEREDINTENSITY; BAKETEXTURE_DISPLACEMENT_METHOD_REDGREEN; BAKETEXTURE_DISPLACEMENT_METHOD_OBJECT; BAKETEXTURE_DISPLACEMENT_METHOD_TANGENT; BAKETEXTURE_DISPLACEMENT_METHOD_WORLD
Sub Polygon Displacement | BAKETEXTURE_DISPLACEMENT_SUBPOLY | BOOL |  |  |  | 
Subdivision Level | BAKETEXTURE_DISPLACEMENT_SUBPOLY_SUBDIVISION | LONG | 1 | 12 |  | 
Round Geometry | BAKETEXTURE_DISPLACEMENT_SUBPOLY_ROUND | BOOL |  |  |  | 
Round Contour | BAKETEXTURE_DISPLACEMENT_SUBPOLY_ROUNDCONTOUR | BOOL |  |  |  | 
Map Rounded Geometry | BAKETEXTURE_DISPLACEMENT_SUBPOLY_HQREMAPPING | BOOL |  |  |  | 
Map Resulting Geometry | BAKETEXTURE_DISPLACEMENT_SUBPOLY_MAPRESULT | BOOL |  |  |  | 
Keep Original Edges | BAKETEXTURE_DISPLACEMENT_SUBPOLY_KEEPEDGES | BOOL |  |  |  | 
Best Distribution | BAKETEXTURE_DISPLACEMENT_SUBPOLY_DISTRIBUTION | BOOL |  |  |  | 
Use Max Ray Cast Distance | BAKETEXTURE_RAYCAST_USE_MAX_DISTANCE | BOOL |  |  |  | 
Custom Ray Cast Distance | BAKETEXTURE_RAYCAST_CUSTOM_MAX_DISTANCE | REAL | 0.0 |  |  | 
Use Auto Spike Filter Threshold | BAKETEXTURE_RAYCAST_USE_AUTO_SPIKE_THRESHOLD | BOOL |  |  |  | 
Custom Spike Filter Threshold | BAKETEXTURE_RAYCAST_CUSTOM_SPIKE_THRESHOLD | REAL | 0 | 100 |  | 
Auto UV | BAKETEXTURE_MAPPING | LONG |  |  |  | BAKETEXTURE_MAPPING_OFF; BAKETEXTURE_MAPPING_PACKED; BAKETEXTURE_MAPPING_CUBIC; BAKETEXTURE_MAPPING_ANGLE
Relax | BAKETEXTURE_RELAXCOUNT | LONG | 0 |  |  | 
Bake | BAKETEXTURE_BAKE | BUTTON |  |  |  | 
Stop | BAKETEXTURE_STOP | BUTTON |  |  |  | 
Delete | BAKETEXTURE_DELETE | BUTTON |  |  |  | 
Preview | BAKETEXTURE_BAKE_PREVIEW | BUTTON |  |  |  | 
No label | BAKETEXTURE_PREVIEW | MATPREVIEW |  |  |  | 
Use Current Render Data | BAKETEXTURE_USE_CURRENT | BOOL |  |  |  | 
Start  Time | BAKETEXTURE_TIME_MIN | BASETIME |  |  |  | 
End Time | BAKETEXTURE_TIME_MAX | BASETIME |  |  |  | 
Frame Rate | BAKETEXTURE_FPS | LONG | 1 |  |  | 
Name Format | BAKETEXTURE_NAME_FORMAT | LONG |  |  |  | BAKETEXTURE_NAME_0000_TIF; BAKETEXTURE_NAME0000_TIF; BAKETEXTURE_NAME0000; BAKETEXTURE_NAME_0000; BAKETEXTURE_NAME000_TIF; BAKETEXTURE_NAME000; BAKETEXTURE_NAME_000
Material Tags | BAKETEXTURE_TAGLIST | IN_EXCLUDE |  |  |  | 
