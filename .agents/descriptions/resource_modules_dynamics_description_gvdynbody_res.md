# Description: Dynamics Body State

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/dynamics/description/gvdynbody.res`
- **Symbol:** `GVdynbody`
- **Category:** Graph View

Use parameter symbols to access parameters and cycle option symbols for cycle values, never their numeric IDs. Treat Min and Max as constraints and Default as the declared initial value; blank cells mean the resource does not declare that metadata, not that the value is zero. Base Description Parameters lists inherited fields from each base; All Parameters lists the effective parameter set for this description.

## Base Description Parameters

### Node (`GVbase`)

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Enabled | ID_GVBASE_ENABLE | BOOL |  |  |  | 
Title Color | ID_GVBASE_COLOR | COLOR |  |  |  | 
Remark | ID_GVBASE_REMARK | STRING |  |  |  | 

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
Enabled | ID_GVBASE_ENABLE | BOOL |  |  |  | 
Title Color | ID_GVBASE_COLOR | COLOR |  |  |  | 
Remark | ID_GVBASE_REMARK | STRING |  |  |  | 
Object | DYNAMICS_BODY_NODE_OBJECT | LINK |  |  |  | 
On | DYNAMICS_BODY_NODE_INPUT_ON | BOOL |  |  |  | 
Object | DYNAMICS_BODY_NODE_INPUT_OBJECT | GVGENERALOBJECT |  |  |  | 
Object Index | DYNAMICS_BODY_NODE_INPUT_INDEX | LONG | 0 |  |  | 
Point Index | DYNAMICS_BODY_NODE_INPUT_POINT_INDEX | LONG | 0 |  |  | 
Trigger | DYNAMICS_BODY_NODE_INPUT_TRIGGER | BOOL |  |  |  | 
Mass | DYNAMICS_BODY_NODE_INPUT_MASS | REAL |  |  |  | 
Position | DYNAMICS_BODY_NODE_INPUT_POSITION | VECTOR |  |  |  | 
Local Position | DYNAMICS_BODY_NODE_INPUT_LOCAL_POSITION | VECTOR |  |  |  | 
Rotation | DYNAMICS_BODY_NODE_INPUT_ROTATION | VECTOR |  |  |  | 
Global Matrix | DYNAMICS_BODY_NODE_INPUT_MATRIX | MATRIX |  |  |  | 
Linear Velocity | DYNAMICS_BODY_NODE_INPUT_LINEAR_VELOCITY | VECTOR |  |  |  | 
Angular Velocity | DYNAMICS_BODY_NODE_INPUT_ANGULAR_VELOCITY | VECTOR |  |  |  | 
Add Linear Acceleration | DYNAMICS_BODY_NODE_INPUT_ADD_LINEAR_ACCELERATION | VECTOR |  |  |  | 
Add Angular Acceleration | DYNAMICS_BODY_NODE_INPUT_ADD_ANGULAR_ACCELERATION | VECTOR |  |  |  | 
Add Force | DYNAMICS_BODY_NODE_INPUT_ADD_FORCE | VECTOR |  |  |  | 
Add Torque | DYNAMICS_BODY_NODE_INPUT_ADD_TORQUE | VECTOR |  |  |  | 
Point of Application | DYNAMICS_BODY_NODE_INPUT_POINT_OF_APPLICATION | VECTOR |  |  |  | 
Local Point of Application | DYNAMICS_BODY_NODE_INPUT_LOCAL_POINT_OF_APPLICATION | VECTOR |  |  |  | 
Count | DYNAMICS_BODY_NODE_OUTPUT_COUNT | LONG |  |  |  | 
Object | DYNAMICS_BODY_NODE_OUTPUT_OBJECT | GVGENERALOBJECT |  |  |  | 
Object Index | DYNAMICS_BODY_NODE_OUTPUT_INDEX | LONG |  |  |  | 
Tag | DYNAMICS_BODY_NODE_OUTPUT_TAG | GVGENERALTAG |  |  |  | 
Mass | DYNAMICS_BODY_NODE_OUTPUT_MASS | REAL |  |  |  | 
Dynamic | DYNAMICS_BODY_NODE_OUTPUT_DYNAMIC | BOOL |  |  |  | 
Position | DYNAMICS_BODY_NODE_OUTPUT_POSITION | VECTOR |  |  |  | 
Local Position | DYNAMICS_BODY_NODE_OUTPUT_LOCAL_POSITION | VECTOR |  |  |  | 
Rotation | DYNAMICS_BODY_NODE_OUTPUT_ROTATION | VECTOR |  |  |  | 
Global Matrix | DYNAMICS_BODY_NODE_OUTPUT_MATRIX | MATRIX |  |  |  | 
Linear Velocity | DYNAMICS_BODY_NODE_OUTPUT_LINEAR_VELOCITY | VECTOR |  |  |  | 
Angular Velocity | DYNAMICS_BODY_NODE_OUTPUT_ANGULAR_VELOCITY | VECTOR |  |  |  | 
Linear Acceleration | DYNAMICS_BODY_NODE_OUTPUT_LINEAR_ACCELERATION | VECTOR |  |  |  | 
Angular Acceleration | DYNAMICS_BODY_NODE_OUTPUT_ANGULAR_ACCELERATION | VECTOR |  |  |  | 
Force | DYNAMICS_BODY_NODE_OUTPUT_FORCE | VECTOR |  |  |  | 
Torque | DYNAMICS_BODY_NODE_OUTPUT_TORQUE | VECTOR |  |  |  | 
