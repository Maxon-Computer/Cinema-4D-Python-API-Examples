# Description: Theme

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/c4d_base/description/prefstheme.res`
- **Symbol:** `Prefstheme`
- **Category:** Other

Use parameter symbols to access parameters and cycle option symbols for cycle values, never their numeric IDs. Treat Min and Max as constraints and Default as the declared initial value; blank cells mean the resource does not declare that metadata, not that the value is zero. Base Description Parameters lists inherited fields from each base; All Parameters lists the effective parameter set for this description.

## Base Description Parameters

No base descriptions.

## All Parameters

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
No label | PREF_THEME_LIST_OVERLAYMODE | LONG |  |  |  | PREF_THEME_LIST_OVERLAYMODE_OPAQUE; PREF_THEME_LIST_OVERLAYMODE_OVERLAY
No label | PREF_THEME_LIST | LISTVIEW |  |  |  | 
No label | PREF_THEME_TYPE | LONG |  |  |  | PREF_THEME_TYPERGB; PREF_THEME_TYPERGBA; PREF_THEME_TYPEBMP; PREF_THEME_TYPEREF
Color | PREF_THEME_COLORS | COLOR |  |  |  | 
Color | PREF_THEME_COLORS_ALPHA | COLORA |  |  |  | 
No label | PREF_THEME_BMP | FILENAME |  |  |  | 
No label | PREF_THEME_BMPPIC | BITMAPBUTTON |  |  |  | 
No label | PREF_THEME_REF | LISTVIEW |  |  |  | 
Live Refresh | PREF_THEME_LIVE | BOOL |  |  |  | 
Reset... | PREF_THEME_RESET | BUTTON |  |  |  | 
