# Description: Scatter Placement

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/tool_system_hybrid/description/toolscatterplacement.res`
- **Symbol:** `ToolScatterPlacement`
- **Category:** Other

Use parameter symbols to access parameters and cycle option symbols for cycle values, never their numeric IDs. Treat Min and Max as constraints and Default as the declared initial value; blank cells mean the resource does not declare that metadata, not that the value is zero. Base Description Parameters lists inherited fields from each base; All Parameters lists the effective parameter set for this description.

## Base Description Parameters

No base descriptions.

## All Parameters

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Mode | TOOL_MODE_INTERACTION | LONG |  |  |  | TOOL_MODE_SCATTER; TOOL_MODE_ERASE
Radius | TOOL_PLACEMENT_OUTER_RADIUS | REAL | 0.0 |  |  | 
Object Spacing | TOOL_EXCLUSION_RADIUS | REAL |  |  |  | 
Use Splats | TOOL_USE_SPLATS | BOOL |  |  |  | 
Splat Spacing | TOOL_INTER_SPLAT_SEP_DISTANCE | REAL |  |  |  | 
Count | TOOL_PLACEMENT_ATTEMPTS_PER_SPLAT | LONG | 0 |  |  | 
Density | TOOL_PLACEMENT_DENSITY | REAL | 0.0 |  |  | 
Source | TOOL_MODE_OBJECT_SOURCE | LONG |  |  |  | TOOL_MODE_SOURCE_SELECTION; TOOL_MODE_SOURCE_PALETTE
Object Palette | TOOL_OBJECT_PALETTE | ITEMTREE |  |  |  | 
Random Order | TOOL_RANDOMIZE_ORDER | BOOL |  |  |  | 
Seed | TOOL_RANDOM_SEED | LONG | 1 |  |  | 
Align To | TOOL_MODE_ALIGN_TO | LONG |  |  |  | TOOL_MODE_ALIGN_STROKE; TOOL_MODE_ALIGN_OBJECT
Reference Point | TOOL_ALIGN_REFERENCE | LONG |  |  |  | TOOL_REF_AXIS; TOOL_REF_BOUNDINGBOX
Position Min/Max | TOOL_MIN_MAX_Y_OFFSET | VECTOR | 0.0 |  |  | 
Rotation Range | TOOL_ROTATION_RANGE | VECTOR | 0.0 |  |  | 
Scale Min/Max | TOOL_MIN_MAX_SCALE | VECTOR | 0.0 |  |  | 
Show mouse region preview | TOOL_SHOW_PREVIEW_REGION | BOOL |  |  |  | 
Show Placements | TOOL_SHOW_PLACEMENTS | BOOL |  |  |  | 
Show Splat Regions | TOOL_SHOW_SPLAT_REGIONS | BOOL |  |  |  | 
End Stroke | TOOL_BUTTON_END_SESSION | BUTTON |  |  |  | 
