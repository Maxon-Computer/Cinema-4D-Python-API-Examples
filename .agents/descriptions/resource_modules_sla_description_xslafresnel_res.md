# Description: Fresnel Shader

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/sla/description/xslafresnel.res`
- **Symbol:** `XSLAFresnel`
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
Use Bump | SLA_FRESNEL_USE_BUMP | BOOL |  |  |  | 
Render | SLA_FRESNEL_RENDER | LONG |  |  |  | SLA_FRESNEL_RENDER_FRONT_ONLY; SLA_FRESNEL_RENDER_FRONT_TRANS; SLA_FRESNEL_RENDER_BACK_ONLY; SLA_FRESNEL_RENDER_BACK_TRANS; SLA_FRESNEL_RENDER_FRONT_BACK
Gradient | SLA_FRESNEL_GRADIENT | GRADIENT |  |  |  | 
Physical | SLA_FRESNEL_PHY_ENABLE | BOOL |  |  |  | 
IOR | SLA_FRESNEL_PHY_IOR | REAL | 1.0 |  |  | 
Preset | SLA_FRESNEL_PHY_IOR_PRESET | LONG |  |  |  | SLA_FRESNEL_PHY_IOR_PRESET_CUSTOM; SLA_FRESNEL_PHY_IOR_PRESET_ASPHALT; SLA_FRESNEL_PHY_IOR_PRESET_BEER; SLA_FRESNEL_PHY_IOR_PRESET_BRONZE; SLA_FRESNEL_PHY_IOR_PRESET_COPPER; SLA_FRESNEL_PHY_IOR_PRESET_DIAMOND; SLA_FRESNEL_PHY_IOR_PRESET_EMERALD; SLA_FRESNEL_PHY_IOR_PRESET_ETHANOL; SLA_FRESNEL_PHY_IOR_PRESET_GLASS; SLA_FRESNEL_PHY_IOR_PRESET_HEAVYFLINTGLASS; SLA_FRESNEL_PHY_IOR_PRESET_IRON; SLA_FRESNEL_PHY_IOR_PRESET_JADE; SLA_FRESNEL_PHY_IOR_PRESET_MILK; SLA_FRESNEL_PHY_IOR_PRESET_MOONSTONE; SLA_FRESNEL_PHY_IOR_PRESET_OIL_VEGETABLE; SLA_FRESNEL_PHY_IOR_PRESET_OPAL; SLA_FRESNEL_PHY_IOR_PRESET_PEARL; SLA_FRESNEL_PHY_IOR_PRESET_PLASTIC; SLA_FRESNEL_PHY_IOR_PRESET_PET; SLA_FRESNEL_PHY_IOR_PRESET_PLEXIGLASS; SLA_FRESNEL_PHY_IOR_PRESET_RUBBER; SLA_FRESNEL_PHY_IOR_PRESET_RUBY; SLA_FRESNEL_PHY_IOR_PRESET_SALT; SLA_FRESNEL_PHY_IOR_PRESET_SAPPHIRE; SLA_FRESNEL_PHY_IOR_PRESET_TEFLON; SLA_FRESNEL_PHY_IOR_PRESET_TITANIUM; SLA_FRESNEL_PHY_IOR_PRESET_TOPAZ; SLA_FRESNEL_PHY_IOR_PRESET_WATER; SLA_FRESNEL_PHY_IOR_PRESET_WATER_ICE; SLA_FRESNEL_PHY_IOR_PRESET_WHISKEY; SLA_FRESNEL_PHY_IOR_PRESET_WOOD
Invert | SLA_FRESNEL_PHY_INVERT | BOOL |  |  |  | 
