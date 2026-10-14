# Description: Emitter

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/c4d_simulation/description/temitter.res`
- **Symbol:** `temitter`
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
Simulation | EMITTER_PBD_SIMULATION_PRIORITY | PRIORITY |  |  |  | 
Enable | EMITTER_PBD_USE | BOOL |  |  |  | 
Density | EMITTER_PBD_MASS_DENSITY | REAL | 0.0 |  |  | 
Mass | EMITTER_PBD_MASS | REAL | 0.0001 |  | 1.0 | 
Radius | EMITTER_PBD_RADIUS | REAL | 0.0001 |  | 1.5 | 
Radius Variance | EMITTER_PBD_RADIUS_VARIANCE | REAL | 0.0 |  | 0.0 | 
Viscosity | EMITTER_PBD_VISCOSITY | REAL | 0.0 | 1.0 |  | 
Phase | EMITTER_PBD_PHASE | LONG | 0 |  |  | 
Type | EMITTER_PBD_TYPE | LONG |  |  | EMITTER_PBD_TYPE_LIQUID | EMITTER_PBD_TYPE_FREE; EMITTER_PBD_TYPE_LIQUID; EMITTER_PBD_TYPE_GRAINS
Infinite Time | EMITTER_PBD_LIFETIME_INFINITE_TIME | BOOL |  |  |  | 
Expectation | EMITTER_PBD_LIFETIME_EXPECTATION | BASETIME | 0 |  |  | 
Variance | EMITTER_PBD_LIFETIME_VARIANCE | BASETIME | 0 |  |  | 
Infinite Distance | EMITTER_PBD_LIFETIME_INFINITE_DISTANCE | BOOL |  |  |  | 
Expectation | EMITTER_PBD_MAXTRAVELED | REAL | 0.0 |  |  | 
Variance | EMITTER_PBD_MAXTRAVELED_VARIANCE | REAL | 0.0 |  |  | 
Override | EMITTER_PBD_DAMPING_OVERRIDE | BOOL |  |  |  | 
Strength | EMITTER_PBD_DAMPING | REAL | 0.0 |  |  | 
Friction | EMITTER_PBD_FRICTION | REAL | 0.0 |  |  | 
Bounciness | EMITTER_PBD_BOUNCINESS | REAL | 0.0 |  |  | 
Stickiness | EMITTER_PBD_STICKINESS | REAL | 0.0 |  |  | 
Enable | EMITTER_PBD_EMISSION_ENABLE | BOOL |  |  |  | 
From | EMITTER_PBD_EMISSION_FROM | LONG |  |  | EMITTER_PBD_EMISSION_FROM_SURFACE | EMITTER_PBD_EMISSION_FROM_POINTS; EMITTER_PBD_EMISSION_FROM_SURFACE; EMITTER_PBD_EMISSION_FROM_VOLUME
Mode | EMITTER_PBD_EMISSION_MODE | LONG |  |  | EMITTER_PBD_EMISSION_MODE_SHOT | EMITTER_PBD_EMISSION_MODE_SHOT; EMITTER_PBD_EMISSION_MODE_CONSTANT; EMITTER_PBD_EMISSION_MODE_PULSE
Rate | EMITTER_PBD_EMISSION_RATE | LONG | 1 |  |  | 
Seed | EMITTER_PBD_EMISSION_SEED | LONG | 0 |  |  | 
Speed | EMITTER_PBD_INITIALVELOCITY_SPEED | REAL |  |  | 100.0 | 
Speed Variance | EMITTER_PBD_INITIALVELOCITY_SPEED_VARIATION | REAL |  |  | 0 | 
Add Emitter Velocity	 | EMITTER_PBD_INITIALVELOCITY_ADDSOURCEVELOCITY | REAL |  |  | 0.0 | 
Linear | EMITTER_PBD_INITIALVELOCITY_ADDSOURCEVELOCITY_LINEAR | REAL |  |  | 0.0 | 
Angular | EMITTER_PBD_INITIALVELOCITY_ADDSOURCEVELOCITY_ANGULAR | REAL |  |  | 0.0 | 
Mode | EMITTER_PBD_FORCES_INEXMODE | LONG |  |  | EMITTER_PBD_FORCES_INEXMODE_EXCLUDE | EMITTER_PBD_FORCES_INEXMODE_INCLUDE; EMITTER_PBD_FORCES_INEXMODE_EXCLUDE
Objects | EMITTER_PBD_FORCES_INEXCLUDE | IN_EXCLUDE |  |  |  | 
Pyro | EMITTER_PBD_FORCES_INEX_PYRO | BOOL |  |  |  | 
Cache Mode | EMITTER_PBD_CACHE_ENABLE | BOOL |  |  |  | 
Start | EMITTER_PBD_CACHE_START | BASETIME |  |  |  | 
Calculate Cache | EMITTER_PBD_DO_CALCULATE | BUTTON |  |  |  | 
Cache Scene | EMITTER_PBD_DO_CALCULATE_ALL | BUTTON |  |  |  | 
Clear Cache | EMITTER_PBD_DELCACHE | BUTTON |  |  |  | 
Clear Cache Scene | EMITTER_PBD_DELCACHE_ALL | BUTTON |  |  |  | 
Update Frame | EMITTER_PBD_CACHE_FRAME | BUTTON |  |  |  | 
Draw | EMITTER_PBD_DRAW | BOOL |  |  |  | 
Draw Radius | EMITTER_PBD_DRAW_RADIUS | BOOL |  |  |  | 
Draw Velocity | EMITTER_PBD_DRAW_VELOCITY | BOOL |  |  |  | 
Normalized | EMITTER_PBD_DRAW_VELOCITY_NORMALIZED | BOOL |  |  |  | 
Mode | EMITTER_PBD_COLORS_MODE | LONG |  |  | EMITTER_PBD_COLORS_MODE_CONSTANT | EMITTER_PBD_COLORS_MODE_CONSTANT; EMITTER_PBD_COLORS_MODE_DIRECTION; EMITTER_PBD_COLORS_MODE_MAP
Color | EMITTER_PBD_COLORS_CONSTANT | COLOR |  |  |  | 
Color Map | EMITTER_PBD_COLORS_MAP | STRING |  |  |  | 
