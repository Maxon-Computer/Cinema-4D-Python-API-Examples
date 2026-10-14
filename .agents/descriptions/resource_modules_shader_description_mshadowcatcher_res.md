# Description: Shadow Catcher

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/shader/description/mshadowcatcher.res`
- **Symbol:** `Mshadowcatcher`
- **Category:** Materials

Use parameter symbols to access parameters and cycle option symbols for cycle values, never their numeric IDs. Treat Min and Max as constraints and Default as the declared initial value; blank cells mean the resource does not declare that metadata, not that the value is zero. Base Description Parameters lists inherited fields from each base; All Parameters lists the effective parameter set for this description.

## Base Description Parameters

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

### No label (`Millum`)

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Illumination | MATERIAL_PAGE_ILLUMINATION | BOOL |  |  |  | 
Polygon Light | MATERIAL_GLOBALILLUM_AREA | BOOL |  |  |  | 
Portal | MATERIAL_GLOBALILLUM_PORTAL | BOOL |  |  |  | 
GI Generate | MATERIAL_GLOBALILLUM_GENERATE | BOOL |  |  |  | 
GI Generate Strength | MATERIAL_GLOBALILLUM_GENERATE_STRENGTH | REAL | 0.0 | 10000.0 |  | 
GI Generate Saturation | MATERIAL_GLOBALILLUM_GENERATE_SATURATION | REAL | 0.0 | 1000.0 |  | 
GI Receive | MATERIAL_GLOBALILLUM_RECEIVE | BOOL |  |  |  | 
GI Receive Strength | MATERIAL_GLOBALILLUM_RECEIVE_STRENGTH | REAL | 0.0 | 10000.0 |  | 
GI Receive Saturation | MATERIAL_GLOBALILLUM_SATURATION | REAL | 0.0 | 1000.0 |  | 
Caustics Generate | MATERIAL_CAUSTICS_GENERATE | BOOL |  |  |  | 
Caustics Generate Strength | MATERIAL_CAUSTICS_GENERATE_STRENGTH | REAL | 0.0 | 10000.0 |  | 
Caustics Receive | MATERIAL_CAUSTICS_RECEIVE | BOOL |  |  |  | 
Caustics Receive Strength | MATERIAL_CAUSTICS_RECEIVE_STRENGTH | REAL | 0.0 | 10000.0 |  | 
Caustics Sample Radius | MATERIAL_CAUSTICS_SAMPLERADIUS | REAL | 0.0 |  |  | 
Caustics Samples | MATERIAL_CAUSTICS_SAMPLES | LONG | 1 | 10000 |  | 

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
No label | MATERIAL_PAGE_PROPERTIES | BOOL |  |  |  | 
Background Reflection      | SHADOWCATCHER_REFLECTION_COLOR | SHADERLINK |  |  |  | 
Catch Shadows | SHADOWCATCHER_SHADOWS | BOOL |  |  |  | 
Shadow Strength | SHADOWCATCHER_SHADOW_STRENGTH | REAL | 0 | 100 |  | 
Shadow Color | SHADOWCATCHER_SHADOW_COLOR | COLOR |  |  |  | 
Include Lighting               | SHADOWCATCHER_SHADOW_LIGHTING | BOOL |  |  |  | 
Catch Reflections | SHADOWCATCHER_REFLECTIONS | BOOL |  |  |  | 
Reflection Strength          | SHADOWCATCHER_REFLECTIONS_STRENGTH | REAL | 0 | 100 |  | 
Reflection Mask | SHADOWCATCHER_REFLECTIONS_MASK | SHADERLINK |  |  |  | 
Assignment | MATERIAL_PAGE_ASSIGNMENT | BOOL |  |  |  | 
No label | ID_MATERIALASSIGNMENTS | MATASSIGN |  |  |  | 
Illumination | MATERIAL_PAGE_ILLUMINATION | BOOL |  |  |  | 
Polygon Light | MATERIAL_GLOBALILLUM_AREA | BOOL |  |  |  | 
Portal | MATERIAL_GLOBALILLUM_PORTAL | BOOL |  |  |  | 
GI Generate | MATERIAL_GLOBALILLUM_GENERATE | BOOL |  |  |  | 
GI Generate Strength | MATERIAL_GLOBALILLUM_GENERATE_STRENGTH | REAL | 0.0 | 10000.0 |  | 
GI Generate Saturation | MATERIAL_GLOBALILLUM_GENERATE_SATURATION | REAL | 0.0 | 1000.0 |  | 
GI Receive | MATERIAL_GLOBALILLUM_RECEIVE | BOOL |  |  |  | 
GI Receive Strength | MATERIAL_GLOBALILLUM_RECEIVE_STRENGTH | REAL | 0.0 | 10000.0 |  | 
GI Receive Saturation | MATERIAL_GLOBALILLUM_SATURATION | REAL | 0.0 | 1000.0 |  | 
Caustics Generate | MATERIAL_CAUSTICS_GENERATE | BOOL |  |  |  | 
Caustics Generate Strength | MATERIAL_CAUSTICS_GENERATE_STRENGTH | REAL | 0.0 | 10000.0 |  | 
Caustics Receive | MATERIAL_CAUSTICS_RECEIVE | BOOL |  |  |  | 
Caustics Receive Strength | MATERIAL_CAUSTICS_RECEIVE_STRENGTH | REAL | 0.0 | 10000.0 |  | 
Caustics Sample Radius | MATERIAL_CAUSTICS_SAMPLERADIUS | REAL | 0.0 |  |  | 
Caustics Samples | MATERIAL_CAUSTICS_SAMPLES | LONG | 1 | 10000 |  | 
