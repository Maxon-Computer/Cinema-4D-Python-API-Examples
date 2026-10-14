# Description: Phong Break Selection

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/c4d_objects/description/toolphongselection.res`
- **Symbol:** `ToolPhongSelection`
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
Override Phong Tag | MDATA_PWS_OVERRIDE_PHONG | BOOL |  |  |  | 
Phong Angle | MDATA_PWS_ANGLE_THRESHOLD | REAL | 0 | 180 |  | 
Use Edge Breaks | MDATA_PWS_USE_PHONGBREAKS | BOOL |  |  |  | 
Select All | PWS_BTN_SELECT_ALL | BUTTON |  |  |  | 
Tag Name | PWS_TAG_LINK | STRING |  |  |  | 
Auto Set Selection | PWS_TAG_AUTO_SET_SEL | BOOL |  |  |  | 
Set Selection | PWS_TAG_SET_SEL | BUTTON |  |  |  | 
Add Selection | PWS_TAG_ADD_SEL | BUTTON |  |  |  | 
Subtract Selection | PWS_TAG_REM_SEL | BUTTON |  |  |  | 
