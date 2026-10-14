# Description: Sketch and Toon Preferences

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/sketch/description/ttoonupprefs.res`
- **Symbol:** `Ttoonupprefs`
- **Category:** Other

Use parameter symbols to access parameters and cycle option symbols for cycle values, never their numeric IDs. Treat Min and Max as constraints and Default as the declared initial value; blank cells mean the resource does not declare that metadata, not that the value is zero. Base Description Parameters lists inherited fields from each base; All Parameters lists the effective parameter set for this description.

## Base Description Parameters

No base descriptions.

## All Parameters

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Auto Add Post Effect | TOONUP_PREFS_SETUP_AUTOVP | BOOL |  |  |  | 
Auto Add Material (Post Effect) | TOONUP_PREFS_SETUP_AUTOADDVPMAT | BOOL |  |  |  | 
Auto Add Material (Style Tag) | TOONUP_PREFS_SETUP_AUTOADDTAGMAT | BOOL |  |  |  | 
Material Background Color | TOONUP_PREFS_PREVIEW_BACKGROUND | LONG |  |  |  | TOONUP_PREFS_PREVIEW_BACKGROUND_DEFAULT; TOONUP_PREFS_PREVIEW_BACKGROUND_WHITE; TOONUP_PREFS_PREVIEW_BACKGROUND_BLACK; TOONUP_PREFS_PREVIEW_BACKGROUND_SHADED
Material Object Color | TOONUP_PREFS_PREVIEW_OBJECT | LONG |  |  |  | TOONUP_PREFS_PREVIEW_OBJECT_DEFAULT; TOONUP_PREFS_PREVIEW_OBJECT_WHITE; TOONUP_PREFS_PREVIEW_OBJECT_BLACK; TOONUP_PREFS_PREVIEW_OBJECT_TRANS; TOONUP_PREFS_PREVIEW_OBJECT_SHADED
Material Preview | TOONUP_PREFS_PREVIEW | LONG |  |  |  | TOONUP_PREFS_PREVIEW_STANDARD; TOONUP_PREFS_PREVIEW_CUBE; TOONUP_PREFS_PREVIEW_ROUNDCUBE; TOONUP_PREFS_PREVIEW_PLANE; TOONUP_PREFS_PREVIEW_CYLINDER; TOONUP_PREFS_PREVIEW_TORUS; TOONUP_PREFS_PREVIEW_PLANEBACK; TOONUP_PREFS_PREVIEW_SPHERE; TOONUP_PREFS_PREVIEW_DOUBLETORUS; TOONUP_PREFS_PREVIEW_KNOT; TOONUP_PREFS_PREVIEW_STROKE; TOONUP_PREFS_PREVIEW_CUSTOM
Custom Preview | TOONUP_PREFS_CUSTOMPREVIEW | LONG |  |  |  | 
