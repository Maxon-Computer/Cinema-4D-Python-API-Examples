# Description: Timeline/Spline Gadget

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/c4d_manager/description/prefstimeline.res`
- **Symbol:** `Prefstimeline`
- **Category:** Other

Use parameter symbols to access parameters and cycle option symbols for cycle values, never their numeric IDs. Treat Min and Max as constraints and Default as the declared initial value; blank cells mean the resource does not declare that metadata, not that the value is zero. Base Description Parameters lists inherited fields from each base; All Parameters lists the effective parameter set for this description.

## Base Description Parameters

No base descriptions.

## All Parameters

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
General | PREF_TL_DISPLAYGROUP | SEPARATOR |  |  |  | 
Cursor Indicator | PREF_TL_INDICATOR | BOOL |  |  |  | 
Interactive Update | PREF_TL_INTERACTIVE | BOOL |  |  |  | 
Highlight | PREF_TL_HIGHLIGHT | BOOL |  |  |  | 
Remove Empty Tracks | PREF_TL_DOTSKILLTRACKS | BOOL |  |  |  | 
Track Color | PREF_TL_TRACKCOL | LONG |  |  |  | PREF_TL_TRACKCOL_NO; PREF_TL_TRACKCOL_COL; PREF_TL_TRACKCOL_PSR
Timeline/Object Manager - Linking | PREF_TL_LINKGROUP | SEPARATOR |  |  |  | 
Link Key/F-Curve Selection | PREF_TL_LINKKEYFCSELECTION | BOOL |  |  |  | 
Selected Object Linking | PREF_TL_LINKOMSELECTONLY | BOOL |  |  |  | 
Selected Object Tags Linking | PREF_TL_LINKOMSELECTONLYBUTTAGS | BOOL |  |  |  | 
Timeline - Tree View | PREF_TL_OBJECTGROUP | SEPARATOR |  |  |  | 
Show Branches | PREF_TL_SHOWBRANCHES | BOOL |  |  |  | 
Show Vector Track | PREF_TL_SHOWVECTOR | BOOL |  |  |  | 
F-Curve List View | PREF_TL_FCLISTVIEW_HIERARCHICAL | BOOL |  |  |  | 
F-Curve Non-Hierarchical List View | PREF_TL_FCLISTVIEW | BOOL |  |  |  | 
Timeline - Dope Sheet | PREF_TL_KEYGROUP | SEPARATOR |  |  |  | 
Summary Track | PREF_TL_SUMMARY | BOOL |  |  |  | 
Track Start/End | PREF_TL_TRACKSTARTEND | BOOL |  |  |  | 
Draw Keys on Cells | PREF_TL_DOPESHEET | BOOL |  |  |  | 
Show Key Symbols | PREF_TL_KEYSYMBOLS | BOOL |  |  |  | 
Layer Colors | PREF_TL_LAYERCOL | BOOL |  |  |  | 
Key Width Min | PREF_TL_KEYWIDTHVALUE | LONG | 1 | 100 |  | 
Timeline - F-Curve | PREF_TL_FCGROUP | SEPARATOR |  |  |  | 
Reduced Modification Value | PREF_TL_RMREDUCTION | REAL | 0.0 | 100.0 |  | 
Timeline - Motion | PREF_TL_MOTIONGROUP | SEPARATOR |  |  |  | 
Motion Clip Transition Time | PREF_TL_MOTION | BASETIME | 0 |  |  | 
