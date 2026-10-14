# Description: Close Polygon Hole

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/c4d_objects/description/toolclosehole.res`
- **Symbol:** `ToolClosehole`
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
Polygon Type | MDATA_CLOSEHOLE_POLYTYPE | LONG |  |  |  | MDATA_CLOSEHOLE_POLYTYPE_BASIC; MDATA_CLOSEHOLE_POLYTYPE_GRID; MDATA_CLOSEHOLE_POLYTYPE_PATCH
Patch Rotation | MDATA_CLOSEHOLE_ROTATION_OFFSET | LONG |  |  |  | 
Patch Width | MDATA_CLOSEHOLE_WIDTH_OFFSET | LONG |  |  |  | 
Basic Polygon Type | MDATA_CLOSEHOLE_BASIC_POLYTYPE | LONG |  |  |  | MDATA_CLOSEHOLE_POLYTYPE_NGON; MDATA_CLOSEHOLE_POLYTYPE_TRIANGLE; MDATA_CLOSEHOLE_POLYTYPE_QUADS
Create Tri-/Quadrangle | MDATA_CLOSEHOLE_TRI | BOOL |  |  |  | 
Select New Polygons | MDATA_CLOSEHOLE_SELECTNEWPOLY | BOOL |  |  |  | 
Select Outline | MDATA_CLOSEHOLE_SELECTOUTLINE | BOOL |  |  |  | 
Phong Break Outline | MDATA_CLOSEHOLE_BREAKOUTLINE | BOOL |  |  |  | 
Close All Holes | MDATA_CLOSEHOLE_CLOSEALLBTN | BUTTON |  |  |  | 
