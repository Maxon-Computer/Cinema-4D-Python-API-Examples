# Description: Dynamics

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/dynamics/description/dynworldobject.res`
- **Symbol:** `DynWorldObject`
- **Category:** Other

Use parameter symbols to access parameters and cycle option symbols for cycle values, never their numeric IDs. Treat Min and Max as constraints and Default as the declared initial value; blank cells mean the resource does not declare that metadata, not that the value is zero. Base Description Parameters lists inherited fields from each base; All Parameters lists the effective parameter set for this description.

## Base Description Parameters

No base descriptions.

## All Parameters

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Enabled | WORLD_ENABLED | BOOL |  |  |  | 
Disable on Skip Frame | WORLD_DISABLE_DURING_LEAP | BOOL |  |  |  | 
Time Scale | WORLD_TIMESCALE | REAL | 0 |  |  | 
Gravity | WORLD_GRAVITY | REAL |  |  |  | 
Density | WORLD_DENSITY | REAL | 0.0 |  |  | 
Air Density | WORLD_AIR_DENSITY | REAL | 0.0 |  |  | 
Bake | WORLD_CACHE_BAKE | BUTTON |  |  |  | 
Clear Cache | WORLD_CACHE_CLEAR | BUTTON |  |  |  | 
Memory | WORLD_CACHE_MEMORY | STATICTEXT |  |  |  | 
Use Cached Data | WORLD_CACHE_USE | BOOL |  |  |  | 
Disable Cached Objects for Simulation | WORLD_CACHE_DISABLE_BAKED_OBJECTS | BOOL |  |  |  | 
Use | WORLD_CACHE_USE_TIME | BOOL |  |  |  | 
Playback Time | WORLD_CACHE_TIME | BASETIME |  |  |  | 
Collision Margin | WORLD_MARGIN | REAL | 0.0 |  |  | 
Scale | WORLD_SCALE | REAL | 0.0 |  |  | 
Restitution Lifetime for Resting Contact | WORLD_CONTACT_RESTITUTION_LIFETIME | REAL | 0.0 |  |  | 
Random Seed | WORLD_SEED | LONG |  |  |  | 
Steps per Frame | WORLD_SUBSTEPS | LONG | 1 | 1000 |  | 
Maximum Solver Iterations per Step | WORLD_ITERATIONS | LONG | 3 | 10000 |  | 
Error Threshold | WORLD_ERROR_THRESHOLD | REAL | 0.1 | 100 |  | 
Enable | WORLD_VISUALIZE | BOOL |  |  |  | 
Collision Shapes | WORLD_VISUALIZE_SHAPES | BOOL |  |  |  | 
Bounding Boxes | WORLD_VISUALIZE_AABBS | BOOL |  |  |  | 
Contact Points | WORLD_VISUALIZE_CONTACT_POINTS | BOOL |  |  |  | 
Connectors | WORLD_VISUALIZE_CONSTRAINTS | BOOL |  |  |  | 
