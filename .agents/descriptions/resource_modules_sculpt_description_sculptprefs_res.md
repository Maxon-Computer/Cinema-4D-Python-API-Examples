# Description: Sculpting

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/sculpt/description/sculptprefs.res`
- **Symbol:** `Sculptprefs`
- **Category:** Other

Use parameter symbols to access parameters and cycle option symbols for cycle values, never their numeric IDs. Treat Min and Max as constraints and Default as the declared initial value; blank cells mean the resource does not declare that metadata, not that the value is zero. Base Description Parameters lists inherited fields from each base; All Parameters lists the effective parameter set for this description.

## Base Description Parameters

No base descriptions.

## All Parameters

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Modeling | PREF_SCULPTPREF_MODELING_GROUP | SEPARATOR |  |  |  | 
Disconnected Points on Delete | PREF_MODELING_DISCONNECTED_POINTS_ON_DELETE | LONG |  |  |  | PREF_MODELING_DISCONNECTED_POINTS_ON_DELETE_REMOVE; PREF_MODELING_DISCONNECTED_POINTS_ON_DELETE_KEEP
Sculpting | PREF_SCULPTPREF_SCULPTING_GROUP | SEPARATOR |  |  |  | 
Always Update (Slow) | PREF_SCULPTPREF_ALWAYS_UPDATE | BOOL |  |  |  | 
Respect Selections | PREF_SCULPTPREF_RESPECT_SELECTIONS | BOOL |  |  |  | 
Polygon Object Normals Threshold | PREF_SCULPTPREF_DISPLAY_POLYGONOBJECT_NORMALS_THRESHOLD | LONG |  |  |  | 
Stamp | PREF_SCULPTPREF_BRUSH_STAMP_GROUP | SEPARATOR |  |  |  | 
Default Gray Value | PREF_SCULPTPREF_BRUSH_STAMP_GREYVALUE_DEFAULT | REAL | 0.0 | 1.0 |  | 
Use Top Left Pixel For Gray Value | PREF_SCULPTPREF_BRUSH_STAMP_GREYVALUE_TOPLEFTPIXEL | BOOL |  |  |  | 
Material Resolution | PREF_SCULPTPREF_BRUSH_STAMP_MATERIAL_SAMPLERES | LONG |  |  |  | 
Stencil | PREF_SCULPTPREF_BRUSH_STENCIL_GROUP | SEPARATOR |  |  |  | 
Default Gray Value | PREF_SCULPTPREF_BRUSH_STENCIL_GREYVALUE_DEFAULT | REAL | 0.0 | 1.0 |  | 
Use Top Left Pixel For Gray Value | PREF_SCULPTPREF_BRUSH_STENCIL_GREYVALUE_TOPLEFTPIXEL | BOOL |  |  |  | 
Material Resolution | PREF_SCULPTPREF_BRUSH_STENCIL_MATERIAL_SAMPLERES | LONG |  |  |  | 
