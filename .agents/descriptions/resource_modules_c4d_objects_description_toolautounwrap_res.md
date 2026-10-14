# Description: Automatic UV

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/c4d_objects/description/toolautounwrap.res`
- **Symbol:** `ToolAutoUnwrap`
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
Override Resolution | TOOL_AUTOUNWRAP_RESOLUTION_OVERRIDE | BOOL |  |  |  | 
Resolution Width | TOOL_AUTOUNWRAP_RESOLUTION_OVERRIDE_WIDTH | LONG | 32 |  |  | 
Resolution Height | TOOL_AUTOUNWRAP_RESOLUTION_OVERRIDE_HEIGHT | LONG | 32 |  |  | 
Gap Size | TOOL_AUTOUNWRAP_GAPSIZE | LONG | 0 |  |  | 
Unwrap Mode | TOOL_AUTOUNWRAP_MODE | LONG |  |  |  | TOOL_AUTOUNWRAP_MODE_PACKED; TOOL_AUTOUNWRAP_MODE_CUBIC; TOOL_AUTOUNWRAP_MODE_ANGLE
Stretch | TOOL_AUTOUNWRAP_PACKED_STRETCH | REAL | 0.0 | 0.5 |  | 
Stack Identical Islands | TOOL_AUTOUNWRAP_PACKED_STACK_IDENTICAL_ISLANDS | BOOL |  |  |  | 
Stack Mirrored Islands | TOOL_AUTOUNWRAP_PACKED_STACK_MIRRORED_ISLANDS | BOOL |  |  |  | 
Preserve Orientation | TOOL_AUTOUNWRAP_CUBIC_PRESERVE_ORIENTATION | BOOL |  |  |  | 
Stretch to Fit | TOOL_AUTOUNWRAP_CUBIC_STRETCH_TO_FIT | BOOL |  |  |  | 
Relaxation Steps | TOOL_AUTOUNWRAP_CUBIC_RELAXATION_STEPS | LONG | 0 |  |  | 
Angle | TOOL_AUTOUNWRAP_ANGLE_ANGLE | REAL | 0.0 | 180.0 |  | 
Preserve Orientation | TOOL_AUTOUNWRAP_ANGLE_PRESERVE_ORIENTATION | BOOL |  |  |  | 
Stretch to Fit | TOOL_AUTOUNWRAP_ANGLE_STRETCH_TO_FIT | BOOL |  |  |  | 
Relaxation Steps | TOOL_AUTOUNWRAP_ANGLE_RELAXATION_STEPS | LONG | 0 |  |  | 
