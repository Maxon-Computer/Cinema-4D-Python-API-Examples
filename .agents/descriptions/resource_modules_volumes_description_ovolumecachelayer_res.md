# Description: Cache

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/volumes/description/ovolumecachelayer.res`
- **Symbol:** `Ovolumecachelayer`
- **Category:** Other

Use parameter symbols to access parameters and cycle option symbols for cycle values, never their numeric IDs. Treat Min and Max as constraints and Default as the declared initial value; blank cells mean the resource does not declare that metadata, not that the value is zero. Base Description Parameters lists inherited fields from each base; All Parameters lists the effective parameter set for this description.

## Base Description Parameters

No base descriptions.

## All Parameters

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Cache Location | ID_VOLUMECACHELAYER_CACHE_MODE | LONG |  |  |  | ID_VOLUMECACHELAYER_CACHE_MODE_EXTERNAL; ID_VOLUMECACHELAYER_CACHE_MODE_INTERNAL
Path | ID_VOLUMECACHELAYER_FILEPATH | FILENAME |  |  |  | 
Animation | ID_VOLUMECACHELAYER_ANIMATION | BOOL |  |  |  | 
From | ID_VOLUMECACHELAYER_FROM | LONG |  |  |  | 
To | ID_VOLUMECACHELAYER_TO | LONG |  |  |  | 
Cache | ID_VOLUMECACHELAYER_BUTTON_CACHE | BUTTON |  |  |  | 
Refresh | ID_VOLUMECACHELAYER_BUTTON_REFRESH | BUTTON |  |  |  | 
Clear | ID_VOLUMECACHELAYER_BUTTON_CLEAR | BUTTON |  |  |  | 
Move Cache to Internal | ID_VOLUMECACHELAYER_CONVERT_TO_INTERNAL | BUTTON |  |  |  | 
Move Cache to External | ID_VOLUMECACHELAYER_CONVERT_TO_EXTERNAL | BUTTON |  |  |  | 
No label | ID_VOLUMECACHELAYER_STATS_TYPE | STATICTEXT |  |  |  | 
No label | ID_VOLUMECACHELAYER_STATS_SIZE | STATICTEXT |  |  |  | 
