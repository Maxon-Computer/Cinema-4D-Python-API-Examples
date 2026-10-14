# Description: PBlurp

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/thinking_particles/description/op_blurp.res`
- **Symbol:** `OP_Blurp`
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
Objects | OP_BLURP_OBJECTS | IN_EXCLUDE |  |  |  | 
Animation Phase | OP_BLURP_PHASE | REAL | 0.0 | 100.0 |  | 
Stay | OP_BLURP_STAY | REAL | 0.0 |  |  | 
Frag | OP_BLURP_FRAG | REAL | 0.0 |  |  | 
Next | OP_BLURP_NEXT | REAL | 0.0 |  |  | 
In Tangent | OP_BLURP_INTANGENT | REAL | 0.0 |  |  | 
Out Tangent | OP_BLURP_OUTTANGENT | REAL | 0.0 |  |  | 
From to | OP_BLURP_FROMTO | LONG |  |  |  | OP_BLURP_FROMTO_NZ_PZ; OP_BLURP_FROMTO_PZ_NZ; OP_BLURP_FROMTO_NY_PY; OP_BLURP_FROMTO_PY_NY; OP_BLURP_FROMTO_NX_PX; OP_BLURP_FROMTO_PX_NX
Type | OP_BLURP_TYPE | LONG |  |  |  | OP_BLURP_TYPE_FACE; OP_BLURP_TYPE_SMOOTH; OP_BLURP_TYPE_COUNT
Angle | OP_BLURP_SANGLE | REAL | 0.0 | 180 |  | 
Radius | OP_BLURP_SRAD | REAL | 0.0 |  |  | 
Count | OP_BLURP_COUNT | LONG | 0 |  |  | 
Thickness | OP_BLURP_THICK | REAL | 0.0 |  |  | 
No Fragments | OP_BLURP_NOFRAG | BOOL |  |  |  | 
Remaining Type | OP_BLURP_RTYPE | LONG |  |  |  | OP_BLURP_RTYPE_NONE; OP_BLURP_RTYPE_HOLLOW; OP_BLURP_RTYPE_SOLID
Thickness | OP_BLURP_RTHICK | REAL | 0.0 |  |  | 
On | OP_BLURP_IN_ON | BOOL |  |  |  | 
Animation Time | OP_BLURP_IN_ATIME | BASETIME |  |  |  | 
Remaining Particle | OP_BLURP_OUT_REMAINING | TP_PARTICLE |  |  |  | 
Remaining Count | OP_BLURP_OUT_REMAININGCOUNT | LONG |  |  |  | 
Remaining Number | OP_BLURP_OUT_REMAININGNUM | LONG |  |  |  | 
Fragment Particle | OP_BLURP_OUT_FRAGMENT | TP_PARTICLE |  |  |  | 
Fragment Count | OP_BLURP_OUT_FRAGMENTCOUNT | LONG |  |  |  | 
Fragment Number | OP_BLURP_OUT_FRAGMENTNUM | LONG |  |  |  | 
