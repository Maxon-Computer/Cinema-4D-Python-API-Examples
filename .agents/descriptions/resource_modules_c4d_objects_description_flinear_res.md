# Description: Linear Field

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/c4d_objects/description/flinear.res`
- **Symbol:** `Flinear`
- **Category:** Objects

Use parameter symbols to access parameters and cycle option symbols for cycle values, never their numeric IDs. Treat Min and Max as constraints and Default as the declared initial value; blank cells mean the resource does not declare that metadata, not that the value is zero. Base Description Parameters lists inherited fields from each base; All Parameters lists the effective parameter set for this description.

## Base Description Parameters

### Field (`Ofield`)

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Type | FIELD_TYPE | LONG |  |  |  | 

### Base Object (`Obase`)

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Icon Color | ID_BASELIST_ICON_COLORIZE_MODE | LONG |  |  |  | ID_BASELIST_ICON_COLORIZE_MODE_NONE; ID_BASELIST_ICON_COLORIZE_MODE_DISPLAYCOLOR; ID_BASELIST_ICON_COLORIZE_MODE_CUSTOM
Viewport Visibility | ID_BASEOBJECT_VISIBILITY_EDITOR | LONG |  |  |  | OBJECT_UNDEF; OBJECT_ON; OBJECT_OFF
Renderer Visibility | ID_BASEOBJECT_VISIBILITY_RENDER | LONG |  |  |  | OBJECT_UNDEF; OBJECT_ON; OBJECT_OFF
Enabled | ID_BASEOBJECT_GENERATOR_FLAG | BOOL |  |  |  | 
Display Color | ID_BASEOBJECT_USECOLOR | LONG |  |  |  | ID_BASEOBJECT_USECOLOR_OFF; ID_BASEOBJECT_USECOLOR_LAYER; ID_BASEOBJECT_USECOLOR_AUTOMATIC; ID_BASEOBJECT_USECOLOR_ALWAYS
Color | ID_BASEOBJECT_COLOR | COLOR |  |  |  | 
X-Ray | ID_BASEOBJECT_XRAY | BOOL |  |  |  | 
Position | ID_BASEOBJECT_REL_POSITION | VECTOR |  |  |  | 
Rotation | ID_BASEOBJECT_REL_ROTATION | VECTOR |  |  |  | 
Scale | ID_BASEOBJECT_REL_SCALE | VECTOR |  |  |  | 
Rotation Order | ID_BASEOBJECT_ROTATION_ORDER | LONG |  |  |  | ID_BASEOBJECT_ROTATION_ORDER_HPB; ID_BASEOBJECT_ROTATION_ORDER_XYZ; ID_BASEOBJECT_ROTATION_ORDER_XZY; ID_BASEOBJECT_ROTATION_ORDER_YXZ; ID_BASEOBJECT_ROTATION_ORDER_YZX; ID_BASEOBJECT_ROTATION_ORDER_ZXY; ID_BASEOBJECT_ROTATION_ORDER_ZYX
Quaternion Rotation | ID_BASEOBJECT_QUATERNION_ROTATION_INTERPOLATION | BOOL |  |  |  | 
Freeze All | ID_BASEOBJECT_FREEZE | BUTTON |  |  |  | 
Unfreeze All | ID_BASEOBJECT_FROZEN_RESET | BUTTON |  |  |  | 
Frozen Position | ID_BASEOBJECT_FROZEN_POSITION | VECTOR |  |  |  | 
Freeze P | ID_BASEOBJECT_FREEZE_P | BUTTON |  |  |  | 
Frozen Rotation | ID_BASEOBJECT_FROZEN_ROTATION | VECTOR |  |  |  | 
Freeze R | ID_BASEOBJECT_FREEZE_R | BUTTON |  |  |  | 
Frozen Scale | ID_BASEOBJECT_FROZEN_SCALE | VECTOR |  |  |  | 
Freeze S | ID_BASEOBJECT_FREEZE_S | BUTTON |  |  |  | 
Deform Position | ID_BASEOBJECT_DEFORM_POSITION | VECTOR |  |  |  | 
Deform Rotation | ID_BASEOBJECT_DEFORM_ROTATION | VECTOR |  |  |  | 
Deform Scale | ID_BASEOBJECT_DEFORM_SCALE | VECTOR |  |  |  | 
Global Position | ID_BASEOBJECT_GLOBAL_POSITION | VECTOR |  |  |  | 
Global Rotation | ID_BASEOBJECT_GLOBAL_ROTATION | VECTOR |  |  |  | 
Transformed Position | ID_BASEOBJECT_ABS_POSITION | VECTOR |  |  |  | 
Transformed Scale | ID_BASEOBJECT_ABS_SCALE | VECTOR |  |  |  | 
Transformed Rotation | ID_BASEOBJECT_ABS_ROTATION | VECTOR |  |  |  | 

### Basic Properties (`Obaselist`)

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Icon File / ID | ID_BASELIST_ICON_FILE | TEXTURE |  |  |  | 
Icon Color | ID_BASELIST_ICON_COLORIZE_MODE | BOOL |  |  |  | 
Color | ID_BASELIST_ICON_COLOR | COLOR |  |  | 1.0 0.9 0.4 | 
No label | ID_BASELIST_ICON_PRESET_BUTTONS | ICONCHOOSER |  |  |  | 
Name | ID_BASELIST_NAME | STRING |  |  |  | 
Layer | ID_LAYER_LINK | LINK |  |  |  | 
No label | ID_BASELIST_NODESPACE_ADD_REMOVE_BUTTONS | NODESPACE_ADD_REMOVE |  |  |  | 

### Field Remapper (`Fieldremapper`)

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Enable Remapping | FIELD_REMAP_ENABLE | BOOL |  |  |  | 
Mirror Graph | FIELD_REMAP_MIRROR | BOOL |  |  |  | 
No label | FIELD_PREVIEW | BITMAPBUTTON |  |  |  | 
Strength | FIELD_STRENGTH | REAL |  |  |  | 
Invert | FIELD_INVERT | BOOL |  |  |  | 
Inner Offset | FIELD_INNER_OFFSET | REAL | 0.0 | 100.0 |  | 
Min | FIELD_MIN | REAL |  |  |  | 
Clamp Min | FIELD_CLAMP_MIN | BOOL |  |  |  | 
Max | FIELD_MAX | REAL |  |  |  | 
Clamp Max | FIELD_CLAMP_MAX | BOOL |  |  |  | 
Multiplier | FIELD_MULTIPLIER | REAL |  |  |  | 
Contour Mode | FIELD_CONTOUR_MODE | LONG |  |  |  | FIELD_CONTOUR_MODE_NONE; FIELD_CONTOUR_MODE_QUAD; FIELD_CONTOUR_MODE_STEP; FIELD_CONTOUR_MODE_QUANTIZE; FIELD_CONTOUR_MODE_CURVE
Curve | FIELD_CONTOUR_CURVE | REAL | -100.0 | 100.0 |  | 
Steps | FIELD_CONTOUR_STEPS | LONG | 1 |  |  | 
Spline | FIELD_CONTOUR_SPLINE | SPLINE |  |  |  | 
Spline Animation Speed | FIELD_CONTOUR_ANIMATION_SPEED | BASETIME |  |  |  | 
Spline Offset | FIELD_CONTOUR_SPLINE_OFFSET | REAL |  |  |  | 
Spline Range | FIELD_CONTOUR_SPLINE_RANGE | REAL |  |  |  | 
Color Mode | FIELD_COLOR_MODE | LONG |  |  |  | FIELD_COLOR_MODE_OFF; FIELD_COLOR_MODE_COLOR; FIELD_COLOR_MODE_GRADIENT
Color | FIELD_COLOR | COLOR |  |  |  | 
Gradient | FIELD_GRADIENT | GRADIENT |  |  |  | 
Length | FIELD_DIRECTIONMODE | LONG |  |  |  | FIELD_DIRECTIONMODE_OFF; FIELD_DIRECTIONMODE_NORMALIZE; FIELD_DIRECTIONMODE_ATTENUATE; FIELD_DIRECTIONMODE_INVERSESQUARE
Scale | FIELD_DIRECTIONSCALE | REAL |  |  |  | 
Invert Direction | FIELD_DIRECTIONINVERT | BOOL |  |  |  | 
Strength | FIELD_ROTATIONMODE | LONG |  |  |  | FIELD_ROTATIONMODE_OFF; FIELD_ROTATIONMODE_NORMALIZE; FIELD_ROTATIONMODE_REMAP; FIELD_ROTATIONMODE_ATTENUATE; FIELD_ROTATIONMODE_INVERSESQUARE
Scale | FIELD_ROTATIONSCALE | REAL |  |  |  | 
Invert Rotations | FIELD_ROTATIONINVERT | BOOL |  |  |  | 

## All Parameters

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Icon File / ID | ID_BASELIST_ICON_FILE | TEXTURE |  |  |  | 
Color | ID_BASELIST_ICON_COLOR | COLOR |  |  | 1.0 0.9 0.4 | 
No label | ID_BASELIST_ICON_PRESET_BUTTONS | ICONCHOOSER |  |  |  | 
Name | ID_BASELIST_NAME | STRING |  |  |  | 
Layer | ID_LAYER_LINK | LINK |  |  |  | 
No label | ID_BASELIST_NODESPACE_ADD_REMOVE_BUTTONS | NODESPACE_ADD_REMOVE |  |  |  | 
Icon Color | ID_BASELIST_ICON_COLORIZE_MODE | LONG |  |  |  | ID_BASELIST_ICON_COLORIZE_MODE_NONE; ID_BASELIST_ICON_COLORIZE_MODE_DISPLAYCOLOR; ID_BASELIST_ICON_COLORIZE_MODE_CUSTOM
Viewport Visibility | ID_BASEOBJECT_VISIBILITY_EDITOR | LONG |  |  |  | OBJECT_UNDEF; OBJECT_ON; OBJECT_OFF
Renderer Visibility | ID_BASEOBJECT_VISIBILITY_RENDER | LONG |  |  |  | OBJECT_UNDEF; OBJECT_ON; OBJECT_OFF
Enabled | ID_BASEOBJECT_GENERATOR_FLAG | BOOL |  |  |  | 
Display Color | ID_BASEOBJECT_USECOLOR | LONG |  |  |  | ID_BASEOBJECT_USECOLOR_OFF; ID_BASEOBJECT_USECOLOR_LAYER; ID_BASEOBJECT_USECOLOR_AUTOMATIC; ID_BASEOBJECT_USECOLOR_ALWAYS
Color | ID_BASEOBJECT_COLOR | COLOR |  |  |  | 
X-Ray | ID_BASEOBJECT_XRAY | BOOL |  |  |  | 
Position | ID_BASEOBJECT_REL_POSITION | VECTOR |  |  |  | 
Rotation | ID_BASEOBJECT_REL_ROTATION | VECTOR |  |  |  | 
Scale | ID_BASEOBJECT_REL_SCALE | VECTOR |  |  |  | 
Rotation Order | ID_BASEOBJECT_ROTATION_ORDER | LONG |  |  |  | ID_BASEOBJECT_ROTATION_ORDER_HPB; ID_BASEOBJECT_ROTATION_ORDER_XYZ; ID_BASEOBJECT_ROTATION_ORDER_XZY; ID_BASEOBJECT_ROTATION_ORDER_YXZ; ID_BASEOBJECT_ROTATION_ORDER_YZX; ID_BASEOBJECT_ROTATION_ORDER_ZXY; ID_BASEOBJECT_ROTATION_ORDER_ZYX
Quaternion Rotation | ID_BASEOBJECT_QUATERNION_ROTATION_INTERPOLATION | BOOL |  |  |  | 
Freeze All | ID_BASEOBJECT_FREEZE | BUTTON |  |  |  | 
Unfreeze All | ID_BASEOBJECT_FROZEN_RESET | BUTTON |  |  |  | 
Frozen Position | ID_BASEOBJECT_FROZEN_POSITION | VECTOR |  |  |  | 
Freeze P | ID_BASEOBJECT_FREEZE_P | BUTTON |  |  |  | 
Frozen Rotation | ID_BASEOBJECT_FROZEN_ROTATION | VECTOR |  |  |  | 
Freeze R | ID_BASEOBJECT_FREEZE_R | BUTTON |  |  |  | 
Frozen Scale | ID_BASEOBJECT_FROZEN_SCALE | VECTOR |  |  |  | 
Freeze S | ID_BASEOBJECT_FREEZE_S | BUTTON |  |  |  | 
Deform Position | ID_BASEOBJECT_DEFORM_POSITION | VECTOR |  |  |  | 
Deform Rotation | ID_BASEOBJECT_DEFORM_ROTATION | VECTOR |  |  |  | 
Deform Scale | ID_BASEOBJECT_DEFORM_SCALE | VECTOR |  |  |  | 
Global Position | ID_BASEOBJECT_GLOBAL_POSITION | VECTOR |  |  |  | 
Global Rotation | ID_BASEOBJECT_GLOBAL_ROTATION | VECTOR |  |  |  | 
Transformed Position | ID_BASEOBJECT_ABS_POSITION | VECTOR |  |  |  | 
Transformed Scale | ID_BASEOBJECT_ABS_SCALE | VECTOR |  |  |  | 
Transformed Rotation | ID_BASEOBJECT_ABS_ROTATION | VECTOR |  |  |  | 
Type | FIELD_TYPE | LONG |  |  |  | 
Enable Remapping | FIELD_REMAP_ENABLE | BOOL |  |  |  | 
Mirror Graph | FIELD_REMAP_MIRROR | BOOL |  |  |  | 
No label | FIELD_PREVIEW | BITMAPBUTTON |  |  |  | 
Strength | FIELD_STRENGTH | REAL |  |  |  | 
Invert | FIELD_INVERT | BOOL |  |  |  | 
Inner Offset | FIELD_INNER_OFFSET | REAL | 0.0 | 100.0 |  | 
Min | FIELD_MIN | REAL |  |  |  | 
Clamp Min | FIELD_CLAMP_MIN | BOOL |  |  |  | 
Max | FIELD_MAX | REAL |  |  |  | 
Clamp Max | FIELD_CLAMP_MAX | BOOL |  |  |  | 
Multiplier | FIELD_MULTIPLIER | REAL |  |  |  | 
Contour Mode | FIELD_CONTOUR_MODE | LONG |  |  |  | FIELD_CONTOUR_MODE_NONE; FIELD_CONTOUR_MODE_QUAD; FIELD_CONTOUR_MODE_STEP; FIELD_CONTOUR_MODE_QUANTIZE; FIELD_CONTOUR_MODE_CURVE
Curve | FIELD_CONTOUR_CURVE | REAL | -100.0 | 100.0 |  | 
Steps | FIELD_CONTOUR_STEPS | LONG | 1 |  |  | 
Spline | FIELD_CONTOUR_SPLINE | SPLINE |  |  |  | 
Spline Animation Speed | FIELD_CONTOUR_ANIMATION_SPEED | BASETIME |  |  |  | 
Spline Offset | FIELD_CONTOUR_SPLINE_OFFSET | REAL |  |  |  | 
Spline Range | FIELD_CONTOUR_SPLINE_RANGE | REAL |  |  |  | 
Color Mode | FIELD_COLOR_MODE | LONG |  |  |  | FIELD_COLOR_MODE_OFF; FIELD_COLOR_MODE_COLOR; FIELD_COLOR_MODE_GRADIENT
Color | FIELD_COLOR | COLOR |  |  |  | 
Gradient | FIELD_GRADIENT | GRADIENT |  |  |  | 
Length | FIELD_DIRECTIONMODE | LONG |  |  |  | FIELD_DIRECTIONMODE_OFF; FIELD_DIRECTIONMODE_NORMALIZE; FIELD_DIRECTIONMODE_ATTENUATE; FIELD_DIRECTIONMODE_INVERSESQUARE
Scale | FIELD_DIRECTIONSCALE | REAL |  |  |  | 
Invert Direction | FIELD_DIRECTIONINVERT | BOOL |  |  |  | 
Strength | FIELD_ROTATIONMODE | LONG |  |  |  | FIELD_ROTATIONMODE_OFF; FIELD_ROTATIONMODE_NORMALIZE; FIELD_ROTATIONMODE_REMAP; FIELD_ROTATIONMODE_ATTENUATE; FIELD_ROTATIONMODE_INVERSESQUARE
Scale | FIELD_ROTATIONSCALE | REAL |  |  |  | 
Invert Rotations | FIELD_ROTATIONINVERT | BOOL |  |  |  | 
Length | LINEAR_SIZE | REAL | 0.0 |  |  | 
Direction | LINEAR_DIRECTION | LONG |  |  |  | LINEAR_DIRECTION_XP; LINEAR_DIRECTION_XN; LINEAR_DIRECTION_YP; LINEAR_DIRECTION_YN; LINEAR_DIRECTION_ZP; LINEAR_DIRECTION_ZN
Clip to Shape | LINEAR_CLIP | BOOL |  |  |  | 
