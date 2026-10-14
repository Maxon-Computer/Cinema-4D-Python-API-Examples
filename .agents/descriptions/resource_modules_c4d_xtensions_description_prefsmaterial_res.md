# Description: Material

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/c4d_xtensions/description/prefsmaterial.res`
- **Symbol:** `Prefsmaterial`
- **Category:** Other

Use parameter symbols to access parameters and cycle option symbols for cycle values, never their numeric IDs. Treat Min and Max as constraints and Default as the declared initial value; blank cells mean the resource does not declare that metadata, not that the value is zero. Base Description Parameters lists inherited fields from each base; All Parameters lists the effective parameter set for this description.

## Base Description Parameters

No base descriptions.

## All Parameters

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Default Size | PREF_MM_SIZE | LONG |  |  |  | PREF_MM_SIZE_SMALL; PREF_MM_SIZE_MED; PREF_MM_SIZE_LARGE; PREF_MM_SIZE_HUGE
Shader Default Project | PREF_MM_SHSCENE | LONG |  |  |  | 
Material Default Project | PREF_MM_MATSCENE | LONG |  |  |  | 
Frame Rate (FPS) | PREF_MM_FRATE | LONG | 1 | 100 |  | 
Preview Length (sec) | PREF_MM_PREV | LONG | 0 |  |  | 
Node Preview Size | PREF_MM_NODE_PREVIEW_SIZE | LONG |  |  |  | PREF_MM_NODE_PREVIEW_SIZE_SMALL; PREF_MM_NODE_PREVIEW_SIZE_MED; PREF_MM_NODE_PREVIEW_SIZE_LARGE; PREF_MM_NODE_PREVIEW_SIZE_HUGE
3D Preview Scene | PREF_MM_NODE_MAT_PREVIEW_SCENE | LONG |  |  |  | 
Default Material | PREF_MM_DEFAULT_MATERIAL | LONG |  |  |  | 
Always Open Node Editor | PREF_MM_ALWAYS_OPEN_NODE_EDITOR | BOOL |  |  |  | 
