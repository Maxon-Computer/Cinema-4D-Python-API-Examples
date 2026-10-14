# Description: Navigation

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/c4d_xtensions/description/prefsnavigation.res`
- **Symbol:** `Prefsnavigation`
- **Category:** Other

Use parameter symbols to access parameters and cycle option symbols for cycle values, never their numeric IDs. Treat Min and Max as constraints and Default as the declared initial value; blank cells mean the resource does not declare that metadata, not that the value is zero. Base Description Parameters lists inherited fields from each base; All Parameters lists the effective parameter set for this description.

## Base Description Parameters

No base descriptions.

## All Parameters

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Camera Mode | PREF_NAVIGATION_CAMERA | LONG |  |  |  | PREF_NAVIGATION_CAMERA_CUR; PREF_NAVIGATION_CAMERA_CTR; PREF_NAVIGATION_CAMERA_OBJ; PREF_NAVIGATION_CAMERA_CAM; PREF_NAVIGATION_CAMERA_CUSTOM
Point of Interest | PREF_NAVIGATION_POI | LONG |  |  |  | PREF_NAVIGATION_POI_CTR; PREF_NAVIGATION_POI_OBJ; PREF_NAVIGATION_POI_CAM
Cursor Placement | PREF_NAVIGATION_CURSOR | LONG |  |  |  | PREF_NAVIGATION_CURSOR_OFF; PREF_NAVIGATION_CURSOR_SELECTED; PREF_NAVIGATION_CURSOR_CHILDREN; PREF_NAVIGATION_CURSOR_ALL
Deep | PREF_NAVIGATION_DEEPCURSOR | BOOL |  |  |  | 
Lock PoI for Dolly | PREF_NAVIGATION_FIXEDDOLLY | BOOL |  |  |  | 
Dolly to Cursor | PREF_NAVIGATION_DOLLY | LONG |  |  |  | PREF_NAVIGATION_DOLLY_OFF; PREF_NAVIGATION_DOLLY_ORTHO; PREF_NAVIGATION_DOLLY_ALL
Navigation Cross | PREF_NAVIGATION_DISPLAYFILTER_POI | BOOL |  |  |  | 
Sync Orthographic Views | PREF_NAVIGATION_SYNCVIEWS | BOOL |  |  |  | 
Reverse Orbit | PREF_NAVIGATION_CAMERAREVERSE | BOOL |  |  |  | 
View Rotation CTRL/CMD Modifier | PREF_NAVIGATION_CTRLCMD_MODIFIER | LONG |  |  |  | PREF_NAVIGATION_CTRLCMD_TRACKBALL; PREF_NAVIGATION_CTRLCMD_ORTHOGONAL
Trackball Rotation | PREF_NAVIGATION_TRACKBALL | BOOL |  |  |  | 
Smooth View Transition | PREF_NAVIGATION_VIEW_TRANSITION | BOOL |  |  |  | 
Smooth Freelook Camera Rotation | PREF_NAVIGATION_FREELOOK_SMOOTHING | BOOL |  |  |  | 
Smooth Freelook Camera Movement | PREF_NAVIGATION_SMOOTHING | BOOL |  |  |  | 
Pan Speed | PREF_NAVIGATION_MOVE | REAL | 1.0 | 10000.0 |  | 
Dolly/Zoom Speed | PREF_NAVIGATION_SCALE | REAL | 1.0 | 10000.0 |  | 
Orbit Speed | PREF_NAVIGATION_ROTATE | REAL | 1.0 | 10000.0 |  | 
