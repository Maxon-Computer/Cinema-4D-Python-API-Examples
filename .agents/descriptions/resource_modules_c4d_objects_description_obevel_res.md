# Description: Bevel Deformer

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/c4d_objects/description/obevel.res`
- **Symbol:** `obevel`
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
Component Mode | O_BEVEL_MODE_COMPONENT_TYPE | LONG |  |  |  | O_BEVEL_MODE_COMPONENT_TYPE_POINT; O_BEVEL_MODE_COMPONENT_TYPE_EDGE; O_BEVEL_MODE_COMPONENT_TYPE_POLYGON
Add | O_BEVEL_RESTRICTION_ADD | BUTTON |  |  |  | 
Remove | O_BEVEL_RESTRICTION_REMOVE | BUTTON |  |  |  | 
Selection | O_BEVEL_RESTRICTION_START | STRING |  |  |  | 
Use Angle | O_BEVEL_MODE_SELECTION_ANGLE_USE | BOOL |  |  |  | 
Angle Threshold | O_BEVEL_MODE_SELECTION_ANGLE_VAL | REAL | 0 |  |  | 
Bevel Mode | O_BEVEL_MASTER_MODE | LONG |  |  |  | O_BEVEL_MASTER_MODE_CHAMFER; O_BEVEL_MASTER_MODE_SOLID
Offset Mode | O_BEVEL_OFFSET_MODE | LONG |  |  |  | O_BEVEL_OFFSET_MODE_FIXED; O_BEVEL_OFFSET_MODE_RADIAL; O_BEVEL_OFFSET_MODE_PROPORTIONAL
Offset | O_BEVEL_RADIUS | REAL |  |  |  | 
Subdivision | O_BEVEL_SUB | REAL | 0 |  |  | 
Depth | O_BEVEL_DEPTH | REAL |  |  |  | 
Depth | O_BEVEL_SHAPING_EXTR | REAL |  |  |  | 
Limit | O_BEVEL_LIMIT | BOOL |  |  |  | 
Extrusion | O_BEVEL_EXTRUSION | REAL |  |  |  | 
Max Angle | O_BEVEL_POLY_ANGLE | REAL | 0 |  |  | 
Preserve Groups | O_BEVEL_GROUP | BOOL |  |  |  | 
Shape | O_BEVEL_SHAPING_MODE | LONG |  |  |  | O_BEVEL_SHAPING_MODE_ROUND; O_BEVEL_SHAPING_MODE_USER; O_BEVEL_SHAPING_MODE_PROFILE
Tension | O_BEVEL_SHAPING_TENSION | REAL |  |  |  | 
User Shape | O_BEVEL_SHAPING_SPLINE | SPLINE |  |  |  | 
Profile Spline | O_BEVEL_SHAPING_SPLINE_LINK | LINK |  |  |  | 
Profile Plane | O_BEVEL_SHAPING_SPLINE_PLANE | LONG |  |  |  | O_BEVEL_SHAPING_SPLINE_PLANE_XY; O_BEVEL_SHAPING_SPLINE_PLANE_XZ; O_BEVEL_SHAPING_SPLINE_PLANE_ZY
Symmetry | O_BEVEL_SHAPING_SYMMETRY | BOOL |  |  |  | 
Constant Cross Section | O_BEVELL_SHAPING_CONSTANT | BOOL |  |  |  | 
Mitering | O_BEVEL_MITERING | LONG |  |  |  | O_BEVEL_MITERING_DEFAULT; O_BEVEL_MITERING_UNIFORM; O_BEVEL_MITERING_RADIAL; O_BEVEL_MITERING_PATCH
Ending | O_BEVEL_CORNER_ENDING | LONG |  |  |  | O_BEVEL_CORNER_ENDING_DEFAULT; O_BEVEL_CORNER_ENDING_EXTEND; O_BEVEL_CORNER_ENDING_INSET
Partial Rounding | O_BEVEL_PROUNDING_TYPE | LONG |  |  |  | O_BEVEL_PROUNDING_TYPE_FLAT; O_BEVEL_PROUNDING_TYPE_FULL; O_BEVEL_PROUNDING_TYPE_CONVEX
Corner N-gons | O_BEVEL_CORNER_NGON | BOOL |  |  |  | 
Rounding N-gons | O_BEVEL_ROUNDING_NGON | BOOL |  |  |  | 
Phong Break Rounding | O_BEVEL_SELECTION_PHONG_BREAK | BOOL |  |  |  | 
Phong Break Miters | O_BEVEL_SELECTION_PHONG_BREAK_M | BOOL |  |  |  | 
