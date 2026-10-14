# Description: Alembic

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/io_alembic/description/Oalembicgenerator.res`
- **Symbol:** `Oalembicgenerator`
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
Scale | ALEMBIC_UNIT_SCALE | UNITSCALE |  |  |  | 
SDS Weight Scale | ALEMBIC_SDS_WEIGHT_SCALE | REAL | 0.0 |  |  | 
Path to Alembic File | ALEMBIC_PATH | FILENAME |  |  |  | 
No label | ALEMBIC_PATH_STATE | BOOL |  |  |  | 
Object Identifier | ALEMBIC_IDENTIFIER | STRING |  |  |  | 
No label | ALEMBIC_IDENT_STATE | BOOL |  |  |  | 
Animation | ALEMBIC_STR_ANIMATION | SEPARATOR |  |  |  | 
Use Animation | ALEMBIC_USE_ANIMATION | BOOL |  |  |  | 
Frame | ALEMBIC_ANIMATION_FRAME | BASETIME |  |  |  | 
Interpolation | ALEMBIC_INTERPOLATION | BOOL |  |  |  | 
Offset | ALEMBIC_ANIMATION_OFFSET | BASETIME |  |  |  | 
Mode | ALEMBIC_ANIMATION_MODE | LONG |  |  | ALEMBIC_ANIMATION_MODE_PLAY | ALEMBIC_ANIMATION_MODE_PLAY; ALEMBIC_ANIMATION_MODE_LOOP; ALEMBIC_ANIMATION_MODE_PINGPONG
Speed | ALEMBIC_ANIMATION_SPEED | REAL | 0.0 |  |  | 
Reset | ALEMBIC_ANIMATION_RESET | BUTTON |  |  |  | 
Interpolation | ALEMBIC_POSITION_INTERPOLATION | LONG |  |  | ALEMBIC_POSITION_INTERPOLATION_CUBIC | ALEMBIC_POSITION_INTERPOLATION_LINEAR; ALEMBIC_POSITION_INTERPOLATION_CUBIC; ALEMBIC_POSITION_INTERPOLATION_CUBIC_MONOTONE
Tangent Scale | ALEMBIC_POSITION_INTERPOLATION_CUBIC_WEIGHT | REAL | 0.0 |  |  | 
Remapping Curve | ALEMBIC_ANIMATION_CURVE | SPLINE |  |  |  | 
Rendering | ALEMBIC_STR_RENDERING | SEPARATOR |  |  |  | 
Override Object for Rendering | ALEMBIC_OVERRIDE_FOR_RENDERING | BOOL |  |  |  | 
Use Original Path | ALEMBIC_USE_ORIGINAL_PATH | BOOL |  |  |  | 
Path to Alembic File | ALEMBIC_PATH_FOR_RENDERING | FILENAME |  |  |  | 
No label | ALEMBIC_PATH_STATE_RENDERING | BOOL |  |  |  | 
Object Identifier | ALEMBIC_IDENTIFIER_FOR_RENDERING | STRING |  |  |  | 
No label | ALEMBIC_IDENT_STATE_RENDERING | BOOL |  |  |  | 
Streaming | ALEMBIC_STR_UPDATE | SEPARATOR |  |  |  | 
Update Transform | ALEMBIC_UPDATE_XFORM | BOOL |  |  |  | 
Update Geometry | ALEMBIC_UPDATE_GEOMETRY | BOOL |  |  |  | 
Visibility | ALEMBIC_USE_VISIBILITY | BOOL |  |  |  | 
Normals | ALEMBIC_USE_NORMALS | BOOL |  |  |  | 
UV Set | ALEMBIC_USE_UVS | BOOL |  |  |  | 
Face Sets | ALEMBIC_USE_FACESETS | BOOL |  |  |  | 
Color Maps | ALEMBIC_USE_COLORMAPS | BOOL |  |  |  | 
Creases and Corners | ALEMBIC_USE_SDSWEIGHTS | BOOL |  |  |  | 
Other Attributes | ALEMBIC_USE_OTHERATTR | BOOL |  |  |  | 
Camera Attributes | ALEMBIC_USE_CAMERAPARAMS | BOOL |  |  |  | 
Instance | ALEMBIC_INSTANCE | LONG |  |  | ALEMBIC_INSTANCE_RENDERINSTANCE | ALEMBIC_INSTANCE_NONE; ALEMBIC_INSTANCE_INSTANCE; ALEMBIC_INSTANCE_RENDERINSTANCE
