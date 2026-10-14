# Description: Depth of Field

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/advanced_render/description/distanceblur.res`
- **Symbol:** `DistanceBlur`
- **Category:** Video Posts

Use parameter symbols to access parameters and cycle option symbols for cycle values, never their numeric IDs. Treat Min and Max as constraints and Default as the declared initial value; blank cells mean the resource does not declare that metadata, not that the value is zero. Base Description Parameters lists inherited fields from each base; All Parameters lists the effective parameter set for this description.

## Base Description Parameters

### Post Effect (`VPbase`)

No parameters.

## All Parameters

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Blur Strength | DB_FBLUR | REAL | 0.0 | 100.0 |  | 
Use Distance Blur | DB_DBLURON | BOOL |  |  |  | 
Distance Blur | DB_DBLUR | REAL | 0.0 | 100.0 |  | 
Use Background Blur | DB_BBLURON | BOOL |  |  |  | 
Background Blur | DB_BBLUR | REAL | 0.0 | 100.0 |  | 
Use Radial Blur | DB_DOFON | BOOL |  |  |  | 
Radial Blur | DB_DOF | REAL | 0.0 | 100.0 |  | 
Use Autofocus | DB_AFOCUSON | BOOL |  |  |  | 
Autofocus Size | DB_AFOCUS | REAL | 0.0 | 100.0 |  | 
Use Gradients | DB_RANGE_USE | BOOL |  |  |  | 
Front Blur | DB_RANGE_FGRAD | GRADIENT |  |  |  | 
Rear Blur | DB_RANGE_BGRAD | GRADIENT |  |  |  | 
Lens Sharpness | DB_SHARP | REAL | 0.0 | 100.0 |  | 
Lens Intensity | DB_MINT | REAL | 0.0 |  |  | 
Lens Shape | DB_REFTYPE | LONG |  |  |  | CIRCULAR; TRIANGLE; RHOMBIC; PENTAGON; HEXAGON; HEPTAGON; OCTAGON; NANOGON
Lens Rotate | DB_ROT | REAL |  |  |  | 
Use Tint | DB_TINT_USE | BOOL |  |  |  | 
Front Color | DB_TINT_FGRAD | GRADIENT |  |  |  | 
Rear Color | DB_TINT_BGRAD | GRADIENT |  |  |  | 
Use Ranges | DB_TINT_USERANGE | BOOL |  |  |  | 
Use Camera Ranges | DB_TINT_USECAM | BOOL |  |  |  | 
Front Start | DB_TINT_FSTART | REAL | 0.0 |  |  | 
Rear Start | DB_TINT_BSTART | REAL | 0.0 |  |  | 
Front End | DB_TINT_FEND | REAL | 0.0 |  |  | 
Rear End | DB_TINT_BEND | REAL | 0.0 |  |  | 
