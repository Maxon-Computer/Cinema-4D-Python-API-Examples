# Description: Ambient Occlusion

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/advanced_render/description/vpambientocclusion.res`
- **Symbol:** `VPambientocclusion`
- **Category:** Video Posts

Use parameter symbols to access parameters and cycle option symbols for cycle values, never their numeric IDs. Treat Min and Max as constraints and Default as the declared initial value; blank cells mean the resource does not declare that metadata, not that the value is zero. Base Description Parameters lists inherited fields from each base; All Parameters lists the effective parameter set for this description.

## Base Description Parameters

### Post Effect (`VPbase`)

No parameters.

## All Parameters

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Apply to Project | VPAMBIENTOCCLUSION_APPLYTOSCENE | BOOL |  |  |  | 
Color | VPAMBIENTOCCLUSION_GRADIENT | GRADIENT |  |  |  | 
Minimum Ray Length | VPAMBIENTOCCLUSION_MINLENGTH | REAL | 0.0 |  |  | 
Maximum Ray Length | VPAMBIENTOCCLUSION_MAXLENGTH | REAL | 0.0 |  |  | 
Dispersion | VPAMBIENTOCCLUSION_DISPERSION | REAL | 0.0 | 100.0 |  | 
Accuracy | VPAMBIENTOCCLUSION_ACCURACY | REAL | 0.0 | 100.0 |  | 
Minimum Samples | VPAMBIENTOCCLUSION_MINSAMPLES | LONG | 1 | 10000 |  | 
Maximum Samples | VPAMBIENTOCCLUSION_MAXSAMPLES | LONG | 1 | 10000 |  | 
Contrast | VPAMBIENTOCCLUSION_CONTRAST | REAL | -100.0 | 100.0 |  | 
Use Sky Environment | VPAMBIENTOCCLUSION_ENVIRONMENT | BOOL |  |  |  | 
Evaluate Transparency | VPAMBIENTOCCLUSION_TRANSPARENCY | BOOL |  |  |  | 
Self Shadowing Only | VPAMBIENTOCCLUSION_SELFTEST | BOOL |  |  |  | 
Invert Direction | VPAMBIENTOCCLUSION_REVERSE | BOOL |  |  |  | 
Enable Cache | VPAMBIENTOCCLUSION_CACHE_ENABLE | BOOL |  |  |  | 
Samples | VPAMBIENTOCCLUSION_CACHE_SAMPLES | LONG | 16 | 16384 |  | 
Record Density | VPAMBIENTOCCLUSION_CACHE_QUALITY | LONG |  |  |  | VPAMBIENTOCCLUSION_CACHE_QUALITY_CUSTOM; VPAMBIENTOCCLUSION_CACHE_QUALITY_PREVIEW; VPAMBIENTOCCLUSION_CACHE_QUALITY_LOW; VPAMBIENTOCCLUSION_CACHE_QUALITY_MEDIUM; VPAMBIENTOCCLUSION_CACHE_QUALITY_HIGH
Min Rate | VPAMBIENTOCCLUSION_CACHE_RATE_MIN | LONG | -8 | 4 |  | 
Max Rate | VPAMBIENTOCCLUSION_CACHE_RATE_MAX | LONG | -8 | 4 |  | 
Density | VPAMBIENTOCCLUSION_CACHE_DENSITY | REAL | 10.0 | 1000.0 |  | 
Minimum Spacing | VPAMBIENTOCCLUSION_CACHE_DETAILS | REAL | 0.0 | 1000.0 |  | 
Maximum Spacing | VPAMBIENTOCCLUSION_CACHE_MAX_LIMIT | REAL | 0.0 | 1000.0 |  | 
Smoothing | VPAMBIENTOCCLUSION_CACHE_SMOOTHING | REAL | 0.0 | 1000.0 |  | 
Screen Scale | VPAMBIENTOCCLUSION_CACHE_SCALE | BOOL |  |  |  | 
Flush Cache(s) | VPAMBIENTOCCLUSION_CACHE_FILE_FLUSH | BUTTON |  |  |  | 
No label | VPAMBIENTOCCLUSION_CACHE_FILE_SIZE | STATICTEXT |  |  |  | 
Skip Prepass (If Present) | VPAMBIENTOCCLUSION_CACHE_FILE_LOCK | BOOL |  |  |  | 
Auto Load | VPAMBIENTOCCLUSION_CACHE_FILE_AUTOLOAD | BOOL |  |  |  | 
Auto Save | VPAMBIENTOCCLUSION_CACHE_FILE_AUTOSAVE | BOOL |  |  |  | 
Full Animation Mode | VPAMBIENTOCCLUSION_CACHE_FILE_ANIMATION | BOOL |  |  |  | 
Custom Location | VPAMBIENTOCCLUSION_CACHE_FILE_PATH_ENABLED | BOOL |  |  |  | 
Location | VPAMBIENTOCCLUSION_CACHE_FILE_PATH | FILENAME |  |  |  | 
