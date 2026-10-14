# Description: Character BodyPart Tool

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/mocca/description/toolbodypart.res`
- **Symbol:** `Toolbodypart`
- **Category:** Other

Use parameter symbols to access parameters and cycle option symbols for cycle values, never their numeric IDs. Treat Min and Max as constraints and Default as the declared initial value; blank cells mean the resource does not declare that metadata, not that the value is zero. Base Description Parameters lists inherited fields from each base; All Parameters lists the effective parameter set for this description.

## Base Description Parameters

No base descriptions.

## All Parameters

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Joints | TBP_PART_JOINTS_NAME | STATICTEXT |  |  |  | 
No label | TBP_PART_JOINTS | IN_EXCLUDE |  |  |  | 
P | TBP_PART_JOINTS_POSITIONTRANSFER | BOOL |  |  |  | 
R | TBP_PART_JOINTS_ROTATIONTRANSFER | BOOL |  |  |  | 
S | TBP_PART_JOINTS_SCALETRANSFER | BOOL |  |  |  | 
UD | TBP_PART_JOINTS_USERDATATRANSFER | BOOL |  |  |  | 
UD Mode | TBP_PART_JOINTS_USERDATATRANSFER_MODE | LONG |  |  |  | TBP_PART_JOINTS_USERDATATRANSFER_MODE_NAME; TBP_PART_JOINTS_USERDATATRANSFER_MODE_UUID; TBP_PART_JOINTS_USERDATATRANSFER_MODE_BOTH
Controller | TBP_PART_CONTROLS_NAME | STATICTEXT |  |  |  | 
No label | TBP_PART_CONTROLS | IN_EXCLUDE |  |  |  | 
Strings to Include | TBP_PART_INCLUDESTRING_NAME | STATICTEXT |  |  |  | 
No label | TBP_PART_INCLUDESTRING | STRING |  |  |  | 
Strings to Exclude | TBP_PART_EXCLUDESTRING_NAME | STATICTEXT |  |  |  | 
No label | TBP_PART_EXCLUDESTRING | STRING |  |  |  | 
Identifier | TBP_PART_IDENTIFIER_NAME | STATICTEXT |  |  |  | 
No label | TBP_PART_IDENTIFIER | STRING |  |  |  | 
