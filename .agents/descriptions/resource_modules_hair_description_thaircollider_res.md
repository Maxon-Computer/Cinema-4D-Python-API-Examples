# Description: Collider

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/hair/description/thaircollider.res`
- **Symbol:** `Thaircollider`
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
Collisions | HAIR_COLLIDER_COLLISIONS | BOOL |  |  |  | 
Friction | HAIR_COLLIDER_FRICTION | REAL | 0.0 | 100.0 |  | 
Bounciness | HAIR_COLLIDER_BOUNCE | REAL | 0.0 |  |  | 
Forces | HAIR_COLLIDER_FORCES | BOOL |  |  |  | 
Radius | HAIR_COLLIDER_FORCES_OBJECTS_RADIUS | REAL | 0.0 |  |  | 
Strength | HAIR_COLLIDER_FORCE_STRENGTH | REAL |  |  |  | 
Max Strength | HAIR_COLLIDER_FORCES_OBJECTS_MAXSTRENGTH | REAL |  |  |  | 
Falloff | HAIR_COLLIDER_FORCES_OBJECTS_FALLOFF | LONG |  |  |  | HAIR_COLLIDER_FORCES_FALLOFF_CONSTANT; HAIR_COLLIDER_FORCES_FALLOFF_LINEAR; HAIR_COLLIDER_FORCES_FALLOFF_SQUARE; HAIR_COLLIDER_FORCES_FALLOFF_CUBIC; HAIR_COLLIDER_FORCES_FALLOFF_CUSTOM
Custom | HAIR_COLLIDER_FORCES_OBJECTS_FALLOFF_SPLINE | SPLINE |  |  |  | 
Restrict | HAIR_COLLIDER_LINK | LINK |  |  |  | 
Strength | HAIR_COLLIDER_FORCE_STRENGTH_LINK | LINK |  |  |  | 
