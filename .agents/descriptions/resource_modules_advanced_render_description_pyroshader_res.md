# Description: PyroCluster

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/advanced_render/description/pyroshader.res`
- **Symbol:** `PyroShader`
- **Category:** Materials

Use parameter symbols to access parameters and cycle option symbols for cycle values, never their numeric IDs. Treat Min and Max as constraints and Default as the declared initial value; blank cells mean the resource does not declare that metadata, not that the value is zero. Base Description Parameters lists inherited fields from each base; All Parameters lists the effective parameter set for this description.

## Base Description Parameters

### No label (`Mpreview`)

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
No label | MATERIAL_PREVIEW | MATPREVIEW |  |  |  | 

### Material (`Mbase`)

No parameters.

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
No label | MATERIAL_PREVIEW | MATPREVIEW |  |  |  | 
Icon File / ID | ID_BASELIST_ICON_FILE | TEXTURE |  |  |  | 
Icon Color | ID_BASELIST_ICON_COLORIZE_MODE | BOOL |  |  |  | 
Color | ID_BASELIST_ICON_COLOR | COLOR |  |  | 1.0 0.9 0.4 | 
No label | ID_BASELIST_ICON_PRESET_BUTTONS | ICONCHOOSER |  |  |  | 
Name | ID_BASELIST_NAME | STRING |  |  |  | 
Layer | ID_LAYER_LINK | LINK |  |  |  | 
No label | ID_BASELIST_NODESPACE_ADD_REMOVE_BUTTONS | NODESPACE_ADD_REMOVE |  |  |  | 
Globals | PYRO_PAGE_GLOBALS | BOOL |  |  |  | 
Age | PYRO_PAGE_AGE | BOOL |  |  |  | 
Distance | PYRO_PAGE_DIST | BOOL |  |  |  | 
Cyl. Distance | PYRO_PAGE_RADDIST | BOOL |  |  |  | 
Shape | PYRO_PAGE_SHP | BOOL |  |  |  | 
Illumination | PYRO_PAGE_IL | BOOL |  |  |  | 
Shadow | PYRO_PAGE_SH | BOOL |  |  |  | 
Noise | PYRO_PAGE_FF | BOOL |  |  |  | 
On | PS_ON | BOOL |  |  |  | 
Preview... | PS_PREVIEW | BUTTON |  |  |  | 
Volume | PS_SAMPLES | REAL | 1.0 | 100.0 |  | 
Luminosity | PS_PARTLUM | REAL | 0.0 | 100.0 |  | 
Density | PS_DENSITY | REAL | 0.0 |  |  | 
Color | PS_GRADPART | GRADIENT |  |  |  | 
Gradient Mode | PS_GRADMODE | LONG |  |  |  | GRAD_MODE_FLAT; GRAD_MODE_LOCAL; GRAD_MODE_WORLD; GRAD_MODE_DENSITY
Min | PS_GRADMIN | REAL | 0.0 |  |  | 
Max | PS_GRADMAX | REAL | 0.0 |  |  | 
Use Intersection | PS_INTERSECT | BOOL |  |  |  | 
Ray Bias | PS_ISECTBIAS | REAL | 0.0 |  |  | 
Settings | PS_SETTINGS | LONG |  |  |  | PS_SET_FIRE; PS_SET_VOLCANO; PS_SET_CLOUD; PS_SET_STEAM; PS_SET_FIREBALL; PS_SET_SMOKE; PS_SET_USER
Use Age Effects | PS_AGEON | BOOL |  |  |  | 
Radius | PS_AGERAD | GRADIENT |  |  |  | 
Luminosity | PS_AGEPLUM | GRADIENT |  |  |  | 
Color Mix | PS_AGEMIX | GRADIENT |  |  |  | 
Color | PS_GRADLIFE | GRADIENT |  |  |  | 
Use Distance Effects | PS_USEDIST | BOOL |  |  |  | 
Use Emitter Plane | PS_USEEPLANE | BOOL |  |  |  | 
Near Range | PS_NEARDIST | REAL | 0.0 |  |  | 
Far Range | PS_FARDIST | REAL | 0.0 |  |  | 
Radius | PS_DISTRAD | GRADIENT |  |  |  | 
Luminosity | PS_DISTPLUM | GRADIENT |  |  |  | 
Color Mix | PS_DISTMIX | GRADIENT |  |  |  | 
Color | PS_DISTGRAD | GRADIENT |  |  |  | 
Use Cylindrical Distance Effects | PS_USERADDIST | BOOL |  |  |  | 
Emitter Direction | PS_EMITTERDIR | LONG |  |  |  | PS_EMITTERDIR_X; PS_EMITTERDIR_Y; PS_EMITTERDIR_Z
Near Range | PS_NEARRADDIST | REAL | 0.0 |  |  | 
Far Range | PS_FARRADDIST | REAL | 0.0 |  |  | 
Radius | PS_RADDISTRAD | GRADIENT |  |  |  | 
Luminosity | PS_RADDISTPLUM | GRADIENT |  |  |  | 
Color Mix | PS_RADDISTMIX | GRADIENT |  |  |  | 
Color | PS_RADDISTGRAD | GRADIENT |  |  |  | 
Type | PS_SHP_TYPE | LONG |  |  |  | PART_SHAPE_SPHERE; PART_SHAPE_CYLINDER; PART_SHAPE_BOX
Radius | PS_SHP_RADIUS | REAL | 0.0 |  |  | 
Use Hemisphere | PS_SHP_HEMI | BOOL |  |  |  | 
Hemisphere | PS_SHP_HEMILEN | REAL | 0.0 | 100.0 |  | 
Use Particle TM | PS_SHP_USETM | BOOL |  |  |  | 
Use Auto Rotation | PS_SHP_AUTOROT | BOOL |  |  |  | 
Rotation | PS_SHP_ROTVECTOR | VECTOR |  |  |  | 
Scale | PS_SHP_SCALE | VECTOR | 0.0 |  |  | 
Velocity Scale | PS_SHP_VELSCALE | VECTOR | 0.0 |  |  | 
Preview | PS_SHP_PREVIEW | BOOL |  |  |  | 
Max. Visible | PS_SHP_VISIBLE | LONG | 1 |  |  | 
Use Illumination | PS_IL_ON | BOOL |  |  |  | 
Mode | PS_IL_MODE | LONG |  |  |  | PS_IL_MODE_ISOTROPIC; PS_IL_MODE_RAYANGLE; PS_IL_MODE_BUMP
No label | PS_IL_HIGHLIGHT | BITMAPBUTTON |  |  |  | 
Self Illum. | PS_IL_SELF | REAL | 0.0 | 100.0 |  | 
Trans. Illum. | PS_IL_TRANS | REAL | 0.0 | 100.0 |  | 
Shininess | PS_IL_SHINY | REAL | 0.0 | 100.0 |  | 
Strength | PS_IL_STRENGTH | REAL | 0.0 |  |  | 
Soften | PS_IL_SOFTEN | REAL | 0.0 | 100.0 |  | 
Bump | PS_IL_BUMP | REAL |  |  |  | 
Receive Shadows | PS_SH_RECVSHADOWS | BOOL |  |  |  | 
Cast Shadows | PS_SH_CASTSHADOWS | BOOL |  |  |  | 
Self Shadows | PS_SH_SELFSHADOWS | BOOL |  |  |  | 
Transparency | PS_SH_TRANS | REAL | 0.0 | 100.0 |  | 
Ambient | PS_SH_AMBIENT | COLOR |  |  |  | 
Shadow Color Filter | PS_SH_CFILTER | BOOL |  |  |  | 
Use ShadowMaps Samples | PS_SH_MAPSAMPLESON | BOOL |  |  |  | 
Volume | PS_SH_MAPSAMPLES | REAL | 1.0 | 100.0 |  | 
Use Raytraced Samples | PS_SH_TRACEDSAMPLESON | BOOL |  |  |  | 
Volume | PS_SH_TRACEDSAMPLES | REAL | 1.0 | 100.0 |  | 
Darken Opacity | PS_SH_DARKALPHA | BOOL |  |  |  | 
Dark Factor | PS_SH_DARKFAC | REAL |  |  |  | 
Brightness | PS_SH_DARKBRIGHT | REAL | 0.0 |  |  | 
Self Shadow Options | PS_SH_USESELFOPT | BOOL |  |  |  | 
Bias | PS_SH_SELFBIAS | REAL | 0.0 |  |  | 
Smp. Range | PS_SH_SELFSAMPLES | REAL | 0.0 | 20.0 |  | 
Use Noise | PS_FFON | BOOL |  |  |  | 
Noise Type | PS_FF_TYPE | LONG |  |  |  | PS_FF_TYPE_GAS; PS_FF_TYPE_FIRE; PS_FF_TYPE_ELECTRIC; PS_FF_TYPE_REGULAR; PS_FF_TYPE_FRACTAL; PS_FF_TYPE_TURBULENCE; PS_FF_TYPE_FBM_FRACTAL; PS_FF_TYPE_FBM_TURBULENCE
Regularity | PS_FF_REGULAR | REAL | 0.0 | 100.0 |  | 
Grow Radius | PS_FF_GROWRAD | REAL | 0.0 | 100.0 |  | 
Scale | PS_FF_SCALE | REAL | 0.0 |  |  | 
Peak Blend | PS_FF_EXP | REAL |  |  |  | 
Detail | PS_FF_LEVEL | REAL | 1.0 | 5.0 |  | 
Phase | PS_FF_PHASE | REAL |  |  |  | 
Gain | PS_FF_GAIN | REAL | 0.0 | 100.0 |  | 
Bias | PS_FF_BIAS | REAL | 0.0 | 100.0 |  | 
Low Threshold | PS_FF_LOWTHRESH | REAL | 0.0 | 100.0 |  | 
High Threshold | PS_FF_HIGHTHRESH | REAL | 0.0 | 100.0 |  | 
Use Color | PS_FF_COLORON | BOOL |  |  |  | 
Color | PS_FF_COLOR | GRADIENT |  |  |  | 
Static Pos | PS_FF_PSTATIC | BOOL |  |  |  | 
No Scale | PS_FF_NOSCALE | BOOL |  |  |  | 
Invert Noise | PS_FF_INVERT | BOOL |  |  |  | 
