# Description: Hierarchy Operator

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/xpressocore/description/gvhierarchy.res`
- **Symbol:** `GVhierarchy`
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
Reference | GV_HIERARCHY_OBJECT_ID | LINK |  |  |  | 
Reference Mode | GV_HIERARCHY_PATH_TYPE | LONG |  |  |  | GV_HIERARCHY_PATH_TYPE_START; GV_HIERARCHY_PATH_TYPE_ABSOLUTE; GV_HIERARCHY_PATH_TYPE_RELATIVE
Start Position | GV_HIERARCHY_START_TYPE_ID | LONG |  |  |  | 
Start Distance | GV_HIERARCHY_DISTANCE_ID | LONG | 1 |  |  | 
Reference Path | GV_HIERARCHY_PATH_ID | STRING |  |  |  | 
Start Path | GV_HIERARCHY_START_ID | STRING |  |  |  | 
Iteration Path | GV_HIERARCHY_ITERATION_ID | STRING |  |  |  | 
Exclude | GV_HIERARCHY_EXCLUDE_ID | IN_EXCLUDE |  |  |  | 
Object | GV_HIERARCHY_INPUT_OBJECT | GVGENERALOBJECT |  |  |  | 
Maximum Iterations | GV_HIERARCHY_INPUT_MAX | LONG | 0 |  |  | 
On | GV_HIERARCHY_OPERATOR_ON | BOOL |  |  |  | 
Object | GV_HIERARCHY_OUTPUT_OBJECT | GVGENERALOBJECT |  |  |  | 
Count | GV_HIERARCHY_OUTPUT_COUNT | LONG |  |  |  | 
