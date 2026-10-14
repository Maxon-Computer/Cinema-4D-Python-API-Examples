# Description: Sun Expression

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/sky/description/tsunexpression.res`
- **Symbol:** `Tsunexpression`
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
Time | SUNEXPRESSIONTAG_DATETIME | DATETIME |  |  |  | 
Current Time | SUNEXPRESSIONTAG_TIME_NOW | BOOL |  |  |  | 
Today | SUNEXPRESSIONTAG_DATE_TODAY | BOOL |  |  |  | 
Animate Date | SUNEXPRESSIONTAG_INTERPOLATE_DATE | BOOL |  |  |  | 
Animate Time | SUNEXPRESSIONTAG_INTERPOLATE_TIME | BOOL |  |  |  | 
City | SUNEXPRESSIONTAG_POS_CITY_COMBO | LONG |  |  |  | 
Latitude | SUNEXPRESSIONTAG_LATITUDE | REAL | -90 | 90 |  | 
Longitude | SUNEXPRESSIONTAG_LONGITUDE | REAL | -180 | 180 |  | 
Time Zone | SUNEXPRESSIONTAG_POS_TIMEZONE | LONG |  |  |  | SUNEXPRESSIONTAG_POS_TZ_OS; SUNEXPRESSIONTAG_POS_TZ_CUSTOM
Daylight Saving | SUNEXPRESSIONTAG_POS_DST_SETTINGS | LONG |  |  |  | SUNEXPRESSIONTAG_POS_DST_OFF; SUNEXPRESSIONTAG_POS_DST_LAST_MARCH_LAST_OCT; SUNEXPRESSIONTAG_POS_DST_SECOND_MARCH_FIRST_NOV; SUNEXPRESSIONTAG_POS_DST_FIRST_APR_LAST_OCT; SUNEXPRESSIONTAG_POS_DST_FIRST_OCT_LAST_MARCH; SUNEXPRESSIONTAG_POS_DST_LAST_OCT_LAST_MARCH
Time Zone Diff. | SUNEXPRESSIONTAG_POS_TIME_ZONE | REAL |  |  |  | 
DS Time Zone | SUNEXPRESSIONTAG_POS_DST_TIME_ZONE | REAL |  |  |  | 
Distance | SUNEXPRESSIONTAG_DISTANCE | REAL | 0.0 |  |  | 
Set Light Color | SUNEXPRESSIONTAG_SETLIGHTCOLOR | BOOL |  |  |  | 
