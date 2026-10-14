# Description: Interface

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/c4d_base/description/prefsinterface.res`
- **Symbol:** `Prefsinterface`
- **Category:** Other

Use parameter symbols to access parameters and cycle option symbols for cycle values, never their numeric IDs. Treat Min and Max as constraints and Default as the declared initial value; blank cells mean the resource does not declare that metadata, not that the value is zero. Base Description Parameters lists inherited fields from each base; All Parameters lists the effective parameter set for this description.

## Base Description Parameters

No base descriptions.

## All Parameters

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Translation | PREF_INTERFACE_TRANSLATIONGROUP | SEPARATOR |  |  |  | 
Language | PREF_INTERFACE_LANGUAGE | LONG |  |  |  | 
Scheme | PREF_INTERFACE_SCHEME | LONG |  |  |  | 
Font | PREF_INTERFACE_FONTGROUP | SEPARATOR |  |  |  | 
User Interface | PREF_INTERFACE_FONTSTD | FONT |  |  |  | 
Monospaced | PREF_INTERFACE_FONTMONO | FONT |  |  |  | 
Helpers | PREF_INTERFACE_HELPERSGROUP | SEPARATOR |  |  |  | 
Highlight Features | PREF_INTERFACE_NEWFEATUREHIGHLIGHT | LONG |  |  |  | 
Fading | PREF_INTERFACE_NEWFEATUREHIGHLIGHT_FADE | BOOL |  |  |  | 
Warning | PREF_INTERFACE_NEWFEATUREHIGHLIGHT_RESET_WARNING | STATICTEXT |  |  |  | 
Reset Highlights | PREF_INTERFACE_NEWFEATUREHIGHLIGHT_RESET | BUTTON |  |  |  | 
Mac Menu Bar | PREF_INTERFACE_MACMENU | BOOL |  |  |  | 
Icons in Menu | PREF_INTERFACE_MENUICONS | BOOL |  |  |  | 
Shortcuts in Menu | PREF_INTERFACE_MENUSCUT | BOOL |  |  |  | 
Tooltips | PREF_INTERFACE_BUBBLE | BOOL |  |  |  | 
Online Content | PREF_INTERFACE_ONLINEHELP | BOOL |  |  |  | 
External Browser | PREF_INTERFACE_EXTERNALHELP | BOOL |  |  |  | 
Script Word Wrap | PREF_INTERFACE_SCRIPTWORDWRAP | BOOL |  |  |  | 
Object Creation | PREF_INTERFACE_OBJECTGROUP | SEPARATOR |  |  |  | 
Create Objects at View Center | PREF_INTERFACE_CENTEROBJECT | BOOL |  |  |  | 
Insert Objects at | PREF_INTERFACE_INSERTAT | LONG |  |  |  | PREF_INTERFACE_I_TOP; PREF_INTERFACE_I_BOTTOM; PREF_INTERFACE_I_PREV; PREF_INTERFACE_I_NEXT; PREF_INTERFACE_I_PARENT; PREF_INTERFACE_I_CHILD; PREF_INTERFACE_I_ROOT
Paste Objects at | PREF_INTERFACE_PASTEAT | LONG |  |  |  | PREF_INTERFACE_I_TOP; PREF_INTERFACE_I_BOTTOM; PREF_INTERFACE_I_PREV; PREF_INTERFACE_I_NEXT; PREF_INTERFACE_I_PARENT; PREF_INTERFACE_I_CHILD; PREF_INTERFACE_I_ROOT
Drag/Clone Objects at | PREF_INTERFACE_DRAGCLONEAT | LONG |  |  |  | PREF_INTERFACE_I_SAMELEVEL; PREF_INTERFACE_I_TOP; PREF_INTERFACE_I_BOTTOM; PREF_INTERFACE_I_PREV; PREF_INTERFACE_I_NEXT; PREF_INTERFACE_I_PARENT; PREF_INTERFACE_I_CHILD; PREF_INTERFACE_I_ROOT
Attribute Manager | PREF_INTERFACE_ATTRIBUTEGROUP | SEPARATOR |  |  |  | 
UI Spacing | PREF_INTERFACE_UI_SPACING | LONG |  |  |  | PREF_INTERFACE_UI_SPACING_COMPACT; PREF_INTERFACE_UI_SPACING_MEDIUM; PREF_INTERFACE_UI_SPACING_COMFORTABLE
Selection Limit | PREF_INTERFACE_AMLIMIT | LONG | 10 | 100000 |  | 
Selection Limit (Nodes) | PREF_INTERFACE_AMLIMIT_NODES | LONG | 1 | 100000 |  | 
Field Remapping Graph | PREF_INTERFACE_HIDEFIELDGRAPH | LONG |  |  |  | PREF_INTERFACE_HIDEFIELDGRAPH_OFF; PREF_INTERFACE_HIDEFIELDGRAPH_INFIELDS; PREF_INTERFACE_HIDEFIELDGRAPH_ON
