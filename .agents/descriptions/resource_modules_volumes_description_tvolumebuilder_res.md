# Description: Volume Builder Tag

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/volumes/description/tvolumebuilder.res`
- **Symbol:** `Tvolumebuilder`
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
Perfect Primitive | ID_VOLUMEBUILDER_TAG_PERFECT_PRIMITIVE | BOOL |  |  |  | 
Use Mesh Points | ID_VOLUMEBUILDER_TAG_USEPOINTS | BOOL |  |  |  | 
Mesh Point Radius | ID_VOLUMEBUILDER_TAG_MESHRADIUS | REAL | 0.01 |  |  | 
Optimize and Close Holes | ID_VOLUMEBUILDER_TAG_OPTIMIZEANDCLOSE | BOOL |  |  |  | 
Use Particle Size | ID_VOLUMEBUILDER_TAG_USEPARTICLERADIUS | BOOL |  |  |  | 
Radius | ID_VOLUMEBUILDER_TAG_RADIUS | REAL | 0.01 |  |  | 
Density | ID_VOLUMEBUILDER_TAG_DENSITY | REAL | 0.01 |  |  | 
Scale Along | ID_VOLUMEBUILDER_TAG_SPLINERADIUS_SCALESPLINE | SPLINE |  |  |  | 
Scale per Segment | ID_VOLUMEBUILDER_TAG_SPLINERADIUS_PERSEGMENT | BOOL |  |  |  | 
Velocity Scale | ID_VOLUMEBUILDER_TAG_VELOCITY_SCALE | REAL | 0.0 |  |  | 
Convert From | ID_VOLUMEBUILDER_TAG_VECTOR_CONVERSION_MODE | LONG |  |  |  | ID_VOLUMEBUILDER_TAG_VECTOR_CONVERSION_MODE_SDF; ID_VOLUMEBUILDER_TAG_VECTOR_CONVERSION_MODE_UDF; ID_VOLUMEBUILDER_TAG_VECTOR_CONVERSION_MODE_FOG
Inside Voxel Falloff | ID_VOLUMEBUILDER_TAG_INTERIOR_VOXEL_FALLOFF | LONG | 1 |  |  | 
Maximum Voxel Falloff | ID_VOLUMEBUILDER_TAG_INFINITEFALLOFF | BOOL |  |  |  | 
Surface Threshold | ID_VOLUMEBUILDER_TAG_ISO | REAL |  |  |  | 
Creation Space | ID_VOLUMEBUILDER_TAG_SOURCETYPE | LONG |  |  |  | ID_VOLUMEBUILDER_TAG_SOURCETYPE_BOUNDINGBOX; ID_VOLUMEBUILDER_TAG_SOURCETYPE_PREVIOUS
P | ID_VOLUMEBUILDER_TAG_BBPOSITION | VECTOR |  |  |  | 
R | ID_VOLUMEBUILDER_TAG_BBROTATION | VECTOR |  |  |  | 
S | ID_VOLUMEBUILDER_TAG_BBSIZE | VECTOR | 0.0 |  |  | 
Override Box Matrix | ID_VOLUMEBUILDER_TAG_FIELD_CREATION_REF | LINK |  |  |  | 
Create Controller | ID_VOLUMEBUILDER_TAG_CREATE_CONTROLLER | BUTTON |  |  |  | 
Interior Voxel Range | ID_VOLUMEBUILDER_TAG_HALF_BAND_MESH_INTERIOR | LONG | 1 |  |  | 
Exterior Voxel Range | ID_VOLUMEBUILDER_TAG_HALF_BAND_MESH_EXTERIOR | LONG | 1 |  |  | 
Spline Voxel Range | ID_VOLUMEBUILDER_TAG_HALF_BAND_SPLINE | LONG | 1 |  |  | 
Particle Voxel Range | ID_VOLUMEBUILDER_TAG_HALF_BAND_PARTICLE | LONG | 1 |  |  | 
