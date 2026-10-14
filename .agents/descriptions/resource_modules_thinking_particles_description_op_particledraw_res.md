# Description: PDraw

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/thinking_particles/description/op_particledraw.res`
- **Symbol:** `OP_ParticleDraw`
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
Type | OP_PARTICLEDRAW_TYPE | LONG |  |  |  | OP_PARTICLEDRAW_TYPE_POINT; OP_PARTICLEDRAW_TYPE_SPHERICAL
Radius | OP_PARTICLEDRAW_RADIUS | REAL | 0.0 |  |  | 
Count | OP_PARTICLEDRAW_COUNT | LONG | 1 |  |  | 
Draw Position | OP_PARTICLEDRAW_DRAWPOS | VECTOR |  |  |  | 
Life Time | OP_PARTICLEDRAW_LIFE | BASETIME | 0.0 |  |  | 
Life Variation | OP_PARTICLEDRAW_LIFEVAR | REAL | 0.0 | 100.0 |  | 
Random Seed | OP_PARTICLEDRAW_SEED | LONG | 0 |  |  | 
Remove | OP_PARTICLEDRAW_REMOVE | BUTTON |  |  |  | 
On | OP_PARTICLEDRAW_ON | BOOL |  |  |  | 
Animation Time | OP_PARTICLEDRAW_ATIME | BASETIME |  |  |  | 
Particle Birth | OP_PARTICLEDRAW_OUT_PARTICLE | TP_PARTICLE |  |  |  | 
Birth Count | OP_PARTICLEDRAW_OUT_PARTICLECOUNT | LONG |  |  |  | 
Birth Num | OP_PARTICLEDRAW_OUT_PARTICLENUM | LONG |  |  |  | 
