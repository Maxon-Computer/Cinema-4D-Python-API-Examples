# Description: Pose Morph

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/ca/description/tcaposemorph.res`
- **Symbol:** `Tcaposemorph`
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
Base Priority | ID_CA_POSE_BASE_PRI | PRIORITY |  |  |  | 
Position | ID_CA_POSE_P | BOOL |  |  |  | 
Rotation | ID_CA_POSE_R | BOOL |  |  |  | 
Scale | ID_CA_POSE_S | BOOL |  |  |  | 
Points | ID_CA_POSE_POINTS | BOOL |  |  |  | 
UV | ID_CA_POSE_UV | BOOL |  |  |  | 
Parameters | ID_CA_POSE_PARAM | BOOL |  |  |  | 
Hierarchy | ID_CA_POSE_HIERARCHY | BOOL |  |  |  | 
User Data | ID_CA_POSE_USERDATA | BOOL |  |  |  | 
Maps | ID_CA_POSE_MAPS | BOOL |  |  |  | 
Normal | ID_CA_POSE_NORMAL | BOOL |  |  |  | 
Draw PSD Drivers | ID_CA_POSE_OPTIONS_PSD_DRAWDRIVER | BOOL |  |  |  | 
PSD Driver Color | ID_CA_POSE_OPTIONS_PSD_DRIVERCOLOR | COLOR |  |  |  | 
Position Threshold | ID_CA_POSE_OPTIONS_PSD_POS_THRESHOLD | REAL | 0.0 | 100000.0 |  | 
Orient Threshold | ID_CA_POSE_OPTIONS_PSD_ORIENT_THRESHOLD | REAL | 0.0 | 180.0 |  | 
Twist Threshold | ID_CA_POSE_OPTIONS_PSD_TWIST_THRESHOLD | REAL | 0.0 | 180.0 |  | 
Memory Used :  | ID_CA_POSE_MEMORY_USED | STATICTEXT |  |  |  | 
Mode | ID_CA_POSE_MODE | LONG |  |  |  | ID_CA_POSE_MODE_EDIT; ID_CA_POSE_MODE_ANIMATE
Poses | ID_CA_POSE_MORPHS | ITEMTREE |  |  |  | 
Add Pose | ID_CA_POSE_ADDMORPH | BUTTON |  |  |  | 
Edit | ID_CA_POSE_EDIT_MODE | LONG |  |  |  | ID_CA_POSE_EDIT_MODE_OFF; ID_CA_POSE_EDIT_MODE_TARGET; ID_CA_POSE_EDIT_MODE_INPLACE
Mixing | ID_CA_POSE_MIXING | LONG |  |  |  | ID_CA_POSE_MIXING_ABS; ID_CA_POSE_MIXING_REL; ID_CA_POSE_MIXING_ROT; ID_CA_POSE_MIXING_CORRECTIONAL; ID_CA_POSE_MIXING_CORRECTIONAL_AREA; ID_CA_POSE_MIXING_CORRECTIONAL_PSD
Post Deformers | ID_CA_POSE_MIXING_DEFORMED | BOOL |  |  |  | 
Use | ID_CA_POSE_USE_STRENGTH | BOOL |  |  |  | 
Strength | ID_CA_POSE_STRENGTH | REAL |  |  |  | 
Pos | ID_CA_POSE_ROTATION_POS | VECTOR |  |  |  | 
Axis | ID_CA_POSE_ROTATION_AXIS | VECTOR |  |  |  | 
From Edges | ID_CA_POSE_ROTATION_FROMEDGE | BUTTON |  |  |  | 
From Points | ID_CA_POSE_ROTATION_FROMPOINTS | BUTTON |  |  |  | 
Set Pose | ID_CA_POSE_UPDATE_PSD_POSE | BUTTON |  |  |  | 
Go To Pose | ID_CA_POSE_RESTORE_PSD_POSE | BUTTON |  |  |  | 
Set Drivers | ID_CA_POSE_FORCE_AUTOWEIGHTDRIVER | BUTTON |  |  |  | 
Select Drivers | ID_CA_POSE_SHOW_AUTOWEIGHTDRIVER | BUTTON |  |  |  | 
Interpolation Mode | ID_CA_POSE_PSD_INTERP_MODE_UI_ONLY | LONG |  |  |  | ID_CA_POSE_PSD_INTERP_MODE_JOINT; ID_CA_POSE_PSD_INTERP_MODE_AXIS; ID_CA_POSE_PSD_INTERP_MODE_GLOBALAVERAGE
PSD Weight Tag | ID_CA_POSE_WEIGHTTAG_UI_ONLY | LINK |  |  |  | 
Target | ID_CA_POSE_TARGET | LINK |  |  |  | 
External | ID_CA_POSE_EXTERNAL | FILENAME |  |  |  | 
Save... | ID_CA_POSE_EXTERNAL_SAVE | BUTTON |  |  |  | 
Strength | ID_CA_POSE_TOTAL_STRENGTH | REAL |  |  |  | 
Record Sliders | ID_CA_POSE_RECORD_SLIDER | BUTTON |  |  |  | 
Reset Sliders | ID_CA_POSE_RESET_SLIDER | BUTTON |  |  |  | 
Destination | ID_CA_POSE_DEST | LINK |  |  |  | 
Mode | ID_CA_POSE_TARGET_INCLUDE_MODE | LONG |  |  |  | ID_CA_POSE_TARGET_INCLUDE_MODE_INCLUDE; ID_CA_POSE_TARGET_INCLUDE_MODE_EXCLUDE
Objects | ID_CA_POSE_TARGET_INCLUDE | IN_EXCLUDE |  |  |  | 
Auto Weighting | ID_CA_POSE_PSD_AUTOWEIGHT_INTERP_UI_ONLY | BOOL |  |  |  | 
Auto Orient Blend | ID_CA_POSE_PSD_ORIENT_INTERP_UI_ONLY | BOOL |  |  |  | 
Auto Twist Blend | ID_CA_POSE_PSD_TWIST_INTERP_UI_ONLY | BOOL |  |  |  | 
Auto Pos Blend | ID_CA_POSE_PSD_POS_INTERP_UI_ONLY | BOOL |  |  |  | 
Orient Average Output | ID_CA_POSE_PSD_ORIENT_INTERP_AVERAGEWEIGHT_UI_ONLY | REAL |  |  |  | 
Pos Average Output | ID_CA_POSE_PSD_POS_INTERP_AVERAGEWEIGHT_UI_ONLY | REAL |  |  |  | 
Twist Average Output | ID_CA_POSE_PSD_TWIST_INTERP_AVERAGEWEIGHT_UI_ONLY | REAL |  |  |  | 
Total Average Output | ID_CA_POSE_PSD_INTERP_AVERAGEWEIGHT_UI_ONLY | REAL |  |  |  | 
No label | ID_CA_POSE_PSD_INTERP_MODE | BOOL |  |  |  | 
X Axis Weight | ID_CA_POSE_PSD_JOINT_X_WEIGHT | REAL |  |  |  | 
Y Axis Weight | ID_CA_POSE_PSD_JOINT_Y_WEIGHT | REAL |  |  |  | 
Z Axis Weight | ID_CA_POSE_PSD_JOINT_Z_WEIGHT | REAL |  |  |  | 
Consider In AutoWeighting | ID_CA_POSE_PSD_JOINT_FORCE_IN_AUTOWEIGHT | BOOL |  |  |  | 
