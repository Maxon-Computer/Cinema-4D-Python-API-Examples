# Description: Alembic Morph Tag

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/io_alembic/description/Talembicmorphtag.res`
- **Symbol:** `Talembicmorphtag`
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
Scale | ALEMBIC_MT_UNIT_SCALE | UNITSCALE |  |  |  | 
Path to Alembic File | ALEMBIC_MT_PATH | FILENAME |  |  |  | 
No label | ALEMBIC_MT_PATH_STATE | BOOL |  |  |  | 
Object Identifier | ALEMBIC_MT_IDENTIFIER | STRING |  |  |  | 
No label | ALEMBIC_MT_IDENT_STATE | BOOL |  |  |  | 
Animation | ALEMBIC_MT_STR_ANIMATION | SEPARATOR |  |  |  | 
Use Animation | ALEMBIC_MT_USE_ANIMATION | BOOL |  |  |  | 
Frame | ALEMBIC_MT_ANIMATION_FRAME | BASETIME |  |  |  | 
Interpolation | ALEMBIC_MT_INTERPOLATION | BOOL |  |  |  | 
Offset | ALEMBIC_MT_ANIMATION_OFFSET | BASETIME |  |  |  | 
Mode | ALEMBIC_MT_ANIMATION_MODE | LONG |  |  | ALEMBIC_MT_ANIMATION_MODE_PLAY | ALEMBIC_MT_ANIMATION_MODE_PLAY; ALEMBIC_MT_ANIMATION_MODE_LOOP; ALEMBIC_MT_ANIMATION_MODE_PINGPONG
Speed | ALEMBIC_MT_ANIMATION_SPEED | REAL | 0.0 |  |  | 
Reset | ALEMBIC_MT_ANIMATION_RESET | BUTTON |  |  |  | 
Remapping Curve | ALEMBIC_MT_ANIMATION_CURVE | SPLINE |  |  |  | 
Streaming | ALEMBIC_MT_STR_UPDATE | SEPARATOR |  |  |  | 
Update Transform | ALEMBIC_MT_UPDATE_XFORM | BOOL |  |  |  | 
Update Geometry | ALEMBIC_MT_UPDATE_GEOMETRY | BOOL |  |  |  | 
Visibility | ALEMBIC_MT_USE_VISIBILITY | BOOL |  |  |  | 
Color Maps | ALEMBIC_MT_USE_COLORMAPS | BOOL |  |  |  | 
Other Attributes | ALEMBIC_MT_USE_OTHERATTR | BOOL |  |  |  | 
