# Description: Physical Sky

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/sky/description/oskyshader.res`
- **Symbol:** `Oskyshader`
- **Category:** Objects

Use parameter symbols to access parameters and cycle option symbols for cycle values, never their numeric IDs. Treat Min and Max as constraints and Default as the declared initial value; blank cells mean the resource does not declare that metadata, not that the value is zero. Base Description Parameters lists inherited fields from each base; All Parameters lists the effective parameter set for this description.

## Base Description Parameters

### Base Object (`Obase`)

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Icon Color | ID_BASELIST_ICON_COLORIZE_MODE | LONG |  |  |  | ID_BASELIST_ICON_COLORIZE_MODE_NONE; ID_BASELIST_ICON_COLORIZE_MODE_DISPLAYCOLOR; ID_BASELIST_ICON_COLORIZE_MODE_CUSTOM
Viewport Visibility | ID_BASEOBJECT_VISIBILITY_EDITOR | LONG |  |  |  | OBJECT_UNDEF; OBJECT_ON; OBJECT_OFF
Renderer Visibility | ID_BASEOBJECT_VISIBILITY_RENDER | LONG |  |  |  | OBJECT_UNDEF; OBJECT_ON; OBJECT_OFF
Enabled | ID_BASEOBJECT_GENERATOR_FLAG | BOOL |  |  |  | 
Display Color | ID_BASEOBJECT_USECOLOR | LONG |  |  |  | ID_BASEOBJECT_USECOLOR_OFF; ID_BASEOBJECT_USECOLOR_LAYER; ID_BASEOBJECT_USECOLOR_AUTOMATIC; ID_BASEOBJECT_USECOLOR_ALWAYS
Color | ID_BASEOBJECT_COLOR | COLOR |  |  |  | 
X-Ray | ID_BASEOBJECT_XRAY | BOOL |  |  |  | 
Position | ID_BASEOBJECT_REL_POSITION | VECTOR |  |  |  | 
Rotation | ID_BASEOBJECT_REL_ROTATION | VECTOR |  |  |  | 
Scale | ID_BASEOBJECT_REL_SCALE | VECTOR |  |  |  | 
Rotation Order | ID_BASEOBJECT_ROTATION_ORDER | LONG |  |  |  | ID_BASEOBJECT_ROTATION_ORDER_HPB; ID_BASEOBJECT_ROTATION_ORDER_XYZ; ID_BASEOBJECT_ROTATION_ORDER_XZY; ID_BASEOBJECT_ROTATION_ORDER_YXZ; ID_BASEOBJECT_ROTATION_ORDER_YZX; ID_BASEOBJECT_ROTATION_ORDER_ZXY; ID_BASEOBJECT_ROTATION_ORDER_ZYX
Quaternion Rotation | ID_BASEOBJECT_QUATERNION_ROTATION_INTERPOLATION | BOOL |  |  |  | 
Freeze All | ID_BASEOBJECT_FREEZE | BUTTON |  |  |  | 
Unfreeze All | ID_BASEOBJECT_FROZEN_RESET | BUTTON |  |  |  | 
Frozen Position | ID_BASEOBJECT_FROZEN_POSITION | VECTOR |  |  |  | 
Freeze P | ID_BASEOBJECT_FREEZE_P | BUTTON |  |  |  | 
Frozen Rotation | ID_BASEOBJECT_FROZEN_ROTATION | VECTOR |  |  |  | 
Freeze R | ID_BASEOBJECT_FREEZE_R | BUTTON |  |  |  | 
Frozen Scale | ID_BASEOBJECT_FROZEN_SCALE | VECTOR |  |  |  | 
Freeze S | ID_BASEOBJECT_FREEZE_S | BUTTON |  |  |  | 
Deform Position | ID_BASEOBJECT_DEFORM_POSITION | VECTOR |  |  |  | 
Deform Rotation | ID_BASEOBJECT_DEFORM_ROTATION | VECTOR |  |  |  | 
Deform Scale | ID_BASEOBJECT_DEFORM_SCALE | VECTOR |  |  |  | 
Global Position | ID_BASEOBJECT_GLOBAL_POSITION | VECTOR |  |  |  | 
Global Rotation | ID_BASEOBJECT_GLOBAL_ROTATION | VECTOR |  |  |  | 
Transformed Position | ID_BASEOBJECT_ABS_POSITION | VECTOR |  |  |  | 
Transformed Scale | ID_BASEOBJECT_ABS_SCALE | VECTOR |  |  |  | 
Transformed Rotation | ID_BASEOBJECT_ABS_ROTATION | VECTOR |  |  |  | 

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
Color | ID_BASELIST_ICON_COLOR | COLOR |  |  | 1.0 0.9 0.4 | 
No label | ID_BASELIST_ICON_PRESET_BUTTONS | ICONCHOOSER |  |  |  | 
Name | ID_BASELIST_NAME | STRING |  |  |  | 
Layer | ID_LAYER_LINK | LINK |  |  |  | 
No label | ID_BASELIST_NODESPACE_ADD_REMOVE_BUTTONS | NODESPACE_ADD_REMOVE |  |  |  | 
Icon Color | ID_BASELIST_ICON_COLORIZE_MODE | LONG |  |  |  | ID_BASELIST_ICON_COLORIZE_MODE_NONE; ID_BASELIST_ICON_COLORIZE_MODE_DISPLAYCOLOR; ID_BASELIST_ICON_COLORIZE_MODE_CUSTOM
Viewport Visibility | ID_BASEOBJECT_VISIBILITY_EDITOR | LONG |  |  |  | OBJECT_UNDEF; OBJECT_ON; OBJECT_OFF
Renderer Visibility | ID_BASEOBJECT_VISIBILITY_RENDER | LONG |  |  |  | OBJECT_UNDEF; OBJECT_ON; OBJECT_OFF
Enabled | ID_BASEOBJECT_GENERATOR_FLAG | BOOL |  |  |  | 
Display Color | ID_BASEOBJECT_USECOLOR | LONG |  |  |  | ID_BASEOBJECT_USECOLOR_OFF; ID_BASEOBJECT_USECOLOR_LAYER; ID_BASEOBJECT_USECOLOR_AUTOMATIC; ID_BASEOBJECT_USECOLOR_ALWAYS
Color | ID_BASEOBJECT_COLOR | COLOR |  |  |  | 
X-Ray | ID_BASEOBJECT_XRAY | BOOL |  |  |  | 
Position | ID_BASEOBJECT_REL_POSITION | VECTOR |  |  |  | 
Rotation | ID_BASEOBJECT_REL_ROTATION | VECTOR |  |  |  | 
Scale | ID_BASEOBJECT_REL_SCALE | VECTOR |  |  |  | 
Rotation Order | ID_BASEOBJECT_ROTATION_ORDER | LONG |  |  |  | ID_BASEOBJECT_ROTATION_ORDER_HPB; ID_BASEOBJECT_ROTATION_ORDER_XYZ; ID_BASEOBJECT_ROTATION_ORDER_XZY; ID_BASEOBJECT_ROTATION_ORDER_YXZ; ID_BASEOBJECT_ROTATION_ORDER_YZX; ID_BASEOBJECT_ROTATION_ORDER_ZXY; ID_BASEOBJECT_ROTATION_ORDER_ZYX
Quaternion Rotation | ID_BASEOBJECT_QUATERNION_ROTATION_INTERPOLATION | BOOL |  |  |  | 
Freeze All | ID_BASEOBJECT_FREEZE | BUTTON |  |  |  | 
Unfreeze All | ID_BASEOBJECT_FROZEN_RESET | BUTTON |  |  |  | 
Frozen Position | ID_BASEOBJECT_FROZEN_POSITION | VECTOR |  |  |  | 
Freeze P | ID_BASEOBJECT_FREEZE_P | BUTTON |  |  |  | 
Frozen Rotation | ID_BASEOBJECT_FROZEN_ROTATION | VECTOR |  |  |  | 
Freeze R | ID_BASEOBJECT_FREEZE_R | BUTTON |  |  |  | 
Frozen Scale | ID_BASEOBJECT_FROZEN_SCALE | VECTOR |  |  |  | 
Freeze S | ID_BASEOBJECT_FREEZE_S | BUTTON |  |  |  | 
Deform Position | ID_BASEOBJECT_DEFORM_POSITION | VECTOR |  |  |  | 
Deform Rotation | ID_BASEOBJECT_DEFORM_ROTATION | VECTOR |  |  |  | 
Deform Scale | ID_BASEOBJECT_DEFORM_SCALE | VECTOR |  |  |  | 
Global Position | ID_BASEOBJECT_GLOBAL_POSITION | VECTOR |  |  |  | 
Global Rotation | ID_BASEOBJECT_GLOBAL_ROTATION | VECTOR |  |  |  | 
Transformed Position | ID_BASEOBJECT_ABS_POSITION | VECTOR |  |  |  | 
Transformed Scale | ID_BASEOBJECT_ABS_SCALE | VECTOR |  |  |  | 
Transformed Rotation | ID_BASEOBJECT_ABS_ROTATION | VECTOR |  |  |  | 
Load Sky Preset... | SKY_PRESET | BUTTON |  |  |  | 
Load Weather Preset... | SKY_WEATHERPRESET | BUTTON |  |  |  | 
Time and Location | SKY_TIMEANDLOCATION | BOOL |  |  |  | 
Sky | SKY_PHYSICALSKYPAGE | BOOL |  |  |  | 
Sun | SKY_PHYSICAL_SUN_ENABLE | BOOL |  |  |  | 
Atmosphere | SKY_PHYSICAL_ATM_ENABLE | BOOL |  |  |  | 
Clouds | SKY_CLOUD_ENABLE | BOOL |  |  |  | 
Details | SKY_DETAILS | BOOL |  |  |  | 
No label | SKY_LEFT_SEPARATOR | SEPARATOR |  |  |  | 
Volumetric Clouds | SKY_VOL_CLOUDS_RENDER | BOOL |  |  |  | 
Fog | SKY_FOG_ENABLE | BOOL |  |  |  | 
Rainbow | SKY_RAINBOW_RENDER | BOOL |  |  |  | 
Sunbeams | SKY_BEAMS_ENABLE | BOOL |  |  |  | 
Sky Objects | SKY_OBJECTS | BOOL |  |  |  | 
Time | SKY_DATE_TIME | DATETIME |  |  |  | 
Current Time | SKY_TIME_NOW | BOOL |  |  |  | 
Today | SKY_DATE_TODAY | BOOL |  |  |  | 
Animate Date | SKY_DATE_ANIMATE | BOOL |  |  |  | 
Animate Time | SKY_TIME_ANIMATE | BOOL |  |  |  | 
x | SKY_POS_CITY | STRING |  |  |  | 
City | SKY_POS_CITY_COMBO | LONG |  |  |  | 
Latitude | SKY_POS_LATITUDE | REAL | -90 | 90 |  | 
Longitude | SKY_POS_LONGITUDE | REAL | -180 | 180 |  | 
Time Zone | SKY_POS_TIMEZONE | LONG |  |  |  | SKY_POS_TZ_OS; SKY_POS_TZ_CUSTOM
Daylight Saving | SKY_POS_DST_SETTINGS | LONG |  |  |  | SKY_POS_DST_OFF; SKY_POS_DST_LAST_MARCH_LAST_OCT; SKY_POS_DST_SECOND_MARCH_FIRST_NOV; SKY_POS_DST_FIRST_APR_LAST_OCT; SKY_POS_DST_FIRST_OCT_LAST_MARCH; SKY_POS_DST_LAST_OCT_LAST_MARCH
Time Zone Diff. | SKY_POS_TIME_ZONE | REAL |  |  |  | 
DS Time Zone | SKY_POS_DST_TIME_ZONE | REAL |  |  |  | 
Physical Sky | SKY_PHYSICAL_SKY_ENABLE | BOOL |  |  |  | 
Horizon Line | SKY_REAL_SKY_SKY_HORIZON | BOOL |  |  |  | 
Color Warmth | SKY_REAL_SKY_SKY_COLOR_WARMNESS | REAL | 0.0 | 100.0 |  | 
Intensity | SKY_REAL_SKY_SKY_INTENSITY | REAL | 0.0 | 10000.0 |  | 
Night Intensity Ratio | SKY_REAL_SKY_SKY_INTENSITY_NIGHT | REAL | 0.0 | 10000.0 |  | 
Saturation Correction | SKY_REAL_SKY_SKY_SATURATION | REAL | 0.0 | 200.0 |  | 
Hue Correction | SKY_REAL_SKY_SKY_HUE | REAL | 0.0 | 100.0 |  | 
Gamma Correction | SKY_REAL_SKY_SKY_GAMMA | REAL | 0.1 | 10.0 |  | 
As Seen Intensity | SKY_REAL_SKY_SKY_SEEN_INTENSITY | REAL | 0.0 | 10000.0 |  | 
Dithering | SKY_REAL_SKY_SKY_DITHER | REAL | 0.0 | 100.0 |  | 
Turbidity | SKY_REAL_SKY_TURBIDITY | REAL | 2.0 | 32.0 |  | 
Ozone (cm) | SKY_REAL_SKY_OZONE | REAL | 0.0 | 50.0 |  | 
Custom Horizon | SKY_GENERAL_USER_HORIZON | BOOL |  |  |  | 
Max. Altitude | SKY_GENERAL_USER_HORIZON_MAX_ALT | REAL | 0 | 90 |  | 
Color | SKY_GENERAL_USER_COLOR | GRADIENT |  |  |  | 
Atmosphere Strength | SKY_GENERAL_STRENGTH | REAL | 0 | 100 |  | 
Effects Turbidity | SKY_GENERAL_MOISTURE | REAL | 0 | 100 |  | 
Horizon Start | SKY_GENERAL_HORIZON_START | REAL | -89 | 89 |  | 
Earth Radius (km) | SKY_GENERAL_EARTH_RADIUS | REAL | 10 |  |  | 
Preview Color | SKY_REAL_SKY_SUN_COLOR | COLOR |  |  |  | 
Intensity | SKY_REAL_SKY_SUN_INTENSITY | REAL | 0.0 | 10000.0 |  | 
Saturation Correction | SKY_REAL_SKY_SUN_SATURATION | REAL | 0.0 | 200.0 |  | 
Hue Correction | SKY_REAL_SKY_SUN_HUE | REAL | 0.0 | 100.0 |  | 
Gamma Correction | SKY_REAL_SKY_SUN_GAMMA | REAL | 0.1 | 10.0 |  | 
Size Ratio | SKY_REAL_SKY_SUN_SIZE_RATIO | REAL | 0.0 | 10000.0 |  | 
As Seen Intensity | SKY_REAL_SKY_SUN_SEEN_INTENSITY | REAL | 0.0 | 10000.0 |  | 
Custom Color | SKY_GENERAL_CHANGE_SUN_COL | BOOL |  |  |  | 
Color | SKY_GENERAL_SUN_COLOR | COLOR |  |  |  | 
Lensflares | SKY_GENERAL_LENSFLARES | BOOL |  |  |  | 
Glow Intensity | SKY_GENERAL_MAX_FLARE_GLOW | REAL | 0 | 100 |  | 
Flare Intensity | SKY_GENERAL_MAX_FLARE_REFL | REAL | 0 | 100 |  | 
Distance Scale | SKY_GENERAL_SUN_DIST_SCALE | REAL | 0 |  |  | 
Custom Sun Object | SKY_OBJECT_SUN_OBJECT | LINK |  |  |  | 
Shadow Type | SKY_REAL_SKY_SUN_SHADOW_TYPE | LONG |  |  |  | SKY_SUN_SHADOW_TYPE_NONE; SKY_SUN_SHADOW_TYPE_HARD; SKY_SUN_SHADOW_TYPE_AREA
Density | SKY_REAL_SKY_SUN_SHADOW_DENSITY | REAL | 0.0 | 10000.0 |  | 
Shadow Color | SKY_REAL_SKY_SUN_SHADOW_COLOR | COLOR |  |  |  | 
Transparency | SKY_REAL_SKY_SUN_SHADOW_TRANSPARENCY | BOOL |  |  |  | 
Shadow Accuracy | SKY_REAL_SKY_SUN_SAMPLING_QUALITY | REAL | 0.0 | 100.0 |  | 
Minimum Samples | SKY_REAL_SKY_SUN_SAMPLING_SAMPLES_MIN | LONG | 1 | 16384 |  | 
Maximum Samples | SKY_REAL_SKY_SUN_SAMPLING_SAMPLES_MAX | LONG | 4 | 16384 |  | 
Intensity | SKY_REAL_SKY_ATM_INTENSITY | REAL | 0.0 | 1000.0 |  | 
Horizon Fade | SKY_REAL_SKY_ATM_HORIZON | REAL | 0.0 | 100.0 |  | 
Saturation Correction | SKY_REAL_SKY_ATM_SATURATION | REAL | 0.0 | 200.0 |  | 
Hue Correction | SKY_REAL_SKY_ATM_HUE | REAL | 0.0 | 100.0 |  | 
Gamma Correction | SKY_REAL_SKY_ATM_GAMMA | REAL | 0.1 | 10.0 |  | 
World Scale Ratio | SKY_REAL_SKY_ATM_SCALE_RATIO | REAL | 0.0 | 10000.0 |  | 
Dithering | SKY_REAL_SKY_ATM_DITHER | REAL | 0.0 | 100.0 |  | 
Rolloff | SKY_CLOUD_ROLLOFF | GRADIENT |  |  |  | 
Cast Shadows | SKY_CLOUDS_SHADOW | BOOL |  |  |  | 
Layer 1 | SKY_CLOUD_1_ACTIVE | BOOL |  |  |  | 
Layer 2 | SKY_CLOUD_2_ACTIVE | BOOL |  |  |  | 
Layer 3 | SKY_CLOUD_3_ACTIVE | BOOL |  |  |  | 
Layer 4 | SKY_CLOUD_4_ACTIVE | BOOL |  |  |  | 
Layer 5 | SKY_CLOUD_5_ACTIVE | BOOL |  |  |  | 
Layer 6 | SKY_CLOUD_6_ACTIVE | BOOL |  |  |  | 
Noise 1 | SKY_CLOUD_1_NOISE | LONG |  |  |  | 
Color 1 | SKY_CLOUD_1_COLOR | COLOR |  |  |  | 
Height 1 | SKY_CLOUD_1_HEIGHT | REAL | 0 | 50000 |  | 
Density 1 | SKY_CLOUD_1_DENSITY | REAL | 0 | 5000 |  | 
Coverage 1 | SKY_CLOUD_1_COVERAGE | REAL | 0 | 100 |  | 
Thickness 1 | SKY_CLOUD_1_THICKNESS | REAL | 0 | 5000 |  | 
Transparency 1 | SKY_CLOUD_1_TRANSPARENCY | REAL | 0 | 100 |  | 
No label | SKY_CLOUD_1_PREVIEW | MATPREVIEW |  |  |  | 
Save as Preset... | SKY_CLOUD_1_SAVE_PRESET | BUTTON |  |  |  | 
Load Preset... | SKY_CLOUD_1_LOAD_PRESET | BUTTON |  |  |  | 
Anim. Speed 1 | SKY_CLOUD_1_SPEED | REAL |  |  |  | 
Noise Offset 1 | SKY_CLOUD_1_OFFSET | REAL |  |  |  | 
Scale N-S 1 | SKY_CLOUD_1_SCALE_NS | REAL | 1 |  |  | 
Scale W-E 1 | SKY_CLOUD_1_SCALE_WE | REAL | 1 |  |  | 
Pos. N-S 1 | SKY_CLOUD_1_MOVE_NS | REAL |  |  |  | 
Pos. W-E 1 | SKY_CLOUD_1_MOVE_WE | REAL |  |  |  | 
Noise 2 | SKY_CLOUD_2_NOISE | LONG |  |  |  | 
Color 2 | SKY_CLOUD_2_COLOR | COLOR |  |  |  | 
Height 2 | SKY_CLOUD_2_HEIGHT | REAL | 0 | 50000 |  | 
Density 2 | SKY_CLOUD_2_DENSITY | REAL | 0 | 5000 |  | 
Coverage 2 | SKY_CLOUD_2_COVERAGE | REAL | 0 | 100 |  | 
Thickness 2 | SKY_CLOUD_2_THICKNESS | REAL | 0 | 5000 |  | 
Transparency 2 | SKY_CLOUD_2_TRANSPARENCY | REAL | 0 | 100 |  | 
No label | SKY_CLOUD_2_PREVIEW | MATPREVIEW |  |  |  | 
Save as Preset... | SKY_CLOUD_2_SAVE_PRESET | BUTTON |  |  |  | 
Load Preset... | SKY_CLOUD_2_LOAD_PRESET | BUTTON |  |  |  | 
Anim. Speed 2 | SKY_CLOUD_2_SPEED | REAL |  |  |  | 
Noise Offset 2 | SKY_CLOUD_2_OFFSET | REAL |  |  |  | 
Scale N-S 2 | SKY_CLOUD_2_SCALE_NS | REAL | 1 |  |  | 
Scale W-E 2 | SKY_CLOUD_2_SCALE_WE | REAL | 1 |  |  | 
Pos. N-S 2 | SKY_CLOUD_2_MOVE_NS | REAL |  |  |  | 
Pos. W-E 2 | SKY_CLOUD_2_MOVE_WE | REAL |  |  |  | 
Noise 3 | SKY_CLOUD_3_NOISE | LONG |  |  |  | 
Color 3 | SKY_CLOUD_3_COLOR | COLOR |  |  |  | 
Height 3 | SKY_CLOUD_3_HEIGHT | REAL | 0 | 50000 |  | 
Density 3 | SKY_CLOUD_3_DENSITY | REAL | 0 | 5000 |  | 
Coverage 3 | SKY_CLOUD_3_COVERAGE | REAL | 0 | 100 |  | 
Thickness 3 | SKY_CLOUD_3_THICKNESS | REAL | 0 | 5000 |  | 
Transparency 3 | SKY_CLOUD_3_TRANSPARENCY | REAL | 0 | 100 |  | 
No label | SKY_CLOUD_3_PREVIEW | MATPREVIEW |  |  |  | 
Save as Preset... | SKY_CLOUD_3_SAVE_PRESET | BUTTON |  |  |  | 
Load Preset... | SKY_CLOUD_3_LOAD_PRESET | BUTTON |  |  |  | 
Anim. Speed 3 | SKY_CLOUD_3_SPEED | REAL |  |  |  | 
Noise Offset 3 | SKY_CLOUD_3_OFFSET | REAL |  |  |  | 
Scale N-S 3 | SKY_CLOUD_3_SCALE_NS | REAL | 1 |  |  | 
Scale W-E 3 | SKY_CLOUD_3_SCALE_WE | REAL | 1 |  |  | 
Pos. N-S 3 | SKY_CLOUD_3_MOVE_NS | REAL |  |  |  | 
Pos. W-E 3 | SKY_CLOUD_3_MOVE_WE | REAL |  |  |  | 
Noise 4 | SKY_CLOUD_4_NOISE | LONG |  |  |  | 
Color 4 | SKY_CLOUD_4_COLOR | COLOR |  |  |  | 
Height 4 | SKY_CLOUD_4_HEIGHT | REAL | 0 | 50000 |  | 
Density 4 | SKY_CLOUD_4_DENSITY | REAL | 0 | 5000 |  | 
Coverage 4 | SKY_CLOUD_4_COVERAGE | REAL | 0 | 100 |  | 
Thickness 4 | SKY_CLOUD_4_THICKNESS | REAL | 0 | 5000 |  | 
Transparency 4 | SKY_CLOUD_4_TRANSPARENCY | REAL | 0 | 100 |  | 
No label | SKY_CLOUD_4_PREVIEW | MATPREVIEW |  |  |  | 
Save as Preset... | SKY_CLOUD_4_SAVE_PRESET | BUTTON |  |  |  | 
Load Preset... | SKY_CLOUD_4_LOAD_PRESET | BUTTON |  |  |  | 
Anim. Speed 4 | SKY_CLOUD_4_SPEED | REAL |  |  |  | 
Noise Offset 4 | SKY_CLOUD_4_OFFSET | REAL |  |  |  | 
Scale N-S 4 | SKY_CLOUD_4_SCALE_NS | REAL | 1 |  |  | 
Scale W-E 4 | SKY_CLOUD_4_SCALE_WE | REAL | 1 |  |  | 
Pos. N-S 4 | SKY_CLOUD_4_MOVE_NS | REAL |  |  |  | 
Pos. W-E 4 | SKY_CLOUD_4_MOVE_WE | REAL |  |  |  | 
Noise 5 | SKY_CLOUD_5_NOISE | LONG |  |  |  | 
Color 5 | SKY_CLOUD_5_COLOR | COLOR |  |  |  | 
Height 5 | SKY_CLOUD_5_HEIGHT | REAL | 0 | 50000 |  | 
Density 5 | SKY_CLOUD_5_DENSITY | REAL | 0 | 5000 |  | 
Coverage 5 | SKY_CLOUD_5_COVERAGE | REAL | 0 | 100 |  | 
Thickness 5 | SKY_CLOUD_5_THICKNESS | REAL | 0 | 5000 |  | 
Transparency 5 | SKY_CLOUD_5_TRANSPARENCY | REAL | 0 | 100 |  | 
No label | SKY_CLOUD_5_PREVIEW | MATPREVIEW |  |  |  | 
Save as Preset... | SKY_CLOUD_5_SAVE_PRESET | BUTTON |  |  |  | 
Load Preset... | SKY_CLOUD_5_LOAD_PRESET | BUTTON |  |  |  | 
Anim. Speed 5 | SKY_CLOUD_5_SPEED | REAL |  |  |  | 
Noise Offset 5 | SKY_CLOUD_5_OFFSET | REAL |  |  |  | 
Scale N-S 5 | SKY_CLOUD_5_SCALE_NS | REAL | 1 |  |  | 
Scale W-E 5 | SKY_CLOUD_5_SCALE_WE | REAL | 1 |  |  | 
Pos. N-S 5 | SKY_CLOUD_5_MOVE_NS | REAL |  |  |  | 
Pos. W-E 5 | SKY_CLOUD_5_MOVE_WE | REAL |  |  |  | 
Noise 6 | SKY_CLOUD_6_NOISE | LONG |  |  |  | 
Color 6 | SKY_CLOUD_6_COLOR | COLOR |  |  |  | 
Height 6 | SKY_CLOUD_6_HEIGHT | REAL | 0 | 50000 |  | 
Density 6 | SKY_CLOUD_6_DENSITY | REAL | 0 | 5000 |  | 
Coverage 6 | SKY_CLOUD_6_COVERAGE | REAL | 0 | 100 |  | 
Thickness 6 | SKY_CLOUD_6_THICKNESS | REAL | 0 | 5000 |  | 
Transparency 6 | SKY_CLOUD_6_TRANSPARENCY | REAL | 0 | 100 |  | 
No label | SKY_CLOUD_6_PREVIEW | MATPREVIEW |  |  |  | 
Save as Preset... | SKY_CLOUD_6_SAVE_PRESET | BUTTON |  |  |  | 
Load Preset... | SKY_CLOUD_6_LOAD_PRESET | BUTTON |  |  |  | 
Anim. Speed 6 | SKY_CLOUD_6_SPEED | REAL |  |  |  | 
Noise Offset 6 | SKY_CLOUD_6_OFFSET | REAL |  |  |  | 
Scale N-S 6 | SKY_CLOUD_6_SCALE_NS | REAL | 1 |  |  | 
Scale W-E 6 | SKY_CLOUD_6_SCALE_WE | REAL | 1 |  |  | 
Pos. N-S 6 | SKY_CLOUD_6_MOVE_NS | REAL |  |  |  | 
Pos. W-E 6 | SKY_CLOUD_6_MOVE_WE | REAL |  |  |  | 
Show Moon | SKY_ASTRO_MOON_SHOW | BOOL |  |  |  | 
Scale | SKY_GENERAL_SCALE_MOON | REAL | 0.1 |  |  | 
Bright Intensity | SKY_GENERAL_MOON_BRIGHT | REAL | 0 | 100 |  | 
Dark Intensity | SKY_GENERAL_MOON_DARK | REAL | 0 | 100 |  | 
Distance Scale | SKY_GENERAL_MOON_DIST_SCALE | REAL | 0 |  |  | 
Custom Moon Object | SKY_OBJECT_MOON_OBJECT | LINK |  |  |  | 
Show Stars | SKY_ASTRO_SHOW_STARS | BOOL |  |  |  | 
Min Magnitude | SKY_GENERAL_MIN_MAG | REAL | 0 | 10.5 |  | 
Resize Stars with Magnitude | SKY_GENERAL_RESIZE_STARS | BOOL |  |  |  | 
Brighten Stars | SKY_GENERAL_LIGHTEN_UP_STARS | REAL | 0 | 100 |  | 
Star Radius | SKY_GENERAL_STAR_RADIUS | REAL | 0.1 | 5 |  | 
Show Constellations | SKY_GENERAL_SHOW_CONSTELLATIONS | BOOL |  |  |  | 
Constellation color | SKY_GENERAL_CONSTELLATION_COLOR | COLOR |  |  |  | 
Grid Width | SKY_GENERAL_GRID_WIDTH | REAL | 0 | 180 |  | 
Grid Color | SKY_GENERAL_GRID_COLOR | COLOR |  |  |  | 
Show Planets | SKY_ASTRO_PLANETS_SHOW | BOOL |  |  |  | 
Scale | SKY_GENERAL_SCALE_PLANETS | REAL | 0.1 |  |  | 
Sky Dome Ambient Light | SKY_GENERAL_SKY_DOME | BOOL |  |  |  | 
Merge Sky and Sun | SKY_GENERAL_MERGE_SUN | BOOL |  |  |  | 
GI Generate | SKY_MATERIAL_GLOBALILLUM_GENERATE | BOOL |  |  |  | 
GI Generate Strength | SKY_MATERIAL_GLOBALILLUM_GENERATE_STRENGTH | REAL | 0.0 | 10000.0 |  | 
Saturation | SKY_GENERAL_GI_SATURATION | REAL | 0 | 100 |  | 
Cloud Influence | SKY_GENERAL_GI_INFLUENCE | REAL | 0 | 100 |  | 
Priority | SKY_EXPRESSION_PRIORITY | PRIORITY |  |  |  | 
Texture Preview Size | SKY_MATERIAL_PREVIEWSIZE | LONG |  |  |  | SKY_MATERIAL_PREVIEWSIZE_DEF; SKY_MATERIAL_PREVIEWSIZE_64; SKY_MATERIAL_PREVIEWSIZE_128; SKY_MATERIAL_PREVIEWSIZE_256; SKY_MATERIAL_PREVIEWSIZE_512; SKY_MATERIAL_PREVIEWSIZE_1024; SKY_MATERIAL_PREVIEWSIZE_2048; SKY_MATERIAL_PREVIEWSIZE_4096
Show Location HUD | SKY_SHOW_HUD | BOOL |  |  |  | 
Update Editor | SKY_UPDATE_EDITOR | BOOL |  |  |  | 
Show Bounding Box | SKY_SHOW_CLOUD_BOX | BOOL |  |  |  | 
Editor Color | SKY_CLOUD_EDITOR_COLOR | COLOR |  |  |  | 
Editor Quality | SKY_CLOUD_EDITOR_QUALITY | REAL | 0 | 100 |  | 
Adjust Altitude | SKY_VOL_CLOUDS_ADJUST_ALTITUDE | BOOL |  |  |  | 
Receive Shadows | SKY_VOL_CLOUDS_RECEIVE_SHADOWS | BOOL |  |  |  | 
Sample Size | SKY_VOL_CLOUDS_SAMPLE_SIZE | REAL | 0 |  |  | 
Edge Noise | SKY_VOL_CLOUDS_EDGE_NOISE_NOISE | LONG |  |  |  | 
Contrast | SKY_VOL_CLOUDS_EDGE_NOISE_CONTRAST | REAL | 0 | 100 |  | 
Scale | SKY_VOL_CLOUDS_EDGE_NOISE_SCALE | REAL | 0 |  |  | 
Noise Speed | SKY_VOL_CLOUDS_EDGE_NOISE_SPEED | REAL | 0 |  |  | 
Lights | SKY_VOL_CLOUDS_LIGHT_LIST | IN_EXCLUDE |  |  |  | 
Color | SKY_FOG_COLOR | COLOR |  |  |  | 
Start Height | SKY_FOG_START | REAL |  |  |  | 
End Height | SKY_FOG_END | REAL |  |  |  | 
Max. Distance | SKY_FOG_MAXDIST | REAL | 0 | 200000 |  | 
Density | SKY_FOG_DENSITY | REAL | 0 |  |  | 
Density Distribution | SKY_FOG_DENSITY_DISTRIB | SPLINE |  |  |  | 
Noise | SKY_FOG_NOISE | LONG |  |  |  | 
Noise Strength | SKY_FOG_NOISE_STRENGTH | REAL | -1000 | 1000 |  | 
Scale | SKY_FOG_SCALE | VECTOR | 0 |  |  | 
Movement | SKY_FOG_MOVEMENT | VECTOR |  |  |  | 
Sample Size | SKY_FOG_SAMPLE_SIZE | REAL | 5 |  |  | 
Animation Speed | SKY_FOG_ANIMATION_SPEED | REAL | 0 |  |  | 
Shadow Intensity | SKY_FOG_SHADOW_INTENSITY | REAL | 0 | 100 |  | 
Illumination Intensity | SKY_FOG_ILLUM_INTENSITY | REAL | 0 | 100 |  | 
Max. Strength | SKY_RAINBOW_MAX_STRENGTH | REAL | 0 | 100 |  | 
Turbidity Dependent | SKY_RAINBOW_TURBIDITY_DEP | BOOL |  |  |  | 
Min. Turbidity Threshold | SKY_RAINBOW_TURBIDITY_THRESHOLD_MIN | REAL | 0 | 100 |  | 
Max. Turbidity Threshold | SKY_RAINBOW_TURBIDITY_THRESHOLD_MAX | REAL | 0 | 100 |  | 
First Rainbow Inner Angle | SKY_RAINBOW_1_INNER | REAL | 0 | 180 |  | 
First Rainbow Outer Angle | SKY_RAINBOW_1_OUTER | REAL | 0 | 180 |  | 
Secondary Rainbow Inner Angle | SKY_RAINBOW_2_INNER | REAL | 0 | 180 |  | 
Secondary Rainbow Outer Angle | SKY_RAINBOW_2_OUTER | REAL | 0 | 180 |  | 
Start Clipping | SKY_RAINBOW_START_CLIP | REAL |  |  |  | 
End Clipping | SKY_RAINBOW_END_CLIP | REAL |  |  |  | 
Turbidity Dependent | SKY_BEAMS_TURBIDITY_DEPENDENT | BOOL |  |  |  | 
Intensity | SKY_BEAMS_INTENS | REAL | 0 | 100 |  | 
Min. Brightness | SKY_BEAMS_MIN_BRIGHTNESS | REAL | 0 | 200 |  | 
Start Distance | SKY_BEAMS_START | REAL | 0 |  |  | 
End Distance | SKY_BEAMS_END | REAL | 0 |  |  | 
Sample Distance | SKY_BEAMS_SAMPLE_DIST | REAL | 20 |  |  | 
Sky Objects | SKY_SKY_OBJECTS | SKY_OBJECTS |  |  |  | 
Place Object... | SKY_SKY_OBECT_PLACE | BUTTON |  |  |  | 
