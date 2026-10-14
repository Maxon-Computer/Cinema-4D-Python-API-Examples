# Description: GoZ Preferences

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/io_goz/description/prefsgoz.res`
- **Symbol:** `prefsgoz`
- **Category:** Other

Use parameter symbols to access parameters and cycle option symbols for cycle values, never their numeric IDs. Treat Min and Max as constraints and Default as the declared initial value; blank cells mean the resource does not declare that metadata, not that the value is zero. Base Description Parameters lists inherited fields from each base; All Parameters lists the effective parameter set for this description.

## Base Description Parameters

No base descriptions.

## All Parameters

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Import | GOZ_IMPORT_GROUP | SEPARATOR |  |  |  | 
Scale | GOZ_SCALE_FACTOR_IMPORT | REAL |  |  |  | 
Color Map | GOZ_IMPORT_COLOR_MAP | BOOL |  |  |  | 
Normal Map | GOZ_IMPORT_NORMAL_MAP | BOOL |  |  |  | 
Displacement Map | GOZ_IMPORT_DISPLACEMENT_MAP | BOOL |  |  |  | 
UVs | GOZ_IMPORT_UVW | BOOL |  |  |  | 
Subdivision Surface | GOZ_IMPORT_CREASE_EDGE | BOOL |  |  |  | 
Polypaint | GOZ_IMPORT_POLYPAINT | BOOL |  |  |  | 
Polygroup | GOZ_IMPORT_POLYGROUP | BOOL |  |  |  | 
Replace Existing | GOZ_IMPORT_REPLACEEXISTING | BOOL |  |  |  | 
Target | GOZ_IMPORT_TARGET | LONG |  |  |  | GOZ_IMPORT_TARGET_AUTO; GOZ_IMPORT_TARGET_STANDARD; GOZ_IMPORT_TARGET_REDSHIFT
Export | GOZ_EXPORT_GROUP | SEPARATOR |  |  |  | 
Scale | GOZ_SCALE_FACTOR_EXPORT | REAL |  |  |  | 
Color Map | GOZ_EXPORT_COLOR_MAP | BOOL |  |  |  | 
Normal Map | GOZ_EXPORT_NORMAL_MAP | BOOL |  |  |  | 
Displacement Map | GOZ_EXPORT_DISPLACEMENT_MAP | BOOL |  |  |  | 
UVs | GOZ_EXPORT_UVW | BOOL |  |  |  | 
Crease Edge | GOZ_EXPORT_CREASE_EDGE | BOOL |  |  |  | 
Polypaint | GOZ_EXPORT_POLYPAINT | BOOL |  |  |  | 
Polygroup | GOZ_EXPORT_POLYGROUP | BOOL |  |  |  | 
Connect With Children | GOZ_EXPORT_CONNECTWITHCHILDREN | BOOL |  |  |  | 
Bake Materials | GOZ_EXPORT_BAKE_MATERIALS | BOOL |  |  | 1 | 
Width | GOZ_EXPORT_BAKEDTEXTURE_WIDTH | LONG | 0 | 128000 |  | 
Height | GOZ_EXPORT_BAKEDTEXTURE_HEIGHT | LONG | 0 | 128000 |  | 
Format | GOZ_EXPORT_BAKEDTEXTURE_FORMAT | LONG |  |  |  | 
Depth | GOZ_EXPORT_BAKEDTEXTURE_DEPTH | LONG |  |  | GOZ_EXPORT_BAKEDTEXTURE_DEPTH_8 | GOZ_EXPORT_BAKEDTEXTURE_DEPTH_8; GOZ_EXPORT_BAKEDTEXTURE_DEPTH_16; GOZ_EXPORT_BAKEDTEXTURE_DEPTH_32
Hold SHIFT to invert the behaviour. | GOZ_EXPORT_SHIFTKEY | STATICTEXT |  |  |  | 
