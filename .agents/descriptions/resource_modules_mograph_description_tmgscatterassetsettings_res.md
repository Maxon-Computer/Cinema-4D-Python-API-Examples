# Description: Scatter Object Asset Settings

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/mograph/description/tmgscatterassetsettings.res`
- **Symbol:** `Tmgscatterassetsettings`
- **Category:** Other

Use parameter symbols to access parameters and cycle option symbols for cycle values, never their numeric IDs. Treat Min and Max as constraints and Default as the declared initial value; blank cells mean the resource does not declare that metadata, not that the value is zero. Base Description Parameters lists inherited fields from each base; All Parameters lists the effective parameter set for this description.

## Base Description Parameters

No base descriptions.

## All Parameters

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Up Axis | MGSCATTER_ASSET_SETTINGS_UP_AXIS | LONG |  |  |  | MGSCATTER_ASSET_SETTINGS_UP_AXIS_XP; MGSCATTER_ASSET_SETTINGS_UP_AXIS_XM; MGSCATTER_ASSET_SETTINGS_UP_AXIS_YP; MGSCATTER_ASSET_SETTINGS_UP_AXIS_YM; MGSCATTER_ASSET_SETTINGS_UP_AXIS_ZP; MGSCATTER_ASSET_SETTINGS_UP_AXIS_ZM
Offset | MGSCATTER_ASSET_SETTINGS_OFFSET | REAL |  |  |  | 
Scale | MGSCATTER_ASSET_SETTINGS_SCALE | VECTOR | 0.01 | 100.0 | 1.0 1.0 1.0 | 
Frequency | MGSCATTER_ASSET_SETTINGS_FREQUENCY | REAL | 0.0 | 1000000.0 | 1.0 | 
