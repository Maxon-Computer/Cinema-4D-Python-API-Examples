# Description: Visual Selector

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/ca/description/tcavs.res`
- **Symbol:** `Tcavs`
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
No label | ID_CA_TAG_VS_IMAGE | IMAGE |  |  |  | 
Mode | ID_CA_TAG_VS_MODE | LONG |  |  |  | ID_CA_TAG_VS_MODE_EDIT; ID_CA_TAG_VS_MODE_ANIMATE
No label | ID_CA_TAG_VS_HOTSPOTS | ITEMTREE |  |  |  | 
Add View | ID_CA_TAG_VS_ADD_VIEW | BUTTON |  |  |  | 
Add Hotspot | ID_CA_TAG_VS_ADD_HOTSPOT | BUTTON |  |  |  | 
Remove | ID_CA_TAG_VS_REMOVE | BUTTON |  |  |  | 
Image | ID_CA_TAG_VS_IMAGE_NAME | TEXTURE |  |  |  | 
Zoom | ID_CA_TAG_VS_ZOOM | REAL | 0.0 | 1600 |  | 
Left | ID_CA_TAG_VS_LEFT | LONG | 0 |  |  | 
Top | ID_CA_TAG_VS_TOP | LONG | 0 |  |  | 
Right | ID_CA_TAG_VS_RIGHT | LONG | 0 |  |  | 
Bottom | ID_CA_TAG_VS_BOTTOM | LONG | 0 |  |  | 
Color | ID_CA_TAG_VS_COL | COLOR |  |  |  | 
Transparency | ID_CA_TAG_VS_TRANS | REAL | 0.0 | 100.0 |  | 
Highlight | ID_CA_TAG_VS_HIGHLIGHT_COL | COLOR |  |  |  | 
Transparency | ID_CA_TAG_VS_HIGHLIGHT_TRANS | REAL | 0.0 | 100.0 |  | 
Selected | ID_CA_TAG_VS_SELECT_COL | COLOR |  |  |  | 
Transparency | ID_CA_TAG_VS_SELECT_TRANS | REAL | 0.0 | 100.0 |  | 
Link | ID_CA_TAG_VS_LINK | LINK |  |  |  | 
Action | ID_CA_TAG_VS_ACTION | LONG |  |  |  | ID_CA_TAG_VS_ACTION_NONE; ID_CA_TAG_VS_ACTION_MOVE; ID_CA_TAG_VS_ACTION_SCALE; ID_CA_TAG_VS_ACTION_ROTATE; ID_CA_TAG_VS_ACTION_COMMAND; ID_CA_TAG_VS_ACTION_VIEW; ID_CA_TAG_VS_ACTION_SCRIPT
Command | ID_CA_TAG_VS_COMMAND | STRING |  |  |  | 
Script | ID_CA_TAG_VS_PYTHON | STRING |  |  |  | 
Views | ID_CA_TAG_VS_VIEW | LONG |  |  |  | 
Brush | ID_CA_TAG_VS_BRUSH | LONG | 1 |  |  | 
Lasso | ID_CA_TAG_VS_LASSO | LONG |  |  |  | ID_CA_TAG_VS_LASSO_FREE; ID_CA_TAG_VS_LASSO_POLY; ID_CA_TAG_VS_LASSO_RECT
Shape | ID_CA_TAG_VS_SHAPE | LONG |  |  |  | ID_CA_TAG_VS_SHAPE_RECT; ID_CA_TAG_VS_SHAPE_ELLIPSE
