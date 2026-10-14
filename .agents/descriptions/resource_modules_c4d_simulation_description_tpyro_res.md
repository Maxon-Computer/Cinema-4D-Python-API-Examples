# Description: Pyro Emitter

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/c4d_simulation/description/tpyro.res`
- **Symbol:** `tpyro`
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
Enabled | PYRO_TAG_EMITTER_ENABLED | BOOL |  |  |  | 
Object Fidelity | PYRO_TAG_OBJECT_VOXEL_SIZE | REAL | 0.0 | 100.0 | 2.5 | 
Substep Mode | PYRO_TAG_SUBSTEP_MODE | LONG |  |  |  | PYRO_TAG_SUBSTEP_MODE_DISCRETE; PYRO_TAG_SUBSTEP_MODE_CONTINUOUS
Keep Domain Static | PYRO_TAG_NO_REQUESTS | BOOL |  |  |  | 
Substeps | PYRO_TAG_SUBSTEPS | LONG | 0 | 100 |  | 
Emission Type | PYRO_TAG_EMISSION_TYPE | LONG |  |  |  | PYRO_TAG_EMISSION_TYPE_SURFACE; PYRO_TAG_EMISSION_TYPE_VOLUME; PYRO_TAG_EMISSION_TYPE_PARTICLE; PYRO_TAG_EMISSION_TYPE_SURFACE_DYNAMIC; PYRO_TAG_EMISSION_TYPE_SURFACE_NANO; PYRO_TAG_EMISSION_TYPE_VOLUME_NANO
Thickness | PYRO_TAG_SURFACE_THICKNESS | REAL | 0.0 | 10000.0 |  | 
Emission Falloff | PYRO_TAG_EMISSION_VOXEL_FALLOFF | REAL | 0.0 | 256.0 |  | 
Emission Map | PYRO_TAG_SURFACE_WEIGHTS_GLOBAL | STRING |  |  |  | 
Attribute | PYRO_TAG_SURFACE_WEIGHTS_GLOBAL_POPUP | POPUP |  |  |  | 
Density Enabled | PYRO_TAG_DENSITY_ENABLED | BOOL |  |  |  | 
Density Map | PYRO_TAG_SURFACE_WEIGHTS_DENSITY | STRING |  |  |  | 
Attribute | PYRO_TAG_SURFACE_WEIGHTS_DENSITY_POPUP | POPUP |  |  |  | 
Density Set | PYRO_TAG_DENSITY_MIN | REAL | 0.0 | 50000.0 |  | 
Density Add | PYRO_TAG_DENSITY_ADD | REAL |  |  |  | 
Color Enabled | PYRO_TAG_DENSITY_COLOR_ENABLED | BOOL |  |  |  | 
Color Map | PYRO_TAG_SURFACE_WEIGHTS_COLOR | STRING |  |  |  | 
Attribute | PYRO_TAG_SURFACE_WEIGHTS_COLOR_POPUP | POPUP |  |  |  | 
Color | PYRO_TAG_DENSITY_COLOR | COLOR |  |  |  | 
Weight | PYRO_TAG_DENSITY_COLOR_ALPHA | REAL | 0.0 |  |  | 
Override | PYRO_TAG_DENSITY_COLOR_SET | BOOL |  |  |  | 
Temperature Enabled | PYRO_TAG_TEMPERATURE_ENABLED | BOOL |  |  |  | 
Temperature Map | PYRO_TAG_SURFACE_WEIGHTS_TEMPERATURE | STRING |  |  |  | 
Attribute | PYRO_TAG_SURFACE_WEIGHTS_TEMPERATURE_POPUP | POPUP |  |  |  | 
Temperature Set | PYRO_TAG_TEMPERATURE_MIN | REAL | 0.0 | 50000.0 |  | 
Temperature Add | PYRO_TAG_TEMPERATURE_ADD | REAL |  |  |  | 
Fuel Enabled | PYRO_TAG_FUEL_ENABLED | BOOL |  |  |  | 
Fuel Map | PYRO_TAG_SURFACE_WEIGHTS_FUEL | STRING |  |  |  | 
Attribute | PYRO_TAG_SURFACE_WEIGHTS_FUEL_POPUP | POPUP |  |  |  | 
Fuel Type | PYRO_TAG_FUEL_TYPE | LONG |  |  |  | PYRO_TAG_FUEL_TYPE_CONTINUOUS; PYRO_TAG_FUEL_TYPE_ONESHOT; PYRO_TAG_FUEL_TYPE_CONTINGENT
Fuel Set | PYRO_TAG_FUEL_MIN | REAL |  |  |  | 
Fuel Add | PYRO_TAG_FUEL_ADD | REAL |  |  |  | 
Match Burning Rate | PYRO_TAG_FUEL_MATCH_BURNING_RATE | BOOL |  |  |  | 
Constant Pressure | PYRO_TAG_FUEL_CONSTANT_PRESSURE | BOOL |  |  |  | 
Burning Rate | PYRO_TAG_FUEL_BURNING_RATE | REAL | 0.0 | 1000.0 |  | 
Initial Contingent | PYRO_TAG_FUEL_INITIAL_CONTINGENT | REAL | 0.0 | 1000.0 |  | 
Emission Frame Start | PYRO_TAG_FUEL_TARGET_FRAME | LONG | 0 |  |  | 
Emission Frame End | PYRO_TAG_FUEL_TARGET_FRAME_END | LONG | 0 |  |  | 
Velocity Enabled | PYRO_TAG_VELOCITY_ENABLED | BOOL |  |  |  | 
Type | PYRO_TAG_VELOCITY_TYPE | LONG |  |  |  | PYRO_TAG_VELOCITY_TYPE_ADD; PYRO_TAG_VELOCITY_TYPE_ABSOLUTE; PYRO_TAG_VELOCITY_TYPE_DIRECTION; PYRO_TAG_VELOCITY_TYPE_MOVEMENT
Strength | PYRO_TAG_VELOCITY_STRENGTH | REAL |  |  |  | 
Direction | PYRO_TAG_VELOCITY_DIRECTION | VECTOR | -100.0 | 100.0 |  | 
Coordinate System | PYRO_TAG_VELOCITY_SPACE | LONG |  |  |  | PYRO_TAG_VELOCITY_SPACE_LOCAL; PYRO_TAG_VELOCITY_SPACE_GLOBAL
Custom Normals | PYRO_TAG_VELOCITY_SPACE_CUSTOM_NORMAL | BOOL |  |  |  | 
Divergence Add | PYRO_TAG_DIVERGENCE_CONTROL_STRENGTH | REAL |  |  |  | 
Noise Enabled | PYRO_TAG_NOISE_ENABLED | BOOL |  |  |  | 
Seed | PYRO_TAG_NOISE_SCALE_SEED | LONG |  |  |  | 
Noise Type | PYRO_TAG_NOISE_MODE | LONG |  |  |  | PYRO_TAG_NOISE_MODE_BOX; PYRO_TAG_NOISE_MODE_BLISTEREDTURBULENCE; PYRO_TAG_NOISE_MODE_BUYA; PYRO_TAG_NOISE_MODE_CELL; PYRO_TAG_NOISE_MODE_CRANAL; PYRO_TAG_NOISE_MODE_DENTS; PYRO_TAG_NOISE_MODE_DISPLACEDTURBULENCE; PYRO_TAG_NOISE_MODE_ELECTRIC; PYRO_TAG_NOISE_MODE_GASEOUS; PYRO_TAG_NOISE_MODE_HAMA; PYRO_TAG_NOISE_MODE_LUKA; PYRO_TAG_NOISE_MODE_MOD; PYRO_TAG_NOISE_MODE_NAKI; PYRO_TAG_NOISE_MODE_NUTOUS; PYRO_TAG_NOISE_MODE_OBER; PYRO_TAG_NOISE_MODE_PERLIN; PYRO_TAG_NOISE_MODE_PEZO; PYRO_TAG_NOISE_MODE_POXO; PYRO_TAG_NOISE_MODE_SEMA; PYRO_TAG_NOISE_MODE_STUPL; PYRO_TAG_NOISE_MODE_TURBULENCE; PYRO_TAG_NOISE_MODE_VL; PYRO_TAG_NOISE_MODE_WAVYTURBULENCE; PYRO_TAG_NOISE_MODE_ZADA
Noise Space | PYRO_TAG_NOISE_SPACE | LONG |  |  |  | PYRO_TAG_NOISE_SPACE_LOCAL; PYRO_TAG_NOISE_SPACE_GLOBAL
Octaves | PYRO_TAG_NOISE_OCTAVES | REAL | 1.0 | 20.0 |  | 
Relative Scale | PYRO_TAG_NOISE_GLOBAL_SCALE | VECTOR |  |  |  | 
Scale | PYRO_TAG_NOISE_SCALE | REAL |  |  |  | 
Animation Speed | PYRO_TAG_NOISE_FREQUENCY | REAL |  |  |  | 
Loop Period | PYRO_TAG_NOISE_LOOP_PERIOD | REAL | 0.0 |  |  | 
Uniform per Quantity | PYRO_TAG_NOISE_UNIFORM | BOOL |  |  |  | 
Movement | PYRO_TAG_NOISE_MOVEMENT | VECTOR |  |  |  | 
Speed | PYRO_TAG_NOISE_SPEED | REAL |  |  |  | 
Low Clip | PYRO_TAG_NOISE_MIN | REAL | 0.0 | 100.0 |  | 
High Clip | PYRO_TAG_NOISE_MAX | REAL | 0.0 | 100.0 |  | 
Brightness | PYRO_TAG_NOISE_BRIGHTNESS | REAL | -100.0 | 100.0 |  | 
Contrast | PYRO_TAG_NOISE_CONTRAST | REAL | -100.0 | 100.0 |  | 
