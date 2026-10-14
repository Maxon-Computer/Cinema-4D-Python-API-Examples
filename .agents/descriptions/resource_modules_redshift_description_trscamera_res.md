# Description: Redshift Camera

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/redshift/description/trscamera.res`
- **Symbol:** `Trscamera`
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
Please install Redshift to set advanced options. | REDSHIFT_NOT_INSTALLED_NOTICE | STATICTEXT |  |  |  | 
Camera Type | REDSHIFT_CAMERA_TYPE | LONG |  |  |  | REDSHIFT_CAMERA_TYPE_STANDARD; REDSHIFT_CAMERA_TYPE_FISHEYE; REDSHIFT_CAMERA_TYPE_SPHERICAL; REDSHIFT_CAMERA_TYPE_CYLINDRICAL
FOV | REDSHIFT_CAMERA_FISHEYE_ANGLE | REAL | 1.0 | 180.0 |  | 
Horizontal Scale | REDSHIFT_CAMERA_FISHEYE_SCALE_X | REAL | 0.0 |  |  | 
Vertical Scale | REDSHIFT_CAMERA_FISHEYE_SCALE_Y | REAL | 0.0 |  |  | 
Orthographic Cylindrical | REDSHIFT_CAMERA_CYLINDRICAL_ORTHOGRAPHIC | BOOL |  |  |  | 
Horizontal FOV | REDSHIFT_CAMERA_CYLINDRICAL_FOVH | REAL | 0.0 | 360.0 |  | 
Vertical FOV | REDSHIFT_CAMERA_CYLINDRICAL_FOVV | REAL | 0.0 | 180.0 |  | 
Orthographic Height | REDSHIFT_CAMERA_CYLINDRICAL_ORTHOGRAPHIC_HEIGHT | REAL | 0.0 |  |  | 
