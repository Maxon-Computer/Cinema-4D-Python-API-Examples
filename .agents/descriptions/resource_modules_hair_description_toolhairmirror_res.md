# Description: Mirror

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/hair/description/toolhairmirror.res`
- **Symbol:** `ToolHairMirror`
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
Mode | HAIR_MIRROR_MODE | LONG |  |  |  | HAIR_MIRROR_MODE_CLONE; HAIR_MIRROR_MODE_INTERPOLATED
Auto Root | HAIR_MIRROR_ROOT | BOOL |  |  |  | 
Strength | HAIR_MIRROR_STRENGTH | REAL | 0.0 | 100.0 |  | 
Search | HAIR_MIRROR_SEARCH | REAL | 0.0 |  |  | 
Guides | HAIR_MIRROR_NEIGHBORS | LONG |  |  |  | 
Coords | HAIR_MIRROR_COORDS | LONG |  |  |  | HAIR_MIRROR_COORDS_WORLD; HAIR_MIRROR_COORDS_LOCAL; HAIR_MIRROR_COORDS_OBJECT
Mirror | HAIR_MIRROR_PLANE | LONG |  |  |  | HAIR_MIRROR_PLANE_XY; HAIR_MIRROR_PLANE_XZ; HAIR_MIRROR_PLANE_YZ
Object | HAIR_MIRROR_LINK | LINK |  |  |  | 
