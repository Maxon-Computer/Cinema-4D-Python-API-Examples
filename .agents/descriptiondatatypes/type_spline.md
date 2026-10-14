# Description Data Type: SPLINE

- **Cinema 4D Version:** `2027.0.0`

This file describes the SPLINE description data type and lists all flags encountered in the resources for Cinema 4D 2027.0.0.

## Flags

Flag | Arguments | Example
---- | --------- | -------
ALLOW_VERT_SCALE_MOVE |  | <code>SPLINE ID_CA_COLLISION_DEFORMER_OBJECT_FALLOFF<br>{<br>&nbsp;&nbsp;ALLOW_VERT_SCALE_MOVE;<br>&nbsp;&nbsp;USE_OPTIMAL_RANGE;<br><br>&nbsp;&nbsp;X_MIN 0;<br>&nbsp;&nbsp;X_MAX 1;<br>&nbsp;&nbsp;OPTIMAL_X_MIN 0;<br>&nbsp;&nbsp;OPTIMAL_X_MAX 1;<br><br>&nbsp;&nbsp;OPTIMAL_Y_MIN 0;<br>&nbsp;&nbsp;OPTIMAL_Y_MAX 1;<br>&nbsp;&nbsp;Y_MIN -1;<br>&nbsp;&nbsp;Y_MAX 1;<br>}</code>
ANIM | OFF | <code>SPLINE ID_MT_CLIP_FADESPLINEWND<br>{<br>&nbsp;&nbsp;FIT_H;<br>&nbsp;&nbsp;ANIM OFF;<br><br>&nbsp;&nbsp;SHOWGRID_H;<br>&nbsp;&nbsp;SHOWGRID_V;<br><br>&nbsp;&nbsp;EDIT_H;<br>&nbsp;&nbsp;EDIT_V;<br><br>&nbsp;&nbsp;X_MIN 0;<br>&nbsp;&nbsp;X_MAX 1;<br><br>&nbsp;&nbsp;Y_MIN 0;<br>&nbsp;&nbsp;Y_MAX 1;<br><br>&nbsp;&nbsp;X_STEPS 0.1;<br>&nbsp;&nbsp;Y_STEPS 0.1;<br>}</code>
CUSTOMCOLOR_COL | 1.0 0.0 0.0 | <code>SPLINE ID_PV_FILTER_GRAD_SPLINE_R<br>{<br>&nbsp;&nbsp;SHOWGRID_H;<br>&nbsp;&nbsp;SHOWGRID_V;<br><br>&nbsp;&nbsp;EDIT_H;<br>&nbsp;&nbsp;EDIT_V;<br><br>&nbsp;&nbsp;X_MIN 0;<br>&nbsp;&nbsp;X_MAX 1;<br><br>&nbsp;&nbsp;Y_MIN 0;<br>&nbsp;&nbsp;Y_MAX 1;<br><br>&nbsp;&nbsp;X_STEPS 0.01;<br>&nbsp;&nbsp;Y_STEPS 0.01;<br><br>&nbsp;&nbsp;CUSTOMCOLOR_SET;<br>&nbsp;&nbsp;CUSTOMCOLOR_COL 1.0 0.0 0.0;<br>}</code>
CUSTOMCOLOR_SET |  | <code>SPLINE ID_PV_FILTER_GRAD_SPLINE_R<br>{<br>&nbsp;&nbsp;SHOWGRID_H;<br>&nbsp;&nbsp;SHOWGRID_V;<br><br>&nbsp;&nbsp;EDIT_H;<br>&nbsp;&nbsp;EDIT_V;<br><br>&nbsp;&nbsp;X_MIN 0;<br>&nbsp;&nbsp;X_MAX 1;<br><br>&nbsp;&nbsp;Y_MIN 0;<br>&nbsp;&nbsp;Y_MAX 1;<br><br>&nbsp;&nbsp;X_STEPS 0.01;<br>&nbsp;&nbsp;Y_STEPS 0.01;<br><br>&nbsp;&nbsp;CUSTOMCOLOR_SET;<br>&nbsp;&nbsp;CUSTOMCOLOR_COL 1.0 0.0 0.0;<br>}</code>
EDITPORT |  | <code>SPLINE GV_RANGEMAPPER_SPLINE { INPORT; EDITPORT; SHOWGRID_H; SHOWGRID_V; EDIT_H; EDIT_V; }</code>
EDIT_H |  | <code>SPLINE MGMOSPLINEOBJECT_LENGTH_SPLINE<br>{<br>&nbsp;&nbsp;EDIT_H;<br>&nbsp;&nbsp;EDIT_V;<br>&nbsp;&nbsp;PARENTCOLLAPSE MGMOSPLINEOBJECT_LENGTH;<br>}</code>
EDIT_V |  | <code>SPLINE MGMOSPLINEOBJECT_LENGTH_SPLINE<br>{<br>&nbsp;&nbsp;EDIT_H;<br>&nbsp;&nbsp;EDIT_V;<br>&nbsp;&nbsp;PARENTCOLLAPSE MGMOSPLINEOBJECT_LENGTH;<br>}</code>
FIT_H |  | <code>SPLINE MGSOUNDEFFECTOR_FILTERSHAPE<br>{<br>&nbsp;&nbsp;FIT_H;<br>}</code>
HIDDEN |  | <code>SPLINE ID_CA_MUSCLE_OBJECT_SHAPE_COMPRESS<br>{<br>&nbsp;&nbsp;HIDDEN;<br>&nbsp;&nbsp;PARENTCOLLAPSE ID_CA_MUSCLE_OBJECT_STATE;<br>}</code>
INPORT |  | <code>SPLINE IN_SPLINEDATA { INPORT; MULTIPLE; }</code>
MINSIZE_H | 120 | <code>SPLINE CACHE_TOOL_FALLOFF<br>{<br>&nbsp;&nbsp;SHOWGRID_H;<br>&nbsp;&nbsp;SHOWGRID_V;<br><br>&nbsp;&nbsp;MINSIZE_H 120;<br>&nbsp;&nbsp;MINSIZE_V 90;<br><br>&nbsp;&nbsp;EDIT_H;<br>&nbsp;&nbsp;EDIT_V;<br>}</code>
MINSIZE_V | 90 | <code>SPLINE CACHE_TOOL_FALLOFF<br>{<br>&nbsp;&nbsp;SHOWGRID_H;<br>&nbsp;&nbsp;SHOWGRID_V;<br><br>&nbsp;&nbsp;MINSIZE_H 120;<br>&nbsp;&nbsp;MINSIZE_V 90;<br><br>&nbsp;&nbsp;EDIT_H;<br>&nbsp;&nbsp;EDIT_V;<br>}</code>
MULTIPLE |  | <code>SPLINE IN_SPLINEDATA { INPORT; MULTIPLE; }</code>
NEWLINE |  | <code>SPLINE ID_VOLUMEBUILDER_TAG_SPLINERADIUS_SCALESPLINE { NEWLINE; }</code>
OPTIMAL_X_MAX | 1 | <code>SPLINE ID_CA_COLLISION_DEFORMER_OBJECT_FALLOFF<br>{<br>&nbsp;&nbsp;ALLOW_VERT_SCALE_MOVE;<br>&nbsp;&nbsp;USE_OPTIMAL_RANGE;<br><br>&nbsp;&nbsp;X_MIN 0;<br>&nbsp;&nbsp;X_MAX 1;<br>&nbsp;&nbsp;OPTIMAL_X_MIN 0;<br>&nbsp;&nbsp;OPTIMAL_X_MAX 1;<br><br>&nbsp;&nbsp;OPTIMAL_Y_MIN 0;<br>&nbsp;&nbsp;OPTIMAL_Y_MAX 1;<br>&nbsp;&nbsp;Y_MIN -1;<br>&nbsp;&nbsp;Y_MAX 1;<br>}</code>
OPTIMAL_X_MIN | 0 | <code>SPLINE ID_CA_COLLISION_DEFORMER_OBJECT_FALLOFF<br>{<br>&nbsp;&nbsp;ALLOW_VERT_SCALE_MOVE;<br>&nbsp;&nbsp;USE_OPTIMAL_RANGE;<br><br>&nbsp;&nbsp;X_MIN 0;<br>&nbsp;&nbsp;X_MAX 1;<br>&nbsp;&nbsp;OPTIMAL_X_MIN 0;<br>&nbsp;&nbsp;OPTIMAL_X_MAX 1;<br><br>&nbsp;&nbsp;OPTIMAL_Y_MIN 0;<br>&nbsp;&nbsp;OPTIMAL_Y_MAX 1;<br>&nbsp;&nbsp;Y_MIN -1;<br>&nbsp;&nbsp;Y_MAX 1;<br>}</code>
OPTIMAL_Y_MAX | 1 | <code>SPLINE ID_CA_COLLISION_DEFORMER_OBJECT_FALLOFF<br>{<br>&nbsp;&nbsp;ALLOW_VERT_SCALE_MOVE;<br>&nbsp;&nbsp;USE_OPTIMAL_RANGE;<br><br>&nbsp;&nbsp;X_MIN 0;<br>&nbsp;&nbsp;X_MAX 1;<br>&nbsp;&nbsp;OPTIMAL_X_MIN 0;<br>&nbsp;&nbsp;OPTIMAL_X_MAX 1;<br><br>&nbsp;&nbsp;OPTIMAL_Y_MIN 0;<br>&nbsp;&nbsp;OPTIMAL_Y_MAX 1;<br>&nbsp;&nbsp;Y_MIN -1;<br>&nbsp;&nbsp;Y_MAX 1;<br>}</code>
OPTIMAL_Y_MIN | 0 | <code>SPLINE ID_CA_COLLISION_DEFORMER_OBJECT_FALLOFF<br>{<br>&nbsp;&nbsp;ALLOW_VERT_SCALE_MOVE;<br>&nbsp;&nbsp;USE_OPTIMAL_RANGE;<br><br>&nbsp;&nbsp;X_MIN 0;<br>&nbsp;&nbsp;X_MAX 1;<br>&nbsp;&nbsp;OPTIMAL_X_MIN 0;<br>&nbsp;&nbsp;OPTIMAL_X_MAX 1;<br><br>&nbsp;&nbsp;OPTIMAL_Y_MIN 0;<br>&nbsp;&nbsp;OPTIMAL_Y_MAX 1;<br>&nbsp;&nbsp;Y_MIN -1;<br>&nbsp;&nbsp;Y_MAX 1;<br>}</code>
OUTPORT |  | <code>SPLINE OUT_SPLINEDATA { OUTPORT; MULTIPLE; }</code>
PARENTCOLLAPSE | ID_CA_MUSCLE_OBJECT_STATE | <code>SPLINE ID_CA_MUSCLE_OBJECT_SHAPE_RELAX<br>{<br>&nbsp;&nbsp;PARENTCOLLAPSE ID_CA_MUSCLE_OBJECT_STATE;<br>}</code>
SCALE_H |  | <code>SPLINE ID_CA_WEIGHT_MGR_SPREADSHEET_REMAP_SPLINE { SCALE_H; }</code>
SHOWGRID_H |  | <code>SPLINE ID_CA_ANIMATION_MODIFIER_TAG_SMOOTH_SPLINE { SHOWGRID_H; SHOWGRID_V;}</code>
SHOWGRID_V |  | <code>SPLINE ID_CA_ANIMATION_MODIFIER_TAG_SMOOTH_SPLINE { SHOWGRID_H; SHOWGRID_V;}</code>
UNIMPORTANTFORDEFAULTS |  | <code>SPLINE SKY_FOG_DENSITY_DISTRIB { UNIMPORTANTFORDEFAULTS; SHOWGRID_H; SHOWGRID_V; MINSIZE_H 120;<br>&nbsp;&nbsp;MINSIZE_V 90; EDIT_H; EDIT_V;<br>&nbsp;&nbsp;X_MIN 0; X_MAX 100; Y_MIN 0; Y_MAX 100; X_STEPS 1; Y_STEPS 1; }</code>
USE_OPTIMAL_RANGE |  | <code>SPLINE ID_CA_COLLISION_DEFORMER_OBJECT_FALLOFF<br>{<br>&nbsp;&nbsp;ALLOW_VERT_SCALE_MOVE;<br>&nbsp;&nbsp;USE_OPTIMAL_RANGE;<br><br>&nbsp;&nbsp;X_MIN 0;<br>&nbsp;&nbsp;X_MAX 1;<br>&nbsp;&nbsp;OPTIMAL_X_MIN 0;<br>&nbsp;&nbsp;OPTIMAL_X_MAX 1;<br><br>&nbsp;&nbsp;OPTIMAL_Y_MIN 0;<br>&nbsp;&nbsp;OPTIMAL_Y_MAX 1;<br>&nbsp;&nbsp;Y_MIN -1;<br>&nbsp;&nbsp;Y_MAX 1;<br>}</code>
X_MAX | 1 | <code>SPLINE ID_MT_CLIP_TIMWARPWND<br>{<br>&nbsp;&nbsp;SHOWGRID_H;<br>&nbsp;&nbsp;SHOWGRID_V;<br><br>&nbsp;&nbsp;EDIT_H;<br>&nbsp;&nbsp;EDIT_V;<br><br>&nbsp;&nbsp;X_MIN 0;<br>&nbsp;&nbsp;X_MAX 1;<br><br>&nbsp;&nbsp;Y_MIN 0;<br>&nbsp;&nbsp;Y_MAX 1;<br><br>&nbsp;&nbsp;X_STEPS 0.1;<br>&nbsp;&nbsp;Y_STEPS 0.1;<br>}</code>
X_MIN | 0 | <code>SPLINE ID_MT_CLIP_TIMWARPWND<br>{<br>&nbsp;&nbsp;SHOWGRID_H;<br>&nbsp;&nbsp;SHOWGRID_V;<br><br>&nbsp;&nbsp;EDIT_H;<br>&nbsp;&nbsp;EDIT_V;<br><br>&nbsp;&nbsp;X_MIN 0;<br>&nbsp;&nbsp;X_MAX 1;<br><br>&nbsp;&nbsp;Y_MIN 0;<br>&nbsp;&nbsp;Y_MAX 1;<br><br>&nbsp;&nbsp;X_STEPS 0.1;<br>&nbsp;&nbsp;Y_STEPS 0.1;<br>}</code>
X_STEPS | 0.1 | <code>SPLINE ID_MT_CLIP_TIMWARPWND<br>{<br>&nbsp;&nbsp;SHOWGRID_H;<br>&nbsp;&nbsp;SHOWGRID_V;<br><br>&nbsp;&nbsp;EDIT_H;<br>&nbsp;&nbsp;EDIT_V;<br><br>&nbsp;&nbsp;X_MIN 0;<br>&nbsp;&nbsp;X_MAX 1;<br><br>&nbsp;&nbsp;Y_MIN 0;<br>&nbsp;&nbsp;Y_MAX 1;<br><br>&nbsp;&nbsp;X_STEPS 0.1;<br>&nbsp;&nbsp;Y_STEPS 0.1;<br>}</code>
Y_MAX | 1 | <code>SPLINE HAIRMATERIAL_CLUMP_CURVE<br>{<br>&nbsp;&nbsp;Y_MIN -1;<br>&nbsp;&nbsp;Y_MAX 1;<br>}</code>
Y_MIN | -1 | <code>SPLINE HAIRMATERIAL_CLUMP_CURVE<br>{<br>&nbsp;&nbsp;Y_MIN -1;<br>&nbsp;&nbsp;Y_MAX 1;<br>}</code>
Y_STEPS | 0.1 | <code>SPLINE ID_MT_CLIP_TIMWARPWND<br>{<br>&nbsp;&nbsp;SHOWGRID_H;<br>&nbsp;&nbsp;SHOWGRID_V;<br><br>&nbsp;&nbsp;EDIT_H;<br>&nbsp;&nbsp;EDIT_V;<br><br>&nbsp;&nbsp;X_MIN 0;<br>&nbsp;&nbsp;X_MAX 1;<br><br>&nbsp;&nbsp;Y_MIN 0;<br>&nbsp;&nbsp;Y_MAX 1;<br><br>&nbsp;&nbsp;X_STEPS 0.1;<br>&nbsp;&nbsp;Y_STEPS 0.1;<br>}</code>
