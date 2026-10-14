# Description: Gradient Shader

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/sla/description/xslagradient.res`
- **Symbol:** `XSLAGradient`
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
Gradient | SLA_GRADIENT_GRADIENT | GRADIENT |  |  |  | 
Type | SLA_GRADIENT_TYPE | LONG |  |  |  | SLA_GRADIENT_TYPE_2D_U; SLA_GRADIENT_TYPE_2D_V; SLA_GRADIENT_TYPE_2D_DIAG; SLA_GRADIENT_TYPE_2D_RAD; SLA_GRADIENT_TYPE_2D_CIRC; SLA_GRADIENT_TYPE_2D_BOX; SLA_GRADIENT_TYPE_2D_STAR; SLA_GRADIENT_TYPE_2D_FOUR_CORNER; SLA_GRADIENT_TYPE_3D_LINEAR; SLA_GRADIENT_TYPE_3D_CYLINDRICAL; SLA_GRADIENT_TYPE_3D_SPHERICAL
Cycle | SLA_GRADIENT_CYCLE | BOOL |  |  |  | 
Start | SLA_GRADIENT_START | VECTOR |  |  |  | 
End | SLA_GRADIENT_END | VECTOR |  |  |  | 
Radius | SLA_GRADIENT_RADIUS | REAL |  |  |  | 
Turbulence | SLA_GRADIENT_TURBULENCE | REAL | 0 | 100 |  | 
Octaves | SLA_GRADIENT_OCTAVES | REAL | 0 | 10 |  | 
Scale | SLA_GRADIENT_SCALE | REAL | 0 |  |  | 
Frequency | SLA_GRADIENT_FREQ | REAL |  |  |  | 
Seed | SLA_GRADIENT_SEED | LONG |  |  |  | 
Angle | SLA_GRADIENT_ANGLE | REAL |  |  |  | 
Absolute | SLA_GRADIENT_ABSOLUTE | BOOL |  |  |  | 
Space | SLA_GRADIENT_SPACE | LONG |  |  |  | SLA_GRADIENT_SPACE_TEXTURE; SLA_GRADIENT_SPACE_OBJECT; SLA_GRADIENT_SPACE_WORLD; SLA_GRADIENT_SPACE_CAMERA; SLA_GRADIENT_SPACE_SCREEN; SLA_GRADIENT_SPACE_RASTER
