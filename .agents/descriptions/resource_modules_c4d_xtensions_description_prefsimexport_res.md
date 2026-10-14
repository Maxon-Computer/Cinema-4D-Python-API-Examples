# Description: Import/Export

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/c4d_xtensions/description/prefsimexport.res`
- **Symbol:** `Prefsimexport`
- **Category:** Other

Use parameter symbols to access parameters and cycle option symbols for cycle values, never their numeric IDs. Treat Min and Max as constraints and Default as the declared initial value; blank cells mean the resource does not declare that metadata, not that the value is zero. Base Description Parameters lists inherited fields from each base; All Parameters lists the effective parameter set for this description.

## Base Description Parameters

No base descriptions.

## All Parameters

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Import | PREF_IMEXPORT_IMPORT_GROUP | SEPARATOR |  |  |  | 
Target | PREF_IMEXPORT_NODESPACE | LONG |  |  | 0 | 
Color Space | PREF_IMEXPORT_OCIO_IMPORT_MODE | LONG |  |  |  | 
Show Dialog | PREF_IMEXPORT_SHOW_IMPORT_DLG | BOOL |  |  |  | 
Merge on Drag &amp; Drop | PREF_IMEXPORT_MERGE_ON_DD | BOOL |  |  |  | 
Verify Scripts | PREF_IMEXPORT_VERIFY_SCRIPT | LONG |  |  |  | PREF_IMEXPORT_VERIFY_SCRIPT_NEVER; PREF_IMEXPORT_VERIFY_SCRIPT_ONCE; PREF_IMEXPORT_VERIFY_SCRIPT_ALWAYS
Flush Data | PREF_IMEXPORT_VERIFY_SCRIPT_FLUSH | BUTTON |  |  |  | 
Export | PREF_IMEXPORT_EXPORT_GROUP | SEPARATOR |  |  |  | 
Color Space | PREF_IMEXPORT_OCIO_EXPORT_MODE | LONG |  |  |  | 
Show Dialog | PREF_IMEXPORT_SHOW_EXPORT_DLG | BOOL |  |  |  | 
No label | PREF_IMEXPORT_INFOTEXT | STRING |  |  |  | 
