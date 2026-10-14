# Description: PDeflector

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/thinking_particles/description/op_deflector.res`
- **Symbol:** `OP_Deflector`
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
Seed | UD_SEED | LONG | 0 |  |  | 
Object | UD_OBJECT | LINK |  |  |  | 
Deflector Type | UD_DTYPE | LONG |  |  |  | UD_DTYPE_BOX; UD_DTYPE_SPHERE; UD_DTYPE_OBJECT; UD_DTYPE_GEOM
X Size | UD_XSIZE | REAL | 0.0 |  |  | 
Y Size | UD_YSIZE | REAL | 0.0 |  |  | 
Z Size | UD_ZSIZE | REAL | 0.0 |  |  | 
Radius | UD_RADIUS | REAL | 0.0 |  |  | 
Collision Type | UD_CTYPE | LONG |  |  |  | UD_CTYPE_FRONT; UD_CTYPE_BACK; UD_CTYPE_TWO
Offset Type | UD_OTYPE | LONG |  |  |  | UD_OTYPE_NONE; UD_OTYPE_PSIZE_TRAVEL; UD_OTYPE_PSIZE_X; UD_OTYPE_PSIZE_Y; UD_OTYPE_PSIZE_Z; UD_OTYPE_VALUE_TRAVEL; UD_OTYPE_VALUE_X; UD_OTYPE_VALUE_Y; UD_OTYPE_VALUE_Z
Offset | UD_OFFSET | REAL |  |  |  | 
Variation | UD_OFFSETVAR | REAL | 0.0 | 100.0 |  | 
Bounce | UD_BOUNCE | REAL | 0.0 |  |  | 
Variation | UD_BOUNCEVAR | REAL | 0.0 | 100.0 |  | 
Surface | UD_SURFACE | REAL | 0.0 | 100.0 |  | 
Energy | UD_ENERGY | REAL | 0.0 |  |  | 
Friction | UD_FRICTION | REAL | 0.0 | 100.0 |  | 
Spin | UD_SPIN | REAL | 0.0 |  |  | 
Chaos | UD_CHAOS | REAL | 0.0 | 100.0 |  | 
Vel. Inheritance | UD_VELINHERI | REAL |  |  |  | 
Event Only | UD_EVENT | BOOL |  |  |  | 
Particle | IN_UD_PARTICLE | TP_PARTICLE |  |  |  | 
On | IN_UD_ON | BOOL |  |  |  | 
Animation Time | IN_UD_ATIME | BASETIME |  |  |  | 
Event | OUT_UD_EVENT | BOOL |  |  |  | 
Event Position | OUT_UD_EVENT_POSITION | VECTOR |  |  |  | 
Event Normal | OUT_UD_EVENT_NORMAL | NORMAL |  |  |  | 
Event Reflection | OUT_UD_EVENT_REFLECTION | NORMAL |  |  |  | 
