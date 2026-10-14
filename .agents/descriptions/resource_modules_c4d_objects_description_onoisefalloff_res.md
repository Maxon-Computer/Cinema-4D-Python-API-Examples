# Description: Falloff Noise

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/c4d_objects/description/onoisefalloff.res`
- **Symbol:** `onoisefalloff`
- **Category:** Other

Use parameter symbols to access parameters and cycle option symbols for cycle values, never their numeric IDs. Treat Min and Max as constraints and Default as the declared initial value; blank cells mean the resource does not declare that metadata, not that the value is zero. Base Description Parameters lists inherited fields from each base; All Parameters lists the effective parameter set for this description.

## Base Description Parameters

### Falloff Panel (`Ofalloff_standard`)

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Weight | FALLOFF_STRENGTH | REAL |  |  |  | 
Size | FALLOFF_SIZE | VECTOR |  |  |  | 
Scale | FALLOFF_SCALE | REAL |  |  |  | 
Offset | FALLOFF_SHAPE_OFFSET | VECTOR |  |  |  | 
Orientation | FALLOFF_SHAPE_AXIS | LONG |  |  |  | FALLOFF_SHAPE_AXIS_XP; FALLOFF_SHAPE_AXIS_XN; FALLOFF_SHAPE_AXIS_YP; FALLOFF_SHAPE_AXIS_YN; FALLOFF_SHAPE_AXIS_ZP; FALLOFF_SHAPE_AXIS_ZN
Slice | FALLOFF_SHAPE_SLICE | REAL | 0.0 | 360.0 |  | 
Radius | FALLOFF_SHAPE_TORUS_RADIUS | REAL | 0.0 | 100.0 |  | 
Spherical Falloff | FALLOFF_FUNCTION_SPHERICAL | BOOL |  |  |  | 
Outer Radius | FALLOFF_FUNCTION_RADIUS | REAL | 0.0 |  |  | 
Falloff | FALLOFF_FALLOFF | REAL | 0.0 | 100.0 |  | 
Falloff Function | FALLOFF_FUNCTION | LONG |  |  |  | FALLOFF_FUNCTION_LIN; FALLOFF_FUNCTION_SPLINE; FALLOFF_FUNCTION_INV; FALLOFF_FUNCTION_INVS; FALLOFF_FUNCTION_INVC; FALLOFF_FUNCTION_STEP
Clamped | FALLOFF_CLAMPED | BOOL |  |  |  | 
Spline | FALLOFF_SPLINE | SPLINE |  |  |  | 
Spline Animation Speed | FALLOFF_ANIM_SPEED | REAL | -100 | 100.0 |  | 

### Fields Panel (`Ofalloff_panel`)

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Switch To Field | FALLOFF_SWITCHTOFIELD | BUTTON |  |  |  | 
Field | FIELDS | FIELDLIST |  |  |  | 
Shape | FALLOFF_MODE | LONG |  |  |  | 
Invert | FALLOFF_INVERT | BOOL |  |  |  | 
Visible | FALLOFF_VISIBLE | BOOL |  |  |  | 

## All Parameters

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Switch To Field | FALLOFF_SWITCHTOFIELD | BUTTON |  |  |  | 
Field | FIELDS | FIELDLIST |  |  |  | 
Shape | FALLOFF_MODE | LONG |  |  |  | 
Invert | FALLOFF_INVERT | BOOL |  |  |  | 
Visible | FALLOFF_VISIBLE | BOOL |  |  |  | 
Weight | FALLOFF_STRENGTH | REAL |  |  |  | 
Size | FALLOFF_SIZE | VECTOR |  |  |  | 
Scale | FALLOFF_SCALE | REAL |  |  |  | 
Offset | FALLOFF_SHAPE_OFFSET | VECTOR |  |  |  | 
Orientation | FALLOFF_SHAPE_AXIS | LONG |  |  |  | FALLOFF_SHAPE_AXIS_XP; FALLOFF_SHAPE_AXIS_XN; FALLOFF_SHAPE_AXIS_YP; FALLOFF_SHAPE_AXIS_YN; FALLOFF_SHAPE_AXIS_ZP; FALLOFF_SHAPE_AXIS_ZN
Slice | FALLOFF_SHAPE_SLICE | REAL | 0.0 | 360.0 |  | 
Radius | FALLOFF_SHAPE_TORUS_RADIUS | REAL | 0.0 | 100.0 |  | 
Spherical Falloff | FALLOFF_FUNCTION_SPHERICAL | BOOL |  |  |  | 
Outer Radius | FALLOFF_FUNCTION_RADIUS | REAL | 0.0 |  |  | 
Falloff | FALLOFF_FALLOFF | REAL | 0.0 | 100.0 |  | 
Falloff Function | FALLOFF_FUNCTION | LONG |  |  |  | FALLOFF_FUNCTION_LIN; FALLOFF_FUNCTION_SPLINE; FALLOFF_FUNCTION_INV; FALLOFF_FUNCTION_INVS; FALLOFF_FUNCTION_INVC; FALLOFF_FUNCTION_STEP
Clamped | FALLOFF_CLAMPED | BOOL |  |  |  | 
Spline | FALLOFF_SPLINE | SPLINE |  |  |  | 
Spline Animation Speed | FALLOFF_ANIM_SPEED | REAL | -100 | 100.0 |  | 
Noise Type | ID_NOISEFALLOFF_NOISE_TYPE | LONG |  |  |  | ID_NOISEFALLOFF_NOISE_TYPE_BOX; ID_NOISEFALLOFF_NOISE_TYPE_BLISTEREDTURBULENCE; ID_NOISEFALLOFF_NOISE_TYPE_BUYA; ID_NOISEFALLOFF_NOISE_TYPE_CELL; ID_NOISEFALLOFF_NOISE_TYPE_CRANAL; ID_NOISEFALLOFF_NOISE_TYPE_DENTS; ID_NOISEFALLOFF_NOISE_TYPE_DISPLACEDTURBULENCE; ID_NOISEFALLOFF_NOISE_TYPE_ELECTRIC; ID_NOISEFALLOFF_NOISE_TYPE_FBM; ID_NOISEFALLOFF_NOISE_TYPE_GASEOUS; ID_NOISEFALLOFF_NOISE_TYPE_HAMA; ID_NOISEFALLOFF_NOISE_TYPE_LUKA; ID_NOISEFALLOFF_NOISE_TYPE_MODNOISE; ID_NOISEFALLOFF_NOISE_TYPE_NAKI; ID_NOISEFALLOFF_NOISE_TYPE_NUTOUS; ID_NOISEFALLOFF_NOISE_TYPE_OBER; ID_NOISEFALLOFF_NOISE_TYPE_PEZO; ID_NOISEFALLOFF_NOISE_TYPE_POXO; ID_NOISEFALLOFF_NOISE_TYPE_SEMA; ID_NOISEFALLOFF_NOISE_TYPE_STUPL; ID_NOISEFALLOFF_NOISE_TYPE_TURBULENCE; ID_NOISEFALLOFF_NOISE_TYPE_VLNOISE; ID_NOISEFALLOFF_NOISE_TYPE_WAVYTURBULENCE; ID_NOISEFALLOFF_NOISE_TYPE_CELLVORONOI; ID_NOISEFALLOFF_NOISE_TYPE_DISPLACEDVORONOI; ID_NOISEFALLOFF_NOISE_TYPE_VORONOI1; ID_NOISEFALLOFF_NOISE_TYPE_VORONOI2; ID_NOISEFALLOFF_NOISE_TYPE_VORONOI3; ID_NOISEFALLOFF_NOISE_TYPE_ZADA; ID_NOISEFALLOFF_NOISE_TYPE_PERLIN; ID_NOISEFALLOFF_NOISE_TYPE_RIDGEDMULTIFRACTAL
Seed | ID_NOISEFALLOFF_NOISE_SEED | LONG | 0 |  |  | 
Global Scale | ID_NOISEFALLOFF_SCALE_GLOBAL | REAL | 0.01 |  |  | 
Relative Scale | ID_NOISEFALLOFF_SCALE_LOCAL | VECTOR | 0.01 |  |  | 
Animation Speed | ID_NOISEFALLOFF_NOISE_ANIMATIONSPEED | REAL | 0.0 |  |  | 
Low Clip | ID_NOISEFALLOFF_NOISE_LOW_CLIP | REAL | 0.0 | 100.0 |  | 
High Clip | ID_NOISEFALLOFF_NOISE_HIGH_CLIP | REAL | 0.0 | 100.0 |  | 
Show X | ID_NOISEFALLOFF_VIEWPLANES_ACTIVEX | BOOL |  |  |  | 
Y | ID_NOISEFALLOFF_VIEWPLANES_ACTIVEY | BOOL |  |  |  | 
Z | ID_NOISEFALLOFF_VIEWPLANES_ACTIVEZ | BOOL |  |  |  | 
Display Box | ID_NOISEFALLOFF_VIEWPLANES | VECTOR |  |  |  | 
Plane Resolution | ID_NOISEFALLOFF_VIEWDENSITY | LONG | 0 | 500 |  | 
