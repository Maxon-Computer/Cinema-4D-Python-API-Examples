# Description: Proximal Shader

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/sla/description/xslaproximal.res`
- **Symbol:** `XSLAProximal`
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
Objects | SLA_PROXIMAL_OBJECTS | IN_EXCLUDE |  |  |  | 
Exclude Parent | SLA_PROXIMAL_EXCLUDE_PARENT | BOOL |  |  |  | 
Include Subobjects | SLA_PROXIMAL_INCLUDE_SUBOBJECTS | BOOL |  |  |  | 
Use Vertices | SLA_PROXIMAL_USE_VERTICES | BOOL |  |  |  | 
Use Edges | SLA_PROXIMAL_USE_EDGES | BOOL |  |  |  | 
Polygon Radius | SLA_PROXIMAL_POLYGON_RADIUS | BOOL |  |  |  | 
Function | SLA_PROXIMAL_FUNCTION | LONG |  |  |  | SLA_PROXIMAL_FUNCTION_LINEAR; SLA_PROXIMAL_FUNCTION_SQUARE; SLA_PROXIMAL_FUNCTION_CUBIC; SLA_PROXIMAL_FUNCTION_STEP; SLA_PROXIMAL_FUNCTION_INVERSE; SLA_PROXIMAL_FUNCTION_INVERSE_SQUARE; SLA_PROXIMAL_FUNCTION_INVERSE_CUBIC; SLA_PROXIMAL_FUNCTION_SMOOTH
Blend Mode | SLA_PROXIMAL_BLEND_MODE | LONG |  |  |  | SLA_PROXIMAL_BLEND_MODE_LIGHTEN; SLA_PROXIMAL_BLEND_MODE_SCREEN; SLA_PROXIMAL_BLEND_MODE_DIFFERENCE; SLA_PROXIMAL_BLEND_MODE_EXCLUSION; SLA_PROXIMAL_BLEND_MODE_ADD
Start Distance | SLA_PROXIMAL_START_DISTANCE | REAL | 0 |  |  | 
End Distance | SLA_PROXIMAL_END_DISTANCE | REAL | 0 |  |  | 
Intensity | SLA_PROXIMAL_INTENSITY | REAL | 0 |  |  | 
