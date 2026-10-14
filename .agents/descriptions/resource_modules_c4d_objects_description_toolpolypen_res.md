# Description: Polygon Pen

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/c4d_objects/description/toolpolypen.res`
- **Symbol:** `toolpolypen`
- **Category:** Other

Use parameter symbols to access parameters and cycle option symbols for cycle values, never their numeric IDs. Treat Min and Max as constraints and Default as the declared initial value; blank cells mean the resource does not declare that metadata, not that the value is zero. Base Description Parameters lists inherited fields from each base; All Parameters lists the effective parameter set for this description.

## Base Description Parameters

### Base Tool (`ToolBase`)

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Realtime Update | MDATA_INTERACTIVE | BOOL |  |  |  | 
    Apply     | MDATA_APPLY | BUTTON |  |  |  | 
New Transform | MDATA_NEWTRANSFORM | BUTTON |  |  |  | 
No label | ID_SNAPSETTINGS | SUBCONTAINER |  |  |  | 

## All Parameters

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Realtime Update | MDATA_INTERACTIVE | BOOL |  |  |  | 
    Apply     | MDATA_APPLY | BUTTON |  |  |  | 
New Transform | MDATA_NEWTRANSFORM | BUTTON |  |  |  | 
No label | ID_SNAPSETTINGS | SUBCONTAINER |  |  |  | 
Draw Mode | MDATA_POLYPEN_DRAWMODE | LONG |  |  |  | MDATA_POLYPEN_DRAWMODE_POINTS; MDATA_POLYPEN_DRAWMODE_EDGES; MDATA_POLYPEN_DRAWMODE_POLYGONS
Quad Strip Mode | MDATA_POLYPEN_QUADSTRIP | BOOL |  |  |  | 
Auto Weld | MDATA_POLYPEN_AUTOWELD | BOOL |  |  |  | 
Reproject Result | MDATA_POLYPEN_REPROJECT | BOOL |  |  |  | 
Create Coplanar Edge On Extrude | MDATA_POLYPEN_CREATEEDGEEXTRUED | BOOL |  |  |  | 
Create N-gons | MDATA_POLYPEN_CREATENGONS | BOOL |  |  |  | 
Create Semi Circle | MDATA_POLYPEN_HALFCIRCLE | BOOL |  |  |  | 
Arc Direction Max Angle | MDATA_POLYPEN_ARCANGLE | REAL | 0 | 180 |  | 
Arc Subdivision | MDATA_POLYPEN_ARCSUBDIVISION | LONG | 0 | 500 |  | 
Polygon Brush Radius | MDATA_POLYPEN_POLYPAINTSIZE | REAL | 0.001 |  |  | 
Tweaking Mode | MDATA_POLYPEN_EXCLUSIVEMODE | LONG |  |  |  | MDATA_POLYPEN_EXCLUSIVEMODE_POINTEDGEPOLYS; MDATA_POLYPEN_EXCLUSIVEMODE_POINT; MDATA_POLYPEN_EXCLUSIVEMODE_EDGE; MDATA_POLYPEN_EXCLUSIVEMODE_POLY; MDATA_POLYPEN_EXCLUSIVEMODE_USEMODE
