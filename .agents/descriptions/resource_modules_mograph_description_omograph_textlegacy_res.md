# Description: Text

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/mograph/description/omograph_textlegacy.res`
- **Symbol:** `Omograph_textlegacy`
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

### No label (`Onurbscapslegacy`)

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Migrate | CAP_MIGRATE_BUTTON | BUTTON |  |  |  | 
Start Cap | CAP_START | LONG |  |  |  | CAPTYPE_NOCAP; CAPTYPE_CAP; CAPTYPE_ROUNDING; CAPTYPE_ROUNDINGANDCAP
Start Cap Steps | CAP_STARTSTEPS | LONG | 1 | 100 |  | 
Start Cap Radius | CAP_STARTRADIUS | REAL | 0.0 |  |  | 
End Cap | CAP_END | LONG |  |  |  | CAPTYPE_NOCAP; CAPTYPE_CAP; CAPTYPE_ROUNDING; CAPTYPE_ROUNDINGANDCAP
End Cap Steps | CAP_ENDSTEPS | LONG | 1 | 100 |  | 
End Cap Radius | CAP_ENDRADIUS | REAL | 0.0 |  |  | 
Fillet Type | CAP_ROUNDING | LONG |  |  |  | CAP_ROUNDING_LINEAR; CAP_ROUNDING_CONVEX; CAP_ROUNDING_CONCAVE; CAP_ROUNDING_HALFCIRCLE; CAP_ROUNDING_STEP; CAP_ROUNDING_2STEPS; CAP_ROUNDING_ENGRAVED
Phong Angle | CAP_PHONG | REAL | 0.0 | 180.0 |  | 
Hull Inwards | CAP_HULLINWARD | BOOL |  |  |  | 
Hole Inwards | CAP_HOLEINWARD | BOOL |  |  |  | 
Constrain | CAP_CONSTRAIN | BOOL |  |  |  | 
Create Single Object | CAP_CONNECT | BOOL |  |  |  | 
Rounding UVW Keep Shape | CAP_UVWROUDING | BOOL |  |  |  | 
Type | CAP_TYPE | LONG |  |  |  | CAP_TYPE_TRI; CAP_TYPE_QUAD; CAP_TYPE_NGON
Regular Grid | CAP_REGULAR | BOOL |  |  |  | 
Width | CAP_REGULARWIDTH | REAL | 0.01 |  |  | 

### Text Spline Object (`Osplinetext`)

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Text Spline | PRIM_TEXT_TEXT | STRING |  |  |  | 
Font | PRIM_TEXT_FONT | FONT |  |  |  | 
Align | PRIM_TEXT_ALIGN | LONG |  |  |  | PRIM_TEXT_ALIGN_LEFT; PRIM_TEXT_ALIGN_MIDDLE; PRIM_TEXT_ALIGN_RIGHT
Height | PRIM_TEXT_HEIGHT | REAL |  |  |  | 
Horizontal Spacing | PRIM_TEXT_HSPACING | REAL |  |  |  | 
Vertical Spacing | PRIM_TEXT_VSPACING | REAL |  |  |  | 
Separate Letters | PRIM_TEXT_SEPARATE | BOOL |  |  |  | 
Kerning | PRIM_TEXT_KERNING | KERNING |  |  |  | 

### No label (`Osplineprimitive`)

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Plane | PRIM_PLANE | LONG |  |  |  | PRIM_PLANE_XY; PRIM_PLANE_ZY; PRIM_PLANE_XZ
Reverse | PRIM_REVERSE | BOOL |  |  |  | 

### Spline (`Ospline`)

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Type | SPLINEOBJECT_TYPE | LONG |  |  |  | SPLINEOBJECT_TYPE_LINEAR; SPLINEOBJECT_TYPE_CUBIC; SPLINEOBJECT_TYPE_AKIMA; SPLINEOBJECT_TYPE_BSPLINE; SPLINEOBJECT_TYPE_BEZIER
Close Spline | SPLINEOBJECT_CLOSED | BOOL |  |  |  | 
Interpolation | SPLINEOBJECT_INTERPOLATION | LONG |  |  |  | SPLINEOBJECT_INTERPOLATION_NONE; SPLINEOBJECT_INTERPOLATION_NATURAL; SPLINEOBJECT_INTERPOLATION_UNIFORM; SPLINEOBJECT_INTERPOLATION_ADAPTIVE; SPLINEOBJECT_INTERPOLATION_SUBDIV
Points | SPLINEOBJECT_SUB | LONG | 0 | 5000 |  | 
Angle | SPLINEOBJECT_ANGLE | REAL | 0.0 | 90.0 |  | 
Max Length | SPLINEOBJECT_MAXIMUMLENGTH | REAL | 0.01 |  |  | 

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
Migrate | CAP_MIGRATE_BUTTON | BUTTON |  |  |  | 
Start Cap | CAP_START | LONG |  |  |  | CAPTYPE_NOCAP; CAPTYPE_CAP; CAPTYPE_ROUNDING; CAPTYPE_ROUNDINGANDCAP
Start Cap Steps | CAP_STARTSTEPS | LONG | 1 | 100 |  | 
Start Cap Radius | CAP_STARTRADIUS | REAL | 0.0 |  |  | 
End Cap | CAP_END | LONG |  |  |  | CAPTYPE_NOCAP; CAPTYPE_CAP; CAPTYPE_ROUNDING; CAPTYPE_ROUNDINGANDCAP
End Cap Steps | CAP_ENDSTEPS | LONG | 1 | 100 |  | 
End Cap Radius | CAP_ENDRADIUS | REAL | 0.0 |  |  | 
Fillet Type | CAP_ROUNDING | LONG |  |  |  | CAP_ROUNDING_LINEAR; CAP_ROUNDING_CONVEX; CAP_ROUNDING_CONCAVE; CAP_ROUNDING_HALFCIRCLE; CAP_ROUNDING_STEP; CAP_ROUNDING_2STEPS; CAP_ROUNDING_ENGRAVED
Phong Angle | CAP_PHONG | REAL | 0.0 | 180.0 |  | 
Hull Inwards | CAP_HULLINWARD | BOOL |  |  |  | 
Hole Inwards | CAP_HOLEINWARD | BOOL |  |  |  | 
Constrain | CAP_CONSTRAIN | BOOL |  |  |  | 
Create Single Object | CAP_CONNECT | BOOL |  |  |  | 
Rounding UVW Keep Shape | CAP_UVWROUDING | BOOL |  |  |  | 
Type | CAP_TYPE | LONG |  |  |  | CAP_TYPE_TRI; CAP_TYPE_QUAD; CAP_TYPE_NGON
Regular Grid | CAP_REGULAR | BOOL |  |  |  | 
Width | CAP_REGULARWIDTH | REAL | 0.01 |  |  | 
Depth | MGTEXTOBJECT_SPLINEMOVE | REAL |  |  |  | 
Subdivision | MGTEXTOBJECT_SPLINESUB | LONG | 1 |  |  | 
Text Spline | PRIM_TEXT_TEXT | STRING |  |  |  | 
Font | PRIM_TEXT_FONT | FONT |  |  |  | 
Align | PRIM_TEXT_ALIGN | LONG |  |  |  | PRIM_TEXT_ALIGN_LEFT; PRIM_TEXT_ALIGN_MIDDLE; PRIM_TEXT_ALIGN_RIGHT
Height | PRIM_TEXT_HEIGHT | REAL |  |  |  | 
Horizontal Spacing | PRIM_TEXT_HSPACING | REAL |  |  |  | 
Vertical Spacing | PRIM_TEXT_VSPACING | REAL |  |  |  | 
Separate Letters | PRIM_TEXT_SEPARATE | BOOL |  |  |  | 
Kerning | PRIM_TEXT_KERNING | KERNING |  |  |  | 
Plane | PRIM_PLANE | LONG |  |  |  | PRIM_PLANE_XY; PRIM_PLANE_ZY; PRIM_PLANE_XZ
Reverse | PRIM_REVERSE | BOOL |  |  |  | 
Type | SPLINEOBJECT_TYPE | LONG |  |  |  | SPLINEOBJECT_TYPE_LINEAR; SPLINEOBJECT_TYPE_CUBIC; SPLINEOBJECT_TYPE_AKIMA; SPLINEOBJECT_TYPE_BSPLINE; SPLINEOBJECT_TYPE_BEZIER
Close Spline | SPLINEOBJECT_CLOSED | BOOL |  |  |  | 
Interpolation | SPLINEOBJECT_INTERPOLATION | LONG |  |  |  | SPLINEOBJECT_INTERPOLATION_NONE; SPLINEOBJECT_INTERPOLATION_NATURAL; SPLINEOBJECT_INTERPOLATION_UNIFORM; SPLINEOBJECT_INTERPOLATION_ADAPTIVE; SPLINEOBJECT_INTERPOLATION_SUBDIV
Points | SPLINEOBJECT_SUB | LONG | 0 | 5000 |  | 
Angle | SPLINEOBJECT_ANGLE | REAL | 0.0 | 90.0 |  | 
Max Length | SPLINEOBJECT_MAXIMUMLENGTH | REAL | 0.01 |  |  | 
Shader Indexing | MGTEXTOBJECT_INDEXING | LONG |  |  |  | MGTEXTOBJECT_WORDINDEX; MGTEXTOBJECT_LINEINDEX; MGTEXTOBJECT_LETTERINDEX
Effects | MGTEXTOBJECT_EFFECTORLIST_ALL | IN_EXCLUDE |  |  |  | 
Axis | MGTEXTOBJECT_AXIS_ALL | VECTOR | 0.0 | 100.0 |  | 
Effects | MGTEXTOBJECT_EFFECTORLIST_LINE | IN_EXCLUDE |  |  |  | 
Axis | MGTEXTOBJECT_AXIS_LINE | VECTOR | 0.0 | 100.0 |  | 
Align Height | MGTEXTOBJECT_AXIS_LINE_ALIGN | BOOL |  |  |  | 
Effects | MGTEXTOBJECT_EFFECTORLIST_WORD | IN_EXCLUDE |  |  |  | 
Axis | MGTEXTOBJECT_AXIS_WORD | VECTOR | 0.0 | 100.0 |  | 
Align Height | MGTEXTOBJECT_AXIS_WORD_ALIGN | BOOL |  |  |  | 
Effects | MGTEXTOBJECT_EFFECTORLIST_CHAR | IN_EXCLUDE |  |  |  | 
Axis | MGTEXTOBJECT_AXIS_CHAR | VECTOR | 0.0 | 100.0 |  | 
Align Height | MGTEXTOBJECT_AXIS_CHAR_ALIGN | BOOL |  |  |  | 
