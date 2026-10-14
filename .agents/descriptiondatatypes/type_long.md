# Description Data Type: LONG

- **Cinema 4D Version:** `2027.0.0`

This file describes the LONG description data type and lists all flags encountered in the resources for Cinema 4D 2027.0.0.

## Flags

Flag | Arguments | Example
---- | --------- | -------
ALIGN_LEFT |  | <code>LONG MDATA_ARRANGE_MODE { ALIGN_LEFT; CYCLE { MDATA_ARRANGE_MODE_SELECTMODE; MDATA_ARRANGE_MODE_LINEAR; MDATA_ARRANGE_MODE_CIRCLE; MDATA_ARRANGE_MODE_ALONGSPLINE; } }</code>
ANIM | OFF | <code>LONG PREF_BROWSER_MXAI_PORT {ANIM OFF;}</code>
ANIM | ON | <code>LONG EXTRUDEOBJECT_DIRECTION<br>{<br>&nbsp;&nbsp;CYCLE<br>&nbsp;&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;EXTRUDEOBJECT_DIRECTION_AUTO;<br>&nbsp;&nbsp;&nbsp;&nbsp;EXTRUDEOBJECT_DIRECTION_X;<br>&nbsp;&nbsp;&nbsp;&nbsp;EXTRUDEOBJECT_DIRECTION_Y;<br>&nbsp;&nbsp;&nbsp;&nbsp;EXTRUDEOBJECT_DIRECTION_Z;<br>&nbsp;&nbsp;&nbsp;&nbsp;EXTRUDEOBJECT_DIRECTION_ABSOLUTE;<br>&nbsp;&nbsp;&nbsp;&nbsp;EXTRUDEOBJECT_DIRECTION_CUSTOM;<br>&nbsp;&nbsp;}<br>&nbsp;&nbsp;ANIM ON;<br>}</code>
COLUMNS | 2 | <code>LONG MDATA_UVPEELER_UV_ISLAND_STORAGE<br>{<br>&nbsp;&nbsp;CYCLE<br>&nbsp;&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;MDATA_UVPEELER_SINGLE_UV_TILE;<br>&nbsp;&nbsp;&nbsp;&nbsp;MDATA_UVPEELER_MULTIPLE_UV_TILES;<br>&nbsp;&nbsp;}<br>&nbsp;&nbsp;CUSTOMGUI RADIOBUTTONS; COLUMNS 2;<br>&nbsp;&nbsp;ANIM OFF;<br>}</code>
CREATEPORT |  | <code>LONG GV_NEARESTPOINT_OUTPUT_POINTINDEX { OUTPORT; CREATEPORT; }</code>
CUSTOMGUI | QUICKTABRADIO | <code>LONG REDSHIFT_POSTEFFECTS_BACKGROUND_FRAME<br>{<br>&nbsp;&nbsp;CUSTOMGUI QUICKTABRADIO;<br>&nbsp;&nbsp;CYCLE<br>&nbsp;&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;REDSHIFT_POSTEFFECTS_BACKGROUND_FRAME_STRETCH;<br>&nbsp;&nbsp;&nbsp;&nbsp;REDSHIFT_POSTEFFECTS_BACKGROUND_FRAME_CROP;<br>&nbsp;&nbsp;&nbsp;&nbsp;REDSHIFT_POSTEFFECTS_BACKGROUND_FRAME_FIT;<br>&nbsp;&nbsp;}<br>}</code>
CUSTOMGUI | COLORSPACE | <code>LONG BITMAPSHADER_OCIO_INPUT_COLORSPACE<br>{<br>&nbsp;&nbsp;ANIM OFF;<br>&nbsp;&nbsp;CUSTOMGUI COLORSPACE;<br>}</code>
CUSTOMGUI | NOISE | <code>LONG SKY_CLOUD_1_NOISE<br>{<br>&nbsp;&nbsp;CYCLE<br>&nbsp;&nbsp;{<br>&nbsp;&nbsp;}<br>&nbsp;&nbsp;CUSTOMGUI NOISE;<br>}</code>
CUSTOMGUI | LONGSLIDER | <code>LONG REDSHIFT_POSTEFFECTS_DOF_BLADE_COUNT { MIN 0; MAX 64; CUSTOMGUI LONGSLIDER; }</code>
CUSTOMGUI | CYCLEBUTTON | <code>LONG ID_CA_WEIGHT_MGR_PASTE_WEIGHTS<br>{<br>&nbsp;&nbsp;SCALE_H;<br>&nbsp;&nbsp;CUSTOMGUI CYCLEBUTTON;<br>&nbsp;&nbsp;CYCLE<br>&nbsp;&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;ID_CA_WEIGHT_MGR_PASTE_MERGE;<br>&nbsp;&nbsp;&nbsp;&nbsp;ID_CA_WEIGHT_MGR_PASTE_REPLACE;<br>&nbsp;&nbsp;}<br>}</code>
CUSTOMGUI | SKY_II_CITYLIST | <code>LONG SKY_POS_CITY_COMBO<br>{<br>&nbsp;&nbsp;PARENTCOLLAPSE;<br>&nbsp;&nbsp;CUSTOMGUI SKY_II_CITYLIST;<br>&nbsp;&nbsp;ANIM OFF;<br>}</code>
CUSTOMGUI | RADIOBUTTONS | <code>LONG MDATA_UVPEELER_UV_ISLAND_STORAGE<br>{<br>&nbsp;&nbsp;CYCLE<br>&nbsp;&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;MDATA_UVPEELER_SINGLE_UV_TILE;<br>&nbsp;&nbsp;&nbsp;&nbsp;MDATA_UVPEELER_MULTIPLE_UV_TILES;<br>&nbsp;&nbsp;}<br>&nbsp;&nbsp;CUSTOMGUI RADIOBUTTONS; COLUMNS 2;<br>&nbsp;&nbsp;ANIM OFF;<br>}</code>
CYCLE | REDSHIFT_AOV_FILE_DATATYPE_RGB REDSHIFT_AOV_FILE_DATATYPE_RGBA REDSHIFT_AOV_FILE_DATATYPE_POINT REDSHIFT_AOV_FILE_DATATYPE_SCALAR | <code>LONG REDSHIFT_AOV_FILE_DATA_TYPE<br>{<br>&nbsp;&nbsp;CYCLE<br>&nbsp;&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;REDSHIFT_AOV_FILE_DATATYPE_RGB;<br>&nbsp;&nbsp;&nbsp;&nbsp;REDSHIFT_AOV_FILE_DATATYPE_RGBA;<br>&nbsp;&nbsp;&nbsp;&nbsp;REDSHIFT_AOV_FILE_DATATYPE_POINT;<br>&nbsp;&nbsp;&nbsp;&nbsp;REDSHIFT_AOV_FILE_DATATYPE_SCALAR;<br>&nbsp;&nbsp;}<br>}</code>
DEFAULT | 0 | <code>LONG FP_EMITTER_ATTRIBUTES_LIQUID_CONSTRAINTS_MIXTURE { DEFAULT 0; }</code>
EDITPORT |  | <code>LONG GV_NOISE_SEED { INPORT; EDITPORT; }</code>
FIELD | COLOR | <code>LONG FIELD_COLOR_MODE<br>{<br>&nbsp;&nbsp;FIELD COLOR;<br><br>&nbsp;&nbsp;CYCLE<br>&nbsp;&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;FIELD_COLOR_MODE_OFF;<br>&nbsp;&nbsp;&nbsp;&nbsp;-1;<br>&nbsp;&nbsp;&nbsp;&nbsp;FIELD_COLOR_MODE_COLOR;<br>&nbsp;&nbsp;&nbsp;&nbsp;FIELD_COLOR_MODE_GRADIENT;<br>&nbsp;&nbsp;}<br>}</code>
FIELD | HIDE | <code>LONG FIELD_TYPE<br>{<br>&nbsp;&nbsp;ANIM OFF;<br>&nbsp;&nbsp;FIELD HIDE;<br>&nbsp;&nbsp;CYCLE<br>&nbsp;&nbsp;{<br>&nbsp;&nbsp;}<br>}</code>
FIT_H |  | <code>LONG TEXTURETAG_PROJECTION<br>{<br>&nbsp;&nbsp;FIT_H;<br><br>&nbsp;&nbsp;CYCLE<br><br>&nbsp;&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;TEXTURETAG_PROJECTION_SPHERICAL;<br>&nbsp;&nbsp;&nbsp;&nbsp;TEXTURETAG_PROJECTION_CYLINDRICAL;<br>&nbsp;&nbsp;&nbsp;&nbsp;TEXTURETAG_PROJECTION_FLAT;<br>&nbsp;&nbsp;&nbsp;&nbsp;TEXTURETAG_PROJECTION_CUBIC;<br>&nbsp;&nbsp;&nbsp;&nbsp;TEXTURETAG_PROJECTION_FRONTAL;<br>&nbsp;&nbsp;&nbsp;&nbsp;TEXTURETAG_PROJECTION_SPATIAL;<br>&nbsp;&nbsp;&nbsp;&nbsp;TEXTURETAG_PROJECTION_UVW;<br>&nbsp;&nbsp;&nbsp;&nbsp;TEXTURETAG_PROJECTION_SHRINKWRAP;<br>&nbsp;&nbsp;&nbsp;&nbsp;TEXTURETAG_PROJECTION_CAMERAMAP;<br>&nbsp;&nbsp;&nbsp;&nbsp;TEXTURETAG_PROJECTION_TRIPLANAR;<br>&nbsp;&nbsp;}<br>}</code>
HIDDEN |  | <code>LONG TAKEBASE_INDEX { HIDDEN; }</code>
INPORT |  | <code>LONG GV_HAIR_POINT_INPUT_GUIDE { INPORT; }</code>
ITERATOR |  | <code>LONG OP_LBW_OUT_ST_PARTICLECOUNT{ OUTPORT; PORTONLY; ITERATOR; }</code>
MATEDNOTEXT |  | <code>LONG SLA_MABEL_SURFACE<br>{<br>&nbsp;&nbsp;MATEDNOTEXT;<br>&nbsp;&nbsp;CYCLE<br>&nbsp;&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;SLA_MABEL_SURFACE_1;<br>&nbsp;&nbsp;&nbsp;&nbsp;SLA_MABEL_SURFACE_2;<br>&nbsp;&nbsp;&nbsp;&nbsp;SLA_MABEL_SURFACE_BOTH;<br>&nbsp;&nbsp;}<br>}</code>
MAX | 20 | <code>LONG REDSHIFT_AOV_CRYPTOMATTE_DEPTH { MIN 1; MAX 20; }</code>
MAXSLIDER | 100 | <code>LONG REDSHIFT_AOV_AO_NUM_SAMPLES { MIN 1; MAXSLIDER 100; }</code>
MIN | 0 | <code>LONG REDSHIFT_AOV_MAX_MOTION_PIXELS { MIN 0; }</code>
MINEX |  | <code>LONG ONION_PSIZE { PARENTCOLLAPSE ONION_MODE; MIN 0; MINEX; MAX 10; ANIM OFF;}</code>
MINSLIDER | 0 | <code>LONG LIQUID_MESH_GEOMETRY_SMOOTH_ITER { MIN 0; MINSLIDER 0; MAXSLIDER 100;}</code>
MULTIPLE |  | <code>LONG IN_LONG {INPORT; MULTIPLE;}</code>
NEEDCONNECTION |  | <code>LONG GV_CONDITION_SWITCH { INPORT; STATICPORT; NEEDCONNECTION; CREATEPORT; }</code>
NOISE_OFFSET | 2100 | <code>LONG SLA_BANJI_ROUGHNESS_NOISE<br>{<br>&nbsp;&nbsp;CYCLE<br>&nbsp;&nbsp;{<br>&nbsp;&nbsp;}<br>&nbsp;&nbsp;CUSTOMGUI NOISE; NOISE_OFFSET 2100;<br>}</code>
NOPARENTCOLLAPSE |  | <code>LONG MDATA_SCULPTBRUSH_SETTINGS_DRAWMODE<br>{<br>&nbsp;&nbsp;NOPARENTCOLLAPSE;<br>&nbsp;&nbsp;CYCLE<br>&nbsp;&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;MDATA_SCULPTBRUSH_SETTINGS_DRAWMODE_FREEHAND;<br>&nbsp;&nbsp;&nbsp;&nbsp;MDATA_SCULPTBRUSH_SETTINGS_DRAWMODE_LINE;<br>&nbsp;&nbsp;}<br>}</code>
OUTPORT |  | <code>LONG DYNAMICS_BODY_NODE_OUTPUT_COUNT {OUTPORT;}</code>
PARENTCOLLAPSE | FP_BLEND_OBJECT_DETECTION_MODE | <code>LONG FP_BLEND_OBJECT_MAXIMUM_CHECKS { MIN 1; PARENTCOLLAPSE FP_BLEND_OBJECT_DETECTION_MODE; }</code>
PARENTID | GW_AT_USE | <code>LONG GW_AT_POS { PARENTID GW_AT_USE; CYCLE { GW_AT_ZBUFFER; GW_AT_3DPOS; } }</code>
PORTONLY |  | <code>LONG GV_REDSHIFT_MULTISHADER_OUTPUT_COUNT { OUTPORT; PORTONLY; }</code>
SCALE_H |  | <code>LONG REDSHIFT_RENDERER_AOV_QUICK_ADD { ANIM OFF; SCALE_H; }</code>
STATICPORT |  | <code>LONG COLLISION_NODE_OUTPUT_COUNT {OUTPORT; STATICPORT; CREATEPORT;}</code>
STEP | 1 | <code>LONG MDATA_TOOLUDIMMOVE_OFFSETU { STEP 1;}</code>
UNIMPORTANTFORDEFAULTS |  | <code>LONG DOCUMENT_INFO_PRGCREATOR_ID { UNIMPORTANTFORDEFAULTS; HIDDEN; ANIM OFF; }</code>
