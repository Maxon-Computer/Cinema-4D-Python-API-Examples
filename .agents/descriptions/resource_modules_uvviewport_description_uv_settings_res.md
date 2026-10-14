# Description: UV Settings

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/uvviewport/description/uv_settings.res`
- **Symbol:** `uv_settings`
- **Category:** Other

Use parameter symbols to access parameters and cycle option symbols for cycle values, never their numeric IDs. Treat Min and Max as constraints and Default as the declared initial value; blank cells mean the resource does not declare that metadata, not that the value is zero. Base Description Parameters lists inherited fields from each base; All Parameters lists the effective parameter set for this description.

## Base Description Parameters

No base descriptions.

## All Parameters

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
UV Display | UV_SETTINGS_DISPLAY_UVDISPLAY | BOOL |  |  |  | 
Pins | UV_SETTINGS_DISPLAY_PINS | BOOL |  |  |  | 
Boundaries | UV_SETTINGS_DISPLAY_BOUNDARIES | LONG |  |  |  | UV_SETTINGS_DISPLAY_BOUNDARIES_NONE; UV_SETTINGS_DISPLAY_BOUNDARIES_SEAMS; UV_SETTINGS_DISPLAY_BOUNDARIES_CONNECTIVITY
UV Mesh | UV_SETTINGS_DISPLAY_UVMESH | BOOL |  |  |  | 
Shading | UV_SETTINGS_DISPLAY_SHADING | LONG |  |  |  | UV_SETTINGS_DISPLAY_SHADING_LINES; UV_SETTINGS_DISPLAY_SHADING_OVERLAPPING_POLYGONS; UV_SETTINGS_DISPLAY_SHADING_FILLED_POLYGONS; UV_SETTINGS_DISPLAY_SHADING_MULTI_COLOR_ISLANDS; UV_SETTINGS_DISPLAY_SHADING_DISTORTION; UV_SETTINGS_DISPLAY_SHADING_POLYGONS_CROSSING_TILES; UV_SETTINGS_DISPLAY_SHADING_TEXEL_DENSITY
Opacity | UV_SETTINGS_DISPLAY_OPACITY | REAL | 0.0 | 100.0 |  | 
Resolution | UV_SETTINGS_DISPLAY_TEXEL_DENSITY_RESOLUTION | LONG | 1 |  |  | 
Target TD | UV_SETTINGS_DISPLAY_TEXEL_DENSITY_TARGET | REAL | 0.0 |  |  | 
HUD | UV_SETTINGS_FILTER_UV_HUD | BOOL |  |  |  | 
Canvas Axis | UV_SETTINGS_FILTER_UV_RULERS | BOOL |  |  |  | 
Editor Axis | UV_SETTINGS_FILTER_UV_AXIS | BOOL |  |  |  | 
UV Units | UV_SETTINGS_FILTER_UV_UNITS | BOOL |  |  |  | 
UV Component Highlighting | UV_SETTINGS_FILTER_UV_COMPONENTS | BOOL |  |  |  | 
Show UV Grid | UV_SETTINGS_FILTER_SHOW_GRID | BOOL |  |  |  | 
Subdivisions U | UV_SETTINGS_FILTER_GRID_SUBDIVS_U | REAL | 1.0 | 128.0 |  | 
Subdivisions V | UV_SETTINGS_FILTER_GRID_SUBDIVS_V | REAL | 1.0 | 128.0 |  | 
Show Subgrid | UV_SETTINGS_FILTER_SHOW_SUBGRID | BOOL |  |  |  | 
Show Tile Coordinates | UV_SETTINGS_FILTER_SHOW_UDIM_INDEX | BOOL |  |  |  | 
Texture | UV_SETTINGS_BACK_TEXTURE | LONG |  |  |  | UV_SETTINGS_BACK_TEXTURE_EMPTY; UV_SETTINGS_BACK_TEXTURE_UVMAP; UV_SETTINGS_BACK_TEXTURE_LOAD_TEXTURE; UV_SETTINGS_BACK_TEXTURE_CREATE_TEXTURE
Opacity | UV_SETTINGS_BACK_OPACITY | REAL | 0.0 | 100.0 |  | 
