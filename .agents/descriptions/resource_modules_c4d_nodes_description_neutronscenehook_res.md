# Description: Nodes

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/c4d_nodes/description/neutronscenehook.res`
- **Symbol:** `NeutronSceneHook`
- **Category:** Other

Use parameter symbols to access parameters and cycle option symbols for cycle values, never their numeric IDs. Treat Min and Max as constraints and Default as the declared initial value; blank cells mean the resource does not declare that metadata, not that the value is zero. Base Description Parameters lists inherited fields from each base; All Parameters lists the effective parameter set for this description.

## Base Description Parameters

No base descriptions.

## All Parameters

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Scene Nodes | NEUTRON_SEPARATOR | SEPARATOR |  |  |  | 
Display | NEUTRON_VIEWPORT_MODE | LONG |  |  |  | NEUTRON_VIEWPORT_MODE_NONE; NEUTRON_VIEWPORT_MODE_NEUTRON; NEUTRON_VIEWPORT_MODE_LEGACY
Render Only | NEUTRON_RENDER_ONLY | BOOL |  |  |  | 
Material Nodes | CONVERT_BXDF_TO_COLORCHANNEL_SEPARATOR | SEPARATOR |  |  |  | 
Use Color Channel | CONVERT_BXDF_TO_COLORCHANNEL | BOOL |  |  |  | 
