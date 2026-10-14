# Description: Display Tag

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/c4d_base/description/tdisplay.res`
- **Symbol:** `Tdisplay`
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
Use Shading Mode | DISPLAYTAG_AFFECT_DISPLAYMODE | BOOL |  |  |  | 
Shading Mode | DISPLAYTAG_SDISPLAYMODE | LONG |  |  |  | DISPLAYTAG_SDISPLAY_GOURAUD; DISPLAYTAG_SDISPLAY_GOURAUD_WIRE; DISPLAYTAG_SDISPLAY_QUICK; DISPLAYTAG_SDISPLAY_QUICK_WIRE; DISPLAYTAG_SDISPLAY_FLAT; DISPLAYTAG_SDISPLAY_FLAT_WIRE; DISPLAYTAG_SDISPLAY_HIDDENLINE; DISPLAYTAG_SDISPLAY_NOSHADING
Style | DISPLAYTAG_WDISPLAYMODE | LONG |  |  |  | DISPLAYTAG_WDISPLAY_WIREFRAME; DISPLAYTAG_WDISPLAY_ISOPARMS; DISPLAYTAG_WDISPLAY_BOX; DISPLAYTAG_WDISPLAY_SKELETON
Volume Vector | DISPLAYTAG_VDISPLAYMODE | LONG |  |  |  | DISPLAYTAG_VDISPLAY_DIRECTION; DISPLAYTAG_VDISPLAY_LENGTH
Use Level of Detail | DISPLAYTAG_AFFECT_LEVELOFDETAIL | BOOL |  |  |  | 
Level of Detail | DISPLAYTAG_LEVELOFDETAIL | REAL | 0.0 | 1000 |  | 
Use Visiblity | DISPLAYTAG_AFFECT_VISIBILITY | BOOL |  |  |  | 
Visibility | DISPLAYTAG_VISIBILITY | REAL | 0.0 | 100.0 |  | 
Use Backface Culling | DISPLAYTAG_AFFECT_BACKFACECULLING | BOOL |  |  |  | 
Backface Culling | DISPLAYTAG_BACKFACECULLING | BOOL |  |  |  | 
Use Materials | DISPLAYTAG_AFFECT_TEXTURES | BOOL |  |  |  | 
Materials | DISPLAYTAG_TEXTURES | BOOL |  |  |  | 
Use Reflections | DISPLAYTAG_AFFECT_REFLECTIONS | BOOL |  |  |  | 
Reflections | DISPLAYTAG_REFLECTIONS | BOOL |  |  |  | 
Use Tessellation | DISPLAYTAG_AFFECT_TESSELLATION | BOOL |  |  |  | 
Tessellation | DISPLAYTAG_TESSELLATION | BOOL |  |  |  | 
Enable | ONION_USE | BOOL |  |  |  | 
Draw Mode | ONION_MODE | LONG |  |  |  | ONION_MODE_OBJECT; ONION_MODE_POINT; ONION_MODE_AXIS; ONION_MODE_TRAIL; ONION_MODE_MTRAIL; ONION_MODE_VELOCITY
Scale | ONION_SCALE | REAL | 0 |  |  | 
Size | ONION_PSIZE | LONG | 0 | 10 |  | 
Shading Mode | ONION_DISPLAYMODE | LONG |  |  |  | ONION_DISPLAY_GOURAUD; ONION_DISPLAY_GOURAUD_WIRE; ONION_DISPLAY_QUICK; ONION_DISPLAY_QUICK_WIRE; ONION_DISPLAY_FLAT; ONION_DISPLAY_FLAT_WIRE; ONION_DISPLAY_NOSHADING
XRay | ONION_XRAY | BOOL |  |  |  | 
Frames Before | ONION_FRAMES_BEFORE | LONG | 0 |  |  | 
Frames Before Color | ONION_COL_FRAMES_BEFORE | COLOR |  |  |  | 
Frames After | ONION_FRAMES_AFTER | LONG | 0 |  |  | 
Frames After Color | ONION_COL_FRAMES_AFTER | COLOR |  |  |  | 
Frames Step | ONION_FRAMES_STEP | LONG | 1 |  |  | 
Use Range | ONION_ONLY_RANGE | BOOL |  |  |  | 
Start | ONION_FROM | BASETIME |  |  |  | 
End | ONION_TO | BASETIME |  |  |  | 
Use Keys | ONION_USE_KEYS | BOOL |  |  |  | 
Keys Before | ONION_KEYS_BEFORE | LONG | 0 |  |  | 
Keys Before Color | ONION_COL_KEYS_BEFORE | COLOR |  |  |  | 
Keys After | ONION_KEYS_AFTER | LONG | 0 |  |  | 
Keys After Color | ONION_COL_KEYS_AFTER | COLOR |  |  |  | 
Use Custom | ONION_USE_CUSTOM | BOOL |  |  |  | 
Custom Frames | ONION_CUSTOM | STRING |  |  |  | 
Custom Color | ONION_COL_CUSTOM | COLOR |  |  |  | 
Use Cache | ONION_CACHE | BOOL |  |  |  | 
Cached:  | ONION_CACHE_INFO1 | STATICTEXT |  |  |  | 
Calculate Cache | ONION_CALCULATE | BUTTON |  |  |  | 
Empty Cache | ONION_DELCACHE | BUTTON |  |  |  | 
