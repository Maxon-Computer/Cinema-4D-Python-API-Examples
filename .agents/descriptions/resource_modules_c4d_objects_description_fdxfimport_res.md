# Description: DXF Import Settings

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/c4d_objects/description/fdxfimport.res`
- **Symbol:** `Fdxfimport`
- **Category:** Files

Use parameter symbols to access parameters and cycle option symbols for cycle values, never their numeric IDs. Treat Min and Max as constraints and Default as the declared initial value; blank cells mean the resource does not declare that metadata, not that the value is zero. Base Description Parameters lists inherited fields from each base; All Parameters lists the effective parameter set for this description.

## Base Description Parameters

### Filter (`Fbase`)

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Presets | PRESET_OPTIONS_PRESETS | LONG |  |  | 0 | 
Save... | PRESET_OPTIONS_PRESETS_CUSTOM_SAVEBUTTON | BUTTON |  |  |  | 
Delete... | PRESET_OPTIONS_PRESETS_CUSTOM_DELETEBUTTON | BUTTON |  |  |  | 

## All Parameters

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Presets | PRESET_OPTIONS_PRESETS | LONG |  |  | 0 | 
Save... | PRESET_OPTIONS_PRESETS_CUSTOM_SAVEBUTTON | BUTTON |  |  |  | 
Delete... | PRESET_OPTIONS_PRESETS_CUSTOM_DELETEBUTTON | BUTTON |  |  |  | 
Scale | DXFIMPORTFILTER_SCALE | UNITSCALE |  |  |  | 
Circle Subdivision | DXFIMPORTFILTER_CIRCLESEGMENTS | LONG | 12 | 500 | 72 | 
Connect | DXFIMPORTFILTER_LAYER | LONG |  |  | DXFIMPORTFILTER_LAYER_BYCOLOR | DXFIMPORTFILTER_LAYER_NONE; DXFIMPORTFILTER_LAYER_BYLAYER; DXFIMPORTFILTER_LAYER_BYCOLOR
Frozen Layers | DXFIMPORTFILTER_FROZEN | BOOL |  |  | 0 | 
2D Elements | DXFIMPORTFILTER_ELEMENTS2D | BOOL |  |  | 0 | 
Align Normals | DXFIMPORTFILTER_ALIGN | BOOL |  |  | 1 | 
Triangulate Polygons | DXFIMPORTFILTER_TRIANGULATE | BOOL |  |  | 1 | 
