# Description: Measure Object

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/c4d_objects/description/omeasure.res`
- **Symbol:** `Omeasure`
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

### Measure Tool (`ToolMeasure`)

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Selection | MDATA_MEASURE_SELECTION | LONG |  |  |  | 
Show | MDATA_MEASURE_VISIBLE | BOOL |  |  |  | 
New Measure | MDATA_MEASURE_NEW | BUTTON |  |  |  | 
Delete Measure | MDATA_MEASURE_DELETE | BUTTON |  |  |  | 
Create Object | MDATA_MEASURE_CREATEOBJECT | BUTTON |  |  |  | 
3rd Point | MDATA_MEASURE_3RD_POINT | BOOL |  |  |  | 
Measure Distance 1 | MDATA_MEASURE_SHOWDIST1 | BOOL |  |  |  | 
Distance 1 | MDATA_MEASURE_DIST1 | REAL |  |  |  | 
Revert Direction | MDATA_MEASURE_DIR1 | BOOL |  |  |  | 
Measure Distance 2 | MDATA_MEASURE_SHOWDIST2 | BOOL |  |  |  | 
Distance 2 | MDATA_MEASURE_DIST2 | REAL |  |  |  | 
Revert Direction | MDATA_MEASURE_DIR2 | BOOL |  |  |  | 
Measure Angle | MDATA_MEASURE_SHOWANGLE | BOOL |  |  |  | 
Angle | MDATA_MEASURE_ANGLE | REAL |  |  |  | 
Revert Axis | MDATA_MEASURE_FIXROT | BOOL |  |  |  | 
Colors | MDATA_MEASUREGROUP_COLORS | SEPARATOR |  |  |  | 
Point Color | MDATA_MEASURE_COLORP | COLOR |  |  |  | 
Color 1 | MDATA_MEASURE_COLOR1 | COLOR |  |  |  | 
Color 2 | MDATA_MEASURE_COLOR2 | COLOR |  |  |  | 
Point1 | MDATA_MEASUREGROUP_P1 | SEPARATOR |  |  |  | 
Point 1 Object | MDATA_MEASURE_PNT1_LINK | LINK |  |  |  | 
Point 1 Mode | MDATA_MEASURE_PNT1_MODE | LONG |  |  |  | MDATA_MEASURE_PNT_MODE_FREE; MDATA_MEASURE_PNT_MODE_POINT; MDATA_MEASURE_PNT_MODE_EDGE; MDATA_MEASURE_PNT_MODE_POLY
Point 1 Index | MDATA_MEASURE_PNT1_IDX | LONG |  |  |  | 
Point 1 Position | MDATA_MEASURE_PNT1_VECTOR | VECTOR |  |  |  | 
Point2 | MDATA_MEASUREGROUP_P2 | SEPARATOR |  |  |  | 
Point 2 Object | MDATA_MEASURE_PNT2_LINK | LINK |  |  |  | 
Point 2 Mode | MDATA_MEASURE_PNT2_MODE | LONG |  |  |  | MDATA_MEASURE_PNT_MODE_FREE; MDATA_MEASURE_PNT_MODE_POINT; MDATA_MEASURE_PNT_MODE_EDGE; MDATA_MEASURE_PNT_MODE_POLY
Point 2 Index | MDATA_MEASURE_PNT2_IDX | LONG |  |  |  | 
Point 2 Position | MDATA_MEASURE_PNT2_VECTOR | VECTOR |  |  |  | 
Point3 | MDATA_MEASUREGROUP_P3 | SEPARATOR |  |  |  | 
Point 3 Object | MDATA_MEASURE_PNT3_LINK | LINK |  |  |  | 
Point 3 Mode | MDATA_MEASURE_PNT3_MODE | LONG |  |  |  | MDATA_MEASURE_PNT_MODE_FREE; MDATA_MEASURE_PNT_MODE_POINT; MDATA_MEASURE_PNT_MODE_EDGE; MDATA_MEASURE_PNT_MODE_POLY
Point 3 Index | MDATA_MEASURE_PNT3_IDX | LONG |  |  |  | 
Point 3 Position | MDATA_MEASURE_PNT3_VECTOR | VECTOR |  |  |  | 

### Base Tool (`ToolBase`)

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Realtime Update | MDATA_INTERACTIVE | BOOL |  |  |  | 
    Apply     | MDATA_APPLY | BUTTON |  |  |  | 
New Transform | MDATA_NEWTRANSFORM | BUTTON |  |  |  | 
No label | ID_SNAPSETTINGS | SUBCONTAINER |  |  |  | 

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
Realtime Update | MDATA_INTERACTIVE | BOOL |  |  |  | 
    Apply     | MDATA_APPLY | BUTTON |  |  |  | 
New Transform | MDATA_NEWTRANSFORM | BUTTON |  |  |  | 
No label | ID_SNAPSETTINGS | SUBCONTAINER |  |  |  | 
Selection | MDATA_MEASURE_SELECTION | LONG |  |  |  | 
Show | MDATA_MEASURE_VISIBLE | BOOL |  |  |  | 
New Measure | MDATA_MEASURE_NEW | BUTTON |  |  |  | 
Delete Measure | MDATA_MEASURE_DELETE | BUTTON |  |  |  | 
Create Object | MDATA_MEASURE_CREATEOBJECT | BUTTON |  |  |  | 
3rd Point | MDATA_MEASURE_3RD_POINT | BOOL |  |  |  | 
Measure Distance 1 | MDATA_MEASURE_SHOWDIST1 | BOOL |  |  |  | 
Distance 1 | MDATA_MEASURE_DIST1 | REAL |  |  |  | 
Revert Direction | MDATA_MEASURE_DIR1 | BOOL |  |  |  | 
Measure Distance 2 | MDATA_MEASURE_SHOWDIST2 | BOOL |  |  |  | 
Distance 2 | MDATA_MEASURE_DIST2 | REAL |  |  |  | 
Revert Direction | MDATA_MEASURE_DIR2 | BOOL |  |  |  | 
Measure Angle | MDATA_MEASURE_SHOWANGLE | BOOL |  |  |  | 
Angle | MDATA_MEASURE_ANGLE | REAL |  |  |  | 
Revert Axis | MDATA_MEASURE_FIXROT | BOOL |  |  |  | 
Colors | MDATA_MEASUREGROUP_COLORS | SEPARATOR |  |  |  | 
Point Color | MDATA_MEASURE_COLORP | COLOR |  |  |  | 
Color 1 | MDATA_MEASURE_COLOR1 | COLOR |  |  |  | 
Color 2 | MDATA_MEASURE_COLOR2 | COLOR |  |  |  | 
Point1 | MDATA_MEASUREGROUP_P1 | SEPARATOR |  |  |  | 
Point 1 Object | MDATA_MEASURE_PNT1_LINK | LINK |  |  |  | 
Point 1 Mode | MDATA_MEASURE_PNT1_MODE | LONG |  |  |  | MDATA_MEASURE_PNT_MODE_FREE; MDATA_MEASURE_PNT_MODE_POINT; MDATA_MEASURE_PNT_MODE_EDGE; MDATA_MEASURE_PNT_MODE_POLY
Point 1 Index | MDATA_MEASURE_PNT1_IDX | LONG |  |  |  | 
Point 1 Position | MDATA_MEASURE_PNT1_VECTOR | VECTOR |  |  |  | 
Point2 | MDATA_MEASUREGROUP_P2 | SEPARATOR |  |  |  | 
Point 2 Object | MDATA_MEASURE_PNT2_LINK | LINK |  |  |  | 
Point 2 Mode | MDATA_MEASURE_PNT2_MODE | LONG |  |  |  | MDATA_MEASURE_PNT_MODE_FREE; MDATA_MEASURE_PNT_MODE_POINT; MDATA_MEASURE_PNT_MODE_EDGE; MDATA_MEASURE_PNT_MODE_POLY
Point 2 Index | MDATA_MEASURE_PNT2_IDX | LONG |  |  |  | 
Point 2 Position | MDATA_MEASURE_PNT2_VECTOR | VECTOR |  |  |  | 
Point3 | MDATA_MEASUREGROUP_P3 | SEPARATOR |  |  |  | 
Point 3 Object | MDATA_MEASURE_PNT3_LINK | LINK |  |  |  | 
Point 3 Mode | MDATA_MEASURE_PNT3_MODE | LONG |  |  |  | MDATA_MEASURE_PNT_MODE_FREE; MDATA_MEASURE_PNT_MODE_POINT; MDATA_MEASURE_PNT_MODE_EDGE; MDATA_MEASURE_PNT_MODE_POLY
Point 3 Index | MDATA_MEASURE_PNT3_IDX | LONG |  |  |  | 
Point 3 Position | MDATA_MEASURE_PNT3_VECTOR | VECTOR |  |  |  | 
