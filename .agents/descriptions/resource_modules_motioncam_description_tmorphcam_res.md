# Description: Camera Morph

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/motioncam/description/tmorphcam.res`
- **Symbol:** `tmorphcam`
- **Category:** Tags

Use parameter symbols to access parameters and cycle option symbols for cycle values, never their numeric IDs. Treat Min and Max as constraints and Default as the declared initial value; blank cells mean the resource does not declare that metadata, not that the value is zero. Base Description Parameters lists inherited fields from each base; All Parameters lists the effective parameter set for this description.

## Base Description Parameters

### Expression (`Texpression`)

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Priority | EXPRESSION_PRIORITY | PRIORITY |  |  |  | 
Enable | EXPRESSION_ENABLE | BOOL |  |  |  | 

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
Priority | EXPRESSION_PRIORITY | PRIORITY |  |  |  | 
Enable | EXPRESSION_ENABLE | BOOL |  |  |  | 
Show Position | TMORPHCAM_VISUALIZATION_POS | BOOL |  |  |  | 
Show Alignment | TMORPHCAM_VISUALIZATION_ALIGN | BOOL |  |  |  | 
Show Names | TMORPHCAM_VISUALIZATION_NAMES | BOOL |  |  |  | 
Use Custom Camera Color | TMORPHCAM_VISUALIZATION_CAM_ENABLED | BOOL |  |  |  | 
Camera Color | TMORPHCAM_VISUALIZATION_CAM_COLOR | COLOR |  |  |  | 
Blend | TMORPHCAM_BLEND | REAL | 0.0 | 100.0 |  | 
Blend Curve | TMORPHCAM_BLEND_CURVE | SPLINE |  |  |  | 
Morph Interpolation | TMORPHCAM_INTERPOLATION | LONG |  |  |  | TMORPHCAM_INTERPOLATION_LINEAR; TMORPHCAM_INTERPOLATION_CUBIC; TMORPHCAM_INTERPOLATION_AKIMA
Stabilize | TMORPHCAM_STEADY | BOOL |  |  |  | 
Stabilizing Object | TMORPHCAM_STEADY_LINK | LINK |  |  |  | 
Source Mode | TMORPHCAM_LIST_MODE | LONG |  |  |  | TMORPHCAM_LIST_MODE_SIMPLE; TMORPHCAM_LIST_MODE_MULTI
Simple Morph: Camera 1 | TMORPHCAM_LIST_LINK_A | LINK |  |  |  | 
Simple Morph: Camera 2 | TMORPHCAM_LIST_LINK_B | LINK |  |  |  | 
Multi Morph: List | TMORPHCAM_LIST_LINKS | IN_EXCLUDE |  |  |  | 
Morph Focal Length | TMORPHCAM_TRACK_FOCALLENGTH | BOOL |  |  |  | 
Morph Sensor Size | TMORPHCAM_TRACK_APERTURE | BOOL |  |  |  | 
Morph Focus Distance | TMORPHCAM_TRACK_TARGETDIST | BOOL |  |  |  | 
Morph Depth of Field | TMORPHCAM_TRACK_DOF | BOOL |  |  |  | 
Morph White Balance | TMORPHCAM_TRACK_WB | BOOL |  |  |  | 
Morph Stereo Parameters | TMORPHCAM_TRACK_STEREO | BOOL |  |  |  | 
Physical Attributes | TMORPHCAM_TRACK_PHY | SEPARATOR |  |  |  | 
Morph F-Stop | TMORPHCAM_TRACK_PHY_FNUMBER | BOOL |  |  |  | 
Morph ISO/Gain | TMORPHCAM_TRACK_PHY_ISOGAIN | BOOL |  |  |  | 
Morph Shutter | TMORPHCAM_TRACK_PHY_SHUTTER | BOOL |  |  |  | 
Morph Lens Distortion | TMORPHCAM_TRACK_PHY_LENSDIST | BOOL |  |  |  | 
Morph Vignetting | TMORPHCAM_TRACK_PHY_VIGNETTE | BOOL |  |  |  | 
Morph Chromatic Aberration | TMORPHCAM_TRACK_PHY_ABERRATION | BOOL |  |  |  | 
