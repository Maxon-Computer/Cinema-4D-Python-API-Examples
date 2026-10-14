# Description: Collider Tag

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/clothilde/description/collidertag.res`
- **Symbol:** `ColliderTag`
- **Category:** Tags

Use parameter symbols to access parameters and cycle option symbols for cycle values, never their numeric IDs. Treat Min and Max as constraints and Default as the declared initial value; blank cells mean the resource does not declare that metadata, not that the value is zero. Base Description Parameters lists inherited fields from each base; All Parameters lists the effective parameter set for this description.

## Base Description Parameters

### Base Tag (`Tbase`)

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Expose on Object | ID_EXPOSETAB | BOOL |  |  |  | 

### Basic Properties (`Obaselist`)

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Icon File / ID | ID_BASELIST_ICON_FILE | TEXTURE |  |  |  | 
Icon Color | ID_BASELIST_ICON_COLORIZE_MODE | BOOL |  |  |  | 
Color | ID_BASELIST_ICON_COLOR | COLOR |  |  | 1.0 0.9 0.4 | 
No label | ID_BASELIST_ICON_PRESET_BUTTONS | ICONCHOOSER |  |  |  | 
Name | ID_BASELIST_NAME | STRING |  |  |  | 
Layer | ID_LAYER_LINK | LINK |  |  |  | 
No label | ID_BASELIST_NODESPACE_ADD_REMOVE_BUTTONS | NODESPACE_ADD_REMOVE |  |  |  | 

## All Parameters

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Icon File / ID | ID_BASELIST_ICON_FILE | TEXTURE |  |  |  | 
Icon Color | ID_BASELIST_ICON_COLORIZE_MODE | BOOL |  |  |  | 
Color | ID_BASELIST_ICON_COLOR | COLOR |  |  | 1.0 0.9 0.4 | 
No label | ID_BASELIST_ICON_PRESET_BUTTONS | ICONCHOOSER |  |  |  | 
Name | ID_BASELIST_NAME | STRING |  |  |  | 
Layer | ID_LAYER_LINK | LINK |  |  |  | 
No label | ID_BASELIST_NODESPACE_ADD_REMOVE_BUTTONS | NODESPACE_ADD_REMOVE |  |  |  | 
Expose on Object | ID_EXPOSETAB | BOOL |  |  |  | 
Use Collider | COLLIDER_USE | BOOL |  |  |  | 
Collision Shape | CONVEX_COLLIDER | LONG |  |  |  | CONVEX_COLLIDER_TRIANGLE_MESH; CONVEX_COLLIDER_CONVEX_HULLS; CONVEX_COLLIDER_SPHERE; CONVEX_COLLIDER_BOX
Geometry Accuracy | CONVEX_COLLIDER_CONVEXDECOMPOSITION_ACCURACY | REAL | 0 |  |  | 
Friction | COLLIDER_FRICTION | REAL | 0.0 |  |  | 
Bounciness | COLLIDER_BOUNCE | REAL | 0.0 | 10.0 |  | 
Stickiness | COLLIDER_STICKINESS | REAL | 0.0 |  |  | 
Collision Side | CLOTH_PBD_COLLIDER_SIDE | LONG |  |  |  | CLOTH_PBD_COLLIDER_SIDE_NORMALS; CLOTH_PBD_COLLIDER_SIDE_INVNORMALS; CLOTH_PBD_COLLIDER_SIDE_BOTH
Mode | COLLIDER_LIQUID_COLLISION_MODE | LONG |  |  |  | COLLIDER_LIQUID_COLLISION_MODE_SURFACE; COLLIDER_LIQUID_COLLISION_MODE_VOLUME; COLLIDER_LIQUID_COLLISION_MODE_OFF
Collision Side | COLLIDER_LIQUID_COLLISION_FROM | LONG |  |  |  | COLLIDER_LIQUID_COLLISION_FROM_OUTSIDE; COLLIDER_LIQUID_COLLISION_FROM_INSIDE; COLLIDER_LIQUID_COLLISION_FROM_BOTH
Voxelization | COLLIDER_SDF_VOXEL_SIZE_MODE | LONG |  |  |  | COLLIDER_SDF_VOXEL_SIZE_MODE_RELATIVE; COLLIDER_SDF_VOXEL_SIZE_MODE_ABSOLUTE
Voxel Size | COLLIDER_SDF_VOXEL_SIZE_ABSOLUTE | REAL | 0.0 |  |  | 
Interior Voxel Range | COLLIDER_SDF_VOXEL_BAND_INTERIOR_ABSOLUTE | LONG | 0 |  |  | 
Exterior Voxel Range | COLLIDER_SDF_VOXEL_BAND_EXTERIOR_ABSOLUTE | LONG | 0 |  |  | 
Voxel Size | COLLIDER_SDF_VOXEL_SIZE_RELATIVE | REAL | 0.0 |  |  | 
Interior Voxel Range | COLLIDER_SDF_VOXEL_BAND_INTERIOR_RELATIVE | LONG | 0 |  |  | 
Exterior Voxel Range | COLLIDER_SDF_VOXEL_BAND_EXTERIOR_RELATIVE | LONG | 0 |  |  | 
On Open Geometry | COLLIDER_PREPROCESS_IF_OPEN | LONG |  |  |  | COLLIDER_PREPROCESS_IF_OPEN_OFF; COLLIDER_PREPROCESS_IF_OPEN_THICKEN; COLLIDER_PREPROCESS_IF_OPEN_CLOSE
Thickness | COLLIDER_THICKNESS | REAL | 0.0 |  |  | 
Position | COLLIDER_THICKNESS_POSITION | REAL | -100.0 | 100.0 |  | 
Restrict To Liquid Collisions | COLLIDER_PREPROCESS_RESTRICT_TO_LIQUIDS | BOOL |  |  |  | 
Set | COLLIDER_SET_EXCL | BUTTON |  |  |  | 
Clear | COLLIDER_CLEAR_EXCL | BUTTON |  |  |  | 
Show | COLLIDER_SHOW_EXCL | BUTTON |  |  |  | 
Draw | COLLIDER_DRAW_EXCL | BOOL |  |  |  | 
Open and thin meshes in Signed Distance Field might not behave as expected. | COLLIDER_INFO_STRING0 | STATICTEXT |  |  |  | 
Consider adding thickness in the range of Voxel Size or larger. | COLLIDER_INFO_STRING1 | STATICTEXT |  |  |  | 
