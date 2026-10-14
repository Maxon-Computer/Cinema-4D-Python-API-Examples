# Description: MoGraph Weight Tool

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/mograph/description/tool_mgweight.res`
- **Symbol:** `Tool_MGWeight`
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
Strength | MDATA_MGWEIGHTTOOL_STRENGTH | REAL | 0.0 |  |  | 
Mode | MDATA_MGWEIGHTTOOL_MODE | LONG |  |  |  | MDATA_MGWEIGHTTOOL_MODE_ADD; MDATA_MGWEIGHTTOOL_MODE_ERASE; MDATA_MGWEIGHTTOOL_MODE_ABS; MDATA_MGWEIGHTTOOL_MODE_SMOOTH
Apply All | MDATA_MGWEIGHTTOOL_APPLYALL | BUTTON |  |  |  | 
Apply Selected | MDATA_MGWEIGHTTOOL_APPLYSELECTED | BUTTON |  |  |  | 
Radius | MDATA_MGWEIGHTTOOL_RADIUS | REAL | 0.0 |  |  | 
Step | MDATA_MGWEIGHTTOOL_STEP | LONG | 1 | 100 |  | 
Pressure | MDATA_MGWEIGHTTOOL_PRESSURE | LONG |  |  |  | MDATA_MGWEIGHTTOOL_PRESSURE_NONE; MDATA_MGWEIGHTTOOL_PRESSURE_STRENGTH; MDATA_MGWEIGHTTOOL_PRESSURE_RADIUS
Show Weights | MDATA_MGWEIGHTTOOL_DISPLAY | BOOL |  |  |  | 
Visible Only | MDATA_MGWEIGHTTOOL_VISIBLE_ONLY | BOOL |  |  |  | 
