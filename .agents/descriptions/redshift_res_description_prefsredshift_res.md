# Description: Redshift

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `Redshift/res/description/prefsredshift.res`
- **Symbol:** `prefsredshift`
- **Category:** Other

Use parameter symbols to access parameters and cycle option symbols for cycle values, never their numeric IDs. Treat Min and Max as constraints and Default as the declared initial value; blank cells mean the resource does not declare that metadata, not that the value is zero. Base Description Parameters lists inherited fields from each base; All Parameters lists the effective parameter set for this description.

## Base Description Parameters

No base descriptions.

## All Parameters

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Redshift Version | PREFS_REDSHIFT_REDSHIFT_VERSION | STATICTEXT |  |  |  | 
Plugin Version | PREFS_REDSHIFT_PLUGIN_VERSION | STATICTEXT |  |  |  | 
No label | PREFS_REDSHIFT_MESSAGE_RESTART | STRING |  |  |  | 
Compute Devices | PREFS_REDSHIFT_HEADER_DEVICES | SEPARATOR |  |  |  | 
Cache | PREFS_REDSHIFT_HEADER_CACHE | SEPARATOR |  |  |  | 
Cache Folder | PREFS_REDSHIFT_CACHE_PATH | STRING |  |  |  | 
... | PRESS_REDSHIFT_BUTTON_CACHE_PATH_BROWSE | BUTTON |  |  |  | 
Texture Cache Max GB (0=Unlimited) | PREFS_REDSHIFT_TEXCACHE_MAX | LONG | 0 |  |  | 
Hybrid Rendering | PREFS_REDSHIFT_HYBRID_RENDERING | BOOL |  |  |  | 
Multi Threading | PREFS_REDSHIFT_MULTITHREADING | BOOL |  |  |  | 
Scene Upgrade Compatibility Warning | PREFS_REDSHIFT_WARN_SCENE_UPGRADE | BOOL |  |  |  | 
Maxon Subscription License (if available) | PREFS_REDSHIFT_MAXON_SUBSCRIPTION_LICENSING | BOOL |  |  |  | 
Node Materials for Presets | PREFS_REDSHIFT_USE_NODE_MATERIALS | BOOL |  |  |  | 
Native Camera for New Scenes | PREFS_REDSHIFT_USE_NATIVE_CAMERA | BOOL |  |  |  | 
Global Attribute Manager for Shader Nodes | PREFS_REDSHIFT_GRAPHEDITOR_GLOBAL_AM | BOOL |  |  |  | 
Adjust RenderView for High DPI Displays | PREFS_REDSHIFT_RENDERVIEW_AUTO_DPI | BOOL |  |  |  | 
Redshift Main Menu | PREFS_REDSHIFT_MENU_VISIBLE | BOOL |  |  |  | 
Material Previews | PREFS_REDSHIFT_MATPREVIEW_MODE | LONG |  |  |  | PREFS_REDSHIFT_MATPREVIEW_MODE_OFF; PREFS_REDSHIFT_MATPREVIEW_MODE_IDLE; PREFS_REDSHIFT_MATPREVIEW_MODE_SUSPEND; PREFS_REDSHIFT_MATPREVIEW_MODE_BACKGROUND
Material Translation (Viewport/Export) | PREFS_REDSHIFT_MATEXCHANGE_MODE | LONG |  |  |  | PREFS_REDSHIFT_MATEXCHANGE_MODE_DRAFT; PREFS_REDSHIFT_MATEXCHANGE_MODE_BAKING
Start Automatically | PREFS_REDSHIFT_IPR_AUTOSTART | BOOL |  |  |  | 
Reset to Defaults | PRESS_REDSHIFT_BUTTON_RESET_ALL | BUTTON |  |  |  | 
