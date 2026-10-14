# Description: PSpin

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/thinking_particles/description/op_spin.res`
- **Symbol:** `OP_Spin`
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
Evaltime | SPIN_INTENS | REAL | 0.0 |  |  | 
Time | SPIN_TIME | REAL | 0.0 |  |  | 
Variation | SPIN_TIMEVAR | REAL | 0.0 | 100.0 |  | 
Phase | SPIN_PHASE | REAL |  |  |  | 
Variation | SPIN_PHASEVAR | REAL | 0.0 | 100.0 |  | 
Friction | SPIN_FRIC | REAL | 0.0 |  |  | 
Speed Dependence | SPIN_SPEEDDEP | REAL | 0.0 |  |  | 
Size Dependence | SPIN_SIZEDEP | REAL | 0.0 |  |  | 
Axis Type | SPIN_AXISTYPE | LONG |  |  |  | SPIN_AXISTYPE_RANDOM; SPIN_AXISTYPE_TRAVEL; SPIN_AXISTYPE_USER
Axis | SPIN_AXIS | VECTOR |  |  |  | 
Variation | SPIN_AXISVAR | REAL | 0.0 | 180.0 |  | 
On | IN_SPIN_ON | BOOL |  |  |  | 
Animation Time | IN_SPIN_ATIME | BASETIME |  |  |  | 
Particle | IN_SPIN_PARTICLE | TP_PARTICLE |  |  |  | 
