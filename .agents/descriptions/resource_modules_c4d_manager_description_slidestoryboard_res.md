# Description: Properties

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/c4d_manager/description/slidestoryboard.res`
- **Symbol:** `SlideStoryboard`
- **Category:** Other

Use parameter symbols to access parameters and cycle option symbols for cycle values, never their numeric IDs. Treat Min and Max as constraints and Default as the declared initial value; blank cells mean the resource does not declare that metadata, not that the value is zero. Base Description Parameters lists inherited fields from each base; All Parameters lists the effective parameter set for this description.

## Base Description Parameters

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
Duration | STORYBOARDSLIDE_DURATION | BASETIME | 0 |  |  | 
Animation | STORYBOARDSLIDE_ANIMATION_TYPE | LONG |  |  |  | STORYBOARDSLIDE_ANIMATION_TYPE_NONE; STORYBOARDSLIDE_ANIMATION_TYPE_SLIDE; STORYBOARDSLIDE_ANIMATION_TYPE_PAN; STORYBOARDSLIDE_ANIMATION_TYPE_ORBIT
Orbit | STORYBOARDSLIDE_ORBIT_DIRECTION | LONG |  |  |  | STORYBOARDSLIDE_ORBIT_DIRECTION_LEFT; STORYBOARDSLIDE_ORBIT_DIRECTION_RIGHT; STORYBOARDSLIDE_ORBIT_DIRECTION_UP; STORYBOARDSLIDE_ORBIT_DIRECTION_DOWN
Rotation Angle | STORYBOARDSLIDE_ORBIT_ANGLE | REAL | 0.0 |  |  | 
Distance | STORYBOARDSLIDE_ORBIT_DISTANCE | REAL | 0.0 |  |  | 
Target Object | STORYBOARDSLIDE_TARGET_OBJECTLINK | LINK |  |  |  | 
Reverse | STORYBOARDSLIDE_ORBIT_REVERSE | BOOL |  |  |  | 
Direction | STORYBOARDSLIDE_PAN_DIRECTION | LONG |  |  |  | STORYBOARDSLIDE_PAN_DIRECTION_LEFT; STORYBOARDSLIDE_PAN_DIRECTION_RIGHT; STORYBOARDSLIDE_PAN_DIRECTION_UP; STORYBOARDSLIDE_PAN_DIRECTION_DOWN
Rotation Angle | STORYBOARDSLIDE_PAN_ANGLE | REAL | 0.0 | 360.0 |  | 
Reverse | STORYBOARDSLIDE_PAN_REVERSE | BOOL |  |  |  | 
Direction | STORYBOARDSLIDE_SLIDE_DIRECTION | LONG |  |  |  | STORYBOARDSLIDE_SLIDE_DIRECTION_FORWARDS; STORYBOARDSLIDE_SLIDE_DIRECTION_BACKWARDS; STORYBOARDSLIDE_SLIDE_DIRECTION_LEFT; STORYBOARDSLIDE_SLIDE_DIRECTION_RIGHT; STORYBOARDSLIDE_SLIDE_DIRECTION_UP; STORYBOARDSLIDE_SLIDE_DIRECTION_DOWN
Radius | STORYBOARDSLIDE_SLIDE_DISTANCE | REAL | 0.0 |  |  | 
Look At | STORYBOARDSLIDE_SLIDE_LOOK_AT | LINK |  |  |  | 
Respect Camera Plane | STORYBOARDSLIDE_SLIDE_IGNORE_TILT | BOOL |  |  |  | 
Reverse | STORYBOARDSLIDE_SLIDE_REVERSE | BOOL |  |  |  | 
Interpolation | STORYBOARDSLIDE_ADVANCED_INTERPOLATION | LONG |  |  |  | STORYBOARDSLIDE_ADVANCED_INTERPOLATION_LINEAR; STORYBOARDSLIDE_ADVANCED_INTERPOLATION_SMOOTH
