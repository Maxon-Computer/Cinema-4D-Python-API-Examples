# Description: PStorm

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/thinking_particles/description/op_storm.res`
- **Symbol:** `OP_Storm`
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
Random Seed | ST_SEED | LONG | 0 |  |  | 
Type | ST_TYPE | LONG |  |  |  | ST_TYPE_RECTANGLE; ST_TYPE_CIRCLE
Birth Type | ST_BTYPE | LONG |  |  |  | ST_BTYPE_COUNT; ST_BTYPE_RATE; ST_BTYPE_SHOT
Count | ST_COUNT | LONG | 0 |  |  | 
Rate | ST_RATE | REAL | 0.0 |  |  | 
Shot | ST_SHOT | LONG | 0 |  |  | 
Life | ST_LIFE | BASETIME | 0.0 |  |  | 
Life Variation | ST_LIFEVAR | REAL | 0.0 | 100.0 |  | 
Speed | ST_SPEED | REAL |  |  |  | 
Speed Variation | ST_SPEEDVAR | REAL | 0.0 | 100.0 |  | 
Size | ST_SIZE | REAL | 0.0 |  |  | 
Size Variation | ST_SIZEVAR | REAL | 0.0 | 100.0 |  | 
X Fov | ST_XANGLE | REAL | 0.0 | 360.0 |  | 
Y Fov | ST_YANGLE | REAL | 0.0 | 360.0 |  | 
X Size | ST_XSIZE | REAL | 0.0 |  |  | 
Y Size | ST_YSIZE | REAL | 0.0 |  |  | 
Distance | ST_DIST | REAL | 0.0 |  |  | 
Distance Variation | ST_DISTVAR | REAL | 0.0 | 100.0 |  | 
Spin | ST_SPIN | REAL | 0.0 |  |  | 
Spin Variation | ST_SPINVAR | REAL | 0.0 | 100.0 |  | 
Spin Type | ST_SPINTYPE | LONG |  |  |  | ST_SPINTYPE_RANDOM; ST_SPINTYPE_USER
Spin Axis | ST_SPINAXIS | VECTOR |  |  |  | 
On | IN_ST_ON | BOOL |  |  |  | 
Animation Time | IN_ST_ATIME | BASETIME |  |  |  | 
Emitter Alignment | IN_ST_ALIGNMENT | MATRIX |  |  |  | 
Emitter Velocity | IN_ST_VELOCITY | VECTOR |  |  |  | 
Emitter Position | IN_ST_POSITION | VECTOR |  |  |  | 
Particle Birth | OUT_ST_PARTICLE | TP_PARTICLE |  |  |  | 
Birth Count | OUT_ST_PARTICLECOUNT | LONG |  |  |  | 
Birth Num | OUT_ST_PARTICLENUM | LONG |  |  |  | 
