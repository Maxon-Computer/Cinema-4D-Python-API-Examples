# Description: Name

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/ca/description/toolcanaming.res`
- **Symbol:** `Toolcanaming`
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
Apply To | ID_CA_JOINT_NAMING_NODETYPE | LONG |  |  |  | ID_CA_JOINT_NAMING_NODETYPE_OBJECT; ID_CA_JOINT_NAMING_NODETYPE_TAG; ID_CA_JOINT_NAMING_NODETYPE_MATERIAL; ID_CA_JOINT_NAMING_NODETYPE_LAYER; ID_CA_JOINT_NAMING_NODETYPE_TAKE
Type | ID_CA_JOINT_NAMING_TYPE | LONG |  |  |  | 
Add | ID_CA_JOINT_NAMING_STORE | BUTTON |  |  |  | 
Remove | ID_CA_JOINT_NAMING_REMOVE | BUTTON |  |  |  | 
Load... | ID_CA_JOINT_NAMING_LOAD | BUTTON |  |  |  | 
Save... | ID_CA_JOINT_NAMING_SAVE | BUTTON |  |  |  | 
Prefix | ID_CA_JOINT_NAMING_PRE | STRING |  |  |  | 
Suffix | ID_CA_JOINT_NAMING_POST | STRING |  |  |  | 
Apply Name | ID_CA_JOINT_NAMING_APPLY | BUTTON |  |  |  | 
Prefix | ID_CA_JOINT_NAMING_REPLACE_PRE | STRING |  |  |  | 
Suffix | ID_CA_JOINT_NAMING_REPLACE_POST | STRING |  |  |  | 
Replace | ID_CA_JOINT_NAMING_REPLACE | STRING |  |  |  | 
With | ID_CA_JOINT_NAMING_REPLACE_WITH | STRING |  |  |  | 
Match Case | ID_CA_JOINT_NAMING_CASE | BOOL |  |  |  | 
Replace Name | ID_CA_JOINT_NAMING_REPLACE_APPLY | BUTTON |  |  |  | 
Name | ID_CA_JOINT_NAMING_SET_NAME | BUTTON |  |  |  | 
