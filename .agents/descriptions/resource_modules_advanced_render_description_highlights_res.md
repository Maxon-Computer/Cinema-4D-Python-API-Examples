# Description: Highlights

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/advanced_render/description/highlights.res`
- **Symbol:** `HighLights`
- **Category:** Video Posts

Use parameter symbols to access parameters and cycle option symbols for cycle values, never their numeric IDs. Treat Min and Max as constraints and Default as the declared initial value; blank cells mean the resource does not declare that metadata, not that the value is zero. Base Description Parameters lists inherited fields from each base; All Parameters lists the effective parameter set for this description.

## Base Description Parameters

### Post Effect (`VPbase`)

No parameters.

## All Parameters

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Threshold | HLIGHT_FACEINTENS | REAL | 0.0 |  |  | 
Minimum Flare Intensity | HLIGHT_MININTENS | REAL | 0.0 |  |  | 
Maximum Flare Intensity | HLIGHT_MAXINTENS | REAL | 0.0 |  |  | 
Flare Size | HLIGHT_SIZE | REAL | 0.0 | 1000.0 |  | 
Preset | HLIGHT_PRESET | LONG |  |  |  | HLIGHT_PRESET_CUSTOM; HLIGHT_PRESET_1; HLIGHT_PRESET_2; HLIGHT_PRESET_3; HLIGHT_PRESET_4; HLIGHT_PRESET_5; HLIGHT_PRESET_6; HLIGHT_PRESET_7; HLIGHT_PRESET_8; HLIGHT_PRESET_9; HLIGHT_PRESET_10; HLIGHT_PRESET_11; HLIGHT_PRESET_12; HLIGHT_PRESET_13; HLIGHT_PRESET_14; HLIGHT_PRESET_15; HLIGHT_PRESET_16; HLIGHT_PRESET_17
Highlight | HLIGHT_LENSGLOW | LENSGLOW |  |  |  | 
Use Object ID | HLIGHT_USE_OBJID | BOOL |  |  |  | 
Object ID | HLIGHT_OBJID | LONG | 1 |  |  | 
