# Description: IK

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/ca/description/tcaik.res`
- **Symbol:** `Tcaik`
- **Category:** Tags

Use parameter symbols to access parameters and cycle option symbols for cycle values, never their numeric IDs. Treat Min and Max as constraints and Default as the declared initial value; blank cells mean the resource does not declare that metadata, not that the value is zero. Base Description Parameters lists inherited fields from each base; All Parameters lists the effective parameter set for this description.

## Base Description Parameters

### Expression (`Texpression`)

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Priority | EXPRESSION_PRIORITY | PRIORITY |  |  |  | 
Enable | EXPRESSION_ENABLE | BOOL |  |  |  | 

### Base Tag (`Tbase`)

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Expose on Object | ID_EXPOSETAB | BOOL |  |  |  | 

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
Icon Color | ID_BASELIST_ICON_COLORIZE_MODE | BOOL |  |  |  | 
Color | ID_BASELIST_ICON_COLOR | COLOR |  |  | 1.0 0.9 0.4 | 
No label | ID_BASELIST_ICON_PRESET_BUTTONS | ICONCHOOSER |  |  |  | 
Name | ID_BASELIST_NAME | STRING |  |  |  | 
Layer | ID_LAYER_LINK | LINK |  |  |  | 
No label | ID_BASELIST_NODESPACE_ADD_REMOVE_BUTTONS | NODESPACE_ADD_REMOVE |  |  |  | 
Expose on Object | ID_EXPOSETAB | BOOL |  |  |  | 
Priority | EXPRESSION_PRIORITY | PRIORITY |  |  |  | 
Enable | EXPRESSION_ENABLE | BOOL |  |  |  | 
Use IK | ID_CA_IK_TAG_ENABLE | BOOL |  |  |  | 
IK Solver | ID_CA_IK_TAG_SOLVER | LONG |  |  |  | ID_CA_IK_TAG_SOLVER_2D; ID_CA_IK_TAG_SOLVER_3D
Point IK | ID_CA_IK_TAG_SPLINE | BOOL |  |  |  | 
Start | ID_CA_IK_TAG_START_INDEX | LONG | 0 |  |  | 
End | ID_CA_IK_TAG_END_INDEX | LONG | 0 |  |  | 
End | ID_CA_IK_TAG_TIP | LINK |  |  |  | 
Goal | ID_CA_IK_TAG_TARGET | LINK |  |  |  | 
Add Goal | ID_CA_IK_TAG_ADD_GOAL | BUTTON |  |  |  | 
IK/FK | ID_CA_IK_TAG_IKFK | REAL | 0.0 | 100.0 |  | 
Reset FK | ID_CA_IK_TAG_RESET_FK | BUTTON |  |  |  | 
Strength | ID_CA_IK_TAG_STRENGTH | REAL | 0.0 | 100.0 |  | 
Preferred Rot | ID_CA_IK_TAG_PREFERRED_WEIGHT | REAL | 0.0 | 100.0 |  | 
Goal Offset | ID_CA_IK_TAG_GOAL_OFFSET | REAL |  |  |  | 
Axis | ID_CA_IK_TAG_POLE_AXIS | LONG |  |  |  | ID_CA_IK_TAG_POLE_AXIS_AUTO; ID_CA_IK_TAG_POLE_AXIS_X; ID_CA_IK_TAG_POLE_AXIS_Y; ID_CA_IK_TAG_POLE_AXIS_Z; ID_CA_IK_TAG_POLE_AXIS_NX; ID_CA_IK_TAG_POLE_AXIS_NY; ID_CA_IK_TAG_POLE_AXIS_NZ
Twist | ID_CA_IK_TAG_POLE_TWIST | REAL |  |  |  | 
Object | ID_CA_IK_TAG_POLE | LINK |  |  |  | 
Add Pole | ID_CA_IK_TAG_ADD_POLE | BUTTON |  |  |  | 
Squash | ID_CA_IK_TAG_SQUASH | REAL | 0.0 | 100.0 |  | 
Type | ID_CA_IK_TAG_SQUASH_TYPE | LONG |  |  |  | ID_CA_IK_TAG_STRETCH_TYPE_POSITION; ID_CA_IK_TAG_STRETCH_TYPE_SCALE_UNIFORM; ID_CA_IK_TAG_STRETCH_TYPE_SCALE_BONE; ID_CA_IK_TAG_STRETCH_TYPE_SCALE_VOLUME
Distance | ID_CA_IK_TAG_SQUASH_CLAMP_DIST | REAL | 0.0 |  |  | 
Clamp | ID_CA_IK_TAG_SQUASH_CLAMP | BOOL |  |  |  | 
Stretch | ID_CA_IK_TAG_STRETCH | REAL | 0.0 | 100.0 |  | 
Type | ID_CA_IK_TAG_STRETCH_TYPE | LONG |  |  |  | ID_CA_IK_TAG_STRETCH_TYPE_POSITION; ID_CA_IK_TAG_STRETCH_TYPE_SCALE_UNIFORM; ID_CA_IK_TAG_STRETCH_TYPE_SCALE_BONE; ID_CA_IK_TAG_STRETCH_TYPE_SCALE_VOLUME
Distance | ID_CA_IK_TAG_STRETCH_CLAMP_DIST | REAL | 0.0 |  |  | 
Clamp | ID_CA_IK_TAG_STRETCH_CLAMP | BOOL |  |  |  | 
Show FK | ID_CA_IK_TAG_DRAW_FK_CHAIN | BOOL |  |  |  | 
Show IK | ID_CA_IK_TAG_DRAW_IK_CHAIN | BOOL |  |  |  | 
Handle Line | ID_CA_IK_TAG_DRAW_HANDLE_LINE | BOOL |  |  |  | 
Pole Vector | ID_CA_IK_TAG_DRAW_POLE | LONG |  |  |  | ID_CA_IK_TAG_DRAW_POLE_NONE; ID_CA_IK_TAG_DRAW_POLE_ROOT; ID_CA_IK_TAG_DRAW_POLE_JOINT
FK | ID_CA_IK_TAG_DRAW_FK_COLOR | COLOR |  |  |  | 
IK | ID_CA_IK_TAG_DRAW_IK_COLOR | COLOR |  |  |  | 
Handle | ID_CA_IK_TAG_DRAW_HANDLE_COLOR | COLOR |  |  |  | 
Pole Vector | ID_CA_IK_TAG_DRAW_POLE_COLOR | COLOR |  |  |  | 
Keep Goal | ID_CA_IK_TAG_GOAL_UPDATE | BOOL |  |  |  | 
Constrain Goal | ID_CA_IK_TAG_GOAL_CONSTRAIN | BOOL |  |  |  | 
Update On Goal | ID_CA_IK_TAG_GOAL_DIRTY | BOOL |  |  |  | 
Align Goal | ID_CA_IK_TAG_ALIGN_GOAL | BOOL |  |  |  | 
Update IK on FK | ID_CA_IK_TAG_UPDATEFKIK | BOOL |  |  |  | 
Rotate to Goal | ID_CA_IK_TAG_ROTATE | BOOL |  |  |  | 
Max Iterations | ID_CA_IK_TAG_SOLVER_ITERATIONS_MAX | LONG | 0 | 9999 |  | 
Threshold | ID_CA_IK_TAG_SOLVER_THRESHOLD | REAL | 0.0 | 100000.0 |  | 
Enable | ID_CA_IK_TAG_DYNAMICS_ENABLE | BOOL |  |  |  | 
Strength | ID_CA_IK_TAG_DYNAMICS_STIFFNESS | REAL | 0.0 |  |  | 
Drag | ID_CA_IK_TAG_DYNAMICS_DRAG | REAL | 0.0 | 100.0 |  | 
Pos Hold | ID_CA_IK_TAG_DYNAMICS_POSHOLD | REAL | 0.0 | 100.0 |  | 
Rot Hold | ID_CA_IK_TAG_DYNAMICS_ROTHOLD | REAL | 0.0 | 100.0 |  | 
Collisions | ID_CA_IK_TAG_DYNAMICS_COLLISIONS | BOOL |  |  |  | 
Radius | ID_CA_IK_TAG_DYNAMICS_RADIUS | REAL |  |  |  | 
Friction | ID_CA_IK_TAG_DYNAMICS_FRICTION | REAL | 0.0 | 100.0 |  | 
Bounce | ID_CA_IK_TAG_DYNAMICS_BOUNCE | REAL | 0.0 | 100.0 |  | 
Objects | ID_CA_IK_TAG_DYNAMICS_COLLIDERS | IN_EXCLUDE |  |  |  | 
Position | ID_CA_IK_TAG_DYNAMICS_POSHOLD_CURVE | SPLINE |  |  |  | 
Rotation | ID_CA_IK_TAG_DYNAMICS_ROTHOLD_CURVE | SPLINE |  |  |  | 
Gravity | ID_CA_IK_TAG_DYNAMICS_GRAVITY | REAL |  |  |  | 
Mode | ID_CA_IK_TAG_DYNAMICS_FORCES_INCEXC | LONG |  |  |  | ID_CA_IK_TAG_DYNAMICS_INCEXC_INCLUDE; ID_CA_IK_TAG_DYNAMICS_INCEXC_EXCLUDE
Forces | ID_CA_IK_TAG_DYNAMICS_FORCES | IN_EXCLUDE |  |  |  | 
Continuous Update | ID_CA_IK_TAG_DYNAMICS_CUPDATE | BOOL |  |  |  | 
Steps | ID_CA_IK_TAG_DYNAMICS_SUBDIV | LONG | 1 | 100 |  | 
Auto | ID_CA_IK_TAG_DYNAMICS_AUTOTIME | BOOL |  |  |  | 
Start | ID_CA_IK_TAG_DYNAMICS_START | BASETIME |  |  |  | 
Stop | ID_CA_IK_TAG_DYNAMICS_STOP | BASETIME |  |  |  | 
