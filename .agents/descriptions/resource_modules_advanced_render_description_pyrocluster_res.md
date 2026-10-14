# Description: PyroCluster - VolumeTracer

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/advanced_render/description/pyrocluster.res`
- **Symbol:** `PyroCluster`
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
No label | MATERIAL_PAGE_PROPERTIES | BOOL |  |  |  | 
Render Objects | PSIMF_RENDOBJ | BOOL |  |  |  | 
Render Hidden Objects | PSIMF_RENDHOBJ | BOOL |  |  |  | 
Render Mode | PSIMF_RENDMODE | LONG |  |  |  | REND_MODE_HIGH; REND_MODE_MEDIUM; REND_MODE_LOW; REND_MODE_USER
World Step Size | PSIMF_STEP | REAL | 0.01 |  |  | 
Ray Trans. Limit | PSIMF_LIMIT | REAL | 0.0 | 100.0 |  | 
ShadowMap Step Size | PSIMF_MAPSTEP | REAL | 0.01 |  |  | 
ShadowMap Trans. Limit | PSIMF_MAPLIMIT | REAL | 0.0 | 100.0 |  | 
Raytraced Step Size | PSIMF_SHADSTEP | REAL | 0.01 |  |  | 
Raytraced Trans. Limit | PSIMF_SHADLIMIT | REAL | 0.0 | 100.0 |  | 
RayTrans. Correction | PSIMF_RTCORRECT | BOOL |  |  |  | 
Volume Light | PSIMF_VOLFILTER | BOOL |  |  |  | 
