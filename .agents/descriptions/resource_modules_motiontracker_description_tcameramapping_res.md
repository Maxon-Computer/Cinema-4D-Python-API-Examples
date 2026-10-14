# Description: Camera Calibrator

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/motiontracker/description/tcameramapping.res`
- **Symbol:** `Tcameramapping`
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
Image | CM_IMAGE_FILENAME | FILENAME |  |  |  | 
Film Aspect | CM_RDATA_FILMASPECT | REAL | 0.001 | 1000.0 |  | 
No label | CM_RDATA_FILMPRESET | LONG |  |  |  | CM_RDATA_FILMPRESET_CUSTOM; CM_RDATA_FILMPRESET_SQUARE; CM_RDATA_FILMPRESET_STANDARD; CM_RDATA_FILMPRESET_HDTV; CM_RDATA_FILMPRESET_35MMSTILL; CM_RDATA_FILMPRESET_WIDESCREEN; CM_RDATA_FILMPRESET_35MM; CM_RDATA_FILMPRESET_PANAVISION
No label | CM_RDATA_RENDER_FILM_ASPECT | STATICTEXT |  |  |  | 
Lens Profile | CM_LENS_PROFILE_FILENAME | FILENAME |  |  |  | 
No label | CM_LENS_PROFILE_TYPE | STATICTEXT |  |  |  | 
No label | CM_LENS_PARAM_RC_00 | STATICTEXT |  |  |  | 
No label | CM_LENS_PARAM_RC_01 | STATICTEXT |  |  |  | 
No label | CM_LENS_PARAM_RC_02 | STATICTEXT |  |  |  | 
No label | CM_LENS_PARAM_RC_03 | STATICTEXT |  |  |  | 
No label | CM_LENS_PARAM_RC_04 | STATICTEXT |  |  |  | 
No label | CM_LENS_PARAM_RC_05 | STATICTEXT |  |  |  | 
No label | CM_LENS_PARAM_RC_10 | STATICTEXT |  |  |  | 
No label | CM_LENS_PARAM_RC_11 | STATICTEXT |  |  |  | 
No label | CM_LENS_PARAM_RC_12 | STATICTEXT |  |  |  | 
No label | CM_LENS_PARAM_RC_13 | STATICTEXT |  |  |  | 
No label | CM_LENS_PARAM_RC_14 | STATICTEXT |  |  |  | 
No label | CM_LENS_PARAM_RC_15 | STATICTEXT |  |  |  | 
No label | CM_LENS_PARAM_RC_20 | STATICTEXT |  |  |  | 
No label | CM_LENS_PARAM_RC_21 | STATICTEXT |  |  |  | 
No label | CM_LENS_PARAM_RC_22 | STATICTEXT |  |  |  | 
No label | CM_LENS_PARAM_RC_23 | STATICTEXT |  |  |  | 
No label | CM_LENS_PARAM_RC_24 | STATICTEXT |  |  |  | 
No label | CM_LENS_PARAM_RC_25 | STATICTEXT |  |  |  | 
No label | CM_LENS_PARAM_RC_30 | STATICTEXT |  |  |  | 
No label | CM_LENS_PARAM_RC_31 | STATICTEXT |  |  |  | 
No label | CM_LENS_PARAM_RC_32 | STATICTEXT |  |  |  | 
No label | CM_LENS_PARAM_RC_33 | STATICTEXT |  |  |  | 
No label | CM_LENS_PARAM_RC_34 | STATICTEXT |  |  |  | 
No label | CM_LENS_PARAM_RC_35 | STATICTEXT |  |  |  | 
No label | CM_LENS_PARAM_RC_40 | STATICTEXT |  |  |  | 
No label | CM_LENS_PARAM_RC_41 | STATICTEXT |  |  |  | 
No label | CM_LENS_PARAM_RC_42 | STATICTEXT |  |  |  | 
No label | CM_LENS_PARAM_RC_43 | STATICTEXT |  |  |  | 
No label | CM_LENS_PARAM_RC_44 | STATICTEXT |  |  |  | 
No label | CM_LENS_PARAM_RC_45 | STATICTEXT |  |  |  | 
Image Scale | CM_IMAGE_VIEW_SCALE | REAL | 1.0 | 10000.0 |  | 
Image Offset X | CM_IMAGE_VIEW_OFFSET_X | REAL | -500.0 | 500.0 |  | 
Show Image | CM_IMAGE_SHOW_IMAGE | BOOL |  |  |  | 
Image Offset Y | CM_IMAGE_VIEW_OFFSET_Y | REAL | -500.0 | 500.0 |  | 
Keep in Foreground | CM_IMAGE_USE_FOREGROUND_DISPLAY | BOOL |  |  |  | 
Brightness | CM_IMAGE_BRIGHTNESS | REAL | 0.0 | 200.0 |  | 
Full Image | CM_IMAGE_VIEW_FULL | BUTTON |  |  |  | 
Match Width | CM_IMAGE_MATCH_VIEW_WIDTH | BUTTON |  |  |  | 
Match Height | CM_IMAGE_MATCH_VIEW_HEIGHT | BUTTON |  |  |  | 
Add Line | ADD_NEW_LINE | BUTTON |  |  |  | 
Add Grid | ADD_NEW_GRID | BUTTON |  |  |  | 
Add Pin | ADD_NEW_PIN | BUTTON |  |  |  | 
Delete Line | DELETE_LINE | BUTTON |  |  |  | 
Delete Grid | DELETE_GRID | BUTTON |  |  |  | 
Delete Pin | DELETE_PIN | BUTTON |  |  |  | 
Selection | IDC_SELECTED_STR | STATICTEXT |  |  |  | 
No label | IDC_SELECTED_STATE | STATICTEXT |  |  |  | 
Known Length  | CM_LINE_AXIS_STR | STATICTEXT |  |  |  | 
No label | CM_LINE_HAS_MEASUREMENT | BOOL |  |  |  | 
No label | CM_LINE_WORLD_LENGTH | REAL | 0.0 |  |  | 
Known Length  | CM_GRID_AXIS_A_STR | STATICTEXT |  |  |  | 
No label | CM_GRID_HAS_MEASUREMENT_A | BOOL |  |  |  | 
No label | CM_GRID_WORLD_LENGTH_A | REAL | 0.0 |  |  | 
Known Length  | CM_GRID_AXIS_B_STR | STATICTEXT |  |  |  | 
No label | CM_GRID_HAS_MEASUREMENT_B | BOOL |  |  |  | 
No label | CM_GRID_WORLD_LENGTH_B | REAL | 0.0 |  |  | 
Aspect | CM_GRID_ASPECT_STR | STATICTEXT |  |  |  | 
No label | CM_GRID_HAS_ASPECT | BOOL |  |  |  | 
No label | CM_GRID_WORLD_ASPECT_A_OVER_B_USER | REAL | 0.0 |  |  | 
No label | CM_GRID_WORLD_ASPECT_A_OVER_B_CAL | STATICTEXT |  |  |  | 
Axis  | CM_GRID_AXIS_AA_STR | STATICTEXT |  |  |  | 
Segments | CM_NUM_GRID_SEGMENTS_A_STR | STATICTEXT |  |  |  | 
No label | CM_NUM_GRID_SEGMENTS_0 | LONG | 1 | 100 |  | 
Offset | CM_GRID_OFFSET_A_STR | STATICTEXT |  |  |  | 
No label | CM_GRID_OFFSET_0 | REAL | 0.0 | 100.0 |  | 
Axis  | CM_GRID_AXIS_BB_STR | STATICTEXT |  |  |  | 
Segments | CM_NUM_GRID_SEGMENTS_B_STR | STATICTEXT |  |  |  | 
No label | CM_NUM_GRID_SEGMENTS_1 | LONG | 1 | 100 |  | 
Offset | CM_GRID_OFFSET_B_STR | STATICTEXT |  |  |  | 
No label | CM_GRID_OFFSET_1 | REAL | 0.0 | 100.0 |  | 
Coordinates | CM_PIN_COORDS_STR | STATICTEXT |  |  |  | 
No label | CM_PIN_COORDS | VECTOR |  |  |  | 
Calibration Status | IDC_STATUS_STR | STATICTEXT |  |  |  | 
X Vanishing Point | IDC_X_VP_STR | STATICTEXT |  |  |  | 
No label | COLOR_X_VP_STATE | COLORBAR |  |  |  | 
No label | IDC_X_VP_STATE | VARTEXT |  |  |  | 
Y Vanishing Point | IDC_Y_VP_STR | STATICTEXT |  |  |  | 
No label | COLOR_Y_VP_STATE | COLORBAR |  |  |  | 
No label | IDC_Y_VP_STATE | VARTEXT |  |  |  | 
Z Vanishing Point | IDC_Z_VP_STR | STATICTEXT |  |  |  | 
No label | COLOR_Z_VP_STATE | COLORBAR |  |  |  | 
No label | IDC_Z_VP_STATE | VARTEXT |  |  |  | 
Camera Focal length | IDC_CAM_CAL_FOCAL_STATE_STR | STATICTEXT |  |  |  | 
No label | COLOR_CAM_CAL_FOCAL_STATE | COLORBAR |  |  |  | 
No label | IDC_CAM_CAL_FOCAL_STATE | VARTEXT |  |  |  | 
Camera Orientation | IDC_CAM_CAL_ORIENTATION_STATE_STR | STATICTEXT |  |  |  | 
No label | COLOR_CAM_CAL_ORIENTATION_STATE | COLORBAR |  |  |  | 
No label | IDC_CAM_CAL_ORIENTATION_STATE | VARTEXT |  |  |  | 
Camera Position | IDC_CAM_CAL_POS_STATE_STR | STATICTEXT |  |  |  | 
No label | COLOR_CAM_CAL_POS_STATE | COLORBAR |  |  |  | 
No label | IDC_CAM_CAL_POS_STATE | VARTEXT |  |  |  | 
35mm Equiv. Focal Length | IDC_CAMERA_CALIBRATOR_FOCAL_LENGTH_35MM_EQUIV | STATICTEXT |  |  |  | 
Create Camera Mapping Tag | CREATE_CAMERA_MAPPING_TEXTURE_TAG | BUTTON |  |  |  | 
Create Background Object | CREATE_BACKGROUND_OBJECT | BUTTON |  |  |  | 
Calculate PP for 3VPs | CM_CALC_PP_WHEN_3VPS | BOOL |  |  |  | 
Offset Magnifier | CM_LOUPE_USE_OFFSET | BOOL |  |  |  | 
Magnifier Zoom Value | CM_LOUPE_MAGNIFICATION | REAL | 100.0 | 1000.0 |  | 
Magnifier Size | CM_LOUPE_SIZE_PIX | REAL | 8.0 | 512.0 |  | 
No label | LINKED_ELEMENT_LIST | IN_EXCLUDE |  |  |  | 
