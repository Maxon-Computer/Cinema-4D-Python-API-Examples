# Description: UV Peeler Tool

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/c4d_objects/description/xuvpeelertool.res`
- **Symbol:** `xuvpeelertool`
- **Category:** Other

Use parameter symbols to access parameters and cycle option symbols for cycle values, never their numeric IDs. Treat Min and Max as constraints and Default as the declared initial value; blank cells mean the resource does not declare that metadata, not that the value is zero. Base Description Parameters lists inherited fields from each base; All Parameters lists the effective parameter set for this description.

## Base Description Parameters

No base descriptions.

## All Parameters

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Min U | MDATA_UVPEELER_MIN_U | REAL | 0.0 | 1.0 |  | 
Max U | MDATA_UVPEELER_MAX_U | REAL | 0.0 | 1.0 |  | 
Min V | MDATA_UVPEELER_MIN_V | REAL | 0.0 | 1.0 |  | 
Max V | MDATA_UVPEELER_MAX_V | REAL | 0.0 | 1.0 |  | 
U Uniformity | MDATA_UVPEELER_U_UNIFORMITY | REAL | 0 | 100 |  | 
V Uniformity | MDATA_UVPEELER_V_UNIFORMITY | REAL | 0 | 100 |  | 
Invert U | MDATA_UVPEELER_U_INVERT | BOOL |  |  |  | 
Fixed Ring Lengths | MDATA_UVPEELER_FIXED_RING_LENGTHS | BOOL |  |  |  | 
Invert V | MDATA_UVPEELER_V_INVERT | BOOL |  |  |  | 
Equidistant Uniformity | MDATA_UVPEELER_EQUIDISTANT_UNIFORMITY | BOOL |  |  |  | 
UV Island Storage | MDATA_UVPEELER_UV_ISLAND_STORAGE | LONG |  |  |  | MDATA_UVPEELER_SINGLE_UV_TILE; MDATA_UVPEELER_MULTIPLE_UV_TILES
Restrict UV Islands to Tiles | MDATA_UVPEELER_RESTRICT_TO_TILES | BOOL |  |  |  | 
Realtime Update | MDATA_UVPEELER_INTERACTIVE | BOOL |  |  |  | 
Valid Seams:  | MDATA_UVPEELER_INFOS_SEAMS | STATICTEXT |  |  |  | 
    Apply     | MDATA_UVPEELER_APPLY | BUTTON |  |  |  | 
Reset Values | MDATA_UVPEELER_RESET | BUTTON |  |  |  | 
