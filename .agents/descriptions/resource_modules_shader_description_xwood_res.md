# Description: Wood

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/shader/description/xwood.res`
- **Symbol:** `xwood`
- **Category:** Shaders

Use parameter symbols to access parameters and cycle option symbols for cycle values, never their numeric IDs. Treat Min and Max as constraints and Default as the declared initial value; blank cells mean the resource does not declare that metadata, not that the value is zero. Base Description Parameters lists inherited fields from each base; All Parameters lists the effective parameter set for this description.

## Base Description Parameters

### No label (`Mpreview`)

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
No label | MATERIAL_PREVIEW | MATPREVIEW |  |  |  | 

### Shader (`Xbase`)

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Blur Offset | SHADER_MIPOFFSET | REAL | 0.0 | 100.0 |  | 
Blur Scale | SHADER_MIPSCALE | REAL | -100.0 | 100.0 |  | 

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
No label | MATERIAL_PREVIEW | MATPREVIEW |  |  |  | 
Icon File / ID | ID_BASELIST_ICON_FILE | TEXTURE |  |  |  | 
Icon Color | ID_BASELIST_ICON_COLORIZE_MODE | BOOL |  |  |  | 
Color | ID_BASELIST_ICON_COLOR | COLOR |  |  | 1.0 0.9 0.4 | 
No label | ID_BASELIST_ICON_PRESET_BUTTONS | ICONCHOOSER |  |  |  | 
Name | ID_BASELIST_NAME | STRING |  |  |  | 
Layer | ID_LAYER_LINK | LINK |  |  |  | 
No label | ID_BASELIST_NODESPACE_ADD_REMOVE_BUTTONS | NODESPACE_ADD_REMOVE |  |  |  | 
Blur Offset | SHADER_MIPOFFSET | REAL | 0.0 | 100.0 |  | 
Blur Scale | SHADER_MIPSCALE | REAL | -100.0 | 100.0 |  | 
Type | WOODSHADER_COLOR_PRESET | LONG |  |  |  | WOODSHADER_COLOR_PRESET_CUSTOM; WOODSHADER_COLOR_PRESET_WALNUT; WOODSHADER_COLOR_PRESET_MAHAGONY; WOODSHADER_COLOR_PRESET_JACARANDA; WOODSHADER_COLOR_PRESET_PINEWOOD
Color | WOODSHADER_COLOR | GRADIENT |  |  |  | 
Scale | WOODSHADER_SCALE | REAL | 0.0 |  |  | 
Stretch | WOODSHADER_STRETCH | REAL | 0.0 |  |  | 
Ring Scale | WOODSHADER_RING_SCALE | REAL | 0.0 |  |  | 
Grainy | WOODSHADER_GRAINY | REAL | 0.0 |  |  | 
Grain Scale | WOODSHADER_GRAIN_SCALE | REAL | 0.0 |  |  | 
Wavy | WOODSHADER_WAVY | REAL | 0.0 |  |  | 
Wavy Scale | WOODSHADER_WAVY_SCALE | REAL | 0.0 |  |  | 
Shift | WOODSHADER_SHIFT | REAL | 0.0 |  |  | 
Annual Rings | WOODSHADER_RINGMODE | BOOL |  |  |  | 
Wavy Rings | WOODSHADER_RING_WAVY | REAL | 0.0 |  |  | 
Wavy Rings Scale | WOODSHADER_RING_WAVY_SCALE | VECTOR | 0.0 |  |  | 
Type | WOODSHADER_SIMPLE_TYPE | LONG |  |  |  | WOODSHADER_SIMPLE_TYPE_CUSTOM; WOODSHADER_SIMPLE_TYPE_WALNUT; WOODSHADER_SIMPLE_TYPE_MAHOGANY; WOODSHADER_SIMPLE_TYPE_JACARANDA; WOODSHADER_SIMPLE_TYPE_PINEWOOD
Color | WOODSHADER_SIMPLE_COLOR | GRADIENT |  |  |  | 
Frequency | WOODSHADER_SIMPLE_SCALE | VECTOR | 0.0 |  |  | 
Turbulence | WOODSHADER_SIMPLE_TURBULENCE | REAL | 0.0 | 300.0 |  | 
Legacy | WOODSHADER_LEGACY | BOOL |  |  |  | 
