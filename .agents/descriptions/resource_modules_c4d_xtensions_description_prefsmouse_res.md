# Description: Mouse

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/c4d_xtensions/description/prefsmouse.res`
- **Symbol:** `Prefsmouse`
- **Category:** Other

Use parameter symbols to access parameters and cycle option symbols for cycle values, never their numeric IDs. Treat Min and Max as constraints and Default as the declared initial value; blank cells mean the resource does not declare that metadata, not that the value is zero. Base Description Parameters lists inherited fields from each base; All Parameters lists the effective parameter set for this description.

## Base Description Parameters

No base descriptions.

## All Parameters

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Transform Cursor | PREF_MOUSE_BASICCURSOR | BOOL |  |  |  | 
Tool Cursors | PREF_MOUSE_CURSOR | BOOL |  |  |  | 
Mouse Move Activation | PREF_MOUSE_ACTIVATION | BOOL |  |  |  | 
Control-Click for Right-Click | PREF_MOUSE_RMB_EMULATION | BOOL |  |  |  | 
Graphics Tablet | PREF_MOUSE_GRAPHICTABLET | BOOL |  |  |  | 
Hi-Res Tablet | PREF_MOUSE_HIRESTABLET | BOOL |  |  |  | 
Commander at Mouse Position | PREF_MOUSE_COMMANDER_AT_CURSOR | BOOL |  |  |  | 
Touch Support | PREF_MOUSE_TOUCHSUPPORT | LONG |  |  |  | PREF_MOUSE_TS_AUTOMATIC; PREF_MOUSE_TS_WHEEL; PREF_MOUSE_TS_TOUCH
