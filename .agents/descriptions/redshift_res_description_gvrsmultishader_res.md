# Description: MultiShader Node

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `Redshift/res/description/gvrsmultishader.res`
- **Symbol:** `GVrsmultishader`
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
Source | GV_REDSHIFT_MULTISHADER_INDEX_SOURCE | LONG |  |  |  | GV_REDSHIFT_MULTISHADER_INDEX_SOURCE_VALUE; GV_REDSHIFT_MULTISHADER_INDEX_SOURCE_MOGRAPH_ID; GV_REDSHIFT_MULTISHADER_INDEX_SOURCE_OBJECT_ID; GV_REDSHIFT_MULTISHADER_INDEX_SOURCE_GEOMETRY_ID; GV_REDSHIFT_MULTISHADER_INDEX_SOURCE_PARTICLE_ID; GV_REDSHIFT_MULTISHADER_INDEX_SOURCE_INDEX_RATIO
Index | GV_REDSHIFT_MULTISHADER_INDEX | REAL | 0.0 |  |  | 
Range | GV_REDSHIFT_MULTISHADER_INDEX_RANGE | LONG |  |  |  | GV_REDSHIFT_MULTISHADER_INDEX_RANGE_INTEGER; GV_REDSHIFT_MULTISHADER_INDEX_RANGE_INTEGER_LOOP; GV_REDSHIFT_MULTISHADER_INDEX_RANGE_SCALAR_NORMALIZED; GV_REDSHIFT_MULTISHADER_INDEX_RANGE_SCALAR_NORMALIZED_CLAMPED
Width | GV_REDSHIFT_MULTISHADER_BAKE_TEXTURE_WIDTH | LONG | 1 |  |  | 
Height | GV_REDSHIFT_MULTISHADER_BAKE_TEXTURE_HEIGHT | LONG | 1 |  |  | 
Depth | GV_REDSHIFT_MULTISHADER_BAKE_TEXTURE_DEPTH | LONG |  |  |  | GV_REDSHIFT_MULTISHADER_BAKE_TEXTURE_DEPTH_8; GV_REDSHIFT_MULTISHADER_BAKE_TEXTURE_DEPTH_16; GV_REDSHIFT_MULTISHADER_BAKE_TEXTURE_DEPTH_32
Shader | GV_REDSHIFT_MULTISHADER_DEFAULT_PARAM | SHADERLINK |  |  |  | 
Slots | GV_REDSHIFT_MULTISHADER_SHADER_SLOTS | LONG | 0 | 500 |  | 
Add | GV_REDSHIFT_MULTISHADER_ADD | BUTTON |  |  |  | 
Clear | GV_REDSHIFT_MULTISHADER_CLEAR | BUTTON |  |  |  | 
Add Texture | GV_REDSHIFT_MULTISHADER_ADD_TEXTURE | BUTTON |  |  |  | 
Add From Folder | GV_REDSHIFT_MULTISHADER_ADD_FOLDER | BUTTON |  |  |  | 
Out Color | GV_REDSHIFT_MULTISHADER_OUTPUT_COLOR | RSCOLORALPHA |  |  |  | 
Count | GV_REDSHIFT_MULTISHADER_OUTPUT_COUNT | LONG |  |  |  | 
