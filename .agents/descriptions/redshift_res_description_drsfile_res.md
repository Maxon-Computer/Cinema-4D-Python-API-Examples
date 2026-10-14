# Description: RSFile Datatype

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `Redshift/res/description/drsfile.res`
- **Symbol:** `Drsfile`
- **Category:** Other

Use parameter symbols to access parameters and cycle option symbols for cycle values, never their numeric IDs. Treat Min and Max as constraints and Default as the declared initial value; blank cells mean the resource does not declare that metadata, not that the value is zero. Base Description Parameters lists inherited fields from each base; All Parameters lists the effective parameter set for this description.

## Base Description Parameters

No base descriptions.

## All Parameters

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Path | REDSHIFT_FILE_PATH | FILENAME |  |  |  | 
Layer | REDSHIFT_FILE_LAYER | STRING |  |  |  | 
Color Space | REDSHIFT_FILE_COLORSPACE | STRING |  |  |  | 
Animation | REDSHIFT_FILE_ANIMATION_MODE | LONG |  |  |  | REDSHIFT_FILE_ANIMATION_MODE_OFF; REDSHIFT_FILE_ANIMATION_MODE_SIMPLE; REDSHIFT_FILE_ANIMATION_MODE_LOOP; REDSHIFT_FILE_ANIMATION_MODE_PINGPONG
Range Start | REDSHIFT_FILE_ANIMATION_RANGE_START | BASETIME |  |  |  | 
Range End | REDSHIFT_FILE_ANIMATION_RANGE_END | BASETIME |  |  |  | 
Loops | REDSHIFT_FILE_ANIMATION_LOOP_COUNT | LONG |  |  |  | 
Start Frame | REDSHIFT_FILE_ANIMATION_FRAME_START | LONG |  |  |  | 
End Frame | REDSHIFT_FILE_ANIMATION_FRAME_END | LONG |  |  |  | 
Frame Rate | REDSHIFT_FILE_ANIMATION_FRAME_RATE | LONG |  |  |  | 
Start Offset | REDSHIFT_FILE_ANIMATION_FRAME_OFFSET | LONG |  |  |  | 
Timing | REDSHIFT_FILE_ANIMATION_TIMING_MODE | LONG |  |  |  | REDSHIFT_FILE_ANIMATION_TIMING_MODE_FRAME; REDSHIFT_FILE_ANIMATION_TIMING_MODE_TIME; REDSHIFT_FILE_ANIMATION_TIMING_MODE_RANGE
