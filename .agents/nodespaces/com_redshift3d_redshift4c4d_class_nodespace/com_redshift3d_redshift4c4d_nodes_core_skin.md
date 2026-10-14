# Node Template: Skin

- **Node Space ID:** `com.redshift3d.redshift4c4d.class.nodespace`
- **Template ID:** `com.redshift3d.redshift4c4d.nodes.core.skin`
- **Template Name:** `Skin`

## Attributes

See `.agents/nodes.md` for an overview of Nodes API skills. Not all attributes and ports have a min, max, or default value. Enum values are listed in the form label = value, labe = value, label = value. I.e., if a user asks you to set the an enum attribute or port to "Foo" (citing an UI label), you must search for the label "Foo" in the enum values and use the corresponding value in your code. If a user asks you to set an attribute or port to a value that is not listed in the enum values, you must respond with an error message.

Name | ID  | Data Type | Parameter Type | isVariadic | isNested | isEnum | Min Value | Max Value | Default Value | Enum Values
---- | --- | --------- | -------------- | ---------- | -------- | ------ | --------- | --------- | ------------- | -----------
Basic/Asset Version | net.maxon.node.base.assetversion | maxon::Id | Attribute | false | false | true |  |  |  | Latest = latest
Basic/Color | net.maxon.node.base.color | maxon::Color | Attribute | false | false | false |  |  |  | 
Basic/Comment | net.maxon.node.base.comment | maxon::String | Attribute | false | false | false |  |  |  | 
Basic/Display Comment | net.maxon.node.base.displaycomment | maxon::Bool | Attribute | false | false | false |  |  |  | 
Basic/Name | net.maxon.node.base.name | maxon::String | Attribute | false | false | false |  |  |  | 
Basic/Ports Display | net.maxon.node.base.portdisplay | maxon::Id | Attribute | false | false | true |  |  | all | Collapsed = none, Connected = connected, Expanded = all
Basic/Show Preview | net.maxon.node.base.displaypreview | maxon::Bool | Attribute | false | false | false |  |  | true | 
Filter Tags | net.maxon.node.base.filtertags | maxon::CString | Attribute | false | false | false |  |  |  | 
Node Category | net.maxon.node.base.category | maxon::InternedId | Attribute | false | false | true |  |  | primitives | distributions = distributions, operators = operators, geometries = geometries, patterns = patterns, primitives = primitives, effectors = effectors, fields = fields, functions = functions, structures = structures, geomodifiers = geomodifiers, geogenerators = geogenerators
Preview/Node | net.maxon.node.base.nodepreviewimage | maxon::ImageBaseRef | Attribute | false | false | false |  |  |  | 
Bump Mapping/Add Bump Input To Material Bump | <com.redshift3d.redshift4c4d.nodes.core.skin.additional_bump_mode | maxon::Bool | Input | false | false | false |  |  | false | 
Bump Mapping/Bump Map | <com.redshift3d.redshift4c4d.nodes.core.skin.bump_input | maxon::Vector64 | Input | false | false | false |  |  |  | 
Bump Mapping/Coat_isGlossiness | <com.redshift3d.redshift4c4d.nodes.core.skin.coat_isglossiness | maxon::Bool | Input | false | false | false |  |  | true | 
Bump Mapping/Refl_isGlossiness | <com.redshift3d.redshift4c4d.nodes.core.skin.refl_isglossiness | maxon::Bool | Input | false | false | false |  |  | true | 
Bump Mapping/Refr_isGlossiness | <com.redshift3d.redshift4c4d.nodes.core.skin.refr_isglossiness | maxon::Bool | Input | false | false | false |  |  | true | 
Bump Mapping/ShaderCompatibility | <com.redshift3d.redshift4c4d.nodes.core.skin.shadercompatibility | maxon::Int | Input | false | false | false |  |  | 2 | 
Reflections/General/Disable Reflection Bump Mapping | <com.redshift3d.redshift4c4d.nodes.core.skin.no_refl_bump | maxon::Bool | Input | false | false | false |  |  | false | 
Reflections/Optimization/Cut-off Override/Enable | <com.redshift3d.redshift4c4d.nodes.core.skin.refl_enablecutoff | maxon::Bool | Input | false | false | false |  |  | false | 
Reflections/Optimization/Cut-off Override/Threshold | <com.redshift3d.redshift4c4d.nodes.core.skin.refl_cutoff | maxon::Float | Input | false | false | false | 0 | 1 | 0.01 | 
Reflections/Optimization/Enable Trace Depth Overrides | <com.redshift3d.redshift4c4d.nodes.core.skin.depth_override | maxon::Bool | Input | false | false | false |  |  | false | 
Reflections/Optimization/Max Trace Depth | <com.redshift3d.redshift4c4d.nodes.core.skin.refl_depth | maxon::Int | Input | false | false | false | 0 | 63 | 3 | 
Reflections/Optimization/Specular Highlights Only | <com.redshift3d.redshift4c4d.nodes.core.skin.refl_hl_only | maxon::Bool | Input | false | false | false |  |  | false | 
Reflections/Primary Reflection/BRDF | <com.redshift3d.redshift4c4d.nodes.core.skin.refl_brdf0 | maxon::Int | Input | false | false | true |  |  | 0 | Beckmann (Cook-Torrance) = 0, GGX = 1, Ashikhmin-Shirley = 2
Reflections/Primary Reflection/Color | <com.redshift3d.redshift4c4d.nodes.core.skin.refl_color0 | maxon::Color64 | Input | false | false | false |  |  | (1,1,1) | 
Reflections/Primary Reflection/Glossiness | <com.redshift3d.redshift4c4d.nodes.core.skin.refl_gloss0 | maxon::Float | Input | false | false | false | 0 | 1 | 0.35 | 
Reflections/Primary Reflection/IOR | <com.redshift3d.redshift4c4d.nodes.core.skin.refl_ior0 | maxon::Float | Input | false | false | false | 0 | 32 | 1.44 | 
Reflections/Primary Reflection/Samples | <com.redshift3d.redshift4c4d.nodes.core.skin.refl_gloss_samples0 | maxon::Int | Input | false | false | false | 0 | 65535 | 32 | 
Reflections/Primary Reflection/Weight | <com.redshift3d.redshift4c4d.nodes.core.skin.refl_weight0 | maxon::Float | Input | false | false | false | 0 | 1 | 0.2 | 
Reflections/Secondary Reflection/BRDF | <com.redshift3d.redshift4c4d.nodes.core.skin.refl_brdf1 | maxon::Int | Input | false | false | true |  |  | 0 | Beckmann (Cook-Torrance) = 0, GGX = 1, Ashikhmin-Shirley = 2
Reflections/Secondary Reflection/Color | <com.redshift3d.redshift4c4d.nodes.core.skin.refl_color1 | maxon::Color64 | Input | false | false | false |  |  | (1,1,1) | 
Reflections/Secondary Reflection/Glossiness | <com.redshift3d.redshift4c4d.nodes.core.skin.refl_gloss1 | maxon::Float | Input | false | false | false | 0 | 1 | 0.7 | 
Reflections/Secondary Reflection/IOR | <com.redshift3d.redshift4c4d.nodes.core.skin.refl_ior1 | maxon::Float | Input | false | false | false | 0 | 32 | 1.44 | 
Reflections/Secondary Reflection/Samples | <com.redshift3d.redshift4c4d.nodes.core.skin.refl_gloss_samples1 | maxon::Int | Input | false | false | false | 0 | 65535 | 16 | 
Reflections/Secondary Reflection/Weight | <com.redshift3d.redshift4c4d.nodes.core.skin.refl_weight1 | maxon::Float | Input | false | false | false | 0 | 1 | 0 | 
Scattering Layers/Common/Diffuse Amount | <com.redshift3d.redshift4c4d.nodes.core.skin.diffuse_amount | maxon::Float | Input | false | false | false | 0 | 1 | 0 | 
Scattering Layers/Common/Disable Diffuse Bump Mapping | <com.redshift3d.redshift4c4d.nodes.core.skin.no_diffuse_bump | maxon::Bool | Input | false | false | false |  |  | false | 
Scattering Layers/Common/Include Mode | <com.redshift3d.redshift4c4d.nodes.core.skin.include_mode | maxon::Int | Input | false | false | true |  |  | 1 | All Objects = 0, Only Self = 1
Scattering Layers/Common/Mode | <com.redshift3d.redshift4c4d.nodes.core.skin.mode | maxon::Int | Input | false | false | true |  |  | 1 | Point-Based (legacy) = 65536, Ray-Traced = 1, Point-Based = 0
Scattering Layers/Common/Normalize Diffuse Weights | <com.redshift3d.redshift4c4d.nodes.core.skin.normalize_weights | maxon::Bool | Input | false | false | false |  |  | true | 
Scattering Layers/Common/Overall Scale | <com.redshift3d.redshift4c4d.nodes.core.skin.overall_scale | maxon::Float | Input | false | false | false | 0 | 100 | 1 | 
Scattering Layers/Common/Radius Scale | <com.redshift3d.redshift4c4d.nodes.core.skin.radius_scale | maxon::Float | Input | false | false | false | 0 | 100000 | 100 | 
Scattering Layers/Common/Samples | <com.redshift3d.redshift4c4d.nodes.core.skin.samples | maxon::Int | Input | false | false | false | 1 | 65535 | 64 | 
Scattering Layers/Deep Scatter/Color | <com.redshift3d.redshift4c4d.nodes.core.skin.deep_color | maxon::Color64 | Input | false | false | false |  |  | (0.7,0.1,0.1) | 
Scattering Layers/Deep Scatter/Radius (cm) | <com.redshift3d.redshift4c4d.nodes.core.skin.deep_radius | maxon::Float | Input | false | false | false |  |  | 0.15 | 
Scattering Layers/Deep Scatter/Weight | <com.redshift3d.redshift4c4d.nodes.core.skin.deep_weight | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Scattering Layers/Mid Scatter/Color | <com.redshift3d.redshift4c4d.nodes.core.skin.mid_color | maxon::Color64 | Input | false | false | false |  |  | (0.95,0.7,0.5) | 
Scattering Layers/Mid Scatter/Radius (cm) | <com.redshift3d.redshift4c4d.nodes.core.skin.mid_radius | maxon::Float | Input | false | false | false |  |  | 0.062 | 
Scattering Layers/Mid Scatter/Weight | <com.redshift3d.redshift4c4d.nodes.core.skin.mid_weight | maxon::Float | Input | false | false | false | 0 | 1 | 0.25 | 
Scattering Layers/Shallow Scatter/Color | <com.redshift3d.redshift4c4d.nodes.core.skin.shallow_color | maxon::Color64 | Input | false | false | false |  |  | (1,0.9,0.7) | 
Scattering Layers/Shallow Scatter/Radius (cm) | <com.redshift3d.redshift4c4d.nodes.core.skin.shallow_radius | maxon::Float | Input | false | false | false |  |  | 0.038 | 
Scattering Layers/Shallow Scatter/Weight | <com.redshift3d.redshift4c4d.nodes.core.skin.shallow_weight | maxon::Float | Input | false | false | false | 0 | 1 | 0.6 | 
Scattering Layers/Single Scattering/Phase | <com.redshift3d.redshift4c4d.nodes.core.skin.ss_phase | maxon::Float | Input | false | false | false | -1 | 1 | 0 | 
Scattering Layers/Single Scattering/Samples | <com.redshift3d.redshift4c4d.nodes.core.skin.ss_samples | maxon::Int | Input | false | false | false | 1 | 65535 | 16 | 
Scattering Layers/Single Scattering/Scatter Amount | <com.redshift3d.redshift4c4d.nodes.core.skin.ss_amount | maxon::Float | Input | false | false | false | 0 | 65535 | 0 | 
Scattering Layers/Single Scattering/Thickness (cm) | <com.redshift3d.redshift4c4d.nodes.core.skin.ss_thickness | maxon::Float | Input | false | false | false | 0 | 100000000 | 0.01 | 
Scattering Layers/Single Scattering/Transmittance | <com.redshift3d.redshift4c4d.nodes.core.skin.ss_transmittance | maxon::Color64 | Input | false | false | false |  |  | (1,1,1) | 
Outputs/outColor | >com.redshift3d.redshift4c4d.nodes.core.skin.outcolor | maxon::Color64 | Output | false | false | false |  |  | (0,0,0) | 

