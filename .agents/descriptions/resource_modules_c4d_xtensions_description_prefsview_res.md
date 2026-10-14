# Description: Viewport Display

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/c4d_xtensions/description/prefsview.res`
- **Symbol:** `Prefsview`
- **Category:** Other

Use parameter symbols to access parameters and cycle option symbols for cycle values, never their numeric IDs. Treat Min and Max as constraints and Default as the declared initial value; blank cells mean the resource does not declare that metadata, not that the value is zero. Base Description Parameters lists inherited fields from each base; All Parameters lists the effective parameter set for this description.

## Base Description Parameters

No base descriptions.

## All Parameters

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Playback | PREFS_VIEW_PERFORMANCE_GROUP | SEPARATOR |  |  |  | 
Playback in All Views | PREF_VIEW_FULLANIMREDRAW | BOOL |  |  |  | 
Refresh Attributes on Playback | PREF_VIEW_REALTIME | BOOL |  |  |  | 
Viewport Elements | PREFS_VIEW_VP_ELEMENTS_GROUP | SEPARATOR |  |  |  | 
Mini-Axis Position | PREF_VIEW_EDITOR_AXIS_POS | LONG |  |  |  | PREF_VIEW_AXIS_POS_OFF; PREF_VIEW_AXIS_POS_BL; PREF_VIEW_AXIS_POS_TL; PREF_VIEW_AXIS_POS_TR; PREF_VIEW_AXIS_POS_BR
Type | PREF_VIEW_EDITOR_AXIS_TYPE | LONG |  |  |  | PREF_VIEW_AXIS_TYPE_WORLD; PREF_VIEW_AXIS_TYPE_OBJECT
Scale | PREF_VIEW_EDIT_AXIS_SCALE | REAL | 0.0 | 400.0 |  | 
Text | PREF_VIEW_EDIT_AXIS_TEXT | BOOL |  |  |  | 
Background Gradient | PREF_VIEW_DISPLAYFILTER_GRADIENT | BOOL |  |  |  | 
Draw Workplane Behind | PREF_VIEW_DRAW_WORKPLANE_BEHIND | BOOL |  |  |  | 
Handles | PREFS_VIEW_HANDLES_GROUP | SEPARATOR |  |  |  | 
Axis Scale | PREF_VIEW_OBJECTAXIS_SCALE | REAL | 0.0 | 400.0 |  | 
Plane Handles | PREF_VIEW_DISPLAYFILTER_HANDLEBANDS | BOOL |  |  |  | 
Spherical Rotation Gizmo | PREF_VIEW_ROTATION_BANDS | BOOL |  |  |  | 
Band Thickness | PREF_VIEW_ROTBAND_SCALE | REAL | 0.0 | 400.0 |  | 
Screen Rotation Circle Scale | PREF_VIEW_ROTATION_CIRCLE | REAL | 0.0 | 300.0 |  | 
Point Size (px) | PREF_VIEW_POINT_HANDLE_SIZE | LONG | 0 | 10 |  | 
Selected Point Size (px) | PREF_VIEW_POINT_SELECTED_SIZE | LONG | 0 | 10 |  | 
Edge Thickness (px) | PREF_VIEW_EDGE_UNSELECTED_SIZE | LONG | 0 | 10 |  | 
Selected Edge Thickness (px) | PREF_VIEW_EDGE_SELECTED_SIZE | LONG | 0 | 10 |  | 
UV Seams Thickness (px) | PREF_VIEW_UV_SEAMS_SIZE | LONG | 0 | 10 |  | 
Points in Edge Mode | PREF_VIEW_EDGE_POINTS | BOOL |  |  |  | 
Normals Scale | PREF_VIEW_NORMALS_SCALE | REAL | 0.0 | 400.0 |  | 
Spline Thickness (px) | PREF_VIEW_SPLINE_WIDTH | LONG | 1 | 10 |  | 
Occluded Selection Visibility | PREF_VIEW_OCCLUDED_SELECTION_VISIBILITY | REAL | 0.0 | 100.0 |  | 
Tag Highlight Visibility | PREF_VIEW_TAG_HIGHLIGHT_VISIBILITY | REAL | 0.0 | 100.0 |  | 
Object Selection | PREFS_VIEW_OBJ_SELECTION_GROUP | SEPARATOR |  |  |  | 
Outlines | PREF_VIEW_OUTLINES | BOOL |  |  |  | 
Outline Thickness (px) | PREF_VIEW_OUTLINE_WIDTH | REAL | 1.0 | 10.0 |  | 
Wireframe | PREF_VIEW_SEL_WIREFRAMESELECTION | BOOL |  |  |  | 
Include Children | PREF_VIEW_SEL_WIREFRAMESELECTION_CHILDREN | BOOL |  |  |  | 
Bounding Box | PREF_VIEW_SEL_BOUNDINGBOXSELECTION | BOOL |  |  |  | 
Include Children | PREF_VIEW_SEL_BOUNDINGBOXSELECTION_CHILDREN | BOOL |  |  |  | 
System | PREFS_VIEW_SYSTEM_GROUP | SEPARATOR |  |  |  | 
Monitor Aspect | PREF_VIEW_MONITORASPECT | REAL | 0.0 |  |  | 
Linear Workflow | PREF_VIEW_LINEAR_WORKFLOW | BOOL |  |  |  | 
Display Color Profile | PREF_VIEW_COLORPROFILE | COLORPROFILE |  |  |  | 
No label | PREF_VIEW_WARNING | STATICTEXT |  |  |  | 
