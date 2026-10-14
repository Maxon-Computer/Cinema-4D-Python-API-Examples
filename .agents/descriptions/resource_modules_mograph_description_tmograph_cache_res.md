# Description: MoGraph Cache

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/mograph/description/tmograph_cache.res`
- **Symbol:** `Tmograph_cache`
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
Range | MGCACHETAG_BAKESEQUENCE_ACTIVE | BOOL |  |  |  | 
From | MGCACHETAG_BAKEFROM | BASETIME |  |  |  | 
To | MGCACHETAG_BAKETO | BASETIME |  |  |  | 
Bake | MGCACHETAG_BAKESEQUENCE | BUTTON |  |  |  | 
Bake Frame | MGCACHETAG_BAKEFRAME | BUTTON |  |  |  | 
Clear Cache | MGCACHETAG_CLEARCACHE | BUTTON |  |  |  | 
Clear Frame | MGCACHETAG_CLEARFRAME | BUTTON |  |  |  | 
Filename | MGCACHETAG_EXPORT_CACHEFILE | FILENAME |  |  |  | 
-&gt; | MGCACHETAG_EXPORT_TOKENS | POPUP |  |  |  | 
Bake to file | MGCACHETAG_BAKETOEXTERNAL | BUTTON |  |  |  | 
Export Cache to File | MGCACHETAG_CACHE_EXPORT | BUTTON |  |  |  | 
Memory Used :  | MGCACHETAG_MEMORYUSED | STATICTEXT |  |  |  | 
External Cache File | MGCACHETAG_ACTIVE_CACHEFILE | FILENAME |  |  |  | 
Cache File Is Sequence | MGCACHETAG_CACHE_ISSEQUENCE | BOOL |  |  |  | 
Loop Start Frame | MGCACHETAG_LOOPSTART | LONG | 0 |  |  | 
Loop End Frame | MGCACHETAG_LOOPEND | LONG | 0 |  |  | 
Enable | MGCACHETAG_ACTIVE | BOOL |  |  |  | 
Strength | MGCACHETAG_STRENGTH | REAL | 0.0 | 100.0 |  | 
Cache Type | MGCACHETAG_MODE | LONG |  |  |  | MGCACHETAG_MODE_INTERNAL; MGCACHETAG_MODE_EXTERNAL
Filename | MGCACHETAG_IMPORT_CACHEFILE | FILENAME |  |  |  | 
No label | MGCACHETAG_IMPORT_TOKENS | POPUP |  |  |  | 
Load Cache From File | MGCACHETAG_CACHE_IMPORT | BUTTON |  |  |  | 
Offset | MGCACHETAG_OFFSET | BASETIME |  |  |  | 
Loop | MGCACHETAG_LOOP | BOOL |  |  |  | 
Loop Blending | MGCACHETAG_LOOP_BLEND | REAL | 0.0 | 100.0 |  | 
