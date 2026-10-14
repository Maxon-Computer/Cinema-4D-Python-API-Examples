# Description: Projection Man

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/c4d_manager/description/prefsproman.res`
- **Symbol:** `Prefsproman`
- **Category:** Other

Use parameter symbols to access parameters and cycle option symbols for cycle values, never their numeric IDs. Treat Min and Max as constraints and Default as the declared initial value; blank cells mean the resource does not declare that metadata, not that the value is zero. Base Description Parameters lists inherited fields from each base; All Parameters lists the effective parameter set for this description.

## Base Description Parameters

No base descriptions.

## All Parameters

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Default Texture Width | PREF_PM_WIDTH | LONG | 1 | 100000 |  | 
Default Texture Height | PREF_PM_HEIGHT | LONG | 1 | 100000 |  | 
Default Channel | PREF_PM_CHANNEL | LONG |  |  |  | PREF_PM_CHANNEL_LA; PREF_PM_CHANNEL_CA
Photoshop Path | PREF_PM_PSPATH | FILENAME |  |  |  | 
Work Path | PREF_PM_WPATH | FILENAME |  |  |  | 
Mode | PREF_PM_MODE | LONG |  |  |  | PREF_PM_MODE_PS; PREF_PM_MODE_BP3D
