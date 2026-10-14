# Description: Brush

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/c4d_objects/description/toolbrush.res`
- **Symbol:** `ToolBrush`
- **Category:** Other

Use parameter symbols to access parameters and cycle option symbols for cycle values, never their numeric IDs. Treat Min and Max as constraints and Default as the declared initial value; blank cells mean the resource does not declare that metadata, not that the value is zero. Base Description Parameters lists inherited fields from each base; All Parameters lists the effective parameter set for this description.

## Base Description Parameters

### Base Tool (`ToolBase`)

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Realtime Update | MDATA_INTERACTIVE | BOOL |  |  |  | 
    Apply     | MDATA_APPLY | BUTTON |  |  |  | 
New Transform | MDATA_NEWTRANSFORM | BUTTON |  |  |  | 
No label | ID_SNAPSETTINGS | SUBCONTAINER |  |  |  | 

## All Parameters

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Realtime Update | MDATA_INTERACTIVE | BOOL |  |  |  | 
    Apply     | MDATA_APPLY | BUTTON |  |  |  | 
New Transform | MDATA_NEWTRANSFORM | BUTTON |  |  |  | 
No label | ID_SNAPSETTINGS | SUBCONTAINER |  |  |  | 
Size | MDATA_BRUSH_FALLOFF_RADIUS | REAL | 0.0 |  |  | 
Size | MDATA_BRUSH_FALLOFF_RADIUS_3D | REAL | 0.0 |  |  | 
Size (UV) | MDATA_BRUSH_FALLOFF_RADIUS_UV | REAL | 0.0 |  |  | 
Strength | MDATA_BRUSH_FALLOFF_STRENGTH | REAL |  |  |  | 
Mode | MDATA_BRUSH_MODE | LONG |  |  |  | MDATA_BRUSH_MODE_SMEAR; MDATA_BRUSH_MODE_PULL; MDATA_BRUSH_MODE_SURFACE; MDATA_BRUSH_MODE_NORMAL; MDATA_BRUSH_MODE_SPREAD; MDATA_BRUSH_MODE_SPIN; MDATA_BRUSH_MODE_TWIST; MDATA_BRUSH_MODE_VORTEX; MDATA_BRUSH_MODE_SMOOTH; MDATA_BRUSH_MODE_RELAX; MDATA_BRUSH_MODE_SURFACE_SMEAR
Update Normals | MDATA_BRUSH_UPDATENORMALS | BOOL |  |  |  | 
Visible Only | MDATA_BRUSH_VISIBLEONLY | BOOL |  |  |  | 
Preserve Boundary | MDATA_BRUSH_PRESERVE_BOUNDARY | BOOL |  |  |  | 
Surface | MDATA_BRUSH_CONNECTED | BOOL |  |  |  | 
Preview | MDATA_BRUSH_PREVIEW | BOOL |  |  |  | 
Space | MDATA_BRUSH_RESTRICTION_SPACE | LONG |  |  |  | MDATA_BRUSH_RESTRICTION_SPACE_WORLD; MDATA_BRUSH_RESTRICTION_SPACE_OBJECT
X | MDATA_BRUSH_RESTRICTION_X | REAL |  |  |  | 
Y | MDATA_BRUSH_RESTRICTION_Y | REAL |  |  |  | 
Z | MDATA_BRUSH_RESTRICTION_Z | REAL |  |  |  | 
Falloff | MDATA_BRUSH_FALLOFF_MODE | LONG |  |  |  | MDATA_BRUSH_MODE_CONSTANT; MDATA_BRUSH_MODE_LINEAR; MDATA_BRUSH_MODE_DOME; MDATA_BRUSH_MODE_BELL; MDATA_BRUSH_MODE_CIRCLE; MDATA_BRUSH_MODE_NEEDLE; MDATA_BRUSH_MODE_USER
Width | MDATA_BRUSH_FALLOFF_WIDTH | REAL | 0.0 |  |  | 
Spline | MDATA_BRUSH_FALLOFF | SPLINE |  |  |  | 
