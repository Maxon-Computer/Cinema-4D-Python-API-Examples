# Description: Make Selection

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/c4d_objects/description/toolmakeselect.res`
- **Symbol:** `ToolMakeSelect`
- **Category:** Other

Use parameter symbols to access parameters and cycle option symbols for cycle values, never their numeric IDs. Treat Min and Max as constraints and Default as the declared initial value; blank cells mean the resource does not declare that metadata, not that the value is zero. Base Description Parameters lists inherited fields from each base; All Parameters lists the effective parameter set for this description.

## Base Description Parameters

No base descriptions.

## All Parameters

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
N-gons | MDATA_MAKESELECT_NGONS | BOOL |  |  |  | 
Quads | MDATA_MAKESELECT_QUADS | BOOL |  |  |  | 
Tris | MDATA_MAKESELECT_TRIS | BOOL |  |  |  | 
State | MDATA_MAKESELECT_STATE | LONG |  |  |  | MDATA_MAKESELECT_STATE_ANY; MDATA_MAKESELECT_STATE_PLANAR; MDATA_MAKESELECT_STATE_NONDEGENERATE; MDATA_MAKESELECT_STATE_NONPLANAR; MDATA_MAKESELECT_STATE_DEGENERATE
Select | MDATA_MAKESELECT_SELECT | BUTTON |  |  |  | 
