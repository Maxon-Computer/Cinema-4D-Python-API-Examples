# Description: Interaction Tag

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/c4d_objects/description/tinteraction.res`
- **Symbol:** `Tinteraction`
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
Enabled | INTERACTIONTAG_ENABLE | BOOL |  |  |  | 
Tweakable | INTERACTIONTAG_TWEAKABLE | BOOL |  |  |  | 
Disable Viewport Selection | INTERACTIONTAG_SELECT | BOOL |  |  |  | 
When Selected | INTERACTIONTAG_SELECTEDTWEAKMODE | LONG |  |  |  | INTERACTIONTAG_SELECTEDTWEAKMODE_INVOKE; INTERACTIONTAG_SELECTEDTWEAKMODE_DISABLE; INTERACTIONTAG_SELECTEDTWEAKMODE_ALWAYS
Disable Transforms | INTERACTIONTAG_DISABLEMOVE | BOOL |  |  |  | 
Display | INTERACTIONTAG_GROUP_DISPLAY | SEPARATOR |  |  |  | 
Highlight Object | INTERACTIONTAG_HIGHLIGHT | BOOL |  |  |  | 
Hide Mouse On Drag | INTERACTIONTAG_HIDE_MOUSE | BOOL |  |  |  | 
Hide Object | INTERACTIONTAG_HIDE_OBJECT | BOOL |  |  |  | 
Scripting Language | INTERACTIONTAG_SCRIPT_LANGUAGE | LONG |  |  |  | INTERACTIONTAG_SCRIPT_LANGUAGE_NONE; INTERACTIONTAG_SCRIPT_LANGUAGE_PYTHON; INTERACTIONTAG_SCRIPT_LANGUAGE_COFFEE
Script | INTERACTIONTAG_SCRIPT_PY | STRING |  |  |  | 
Script | INTERACTIONTAG_SCRIPT_COF | STRING |  |  |  | 
Edit Script | INTERACTIONTAG_EDIT_SCRIPT | BUTTON |  |  |  | 
Use Right Mouse Button | INTERACTIONTAG_USERIGHTMOUSE | BOOL |  |  |  | 
Object Is Selected | INTERACTIONTAG_OBJECT_SELECTED | BOOL |  |  |  | 
Object Is Highlighted | INTERACTIONTAG_OBJECT_HIGHLIGHTED | BOOL |  |  |  | 
Object Is Being Tweaked | INTERACTIONTAG_OBJECT_TWEAKED | BOOL |  |  |  | 
Mouse Button | INTERACTIONTAG_MOUSE_BUTTON | LONG |  |  |  | INTERACTIONTAG_MOUSE_BUTTON_UP; INTERACTIONTAG_MOUSE_BUTTON_LEFT; INTERACTIONTAG_MOUSE_BUTTON_RIGHT
X Mouse | INTERACTIONTAG_XMOUSE | LONG |  |  |  | 
Y Mouse | INTERACTIONTAG_YMOUSE | LONG |  |  |  | 
Pen Pressure | INTERACTIONTAG_MOUSE_PRESSURE | REAL | 0 |  |  | 
Pen Tilt | INTERACTIONTAG_MOUSE_TILT | REAL | 0 |  |  | 
Pen Angle | INTERACTIONTAG_MOUSE_ANGLE | REAL |  |  |  | 
Mouse Wheel | INTERACTIONTAG_MOUSE_WHEEL | REAL |  |  |  | 
X Pixels | INTERACTIONTAG_XPIXELS | LONG |  |  |  | 
Y Pixels | INTERACTIONTAG_YPIXELS | LONG |  |  |  | 
Mouse Travel | INTERACTIONTAG_MOUSE_TRAVEL | REAL |  |  |  | 
Object Delta | INTERACTIONTAG_WORLD_DELTA | VECTOR |  |  |  | 
Calculate Polygon Info | INTERACTIONTAG_USEPOLYINFO | BOOL |  |  |  | 
Live Update During Drag | INTERACTIONTAG_LIVEPOLYINFO | BOOL |  |  |  | 
Hit | INTERACTIONTAG_POLYINFO_HIT | BOOL |  |  |  | 
Hit Point | INTERACTIONTAG_POLYINFO_HITPOINT | VECTOR |  |  |  | 
Polygon Index | INTERACTIONTAG_POLYINFO_POLYGON | LONG |  | 1000000000 |  | 
Edge Index | INTERACTIONTAG_POLYINFO_EDGE | LONG |  | 1000000000 |  | 
Point Index | INTERACTIONTAG_POLYINFO_POINT | LONG |  | 1000000000 |  | 
Selection Tag | INTERACTIONTAG_POLYINFO_SELECTIONTAG | LINK |  |  |  | 
Selection Tag Index | INTERACTIONTAG_POLYINFO_SELECTIONTAGINDEX | LONG |  |  |  | 
Proxy Object | INTERACTIONTAG_PROXY_OBJECT | LINK |  |  |  | 
Highlight Proxy Object | INTERACTIONTAG_HIGHLIGHT_PROXY | BOOL |  |  |  | 
Select Proxy | INTERACTIONTAG_SELECT_PROXY | BOOL |  |  |  | 
Transform Proxy | INTERACTIONTAG_TWEAK_PROXY | BOOL |  |  |  | 
Dynamic Proxies | INTERACTIONTAG_GROUP_DYNAMICPROXY | SEPARATOR |  |  |  | 
Dynamic Proxies | INTERACTIONTAG_POLYINFO_USETAGPROXY | BOOL |  |  |  | 
Tag Proxy | INTERACTIONTAG_POLYINFO_TAGPROXY | LINK |  |  |  | 
