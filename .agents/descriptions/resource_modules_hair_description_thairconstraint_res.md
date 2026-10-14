# Description: Rope Belt

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/hair/description/thairconstraint.res`
- **Symbol:** `Thairconstraint`
- **Category:** Tags

Use parameter symbols to access parameters and cycle option symbols for cycle values, never their numeric IDs. Treat Min and Max as constraints and Default as the declared initial value; blank cells mean the resource does not declare that metadata, not that the value is zero. Base Description Parameters lists inherited fields from each base; All Parameters lists the effective parameter set for this description.

## Base Description Parameters

### Base Tag (`Tbase`)

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Expose on Object | ID_EXPOSETAB | BOOL |  |  |  | 

### Basic Properties (`Obaselist`)

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Icon File / ID | ID_BASELIST_ICON_FILE | TEXTURE |  |  |  | 
Icon Color | ID_BASELIST_ICON_COLORIZE_MODE | BOOL |  |  |  | 
Color | ID_BASELIST_ICON_COLOR | COLOR |  |  | 1.0 0.9 0.4 | 
No label | ID_BASELIST_ICON_PRESET_BUTTONS | ICONCHOOSER |  |  |  | 
Name | ID_BASELIST_NAME | STRING |  |  |  | 
Layer | ID_LAYER_LINK | LINK |  |  |  | 
No label | ID_BASELIST_NODESPACE_ADD_REMOVE_BUTTONS | NODESPACE_ADD_REMOVE |  |  |  | 

## All Parameters

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Icon File / ID | ID_BASELIST_ICON_FILE | TEXTURE |  |  |  | 
Icon Color | ID_BASELIST_ICON_COLORIZE_MODE | BOOL |  |  |  | 
Color | ID_BASELIST_ICON_COLOR | COLOR |  |  | 1.0 0.9 0.4 | 
No label | ID_BASELIST_ICON_PRESET_BUTTONS | ICONCHOOSER |  |  |  | 
Name | ID_BASELIST_NAME | STRING |  |  |  | 
Layer | ID_LAYER_LINK | LINK |  |  |  | 
No label | ID_BASELIST_NODESPACE_ADD_REMOVE_BUTTONS | NODESPACE_ADD_REMOVE |  |  |  | 
Expose on Object | ID_EXPOSETAB | BOOL |  |  |  | 
Draw | HAIR_CONSTRAINTS_TAG_DRAW_ANCHOR | BOOL |  |  |  | 
Set | HAIR_CONSTRAINTS_TAG_SET_ANCHOR | BUTTON |  |  |  | 
Release | HAIR_CONSTRAINTS_TAG_RELEASE_ANCHOR | BUTTON |  |  |  | 
Clear | HAIR_CONSTRAINTS_TAG_CLEAR_ANCHOR | BUTTON |  |  |  | 
Object | HAIR_CONSTRAINTS_TAG_ANCHOR_LINK | LINK |  |  |  | 
Influence | HAIR_CONSTRAINTS_TAG_STRENGTH | REAL | 0.0 | 100.0 |  | 
Offset | HAIR_CONSTRAINTS_TAG_OFFSET | REAL |  |  |  | 
Influence Map | HAIR_CONSTRAINTS_TAG_STRENGTH_LINK | LINK |  |  |  | 
Offset Map | HAIR_CONSTRAINTS_TAG_OFFSET_LINK | LINK |  |  |  | 
