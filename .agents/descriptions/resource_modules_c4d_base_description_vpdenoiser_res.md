# Description: Denoiser

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/c4d_base/description/vpdenoiser.res`
- **Symbol:** `VPdenoiser`
- **Category:** Video Posts

Use parameter symbols to access parameters and cycle option symbols for cycle values, never their numeric IDs. Treat Min and Max as constraints and Default as the declared initial value; blank cells mean the resource does not declare that metadata, not that the value is zero. Base Description Parameters lists inherited fields from each base; All Parameters lists the effective parameter set for this description.

## Base Description Parameters

### Post Effect (`VPbase`)

No parameters.

## All Parameters

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Albedo Pass | VP_DENOISER_ALBEDO_TYPE | LONG |  |  |  | VP_DENOISER_ALBEDO_TYPE_ALBEDO; VP_DENOISER_ALBEDO_TYPE_MATERIAL_COLOR
Use Multi-Passes | VP_DENOISER_USE_PASSES | BOOL |  |  | 0 | 
Save the raw image on a separate layer | VP_DENOISER_ADDRAWLAYER | BOOL |  |  | 0 | 
To get the separate layer, add the Multi-Pass Layer 'Post Effects' to your render settings. | VP_DENOISER_ADDRAWLAYER_INFO | STATICTEXT |  |  |  | 
For best results, add the corresponding Albedo and the 'Material Normal' Multi-Passes. | VP_DENOISER_PASSES_INFO | STATICTEXT |  |  |  | 
