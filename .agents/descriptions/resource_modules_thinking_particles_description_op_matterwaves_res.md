# Description: PMatterWaves

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/thinking_particles/description/op_matterwaves.res`
- **Symbol:** `OP_MatterWaves`
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
Random Seed | OP_MATTERWAVES_SEED | LONG | 0 |  |  | 
Object | OP_MATTERWAVES_OBJECT | LINK |  |  |  | 
Selection | OP_MATTERWAVES_SELECTION | STRING |  |  |  | 
UVW | OP_MATTERWAVES_UVW | STRING |  |  |  | 
UVW Type | OP_MATTERWAVES_UVWTYPE | LONG |  |  |  | OP_MATTERWAVES_UVWTYPE_CLAMP; OP_MATTERWAVES_UVWTYPE_UNCLAMP
Lights | OP_MATTERWAVES_LIGHTLIST | IN_EXCLUDE |  |  |  | 
Birth Type | OP_MATTERWAVES_BTYPE | LONG |  |  |  | OP_MATTERWAVES_BTYPE_COUNT; OP_MATTERWAVES_BTYPE_RATE; OP_MATTERWAVES_BTYPE_SHOT
Count | OP_MATTERWAVES_COUNT | LONG | 0 |  |  | 
Rate | OP_MATTERWAVES_RATE | REAL | 0.0 |  |  | 
Shot | OP_MATTERWAVES_SHOT | LONG | 0 |  |  | 
Birth Type | OP_MATTERWAVES_BIRTHTYPE | LONG |  |  |  | OP_MATTERWAVES_BIRTHTYPE_CONSTANT; OP_MATTERWAVES_BIRTHTYPE_MAP; OP_MATTERWAVES_BIRTHTYPE_LIGHT; OP_MATTERWAVES_BIRTHTYPE_MAPLIGHT
Birth Texture | OP_MATTERWAVES_BIRTHTEX | SHADERLINK |  |  |  | 
Birth Gradient | OP_MATTERWAVES_BIRTHGRAD | GRADIENT |  |  |  | 
Life | OP_MATTERWAVES_LIFE | BASETIME | 0.0 |  |  | 
Life Variation | OP_MATTERWAVES_LIFEVAR | REAL | 0.0 | 100.0 |  | 
Life Type | OP_MATTERWAVES_LIFETYPE | LONG |  |  |  | OP_MATTERWAVES_LIFETYPE_CONSTANT; OP_MATTERWAVES_LIFETYPE_MAP; OP_MATTERWAVES_LIFETYPE_LIGHT; OP_MATTERWAVES_LIFETYPE_MAPLIGHT
Life Texture | OP_MATTERWAVES_LIFETEX | SHADERLINK |  |  |  | 
Life Gradient | OP_MATTERWAVES_LIFEGRAD | GRADIENT |  |  |  | 
Speed | OP_MATTERWAVES_SPEED | REAL |  |  |  | 
Speed Variation | OP_MATTERWAVES_SPEEDVAR | REAL | 0.0 | 100.0 |  | 
Speed Type | OP_MATTERWAVES_SPEEDTYPE | LONG |  |  |  | OP_MATTERWAVES_SPEEDTYPE_CONSTANT; OP_MATTERWAVES_SPEEDTYPE_MAP; OP_MATTERWAVES_SPEEDTYPE_LIGHT; OP_MATTERWAVES_SPEEDTYPE_MAPLIGHT
Speed Texture | OP_MATTERWAVES_SPEEDTEX | SHADERLINK |  |  |  | 
Speed Gradient | OP_MATTERWAVES_SPEEDGRAD | GRADIENT |  |  |  | 
Size | OP_MATTERWAVES_SIZE | REAL |  |  |  | 
Size Variation | OP_MATTERWAVES_SIZEVAR | REAL | 0.0 | 100.0 |  | 
Size Type | OP_MATTERWAVES_SIZETYPE | LONG |  |  |  | OP_MATTERWAVES_SIZETYPE_CONSTANT; OP_MATTERWAVES_SIZETYPE_MAP; OP_MATTERWAVES_SIZETYPE_LIGHT; OP_MATTERWAVES_SIZETYPE_MAPLIGHT
Size Texture | OP_MATTERWAVES_SIZETEX | SHADERLINK |  |  |  | 
Size Gradient | OP_MATTERWAVES_SIZEGRAD | GRADIENT |  |  |  | 
Distance | OP_MATTERWAVES_DISTANCE | REAL |  |  |  | 
Distance Variation | OP_MATTERWAVES_DISTVAR | REAL | 0.0 | 100.0 |  | 
Distance Type | OP_MATTERWAVES_DISTTYPE | LONG |  |  |  | OP_MATTERWAVES_DISTTYPE_CONSTANT; OP_MATTERWAVES_DISTTYPE_MAP; OP_MATTERWAVES_DISTTYPE_LIGHT; OP_MATTERWAVES_DISTTYPE_MAPLIGHT
Distance Texture | OP_MATTERWAVES_DISTTEX | SHADERLINK |  |  |  | 
Distance Gradient | OP_MATTERWAVES_DISTGRAD | GRADIENT |  |  |  | 
Direction | OP_MATTERWAVES_DIRINTENS | REAL | 0.0 |  |  | 
Direction Variation | OP_MATTERWAVES_DIRVAR | REAL | 0.0 | 180.0 |  | 
Direction Type | OP_MATTERWAVES_DIRTYPE | LONG |  |  |  | OP_MATTERWAVES_DIRTYPE_NORMAL; OP_MATTERWAVES_DIRTYPE_MAP; OP_MATTERWAVES_DIRTYPE_LIGHTDIR; OP_MATTERWAVES_DIRTYPE_LIGHTREF
Direction Texture | OP_MATTERWAVES_DIRTEX | SHADERLINK |  |  |  | 
Direction Gradient | OP_MATTERWAVES_DIRGRAD | GRADIENT |  |  |  | 
On | OP_MATTERWAVES_IN_ON | BOOL |  |  |  | 
Animation Time | OP_MATTERWAVES_IN_ATIME | BASETIME |  |  |  | 
Particle | OP_MATTERWAVES_IN_PARTICLE | TP_PARTICLE |  |  |  | 
Particle Birth | OP_MATTERWAVES_OUT_PARTICLE | TP_PARTICLE |  |  |  | 
Birth Count | OP_MATTERWAVES_OUT_PARTICLECOUNT | LONG |  |  |  | 
Birth Num | OP_MATTERWAVES_OUT_PARTICLENUM | LONG |  |  |  | 
Birth UVW | OP_MATTERWAVES_OUT_UVW | VECTOR |  |  |  | 
