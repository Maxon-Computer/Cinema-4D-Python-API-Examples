# Description: Noise

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/c4d_simulation/description/onoise.res`
- **Symbol:** `onoise`
- **Category:** Other

Use parameter symbols to access parameters and cycle option symbols for cycle values, never their numeric IDs. Treat Min and Max as constraints and Default as the declared initial value; blank cells mean the resource does not declare that metadata, not that the value is zero. Base Description Parameters lists inherited fields from each base; All Parameters lists the effective parameter set for this description.

## Base Description Parameters

No base descriptions.

## All Parameters

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Noise Enabled | NOISE_OBJECT_NOISE_ENABLED | BOOL |  |  |  | 
Seed | NOISE_OBJECT_NOISE_SCALE_SEED | LONG |  |  |  | 
Noise Type | NOISE_OBJECT_NOISE_MODE | LONG |  |  |  | NOISE_OBJECT_NOISE_MODE_BOX; NOISE_OBJECT_NOISE_MODE_BLISTEREDTURBULENCE; NOISE_OBJECT_NOISE_MODE_BUYA; NOISE_OBJECT_NOISE_MODE_CELL; NOISE_OBJECT_NOISE_MODE_CRANAL; NOISE_OBJECT_NOISE_MODE_DENTS; NOISE_OBJECT_NOISE_MODE_DISPLACEDTURBULENCE; NOISE_OBJECT_NOISE_MODE_ELECTRIC; NOISE_OBJECT_NOISE_MODE_GASEOUS; NOISE_OBJECT_NOISE_MODE_HAMA; NOISE_OBJECT_NOISE_MODE_LUKA; NOISE_OBJECT_NOISE_MODE_MOD; NOISE_OBJECT_NOISE_MODE_NAKI; NOISE_OBJECT_NOISE_MODE_NUTOUS; NOISE_OBJECT_NOISE_MODE_OBER; NOISE_OBJECT_NOISE_MODE_PERLIN; NOISE_OBJECT_NOISE_MODE_PEZO; NOISE_OBJECT_NOISE_MODE_POXO; NOISE_OBJECT_NOISE_MODE_SEMA; NOISE_OBJECT_NOISE_MODE_STUPL; NOISE_OBJECT_NOISE_MODE_TURBULENCE; NOISE_OBJECT_NOISE_MODE_VL; NOISE_OBJECT_NOISE_MODE_WAVYTURBULENCE; NOISE_OBJECT_NOISE_MODE_ZADA
Noise Space | NOISE_OBJECT_NOISE_SPACE | LONG |  |  |  | NOISE_OBJECT_NOISE_SPACE_LOCAL; NOISE_OBJECT_NOISE_SPACE_GLOBAL
Octaves | NOISE_OBJECT_NOISE_OCTAVES | REAL | 1.0 | 20.0 |  | 
Relative Scale | NOISE_OBJECT_NOISE_GLOBAL_SCALE | VECTOR |  |  |  | 
Scale | NOISE_OBJECT_NOISE_SCALE | REAL |  |  |  | 
Animation Speed | NOISE_OBJECT_NOISE_FREQUENCY | REAL |  |  |  | 
Loop Period | NOISE_OBJECT_NOISE_LOOP_PERIOD | REAL | 0.0 |  |  | 
Uniform per Channel | NOISE_OBJECT_NOISE_UNIFORM | BOOL |  |  |  | 
Movement | NOISE_OBJECT_NOISE_MOVEMENT | VECTOR |  |  |  | 
Speed | NOISE_OBJECT_NOISE_SPEED | REAL |  |  |  | 
Low Clip | NOISE_OBJECT_NOISE_MIN | REAL | 0.0 | 100.0 |  | 
High Clip | NOISE_OBJECT_NOISE_MAX | REAL | 0.0 | 100.0 |  | 
Brightness | NOISE_OBJECT_NOISE_BRIGHTNESS | REAL | -100.0 | 100.0 |  | 
Contrast | NOISE_OBJECT_NOISE_CONTRAST | REAL | -100.0 | 100.0 |  | 
