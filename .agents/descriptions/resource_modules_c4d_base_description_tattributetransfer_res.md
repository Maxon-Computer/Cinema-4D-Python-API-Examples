# Description: No label

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/c4d_base/description/tattributetransfer.res`
- **Symbol:** `Tattributetransfer`
- **Category:** Other

Use parameter symbols to access parameters and cycle option symbols for cycle values, never their numeric IDs. Treat Min and Max as constraints and Default as the declared initial value; blank cells mean the resource does not declare that metadata, not that the value is zero. Base Description Parameters lists inherited fields from each base; All Parameters lists the effective parameter set for this description.

## Base Description Parameters

No base descriptions.

## All Parameters

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Use Deformed Points | TATTRIBUTETRANSFER_DEFORMED_POINTS | BOOL |  |  |  | 
Source Tag | TATTRIBUTETRANSFER_SOURCE | LINK |  |  |  | 
Evaluation Method | TATTRIBUTETRANSFER_EVAL_METHOD | LONG |  |  |  | TATTRIBUTETRANSFER_EVAL_METHOD_NEAREST_SURFACE; TATTRIBUTETRANSFER_EVAL_METHOD_NEAREST_POINT; TATTRIBUTETRANSFER_EVAL_METHOD_NORMALS_PROJECTION; TATTRIBUTETRANSFER_EVAL_METHOD_SOURCE_AXIS_PROJECTION; TATTRIBUTETRANSFER_EVAL_METHOD_TARGET_AXIS_PROJECTION; TATTRIBUTETRANSFER_EVAL_METHOD_NEAREST_POLYGON_DATA_BREAKS
Transform | TATTRIBUTETRANSFER_TRANSFORM | LONG |  |  |  | TATTRIBUTETRANSFER_TRANSFORM_OFF; TATTRIBUTETRANSFER_TRANSFORM_FLIPX; TATTRIBUTETRANSFER_TRANSFORM_FLIPY; TATTRIBUTETRANSFER_TRANSFORM_FLIPZ
Space | TATTRIBUTETRANSFER_SPACE | LONG |  |  |  | TATTRIBUTETRANSFER_SPACE_LOCAL; TATTRIBUTETRANSFER_SPACE_GLOBAL
