# Description: Multi-Pass

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/c4d_base/description/zmultipass.res`
- **Symbol:** `Zmultipass`
- **Category:** Other

Use parameter symbols to access parameters and cycle option symbols for cycle values, never their numeric IDs. Treat Min and Max as constraints and Default as the declared initial value; blank cells mean the resource does not declare that metadata, not that the value is zero. Base Description Parameters lists inherited fields from each base; All Parameters lists the effective parameter set for this description.

## Base Description Parameters

No base descriptions.

## All Parameters

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Group ID | MULTIPASSOBJECT_OBJECTBUFFER | LONG | 1 |  |  | 
AOV ID | MULTIPASSOBJECT_AOVBUFFER | LONG | 1 |  |  | 
Ambient | MULTIPASSOBJECT_AMBIENT | BOOL |  |  |  | 
Diffuse | MULTIPASSOBJECT_DIFFUSE | BOOL |  |  |  | 
Specular | MULTIPASSOBJECT_SPECULAR | BOOL |  |  |  | 
Shadow | MULTIPASSOBJECT_SHADOW | BOOL |  |  |  | 
Reflection | MULTIPASSOBJECT_REFLECTION | BOOL |  |  |  | 
Refraction | MULTIPASSOBJECT_TRANSPARENCY | BOOL |  |  |  | 
Global Illumination | MULTIPASSOBJECT_RADIOSITY | BOOL |  |  |  | 
Caustics | MULTIPASSOBJECT_CAUSTICS | BOOL |  |  |  | 
Atmosphere | MULTIPASSOBJECT_ATMOSPHERE | BOOL |  |  |  | 
Atmosphere (Multiply) | MULTIPASSOBJECT_ATMOSPHERE_MUL | BOOL |  |  |  | 
Post Effects | MULTIPASSOBJECT_ALLPOSTEFFECTS | BOOL |  |  |  | 
Separate Materials | MULTIPASSOBJECT_REFLECTION_MATERIALS | LONG |  |  |  | MULTIPASSOBJECT_REFLECTION_SEPARATE_NONE; MULTIPASSOBJECT_REFLECTION_SEPARATE_ALL; MULTIPASSOBJECT_REFLECTION_SEPARATE_SELECTED
Separate Layers | MULTIPASSOBJECT_REFLECTION_LAYERS | LONG |  |  |  | MULTIPASSOBJECT_REFLECTION_LAYERS_NONE; MULTIPASSOBJECT_REFLECTION_LAYERS_ALL; MULTIPASSOBJECT_REFLECTION_LAYERS_SELECTED
Mode | MULTIPASSOBJECT_REFLECTION_MODE | LONG |  |  |  | MULTIPASSOBJECT_REFLECTION_MODE_NORMAL; MULTIPASSOBJECT_REFLECTION_MODE_RAW; MULTIPASSOBJECT_REFLECTION_MODE_COMBINED
Separate Materials | MULTIPASSOBJECT_SPECULAR_MATERIALS | LONG |  |  |  | MULTIPASSOBJECT_SPECULAR_SEPARATE_NONE; MULTIPASSOBJECT_SPECULAR_SEPARATE_ALL; MULTIPASSOBJECT_SPECULAR_SEPARATE_SELECTED
Separate Layers | MULTIPASSOBJECT_SPECULAR_LAYERS | LONG |  |  |  | MULTIPASSOBJECT_SPECULAR_LAYERS_NONE; MULTIPASSOBJECT_SPECULAR_LAYERS_ALL; MULTIPASSOBJECT_SPECULAR_LAYERS_SELECTED
Mode | MULTIPASSOBJECT_SPECULAR_MODE | LONG |  |  |  | MULTIPASSOBJECT_SPECULAR_MODE_NORMAL; MULTIPASSOBJECT_SPECULAR_MODE_RAW; MULTIPASSOBJECT_SPECULAR_MODE_COMBINED
