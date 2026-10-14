# Description: Motion Clip

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/c4d_manager/description/mt_clip.res`
- **Symbol:** `MT_CLIP`
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
Color | ID_MT_CLIP_COLOR | COLOR |  |  |  | 
Locked | ID_MT_CLIP_LOCK | BOOL |  |  |  | 
Show Ghost | ID_MT_CLIP_GHOST | BOOL |  |  |  | 
Source | ID_MT_CLIP_SOURCE | LINK |  |  |  | 
Start | ID_MT_CLIP_VIEWSTART | BASETIME |  |  |  | 
End | ID_MT_CLIP_VIEWEND | BASETIME |  |  |  | 
Loops | ID_MT_CLIP_LOOP | REAL | 0.0 |  |  | 
Relative Loop | ID_MT_CLIP_LOOPRELATIVE | BOOL |  |  |  | 
Auto Blend Range | ID_MT_CLIP_AUTO | BOOL |  |  |  | 
Blend Gap | ID_MT_CLIP_AUTOGAP | BOOL |  |  |  | 
Blend Start | ID_MT_CLIP_MIX_START | BASETIME |  |  |  | 
Blend End | ID_MT_CLIP_MIX_END | BASETIME |  |  |  | 
Blending | ID_MT_CLIP_TYPEFADEOUT | LONG |  |  |  | ID_MT_CLIP_FADEOFF; ID_MT_CLIP_FADEEASE; ID_MT_CLIP_FADELINEAR; ID_MT_CLIP_EASEIN; ID_MT_CLIP_EASEOUT; ID_MT_CLIP_FADESPLINE
Spline | ID_MT_CLIP_FADESPLINEWND | SPLINE |  |  |  | 
Source View | ID_MT_CLIP_SOURCEVIEW | SOURCECLIP |  |  |  | 
&#92;u0394 Start | ID_MT_CLIP_TRIMSTART | BASETIME | 0.0 |  |  | 
&#92;u0394 End | ID_MT_CLIP_TRIMEND | BASETIME | 0.0 |  |  | 
Pivot | ID_MT_CLIP_PIVOT | LINK |  |  |  | 
Create Pivot | ID_MT_CLIP_CREATEPIVOT | BUTTON |  |  |  | 
Create Keyframed Pivot | ID_MT_CLIP_CREATEPIVOTK | BUTTON |  |  |  | 
Snap to Start Time | ID_MT_CLIP_SNAP1 | BUTTON |  |  |  | 
Snap to Actual Time | ID_MT_CLIP_SNAP2 | BUTTON |  |  |  | 
Snap to End Time | ID_MT_CLIP_SNAP3 | BUTTON |  |  |  | 
Timing | ID_MT_CLIP_TIMWARPWND | SPLINE |  |  |  | 
