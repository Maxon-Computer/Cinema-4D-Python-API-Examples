# Description: Point Cache

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/ca/description/tcageomcache.res`
- **Symbol:** `Tcageomcache`
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
Enable | ID_CA_GEOMCACHE_TAG_ENABLE | BOOL |  |  |  | 
Use Deformer | ID_CA_GEOMCACHE_TAG_DEFORMER | BOOL |  |  |  | 
Transform | ID_CA_GEOMCACHE_TAG_PSR | BOOL |  |  |  | 
Strength | ID_CA_GEOMCACHE_TAG_CACHE_STRENGTH | REAL | 0.0 | 100.0 |  | 
Compress | ID_CA_GEOMCACHE_TAG_COMPRESSED | BOOL |  |  |  | 
Memory:  | ID_CA_GEOMCACHE_TAG_INFO2 | STATICTEXT |  |  |  | 
Store State | ID_CA_GEOMCACHE_TAG_STORE | BUTTON |  |  |  | 
Restore | ID_CA_GEOMCACHE_TAG_RESTORE | BUTTON |  |  |  | 
Calculate | ID_CA_GEOMCACHE_TAG_CALCULATE | BUTTON |  |  |  | 
Update | ID_CA_GEOMCACHE_TAG_UPDATE | BUTTON |  |  |  | 
Empty Cache | ID_CA_GEOMCACHE_TAG_DELETE | BUTTON |  |  |  | 
Load... | ID_CA_GEOMCACHE_TAG_CACHE_LOAD | BUTTON |  |  |  | 
Save... | ID_CA_GEOMCACHE_TAG_CACHE_SAVE | BUTTON |  |  |  | 
Auto Time | ID_CA_GEOMCACHE_TAG_CACHE_AUTOTIME | BOOL |  |  |  | 
Start | ID_CA_GEOMCACHE_TAG_CACHE_START | BASETIME |  |  |  | 
Stop | ID_CA_GEOMCACHE_TAG_CACHE_STOP | BASETIME |  |  |  | 
Offset | ID_CA_GEOMCACHE_TAG_CACHE_OFFSET | BASETIME |  |  |  | 
Scale | ID_CA_GEOMCACHE_TAG_CACHE_TIMESCALE | REAL |  |  |  | 
Loop | ID_CA_GEOMCACHE_TAG_CACHE_LOOP | LONG | 1 |  |  | 
Blend | ID_CA_GEOMCACHE_TAG_CACHE_LOOP_BLEND | REAL | 0.0 | 100.0 |  | 
Cache | ID_CA_GEOMCACHE_TAG_CACHE_LIMIT | LONG | 1 | 1000 |  | 
Maximum Undo Limit (MB) | ID_CA_GEOMCACHE_TAG_TEXT_LIMIT | STATICTEXT |  |  |  | 
