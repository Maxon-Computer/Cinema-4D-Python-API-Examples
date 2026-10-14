# Description: Hair Preferences

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/hair/description/thairprefs.res`
- **Symbol:** `Thairprefs`
- **Category:** Other

Use parameter symbols to access parameters and cycle option symbols for cycle values, never their numeric IDs. Treat Min and Max as constraints and Default as the declared initial value; blank cells mean the resource does not declare that metadata, not that the value is zero. Base Description Parameters lists inherited fields from each base; All Parameters lists the effective parameter set for this description.

## Base Description Parameters

No base descriptions.

## All Parameters

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Auto Add Post Effect | HAIR_PREFS_SETUP_AUTOVP | BOOL |  |  |  | 
Auto Link Object | HAIR_PREFS_SETUP_AUTO_LINK | BOOL |  |  |  | 
Auto Add Material | HAIR_PREFS_SETUP_AUTO_MATERIAL | BOOL |  |  |  | 
Hair as Child | HAIR_PREFS_SETUP_TOCHILD | BOOL |  |  |  | 
Highlighting | HAIR_PREFS_HIGHLIGHTING | BOOL |  |  |  | 
Show Unrooted | HAIR_PREFS_UNROOTED | BOOL |  |  |  | 
Cursor | HAIR_PREFS_SHOW_CURSOR | LONG |  |  |  | HAIR_PREFS_SHOW_CURSOR_OFF; HAIR_PREFS_SHOW_CURSOR_DRAG; HAIR_PREFS_SHOW_CURSOR_ALWAYS
Object Modify Undo | HAIR_PREFS_OBJECT_UNDO | BOOL |  |  |  | 
Dynamics Undo | HAIR_PREFS_DYNAMICS_UNDO | BOOL |  |  |  | 
Default Preview | HAIR_PREFS_PREVIEW | LONG |  |  |  | HAIR_PREFS_PREVIEW_STANDARD; HAIR_PREFS_PREVIEW_SPHERE; HAIR_PREFS_PREVIEW_CUBE; HAIR_PREFS_PREVIEW_ROUNDCUBE; HAIR_PREFS_PREVIEW_PLANE; HAIR_PREFS_PREVIEW_PLANEBACK; HAIR_PREFS_PREVIEW_CYLINDER; HAIR_PREFS_PREVIEW_TORUS; HAIR_PREFS_PREVIEW_DOUBLETORUS; HAIR_PREFS_PREVIEW_KNOT; HAIR_PREFS_PREVIEW_STRAND; HAIR_PREFS_PREVIEW_CUSTOM
Custom | HAIR_PREFS_CUSTOMPREVIEW | LONG |  |  |  | 
