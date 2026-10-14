# Description: GI Physical Sky

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/advanced_render/description/mgirealsky.res`
- **Symbol:** `Mgirealsky`
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

### Assignment (`Massign`)

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Assignment | MATERIAL_PAGE_ASSIGNMENT | BOOL |  |  |  | 
No label | ID_MATERIALASSIGNMENTS | MATASSIGN |  |  |  | 

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
Location | GI_REAL_SKY_PAGE_LOCATION | BOOL |  |  |  | 
Global | GI_REAL_SKY_PAGE_GLOBAL | BOOL |  |  |  | 
Sky | GI_REAL_SKY_PAGE_SKY | BOOL |  |  |  | 
Sun | GI_REAL_SKY_PAGE_SUN | BOOL |  |  |  | 
Atm | GI_REAL_SKY_PAGE_ATM | BOOL |  |  |  | 
Latitude | GI_REAL_SKY_LATITUDE | REAL | -90 | 90 |  | 
Longitude | GI_REAL_SKY_LONGITUDE | REAL | -180 | 180 |  | 
Time | GI_REAL_SKY_DATETIME | DATETIME |  |  |  | 
Time Zone Offset | GI_REAL_SKY_TIME_ZONE | LONG | -12 | 12 |  | 
Show Location HUD | GI_REAL_SKY_HUD | BOOL |  |  |  | 
Turbidity | GI_REAL_SKY_TURBIDITY | REAL | 2.0 | 16.0 |  | 
Ozone | GI_REAL_SKY_OZONE | REAL | 0.0 | 8.0 |  | 
Enabled | GI_REAL_SKY_SKY_ENABLED | BOOL |  |  |  | 
Horizon Line | GI_REAL_SKY_SKY_HORIZON | BOOL |  |  |  | 
Use Warm Colors | GI_REAL_SKY_SKY_WARM_COLORS | BOOL |  |  |  | 
Use Chroma Color Map | GI_REAL_SKY_SKY_CHROMA | BOOL |  |  |  | 
Intensity | GI_REAL_SKY_SKY_INTENSITY | REAL | 0.0 | 10000.0 |  | 
Night Intensity Ratio | GI_REAL_SKY_SKY_INTENSITY_NIGHT | REAL | 0.0 | 10000.0 |  | 
Saturation Correction | GI_REAL_SKY_SKY_SATURATION | REAL | 0.0 | 200.0 |  | 
Hue Correction | GI_REAL_SKY_SKY_HUE | REAL | 0.0 | 1.0 |  | 
Gamma Correction | GI_REAL_SKY_SKY_GAMMA | REAL | 0.1 | 10.0 |  | 
As Seen Intensity Ratio | GI_REAL_SKY_SKY_SEEN_RATIO | REAL | 0.0 | 10000.0 |  | 
Preview Color | GI_REAL_SKY_SUN_COLOR | COLOR |  |  |  | 
Enabled | GI_REAL_SKY_SUN_ENABLED | BOOL |  |  |  | 
Use Warm Colors | GI_REAL_SKY_SUN_WARM_COLORS | BOOL |  |  |  | 
Shadow Color | GI_REAL_SKY_SUN_SHADOW_COLOR | COLOR |  |  |  | 
Intensity | GI_REAL_SKY_SUN_INTENSITY | REAL | 0.0 | 10000.0 |  | 
Saturation Correction | GI_REAL_SKY_SUN_SATURATION | REAL | 0.0 | 200.0 |  | 
Hue Correction | GI_REAL_SKY_SUN_HUE | REAL | 0.0 | 1.0 |  | 
Gamma Correction | GI_REAL_SKY_SUN_GAMMA | REAL | 0.1 | 10.0 |  | 
Size Ratio | GI_REAL_SKY_SUN_SIZE_RATIO | REAL | 0.0 | 10000.0 |  | 
As Seen Intensity Ratio | GI_REAL_SKY_SUN_SEEN_RATIO | REAL | 0.0 | 10000.0 |  | 
Sampling Count | GI_REAL_SKY_SUN_SAMPLING_SAMPLES | LONG | 16 | 16384 |  | 
Sampling Quality | GI_REAL_SKY_SUN_SAMPLING_QUALITY | REAL | 0.0 | 100.0 |  | 
Enabled | GI_REAL_SKY_ATM_ENABLED | BOOL |  |  |  | 
Intensity | GI_REAL_SKY_ATM_INTENSITY | REAL | 0.0 | 1000.0 |  | 
Saturation Correction | GI_REAL_SKY_ATM_SATURATION | REAL | 0.0 | 200.0 |  | 
Hue Correction | GI_REAL_SKY_ATM_HUE | REAL | 0.0 | 1.0 |  | 
Gamma Correction | GI_REAL_SKY_ATM_GAMMA | REAL | 0.1 | 10.0 |  | 
Scene Scale Ratio | GI_REAL_SKY_ATM_SCALE_RATIO | REAL | 0.0 | 10000.0 |  | 
Assignment | MATERIAL_PAGE_ASSIGNMENT | BOOL |  |  |  | 
No label | ID_MATERIALASSIGNMENTS | MATASSIGN |  |  |  | 
