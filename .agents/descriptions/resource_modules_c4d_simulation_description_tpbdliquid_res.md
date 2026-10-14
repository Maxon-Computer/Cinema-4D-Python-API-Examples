# Description: Liquid

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/c4d_simulation/description/tpbdliquid.res`
- **Symbol:** `tpbdliquid`
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
Simulation | PBD_LIQUID_SIMULATION_PRIORITY | PRIORITY |  |  |  | 
Enable | PBD_LIQUID_USE | BOOL |  |  |  | 
Liquid Contribution | PBD_LIQUID_SIMULATE | REAL | 0.0 | 100.0 |  | 
Use Liquid Default | PBD_LIQUID_RADIUS_USE_DEFAULT | BOOL |  |  |  | 
Target Density | PBD_LIQUID_CONSTRAINTS_MASSDENSITY | REAL | 0.0001 |  |  | 
Viscosity | PBD_LIQUID_CONSTRAINTS_VISCOSITY | REAL | 0.0 |  |  | 
Surface Tension | PBD_LIQUID_CONSTRAINTS_SURFACE_TENSION | REAL | 0.0 |  |  | 
Mixture ID | PBD_LIQUID_CONSTRAINTS_MIXTURE | LONG | 0 |  |  | 
Ease In | PBD_LIQUID_CONSTRAINTS_EASEIN | BASETIME | 0 |  | 0 | 
Friction | PBD_LIQUID_COLLISIONS_FRICTION | REAL | 0.0 |  |  | 
Stickiness | PBD_LIQUID_COLLISIONS_STICKINESS | REAL | 0.0 |  |  | 
Override | PBD_LIQUID_DAMPING_OVERRIDE | BOOL |  |  |  | 
Strength | PBD_LIQUID_DAMPING_STRENGTH | REAL | 0.0 |  |  | 
