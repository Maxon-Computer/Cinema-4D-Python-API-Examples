# Description: BodyPaint 3D

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/c4d_xtensions/description/pbodypaint.res`
- **Symbol:** `Pbodypaint`
- **Category:** Other

Use parameter symbols to access parameters and cycle option symbols for cycle values, never their numeric IDs. Treat Min and Max as constraints and Default as the declared initial value; blank cells mean the resource does not declare that metadata, not that the value is zero. Base Description Parameters lists inherited fields from each base; All Parameters lists the effective parameter set for this description.

## Base Description Parameters

No base descriptions.

## All Parameters

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Texture | PBODYPAINT_GROUP_TEX | SEPARATOR |  |  |  | 
Default Format | PBODYPAINT_DEFAULTTEXTUREFORMAT | LONG |  |  |  | PBODYPAINT_DEFAULTTEXTUREFORMAT_B3D; PBODYPAINT_DEFAULTTEXTUREFORMAT_PSD; PBODYPAINT_DEFAULTTEXTUREFORMAT_TIF
Brush | PBODYPAINT_GROUP_BRUSH | SEPARATOR |  |  |  | 
Show on Mouse Move | PBODYPAINT_SHOWBRUSHMOUSEMOVE | BOOL |  |  |  | 
Show while Painting | PBODYPAINT_SHOWBRUSHPAINTING | BOOL |  |  |  | 
Tool Cursors | PBODYPAINT_TOOLCURSOR | LONG |  |  |  | PBODYPAINT_TOOLCURSOR_STAND; PBODYPAINT_TOOLCURSOR_CROSS; PBODYPAINT_TOOLCURSOR_HIDE
Projection Painting | PBODYPAINT_GROUP_PRJPAINT | SEPARATOR |  |  |  | 
Pixel Border around UV Poly | PBODYPAINT_PIXELBORDER | LONG | 0 | 20 |  | 
Tile U | PBODYPAINT_TILEU | BOOL |  |  |  | 
Tile V | PBODYPAINT_TILEV | BOOL |  |  |  | 
Project on Invisible Parts | PBODYPAINT_PROJECTON | BOOL |  |  |  | 
Ignore Unpaintable Geometry | PBODYPAINT_PP_PROJECT_THROUGH_UNPAINTABLE | BOOL |  |  |  | 
Border on Same Object | PBODYPAINT_BORDERON | BOOL |  |  |  | 
Continue UVs on Border | PBODYPAINT_CONTINUE | BOOL |  |  |  | 
Bitmap Filter | PBODYPAINT_GROUP_FILTER | SEPARATOR |  |  |  | 
Preview Width | PBODYPAINT_FILTER_WIDTH | LONG | 64 | 512 |  | 
Preview Height | PBODYPAINT_FILTER_HEIGHT | LONG | 64 | 512 |  | 
Show Source Preview | PBODYPAINT_FILTER_SHOWPREV | BOOL |  |  |  | 
