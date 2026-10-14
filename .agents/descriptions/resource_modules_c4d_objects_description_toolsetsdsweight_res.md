# Description: Weight Subdivision Surface

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/c4d_objects/description/toolsetsdsweight.res`
- **Symbol:** `ToolSetSDSWeight`
- **Category:** Other

Use parameter symbols to access parameters and cycle option symbols for cycle values, never their numeric IDs. Treat Min and Max as constraints and Default as the declared initial value; blank cells mean the resource does not declare that metadata, not that the value is zero. Base Description Parameters lists inherited fields from each base; All Parameters lists the effective parameter set for this description.

## Base Description Parameters

No base descriptions.

## All Parameters

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Mode | MDATA_SDSWEIGHT_MODE | LONG |  |  |  | MDATA_SDSWEIGHT_MODE_SET; MDATA_SDSWEIGHT_MODE_ADD; MDATA_SDSWEIGHT_MODE_SUB
Strength | MDATA_SDSWEIGHT_STRENGTH | REAL | -100.0 | 100.0 |  | 
Set | MDATA_SDSWEIGTH_SETSTRENGTH | BUTTON |  |  |  | 
Interactive Minimum | MDATA_SDSWEIGHT_INTERACTIVEMIN | REAL | -100.0 | 100.0 |  | 
Interactive Maximum | MDATA_SDSWEIGHT_INTERACTIVEMAX | REAL | -100.0 | 100.0 |  | 
