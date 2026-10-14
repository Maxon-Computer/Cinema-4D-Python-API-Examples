# Description: Memory

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/c4d_xtensions/description/prefsmemory.res`
- **Symbol:** `Prefsmemory`
- **Category:** Other

Use parameter symbols to access parameters and cycle option symbols for cycle values, never their numeric IDs. Treat Min and Max as constraints and Default as the declared initial value; blank cells mean the resource does not declare that metadata, not that the value is zero. Base Description Parameters lists inherited fields from each base; All Parameters lists the effective parameter set for this description.

## Base Description Parameters

No base descriptions.

## All Parameters

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Project | PREFS_MEMORY_DOCGROUP | SEPARATOR |  |  |  | 
Undo Depth | PREF_MEMORY_UNDO | LONG | 1 | 10000 |  | 
Animated Materials (MB) | PREF_MEMORY_MATERIAL | LONG | 1 | 10000 |  | 
Renderer | PREFS_MEMORY_RENDGROUP | SEPARATOR |  |  |  | 
Displacement (MB) | PREF_MEMORY_RENDERER | LONG | 1 | 10000 |  | 
BodyPaint 3D | PREFS_MEMORY_BPGROUP | SEPARATOR |  |  |  | 
Texture Undo (MB) | PREF_MEMORY_BP | LONG | 1 | 10000 |  | 
Min Undo Steps | PREF_MEMORY_BPUNDO | LONG | 1 | 1000 |  | 
Picture Viewer | PREFS_MEMORY_PVGROUP | SEPARATOR |  |  |  | 
Memory (MB) | PREF_MEMORY_PVUSEAGE | LONG | 50 |  |  | 
Hard Drive (MB) | PREF_MEMORY_PVHARDUSAGE | LONG | 50 |  |  | 
Unlimited | PREF_MEMORY_PVHARDUNLIMIT | BOOL |  |  |  | 
Cache Path | PREF_MEMORY_PVHARDFOLDER | FILENAME |  |  |  | 
Sculpting | PREFS_MEMORY_SCULPTGROUP | SEPARATOR |  |  |  | 
Memory (MB) | PREF_MEMORY_SCULPTUSAGE | LONG | 1 |  |  | 
Motion Tracker | PREFS_MEMORY_PHGROUP | SEPARATOR |  |  |  | 
Max Footage Cache (MB) | PREF_MEMORY_PHFOOTAGEMAXCACHEMB | LONG | 10 |  |  | 
Min System Reserve (MB) | PREF_MEMORY_PHFOOTAGESYSRESERVEMB | LONG | 10 |  |  | 
