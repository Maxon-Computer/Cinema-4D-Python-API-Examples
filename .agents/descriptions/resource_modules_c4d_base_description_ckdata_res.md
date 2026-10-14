# Description: Data Key

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/c4d_base/description/ckdata.res`
- **Symbol:** `CKdata`
- **Category:** Keys

Use parameter symbols to access parameters and cycle option symbols for cycle values, never their numeric IDs. Treat Min and Max as constraints and Default as the declared initial value; blank cells mean the resource does not declare that metadata, not that the value is zero. Base Description Parameters lists inherited fields from each base; All Parameters lists the effective parameter set for this description.

## Base Description Parameters

### Key (`CKbase`)

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Key Time | ID_CKEY_TIME | BASETIME |  |  |  | 
Lock Time | ID_CKEY_LOCK_T | BOOL |  |  |  | 
Breakdown Color | ID_CKEY_BREAKDOWNCOLOR | BOOL |  |  |  | 
Interpolation | ID_DKEY_INTER | LONG |  |  |  | ID_DKEY_LINEAR; ID_DKEY_STEP
Mute | ID_CKEY_MUTE | BOOL |  |  |  | 
Breakdown | ID_CKEY_BREAKDOWN | BOOL |  |  |  | 

## All Parameters

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Key Time | ID_CKEY_TIME | BASETIME |  |  |  | 
Lock Time | ID_CKEY_LOCK_T | BOOL |  |  |  | 
Breakdown Color | ID_CKEY_BREAKDOWNCOLOR | BOOL |  |  |  | 
Interpolation | ID_DKEY_INTER | LONG |  |  |  | ID_DKEY_LINEAR; ID_DKEY_STEP
Mute | ID_CKEY_MUTE | BOOL |  |  |  | 
Breakdown | ID_CKEY_BREAKDOWN | BOOL |  |  |  | 
