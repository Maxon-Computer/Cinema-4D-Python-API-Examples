# Description: Dynamics Body Tag

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/dynamics/description/dynrigidbodytag.res`
- **Symbol:** `DynRigidBodyTag`
- **Category:** Tags

Use parameter symbols to access parameters and cycle option symbols for cycle values, never their numeric IDs. Treat Min and Max as constraints and Default as the declared initial value; blank cells mean the resource does not declare that metadata, not that the value is zero. Base Description Parameters lists inherited fields from each base; All Parameters lists the effective parameter set for this description.

## Base Description Parameters

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
Enabled | RIGID_BODY_ENABLED | BOOL |  |  |  | 
MoGraph Selection | RIGID_BODY_ENABLED_SELECTION | LINK |  |  |  | 
Dynamic | RIGID_BODY_DYNAMIC | LONG |  |  |  | RIGID_BODY_DYNAMIC_OFF; RIGID_BODY_DYNAMIC_ON; RIGID_BODY_DYNAMIC_GHOST
MoGraph Selection | RIGID_BODY_DYNAMIC_SELECTION | LINK |  |  |  | 
Set Initial State | RIGID_BODY_SET_INITIAL_STATE | BUTTON |  |  |  | 
Clear Initial State | RIGID_BODY_CLEAR_INITIAL_STATE | BUTTON |  |  |  | 
Show in Visualization | RIGID_BODY_SHOW | BOOL |  |  |  | 
Trigger | RIGID_BODY_TRIGGER | LONG |  |  |  | RIGID_BODY_TRIGGER_IMMEDIATELY; RIGID_BODY_TRIGGER_AT_PEAK; RIGID_BODY_TRIGGER_ON_COLLISION; RIGID_BODY_TRIGGER_XPRESSO
Trigger Velocity Threshold | RIGID_BODY_TRIGGER_ON_COLLISION_VELOCITY | REAL |  |  |  | 
Custom Initial Velocity | RIGID_BODY_USE_INITIAL_VELOCITY | BOOL |  |  |  | 
Initial Linear Velocity | RIGID_BODY_INITIAL_LINEAR_VELOCITY | VECTOR |  |  |  | 
Initial Angular Velocity | RIGID_BODY_INITIAL_ANGULAR_VELOCITY | VECTOR |  |  |  | 
Object Coordinates | RIGID_BODY_LOCAL_INITIAL_VELOCITY | BOOL |  |  |  | 
Dynamic Transition | RIGID_BODY_DYNAMIC_TRANSITION | BOOL |  |  |  | 
Transition Time | RIGID_BODY_TRANSITION_TIME | BASETIME | 0.0 |  |  | 
Deactivation | RIGID_BODY_GROUP_DEACTIVATION | SEPARATOR |  |  |  | 
Linear Velocity Threshold | RIGID_BODY_SLEEPING_LINEAR_VELOCITY | REAL | 0.0 |  |  | 
Angular Velocity Threshold | RIGID_BODY_SLEEPING_ANGULAR_VELOCITY | REAL | 0.0 |  |  | 
Inherit Tag | RIGID_BODY_HIERARCHY | LONG |  |  |  | RIGID_BODY_HIERARCHY_NONE; RIGID_BODY_HIERARCHY_APPLY_TAG; RIGID_BODY_HIERARCHY_COMPOUND_SHAPE
Individual Elements | RIGID_BODY_SPLIT_CACHE | LONG |  |  |  | RIGID_BODY_SPLIT_CACHE_OFF; RIGID_BODY_SPLIT_CACHE_TOP_LEVEL; RIGID_BODY_SPLIT_CACHE_SECOND_LEVEL; RIGID_BODY_SPLIT_CACHE_ON
Self Collisions | RIGID_BODY_SELF_COLLISIONS | BOOL |  |  |  | 
Use Deformed Object | RIGID_BODY_SHAPE_DEFORMEDSTATE | BOOL |  |  |  | 
Shape | RIGID_BODY_SHAPE | LONG |  |  |  | RIGID_BODY_SHAPE_DEFAULT; RIGID_BODY_SHAPE_DEFAULT_MODYNAMICS; RIGID_BODY_SHAPE_BOX; RIGID_BODY_SHAPE_ELLIPSOID; RIGID_BODY_SHAPE_CYLINDER_X; RIGID_BODY_SHAPE_CYLINDER_Y; RIGID_BODY_SHAPE_CYLINDER_Z; RIGID_BODY_SHAPE_CONVEX_HULL; RIGID_BODY_SHAPE_KINETIC_MESH; RIGID_BODY_SHAPE_STATIC_MESH; RIGID_BODY_SHAPE_REFERENCE; RIGID_BODY_SHAPE_NO_SHAPE
Size Increment | RIGID_BODY_SHAPE_SIZE_INCREMENT | REAL |  |  |  | 
Use Collision Margin | RIGID_BODY_SPECIFIC_MARGIN | BOOL |  |  |  | 
Margin | RIGID_BODY_MARGIN | REAL | 0.0 |  |  | 
Object | RIGID_BODY_REFERENCE_SHAPE | LINK |  |  |  | 
Keep Soft Body Shape | RIGID_BODY_SB_KEEP_SHAPE | BOOL |  |  |  | 
Bounce | RIGID_BODY_RESTITUTION | REAL | 0.0 |  |  | 
Friction | RIGID_BODY_FRICTION | REAL | 0.0 |  |  | 
Collision Noise | RIGID_BODY_COLLISION_NOISE | REAL | 0.0 | 90.0 |  | 
Use Mass | RIGID_BODY_MASS_SWITCH | LONG |  |  |  | RIGID_BODY_MASS_SWITCH_DEFAULT; RIGID_BODY_MASS_SWITCH_DENSITY; RIGID_BODY_MASS_SWITCH_MASS
Density | RIGID_BODY_DENSITY | REAL | 0.0 |  |  | 
Mass | RIGID_BODY_MASS | REAL | 0.0 |  |  | 
Rotational Mass | RIGID_BODY_INERTIA_FACTOR | REAL | 1 | 10000 |  | 
Use Center of Mass | RIGID_BODY_USE_CENTER_OF_MASS | BOOL |  |  |  | 
Center of Mass | RIGID_BODY_CENTER_OF_MASS | VECTOR |  |  |  | 
Follow Position | RIGID_BODY_LINEAR_FOLLOW_STRENGTH | REAL | 0.0 | 100.0 |  | 
Follow Rotation | RIGID_BODY_ANGULAR_FOLLOW_STRENGTH | REAL | 0.0 | 100.0 |  | 
Linear Damping | RIGID_BODY_LINEAR_DAMPING | REAL | 0.0 |  |  | 
Angular Damping | RIGID_BODY_ANGULAR_DAMPING | REAL | 0.0 |  |  | 
Force Mode | RIGID_BODY_FORCE_MODE | LONG |  |  |  | RIGID_BODY_FORCE_MODE_INCLUDE; RIGID_BODY_FORCE_MODE_EXCLUDE
Force List | RIGID_BODY_FORCE_INCLUDE_LIST | IN_EXCLUDE |  |  |  | 
Aerodynamics | RIGID_BODY_AERODYNAMICS_GROUP | SEPARATOR |  |  |  | 
Drag | RIGID_BODY_AERODYNAMICS_DRAG | REAL | 0.0 |  |  | 
Lift | RIGID_BODY_AERODYNAMICS_LIFT | REAL | 0.0 |  |  | 
Two-Sided | RIGID_BODY_AERODYNAMICS_TWO_SIDED | BOOL |  |  |  | 
Soft Body | RIGID_BODY_SOFT | LONG |  |  |  | RIGID_BODY_SOFT_OFF; RIGID_BODY_SOFT_ON; RIGID_BODY_SOFT_OF_CLONES
Rest State | RIGID_BODY_SB_REST_STATE | LINK |  |  |  | 
Mass Map | RIGID_BODY_SB_MASS_MAP | LINK |  |  |  | 
Use Accurate Solver | RIGID_BODY_SB_ACCURATE_SOLVER | BOOL |  |  |  | 
Springs | RIGID_BODY_SB_SPRING_GROUP | SEPARATOR |  |  |  | 
Structural | RIGID_BODY_SB_STRUCTURAL | REAL | 0.0 |  |  | 
Map | RIGID_BODY_SB_STRUCTURAL_MAP | LINK |  |  |  | 
Damping | RIGID_BODY_SB_STRUCTURAL_DAMPING | REAL | 0.0 |  |  | 
Map | RIGID_BODY_SB_STRUCTURAL_DAMPING_MAP | LINK |  |  |  | 
Elastic Limit | RIGID_BODY_SB_ELASTIC_LIMIT | REAL | 0.0 |  |  | 
Map | RIGID_BODY_SB_ELASTIC_LIMIT_MAP | LINK |  |  |  | 
Shear | RIGID_BODY_SB_SHEAR | REAL | 0.0 |  |  | 
Map | RIGID_BODY_SB_SHEAR_MAP | LINK |  |  |  | 
Damping | RIGID_BODY_SB_SHEAR_DAMPING | REAL | 0.0 |  |  | 
Map | RIGID_BODY_SB_SHEAR_DAMPING_MAP | LINK |  |  |  | 
Flexion | RIGID_BODY_SB_FLEXION | REAL | 0.0 |  |  | 
Map | RIGID_BODY_SB_FLEXION_MAP | LINK |  |  |  | 
Damping | RIGID_BODY_SB_FLEXION_DAMPING | REAL | 0.0 |  |  | 
Map | RIGID_BODY_SB_FLEXION_DAMPING_MAP | LINK |  |  |  | 
Elastic Limit | RIGID_BODY_SB_FLEXION_ELASTIC_LIMIT | REAL | 0.0 | 180.0 |  | 
Map | RIGID_BODY_SB_FLEXION_ELASTIC_LIMIT_MAP | LINK |  |  |  | 
Rest Length | RIGID_BODY_SB_REST_LENGTH | REAL | 1.0 |  |  | 
Map | RIGID_BODY_SB_REST_LENGTH_MAP | LINK |  |  |  | 
Tear-out Length | RIGID_BODY_SB_TEAR_OUT_LENGTH | REAL | 1.0 |  |  | 
Map | RIGID_BODY_SB_TEAR_OUT_LENGTH_MAP | LINK |  |  |  | 
No label | RIGID_BODY_SB_CLONE_ROTATION_SEPARATOR | SEPARATOR |  |  |  | 
Fix Rotation | RIGID_BODY_SB_CLONE_ROTATION | REAL | 0.0 |  |  | 
Map | RIGID_BODY_SB_CLONE_ROTATION_MAP | LINK |  |  |  | 
Damping | RIGID_BODY_SB_CLONE_ROTATION_DAMPING | REAL | 0.0 |  |  | 
Map | RIGID_BODY_SB_CLONE_ROTATION_DAMPING_MAP | LINK |  |  |  | 
Shape Conservation | RIGID_BODY_SB_SHAPE_CONSERVATION_GROUP | SEPARATOR |  |  |  | 
Stiffness | RIGID_BODY_SB_SHAPE_CONSERVATION | REAL | 0.0 |  |  | 
Map | RIGID_BODY_SB_SHAPE_CONSERVATION_MAP | LINK |  |  |  | 
Volume | RIGID_BODY_SB_SHAPE_VOLUME_CONSERVATION | REAL | 0.0 | 100.0 |  | 
Damping | RIGID_BODY_SB_SHAPE_CONSERVATION_DAMPING | REAL | 0.0 |  |  | 
Map | RIGID_BODY_SB_SHAPE_CONSERVATION_DAMPING_MAP | LINK |  |  |  | 
Elastic Limit | RIGID_BODY_SB_SHAPE_CONSERVATION_ELASTIC_LIMIT | REAL | 0.0 |  |  | 
Map | RIGID_BODY_SB_SHAPE_CONSERVATION_ELASTIC_LIMIT_MAP | LINK |  |  |  | 
Pressure | RIGID_BODY_SB_PRESSURE_GROUP | SEPARATOR |  |  |  | 
Pressure | RIGID_BODY_SB_PRESSURE | REAL |  |  |  | 
Volume Conservation | RIGID_BODY_SB_VOLUME_CONSERVATION | REAL | 0.0 |  |  | 
Damping | RIGID_BODY_SB_PRESSURE_DAMPING | REAL | 0.0 |  |  | 
Local Coordinates | RIGID_BODY_CACHE_LOCAL | BOOL |  |  |  | 
Include Collision Data | RIGID_BODY_CACHE_INCLUDE_COLLISIONS | BOOL |  |  |  | 
Bake Object | RIGID_BODY_CACHE_BAKE | BUTTON |  |  |  | 
Bake All | RIGID_BODY_CACHE_BAKE_ALL | BUTTON |  |  |  | 
Clear Object Cache | RIGID_BODY_CACHE_CLEAR | BUTTON |  |  |  | 
Clear All Caches | RIGID_BODY_CACHE_CLEAR_ALL | BUTTON |  |  |  | 
Memory | RIGID_BODY_CACHE_MEMORY | STATICTEXT |  |  |  | 
Use Cached Data | RIGID_BODY_CACHE_USE | BOOL |  |  |  | 
