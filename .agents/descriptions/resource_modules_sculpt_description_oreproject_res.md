# Description: Project Mesh

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/sculpt/description/oreproject.res`
- **Symbol:** `Oreproject`
- **Category:** Other

Use parameter symbols to access parameters and cycle option symbols for cycle values, never their numeric IDs. Treat Min and Max as constraints and Default as the declared initial value; blank cells mean the resource does not declare that metadata, not that the value is zero. Base Description Parameters lists inherited fields from each base; All Parameters lists the effective parameter set for this description.

## Base Description Parameters

No base descriptions.

## All Parameters

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Source | MDATA_REPROJECT_SOURCELIST | IN_EXCLUDE |  |  |  | 
Dest | MDATA_REPROJECT_DEST | LINK |  |  |  | 
Create Copy | MDATA_REPROJECT_CREATECOPY | BOOL |  |  |  | 
Hide When Finished | MDATA_REPROJECT_HIDE | BOOL |  |  |  | 
Subdivision Level | MDATA_REPROJECT_SUBDIVISION_LEVEL | LONG | 0 | 12 |  | 
Polygon Count Estimate:  | MDATA_REPROJECT_POLY_ESTIMATE | STATICTEXT |  |  |  | 
Project | MDATA_REPROJECT_PROJECT | BUTTON |  |  |  | 
