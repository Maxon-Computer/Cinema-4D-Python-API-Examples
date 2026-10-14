# Description: Visual Selector Tag

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/ca/description/vstag.res`
- **Symbol:** `vstag`
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
Name | ID_VS_TAG_NAME | STRING |  |  |  | 
Image File | ID_VS_TAG_IMAGE | TEXTURE |  |  |  | 
Aspect Ratio | ID_VS_TAG_ASPECT | LONG |  |  |  | ID_VS_TAG_ASPECT_11; ID_VS_TAG_ASPECT_43; ID_VS_TAG_ASPECT_34; ID_VS_TAG_ASPECT_169
Base Size | ID_VS_BASE_SIZE | LONG | 150 | 640 |  | 
Lock HotSpots | ID_VS_TAG_LOCK | BOOL |  |  |  | 
Add | ID_VS_TAG_HOTSPOT_ADD | BUTTON |  |  |  | 
Remove | ID_VS_TAG_HOTSPOT_REMOVE | BUTTON |  |  |  | 
Icon | ID_VS_TAG_DYNAMIC_BUTTON | BITMAPBUTTON |  |  |  | 
Link | ID_VS_TAG_DYNAMIC_LINK | LINK |  |  |  | 
Command ID | ID_VS_TAG_DYNAMIC_COMMAND | LONG | 0 |  |  | 
Text | ID_VS_TAG_DYNAMIC_NAME | STRING |  |  |  | 
Action | ID_VS_TAG_DYNAMIC_ACTION | LONG |  |  |  | ID_VS_TAG_ACTION_NONE; ID_VS_TAG_ACTION_MOVE; ID_VS_TAG_ACTION_SCALE; ID_VS_TAG_ACTION_ROTATE; ID_VS_TAG_ACTION_SPECIAL
