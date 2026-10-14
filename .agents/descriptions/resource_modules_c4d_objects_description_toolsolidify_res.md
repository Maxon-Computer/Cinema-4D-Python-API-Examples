# Description: Thicken

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/c4d_objects/description/toolsolidify.res`
- **Symbol:** `ToolSolidify`
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
Mode | MDATA_SOLIDIFYTOOL_MODE | LONG |  |  |  | MDATA_SOLIDIFYTOOL_MODE_SIMPLE; MDATA_SOLIDIFYTOOL_MODE_COMPLEX
Thickness | MDATA_SOLIDIFYTOOL_THICKNESS | REAL | 0.0 |  |  | 
Clamp | MDATA_SOLIDIFYTOOL_THICKNESSCLAMP | REAL | 100.0 |  |  | 
Position | MDATA_SOLIDIFYTOOL_POSITION | REAL | -100.0 | 100.0 |  | 
Subdivision | MDATA_SOLIDIFYTOOL_BOUNDARYSUBDIVISION | LONG | 0 |  |  | 
Shell | MDATA_SOLIDIFYTOOL_CREATEBOUNDARY | BOOL |  |  |  | 
Start Cap | MDATA_SOLIDIFYTOOL_CREATEINSIDE | BOOL |  |  |  | 
End Cap | MDATA_SOLIDIFYTOOL_CREATEOUTSIDE | BOOL |  |  |  | 
Resolve Intersections | MDATA_SOLIDIFYTOOL_COMPLEX_RESOLVEINTERSECTION | BOOL |  |  |  | 
Optimize | MDATA_SOLIDIFYTOOL_COMPLEX_WELDCOLLAPSED | BOOL |  |  |  | 
Perpendicular Boundary | MDATA_SOLIDIFYTOOL_COMPLEX_FORCEPERPENDICULARBOUNDARY | BOOL |  |  |  | 
Perpendicular Boundary | MDATA_SOLIDIFYTOOL_COMPLEX_PERPENDICULARANGLELIMIT | REAL | 0.0 | 180.0 |  | 
Preserve Corners | MDATA_SOLIDIFYTOOL_COMPLEX_PRESERVECORNERS | BOOL |  |  |  | 
Preserve Corners | MDATA_SOLIDIFYTOOL_COMPLEX_PRESERVECORNERSANGLE | REAL | 0.0 | 180.0 |  | 
