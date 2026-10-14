# Description: Watermark

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/c4d_manager/description/vpwatermark.res`
- **Symbol:** `vpwatermark`
- **Category:** Video Posts

Use parameter symbols to access parameters and cycle option symbols for cycle values, never their numeric IDs. Treat Min and Max as constraints and Default as the declared initial value; blank cells mean the resource does not declare that metadata, not that the value is zero. Base Description Parameters lists inherited fields from each base; All Parameters lists the effective parameter set for this description.

## Base Description Parameters

### Post Effect (`VPbase`)

No parameters.

## All Parameters

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Enable | VP_WATERMARK_TEXT_ENABLE | BOOL |  |  |  | 
Dynamic Layout | VP_WATERMARK_TEXT_DYNAMICLAYOUT | BOOL |  |  |  | 
Show Labels | VP_WATERMARK_TEXT_SHOWLABELS | BOOL |  |  |  | 
Time Code | VP_WATERMARK_TEXT_TIMECODE | BOOL |  |  |  | 
Render Time | VP_WATERMARK_TEXT_RENDERTIME | BOOL |  |  |  | 
Active Camera | VP_WATERMARK_TEXT_ACTIVECAMERA | BOOL |  |  |  | 
Date | VP_WATERMARK_TEXT_DATE | BOOL |  |  |  | 
Project Name | VP_WATERMARK_TEXT_SCENENAME | BOOL |  |  |  | 
Polygon Count | VP_WATERMARK_TEXT_POLYCOUNT | BOOL |  |  |  | 
Version Info | VP_WATERMARK_TEXT_C4DVERSION | BOOL |  |  |  | 
Machine Info | VP_WATERMARK_TEXT_MACHINEINFO | BOOL |  |  |  | 
Take | VP_WATERMARK_TEXT_TAKE | BOOL |  |  |  | 
Footer | VP_WATERMARK_TEXT_CUSTOM | BOOL |  |  |  | 
Text | VP_WATERMARK_TEXT_CUSTOM_TEXT | STRING |  |  |  | 
No label | VP_WATERMARK_TEXT_CUSTOM_TEXT_PH | POPUP |  |  |  | 
Background Opacity | VP_WATERMARK_TEXT_BG_OPACITY | REAL | 0.0 | 100.0 |  | 
Vertical Alignment | VP_WATERMARK_TEXT_POS_Y | LONG |  |  |  | VP_WATERMARK_POS_TOP; VP_WATERMARK_POS_BOTTOM
Font | VP_WATERMARK_TEXT_FONT | FONT |  |  |  | 
Color | VP_WATERMARK_TEXT_COLOR | COLOR |  |  |  | 
Background Color | VP_WATERMARK_TEXT_BG_COLOR | COLOR |  |  |  | 
Enable | VP_WATERMARK_IMG_ENABLE | BOOL |  |  |  | 
Filename | VP_WATERMARK_IMG_FILENAME | FILENAME |  |  |  | 
Opacity | VP_WATERMARK_IMG_OPACITY | REAL | 0.0 | 100.0 |  | 
Blend Mode | VP_WATERMARK_IMG_BLENDMODE | LONG |  |  |  | VP_IMG_BLENDMODE_NORMAL; VP_IMG_BLENDMODE_LIGHTEN; VP_IMG_BLENDMODE_DARKEN; VP_IMG_BLENDMODE_MULTIPLY; VP_IMG_BLENDMODE_ADD; VP_IMG_BLENDMODE_OVERLAY; VP_IMG_BLENDMODE_COLORDODGE; VP_IMG_BLENDMODE_COLORBURN; VP_IMG_BLENDMODE_LINEARDODGE; VP_IMG_BLENDMODE_LINEARBURN; VP_IMG_BLENDMODE_COLOR; VP_IMG_BLENDMODE_COLOR_INV
Horizontal Alignment | VP_WATERMARK_IMG_POS_X | LONG |  |  |  | VP_WATERMARK_POS_LEFT; VP_WATERMARK_POS_CENTER; VP_WATERMARK_POS_RIGHT
Vertical Alignment | VP_WATERMARK_IMG_POS_Y | LONG |  |  |  | VP_WATERMARK_POS_TOP; VP_WATERMARK_POS_CENTER; VP_WATERMARK_POS_BOTTOM
Margin | VP_WATERMARK_IMG_MARGIN | LONG | 0 |  |  | 
Scale | VP_WATERMARK_IMG_SCALE | REAL | 0.1 | 1000.0 |  | 
Keep Aspect Ratio | VP_WATERMARK_IMG_SCALE_ASPECT | BOOL |  |  |  | 
Keep Original Size | VP_WATERMARK_IMG_SCALE_KEEPSIZE | BOOL |  |  |  | 
