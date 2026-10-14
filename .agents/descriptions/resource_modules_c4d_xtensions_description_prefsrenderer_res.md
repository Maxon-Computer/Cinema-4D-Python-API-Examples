# Description: Renderer

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/c4d_xtensions/description/prefsrenderer.res`
- **Symbol:** `PrefsRenderer`
- **Category:** Other

Use parameter symbols to access parameters and cycle option symbols for cycle values, never their numeric IDs. Treat Min and Max as constraints and Default as the declared initial value; blank cells mean the resource does not declare that metadata, not that the value is zero. Base Description Parameters lists inherited fields from each base; All Parameters lists the effective parameter set for this description.

## Base Description Parameters

No base descriptions.

## All Parameters

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Custom Number of Render Threads | PREF_RENDERER_THREADCUSTOM | BOOL |  |  |  | 
No label | PREF_RENDERER_THREADNUMBER | LONG | 1 | 256 |  | 
Adapt Thread Priority | PREF_RENDERER_THREADPRIORITY | BOOL |  |  |  | 
Lower Process Priority | PREF_RENDERER_LOWERPROCESSPRIORITY | BOOL |  |  |  | 
Renderer Log File | PREF_RENDERER_CREATELOG | BOOL |  |  |  | 
Global Illumination Info in Console | PREF_RENDERER_GLOBALILLUM | BOOL |  |  |  | 
Render Queue Log | PREF_RENDERER_RENDERQUEUELOG | BOOL |  |  |  | 
Auto Renaming | PREF_RENDERER_RENDERQUEUE_AUTORENAME | BOOL |  |  |  | 
