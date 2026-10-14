# Description: Sound Operator

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/xpressocore/description/gvsound.res`
- **Symbol:** `GVsound`
- **Category:** Graph View

Use parameter symbols to access parameters and cycle option symbols for cycle values, never their numeric IDs. Treat Min and Max as constraints and Default as the declared initial value; blank cells mean the resource does not declare that metadata, not that the value is zero. Base Description Parameters lists inherited fields from each base; All Parameters lists the effective parameter set for this description.

## Base Description Parameters

### Node (`GVbase`)

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Enabled | ID_GVBASE_ENABLE | BOOL |  |  |  | 
Title Color | ID_GVBASE_COLOR | COLOR |  |  |  | 
Remark | ID_GVBASE_REMARK | STRING |  |  |  | 

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
Enabled | ID_GVBASE_ENABLE | BOOL |  |  |  | 
Title Color | ID_GVBASE_COLOR | COLOR |  |  |  | 
Remark | ID_GVBASE_REMARK | STRING |  |  |  | 
Filename | GV_SOUND_FILENAME | FILENAME |  |  |  | 
Probe | GV_SOUND_PROBE | LONG | 0 | 1024 |  | 
Play | GV_SOUND_PLAY | BOOL |  |  |  | 
Time | GV_SOUND_TIME | BASETIME |  |  |  | 
Sample | GV_SOUND_SAMPLE | LONG |  |  |  | 
Left | GV_SOUND_OUTPUT_LEFT | LONG |  |  |  | 
Right | GV_SOUND_OUTPUT_RIGHT | LONG |  |  |  | 
Length | GV_SOUND_LENGTH | BASETIME |  |  |  | 
Samples | GV_SOUND_SAMPLES | LONG |  |  |  | 
Bands | GV_SOUND_FFT_RES | LONG |  |  |  | GV_SOUND_FFT_RES_4; GV_SOUND_FFT_RES_8; GV_SOUND_FFT_RES_16; GV_SOUND_FFT_RES_32; GV_SOUND_FFT_RES_64; GV_SOUND_FFT_RES_128; GV_SOUND_FFT_RES_256; GV_SOUND_FFT_RES_512; GV_SOUND_FFT_RES_1024; GV_SOUND_FFT_RES_2048; GV_SOUND_FFT_RES_4096; GV_SOUND_FFT_RES_8192
Band | GV_SOUND_FFT_BIN | LONG |  |  |  | 
Left Mag | GV_SOUND_FFT_BIN_LEFT | REAL |  |  |  | 
Right Mag | GV_SOUND_FFT_BIN_RIGHT | REAL |  |  |  | 
