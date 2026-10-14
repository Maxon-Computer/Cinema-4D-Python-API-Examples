# Description: UV Projection

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/c4d_objects/description/tooluvprojection.res`
- **Symbol:** `ToolUvProjection`
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
Create New Tag | TOOL_UVPROJECTION_CREATENEWTAG | BOOL |  |  |  | 
Name | TOOL_UVPROJECTION_TAGNAME | STRING |  |  |  | 
Projection Type | TOOL_UVPROJECTION_TYPE | LONG |  |  |  | TOOL_UVPROJECTION_TYPE_CUBIC; TOOL_UVPROJECTION_TYPE_BOX; TOOL_UVPROJECTION_TYPE_SHRINK; TOOL_UVPROJECTION_TYPE_SPHERE; TOOL_UVPROJECTION_TYPE_CYLINDER; TOOL_UVPROJECTION_TYPE_VIEW; TOOL_UVPROJECTION_TYPE_AXIS
Preserve Aspect | TOOL_UVPROJECTION_PRESERVE_ASPECT | BOOL |  |  |  | 
Projection Axis | TOOL_UVPROJECTION_AXIS | LONG |  |  |  | TOOL_UVPROJECTION_AXIS_XPOS; TOOL_UVPROJECTION_AXIS_YPOS; TOOL_UVPROJECTION_AXIS_ZPOS; TOOL_UVPROJECTION_AXIS_XNEG; TOOL_UVPROJECTION_AXIS_YNEG; TOOL_UVPROJECTION_AXIS_ZNEG
Volume Type | TOOL_UVPROJECTION_VOLUMETYPE | LONG |  |  |  | TOOL_UVPROJECTION_VOLUMETYPE_PEROBJECT; TOOL_UVPROJECTION_VOLUMETYPE_PERHIERARCHY; TOOL_UVPROJECTION_VOLUMETYPE_USEALLOBJECTS
Include Children in Volume | TOOL_UVPROJECTION_INCLUDECHILDRENINVOLUME | BOOL |  |  |  | 
Fit Volume to Selection | TOOL_UVPROJECTION_FITVOLUMETOSELECTION | BOOL |  |  |  | 
Volume Orientation | TOOL_UVPROJECTION_VOLUMEORIENTATION | LONG |  |  |  | TOOL_UVPROJECTION_VOLUMEORIENTATION_WORLD; TOOL_UVPROJECTION_VOLUMEORIENTATION_OBJECT; TOOL_UVPROJECTION_VOLUMEORIENTATION_AVERAGENORMAL; TOOL_UVPROJECTION_VOLUMEORIENTATION_WEIGHTEDNORMAL
