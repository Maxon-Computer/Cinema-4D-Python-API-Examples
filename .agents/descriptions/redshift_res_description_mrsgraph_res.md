# Description: Redshift Shader Graph

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `Redshift/res/description/mrsgraph.res`
- **Symbol:** `Mrsgraph`
- **Category:** Materials

Use parameter symbols to access parameters and cycle option symbols for cycle values, never their numeric IDs. Treat Min and Max as constraints and Default as the declared initial value; blank cells mean the resource does not declare that metadata, not that the value is zero. Base Description Parameters lists inherited fields from each base; All Parameters lists the effective parameter set for this description.

## Base Description Parameters

### Material (`Mbase`)

No parameters.

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

### Assignment (`Massign`)

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Assignment | MATERIAL_PAGE_ASSIGNMENT | BOOL |  |  |  | 
No label | ID_MATERIALASSIGNMENTS | MATASSIGN |  |  |  | 

## All Parameters

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
No label | REDSHIFT_GRAPH_MAT_PREVIEW | MATPREVIEW |  |  |  | 
Icon File / ID | ID_BASELIST_ICON_FILE | TEXTURE |  |  |  | 
Icon Color | ID_BASELIST_ICON_COLORIZE_MODE | BOOL |  |  |  | 
Color | ID_BASELIST_ICON_COLOR | COLOR |  |  | 1.0 0.9 0.4 | 
No label | ID_BASELIST_ICON_PRESET_BUTTONS | ICONCHOOSER |  |  |  | 
Name | ID_BASELIST_NAME | STRING |  |  |  | 
Layer | ID_LAYER_LINK | LINK |  |  |  | 
No label | ID_BASELIST_NODESPACE_ADD_REMOVE_BUTTONS | NODESPACE_ADD_REMOVE |  |  |  | 
No label | MATERIAL_PAGE_PROPERTIES | BOOL |  |  |  | 
Edit Shader Graph... | REDSHIFT_GRAPH_BUTTON_EDIT | BUTTON |  |  |  | 
Nodes | REDSHIFT_GRAPH_SEPARATOR_NODES | SEPARATOR |  |  |  | 
Animate Preview | REDSHIFT_GRAPH_PREVIEW_ANIMATE | BOOL |  |  |  | 
Texture Preview Size | REDSHIFT_GRAPH_PREVIEW_SIZE | LONG |  |  |  | REDSHIFT_GRAPH_PREVIEW_SIZE_DEF; REDSHIFT_GRAPH_PREVIEW_SIZE_64; REDSHIFT_GRAPH_PREVIEW_SIZE_128; REDSHIFT_GRAPH_PREVIEW_SIZE_256; REDSHIFT_GRAPH_PREVIEW_SIZE_512; REDSHIFT_GRAPH_PREVIEW_SIZE_1024; REDSHIFT_GRAPH_PREVIEW_SIZE_2048; REDSHIFT_GRAPH_PREVIEW_SIZE_4096; REDSHIFT_GRAPH_PREVIEW_SIZE_8192; REDSHIFT_GRAPH_PREVIEW_SIZE_16384
Assignment | MATERIAL_PAGE_ASSIGNMENT | BOOL |  |  |  | 
No label | ID_MATERIALASSIGNMENTS | MATASSIGN |  |  |  | 
