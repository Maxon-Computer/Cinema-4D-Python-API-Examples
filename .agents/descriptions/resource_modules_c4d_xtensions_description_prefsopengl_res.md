# Description: Viewport Hardware

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/c4d_xtensions/description/prefsopengl.res`
- **Symbol:** `Prefsopengl`
- **Category:** Other

Use parameter symbols to access parameters and cycle option symbols for cycle values, never their numeric IDs. Treat Min and Max as constraints and Default as the declared initial value; blank cells mean the resource does not declare that metadata, not that the value is zero. Base Description Parameters lists inherited fields from each base; All Parameters lists the effective parameter set for this description.

## Base Description Parameters

No base descriptions.

## All Parameters

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Anti-Aliasing | PREF_OPENGL_ANTIALIAS | LONG |  |  |  | 
UV Editor Anti-Aliasing | PREF_OPENGL_UVEDITOR_ANTIALIAS | BOOL |  |  |  | 
Transparency Max | PREF_OPENGL_MAXTRANS | LONG | 0 | 10 |  | 
Lights Max | PREF_OPENGL_MAXLIGHT | LONG | 1 | 1000 |  | 
Shadows Max | PREF_OPENGL_MAXSHAD | LONG | 0 | 100 |  | 
Shader Cache | PREF_OPENGL_USE_SHADER_CACHE | BOOL |  |  |  | 
Viewport Dithering | PREF_OPENGL_VIEWPORT_DITHERING | BOOL |  |  |  | 
HDR | PREF_VIEWPORT_ENABLE_HDR | BOOL |  |  |  | 
Texture | PREF_OPENGL_TEXTURE | SEPARATOR |  |  |  | 
Default Resolution | PREF_OPENGL_PREVIEWSIZE | LONG |  |  |  | PREF_OPENGL_PREVIEWSIZE_64; PREF_OPENGL_PREVIEWSIZE_128; PREF_OPENGL_PREVIEWSIZE_256; PREF_OPENGL_PREVIEWSIZE_512; PREF_OPENGL_PREVIEWSIZE_1024; PREF_OPENGL_PREVIEWSIZE_2048; PREF_OPENGL_PREVIEWSIZE_4096; PREF_OPENGL_PREVIEWSIZE_8192; PREF_OPENGL_PREVIEWSIZE_16384
Dome Light Resolution | PREF_OPENGL_SKY_PREVIEWSIZE | LONG |  |  |  | PREF_OPENGL_SKY_PREVIEWSIZE_64; PREF_OPENGL_SKY_PREVIEWSIZE_128; PREF_OPENGL_SKY_PREVIEWSIZE_256; PREF_OPENGL_SKY_PREVIEWSIZE_512; PREF_OPENGL_SKY_PREVIEWSIZE_1024; PREF_OPENGL_SKY_PREVIEWSIZE_2048; PREF_OPENGL_SKY_PREVIEWSIZE_4096; PREF_OPENGL_SKY_PREVIEWSIZE_8192; PREF_OPENGL_SKY_PREVIEWSIZE_16384
Interpolation | PREF_OPENGL_TEXTUREMODE | LONG |  |  |  | PREF_OPENGL_TEXTUREMODE_NEAREST; PREF_OPENGL_TEXTUREMODE_LINEAR; PREF_OPENGL_TEXTUREMODE_MIPMAP
Load Previous Settings | PREF_OPENGL_LOAD_PREVIOUS | BUTTON |  |  |  | 
Save Current Settings as Startup | PREF_OPENGL_SAVE_AS_STARTUP | BUTTON |  |  |  | 
Information | PREF_OPENGL_INFO | SEPARATOR |  |  |  | 
GPU | PREF_OPENGL_INFO_GPU | STATICTEXT |  |  |  | 
Framework | PREF_OPENGL_INFO_API | STATICTEXT |  |  |  | 
Version | PREF_OPENGL_INFO_VERSION | STATICTEXT |  |  |  | 
Shading Language | PREF_OPENGL_INFO_GLSL_VERSION | STATICTEXT |  |  |  | 
Notice | PREF_OPENGL_NOTICE | SEPARATOR |  |  |  | 
No label | PREF_OPENGL_WARNING | STRING |  |  |  | 
