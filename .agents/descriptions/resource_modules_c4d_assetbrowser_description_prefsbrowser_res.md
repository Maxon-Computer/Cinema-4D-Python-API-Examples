# Description: Asset Browser

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/c4d_assetbrowser/description/prefsbrowser.res`
- **Symbol:** `Prefsbrowser`
- **Category:** Other

Use parameter symbols to access parameters and cycle option symbols for cycle values, never their numeric IDs. Treat Min and Max as constraints and Default as the declared initial value; blank cells mean the resource does not declare that metadata, not that the value is zero. Base Description Parameters lists inherited fields from each base; All Parameters lists the effective parameter set for this description.

## Base Description Parameters

No base descriptions.

## All Parameters

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Download Location | PREF_BROWSER_DOWNLOAD_LOCATION | FILENAME |  |  |  | 
Clear Downloaded | PREF_BROWSER_CLEAR_DOWNLOADED | BUTTON |  |  |  | 
No label | PREF_BROWSER_DOWNLOADED_SIZE | STATICTEXT |  |  |  | 
&#92;u27F3 | PREF_BROWSER_RECALCULATE_SIZE | BUTTON |  |  |  | 
Show Unavailable | PREF_BROWSER_SHOW_UNAVAILABLE | BOOL |  |  |  | 
Preview Width | PREF_BROWSER_PREVIEWWIDTH | LONG | 128 | 1024 |  | 
Preview Height | PREF_BROWSER_PREVIEWHEIGHT | LONG | 128 | 1024 |  | 
Tree Navigation Open by Default | PREF_BROWSER_TREENAV_OPEN_DEFAULT | BOOL |  |  |  | 
Watch Folders | PREF_BROWSER_WATCHFOLDER_SEPARATOR | SEPARATOR |  |  |  | 
Projects as Watch Folders | PREF_BROWSER_WATCHFOLDER_AUTOMOUNT_DOCUMENTS | BOOL |  |  |  | 
Enable automatic preview generation | PREF_BROWSER_WATCHFOLDERS_AUTORUN | BOOL |  |  |  | 
Enable preview generation for all 3d formats | PREF_BROWSER_WATCHFOLDERS_AUTORUN_UNSECURE | BOOL |  |  |  | 
AI | PREF_BROWSER_MXAI_SEPARATOR | SEPARATOR |  |  |  | 
Enable AI (runs locally on your machine) | PREF_BROWSER_MXAI_ENABLED | BOOL |  |  |  | 
AI Service Port | PREF_BROWSER_MXAI_PORT | LONG |  |  |  | 
GPU Mode | PREF_BROWSER_MXAI_GPU_MODE | LONG |  |  |  | PREF_BROWSER_MXAI_GPU_MODE_AUTO; PREF_BROWSER_MXAI_GPU_MODE_FORCE_ON; PREF_BROWSER_MXAI_GPU_MODE_FORCE_OFF
