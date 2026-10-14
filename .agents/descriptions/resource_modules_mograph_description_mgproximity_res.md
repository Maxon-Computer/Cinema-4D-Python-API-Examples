# Description: Proximity

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/mograph/description/mgproximity.res`
- **Symbol:** `MGproximity`
- **Category:** Other

Use parameter symbols to access parameters and cycle option symbols for cycle values, never their numeric IDs. Treat Min and Max as constraints and Default as the declared initial value; blank cells mean the resource does not declare that metadata, not that the value is zero. Base Description Parameters lists inherited fields from each base; All Parameters lists the effective parameter set for this description.

## Base Description Parameters

No base descriptions.

## All Parameters

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Use Deformed Object | MG_SURFACE_SCATTER_PROXIMITY_USE_DEFORMED_OBJECT | BOOL |  |  |  | 
Mode | MG_SURFACE_SCATTER_PROXIMITY_MODE | LONG |  |  |  | MG_SURFACE_SCATTER_PROXIMITY_MODE_MASK; MG_SURFACE_SCATTER_PROXIMITY_MODE_SCALE
Mask Projection | MG_SURFACE_SCATTER_PROXIMITY_MASK_PROJECTION | LONG |  |  |  | MG_SURFACE_SCATTER_PROXIMITY_MASK_PROJECTION_ALONG_X; MG_SURFACE_SCATTER_PROXIMITY_MASK_PROJECTION_ALONG_Y; MG_SURFACE_SCATTER_PROXIMITY_MASK_PROJECTION_ALONG_Z
Scale | MG_SURFACE_SCATTER_PROXIMITY_SCALE | REAL | 0.0 |  |  | 
Distance | MG_SURFACE_SCATTER_PROXIMITY_DISTANCE | REAL | 0.0 |  |  | 
Strength | MG_SURFACE_SCATTER_PROXIMITY_STRENGTH | REAL | 0.0 | 100.0 |  | 
Bias | MG_SURFACE_SCATTER_PROXIMITY_BIAS | REAL | -100.0 | 100.0 |  | 
Invert | MG_SURFACE_SCATTER_PROXIMITY_INVERT | BOOL |  |  |  | 
Restriction | MG_SURFACE_SCATTER_PROXIMITY_RESTRICTION | LONG |  |  |  | MG_SURFACE_SCATTER_PROXIMITY_RESTRICTION_INSIDE; MG_SURFACE_SCATTER_PROXIMITY_RESTRICTION_OUTSIDE; MG_SURFACE_SCATTER_PROXIMITY_RESTRICTION_BOTH
Clip to Shape | MG_SURFACE_SCATTER_PROXIMITY_CLIP_TO_SHAPE | BOOL |  |  |  | 
