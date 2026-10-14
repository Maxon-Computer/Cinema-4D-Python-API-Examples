# Description: Magnet

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/c4d_objects/description/toolmagnet.res`
- **Symbol:** `ToolMagnet`
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
Radius | MDATA_MAGNET_FALLOFF_RADIUS | REAL | 0.0 |  |  | 
Radius | MDATA_MAGNET_FALLOFF_RADIUS_3D | REAL | 0.0 |  |  | 
Radius (UV) | MDATA_MAGNET_FALLOFF_RADIUS_UV | REAL | 0.0 |  |  | 
Strength | MDATA_MAGNET_FALLOFF_STRENGTH | REAL |  |  |  | 
Mode | MDATA_MAGNET_EFFECTMODE | LONG |  |  |  | MDATA_MAGNET_MODE_SMEAR; MDATA_MAGNET_MODE_PULL; MDATA_MAGNET_MODE_SURFACE; MDATA_MAGNET_MODE_NORMAL; MDATA_MAGNET_MODE_SPREAD; MDATA_MAGNET_MODE_SPIN; MDATA_MAGNET_MODE_TWIST; MDATA_MAGNET_MODE_VORTEX; MDATA_MAGNET_MODE_SMOOTH; MDATA_MAGNET_MODE_RELAX; MDATA_MAGNET_MODE_SURFACE_SMEAR
Visible Only | MDATA_MAGNET_MOVEONLYVISIBLE | BOOL |  |  |  | 
Surface | MDATA_MAGNET_CONNECTED | BOOL |  |  |  | 
Preview | MDATA_MAGNET_PREVIEW | BOOL |  |  |  | 
Nearest Point | MDATA_MAGNET_NEAREST | BOOL |  |  |  | 
Snap Visible | MDATA_MAGNET_VISIBLEONLY | BOOL |  |  |  | 
Preserve Boundary | MDATA_MAGNET_PRESERVE_BOUNDARY | BOOL |  |  |  | 
Space | MDATA_MAGNET_RESTRICT | LONG |  |  |  | MDATA_MAGNET_RESTRICT_WORLD; MDATA_MAGNET_RESTRICT_OBJECT; MDATA_MAGNET_RESTRICT_CAMERA
X | MDATA_MAGNET_RESTRICT_X | REAL |  |  |  | 
Y | MDATA_MAGNET_RESTRICT_Y | REAL |  |  |  | 
Z | MDATA_MAGNET_RESTRICT_Z | REAL |  |  |  | 
Falloff | MDATA_MAGNET_MODE | LONG |  |  |  | MDATA_MAGNET_MODE_CONSTANT; MDATA_MAGNET_MODE_LINEAR; MDATA_MAGNET_MODE_DOME; MDATA_MAGNET_MODE_BELL; MDATA_MAGNET_MODE_CIRCLE; MDATA_MAGNET_MODE_NEEDLE; MDATA_MAGNET_MODE_USER
Width | MDATA_MAGNET_FALLOFF_WIDTH | REAL | 0.0 |  |  | 
Spline | MDATA_MAGNET_FALLOFF | SPLINE |  |  |  | 
