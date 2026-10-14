# Description: PFragment

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/thinking_particles/description/op_fragment.res`
- **Symbol:** `OP_Fragment`
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
Weight | FRAG_GRAD | GRADIENT |  |  |  | 
Threshold | FRAG_THRESH | REAL | 0.0 |  |  | 
Variation | FRAG_VAR | REAL | 0.0 | 100.0 |  | 
From to | FRAG_FROMTO | LONG |  |  |  | FRAG_FROMTO_NZ_PZ; FRAG_FROMTO_PZ_NZ; FRAG_FROMTO_NY_PY; FRAG_FROMTO_PY_NY; FRAG_FROMTO_NX_PX; FRAG_FROMTO_PX_NX
Type | FRAG_TYPE | LONG |  |  |  | FRAG_TYPE_FACE; FRAG_TYPE_SMOOTH; FRAG_TYPE_COUNT
Angle | FRAG_SANGLE | REAL | 0.0 | 180 |  | 
Radius | FRAG_SRAD | REAL | 0.0 |  |  | 
Count | FRAG_COUNT | LONG | 0 |  |  | 
No Fragments | FRAG_NOFRAG | BOOL |  |  |  | 
Alignment Correction | FRAG_ALIGNC | BOOL |  |  |  | 
Thickness | FRAG_THICK | REAL | 0.0 |  |  | 
Life Span | FRAG_LIFE | BASETIME | 0.0 |  |  | 
Variation | FRAG_LIFEVAR | REAL | 0.0 | 100.0 |  | 
Speed | FRAG_SPEED | REAL |  |  |  | 
Variation | FRAG_SPEEDVAR | REAL | 0.0 | 100.0 |  | 
Remaining Type | FRAG_RTYPE | LONG |  |  |  | FRAG_RTYPE_NONE; FRAG_RTYPE_HOLLOW; FRAG_RTYPE_SOLID
Thickness | FRAG_RTHICK | REAL | 0.0 |  |  | 
Die after Fragmentation | FRAG_DELP | BOOL |  |  |  | 
On | IN_FRAG_ON | BOOL |  |  |  | 
Animation Time | IN_FRAG_ATIME | BASETIME |  |  |  | 
Particle | IN_FRAG_PARTICLE | TP_PARTICLE |  |  |  | 
Born Particle | OUT_FRAG_PARTICLE | TP_PARTICLE |  |  |  | 
Particle Count | OUT_FRAG_PARTICLECOUNT | LONG |  |  |  | 
Particle Number | OUT_FRAG_PARTICLENUM | LONG |  |  |  | 
