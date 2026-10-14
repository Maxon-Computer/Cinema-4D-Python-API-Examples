# Description: Recording Settings

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/mocca/description/toolrecordingsettings.res`
- **Symbol:** `ToolRecordingSettings`
- **Category:** Other

Use parameter symbols to access parameters and cycle option symbols for cycle values, never their numeric IDs. Treat Min and Max as constraints and Default as the declared initial value; blank cells mean the resource does not declare that metadata, not that the value is zero. Base Description Parameters lists inherited fields from each base; All Parameters lists the effective parameter set for this description.

## Base Description Parameters

No base descriptions.

## All Parameters

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Limit recording range | TOOL_ACTOR_RECORD_RANGE | LONG |  |  |  | TOOL_ACTOR_RECORD_RANGE_DOCUMENT; TOOL_ACTOR_RECORD_RANGE_PREVIEW; TOOL_ACTOR_RECORD_RANGE_RENDER; TOOL_ACTOR_RECORD_RANGE_USER
From frame | TOOL_ACTOR_RECORD_FROM | BASETIME | 0 |  |  | 
To frame | TOOL_ACTOR_RECORD_TO | BASETIME | 0 |  |  | 
Position | TOOL_ACTOR_RECORD_POSITION | BOOL |  |  |  | 
Scale | TOOL_ACTOR_RECORD_SCALE | BOOL |  |  |  | 
Rotation | TOOL_ACTOR_RECORD_ROTATION | BOOL |  |  |  | 
