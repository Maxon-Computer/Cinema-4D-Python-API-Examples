# Description: Soft Selection

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/c4d_objects/description/toolsoftselection.res`
- **Symbol:** `ToolSoftSelection`
- **Category:** Other

Use parameter symbols to access parameters and cycle option symbols for cycle values, never their numeric IDs. Treat Min and Max as constraints and Default as the declared initial value; blank cells mean the resource does not declare that metadata, not that the value is zero. Base Description Parameters lists inherited fields from each base; All Parameters lists the effective parameter set for this description.

## Base Description Parameters

No base descriptions.

## All Parameters

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Enable | MDATA_SOFT_ENABLE | BOOL |  |  |  | 
Surface | MDATA_SOFT_SURFACE | BOOL |  |  |  | 
Rubber | MDATA_SOFT_RUBBER | BOOL |  |  |  | 
Restrict | MDATA_SOFT_RESTRICT | BOOL |  |  |  | 
Preview | MDATA_SOFT_PREVIEW | BOOL |  |  |  | 
Falloff | MDATA_SOFT_FALLOFF | LONG |  |  |  | MDATA_SOFT_FALLOFF_LINEAR; MDATA_SOFT_FALLOFF_DOME; MDATA_SOFT_FALLOFF_BELL; MDATA_SOFT_FALLOFF_CIRCLE; MDATA_SOFT_FALLOFF_NEEDLE; MDATA_SOFT_FALLOFF_VMAP; MDATA_SOFT_FALLOFF_SPLINE
Mode | MDATA_SOFT_MODE | LONG |  |  |  | MDATA_SOFT_MODE_GROUPS; MDATA_SOFT_MODE_CENTER; MDATA_SOFT_MODE_ALL
Radius | MDATA_SOFT_RADIUS | REAL | 0.0 |  |  | 
Radius (UV) | MDATA_SOFT_RADIUS_UV | REAL | 0.0 |  |  | 
Radius | MDATA_SOFT_RADIUS_3D | REAL | 0.0 |  |  | 
Strength | MDATA_SOFT_STRENGTH | REAL | 0.0 | 100.0 |  | 
Width | MDATA_SOFT_WIDTH | REAL | 0.0 | 100.0 |  | 
Spline | MDATA_SOFT_SPLINE | SPLINE |  |  |  | 
