# Description: Text Layer

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/c4d_manager/description/vptext.res`
- **Symbol:** `VPtext`
- **Category:** Video Posts

Use parameter symbols to access parameters and cycle option symbols for cycle values, never their numeric IDs. Treat Min and Max as constraints and Default as the declared initial value; blank cells mean the resource does not declare that metadata, not that the value is zero. Base Description Parameters lists inherited fields from each base; All Parameters lists the effective parameter set for this description.

## Base Description Parameters

### Post Effect (`VPbase`)

No parameters.

## All Parameters

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Rendered | VP_TEXT_RENDER_OUTPUT_RENDER | BOOL |  |  |  | 
VideoPost | VP_TEXT_RENDER_OUTPUT_VIDEOPOST | BOOL |  |  |  | 
MultiPass | VP_TEXT_RENDER_OUTPUT_MULTIPASS | BOOL |  |  |  | 
Title | VP_TEXT_STRING | STRING |  |  |  | 
U | VP_TEXT_U | REAL | 0.0 | 100.0 |  | 
V | VP_TEXT_V | REAL | 0.0 | 100.0 |  | 
Tab Size | VP_TEXT_TAB_SIZE | LONG | 0 | 16 |  | 
Align | VP_TEXT_ALIGN | LONG |  |  |  | VP_TEXT_ALIGN_LEFT; VP_TEXT_ALIGN_CENTER; VP_TEXT_ALIGN_RIGHT
Align | VP_TEXT_INFO_ALIGN | LONG |  |  |  | VP_TEXT_INFO_ALIGN_TOP; VP_TEXT_INFO_ALIGN_BOTTOM
Objects | VP_TEXT_INFO_OBJECTCOUNT | BOOL |  |  |  | 
Lights | VP_TEXT_INFO_LIGHTCOUNT | BOOL |  |  |  | 
Polygons | VP_TEXT_INFO_POLYGONCOUNT | BOOL |  |  |  | 
Vertices | VP_TEXT_INFO_VERTEXCOUNT | BOOL |  |  |  | 
Render Time | VP_TEXT_INFO_SCENETIME | BOOL |  |  |  | 
Color | VP_TEXT_PEN | COLOR |  |  |  | 
Opacity | VP_TEXT_PEN_OPACITY | REAL | 0.0 | 100.0 |  | 
Color | VP_TEXT_PAPER | COLOR |  |  |  | 
Opacity | VP_TEXT_PAPER_OPACITY | REAL | 0.0 | 100.0 |  | 
Border Offset | VP_TEXT_PAPER_BORDER | LONG | 0 | 100 |  | 
Rounding | VP_TEXT_PAPER_ROUNDING | LONG | 0 | 100 |  | 
Draw Border | VP_TEXT_PAPER_DRAW_BORDER | BOOL |  |  |  | 
Image | VP_TEXT_WATERMARK | TEXTURE |  |  |  | 
Opacity | VP_TEXT_WATERMARK_OPACITY | REAL | 0.0 | 100.0 |  | 
Scale | VP_TEXT_WATERMARK_SCALE | REAL | 0.0 | 100.0 |  | 
Vertical Alignment | VP_TEXT_WATERMARK_V_ALIGN | LONG |  |  |  | VP_TEXT_WATERMARK_TOP; VP_TEXT_WATERMARK_VCENTER; VP_TEXT_WATERMARK_BOTTOM
Horizontal Alignment | VP_TEXT_WATERMARK_H_ALIGN | LONG |  |  |  | VP_TEXT_WATERMARK_LEFT; VP_TEXT_WATERMARK_HCENTER; VP_TEXT_WATERMARK_RIGHT
