# Node Template: Material

- **Node Space ID:** `com.redshift3d.redshift4c4d.class.nodespace`
- **Template ID:** `com.redshift3d.redshift4c4d.nodes.core.material`
- **Template Name:** `Material`

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
Node Category | net.maxon.node.base.category | maxon::InternedId | Attribute | false | false | true |  |  | primitives | operators = operators, distributions = distributions, geometries = geometries, patterns = patterns, primitives = primitives, effectors = effectors, fields = fields, functions = functions, structures = structures, geomodifiers = geomodifiers, geogenerators = geogenerators
Preview/Node | net.maxon.node.base.nodepreviewimage | maxon::ImageBaseRef | Attribute | false | false | false |  |  |  | 
Advanced/'Overall Tint' Affects Emission | <com.redshift3d.redshift4c4d.nodes.core.material.overallaffectsemission | maxon::Bool | Input | false | false | false |  |  | false | 
Advanced/Anisotropy/Surface Orientation | <com.redshift3d.redshift4c4d.nodes.core.material.anisotropy_orientation | maxon::Int | Input | false | false | true |  |  | 2 | None = 2, From Tangent Channel = 1
Advanced/Anisotropy/Tangent Channel | <com.redshift3d.redshift4c4d.nodes.core.material.anisotropy_tangentchannel | maxon::String | Input | false | false | false |  |  |  | 
Advanced/Anisotropy/UV Channel | <com.redshift3d.redshift4c4d.nodes.core.material.anisotropy_uvchannel | maxon::String | Input | false | false | false |  |  |  | 
Advanced/Coating/Convert From Glossiness to Roughness | <com.redshift3d.redshift4c4d.nodes.core.material.coat_isglossiness | maxon::Bool | Input | false | false | false |  |  | false | 
Advanced/Coating/Direct Scale | <com.redshift3d.redshift4c4d.nodes.core.material.coat_direct | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Advanced/Coating/Indirect Scale | <com.redshift3d.redshift4c4d.nodes.core.material.coat_indirect | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Advanced/Diffuse/Direct Scale | <com.redshift3d.redshift4c4d.nodes.core.material.diffuse_direct | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Advanced/Diffuse/Indirect Scale | <com.redshift3d.redshift4c4d.nodes.core.material.diffuse_indirect | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Advanced/Energy Conservation | <com.redshift3d.redshift4c4d.nodes.core.material.energycompmode | maxon::Int | Input | false | false | true |  |  | 1 | Mono = 0, RGB = 1
Advanced/Reflection End Color | <com.redshift3d.redshift4c4d.nodes.core.material.refl_endmode | maxon::Int | Input | false | false | true |  |  | 1 | Environment = 0, Diffuse = 1
Advanced/Reflection/Convert From Glossiness to Roughness | <com.redshift3d.redshift4c4d.nodes.core.material.refl_isglossiness | maxon::Bool | Input | false | false | false |  |  | false | 
Advanced/Reflection/Direct Scale | <com.redshift3d.redshift4c4d.nodes.core.material.refl_direct | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Advanced/Reflection/Indirect Scale | <com.redshift3d.redshift4c4d.nodes.core.material.refl_indirect | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Advanced/Refraction/Block Volumes In Sub-Surface Mediums | <com.redshift3d.redshift4c4d.nodes.core.material.block_volumes | maxon::Bool | Input | false | false | false |  |  | true | 
Advanced/Refraction/Convert From Glossiness to Roughness | <com.redshift3d.redshift4c4d.nodes.core.material.refr_isglossiness | maxon::Bool | Input | false | false | false |  |  | false | 
Advanced/Refraction/Decouple IOR From Roughness | <com.redshift3d.redshift4c4d.nodes.core.material.decoupleiorfromroughness | maxon::Bool | Input | false | false | false |  |  | false | 
Advanced/Refraction/Opacity Affects Alpha Channel | <com.redshift3d.redshift4c4d.nodes.core.material.affects_alpha | maxon::Bool | Input | false | false | false |  |  | true | 
Advanced/Refraction/Shadow Opacity | <com.redshift3d.redshift4c4d.nodes.core.material.shadow_opacity | maxon::Float | Input | false | false | false | 0 | 1 | 0 | 
Advanced/Sheen/Convert From Glossiness to Roughness | <com.redshift3d.redshift4c4d.nodes.core.material.sheen_isglossiness | maxon::Bool | Input | false | false | false |  |  | false | 
Advanced/Sheen/Direct Scale | <com.redshift3d.redshift4c4d.nodes.core.material.sheen_direct | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Advanced/Sheen/Indirect Scale | <com.redshift3d.redshift4c4d.nodes.core.material.sheen_indirect | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Advanced/UV Context | <com.redshift3d.redshift4c4d.nodes.core.material.rs_uv_context | RSC4D::UVContext | Input | false | false | false |  |  |  | 
Base Properties/Diffuse/Back-lighting/Translucency/Color | <com.redshift3d.redshift4c4d.nodes.core.material.transl_color | maxon::Color64 | Input | false | false | false |  |  | (0.5,0.5,0.5) | 
Base Properties/Diffuse/Back-lighting/Translucency/Weight | <com.redshift3d.redshift4c4d.nodes.core.material.transl_weight | maxon::Float | Input | false | false | false | 0 | 1 | 0 | 
Base Properties/Diffuse/Color | <com.redshift3d.redshift4c4d.nodes.core.material.diffuse_color | maxon::Color64 | Input | false | false | false |  |  | (0.5,0.5,0.5) | 
Base Properties/Diffuse/Roughness | <com.redshift3d.redshift4c4d.nodes.core.material.diffuse_roughness | maxon::Float | Input | false | false | false | 0 | 1 | 0 | 
Base Properties/Diffuse/Weight | <com.redshift3d.redshift4c4d.nodes.core.material.diffuse_weight | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Base Properties/Preset | <com.redshift3d.redshift4c4d.nodes.core.material.preset | maxon::Int | Input | false | false | true |  |  | 65536 | Custom = 65536, Lead = 7, Glass = 0, Tinted Glass = 13, Water = 1, Gold = 5, Plastic = 2, Copper = 4, Aluminium = 3, Iron = 6, Paper = 12, Platinum = 8, Silver = 9, Milky Coffee = 10, Jade = 11
Base Properties/Reflection/Absorption (k) | <com.redshift3d.redshift4c4d.nodes.core.material.refl_k3 | maxon::Vector64 | Input | false | false | false | (0,0,0) | (16,16,16) | (0,0,0) | 
Base Properties/Reflection/Anisotropy | <com.redshift3d.redshift4c4d.nodes.core.material.refl_aniso | maxon::Float | Input | false | false | false | -1 | 1 | 0 | 
Base Properties/Reflection/BRDF | <com.redshift3d.redshift4c4d.nodes.core.material.refl_brdf | maxon::Int | Input | false | false | true |  |  | 0 | Beckmann (Cook-Torrance) = 0, GGX = 1, Ashikhmin-Shirley = 2
Base Properties/Reflection/Color | <com.redshift3d.redshift4c4d.nodes.core.material.refl_color | maxon::Color64 | Input | false | false | false |  |  | (1,1,1) | 
Base Properties/Reflection/Fresnel Type | <com.redshift3d.redshift4c4d.nodes.core.material.refl_fresnel_mode | maxon::Int | Input | false | false | true |  |  | 3 | IOR (Advanced) = 0, IOR = 3, Color + Edge Tint = 1, Metalness = 2
Base Properties/Reflection/IOR | <com.redshift3d.redshift4c4d.nodes.core.material.refl_ior | maxon::Float | Input | false | false | false | 0 | 100 | 1.5 | 
Base Properties/Reflection/IOR | <com.redshift3d.redshift4c4d.nodes.core.material.refl_ior3 | maxon::Vector64 | Input | false | false | false | (0,0,0) | (100,100,100) | (1.5,1.5,1.5) | 
Base Properties/Reflection/Metal Edge Tint | <com.redshift3d.redshift4c4d.nodes.core.material.refl_edge_tint | maxon::Color64 | Input | false | false | false |  |  | (0,0,0) | 
Base Properties/Reflection/Metalness | <com.redshift3d.redshift4c4d.nodes.core.material.refl_metalness | maxon::Float | Input | false | false | false | 0 | 1 | 0 | 
Base Properties/Reflection/Reflectivity | <com.redshift3d.redshift4c4d.nodes.core.material.refl_reflectivity | maxon::Color64 | Input | false | false | false |  |  | (0.04,0.04,0.04) | 
Base Properties/Reflection/Rotation | <com.redshift3d.redshift4c4d.nodes.core.material.refl_aniso_rotation | maxon::Float | Input | false | false | false | 0 | 1 | 0 | 
Base Properties/Reflection/Roughness | <com.redshift3d.redshift4c4d.nodes.core.material.refl_roughness | maxon::Float | Input | false | false | false | 0 | 1 | 0 | 
Base Properties/Reflection/Samples | <com.redshift3d.redshift4c4d.nodes.core.material.refl_samples | maxon::Int | Input | false | false | false | 0 | 65535 | 16 | 
Base Properties/Reflection/Weight | <com.redshift3d.redshift4c4d.nodes.core.material.refl_weight | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Base Properties/Refraction/Transmission/Color | <com.redshift3d.redshift4c4d.nodes.core.material.refr_color | maxon::Color64 | Input | false | false | false |  |  | (1,1,1) | 
Base Properties/Refraction/Transmission/Dispersion | <com.redshift3d.redshift4c4d.nodes.core.material.refr_abbe | maxon::Float | Input | false | false | false | 0 | 100 | 0 | 
Base Properties/Refraction/Transmission/IOR | <com.redshift3d.redshift4c4d.nodes.core.material.refr_ior | maxon::Float | Input | false | false | false | 1 | 100 | 1.5 | 
Base Properties/Refraction/Transmission/Link to Reflection | <com.redshift3d.redshift4c4d.nodes.core.material.refr_use_base_ior | maxon::Bool | Input | false | false | false |  |  | true | 
Base Properties/Refraction/Transmission/Roughness | <com.redshift3d.redshift4c4d.nodes.core.material.refr_roughness | maxon::Float | Input | false | false | false | 0 | 1 | 0 | 
Base Properties/Refraction/Transmission/Samples | <com.redshift3d.redshift4c4d.nodes.core.material.refr_samples | maxon::Int | Input | false | false | false | 0 | 65535 | 8 | 
Base Properties/Refraction/Transmission/Sub-Surface/Absorption Scale (1/cm) | <com.redshift3d.redshift4c4d.nodes.core.material.refr_absorption_scale | maxon::Float | Input | false | false | false | 0 | 100000000 | 0.01 | 
Base Properties/Refraction/Transmission/Sub-Surface/Attenuation Units | <com.redshift3d.redshift4c4d.nodes.core.material.ss_unitsmode | maxon::Int | Input | false | false | true |  |  | 0 | Transmittance = 0, Extinction = 1
Base Properties/Refraction/Transmission/Sub-Surface/Extinction Coeff (1/cm) | <com.redshift3d.redshift4c4d.nodes.core.material.ss_extinction_coeff | maxon::Color64 | Input | false | false | false |  |  | (0,0,0) | 
Base Properties/Refraction/Transmission/Sub-Surface/Extinction Scale | <com.redshift3d.redshift4c4d.nodes.core.material.ss_extinction_scale | maxon::Float | Input | false | false | false | 0 | 100000000 | 0.01 | 
Base Properties/Refraction/Transmission/Sub-Surface/Phase | <com.redshift3d.redshift4c4d.nodes.core.material.ss_phase | maxon::Float | Input | false | false | false | -1 | 1 | 0 | 
Base Properties/Refraction/Transmission/Sub-Surface/Samples | <com.redshift3d.redshift4c4d.nodes.core.material.ss_samples | maxon::Int | Input | false | false | false | 1 | 65535 | 16 | 
Base Properties/Refraction/Transmission/Sub-Surface/Scatter Coeff (1/cm) | <com.redshift3d.redshift4c4d.nodes.core.material.ss_scatter_coeff | maxon::Color64 | Input | false | false | false |  |  | (1,1,1) | 
Base Properties/Refraction/Transmission/Sub-Surface/Scatter Scale | <com.redshift3d.redshift4c4d.nodes.core.material.ss_amount | maxon::Float | Input | false | false | false | 0 | 65535 | 0 | 
Base Properties/Refraction/Transmission/Sub-Surface/Transmittance Color | <com.redshift3d.redshift4c4d.nodes.core.material.refr_transmittance | maxon::Color64 | Input | false | false | false |  |  | (1,1,1) | 
Base Properties/Refraction/Transmission/Thin Walled | <com.redshift3d.redshift4c4d.nodes.core.material.refr_thin_walled | maxon::Bool | Input | false | false | false |  |  | false | 
Base Properties/Refraction/Transmission/Weight | <com.redshift3d.redshift4c4d.nodes.core.material.refr_weight | maxon::Float | Input | false | false | false | 0 | 1 | 0 | 
Base Properties/Sheen/Color | <com.redshift3d.redshift4c4d.nodes.core.material.sheen_color | maxon::Color64 | Input | false | false | false |  |  | (1,1,1) | 
Base Properties/Sheen/Roughness | <com.redshift3d.redshift4c4d.nodes.core.material.sheen_roughness | maxon::Float | Input | false | false | false | 0 | 1 | 0.3 | 
Base Properties/Sheen/Samples | <com.redshift3d.redshift4c4d.nodes.core.material.sheen_samples | maxon::Int | Input | false | false | false | 0 | 65535 | 64 | 
Base Properties/Sheen/Weight | <com.redshift3d.redshift4c4d.nodes.core.material.sheen_weight | maxon::Float | Input | false | false | false | 0 | 1 | 0 | 
Coating/Advanced/Bump Map | <com.redshift3d.redshift4c4d.nodes.core.material.coat_bump_input | maxon::Vector64 | Input | false | false | false |  |  |  | 
Coating/Advanced/Thickness (cm) | <com.redshift3d.redshift4c4d.nodes.core.material.coat_thickness | maxon::Float | Input | false | false | false |  |  | 0.1 | 
Coating/Advanced/Transmittance | <com.redshift3d.redshift4c4d.nodes.core.material.coat_transmittance | maxon::Color64 | Input | false | false | false |  |  | (1,1,1) | 
Coating/General/BRDF | <com.redshift3d.redshift4c4d.nodes.core.material.coat_brdf | maxon::Int | Input | false | false | true |  |  | 0 | Beckmann (Cook-Torrance) = 0, GGX = 1, Ashikhmin-Shirley = 2
Coating/General/Color | <com.redshift3d.redshift4c4d.nodes.core.material.coat_color | maxon::Color64 | Input | false | false | false |  |  | (1,1,1) | 
Coating/General/Fresnel Type | <com.redshift3d.redshift4c4d.nodes.core.material.coat_fresnel_mode | maxon::Int | Input | false | false | true |  |  | 3 | IOR (Advanced) = 0, Color = 1, IOR = 3
Coating/General/IOR | <com.redshift3d.redshift4c4d.nodes.core.material.coat_ior | maxon::Float | Input | false | false | false | 0 | 100 | 1.4 | 
Coating/General/IOR | <com.redshift3d.redshift4c4d.nodes.core.material.coat_ior3 | maxon::Vector64 | Input | false | false | false | (0,0,0) | (100,100,100) | (1.4,1.4,1.4) | 
Coating/General/Reflectivity | <com.redshift3d.redshift4c4d.nodes.core.material.coat_reflectivity | maxon::Color64 | Input | false | false | false |  |  | (0.027,0.027,0.027) | 
Coating/General/Roughness | <com.redshift3d.redshift4c4d.nodes.core.material.coat_roughness | maxon::Float | Input | false | false | false | 0 | 1 | 0 | 
Coating/General/Samples | <com.redshift3d.redshift4c4d.nodes.core.material.coat_samples | maxon::Int | Input | false | false | false | 0 | 65535 | 16 | 
Coating/General/Weight | <com.redshift3d.redshift4c4d.nodes.core.material.coat_weight | maxon::Float | Input | false | false | false | 0 | 1 | 0 | 
Multi-SSS/General/Amount | <com.redshift3d.redshift4c4d.nodes.core.material.ms_amount | maxon::Float | Input | false | false | false | 0 | 1 | 0 | 
Multi-SSS/General/Include Mode | <com.redshift3d.redshift4c4d.nodes.core.material.ms_include_mode | maxon::Int | Input | false | false | true |  |  | 1 | All Objects = 0, Only Self = 1
Multi-SSS/General/Mode | <com.redshift3d.redshift4c4d.nodes.core.material.ms_mode | maxon::Int | Input | false | false | true |  |  | 1 | Point-Based = 0, Ray-Traced = 1
Multi-SSS/General/Radius Scale | <com.redshift3d.redshift4c4d.nodes.core.material.ms_radius_scale | maxon::Float | Input | false | false | false | 0 | 100000 | 100 | 
Multi-SSS/General/Samples | <com.redshift3d.redshift4c4d.nodes.core.material.ms_samples | maxon::Int | Input | false | false | false | 1 | 65535 | 64 | 
Multi-SSS/Layer 1/Color | <com.redshift3d.redshift4c4d.nodes.core.material.ms_color0 | maxon::Color64 | Input | false | false | false |  |  | (1,0.9,0.7) | 
Multi-SSS/Layer 1/Radius (cm) | <com.redshift3d.redshift4c4d.nodes.core.material.ms_radius0 | maxon::Float | Input | false | false | false | 0 | 100000000 | 1 | 
Multi-SSS/Layer 1/Weight | <com.redshift3d.redshift4c4d.nodes.core.material.ms_weight0 | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Multi-SSS/Layer 2/Color | <com.redshift3d.redshift4c4d.nodes.core.material.ms_color1 | maxon::Color64 | Input | false | false | false |  |  | (1,0.9,0.7) | 
Multi-SSS/Layer 2/Radius (cm) | <com.redshift3d.redshift4c4d.nodes.core.material.ms_radius1 | maxon::Float | Input | false | false | false | 0 | 100000000 | 1 | 
Multi-SSS/Layer 2/Weight | <com.redshift3d.redshift4c4d.nodes.core.material.ms_weight1 | maxon::Float | Input | false | false | false | 0 | 1 | 0 | 
Multi-SSS/Layer 3/Color | <com.redshift3d.redshift4c4d.nodes.core.material.ms_color2 | maxon::Color64 | Input | false | false | false |  |  | (1,0.9,0.7) | 
Multi-SSS/Layer 3/Radius (cm) | <com.redshift3d.redshift4c4d.nodes.core.material.ms_radius2 | maxon::Float | Input | false | false | false | 0 | 100000000 | 1 | 
Multi-SSS/Layer 3/Weight | <com.redshift3d.redshift4c4d.nodes.core.material.ms_weight2 | maxon::Float | Input | false | false | false | 0 | 1 | 0 | 
Optimizations/Combined Trace Depth | <com.redshift3d.redshift4c4d.nodes.core.material.combined_depth | maxon::Int | Input | false | false | false | 0 | 63 | 6 | 
Optimizations/Enable Trace Depth Overrides | <com.redshift3d.redshift4c4d.nodes.core.material.depth_override | maxon::Bool | Input | false | false | false |  |  | false | 
Optimizations/Reflection/Cull Dim Internal Reflections | <com.redshift3d.redshift4c4d.nodes.core.material.skip_inside_refl | maxon::Bool | Input | false | false | false |  |  | true | 
Optimizations/Reflection/Cut-off Override Enable | <com.redshift3d.redshift4c4d.nodes.core.material.refl_enablecutoff | maxon::Bool | Input | false | false | false |  |  | false | 
Optimizations/Reflection/Cut-off Threshold | <com.redshift3d.redshift4c4d.nodes.core.material.refl_cutoff | maxon::Float | Input | false | false | false | 0 | 1 | 0.01 | 
Optimizations/Reflection/Trace Depth | <com.redshift3d.redshift4c4d.nodes.core.material.refl_depth | maxon::Int | Input | false | false | false | 0 | 63 | 3 | 
Optimizations/Refraction/Cut-off Override Enable | <com.redshift3d.redshift4c4d.nodes.core.material.refr_enablecutoff | maxon::Bool | Input | false | false | false |  |  | false | 
Optimizations/Refraction/Cut-off Threshold | <com.redshift3d.redshift4c4d.nodes.core.material.refr_cutoff | maxon::Float | Input | false | false | false | 0 | 1 | 0.01 | 
Optimizations/Refraction/Trace Depth | <com.redshift3d.redshift4c4d.nodes.core.material.refr_depth | maxon::Int | Input | false | false | false | 0 | 63 | 5 | 
Overall/Bump Map | <com.redshift3d.redshift4c4d.nodes.core.material.bump_input | maxon::Vector64 | Input | false | false | false |  |  |  | 
Overall/Emission | <com.redshift3d.redshift4c4d.nodes.core.material.emission_color | maxon::Color64 | Input | false | false | false |  |  | (0,0,0) | 
Overall/Opacity | <com.redshift3d.redshift4c4d.nodes.core.material.opacity_color | maxon::Color64 | Input | false | false | false |  |  | (1,1,1) | 
Overall/Overall Tint | <com.redshift3d.redshift4c4d.nodes.core.material.overall_color | maxon::Color64 | Input | false | false | false |  |  | (1,1,1) | 
Overall/Radiance (W/sr/m^2) | <com.redshift3d.redshift4c4d.nodes.core.material.emission_weight | maxon::Float | Input | false | false | false |  |  | 0 | 
Outputs/outColor | >com.redshift3d.redshift4c4d.nodes.core.material.outcolor | maxon::Color64 | Output | false | false | false |  |  | (0,0,0) | 

