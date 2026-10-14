# Description: ReEffector

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/mograph/description/oereeffector.res`
- **Symbol:** `Oereeffector`
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

### Deformer Panel (`Oedeformer_panel`)

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Deformation | ID_MG_EFFECTORDEFORMER_MODE | LONG |  |  |  | ID_MG_EFFECTORDEFORMER_MODE_OFF; ID_MG_EFFECTORDEFORMER_MODE_OBJECT; ID_MG_EFFECTORDEFORMER_MODE_POINT; ID_MG_EFFECTORDEFORMER_MODE_POLYGON

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
Strength | MGREEFFECTOR_STRENGTH | REAL |  |  |  | 
Selection | MGREEFFECTOR_SELECTION | STRING |  |  |  | 
Effectors | MGREEFFECTOR_EFFECTORS | IN_EXCLUDE |  |  |  | 
Position | MGREEFFECTOR_POSITION | BOOL |  |  |  | 
Position Strength | MGREEFFECTOR_POSITION_STRENGTH | REAL | 0.0 | 100.0 |  | 
Position.X | MGREEFFECTOR_POSITION_X | BOOL |  |  |  | 
Position.X Strength | MGREEFFECTOR_POSITION_STRENGTH_X | REAL | 0.0 | 100.0 |  | 
Position.Y | MGREEFFECTOR_POSITION_Y | BOOL |  |  |  | 
Position.Y Strength | MGREEFFECTOR_POSITION_STRENGTH_Y | REAL | 0.0 | 100.0 |  | 
Position.Z | MGREEFFECTOR_POSITION_Z | BOOL |  |  |  | 
Position.Z Strength | MGREEFFECTOR_POSITION_STRENGTH_Z | REAL | 0.0 | 100.0 |  | 
Rotation | MGREEFFECTOR_ROTATION | BOOL |  |  |  | 
Rotation Strength | MGREEFFECTOR_ROTATION_STRENGTH | REAL | 0.0 | 100.0 |  | 
Rotation.H | MGREEFFECTOR_ROTATION_H | BOOL |  |  |  | 
Rotation.H Strength | MGREEFFECTOR_ROTATION_STRENGTH_H | REAL | 0.0 | 100.0 |  | 
Rotation.P | MGREEFFECTOR_ROTATION_P | BOOL |  |  |  | 
Rotation.P Strength | MGREEFFECTOR_ROTATION_STRENGTH_P | REAL | 0.0 | 100.0 |  | 
Rotation.B | MGREEFFECTOR_ROTATION_B | BOOL |  |  |  | 
Rotation.B Strength | MGREEFFECTOR_ROTATION_STRENGTH_B | REAL | 0.0 | 100.0 |  | 
Scale | MGREEFFECTOR_SCALE | BOOL |  |  |  | 
Scale Strength | MGREEFFECTOR_SCALE_STRENGTH | REAL | 0.0 | 100.0 |  | 
Scale.X | MGREEFFECTOR_SCALE_X | BOOL |  |  |  | 
Scale.X Strength | MGREEFFECTOR_SCALE_STRENGTH_X | REAL | 0.0 | 100.0 |  | 
Scale.Y | MGREEFFECTOR_SCALE_Y | BOOL |  |  |  | 
Scale.Y Strength | MGREEFFECTOR_SCALE_STRENGTH_Y | REAL | 0.0 | 100.0 |  | 
Scale.Z | MGREEFFECTOR_SCALE_Z | BOOL |  |  |  | 
Scale.Z Strength | MGREEFFECTOR_SCALE_STRENGTH_Z | REAL | 0.0 | 100.0 |  | 
Color | MGREEFFECTOR_COLOR | BOOL |  |  |  | 
Color Strength | MGREEFFECTOR_COLOR_STRENGTH | REAL | 0.0 | 100.0 |  | 
Color.R | MGREEFFECTOR_COLOR_R | BOOL |  |  |  | 
Color.R Strength | MGREEFFECTOR_COLOR_STRENGTH_R | REAL | 0.0 | 100.0 |  | 
Color.G | MGREEFFECTOR_COLOR_G | BOOL |  |  |  | 
Color.G Strength | MGREEFFECTOR_COLOR_STRENGTH_G | REAL | 0.0 | 100.0 |  | 
Color.B | MGREEFFECTOR_COLOR_B | BOOL |  |  |  | 
Color.B Strength | MGREEFFECTOR_COLOR_STRENGTH_B | REAL | 0.0 | 100.0 |  | 
Weight | MGREEFFECTOR_WEIGHT | BOOL |  |  |  | 
Weight Strength | MGREEFFECTOR_WEIGHT_STRENGTH | REAL | 0.0 | 100.0 |  | 
Modify Clone | MGREEFFECTOR_CLONE | BOOL |  |  |  | 
Clone Strength | MGREEFFECTOR_CLONE_STRENGTH | REAL | 0.0 | 100.0 |  | 
Time | MGREEFFECTOR_TIME | BOOL |  |  |  | 
Time Strength | MGREEFFECTOR_TIME_STRENGTH | REAL | 0.0 | 100.0 |  | 
U Transform | MGREEFFECTOR_U | BOOL |  |  |  | 
U Strength | MGREEFFECTOR_U_STRENGTH | REAL | 0.0 | 100.0 |  | 
V Transform | MGREEFFECTOR_V | BOOL |  |  |  | 
V Strength | MGREEFFECTOR_V_STRENGTH | REAL | 0.0 | 100.0 |  | 
Visiblity | MGREEFFECTOR_VISIBILITY | BOOL |  |  |  | 
Visibility Strength | MGREEFFECTOR_VISIBILITY_STRENGTH | REAL | 0.0 | 100.0 |  | 
Deformation | ID_MG_EFFECTORDEFORMER_MODE | LONG |  |  |  | ID_MG_EFFECTORDEFORMER_MODE_OFF; ID_MG_EFFECTORDEFORMER_MODE_OBJECT; ID_MG_EFFECTORDEFORMER_MODE_POINT; ID_MG_EFFECTORDEFORMER_MODE_POLYGON
