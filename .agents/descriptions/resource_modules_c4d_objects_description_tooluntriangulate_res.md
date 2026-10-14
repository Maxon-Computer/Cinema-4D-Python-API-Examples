# Description: Untriangulate

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/c4d_objects/description/tooluntriangulate.res`
- **Symbol:** `ToolUntriangulate`
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
Create N-gon | MDATA_UNTRIANGULATE_NGONS_DESC | BOOL |  |  |  | 
Flatness Angle | MDATA_UNTRIANGULATE_ANGLE_DESC | BOOL |  |  |  | 
Angle | MDATA_UNTRIANGULATE_ANGLE_RAD_DESC | REAL | 0.0 | 180.0 |  | 
Internal Angle | MDATA_UNTRIANGULATE_USE_ANGLE_DERIVATION | BOOL |  |  |  | 
Angle | MDATA_UNTRIANGULATE_ANGLE_DERIVATION | REAL | 0.0 | 90.0 |  | 
Alignment Angle | MDATA_UNTRIANGULATE_USE_ALIGNMENT_DERIVATION | BOOL |  |  |  | 
Angle | MDATA_UNTRIANGULATE_ALIGNMENT_DERIVATION | REAL | 0.0 | 90.0 |  | 
Keep UV Boundary | MDATA_UNTRIANGULATE_RESPECTUVBOUNDARY | BOOL |  |  |  | 
Keep Phong Edge Breaks | MDATA_UNTRIANGULATE_RESPECTSHADINGBREAKS | BOOL |  |  |  | 
Keep Mesh Attributes | MDATA_UNTRIANGULATE_RESPECTPOLYATTRIBUTES | BOOL |  |  |  | 
