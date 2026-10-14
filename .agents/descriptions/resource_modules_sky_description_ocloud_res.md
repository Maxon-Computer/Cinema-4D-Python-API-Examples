# Description: Cloud

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/sky/description/ocloud.res`
- **Symbol:** `OCloud`
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
Override Group | SKY_CLOUD_OVERRIDE_GROUP | BOOL |  |  |  | 
Active | SKY_CLOUD_GENERATOR_FLAG | BOOL |  |  |  | 
Mix | SKY_CLOUD_MIX | REAL | 0 | 100 |  | 
Altitude | SKY_CLOUD_ALTITUDE | REAL | 0 |  |  | 
Falloff | SKY_CLOUD_FALLOFF | REAL | 0 |  |  | 
Luminance Falloff | SKY_CLOUD_LUM_FALLOFF | REAL | 0 |  |  | 
Transparency Falloff | SKY_CLOUD_TRANS_FALLOFF | REAL | 0 |  |  | 
Color | SKY_CLOUD_COLOR | COLOR |  |  |  | 
High-Quality Lighting | SKY_CLOUD_HQ_LIGHTING | BOOL |  |  |  | 
Falloff | SKY_CLOUD_OBJECT_FALLOFF | SPLINE |  |  |  | 
Distance | SKY_CLOUD_OFFSET_DIST | REAL | 0 |  |  | 
Keep Shape | SKY_CLOUD_KEEP_SHAPE | BOOL |  |  |  | 
Cloud Type | SKY_CLOUD_TYPE | LONG |  |  |  | SKY_CLOUD_TYPE_STANDARD; SKY_CLOUD_TYPE_ACPERL; SKY_CLOUD_TYPE_ACLENTI; SKY_CLOUD_TYPE_CBCAPINC
Coverage | SKY_CLOUD_COVERAGE | REAL | 0 | 100 |  | 
Contrast | SKY_CLOUD_CONTRAST | REAL | 0 | 100 |  | 
Ratio | SKY_CLOUD_SIZE_RATIO | REAL | 0 | 100 |  | 
Groove Depth | SKY_CLOUD_GROOVE_DEPTH | REAL | 0 |  |  | 
Shape Strength | SKY_CLOUD_SHAPE_STRENGTH | REAL | 0 | 100 |  | 
Scale | SKY_CLOUD_SCALE | VECTOR | 1 |  |  | 
Grid Points | SKY_CLOUD_GRID_POINTS | STATICTEXT |  |  |  | 
