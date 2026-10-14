# Description: Compositing Tag

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/c4d_base/description/tcompositing.res`
- **Symbol:** `Tcompositing`
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
Cast Shadows | COMPOSITINGTAG_CASTSHADOW | BOOL |  |  |  | 
Receive Shadows | COMPOSITINGTAG_RECEIVESHADOW | BOOL |  |  |  | 
Self Shadowing | COMPOSITINGTAG_SELFSHADOW | BOOL |  |  |  | 
Seen by Camera | COMPOSITINGTAG_SEENBYCAMERA | BOOL |  |  |  | 
Seen by Rays | COMPOSITINGTAG_SEENBYRAYS | BOOL |  |  |  | 
Seen by GI | COMPOSITINGTAG_SEENBYGI | BOOL |  |  |  | 
Compositing Background | COMPOSITINGTAG_BACKGROUND | BOOL |  |  |  | 
Compositing Background for HDR Maps | COMPOSITINGTAG_BACKGROUND_GI | BOOL |  |  |  | 
Seen by Transparency | COMPOSITINGTAG_SEENBYTRANSPARENCY | BOOL |  |  |  | 
Seen by Refraction | COMPOSITINGTAG_SEENBYREFRACTION | BOOL |  |  |  | 
Seen by Reflection | COMPOSITINGTAG_SEENBYREFLECTION | BOOL |  |  |  | 
Seen by AO | COMPOSITINGTAG_SEENBYAO | BOOL |  |  |  | 
Force Antialiasing | COMPOSITINGTAG_AAOVERWRITE | BOOL |  |  |  | 
Antialiasing Min | COMPOSITINGTAG_AAMINLEVEL | LONG |  |  |  | COMPOSITINGTAG_AALEVEL_1; COMPOSITINGTAG_AALEVEL_2; COMPOSITINGTAG_AALEVEL_4; COMPOSITINGTAG_AALEVEL_8; COMPOSITINGTAG_AALEVEL_16
Antialiasing Max | COMPOSITINGTAG_AAMAXLEVEL | LONG |  |  |  | COMPOSITINGTAG_AALEVEL_1; COMPOSITINGTAG_AALEVEL_2; COMPOSITINGTAG_AALEVEL_4; COMPOSITINGTAG_AALEVEL_8; COMPOSITINGTAG_AALEVEL_16
Antialiasing Threshold | COMPOSITINGTAG_AATHRESHOLD | REAL | 0 | 100 |  | 
Matte Object | COMPOSITINGTAG_MATTEOBJECT | BOOL |  |  |  | 
Matte Color | COMPOSITINGTAG_MATTECOLOR | COLOR |  |  |  | 
Enable GI Parameters | COMPOSITINGTAG_GIENABLED | BOOL |  |  |  | 
Intensity Ratio | COMPOSITINGTAG_GIINTENSITY | REAL | 0.0 | 1000.0 |  | 
Stochastic Samples Ratio | COMPOSITINGTAG_GIQUALITY | REAL | 1.0 | 1000.0 |  | 
Record Density Ratio | COMPOSITINGTAG_GIDENSITY | REAL | 1.0 | 1000.0 |  | 
Enable Forced QMC Sampling | COMPOSITINGTAG_GIQMC | BOOL |  |  |  | 
Enable Transparency Overlook | COMPOSITINGTAG_GITRANSPARENCY | BOOL |  |  |  | 
Enable Interpolation Grouping | COMPOSITINGTAG_GIINTERPOLATION | BOOL |  |  |  | 
Mode | COMPOSITINGTAG_EXCLUSION_MODE | LONG |  |  |  | COMPOSITINGTAG_EXCLUSION_MODE_INCLUDE; COMPOSITINGTAG_EXCLUSION_MODE_EXCLUDE
Objects | COMPOSITINGTAG_EXCLUSION_LIST | IN_EXCLUDE |  |  |  | 
Enable Buffer A | COMPOSITINGTAG_ENABLECHN0 | BOOL |  |  |  | 
Object Buffer A | COMPOSITINGTAG_IDCHN0 | LONG | 1 | 10000 |  | 
Enable Buffer B | COMPOSITINGTAG_ENABLECHN1 | BOOL |  |  |  | 
Object Buffer B | COMPOSITINGTAG_IDCHN1 | LONG | 1 | 10000 |  | 
Enable Buffer C | COMPOSITINGTAG_ENABLECHN2 | BOOL |  |  |  | 
Object Buffer C | COMPOSITINGTAG_IDCHN2 | LONG | 1 | 10000 |  | 
Enable Buffer D | COMPOSITINGTAG_ENABLECHN3 | BOOL |  |  |  | 
Object Buffer D | COMPOSITINGTAG_IDCHN3 | LONG | 1 | 10000 |  | 
Enable Buffer E | COMPOSITINGTAG_ENABLECHN4 | BOOL |  |  |  | 
Object Buffer E | COMPOSITINGTAG_IDCHN4 | LONG | 1 | 10000 |  | 
Enable Buffer F | COMPOSITINGTAG_ENABLECHN5 | BOOL |  |  |  | 
Object Buffer F | COMPOSITINGTAG_IDCHN5 | LONG | 1 | 10000 |  | 
Enable Buffer G | COMPOSITINGTAG_ENABLECHN6 | BOOL |  |  |  | 
Object Buffer G | COMPOSITINGTAG_IDCHN6 | LONG | 1 | 10000 |  | 
Enable Buffer H | COMPOSITINGTAG_ENABLECHN7 | BOOL |  |  |  | 
Object Buffer H | COMPOSITINGTAG_IDCHN7 | LONG | 1 | 10000 |  | 
Enable Buffer I | COMPOSITINGTAG_ENABLECHN8 | BOOL |  |  |  | 
Object Buffer I | COMPOSITINGTAG_IDCHN8 | LONG | 1 | 10000 |  | 
Enable Buffer J | COMPOSITINGTAG_ENABLECHN9 | BOOL |  |  |  | 
Object Buffer J | COMPOSITINGTAG_IDCHN9 | LONG | 1 | 10000 |  | 
Enable Buffer K | COMPOSITINGTAG_ENABLECHN10 | BOOL |  |  |  | 
Object Buffer K | COMPOSITINGTAG_IDCHN10 | LONG | 1 | 10000 |  | 
Enable Buffer L | COMPOSITINGTAG_ENABLECHN11 | BOOL |  |  |  | 
Object Buffer L | COMPOSITINGTAG_IDCHN11 | LONG | 1 | 10000 |  | 
