# Description: Connector

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/c4d_simulation/description/tpbdconstraint.res`
- **Symbol:** `tpbdconstraint`
- **Category:** Tags

Use parameter symbols to access parameters and cycle option symbols for cycle values, never their numeric IDs. Treat Min and Max as constraints and Default as the declared initial value; blank cells mean the resource does not declare that metadata, not that the value is zero. Base Description Parameters lists inherited fields from each base; All Parameters lists the effective parameter set for this description.

## Base Description Parameters

### Base Tag (`Tbase`)

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Expose on Object | ID_EXPOSETAB | BOOL |  |  |  | 

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
Expose on Object | ID_EXPOSETAB | BOOL |  |  |  | 
Always Draw | PBD_CONSTRAINT_TAG_ALWAYSDRAW | BOOL |  |  |  | 
Search Radius | PBD_CONSTRAINT_TAG_RADIUS | REAL |  |  |  | 
Max Connections | PBD_CONSTRAINT_TAG_MAXCONNECTIONS | LONG | 1 |  |  | 
Point Restriction | PBD_CONSTRAINT_TAG_POINTSELECTION | STRING |  |  |  | 
Same Object | PBD_CONSTRAINT_TAG_SAME_OBJECT | BOOL |  |  |  | 
Other Objects | PBD_CONSTRAINT_TAG_OTHER_OBJECTS | BOOL |  |  |  | 
Mode | PBD_CONSTRAINT_TAG_EXCLUSION_MODE | LONG |  |  |  | PBD_CONSTRAINT_TAG_EXCLUSION_MODE_EXCLUDE; PBD_CONSTRAINT_TAG_EXCLUSION_MODE_INCLUDE
Tags | PBD_CONSTRAINT_TAG_EXCLUDE_OBJECTS | IN_EXCLUDE |  |  |  | 
Update Live | PBD_CONSTRAINT_TAG_GENERATE_LIVE | BOOL |  |  |  | 
Create | PBD_CONSTRAINT_TAG_CREATE | BUTTON |  |  |  | 
Clear | PBD_CONSTRAINT_TAG_CLEAR | BUTTON |  |  |  | 
Stretchiness | PBD_CONSTRAINT_TAG_STRETCHINESS | REAL | 0.0 |  |  | 
Target Length | PBD_CONSTRAINT_TAG_TARGETLENGTH | REAL | 0.0 |  |  | 
Tearing | PBD_CONSTRAINT_TAG_TEAR | BOOL |  |  |  | 
Mode | PBD_CONSTRAINT_TAG_TEAR_MODE | LONG |  |  |  | PBD_CONSTRAINT_TAG_TEAR_MODE_RELATIVE; PBD_CONSTRAINT_TAG_TEAR_MODE_ABSOLUTE
Tear Distance | PBD_CONSTRAINT_TAG_TEAR_ABSOLUTE_DISTANCE | REAL | 0.0 |  |  | 
Tear Past | PBD_CONSTRAINT_TAG_TEARPAST | REAL | 100.0 |  |  | 
