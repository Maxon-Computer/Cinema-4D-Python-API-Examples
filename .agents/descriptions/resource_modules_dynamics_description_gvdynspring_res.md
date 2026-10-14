# Description: Dynamics Spring State

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/dynamics/description/gvdynspring.res`
- **Symbol:** `GVdynspring`
- **Category:** Graph View

Use parameter symbols to access parameters and cycle option symbols for cycle values, never their numeric IDs. Treat Min and Max as constraints and Default as the declared initial value; blank cells mean the resource does not declare that metadata, not that the value is zero. Base Description Parameters lists inherited fields from each base; All Parameters lists the effective parameter set for this description.

## Base Description Parameters

### Dynamics Interaction State (`GVdyninteraction`)

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Object | DYNAMICS_INTERACTION_NODE_OBJECT | LINK |  |  |  | 
On | DYNAMICS_INTERACTION_NODE_INPUT_ON | BOOL |  |  |  | 
Object | DYNAMICS_INTERACTION_NODE_INPUT_OBJECT | GVGENERALOBJECT |  |  |  | 
Object Index | DYNAMICS_INTERACTION_NODE_INPUT_INDEX | LONG | 0 |  |  | 
Count | DYNAMICS_INTERACTION_NODE_OUTPUT_COUNT | LONG |  |  |  | 
Object | DYNAMICS_INTERACTION_NODE_OUTPUT_OBJECT | GVGENERALOBJECT |  |  |  | 
Object A | DYNAMICS_INTERACTION_NODE_OUTPUT_OBJECT_A | GVGENERALOBJECT |  |  |  | 
Tag A | DYNAMICS_INTERACTION_NODE_OUTPUT_TAG_A | GVGENERALTAG |  |  |  | 
Object Index A | DYNAMICS_INTERACTION_NODE_OUTPUT_INDEX_A | LONG |  |  |  | 
Object B | DYNAMICS_INTERACTION_NODE_OUTPUT_OBJECT_B | GVGENERALOBJECT |  |  |  | 
Tag B | DYNAMICS_INTERACTION_NODE_OUTPUT_TAG_B | GVGENERALTAG |  |  |  | 
Object Index B | DYNAMICS_INTERACTION_NODE_OUTPUT_INDEX_B | LONG |  |  |  | 

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
Object | DYNAMICS_INTERACTION_NODE_OBJECT | LINK |  |  |  | 
On | DYNAMICS_INTERACTION_NODE_INPUT_ON | BOOL |  |  |  | 
Object | DYNAMICS_INTERACTION_NODE_INPUT_OBJECT | GVGENERALOBJECT |  |  |  | 
Object Index | DYNAMICS_INTERACTION_NODE_INPUT_INDEX | LONG | 0 |  |  | 
Count | DYNAMICS_INTERACTION_NODE_OUTPUT_COUNT | LONG |  |  |  | 
Object | DYNAMICS_INTERACTION_NODE_OUTPUT_OBJECT | GVGENERALOBJECT |  |  |  | 
Object A | DYNAMICS_INTERACTION_NODE_OUTPUT_OBJECT_A | GVGENERALOBJECT |  |  |  | 
Tag A | DYNAMICS_INTERACTION_NODE_OUTPUT_TAG_A | GVGENERALTAG |  |  |  | 
Object Index A | DYNAMICS_INTERACTION_NODE_OUTPUT_INDEX_A | LONG |  |  |  | 
Object B | DYNAMICS_INTERACTION_NODE_OUTPUT_OBJECT_B | GVGENERALOBJECT |  |  |  | 
Tag B | DYNAMICS_INTERACTION_NODE_OUTPUT_TAG_B | GVGENERALTAG |  |  |  | 
Object Index B | DYNAMICS_INTERACTION_NODE_OUTPUT_INDEX_B | LONG |  |  |  | 
Linear Plastic Elongation | SPRING_NODE_INPUT_LINEAR_PLASTIC_ELONGATION | REAL |  |  |  | 
Angular Plastic Elongation | SPRING_NODE_INPUT_ANGULAR_PLASTIC_ELONGATION | REAL |  |  |  | 
Broken | DYNAMICS_INTERACTION_NODE_INPUT_BROKEN | BOOL |  |  |  | 
Linear Plastic Elongation | SPRING_NODE_OUTPUT_LINEAR_PLASTIC_ELONGATION | REAL |  |  |  | 
Angular Plastic Elongation | SPRING_NODE_OUTPUT_ANGULAR_PLASTIC_ELONGATION | REAL |  |  |  | 
Broken | DYNAMICS_INTERACTION_NODE_OUTPUT_BROKEN | BOOL |  |  |  | 
