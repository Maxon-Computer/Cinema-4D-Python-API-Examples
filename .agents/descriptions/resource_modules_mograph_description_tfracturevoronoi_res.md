# Description: Point Source Object

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/mograph/description/tfracturevoronoi.res`
- **Symbol:** `tfracturevoronoi`
- **Category:** Other

Use parameter symbols to access parameters and cycle option symbols for cycle values, never their numeric IDs. Treat Min and Max as constraints and Default as the declared initial value; blank cells mean the resource does not declare that metadata, not that the value is zero. Base Description Parameters lists inherited fields from each base; All Parameters lists the effective parameter set for this description.

## Base Description Parameters

No base descriptions.

## All Parameters

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Creation Method | ID_FRACTURETAG_POINTCREATIONTYPE | LONG |  |  |  | ID_FRACTURETAG_VERTICES; ID_FRACTURETAG_EDGES; ID_FRACTURETAG_POLYS; ID_FRACTURETAG_SURFACE; ID_FRACTURETAG_VOLUME
Distribution | ID_FRACTURETAG_SPLINE_DISTRIBUTION | LONG |  |  |  | ID_FRACTURETAG_SPLINE_EVEN; ID_FRACTURETAG_SPLINE_STEP; ID_FRACTURETAG_SPLINE_COUNT; ID_FRACTURETAG_SPLINE_VERTICES
Sub Groups | ID_FRACTURETAG_TP_SUBGROUPS | BOOL |  |  |  | 
Point Amount | ID_FRACTURETAG_POINTAMOUNT | LONG | 0 |  |  | 
Seed | ID_FRACTURETAG_SEED | LONG | 0 |  |  | 
Offset | ID_FRACTURETAG_OFFSET | REAL |  |  |  | 
Fix Points to Generator | ID_FRACTURETAG_LOCK | BOOL |  |  |  | 
