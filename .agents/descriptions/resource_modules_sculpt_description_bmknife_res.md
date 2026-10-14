# Description: Knife

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/sculpt/description/bmknife.res`
- **Symbol:** `BMknife`
- **Category:** Other

Use parameter symbols to access parameters and cycle option symbols for cycle values, never their numeric IDs. Treat Min and Max as constraints and Default as the declared initial value; blank cells mean the resource does not declare that metadata, not that the value is zero. Base Description Parameters lists inherited fields from each base; All Parameters lists the effective parameter set for this description.

## Base Description Parameters

### Modifier (`BMbase`)

No parameters.

## All Parameters

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Knife | MDATA_BRUSHMODIFIERBASE_ENABLED | BOOL |  |  |  | 
Strength | MDATA_BRUSHMODIFIERBASE_STRENGTH | REAL | 0 |  |  | 
Invert | BM_KNIFE_INVERT | BOOL |  |  |  | 
Pinch | BM_KNIFE_PINCH | REAL | 0 | 1 |  | 
Push | BM_KNIFE_PUSH | REAL | 0 | 100 |  | 
