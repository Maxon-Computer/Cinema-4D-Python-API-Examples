# Description: Redshift Proxy Export

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `Redshift/res/description/frsproxyexport.res`
- **Symbol:** `Frsproxyexport`
- **Category:** Files

Use parameter symbols to access parameters and cycle option symbols for cycle values, never their numeric IDs. Treat Min and Max as constraints and Default as the declared initial value; blank cells mean the resource does not declare that metadata, not that the value is zero. Base Description Parameters lists inherited fields from each base; All Parameters lists the effective parameter set for this description.

## Base Description Parameters

### Filter (`Fbase`)

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Presets | PRESET_OPTIONS_PRESETS | LONG |  |  | 0 | 
Save... | PRESET_OPTIONS_PRESETS_CUSTOM_SAVEBUTTON | BUTTON |  |  |  | 
Delete... | PRESET_OPTIONS_PRESETS_CUSTOM_DELETEBUTTON | BUTTON |  |  |  | 

## All Parameters

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Presets | PRESET_OPTIONS_PRESETS | LONG |  |  | 0 | 
Save... | PRESET_OPTIONS_PRESETS_CUSTOM_SAVEBUTTON | BUTTON |  |  |  | 
Delete... | PRESET_OPTIONS_PRESETS_CUSTOM_DELETEBUTTON | BUTTON |  |  |  | 
Options | REDSHIFT_PROXYEXPORT_GROUP_OPTIONS | SEPARATOR |  |  |  | 
Export | REDSHIFT_PROXYEXPORT_OBJECTS | LONG |  |  |  | REDSHIFT_PROXYEXPORT_OBJECTS_ALL; REDSHIFT_PROXYEXPORT_OBJECTS_SELECTION
Lights | REDSHIFT_PROXYEXPORT_EXPORT_LIGHTS | BOOL |  |  |  | 
Polygon Connectivity | REDSHIFT_PROXYEXPORT_EXPORT_POLYGON_CONNECTIVITY | BOOL |  |  |  | 
Compress Data | REDSHIFT_PROXYEXPORT_EXPORT_COMPRESS | BOOL |  |  |  | 
Scale | REDSHIFT_PROXYEXPORT_SCALE | UNITSCALE |  |  |  | 
Proxy Origin | REDSHIFT_PROXYEXPORT_ORIGIN | LONG |  |  |  | REDSHIFT_PROXYEXPORT_ORIGIN_WORLD; REDSHIFT_PROXYEXPORT_ORIGIN_OBJECTS
Add Proxy to Scene | REDSHIFT_PROXYEXPORT_AUTOPROXY_CREATE | BOOL |  |  |  | 
Name Prefix | REDSHIFT_PROXYEXPORT_AUTOPROXY_PREFIX | STRING |  |  |  | 
Remove Exported Objects | REDSHIFT_PROXYEXPORT_REMOVE_OBJECTS | BOOL |  |  |  | 
AOVs | REDSHIFT_PROXYEXPORT_GROUP_AOV | SEPARATOR |  |  |  | 
Include Default Beauty AOV | REDSHIFT_PROXYEXPORT_AOV_DEFAULT_BEAUTY | BOOL |  |  |  | 
Animation | REDSHIFT_PROXYEXPORT_GROUP_ANIMATION | SEPARATOR |  |  |  | 
Range | REDSHIFT_PROXYEXPORT_ANIMATION_RANGE | LONG |  |  |  | REDSHIFT_PROXYEXPORT_ANIMATION_RANGE_CURRENT_FRAME; REDSHIFT_PROXYEXPORT_ANIMATION_RANGE_ALL; REDSHIFT_PROXYEXPORT_ANIMATION_RANGE_PREVIEW; REDSHIFT_PROXYEXPORT_ANIMATION_RANGE_MANUAL
Start Frame | REDSHIFT_PROXYEXPORT_ANIMATION_FRAME_START | LONG | -18000 | 3240000 | 0 | 
End Frame | REDSHIFT_PROXYEXPORT_ANIMATION_FRAME_END | LONG | -18000 | 3240000 | 90 | 
Frame Step | REDSHIFT_PROXYEXPORT_ANIMATION_FRAME_STEP | LONG | 1 | 100 | 1 | 
