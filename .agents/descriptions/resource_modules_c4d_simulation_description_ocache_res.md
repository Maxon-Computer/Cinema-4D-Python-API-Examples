# Description: Cache

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/c4d_simulation/description/ocache.res`
- **Symbol:** `ocache`
- **Category:** Other

Use parameter symbols to access parameters and cycle option symbols for cycle values, never their numeric IDs. Treat Min and Max as constraints and Default as the declared initial value; blank cells mean the resource does not declare that metadata, not that the value is zero. Base Description Parameters lists inherited fields from each base; All Parameters lists the effective parameter set for this description.

## Base Description Parameters

No base descriptions.

## All Parameters

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Cache Mode | SIMULATION_CACHE_ENABLED | BOOL |  |  |  | 
Cache Location | SIMULATION_CACHE_LOCATION | LONG |  |  |  | SIMULATION_CACHE_EXTERNAL; SIMULATION_CACHE_INTERNAL
Cache Space | SIMULATION_CACHE_SPACE | LONG |  |  |  | SIMULATION_CACHE_SPACE_LOCAL; SIMULATION_CACHE_SPACE_GLOBAL
Path to Alembic File | SIMULATION_CACHE_EXTERNAL_PATH | FILENAME |  |  |  | 
Identifier | SIMULATION_CACHE_EXTERNAL_IDENTIFIER | STRING |  |  |  | 
Scale | SIMULATION_IMPORT_UNIT_SCALE | UNITSCALE |  |  |  | 
No label | SIMULATION_CACHE_CUSTOM_SEPARATOR | SEPARATOR |  |  |  | 
Cache Object | SIMULATION_DO_CALCULATE | BUTTON |  |  |  | 
Cache Scene | SIMULATION_DO_CALCULATE_ALL | BUTTON |  |  |  | 
Clear Object Cache | SIMULATION_DELCACHE | BUTTON |  |  |  | 
Clear Scene Cache | SIMULATION_DELCACHE_ALL | BUTTON |  |  |  | 
Use Animation | SIMULATION_ANIMATION_ENABLED | BOOL |  |  |  | 
Frame | SIMULATION_ANIMATION_FRAME | BASETIME |  |  |  | 
Offset | SIMULATION_CACHE_START | BASETIME |  |  |  | 
Speed | SIMULATION_SPEED | REAL | 0.0 |  |  | 
Mode | SIMULATION_REPLAY_MODE | LONG |  |  | SIMULATION_REPLAY_MODE_PLAY | SIMULATION_REPLAY_MODE_PLAY; SIMULATION_REPLAY_MODE_LOOP; SIMULATION_REPLAY_MODE_PINGPONG
Interpolation | SIMULATION_CACHE_POSITION_INTERPOLATION | LONG |  |  | SIMULATION_CACHE_POSITION_INTERPOLATION_CUBIC | SIMULATION_CACHE_POSITION_INTERPOLATION_LINEAR; SIMULATION_CACHE_POSITION_INTERPOLATION_CUBIC; SIMULATION_CACHE_POSITION_INTERPOLATION_CUBIC_MONOTONE
Tangent Scale | SIMULATION_CACHE_POSITION_INTERPOLATION_CUBIC_WEIGHT | REAL | 0.0 |  |  | 
Remapping Curve | SIMULATION_ANIMATION_CURVE | SPLINE |  |  |  | 
Convert Object Cache to Alembic | SIMULATION_DO_CONVERT_CACHE | BUTTON |  |  |  | 
Convert Scene Cache to Alembic | SIMULATION_DO_CONVERT_CACHE_ALL | BUTTON |  |  |  | 
