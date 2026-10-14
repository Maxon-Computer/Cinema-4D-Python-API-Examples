# Description: UV Packing

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/c4d_objects/description/tooluvpacking.res`
- **Symbol:** `ToolUvPacking`
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
Override Resolution | TOOL_UVPACKING_RESOLUTION_OVERRIDE | BOOL |  |  |  | 
Resolution Width | TOOL_UVPACKING_RESOLUTION_OVERRIDE_WIDTH | LONG | 32 |  |  | 
Resolution Height | TOOL_UVPACKING_RESOLUTION_OVERRIDE_HEIGHT | LONG | 32 |  |  | 
Gap Size | TOOL_UVPACKING_GAPSIZE | LONG | 0 |  |  | 
UV Space | TOOL_UVPACKING_UVSPACE | LONG |  |  |  | TOOL_UVPACKING_UVSPACE_MERGED; TOOL_UVPACKING_UVSPACE_GROUPED; TOOL_UVPACKING_UVSPACE_PEROBJECT
Start Tile U | TOOL_UVPACKING_STARTTILE_U | LONG | 0 |  |  | 
Start Tile V | TOOL_UVPACKING_STARTTILE_V | LONG | 0 |  |  | 
Skip Populated Tiles | TOOL_UVPACKING_SKIPPOPULATEDTILES | BOOL |  |  |  | 
Orientation | TOOL_UVPACKING_ORIENTATION | LONG |  |  |  | TOOL_UVPACKING_ORIENTATION_FREE; TOOL_UVPACKING_ORIENTATION_45; TOOL_UVPACKING_ORIENTATION_90; TOOL_UVPACKING_ORIENTATION_180; TOOL_UVPACKING_ORIENTATION_PRESERVE
Scaling | TOOL_UVPACKING_SCALING_MODE | LONG |  |  |  | TOOL_UVPACKING_SCALING_MODE_AUTOFIT; TOOL_UVPACKING_SCALING_MODE_PRESERVE; TOOL_UVPACKING_SCALING_MODE_TEXELDENSITY
Override Texel Density | TOOL_UVPACKING_TEXELDENSITY_OVERRIDE | BOOL |  |  |  | 
Texel Density | TOOL_UVPACKING_TEXELDENSITY_OVERRIDE_TD | REAL |  |  |  | 
UV Packing Mode | TOOL_UVPACKING_MODE | LONG |  |  |  | TOOL_UVPACKING_MODE_RASTERIZED; TOOL_UVPACKING_MODE_GEOMETRIC; TOOL_UVPACKING_MODE_BOUNDINGBOX
Stack Identical Islands | TOOL_UVPACKING_RASTERIZED_STACK_IDENTICAL_ISLANDS | BOOL |  |  |  | 
Stack Mirrored Islands | TOOL_UVPACKING_RASTERIZED_STACK_MIRRORED_ISLANDS | BOOL |  |  |  | 
Stretch to Fit | TOOL_UVPACKING_GEOMETRIC_STRETCH_TO_FIT | BOOL |  |  |  | 
Stack Identical Islands | TOOL_UVPACKING_GEOMETRIC_STACK_IDENTICAL_ISLANDS | BOOL |  |  |  | 
Stack Mirrored Islands | TOOL_UVPACKING_GEOMETRIC_STACK_MIRRORED_ISLANDS | BOOL |  |  |  | 
Stretch to Fit | TOOL_UVPACKING_BOUNDINGBOX_STRETCHTOFIT | BOOL |  |  |  | 
