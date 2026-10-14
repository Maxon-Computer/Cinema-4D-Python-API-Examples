# Description: Track Modifier

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/ca/description/tcaanimationmodifier.res`
- **Symbol:** `Tcaanimationmodifier`
- **Category:** Tags

Use parameter symbols to access parameters and cycle option symbols for cycle values, never their numeric IDs. Treat Min and Max as constraints and Default as the declared initial value; blank cells mean the resource does not declare that metadata, not that the value is zero. Base Description Parameters lists inherited fields from each base; All Parameters lists the effective parameter set for this description.

## Base Description Parameters

### Expression (`Texpression`)

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Priority | EXPRESSION_PRIORITY | PRIORITY |  |  |  | 
Enable | EXPRESSION_ENABLE | BOOL |  |  |  | 

### Base Tag (`Tbase`)

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Expose on Object | ID_EXPOSETAB | BOOL |  |  |  | 

### Basic Properties (`Obaselist`)

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Icon File / ID | ID_BASELIST_ICON_FILE | TEXTURE |  |  |  | 
Icon Color | ID_BASELIST_ICON_COLORIZE_MODE | BOOL |  |  |  | 
Color | ID_BASELIST_ICON_COLOR | COLOR |  |  | 1.0 0.9 0.4 | 
No label | ID_BASELIST_ICON_PRESET_BUTTONS | ICONCHOOSER |  |  |  | 
Name | ID_BASELIST_NAME | STRING |  |  |  | 
Layer | ID_LAYER_LINK | LINK |  |  |  | 
No label | ID_BASELIST_NODESPACE_ADD_REMOVE_BUTTONS | NODESPACE_ADD_REMOVE |  |  |  | 

## All Parameters

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Icon File / ID | ID_BASELIST_ICON_FILE | TEXTURE |  |  |  | 
Icon Color | ID_BASELIST_ICON_COLORIZE_MODE | BOOL |  |  |  | 
Color | ID_BASELIST_ICON_COLOR | COLOR |  |  | 1.0 0.9 0.4 | 
No label | ID_BASELIST_ICON_PRESET_BUTTONS | ICONCHOOSER |  |  |  | 
Name | ID_BASELIST_NAME | STRING |  |  |  | 
Layer | ID_LAYER_LINK | LINK |  |  |  | 
No label | ID_BASELIST_NODESPACE_ADD_REMOVE_BUTTONS | NODESPACE_ADD_REMOVE |  |  |  | 
Expose on Object | ID_EXPOSETAB | BOOL |  |  |  | 
Priority | EXPRESSION_PRIORITY | PRIORITY |  |  |  | 
Enable | EXPRESSION_ENABLE | BOOL |  |  |  | 
Mode | ID_CA_ANIMATION_MODIFIER_TAG_MODE | LONG |  |  | ID_CA_ANIMATION_MODIFIER_TAG_SPRING | ID_CA_ANIMATION_MODIFIER_TAG_SPRING; ID_CA_ANIMATION_MODIFIER_TAG_POSTERIZE; ID_CA_ANIMATION_MODIFIER_TAG_NOISE; ID_CA_ANIMATION_MODIFIER_TAG_SMOOTH
Offset | ID_CA_ANIMATION_MODIFIER_TAG_OFFSET | REAL |  |  |  | 
Time Factor | ID_CA_ANIMATION_MODIFIER_TAG_TIME_STRETCH | REAL | -100.0 |  |  | 
Strength | ID_CA_ANIMATION_MODIFIER_TAG_SPRING_STRENGTH | REAL |  |  |  | 
Stiffness | ID_CA_ANIMATION_MODIFIER_TAG_SPRING_STIFFNESS | REAL | 0.0 | 100.0 |  | 
Drag | ID_CA_ANIMATION_MODIFIER_TAG_SPRING_DRAG | REAL |  |  |  | 
Strength | ID_CA_ANIMATION_MODIFIER_TAG_POSTERIZE_STRENGTH | REAL | 0 | 100 |  | 
Frame Step | ID_CA_ANIMATION_MODIFIER_TAG_POSTERIZE_TIME | REAL | 1.0 |  |  | 
Strength | ID_CA_ANIMATION_MODIFIER_TAG_NOISE_STRENGTH | REAL |  |  | 0 | 
Position | ID_CA_ANIMATION_MODIFIER_TAG_NOISE_POSITION | REAL | 0 |  |  | 
Rotation | ID_CA_ANIMATION_MODIFIER_TAG_NOISE_ROTATION | REAL | 0 |  |  | 
Scale | ID_CA_ANIMATION_MODIFIER_TAG_NOISE_SCALE | REAL | 0 |  |  | 
Attributes | ID_CA_ANIMATION_MODIFIER_TAG_NOISE_ATTRIBUTES | REAL | 0 |  |  | 
User Data | ID_CA_ANIMATION_MODIFIER_TAG_NOISE_USERDATA | REAL | 0 |  |  | 
Speed | ID_CA_ANIMATION_MODIFIER_TAG_NOISE_SPEED | REAL | 0 |  |  | 
Seed | ID_CA_ANIMATION_MODIFIER_TAG_NOISE_SEED | REAL | 0.0 |  | 12345 | 
Strength | ID_CA_ANIMATION_MODIFIER_TAG_SMOOTH_STRENGTH | REAL |  |  | 5 | 
Range | ID_CA_ANIMATION_MODIFIER_TAG_SMOOTH_NEIGHBOR | LONG | 1 | 21 |  | 
Mask | ID_CA_ANIMATION_MODIFIER_TAG_SMOOTH_SPLINE | SPLINE |  |  |  | 
Hierarchy | ID_CA_ANIMATION_MODIFIER_TAG_HIERARCHY | BOOL |  |  |  | 
Tags | ID_CA_ANIMATION_MODIFIER_TAG_INCLUDE_TAGS | BOOL |  |  |  | 
Mode | ID_CA_ANIMATION_MODIFIER_TAG_EXCLUSION_MODE | LONG |  |  |  | ID_CA_ANIMATION_MODIFIER_TAG_EXCLUSION_MODE_INCLUDE; ID_CA_ANIMATION_MODIFIER_TAG_EXCLUSION_MODE_EXCLUDE
Tracks | ID_CA_ANIMATION_MODIFIER_TAG_EXCLUSION_MODE_TRACK | IN_EXCLUDE |  |  |  | 
Range | ID_CA_ANIMATION_MODIFIER_TAG_RANGE | BOOL |  |  |  | 
Start | ID_CA_ANIMATION_MODIFIER_TAG_RANGE_START | REAL |  |  | 0 | 
End | ID_CA_ANIMATION_MODIFIER_TAG_RANGE_END | REAL |  |  | 90 | 
Bake | ID_CA_ANIMATION_MODIFIER_TAG_CREATE_CACHE | BUTTON |  |  |  | 
Status :  | ID_CA_ANIMATION_MODIFIER_TAG_SMOOTH_CACHE_UPDATE | STATICTEXT |  |  |  | 
Clear | ID_CA_ANIMATION_MODIFIER_TAG_CLEAR_CACHE | BUTTON |  |  |  | 
