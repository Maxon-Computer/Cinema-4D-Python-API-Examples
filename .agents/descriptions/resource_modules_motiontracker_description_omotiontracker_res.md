# Description: Motion Tracker Object

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/motiontracker/description/omotiontracker.res`
- **Symbol:** `Omotiontracker`
- **Category:** Objects

Use parameter symbols to access parameters and cycle option symbols for cycle values, never their numeric IDs. Treat Min and Max as constraints and Default as the declared initial value; blank cells mean the resource does not declare that metadata, not that the value is zero. Base Description Parameters lists inherited fields from each base; All Parameters lists the effective parameter set for this description.

## Base Description Parameters

### Base Object (`Obase`)

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Icon Color | ID_BASELIST_ICON_COLORIZE_MODE | LONG |  |  |  | ID_BASELIST_ICON_COLORIZE_MODE_NONE; ID_BASELIST_ICON_COLORIZE_MODE_DISPLAYCOLOR; ID_BASELIST_ICON_COLORIZE_MODE_CUSTOM
Viewport Visibility | ID_BASEOBJECT_VISIBILITY_EDITOR | LONG |  |  |  | OBJECT_UNDEF; OBJECT_ON; OBJECT_OFF
Renderer Visibility | ID_BASEOBJECT_VISIBILITY_RENDER | LONG |  |  |  | OBJECT_UNDEF; OBJECT_ON; OBJECT_OFF
Enabled | ID_BASEOBJECT_GENERATOR_FLAG | BOOL |  |  |  | 
Display Color | ID_BASEOBJECT_USECOLOR | LONG |  |  |  | ID_BASEOBJECT_USECOLOR_OFF; ID_BASEOBJECT_USECOLOR_LAYER; ID_BASEOBJECT_USECOLOR_AUTOMATIC; ID_BASEOBJECT_USECOLOR_ALWAYS
Color | ID_BASEOBJECT_COLOR | COLOR |  |  |  | 
X-Ray | ID_BASEOBJECT_XRAY | BOOL |  |  |  | 
Position | ID_BASEOBJECT_REL_POSITION | VECTOR |  |  |  | 
Rotation | ID_BASEOBJECT_REL_ROTATION | VECTOR |  |  |  | 
Scale | ID_BASEOBJECT_REL_SCALE | VECTOR |  |  |  | 
Rotation Order | ID_BASEOBJECT_ROTATION_ORDER | LONG |  |  |  | ID_BASEOBJECT_ROTATION_ORDER_HPB; ID_BASEOBJECT_ROTATION_ORDER_XYZ; ID_BASEOBJECT_ROTATION_ORDER_XZY; ID_BASEOBJECT_ROTATION_ORDER_YXZ; ID_BASEOBJECT_ROTATION_ORDER_YZX; ID_BASEOBJECT_ROTATION_ORDER_ZXY; ID_BASEOBJECT_ROTATION_ORDER_ZYX
Quaternion Rotation | ID_BASEOBJECT_QUATERNION_ROTATION_INTERPOLATION | BOOL |  |  |  | 
Freeze All | ID_BASEOBJECT_FREEZE | BUTTON |  |  |  | 
Unfreeze All | ID_BASEOBJECT_FROZEN_RESET | BUTTON |  |  |  | 
Frozen Position | ID_BASEOBJECT_FROZEN_POSITION | VECTOR |  |  |  | 
Freeze P | ID_BASEOBJECT_FREEZE_P | BUTTON |  |  |  | 
Frozen Rotation | ID_BASEOBJECT_FROZEN_ROTATION | VECTOR |  |  |  | 
Freeze R | ID_BASEOBJECT_FREEZE_R | BUTTON |  |  |  | 
Frozen Scale | ID_BASEOBJECT_FROZEN_SCALE | VECTOR |  |  |  | 
Freeze S | ID_BASEOBJECT_FREEZE_S | BUTTON |  |  |  | 
Deform Position | ID_BASEOBJECT_DEFORM_POSITION | VECTOR |  |  |  | 
Deform Rotation | ID_BASEOBJECT_DEFORM_ROTATION | VECTOR |  |  |  | 
Deform Scale | ID_BASEOBJECT_DEFORM_SCALE | VECTOR |  |  |  | 
Global Position | ID_BASEOBJECT_GLOBAL_POSITION | VECTOR |  |  |  | 
Global Rotation | ID_BASEOBJECT_GLOBAL_ROTATION | VECTOR |  |  |  | 
Transformed Position | ID_BASEOBJECT_ABS_POSITION | VECTOR |  |  |  | 
Transformed Scale | ID_BASEOBJECT_ABS_SCALE | VECTOR |  |  |  | 
Transformed Rotation | ID_BASEOBJECT_ABS_ROTATION | VECTOR |  |  |  | 

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
Color | ID_BASELIST_ICON_COLOR | COLOR |  |  | 1.0 0.9 0.4 | 
No label | ID_BASELIST_ICON_PRESET_BUTTONS | ICONCHOOSER |  |  |  | 
Name | ID_BASELIST_NAME | STRING |  |  |  | 
Layer | ID_LAYER_LINK | LINK |  |  |  | 
No label | ID_BASELIST_NODESPACE_ADD_REMOVE_BUTTONS | NODESPACE_ADD_REMOVE |  |  |  | 
Icon Color | ID_BASELIST_ICON_COLORIZE_MODE | LONG |  |  |  | ID_BASELIST_ICON_COLORIZE_MODE_NONE; ID_BASELIST_ICON_COLORIZE_MODE_DISPLAYCOLOR; ID_BASELIST_ICON_COLORIZE_MODE_CUSTOM
Viewport Visibility | ID_BASEOBJECT_VISIBILITY_EDITOR | LONG |  |  |  | OBJECT_UNDEF; OBJECT_ON; OBJECT_OFF
Renderer Visibility | ID_BASEOBJECT_VISIBILITY_RENDER | LONG |  |  |  | OBJECT_UNDEF; OBJECT_ON; OBJECT_OFF
Enabled | ID_BASEOBJECT_GENERATOR_FLAG | BOOL |  |  |  | 
Display Color | ID_BASEOBJECT_USECOLOR | LONG |  |  |  | ID_BASEOBJECT_USECOLOR_OFF; ID_BASEOBJECT_USECOLOR_LAYER; ID_BASEOBJECT_USECOLOR_AUTOMATIC; ID_BASEOBJECT_USECOLOR_ALWAYS
Color | ID_BASEOBJECT_COLOR | COLOR |  |  |  | 
X-Ray | ID_BASEOBJECT_XRAY | BOOL |  |  |  | 
Position | ID_BASEOBJECT_REL_POSITION | VECTOR |  |  |  | 
Rotation | ID_BASEOBJECT_REL_ROTATION | VECTOR |  |  |  | 
Scale | ID_BASEOBJECT_REL_SCALE | VECTOR |  |  |  | 
Rotation Order | ID_BASEOBJECT_ROTATION_ORDER | LONG |  |  |  | ID_BASEOBJECT_ROTATION_ORDER_HPB; ID_BASEOBJECT_ROTATION_ORDER_XYZ; ID_BASEOBJECT_ROTATION_ORDER_XZY; ID_BASEOBJECT_ROTATION_ORDER_YXZ; ID_BASEOBJECT_ROTATION_ORDER_YZX; ID_BASEOBJECT_ROTATION_ORDER_ZXY; ID_BASEOBJECT_ROTATION_ORDER_ZYX
Quaternion Rotation | ID_BASEOBJECT_QUATERNION_ROTATION_INTERPOLATION | BOOL |  |  |  | 
Freeze All | ID_BASEOBJECT_FREEZE | BUTTON |  |  |  | 
Unfreeze All | ID_BASEOBJECT_FROZEN_RESET | BUTTON |  |  |  | 
Frozen Position | ID_BASEOBJECT_FROZEN_POSITION | VECTOR |  |  |  | 
Freeze P | ID_BASEOBJECT_FREEZE_P | BUTTON |  |  |  | 
Frozen Rotation | ID_BASEOBJECT_FROZEN_ROTATION | VECTOR |  |  |  | 
Freeze R | ID_BASEOBJECT_FREEZE_R | BUTTON |  |  |  | 
Frozen Scale | ID_BASEOBJECT_FROZEN_SCALE | VECTOR |  |  |  | 
Freeze S | ID_BASEOBJECT_FREEZE_S | BUTTON |  |  |  | 
Deform Position | ID_BASEOBJECT_DEFORM_POSITION | VECTOR |  |  |  | 
Deform Rotation | ID_BASEOBJECT_DEFORM_ROTATION | VECTOR |  |  |  | 
Deform Scale | ID_BASEOBJECT_DEFORM_SCALE | VECTOR |  |  |  | 
Global Position | ID_BASEOBJECT_GLOBAL_POSITION | VECTOR |  |  |  | 
Global Rotation | ID_BASEOBJECT_GLOBAL_ROTATION | VECTOR |  |  |  | 
Transformed Position | ID_BASEOBJECT_ABS_POSITION | VECTOR |  |  |  | 
Transformed Scale | ID_BASEOBJECT_ABS_SCALE | VECTOR |  |  |  | 
Transformed Rotation | ID_BASEOBJECT_ABS_ROTATION | VECTOR |  |  |  | 
Footage | PH_FOOTAGE_FILENAME | FILENAME |  |  |  | 
Lens Profile | PH_LENS_PROFILE_FILENAME | FILENAME |  |  |  | 
No label | PH_LENS_PROFILE_TYPE | STATICTEXT |  |  |  | 
No label | PH_LENS_PARAM_RC_00 | STATICTEXT |  |  |  | 
No label | PH_LENS_PARAM_RC_01 | STATICTEXT |  |  |  | 
No label | PH_LENS_PARAM_RC_02 | STATICTEXT |  |  |  | 
No label | PH_LENS_PARAM_RC_03 | STATICTEXT |  |  |  | 
No label | PH_LENS_PARAM_RC_04 | STATICTEXT |  |  |  | 
No label | PH_LENS_PARAM_RC_05 | STATICTEXT |  |  |  | 
No label | PH_LENS_PARAM_RC_10 | STATICTEXT |  |  |  | 
No label | PH_LENS_PARAM_RC_11 | STATICTEXT |  |  |  | 
No label | PH_LENS_PARAM_RC_12 | STATICTEXT |  |  |  | 
No label | PH_LENS_PARAM_RC_13 | STATICTEXT |  |  |  | 
No label | PH_LENS_PARAM_RC_14 | STATICTEXT |  |  |  | 
No label | PH_LENS_PARAM_RC_15 | STATICTEXT |  |  |  | 
No label | PH_LENS_PARAM_RC_20 | STATICTEXT |  |  |  | 
No label | PH_LENS_PARAM_RC_21 | STATICTEXT |  |  |  | 
No label | PH_LENS_PARAM_RC_22 | STATICTEXT |  |  |  | 
No label | PH_LENS_PARAM_RC_23 | STATICTEXT |  |  |  | 
No label | PH_LENS_PARAM_RC_24 | STATICTEXT |  |  |  | 
No label | PH_LENS_PARAM_RC_25 | STATICTEXT |  |  |  | 
No label | PH_LENS_PARAM_RC_30 | STATICTEXT |  |  |  | 
No label | PH_LENS_PARAM_RC_31 | STATICTEXT |  |  |  | 
No label | PH_LENS_PARAM_RC_32 | STATICTEXT |  |  |  | 
No label | PH_LENS_PARAM_RC_33 | STATICTEXT |  |  |  | 
No label | PH_LENS_PARAM_RC_34 | STATICTEXT |  |  |  | 
No label | PH_LENS_PARAM_RC_35 | STATICTEXT |  |  |  | 
No label | PH_LENS_PARAM_RC_40 | STATICTEXT |  |  |  | 
No label | PH_LENS_PARAM_RC_41 | STATICTEXT |  |  |  | 
No label | PH_LENS_PARAM_RC_42 | STATICTEXT |  |  |  | 
No label | PH_LENS_PARAM_RC_43 | STATICTEXT |  |  |  | 
No label | PH_LENS_PARAM_RC_44 | STATICTEXT |  |  |  | 
No label | PH_LENS_PARAM_RC_45 | STATICTEXT |  |  |  | 
Resampling | PH_FOOTAGE_DOWNSAMPLING_FACTOR | REAL | 1.0 | 100.0 |  | 
Film Aspect | PH_RDATA_FILMASPECT | REAL | 0.01 | 100.0 |  | 
No label | PH_RDATA_FILMPRESET | LONG |  |  |  | PH_RDATA_FILMPRESET_CUSTOM; PH_RDATA_FILMPRESET_SQUARE; PH_RDATA_FILMPRESET_STANDARD; PH_RDATA_FILMPRESET_HDTV; PH_RDATA_FILMPRESET_35MMSTILL; PH_RDATA_FILMPRESET_WIDESCREEN; PH_RDATA_FILMPRESET_35MM; PH_RDATA_FILMPRESET_PANAVISION
No label | PH_RDATA_RENDER_FILM_ASPECT | STATICTEXT |  |  |  | 
Frame Start | PH_FOOTAGE_TRACK_FRAME_START | LONG | 0 |  |  | 
Frame Stop | PH_FOOTAGE_TRACK_FRAME_STOP | LONG | 0 |  |  | 
Footage Scale | PH_FOOTAGE_VIEW_SCALE | REAL | 1.0 | 10000.0 |  | 
Footage Offset X | PH_FOOTAGE_VIEW_OFFSET_X | REAL |  |  |  | 
Footage Offset Y | PH_FOOTAGE_VIEW_OFFSET_Y | REAL |  |  |  | 
No label | PH_FOOTAGE_OFFSET_TRACKS_SELECTED | BOOL |  |  |  | 
Full Footage | PH_FOOTAGE_VIEW_FULL | BUTTON |  |  |  | 
Match Width | PH_FOOTAGE_MATCH_VIEW_WIDTH | BUTTON |  |  |  | 
Match Height | PH_FOOTAGE_MATCH_VIEW_HEIGHT | BUTTON |  |  |  | 
Brightness | PH_FOOTAGE_BRIGHTNESS | REAL | 0.0 | 200.0 |  | 
Show Footage through Camera | PH_FOOTAGE_SHOW_IMAGE | BOOL |  |  |  | 
Create Background Object | PH_CREATE_BACKGROUND_OBJECT | BUTTON |  |  |  | 
No label | PH_FOOTAGE_INFO_BOX_00 | STATICTEXT |  |  |  | 
No label | PH_FOOTAGE_INFO_BOX_01 | STATICTEXT |  |  |  | 
No label | PH_FOOTAGE_INFO_BOX_02 | STATICTEXT |  |  |  | 
No label | PH_FOOTAGE_INFO_BOX_03 | STATICTEXT |  |  |  | 
No label | PH_2D_TRACK_SUBTAB_MODE | LONG |  |  |  | PH_SUBTAB_2D_TRACK_AUTO; PH_SUBTAB_2D_TRACK_MANUAL; PH_SUBTAB_2D_TRACK_DISPLAY
&lt; | PH_2D_TRACK_MANUAL_TRACK_BACKWARD | BUTTON |  |  |  | 
&lt; Manual Track &gt; | PH_2D_TRACK_MANUAL_TRACK | BUTTON |  |  |  | 
&gt; | PH_2D_TRACK_MANUAL_TRACK_FORWARD | BUTTON |  |  |  | 
No label | PH_2D_TRACK_USER_TRACKS_ITEMTREE | ITEMTREE |  |  |  | 
Virtual Keyframes | PH_2D_TRACK_USER_AUTOKEYING | BOOL |  |  |  | 
Mode | PH_2D_TRACK_USER_AUTOKEYING_MODE | LONG |  |  |  | PH_2D_TRACK_USER_AUTOKEYING_MODE_INTERVAL; PH_2D_TRACK_USER_AUTOKEYING_MODE_ERROR_THRESH_EXCEEDED; PH_2D_TRACK_USER_AUTOKEYING_MODE_ERROR_THRESH_PREVENT
Error Threshold | PH_2D_TRACK_USER_AUTOKEYING_ERROR_THRESHOLD | REAL |  |  |  | 
Frame Interval | PH_2D_TRACK_USER_AUTOKEYING_INTERVAL | LONG |  |  |  | 
Color Filter | PH_2D_TRACK_COLOR_MIX_PRESET | LONG |  |  |  | PH_2D_TRACK_COLOR_MIX_PRESET_LUMINANCE; PH_2D_TRACK_COLOR_MIX_PRESET_RED; PH_2D_TRACK_COLOR_MIX_PRESET_GREEN; PH_2D_TRACK_COLOR_MIX_PRESET_BLUE; PH_2D_TRACK_COLOR_MIX_PRESET_ENHANCED_RED; PH_2D_TRACK_COLOR_MIX_PRESET_ENHANCED_GREEN; PH_2D_TRACK_COLOR_MIX_PRESET_ENHANCED_BLUE; PH_2D_TRACK_COLOR_MIX_PRESET_CURRENT_DEFAULT; PH_2D_TRACK_COLOR_MIX_PRESET_SET_AS_DEFAULT; PH_2D_TRACK_COLOR_MIX_PRESET_CUSTOM
Filter.Red | PH_2D_TRACK_USER_redWeightActive | REAL | -200.0 | 200.0 |  | 
Filter.Green | PH_2D_TRACK_USER_greenWeightActive | REAL | -200.0 | 200.0 |  | 
Filter.Blue | PH_2D_TRACK_USER_blueWeightActive | REAL | -200.0 | 200.0 |  | 
Number of Tracks | PH_2D_TRACK_numFeatsTargetFullFrame | LONG | 1 | 10000 |  | 
Minimum Spacing | PH_2D_TRACK_minSpacing | LONG | 1 | 1000 |  | 
Auto Replace Lost Tracks | PH_2D_TRACK_autoReplaceLostFeatures | BOOL |  |  |  | 
Create Auto Tracks | PH_2D_TRACK_AUTO_CREATE_MARKERS | BUTTON |  |  |  | 
&lt; | PH_2D_TRACK_AUTO_TRACK_BACKWARD | BUTTON |  |  |  | 
&lt; Auto Track &gt; | PH_2D_TRACK_AUTO_TRACK | BUTTON |  |  |  | 
&gt; | PH_2D_TRACK_AUTO_TRACK_FORWARD | BUTTON |  |  |  | 
Delete Auto Tracks | PH_2D_TRACK_AUTO_RESET | BUTTON |  |  |  | 
No label | PH_2D_TRACK_FILTER_minTrackLen_Active | BOOL |  |  |  | 
Minimum Length (Frames) | PH_2D_TRACK_FILTER_minTrackLen | LONG | 2 | 200 |  | 
No label | PH_2D_TRACK_FILTER_maxAccel_Active | BOOL |  |  |  | 
Maximum Acceleration | PH_2D_TRACK_FILTER_maxAccel | REAL | 0.0 | 10.0 |  | 
No label | PH_2D_TRACK_FILTER_maxError_Active | BOOL |  |  |  | 
Error Threshold | PH_2D_TRACK_FILTER_maxError | REAL | 0.0 | 100.0 |  | 
No label | PH_2D_TRACK_FILTER_smartAccel_Active | BOOL |  |  |  | 
Smart Acceleration | PH_2D_TRACK_FILTER_smartAccel | REAL | 0.0 | 5.0 |  | 
Default Settings | PH_2D_TRACK_STR_SETTINGS | SEPARATOR |  |  |  | 
Default Pattern Size | PH_2D_TRACK_featSizeDefault | LONG | 3 | 10001 |  | 
Default Search Size | PH_2D_TRACK_trackWindowSizeDefault | LONG | 5 | 10001 |  | 
Default Pattern Shape | PH_2D_TRACK_circularFeatsDefault | LONG |  |  |  | PH_2D_TRACK_SQUARE_FEATURE; PH_2D_TRACK_CIRCLE_FEATURE
Display | PH_2D_TRACK_STR_DISPLAY | SEPARATOR |  |  |  | 
Track Display | PH_2D_TRACK_DISP_FEAT_MODE | LONG |  |  |  | PH_2D_TRACK_dispFeat_showFeat; PH_2D_TRACK_dispFeat_showFeatWithTrack; PH_2D_TRACK_dispFeat_none
Footage Display | PH_SHOW_TRACKER_VIEW_OF_FOOTAGE_MODE | LONG |  |  |  | PH_SHOW_TRACKER_VIEW_OF_FOOTAGE_MODE_ORIGINAL; PH_SHOW_TRACKER_VIEW_OF_FOOTAGE_MODE_TRACKER_VIEW
Display Pattern Box | PH_2D_TRACK_showFeatSize | BOOL |  |  |  | 
Display Search Box | PH_2D_TRACK_showTrackWindowSize | BOOL |  |  |  | 
Show Rekey Magnifier | PH_2D_TRACK_showMagnifierOnDrag | BOOL |  |  |  | 
Track Behavior | PH_2D_TRACK_STR_FEATURE_BEHAVIOUR | SEPARATOR |  |  |  | 
Default Red Weight | PH_2D_TRACK_USER_redWeightDefault | REAL | -200.0 | 200.0 |  | 
Default Green Weight | PH_2D_TRACK_USER_greenWeightDefault | REAL | -200.0 | 200.0 |  | 
Default Blue Weight | PH_2D_TRACK_USER_blueWeightDefault | REAL | -200.0 | 200.0 |  | 
Extrapolate Search Position | PH_2D_TRACK_useExtrapolated2dTracking | BOOL |  |  |  | 
Track List | PH_2D_TRACK_STR_TRACK_LIST | SEPARATOR |  |  |  | 
Object Tracker Prefix | PH_USE_VIRTUAL_OBJECT_PREFIX_FOR_TRACK_TREEVIEW | BOOL |  |  |  | 
No label | PH_3D_RECON_SUBTAB_MODE | LONG |  |  |  | PH_SUBTAB_3D_RECON_RECON; PH_SUBTAB_3D_RECON_DISPLAY
Solver Settings | PH_3D_RECON_STR_SOLVER_SETTINGS | SEPARATOR |  |  |  | 
Solve Mode | PH_SOLVE_MODE | LONG |  |  |  | PH_SOLVE_MODE_FULL_3D; PH_SOLVE_MODE_NODAL; PH_SOLVE_MODE_PLANAR
Camera Settings | PH_3D_RECON_STR_CAMERA_SETTINGS | SEPARATOR |  |  |  | 
Focal Length | PH_FOCAL_SOLVE_MODE | LONG |  |  |  | PH_FOCAL_MODE_UNKNOWN_VARIABLE; PH_FOCAL_MODE_UNKNOWN_FIXED; PH_FOCAL_MODE_KNOWN_FIXED
Focal Length | PH_FOCAL_KNOWN_FIXED | REAL | 1.0 | 10000.0 |  | 
No label | PH_CAMERAOBJECT_FOCUS_PRESET | LONG |  |  |  | PH_CAMERAOBJECT_FOCUS_PRESET_CUSTOM; PH_CAMERAOBJECT_FOCUS_PRESET_WIDESUPER; PH_CAMERAOBJECT_FOCUS_PRESET_WIDE; PH_CAMERAOBJECT_FOCUS_PRESET_C4D; PH_CAMERAOBJECT_FOCUS_PRESET_NORMAL; PH_CAMERAOBJECT_FOCUS_PRESET_PORTRAIT; PH_CAMERAOBJECT_FOCUS_PRESET_TELE; PH_CAMERAOBJECT_FOCUS_PRESET_TELESUPER
Sensor Size (Film Gate) | PH_APERTURE_KNOWN_FIXED | REAL | 1.0 | 2000.0 |  | 
No label | PH_CAMERAOBJECT_APERTURE_PRESET | LONG |  |  |  | PH_CAMERAOBJECT_APERTURE_PRESET_CUSTOM; PH_CAMERAOBJECT_APERTURE_PRESET_8; PH_CAMERAOBJECT_APERTURE_PRESET_16; PH_CAMERAOBJECT_APERTURE_PRESET_35MOVIE; PH_CAMERAOBJECT_APERTURE_PRESET_35STILL; PH_CAMERAOBJECT_APERTURE_PRESET_70
35mm Equiv. Focal Length: | PH_CAMERAOBJECT_APERTURE_35 | STATICTEXT |  |  |  | 
Field of View (Horizontal) | PH_CAMERAOBJECT_FOV | REAL | 0.2 | 174.0 |  | 
Field of View (Vertical) | PH_CAMERAOBJECT_FOV_VERTICAL | REAL | 0.2 | 174.0 |  | 
Lock Solved Data | PH_KEEP_BACKGROUND_RECON_WHEN_TRACK_2D_CHANGES | BOOL |  |  |  | 
Run 3D Solver | PH_3D_RECON_HIERARCHICAL_SOLVE_ALL_STAGES | BUTTON |  |  |  | 
Display Settings | PH_3D_RECON_STR_DISPLAY_SETTINGS | SEPARATOR |  |  |  | 
3D Feature Display | PH_3D_RECON_NULLOBJECT_DISPLAY_MODE | LONG |  |  |  | PH_3D_RECON_NULLOBJECT_DISPLAY_NONE; PH_3D_RECON_NULLOBJECT_DISPLAY_DOT; PH_3D_RECON_NULLOBJECT_DISPLAY_POINT; PH_3D_RECON_NULLOBJECT_DISPLAY_CIRCLE; PH_3D_RECON_NULLOBJECT_DISPLAY_RECTANGLE; PH_3D_RECON_NULLOBJECT_DISPLAY_DIAMOND; PH_3D_RECON_NULLOBJECT_DISPLAY_TRIANGLE; PH_3D_RECON_NULLOBJECT_DISPLAY_PENTAGON; PH_3D_RECON_NULLOBJECT_DISPLAY_HEXAGON; PH_3D_RECON_NULLOBJECT_DISPLAY_OCTAGON; PH_3D_RECON_NULLOBJECT_DISPLAY_STAR; PH_3D_RECON_NULLOBJECT_DISPLAY_AXIS; PH_3D_RECON_NULLOBJECT_DISPLAY_CUBE; PH_3D_RECON_NULLOBJECT_DISPLAY_PYRAMID; PH_3D_RECON_NULLOBJECT_DISPLAY_SPHERE
Radius | PH_3D_RECON_NULLOBJECT_RADIUS | REAL | 0.0 |  |  | 
Preset | PH_SR_PRESET_MODE | LONG |  |  |  | PH_SR_PRESET_MODE_PREVIEW; PH_SR_PRESET_MODE_MEDIUM; PH_SR_PRESET_MODE_HIGH; PH_SR_PRESET_MODE_CUSTOM
Iterations | PH_SR_NUM_EXPAND_FILTER_PASSES | LONG | 1 | 3 |  | 
Point Density | PH_SR_POINT_DENSITY | LONG | 1 | 8 |  | 
Patch Size | PH_SR_PATCH_SIZE_PIX | LONG | 3 |  |  | 
Filter Small Groups | PH_SR_RUN_FILTER_GROUPS_DBG | BOOL |  |  |  | 
Min Angle | PH_SR_MIN_BASELINE_ANGLE | REAL | 0.0 | 180.0 |  | 
Area Weight | PH_SR_OVERALL_AREA_WEIGHT | REAL | 0.0 | 100.0 |  | 
Photometric Weight | PH_SR_OVERALL_PHOTOMETRIC_WEIGHT | REAL | 0.0 | 100.0 |  | 
Export Partial Solves | PH_SR_EXPORT_PARTIAL_SOLVES_DBG | BOOL |  |  |  | 
Footage Subsampling | PH_SR_SUBSAMPLING_LEVEL | LONG | 0 |  |  | 
Cell Size | PH_SR_CELL_SIZE_PIX | LONG | 1 | 8 |  | 
Quality Threshold | PH_SR_NCC_THRESH | REAL | 0.0 | 100.0 |  | 
Min Image Set Size | PH_SR_MIN_NUM_SUPPORT_IMAGES | LONG | 2 |  |  | 
Max Frame Range | PH_SR_MAX_FRAME_OFFSET | LONG |  |  |  | 
Max Angle | PH_SR_MAX_BASELINE_ANGLE | REAL | 0.0 |  |  | 
Min Texture Detail | PH_SR_TEXTURE_DETAIL_THRESHOLD | REAL | 0.0 | 100.0 |  | 
Strict Compatibility Mode | PH_SR_STRICT_COMPAT_MODE_DBG | BOOL |  |  |  | 
Run Expansion Phase | PH_SR_RUN_EXPANSION_DBG | BOOL |  |  |  | 
Filter Outer | PH_SR_RUN_FILTER_OUTER_DBG | BOOL |  |  |  | 
Filter Visibility | PH_SR_RUN_FILTER_VISIBILITY_DBG | BOOL |  |  |  | 
Filter Surface | PH_SR_RUN_FILTER_SURFACE_DBG | BOOL |  |  |  | 
Ray Weight | PH_SR_OVERALL_RAY_WEIGHT | REAL | 0.0 | 100.0 |  | 
Selected Patch ID | PH_SR_SELECTED_PATCH_ID_DBG | STATICTEXT |  |  |  | 
Generate Point Cloud | PH_SR_RUN_SCENE_RECONSTRUCTION | BUTTON |  |  |  | 
Generate Mesh | PH_SR_UPDATE_SCENE_MESHING | BUTTON |  |  |  | 
System memory available (MB) | PH_FOOTAGE_SYS_MEMORY_AVAILABLE | STATICTEXT |  |  |  | 
No label | PH_GENERAL_INFO_BOX_00 | STATICTEXT |  |  |  | 
No label | PH_GENERAL_INFO_BOX_01 | STATICTEXT |  |  |  | 
No label | PH_GENERAL_INFO_BOX_02 | STATICTEXT |  |  |  | 
No label | PH_GENERAL_INFO_BOX_03 | STATICTEXT |  |  |  | 
No label | PH_GENERAL_INFO_BOX_04 | STATICTEXT |  |  |  | 
No label | PH_GENERAL_INFO_BOX_05 | STATICTEXT |  |  |  | 
Solve without Deferred | PH_DEBUG_3D_SOLVE_WITHOUT_DEFFERED | BUTTON |  |  |  | 
Solve Deferred | PH_3D_RECON_SOLVE_DEFERRED | BUTTON |  |  |  | 
Run Object Track Solver | PH_OBJECT_SOLVE | BUTTON |  |  |  | 
Dump Sel 2D Track Curr Frame | PH_SELECTED_TRACK_DATA_DUMP_CURR_FRAME | BUTTON |  |  |  | 
Force Re-export | PH_DEBUG_BUTTON_10 | BUTTON |  |  |  | 
Cancel Task | PH_DEBUG_BUTTON_11 | BUTTON |  |  |  | 
Reset tracking | PH_DEBUG_BUTTON_7 | BUTTON |  |  |  | 
No label | PH_DEBUG_BUTTON_15 | LONG |  |  |  | 
Export Partial Recon to Scene | PH_DEBUG_BUTTON_14 | BUTTON |  |  |  | 
Save Partial Reconstructions | PH_DEBUG_SAVE_PARTIAL_RECONSTRUCTIONS | BUTTON |  |  |  | 
Load Partial Reconstructions | PH_DEBUG_LOAD_PARTIAL_RECONSTRUCTIONS | BUTTON |  |  |  | 
Patch Export Test | PH_DEBUG_BUTTON_17 | BUTTON |  |  |  | 
SDK Test | PH_DEBUG_BUTTON_19 | BUTTON |  |  |  | 
Clone selected tracks | PH_DEBUG_BUTTON_18 | BUTTON |  |  |  | 
Discard track data for selected | PH_DEBUG_BUTTON_16 | BUTTON |  |  |  | 
