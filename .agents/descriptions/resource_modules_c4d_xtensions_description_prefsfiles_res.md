# Description: Files

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/c4d_xtensions/description/prefsfiles.res`
- **Symbol:** `Prefsfiles`
- **Category:** Other

Use parameter symbols to access parameters and cycle option symbols for cycle values, never their numeric IDs. Treat Min and Max as constraints and Default as the declared initial value; blank cells mean the resource does not declare that metadata, not that the value is zero. Base Description Parameters lists inherited fields from each base; All Parameters lists the effective parameter set for this description.

## Base Description Parameters

No base descriptions.

## All Parameters

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Recent Files | PREF_FILE_RECENT | LONG | 0 | 100 |  | 
Backup Copies | PREF_FILE_BACKUP | LONG | 0 | 1000 |  | 
Link Assets | PREF_FILE_ASSETS_LINK | LONG |  |  |  | PREF_FILE_ASSETS_LINK_RELATIVE; PREF_FILE_ASSETS_LINK_ABSOLUTE; PREF_FILE_ASSETS_LINK_ASK
Render Output Behavior | PREF_FILE_RENDER_OVERWRITE_DEFAULT | LONG |  |  |  | PREF_FILE_RENDER_OVERWRITE_DEFAULT_ASK; PREF_FILE_RENDER_OVERWRITE_DEFAULT_OVERWRITE; PREF_FILE_RENDER_OVERWRITE_DEFAULT_NEVEROVERWRITE; PREF_FILE_RENDER_OVERWRITE_DEFAULT_SKIP
Auto-Save | PREFS_FILE_AUTOSAVE | SEPARATOR |  |  |  | 
Save | PREF_FILE_AUTOEVERY | BOOL |  |  |  | 
Every (min) | PREF_FILE_AUTOMIN | LONG | 1 | 10000 |  | 
Limit | PREF_FILE_AUTOLIMIT | BOOL |  |  |  | 
To (Copies) | PREF_FILE_AUTOCOPIES | LONG | 1 | 1000 |  | 
Save to Folder | PREF_FILE_AUTOSAVETO | LONG |  |  |  | PREF_FILE_AUTOSAVE_PRJ; PREF_FILE_AUTOSAVE_USR; PREF_FILE_AUTOSAVE_CST
No label | PREF_FILE_AUTOSAVEDIR | FILENAME |  |  |  | 
XRefs Project Load/Save | ID_FILES_GROUP_XREF | SEPARATOR |  |  |  | 
Deferred Refresh on Open | ID_FILES_XREFPREFS_DEFERRED_LOAD | BOOL |  |  |  | 
Reduced References on Save | ID_FILES_XREFPREFS_REDUCED_SAVE | BOOL |  |  |  | 
File Assets | PREF_FILE_ASSETS | SEPARATOR |  |  |  | 
Paths | PREF_FILE_TEXPATHS | STRING |  |  |  | 
Paths as Watch Folders | PREF_WATCHFOLDER_AUTOMOUNT_SEARCHPATHS | BOOL |  |  |  | 
Laubwerk Legacy Library Folder | PREF_FILE_LBWLIRARYPATH | FILENAME |  |  |  | 
Startup | PREF_FILE_STARTUP | SEPARATOR |  |  |  | 
Default Scene | PREF_DEFAULT_SCENE | LONG |  |  |  | PREF_DEFAULT_SCENE_EXAMPLE1; PREF_DEFAULT_SCENE_BLANK; PREF_DEFAULT_SCENE_CUSTOM
No label | PREF_DEFAULT_SCENE_CUSTOM_FILE | FILENAME |  |  |  | 
