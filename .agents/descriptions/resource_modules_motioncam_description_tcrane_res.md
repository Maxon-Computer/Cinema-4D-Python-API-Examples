# Description: Camera Crane

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/motioncam/description/tcrane.res`
- **Symbol:** `tcrane`
- **Category:** Tags

Use parameter symbols to access parameters and cycle option symbols for cycle values, never their numeric IDs. Treat Min and Max as constraints and Default as the declared initial value; blank cells mean the resource does not declare that metadata, not that the value is zero. Base Description Parameters lists inherited fields from each base; All Parameters lists the effective parameter set for this description.

## Base Description Parameters

### Expression (`Texpression`)

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Priority | EXPRESSION_PRIORITY | PRIORITY |  |  |  | 
Enable | EXPRESSION_ENABLE | BOOL |  |  |  | 

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
Priority | EXPRESSION_PRIORITY | PRIORITY |  |  |  | 
Enable | EXPRESSION_ENABLE | BOOL |  |  |  | 
Enabled | TCRANE_VISUALIZATION_ENABLED | BOOL |  |  |  | 
Color | TCRANE_VISUALIZATION_COLOR | COLOR |  |  |  | 
Target Color | TCRANE_VISUALIZATION_COLOR_T | COLOR |  |  |  | 
Base | TCRANE_BASE | SEPARATOR |  |  |  | 
Link | TCRANE_BASE_LINK | LINK |  |  |  | 
Rail Spline | TCRANE_BASE_LINK_RAIL | LINK |  |  |  | 
Base Pos | TCRANE_BASE_LINK_POS | REAL | 0.0 | 100.0 |  | 
Tangential | TCRANE_BASE_LINK_TANGENTIAL | BOOL |  |  |  | 
Base Heading | TCRANE_BASE_HEADING | REAL |  |  |  | 
Base Height | TCRANE_BASE_HEIGHT | REAL | 0.0 |  |  | 
Arm | TCRANE_ARM | SEPARATOR |  |  |  | 
Arm Length | TCRANE_ARM_LENGTH | REAL | 0.0 |  |  | 
Arm Pitch | TCRANE_ARM_PITCH | REAL |  |  |  | 
Arm Target | TCRANE_ARM_TARGETLINK | LINK |  |  |  | 
Head | TCRANE_HEAD | SEPARATOR |  |  |  | 
Head Height | TCRANE_HEAD_A_HEIGHT | REAL |  |  |  | 
Head Heading | TCRANE_HEAD_A_HEADING | REAL |  |  |  | 
Head Width | TCRANE_HEAD_B_LENGTH | REAL |  |  |  | 
Head Target | TCRANE_HEAD_TARGETLINK | LINK |  |  |  | 
Camera | TCRANE_CAM | SEPARATOR |  |  |  | 
Camera Pitch | TCRANE_CAM_PITCH | REAL |  |  |  | 
Camera Banking | TCRANE_CAM_BANKING | REAL |  |  |  | 
Camera Offset | TCRANE_CAM_PARALLAX | REAL |  |  |  | 
Compensate Pitch | TCRANE_CAM_COMPENSATE_PITCH | BOOL |  |  |  | 
Compensate Heading | TCRANE_CAM_COMPENSATE_HEADING | BOOL |  |  |  | 
