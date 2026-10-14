# Description: Edge Selection Tag

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/c4d_base/description/tedgeselection.res`
- **Symbol:** `Tedgeselection`
- **Category:** Tags

Use parameter symbols to access parameters and cycle option symbols for cycle values, never their numeric IDs. Treat Min and Max as constraints and Default as the declared initial value; blank cells mean the resource does not declare that metadata, not that the value is zero. Base Description Parameters lists inherited fields from each base; All Parameters lists the effective parameter set for this description.

## Base Description Parameters

### No label (`Ttransfer`)

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Transfer | TRANSFER_CONTROL | LONG |  |  |  | TRANSFER_CONTROL_OFF; TRANSFER_CONTROL_FIELDS; TRANSFER_CONTROL_PROPERTY

### Expression (`Texpression`)

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Priority | EXPRESSION_PRIORITY | PRIORITY |  |  |  | 
Enable | EXPRESSION_ENABLE | BOOL |  |  |  | 

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

### No label (`Tattributetransfer`)

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Use Deformed Points | TATTRIBUTETRANSFER_DEFORMED_POINTS | BOOL |  |  |  | 
Source Tag | TATTRIBUTETRANSFER_SOURCE | LINK |  |  |  | 
Evaluation Method | TATTRIBUTETRANSFER_EVAL_METHOD | LONG |  |  |  | TATTRIBUTETRANSFER_EVAL_METHOD_NEAREST_SURFACE; TATTRIBUTETRANSFER_EVAL_METHOD_NEAREST_POINT; TATTRIBUTETRANSFER_EVAL_METHOD_NORMALS_PROJECTION; TATTRIBUTETRANSFER_EVAL_METHOD_SOURCE_AXIS_PROJECTION; TATTRIBUTETRANSFER_EVAL_METHOD_TARGET_AXIS_PROJECTION; TATTRIBUTETRANSFER_EVAL_METHOD_NEAREST_POLYGON_DATA_BREAKS
Transform | TATTRIBUTETRANSFER_TRANSFORM | LONG |  |  |  | TATTRIBUTETRANSFER_TRANSFORM_OFF; TATTRIBUTETRANSFER_TRANSFORM_FLIPX; TATTRIBUTETRANSFER_TRANSFORM_FLIPY; TATTRIBUTETRANSFER_TRANSFORM_FLIPZ
Space | TATTRIBUTETRANSFER_SPACE | LONG |  |  |  | TATTRIBUTETRANSFER_SPACE_LOCAL; TATTRIBUTETRANSFER_SPACE_GLOBAL

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
Priority | EXPRESSION_PRIORITY | PRIORITY |  |  |  | 
Enable | EXPRESSION_ENABLE | BOOL |  |  |  | 
Transfer | TRANSFER_CONTROL | LONG |  |  |  | TRANSFER_CONTROL_OFF; TRANSFER_CONTROL_FIELDS; TRANSFER_CONTROL_PROPERTY
Update | EDGESELECTIONTAG_UPDATE | BUTTON |  |  |  | 
Count: | EDGESELECTIONTAG_COUNT | STATICTEXT |  |  |  | 
Select | EDGESELECTIONTAG_COMMAND1 | BUTTON |  |  |  | 
Deselect | EDGESELECTIONTAG_COMMAND4 | BUTTON |  |  |  | 
Hide | EDGESELECTIONTAG_COMMAND5 | BUTTON |  |  |  | 
Show | EDGESELECTIONTAG_COMMAND6 | BUTTON |  |  |  | 
Solo | EDGESELECTIONTAG_COMMAND2 | BUTTON |  |  |  | 
Show All | EDGESELECTIONTAG_UNHIDEALL | BUTTON |  |  |  | 
Select: Shift to add, Ctrl to remove from selection. | EDGESELECTIONTAG_MODIFIERHINT | STATICTEXT |  |  |  | 
Mark Seams | EDGESELECTIONTAG_SEAMS_MARK | BUTTON |  |  |  | 
Unmark Seams | EDGESELECTIONTAG_SEAMS_UNMARK | BUTTON |  |  |  | 
Clear Seams | EDGESELECTIONTAG_SEAMS_CLEAR | BUTTON |  |  |  | 
Select | EDGESELECTIONTAG_SEAMS_SELECT | BUTTON |  |  |  | 
Deselect | EDGESELECTIONTAG_SEAMS_DESELECT | BUTTON |  |  |  | 
Tolerance | EDGESELECTIONTAG_FIELDTOLERANCE | REAL | 0.0 | 100.0 |  | 
Use Deformed Points | EDGESELECTIONTAG_DEFORMEDSTATE | BOOL |  |  |  | 
Fields | EDGESELECTIONTAG_FIELDS | FIELDLIST |  |  |  | 
Use Deformed Points | TATTRIBUTETRANSFER_DEFORMED_POINTS | BOOL |  |  |  | 
Evaluation Method | TATTRIBUTETRANSFER_EVAL_METHOD | LONG |  |  |  | TATTRIBUTETRANSFER_EVAL_METHOD_NEAREST_SURFACE; TATTRIBUTETRANSFER_EVAL_METHOD_NEAREST_POINT; TATTRIBUTETRANSFER_EVAL_METHOD_NORMALS_PROJECTION; TATTRIBUTETRANSFER_EVAL_METHOD_SOURCE_AXIS_PROJECTION; TATTRIBUTETRANSFER_EVAL_METHOD_TARGET_AXIS_PROJECTION; TATTRIBUTETRANSFER_EVAL_METHOD_NEAREST_POLYGON_DATA_BREAKS
Transform | TATTRIBUTETRANSFER_TRANSFORM | LONG |  |  |  | TATTRIBUTETRANSFER_TRANSFORM_OFF; TATTRIBUTETRANSFER_TRANSFORM_FLIPX; TATTRIBUTETRANSFER_TRANSFORM_FLIPY; TATTRIBUTETRANSFER_TRANSFORM_FLIPZ
Space | TATTRIBUTETRANSFER_SPACE | LONG |  |  |  | TATTRIBUTETRANSFER_SPACE_LOCAL; TATTRIBUTETRANSFER_SPACE_GLOBAL
Source Tag | TATTRIBUTETRANSFER_SOURCE | LINK |  |  |  | 
