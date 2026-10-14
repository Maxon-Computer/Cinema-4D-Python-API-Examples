# Description: IK-Spline

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/ca/description/tcaikspline.res`
- **Symbol:** `Tcaikspline`
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
Strength | ID_CA_IKSPLINE_TAG_STRENGTH | REAL | 0.0 | 100.0 |  | 
Type | ID_CA_IKSPLINE_TAG_TYPE | LONG |  |  |  | ID_CA_IKSPLINE_TAG_TYPE_NONE; ID_CA_IKSPLINE_TAG_TYPE_FIT; ID_CA_IKSPLINE_TAG_TYPE_EQUAL; ID_CA_IKSPLINE_TAG_TYPE_REL
Aim | ID_CA_IKSPLINE_TAG_AIM | LONG |  |  |  | ID_CA_IKSPLINE_TAG_AIM_TANGENT; ID_CA_IKSPLINE_TAG_AIM_JOINT
Align | ID_CA_IKSPLINE_TAG_ALIGN_TANGENT | LONG |  |  |  | ID_CA_IKSPLINE_TAG_ALIGN_X; ID_CA_IKSPLINE_TAG_ALIGN_Y; ID_CA_IKSPLINE_TAG_ALIGN_Z
Axis | ID_CA_IKSPLINE_TAG_ALIGN_AXIS | LONG |  |  |  | ID_CA_IKSPLINE_TAG_ALIGN_X; ID_CA_IKSPLINE_TAG_ALIGN_Y; ID_CA_IKSPLINE_TAG_ALIGN_Z
Spline | ID_CA_IKSPLINE_TAG_SPLINE | LINK |  |  |  | 
End | ID_CA_IKSPLINE_TAG_END | LINK |  |  |  | 
Twist | ID_CA_IKSPLINE_TAG_TWIST_TYPE | LONG |  |  |  | ID_CA_IKSPLINE_TAG_TWIST_TYPE_NONE; ID_CA_IKSPLINE_TAG_TWIST_TYPE_WORLD; ID_CA_IKSPLINE_TAG_TWIST_TYPE_LOCAL
Angle | ID_CA_IKSPLINE_TAG_TWIST_AXIS | LONG |  |  |  | ID_CA_IKSPLINE_TAG_TWIST_AXIS_H; ID_CA_IKSPLINE_TAG_TWIST_AXIS_P; ID_CA_IKSPLINE_TAG_TWIST_AXIS_B
Twist | ID_CA_IKSPLINE_TAG_TWIST_CURVE | SPLINE |  |  |  | 
Add | ID_CA_IKSPLINE_HANDLE_ADD | BUTTON |  |  |  | 
Create | ID_CA_IKSPLINE_HANDLE_CREATE | BUTTON |  |  |  | 
Remove | ID_CA_IKSPLINE_HANDLE_REMOVE | BUTTON |  |  |  | 
Index | ID_CA_IKSPLINE_HANDLE_INDEX | LONG | 0 |  |  | 
Object | ID_CA_IKSPLINE_HANDLE_LINK | LINK |  |  |  | 
Twist | ID_CA_IKSPLINE_HANDLE_TWIST | BOOL |  |  |  | 
Depth | ID_CA_IKSPLINE_HANDLE_LENGTH | REAL | 0.0 |  |  | 
Offset | ID_CA_IKSPLINE_HANDLE_OFFSET | BOOL |  |  |  | 
Display | ID_CA_IKSPLINE_DISPLAY_MODE | LONG |  |  |  | ID_CA_IKSPLINE_DISPLAY_MODE_OFF; ID_CA_IKSPLINE_DISPLAY_MODE_ACTIVE; ID_CA_IKSPLINE_DISPLAY_MODE_OBJECT; ID_CA_IKSPLINE_DISPLAY_MODE_ALWAYS
Tangent | ID_CA_IKSPLINE_DISPLAY_TANGENT | BOOL |  |  |  | 
Tangent | ID_CA_IKSPLINE_DISPLAY_TANGENT_COL | COLOR |  |  |  | 
