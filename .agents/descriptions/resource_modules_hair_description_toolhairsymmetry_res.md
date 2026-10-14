# Description: Symmetry

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/hair/description/toolhairsymmetry.res`
- **Symbol:** `ToolHairSymmetry`
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
Symmetry | HAIR_SYMMETRY | BOOL |  |  |  | 
Search | HAIR_SYMMETRY_SEARCH | REAL | 0.0 |  |  | 
Coords | HAIR_SYMMETRY_COORDS | LONG |  |  |  | HAIR_SYMMETRY_COORDS_WORLD; HAIR_SYMMETRY_COORDS_LOCAL; HAIR_SYMMETRY_COORDS_OBJECT
Mirror | HAIR_SYMMETRY_PLANE | LONG |  |  |  | HAIR_SYMMETRY_PLANE_XY; HAIR_SYMMETRY_PLANE_XZ; HAIR_SYMMETRY_PLANE_YZ
Object | HAIR_SYMMETRY_LINK | LINK |  |  |  | 
