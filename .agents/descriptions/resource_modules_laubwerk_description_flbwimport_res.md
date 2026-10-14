# Description: LBW Import

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/laubwerk/description/flbwimport.res`
- **Symbol:** `Flbwimport`
- **Category:** Files

Use parameter symbols to access parameters and cycle option symbols for cycle values, never their numeric IDs. Treat Min and Max as constraints and Default as the declared initial value; blank cells mean the resource does not declare that metadata, not that the value is zero. Base Description Parameters lists inherited fields from each base; All Parameters lists the effective parameter set for this description.

## Base Description Parameters

### Filter (`Fbase`)

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Presets | PRESET_OPTIONS_PRESETS | LONG |  |  | 0 | 
Save... | PRESET_OPTIONS_PRESETS_CUSTOM_SAVEBUTTON | BUTTON |  |  |  | 
Delete... | PRESET_OPTIONS_PRESETS_CUSTOM_DELETEBUTTON | BUTTON |  |  |  | 

## All Parameters

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Presets | PRESET_OPTIONS_PRESETS | LONG |  |  | 0 | 
Save... | PRESET_OPTIONS_PRESETS_CUSTOM_SAVEBUTTON | BUTTON |  |  |  | 
Delete... | PRESET_OPTIONS_PRESETS_CUSTOM_DELETEBUTTON | BUTTON |  |  |  | 
Import As | LBWIMPORT_MODE | LONG |  |  |  | LBWIMPORT_MODE_PLANT; LBWIMPORT_MODE_MESH; LBWIMPORT_MODE_FULL
Model | LBWIMPORT_MODEL | LONG |  |  |  | 
Qualifier | LBWIMPORT_QUALIFIER | LONG |  |  |  | 
Leaf Density | LBWIMPORT_LEAFDENSITY | REAL | 0 | 100 |  | 
Use Document Scale | LBWIMPORT_SCALE_DOCSCALE | BOOL |  |  |  | 
Custom Scale | LBWIMPORT_SCALE_CUSTOM | UNITSCALE |  |  |  | 
Subdivision | LBWIMPORT_LOD_SUBDIVISIONTYPE | LONG |  |  |  | LBWIMPORT_LOD_SUBDIVISIONTYPE_LEVEL; LBWIMPORT_LOD_SUBDIVISIONTYPE_UNIFORM
No label | LBWIMPORT_LOD_SUBDIVISION | LONG | 0 | 4 |  | 
Use | LBWIMPORT_LOD_USEMAXLEVEL | BOOL |  |  |  | 
Maximum Branch Depth | LBWIMPORT_LOD_MAXLEVEL | LONG | 0 | 32 |  | 
Use | LBWIMPORT_LOD_USEMINTHICKNESS | BOOL |  |  |  | 
Minimum Branch Thickness | LBWIMPORT_LOD_MINTHICKNESS | REAL | 0 | 10000 |  | 
Leaf Amount | LBWIMPORT_LOD_LEAFAMOUNT | REAL | 0 | 100 |  | 
Type | LBWIMPORT_MATERIAL_TYPE | LONG |  |  |  | LBWIMPORT_MATERIAL_TYPE_CURRENT; LBWIMPORT_MATERIAL_TYPE_STANDARD; LBWIMPORT_MATERIAL_TYPE_VRAY; LBWIMPORT_MATERIAL_TYPE_CORONA; LBWIMPORT_MATERIAL_TYPE_ARNOLD; LBWIMPORT_MATERIAL_TYPE_OCTANE; LBWIMPORT_MATERIAL_TYPE_REDSHIFT; LBWIMPORT_MATERIAL_TYPE_UNIVERSAL
Quality | LBWIMPORT_MATERIAL_QUALITY | LONG |  |  |  | LBWIMPORT_MATERIAL_QUALITY_LOW; LBWIMPORT_MATERIAL_QUALITY_MEDIUM; LBWIMPORT_MATERIAL_QUALITY_HIGH
Layer | LBWIMPORT_MATERIAL_LAYER | LINK |  |  |  | 
