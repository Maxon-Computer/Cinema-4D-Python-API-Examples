# Description: Feathers

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/hair/description/ohairfeather.res`
- **Symbol:** `Ohairfeather`
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
Show in Viewport | FEATHER_OBJECT_SHOW_EDITOR | BOOL |  |  |  | 
Viewport LOD | FEATHER_OBJECT_EDITOR_LOD | REAL | 0.0 | 100.0 |  | 
Generate | FEATHER_OBJECT_GENERATE | LONG |  |  |  | FEATHER_OBJECT_GENERATE_HAIR; FEATHER_OBJECT_GENERATE_SPLINES
Reverse | FEATHER_OBJECT_REVERSE | BOOL |  |  |  | 
Segments | FEATHER_OBJECT_SEGMENTS | LONG | 1 | 1024 |  | 
Spacing | FEATHER_OBJECT_SPACING | LONG |  |  |  | FEATHER_OBJECT_SPACING_COUNT; FEATHER_OBJECT_SPACING_SPACE
Relative Size | FEATHER_OBJECT_RELATIVE | BOOL |  |  |  | 
Rachis Length | FEATHER_OBJECT_REFERENCE | REAL | 0.0 |  |  | 
Rachis Radius | FEATHER_OBJECT_RACHIS_RADIUS_BASE | REAL | 0.0 |  |  | 
Top | FEATHER_OBJECT_RACHIS_RADIUS_TOP | REAL | 0.0 |  |  | 
Start | FEATHER_OBJECT_BARB_START | REAL | 0.0 | 100.0 |  | 
End | FEATHER_OBJECT_BARB_END | REAL | 0.0 | 100.0 |  | 
Barb Spacing | FEATHER_OBJECT_BARB_SPACING | REAL | 0.0 |  |  | 
Variation | FEATHER_OBJECT_BARB_SPACING_VAR | REAL | 0.0 |  |  | 
Barb Count | FEATHER_OBJECT_BARB_COUNT | LONG | 1 |  |  | 
Barb Length | FEATHER_OBJECT_BARB_LENGTH | REAL | 0.0 |  |  | 
Variation | FEATHER_OBJECT_BARB_LENGTH_VAR | REAL | 0.0 |  |  | 
Curve (Top) | FEATHER_OBJECT_BARB_Y_DISP_T | REAL | 0.0 |  |  | 
Variation | FEATHER_OBJECT_BARB_Y_DISP_T_VAR | REAL | 0.0 |  |  | 
Curve (Base) | FEATHER_OBJECT_BARB_Y_DISP | REAL | 0.0 |  |  | 
Variation | FEATHER_OBJECT_BARB_Y_DISP_VAR | REAL | 0.0 |  |  | 
Displace | FEATHER_OBJECT_BARB_Z_DISP | REAL | 0.0 |  |  | 
Variation | FEATHER_OBJECT_BARB_Z_DISP_VAR | REAL | 0.0 |  |  | 
Rot Step | FEATHER_OBJECT_RACHIS_ROTATION_DELTA | REAL |  |  |  | 
Variation | FEATHER_OBJECT_RACHIS_ROTATION_DELTA_VAR | REAL |  |  |  | 
Rotation | FEATHER_OBJECT_RACHIS_ROTATION | REAL |  |  |  | 
Variation | FEATHER_OBJECT_RACHIS_ROTATION_VAR | REAL | 0.0 |  |  | 
Rachis Rot | FEATHER_OBJECT_BARB_ROTATION_Y_VAR | REAL | 0.0 |  |  | 
Barb Rot | FEATHER_OBJECT_BARB_ROTATION_Z_VAR | REAL | 0.0 |  |  | 
Gap | FEATHER_OBJECT_BARB_GAPS | REAL | 0.0 |  |  | 
Variation | FEATHER_OBJECT_BARB_GAPS_VAR | REAL | 0.0 |  |  | 
Occurrence | FEATHER_OBJECT_BARB_GAPS_OCCUR | REAL | 0.0 | 100.0 |  | 
Left | FEATHER_OBJECT_RACHIS_LEFT | SPLINE |  |  |  | 
Right | FEATHER_OBJECT_RACHIS_RIGHT | SPLINE |  |  |  | 
Left | FEATHER_OBJECT_RACHIS_SECTION_LEFT | SPLINE |  |  |  | 
Right | FEATHER_OBJECT_RACHIS_SECTION_RIGHT | SPLINE |  |  |  | 
Left | FEATHER_OBJECT_RACHIS_CURVE_LEFT | SPLINE |  |  |  | 
Right | FEATHER_OBJECT_RACHIS_CURVE_RIGHT | SPLINE |  |  |  | 
