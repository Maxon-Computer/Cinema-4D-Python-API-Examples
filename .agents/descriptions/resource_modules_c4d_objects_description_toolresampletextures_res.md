# Description: Resample Textures

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/c4d_objects/description/toolresampletextures.res`
- **Symbol:** `ToolResampleTextures`
- **Category:** Other

Use parameter symbols to access parameters and cycle option symbols for cycle values, never their numeric IDs. Treat Min and Max as constraints and Default as the declared initial value; blank cells mean the resource does not declare that metadata, not that the value is zero. Base Description Parameters lists inherited fields from each base; All Parameters lists the effective parameter set for this description.

## Base Description Parameters

### Base Tool (`ToolBase`)

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Realtime Update | MDATA_INTERACTIVE | BOOL |  |  |  | 
    Apply     | MDATA_APPLY | BUTTON |  |  |  | 
New Transform | MDATA_NEWTRANSFORM | BUTTON |  |  |  | 
No label | ID_SNAPSETTINGS | SUBCONTAINER |  |  |  | 

## All Parameters

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Realtime Update | MDATA_INTERACTIVE | BOOL |  |  |  | 
    Apply     | MDATA_APPLY | BUTTON |  |  |  | 
New Transform | MDATA_NEWTRANSFORM | BUTTON |  |  |  | 
No label | ID_SNAPSETTINGS | SUBCONTAINER |  |  |  | 
Source UVW Tag | TOOLRESAMPLETEXTURES_SOURCEUVWTAG | LINK |  |  |  | 
Target Object | TOOLRESAMPLETEXTURES_TARGETOBJECT | LINK |  |  |  | 
Target UVW Tag | TOOLRESAMPLETEXTURES_TARGETUVWTAG | LINK |  |  |  | 
Texture Output Directory | TOOLRESAMPLETEXTURES_OUTPUTFOLDER | FILENAME |  |  |  | 
Reproject UV | TOOLRESAMPLETEXTURES_REPROJECTUV | BOOL |  |  |  | 
Reproject Mode | TOOLRESAMPLETEXTURES_REPROJECTUV_MODE | LONG |  |  |  | TOOLRESAMPLETEXTURES_REPROJECTUV_MODE_CUBIC; TOOLRESAMPLETEXTURES_REPROJECTUV_MODE_ANGLE
Sampling Space | TOOLRESAMPLETEXTURES_SAMPLESPACE | LONG |  |  |  | TOOLRESAMPLETEXTURES_SAMPLESPACE_LOCAL; TOOLRESAMPLETEXTURES_SAMPLESPACE_WORLD
