# Description: Selection

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/hair/description/toolhairselection.res`
- **Symbol:** `ToolHairSelection`
- **Category:** Other

Use parameter symbols to access parameters and cycle option symbols for cycle values, never their numeric IDs. Treat Min and Max as constraints and Default as the declared initial value; blank cells mean the resource does not declare that metadata, not that the value is zero. Base Description Parameters lists inherited fields from each base; All Parameters lists the effective parameter set for this description.

## Base Description Parameters

### Base Tool (`ToolBase`)

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Realtime Update | MDATA_INTERACTIVE | BOOL |  |  |  | 
    Apply     | MDATA_APPLY | BUTTON |  |  |  | 
New Transform | MDATA_NEWTRANSFORM | BUTTON |  |  |  | 
No label | ID_SNAPSETTINGS | SUBCONTAINER |  |  |  | 

## All Parameters

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Realtime Update | MDATA_INTERACTIVE | BOOL |  |  |  | 
    Apply     | MDATA_APPLY | BUTTON |  |  |  | 
New Transform | MDATA_NEWTRANSFORM | BUTTON |  |  |  | 
No label | ID_SNAPSETTINGS | SUBCONTAINER |  |  |  | 
Mode | HAIR_SELECTION_MODE | LONG |  |  |  | HAIR_SELECTION_MODE_NEW; HAIR_SELECTION_MODE_ADD; HAIR_SELECTION_MODE_REMOVE
Select | HAIR_SELECTION_SELECT | LONG |  |  |  | HAIR_SELECTION_SELECT_UNROOTED; HAIR_SELECTION_SELECT_INTERSECTING; HAIR_SELECTION_SELECT_ZERO
Invert | HAIR_SELECTION_INVERT | BOOL |  |  |  | 
