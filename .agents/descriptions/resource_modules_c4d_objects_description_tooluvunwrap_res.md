# Description: UV Unwrap and Relax

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/c4d_objects/description/tooluvunwrap.res`
- **Symbol:** `ToolUvUnwrap`
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
Relax UV mode | TOOL_UVUNWRAP_RELAX_MODE | LONG |  |  |  | TOOL_UVUNWRAP_RELAX_MODE_LSCM; TOOL_UVUNWRAP_RELAX_MODE_ABF
Pin Boundaries | TOOL_UVUNWRAP_KEEP_BORDER | BOOL |  |  |  | 
Pin to Neighbors | TOOL_UVUNWRAP_KEEP_NEIGHBORS | BOOL |  |  |  | 
Pack Islands | TOOL_UVUNWRAP_PACK | BOOL |  |  |  | 
Packing Mode | TOOL_UVUNWRAP_PACK_MODE | LONG |  |  |  | TOOL_UVUNWRAP_PACK_MODE_BOUNDINGBOX; TOOL_UVUNWRAP_PACK_MODE_GEOMETRIC
Gap Size | TOOL_UVUNWRAP_PACK_GAPSIZE | LONG | 0 |  |  | 
Reset &amp; Unwrap | TOOL_UVUNWRAP_RESETUV_BUTTON | BUTTON |  |  |  | 
