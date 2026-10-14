# Description: PWind

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/thinking_particles/description/op_wind.res`
- **Symbol:** `OP_Wind`
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
Icon Size | WIND_ICONSIZE | REAL | 0.0 |  |  | 
Object | WIND_OBJECT | LINK |  |  |  | 
Type | WIND_TYPE | LONG |  |  |  | WIND_TYPE_PLANAR; WIND_TYPE_SPHERICAL
Strength | WIND_STRENGTH | REAL |  |  |  | 
Decay | WIND_DECAY | REAL | 0.0 |  |  | 
Mass Dependence | WIND_MASSDEP | REAL | -100.0 | 100.0 |  | 
Size Dependence | WIND_SIZEDEP | REAL | -100.0 | 100.0 |  | 
Turbulence | WIND_TURBULENCE | REAL | 0.0 |  |  | 
Frequency | WIND_FREQUENCY | REAL | 0.0 |  |  | 
Structure Size | WIND_SCALE | REAL | 0.0 |  |  | 
On | IN_WIND_ON | BOOL |  |  |  | 
Animation Time | IN_WIND_ATIME | BASETIME |  |  |  | 
Particle | IN_WIND_PARTICLE | TP_PARTICLE |  |  |  | 
