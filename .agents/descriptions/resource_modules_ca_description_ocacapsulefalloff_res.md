# Description: Falloff Capsule

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/ca/description/ocacapsulefalloff.res`
- **Symbol:** `ocacapsulefalloff`
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
Top | ID_CA_CAPSULEFALLOFF_OBJECT_TOP | REAL | 0.0 |  |  | 
Bottom | ID_CA_CAPSULEFALLOFF_OBJECT_BOTTOM | REAL | 0.0 |  |  | 
