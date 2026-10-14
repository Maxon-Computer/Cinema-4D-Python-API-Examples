# Description: Curl

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/hair/description/toolhaircurl.res`
- **Symbol:** `ToolHairCurl`
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
Strength | HAIR_TOOL_CURL_STRENGTH | REAL |  |  |  | 
Angle | HAIR_TOOL_CURL_ANGLE | REAL |  |  |  | 
Tightness | HAIR_TOOL_CURL_TIGHTNESS | REAL |  |  |  | 
X Height | HAIR_TOOL_CURL_AMP_X | REAL | 0.0 |  |  | 
X Length | HAIR_TOOL_CURL_PERIOD_X | REAL | 0.0 |  |  | 
Y Height | HAIR_TOOL_CURL_AMP_Y | REAL | 0.0 |  |  | 
Y Length | HAIR_TOOL_CURL_PERIOD_Y | REAL | 0.0 |  |  | 
X Curl | HAIR_TOOL_CURL_X | SPLINE |  |  |  | 
Y Curl | HAIR_TOOL_CURL_Y | SPLINE |  |  |  | 
Strength X | HAIR_TOOL_CURL_STRENGTH_X | SPLINE |  |  |  | 
Strength Y | HAIR_TOOL_CURL_STRENGTH_Y | SPLINE |  |  |  | 
Tighten | HAIR_TOOL_CURL_TIGHTEN | SPLINE |  |  |  | 
