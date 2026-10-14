# Description: PSet Data

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/thinking_particles/description/op_particledata.res`
- **Symbol:** `OP_ParticleData`
- **Category:** Graph View

Use parameter symbols to access parameters and cycle option symbols for cycle values, never their numeric IDs. Treat Min and Max as constraints and Default as the declared initial value; blank cells mean the resource does not declare that metadata, not that the value is zero. Base Description Parameters lists inherited fields from each base; All Parameters lists the effective parameter set for this description.

## Base Description Parameters

### Node (`GVbase`)

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Enabled | ID_GVBASE_ENABLE | BOOL |  |  |  | 
Title Color | ID_GVBASE_COLOR | COLOR |  |  |  | 
Remark | ID_GVBASE_REMARK | STRING |  |  |  | 

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
Enabled | ID_GVBASE_ENABLE | BOOL |  |  |  | 
Title Color | ID_GVBASE_COLOR | COLOR |  |  |  | 
Remark | ID_GVBASE_REMARK | STRING |  |  |  | 
Position | IN_PART_POSITION | VECTOR |  |  |  | 
Velocity | IN_PART_VELOCITY | VECTOR |  |  |  | 
Life | IN_PART_LIFE | BASETIME |  |  |  | 
Age | IN_PART_AGE | BASETIME |  |  |  | 
Size | IN_PART_SIZE | REAL |  |  |  | 
Scale | IN_PART_SCALE | VECTOR |  |  |  | 
Mass | IN_PART_MASS | REAL |  |  |  | 
Alignment | IN_PART_ALIGNMENT | MATRIX |  |  |  | 
Spin | IN_PART_SPIN | TP_SPIN |  |  |  | 
Shape | IN_PART_SHAPE | TP_SHAPE |  |  |  | 
Group | IN_PART_GROUP | TP_GROUP |  |  |  | 
DT Factor | IN_PART_DTFAC | REAL |  |  |  | 
Random Seed | IN_PART_RANDOMSEED | LONG |  |  |  | 
On | IN_PART_ON | BOOL |  |  |  | 
Color | IN_PART_COLOR | VECTOR |  |  |  | 
Particle | IN_PART_PARTICLE | TP_PARTICLE |  |  |  | 
