# Description: Falloff

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/mograph/description/gvmograph_falloff.res`
- **Symbol:** `GVmograph_falloff`
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

### Fields Panel (`Ofalloff_panel`)

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Switch To Field | FALLOFF_SWITCHTOFIELD | BUTTON |  |  |  | 
Field | FIELDS | FIELDLIST |  |  |  | 
Shape | FALLOFF_MODE | LONG |  |  |  | 
Invert | FALLOFF_INVERT | BOOL |  |  |  | 
Visible | FALLOFF_VISIBLE | BOOL |  |  |  | 

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
Switch To Field | FALLOFF_SWITCHTOFIELD | BUTTON |  |  |  | 
Field | FIELDS | FIELDLIST |  |  |  | 
Shape | FALLOFF_MODE | LONG |  |  |  | 
Invert | FALLOFF_INVERT | BOOL |  |  |  | 
Visible | FALLOFF_VISIBLE | BOOL |  |  |  | 
Falloff Matrix | GV_MG_FALLOFF_MATRIX | MATRIX |  |  |  | 
Sample Position | GV_MG_FALLOFF_POSITION | VECTOR |  |  |  | 
Normal Direction | GV_MG_FALLOFF_NORMAL | VECTOR |  |  |  | 
UVW Coordinate | GV_MG_FALLOFF_UVW | VECTOR |  |  |  | 
Array Size | GV_MG_FALLOFF_ITERATIONCOUNT | LONG | 1 |  |  | 
Index | GV_MG_FALLOFF_ITERATION | LONG | 0 |  |  | 
Value | GV_MG_FALLOFF_VALUE | REAL |  |  |  | 
Color | GV_MG_FALLOFF_COLOR | VECTOR |  |  |  | 
Direction | GV_MG_FALLOFF_DIRECTION | VECTOR |  |  |  | 
