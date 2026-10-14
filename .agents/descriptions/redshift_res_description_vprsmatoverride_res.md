# Description: Material Override

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `Redshift/res/description/vprsmatoverride.res`
- **Symbol:** `VPrsmatoverride`
- **Category:** Video Posts

Use parameter symbols to access parameters and cycle option symbols for cycle values, never their numeric IDs. Treat Min and Max as constraints and Default as the declared initial value; blank cells mean the resource does not declare that metadata, not that the value is zero. Base Description Parameters lists inherited fields from each base; All Parameters lists the effective parameter set for this description.

## Base Description Parameters

### Post Effect (`VPbase`)

No parameters.

## All Parameters

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Mode | REDSHIFT_MATERIAL_OVERRIDE_MODE | LONG |  |  |  | REDSHIFT_MATERIAL_OVERRIDE_MODE_REPLACE; REDSHIFT_MATERIAL_OVERRIDE_MODE_CLAY
Custom Material | REDSHIFT_MATERIAL_OVERRIDE_LINK | LINK |  |  |  | 
Mode | REDSHIFT_MATERIAL_OVERRIDE_EXCLUSION_MODE | LONG |  |  |  | REDSHIFT_MATERIAL_OVERRIDE_EXCLUSION_MODE_INCLUDE; REDSHIFT_MATERIAL_OVERRIDE_EXCLUSION_MODE_EXCLUDE
Materials | REDSHIFT_MATERIAL_OVERRIDE_EXCLUSION_LIST | IN_EXCLUDE |  |  |  | 
Color | REDSHIFT_MATERIAL_OVERRIDE_COLOR | COLOR |  |  |  | 
