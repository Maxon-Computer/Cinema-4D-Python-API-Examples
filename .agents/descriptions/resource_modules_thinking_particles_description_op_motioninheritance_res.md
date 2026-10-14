# Description: PMotionInheritance

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/thinking_particles/description/op_motioninheritance.res`
- **Symbol:** `OP_MotionInheritance`
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
Object | MINH_OBJECT | LINK |  |  |  | 
Inheritance | MINH_INHERI | REAL |  |  |  | 
Variation | MINH_VAR | REAL | 0.0 | 100.0 |  | 
Rotation Inheri. | MINH_ROTINHERI | REAL |  |  |  | 
Variation | MINH_ROTVAR | REAL | 0.0 | 100.0 |  | 
Direction Var. | MINH_DIRVAR | REAL | 0.0 |  |  | 
Type | MINH_DTYPE | LONG |  |  |  | MINH_DTYPE_NONE; MINH_DTYPE_SPHERE; MINH_DTYPE_CYLINDER
Radius | MINH_DIST | REAL | 0.0 |  |  | 
Distance Gradient | MINH_DGRAD | GRADIENT |  |  |  | 
Cylinder Axis | MINH_CAXIS | LONG |  |  |  | MINH_CAXIS_X; MINH_CAXIS_Y; MINH_CAXIS_Z
Cylinder Height | MINH_CHEIGHT | REAL | 0.0 |  |  | 
Cylinder Gradient | MINH_CGRAD | GRADIENT |  |  |  | 
Scale Gradient | MINH_SGRAD | GRADIENT |  |  |  | 
On | IN_MINH_ON | BOOL |  |  |  | 
Animation Time | IN_MINH_ATIME | BASETIME |  |  |  | 
Particle | IN_MINH_PARTICLE | TP_PARTICLE |  |  |  | 
