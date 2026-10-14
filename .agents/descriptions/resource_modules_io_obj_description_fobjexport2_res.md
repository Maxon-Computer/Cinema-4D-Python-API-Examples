# Description: OBJ Export Settings

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/io_obj/description/fobjexport2.res`
- **Symbol:** `fobjexport2`
- **Category:** Files

Use parameter symbols to access parameters and cycle option symbols for cycle values, never their numeric IDs. Treat Min and Max as constraints and Default as the declared initial value; blank cells mean the resource does not declare that metadata, not that the value is zero. Base Description Parameters lists inherited fields from each base; All Parameters lists the effective parameter set for this description.

## Base Description Parameters

### Filter (`Fbase`)

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Presets | PRESET_OPTIONS_PRESETS | LONG |  |  | 0 | 
Save... | PRESET_OPTIONS_PRESETS_CUSTOM_SAVEBUTTON | BUTTON |  |  |  | 
Delete... | PRESET_OPTIONS_PRESETS_CUSTOM_DELETEBUTTON | BUTTON |  |  |  | 

## All Parameters

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Presets | PRESET_OPTIONS_PRESETS | LONG |  |  | 0 | 
Save... | PRESET_OPTIONS_PRESETS_CUSTOM_SAVEBUTTON | BUTTON |  |  |  | 
Delete... | PRESET_OPTIONS_PRESETS_CUSTOM_DELETEBUTTON | BUTTON |  |  |  | 
Scale | OBJEXPORTOPTIONS_SCALE | UNITSCALE |  |  |  | 
UVs | OBJEXPORTOPTIONS_EXPORT_UVS | LONG |  |  | OBJEXPORTOPTIONS_UV_ORIGINAL | OBJEXPORTOPTIONS_UV_NONE; OBJEXPORTOPTIONS_UV_ORIGINAL; OBJEXPORTOPTIONS_FLIP_U; OBJEXPORTOPTIONS_FLIP_V; OBJEXPORTOPTIONS_FLIP_UV
Normals | OBJEXPORTOPTIONS_NORMALS | LONG |  |  | OBJEXPORTOPTIONS_NORMALS_VERTEX | OBJEXPORTOPTIONS_NORMALS_NONE; OBJEXPORTOPTIONS_NORMALS_VERTEX
Vertex Colors | OBJEXPORTOPTIONS_VERTEX_COLOR | BOOL |  |  | 0 | 
Flip X Axis | OBJEXPORTOPTIONS_POINTTRANSFORM_FLIPX | BOOL |  |  | 0 | 
Swap X and Y Axes | OBJEXPORTOPTIONS_POINTTRANSFORM_SWAPXY | BOOL |  |  | 0 | 
Flip Y Axis | OBJEXPORTOPTIONS_POINTTRANSFORM_FLIPY | BOOL |  |  | 0 | 
Swap X and Z Axes | OBJEXPORTOPTIONS_POINTTRANSFORM_SWAPXZ | BOOL |  |  | 0 | 
Flip Z Axis | OBJEXPORTOPTIONS_POINTTRANSFORM_FLIPZ | BOOL |  |  | 1 | 
Swap Y and Z Axes | OBJEXPORTOPTIONS_POINTTRANSFORM_SWAPYZ | BOOL |  |  | 0 | 
Flip Faces | OBJEXPORTOPTIONS_FLIPFACES | BOOL |  |  | 0 | 
Resolve N-gons | OBJEXPORTOPTIONS_TRIANGULATE_NGONS | BOOL |  |  | 0 | 
Objects as Groups | OBJEXPORTOPTIONS_OBJECTS_AS_GROUPS | BOOL |  |  | 0 | 
Material | OBJEXPORTOPTIONS_MATERIAL | LONG |  |  | OBJEXPORTOPTIONS_MATERIAL_CONSOLIDATE | OBJEXPORTOPTIONS_MATERIAL_NONE; OBJEXPORTOPTIONS_MATERIAL_NAMEANDDEFAULT; OBJEXPORTOPTIONS_MATERIAL_ORIGINAL_PATHS; OBJEXPORTOPTIONS_MATERIAL_CONSOLIDATE
Default Material | OBJEXPORTOPTIONS_DEFAULTMATERIAL | LONG |  |  | OBJEXPORTOPTIONS_DEFAULTMATERIAL_WHITE | OBJEXPORTOPTIONS_DEFAULTMATERIAL_WHITE; OBJEXPORTOPTIONS_DEFAULTMATERIAL_RANDOMCOLORS
Invert Transparency | OBJEXPORTOPTIONS_INVERT_TRANSPARENCY | BOOL |  |  | 0 | 
Frame Range | OBJEXPORTOPTIONS_ANIMATION_TYPE | LONG |  |  | OBJEXPORTOPTIONS_NO_ANIMATION | OBJEXPORTOPTIONS_NO_ANIMATION; OBJEXPORTOPTIONS_MANUAL_RANGE; OBJEXPORTOPTIONS_LOOP_FRAMES; OBJEXPORTOPTIONS_PREVIEW_FRAMES; OBJEXPORTOPTIONS_ALL_ANIMATED_FRAMES
Start Frame | OBJEXPORTOPTIONS_FRAME_START | LONG | 0 | 3240000 |  | 
End Frame | OBJEXPORTOPTIONS_FRAME_END | LONG | 0 | 3240000 |  | 
Frame Step | OBJEXPORTOPTIONS_FRAME_STEP | LONG | 1 |  | 1 | 
Shared Material File | OBJEXPORTOPTIONS_SHARED_MTL_FILE | BOOL |  |  | 0 | 
Export as UTF-8 | OBJEXPORTOPTIONS_ENCODING_UTF8 | BOOL |  |  | 0 | 
