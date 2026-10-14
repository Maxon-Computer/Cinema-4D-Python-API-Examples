# Description: Turn

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/c4d_simulation/description/ofpturn.res`
- **Symbol:** `ofpturn`
- **Category:** Objects

Use parameter symbols to access parameters and cycle option symbols for cycle values, never their numeric IDs. Treat Min and Max as constraints and Default as the declared initial value; blank cells mean the resource does not declare that metadata, not that the value is zero. Base Description Parameters lists inherited fields from each base; All Parameters lists the effective parameter set for this description.

## Base Description Parameters

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
Mix | FP_TURN_MIX | REAL | 0.0 | 100.0 | 0.0 | 
Mode | FP_TURN_MODE | LONG |  |  |  | FP_TURN_MODE_SET; FP_TURN_MODE_TURN
Angle | FP_TURN_TURN_ANGLE | REAL |  |  |  | 
No label | FP_TURN_TURN_RATE_UNIT | LONG |  |  |  | FP_TURN_TURN_RATE_UNIT_PERFRAME; FP_TURN_TURN_RATE_UNIT_PERSECOND
Direction | FP_TURN_DIRECTION | LONG |  |  | FP_TURN_DIRECTION_AXIS | FP_TURN_DIRECTION_AXIS; FP_TURN_DIRECTION_RANDOM; FP_TURN_DIRECTION_VECTOR; FP_TURN_DIRECTION_OBJECT
Axis | FP_TURN_AXIS | LONG |  |  | FP_TURN_AXIS_POSZ | FP_TURN_AXIS_POSX; FP_TURN_AXIS_NEGX; FP_TURN_AXIS_POSY; FP_TURN_AXIS_NEGY; FP_TURN_AXIS_POSZ; FP_TURN_AXIS_NEGZ
Vector | FP_TURN_VECTOR | VECTOR |  |  |  | 
Object | FP_TURN_OBJECT_LINK | LINK |  |  |  | 
Vector Space | FP_TURN_SPACE | LONG |  |  | FP_TURN_SPACE_ALIGNMENT | FP_TURN_SPACE_ALIGNMENT; FP_TURN_SPACE_GLOBAL
Spread | FP_TURN_FOV | REAL | 0 | 360 | 0 | 
Spread Falloff | FP_TURN_FOVFALLOFF | REAL | 0.0 | 100.0 | 0.0 | 
Seed | FP_TURN_SEED | LONG | 0 |  | 12345 | 
