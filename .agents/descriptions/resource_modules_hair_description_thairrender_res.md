# Description: Render

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/hair/description/thairrender.res`
- **Symbol:** `Thairrender`
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
Enable | HAIR_RENDER_TAG_ENABLE | BOOL |  |  |  | 
Auto Time | HAIR_RENDER_TAG_AUTOTIME | BOOL |  |  |  | 
Start | HAIR_RENDER_TAG_START | BASETIME |  |  |  | 
Stop | HAIR_RENDER_TAG_STOP | BASETIME |  |  |  | 
Mode | HAIR_RENDER_TAG_MODE | LONG |  |  |  | HAIR_RENDER_TAG_MODE_POINTS; HAIR_RENDER_TAG_MODE_SURFACE; HAIR_RENDER_TAG_MODE_LINE; HAIR_RENDER_TAG_MODE_INTERPOLATED; HAIR_RENDER_TAG_MODE_POSITION; HAIR_RENDER_TAG_MODE_VELOCITY; HAIR_RENDER_TAG_MODE_TRAIL
As Fill Hairs | HAIR_RENDER_TAG_HAIRS | BOOL |  |  |  | 
Length | HAIR_RENDER_TAG_LENGTH | REAL | 0.0 |  |  | 
Scale | HAIR_RENDER_TAG_SCALE | REAL | 0.0 | 1000.0 |  | 
Count | HAIR_RENDER_TAG_COUNT | LONG | 1 |  |  | 
Segments | HAIR_RENDER_TAG_SEGMENTS | LONG | 1 | 8192 |  | 
Restrict | HAIR_RENDER_TAG_RESTRICT | LINK |  |  |  | 
Limit | HAIR_RENDER_TAG_TRAIL_LIMIT | BOOL |  |  |  | 
Trail | HAIR_RENDER_TAG_TRAIL | BASETIME | 0 |  |  | 
On Death | HAIR_RENDER_TAG_DEATH | LONG |  |  | 1 | HAIR_RENDER_TAG_REMAIN; HAIR_RENDER_TAG_REMOVE; HAIR_RENDER_TAG_RUNOUT
