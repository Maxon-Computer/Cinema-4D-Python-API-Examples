# Node Template: Standard Material

- **Node Space ID:** `com.redshift3d.redshift4c4d.class.nodespace`
- **Template ID:** `com.redshift3d.redshift4c4d.nodes.core.standardmaterial`
- **Template Name:** `Standard Material`

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
Advanced/Anisotropy/Surface Orientation | <com.redshift3d.redshift4c4d.nodes.core.standardmaterial.anisotropy_orientation | maxon::Int | Input | false | false | true |  |  | 2 | None = 2, From Tangent Channel = 1
Advanced/Anisotropy/Tangent Channel | <com.redshift3d.redshift4c4d.nodes.core.standardmaterial.anisotropy_tangentchannel | maxon::String | Input | false | false | false |  |  |  | 
Advanced/Anisotropy/UV Channel | <com.redshift3d.redshift4c4d.nodes.core.standardmaterial.anisotropy_uvchannel | maxon::String | Input | false | false | false |  |  |  | 
Advanced/Coat/Direct Scale | <com.redshift3d.redshift4c4d.nodes.core.standardmaterial.coat_direct | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Advanced/Coat/Glossiness to Roughness | <com.redshift3d.redshift4c4d.nodes.core.standardmaterial.coat_isglossiness | maxon::Bool | Input | false | false | false |  |  | false | 
Advanced/Coat/Indirect Scale | <com.redshift3d.redshift4c4d.nodes.core.standardmaterial.coat_indirect | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Advanced/Diffuse/Direct Scale | <com.redshift3d.redshift4c4d.nodes.core.standardmaterial.diffuse_direct | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Advanced/Diffuse/Indirect Scale | <com.redshift3d.redshift4c4d.nodes.core.standardmaterial.diffuse_indirect | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Advanced/Microfacet Multi-Scatter Compensation | <com.redshift3d.redshift4c4d.nodes.core.standardmaterial.refl_enablemultiscattercomp | maxon::Bool | Input | false | false | false |  |  | true | 
Advanced/Reflection/Direct Scale | <com.redshift3d.redshift4c4d.nodes.core.standardmaterial.refl_direct | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Advanced/Reflection/End Color | <com.redshift3d.redshift4c4d.nodes.core.standardmaterial.refl_endmode | maxon::Int | Input | false | false | true |  |  | 1 | Environment = 0, Diffuse = 1
Advanced/Reflection/Glossiness to Roughness | <com.redshift3d.redshift4c4d.nodes.core.standardmaterial.refl_isglossiness | maxon::Bool | Input | false | false | false |  |  | false | 
Advanced/Reflection/Indirect Scale | <com.redshift3d.redshift4c4d.nodes.core.standardmaterial.refl_indirect | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Advanced/Sheen/Direct Scale | <com.redshift3d.redshift4c4d.nodes.core.standardmaterial.sheen_direct | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Advanced/Sheen/Glossiness to Roughness | <com.redshift3d.redshift4c4d.nodes.core.standardmaterial.sheen_isglossiness | maxon::Bool | Input | false | false | false |  |  | false | 
Advanced/Sheen/Indirect Scale | <com.redshift3d.redshift4c4d.nodes.core.standardmaterial.sheen_indirect | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Advanced/Transmission/Block Volumes In SSS Mediums | <com.redshift3d.redshift4c4d.nodes.core.standardmaterial.block_volumes | maxon::Bool | Input | false | false | false |  |  | true | 
Advanced/Transmission/Direct Scale | <com.redshift3d.redshift4c4d.nodes.core.standardmaterial.refr_direct | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Advanced/Transmission/Fresnel Affects Shadow | <com.redshift3d.redshift4c4d.nodes.core.standardmaterial.shadow_affected_by_fresnel_mode | maxon::Int | Input | false | false | true |  |  | 2 | Off = 0, On = 1, On (no internal reflection) = 2
Advanced/Transmission/Glossiness to Roughness | <com.redshift3d.redshift4c4d.nodes.core.standardmaterial.refr_isglossiness | maxon::Bool | Input | false | false | false |  |  | false | 
Advanced/Transmission/Legacy Light Sampling | <com.redshift3d.redshift4c4d.nodes.core.standardmaterial.refr_legacy_light_sampling | maxon::Bool | Input | false | false | false |  |  | false | 
Advanced/Transmission/Opacity Affects Alpha Channel | <com.redshift3d.redshift4c4d.nodes.core.standardmaterial.affects_alpha | maxon::Bool | Input | false | false | false |  |  | true | 
Advanced/Transmission/Shadow Opacity | <com.redshift3d.redshift4c4d.nodes.core.standardmaterial.shadow_opacity | maxon::Float | Input | false | false | false | -1 | 1 | 0 | 
Advanced/UV Context | <com.redshift3d.redshift4c4d.nodes.core.standardmaterial.rs_uv_context | RSC4D::UVContext | Input | false | false | false |  |  |  | 
Base Properties/Base/Color | <com.redshift3d.redshift4c4d.nodes.core.standardmaterial.base_color | maxon::Color64 | Input | false | false | false |  |  | (0.5,0.5,0.5) | 
Base Properties/Base/Diffuse Model | <com.redshift3d.redshift4c4d.nodes.core.standardmaterial.diffuse_model | maxon::Int | Input | false | false | true |  |  | 0 | Oren-Nayar = 0, d'Eon Lambertian Spheres = 1, EON = 2
Base Properties/Base/Diffuse Roughness | <com.redshift3d.redshift4c4d.nodes.core.standardmaterial.diffuse_roughness | maxon::Float | Input | false | false | false | 0 | 1 | 0 | 
Base Properties/Base/Metalness | <com.redshift3d.redshift4c4d.nodes.core.standardmaterial.metalness | maxon::Float | Input | false | false | false | 0 | 1 | 0 | 
Base Properties/Base/Weight | <com.redshift3d.redshift4c4d.nodes.core.standardmaterial.base_color_weight | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Base Properties/Coat/Anisotropy | <com.redshift3d.redshift4c4d.nodes.core.standardmaterial.coat_aniso | maxon::Float | Input | false | false | false | 0 | 1 | 0 | 
Base Properties/Coat/Bump Map | <com.redshift3d.redshift4c4d.nodes.core.standardmaterial.coat_bump_input | maxon::Vector64 | Input | false | false | false |  |  |  | 
Base Properties/Coat/Color | <com.redshift3d.redshift4c4d.nodes.core.standardmaterial.coat_color | maxon::Color64 | Input | false | false | false |  |  | (1,1,1) | 
Base Properties/Coat/IOR | <com.redshift3d.redshift4c4d.nodes.core.standardmaterial.coat_ior | maxon::Float | Input | false | false | false | 0 | 32 | 1.5 | 
Base Properties/Coat/Rotation | <com.redshift3d.redshift4c4d.nodes.core.standardmaterial.coat_aniso_rotation | maxon::Float | Input | false | false | false | 0 | 1 | 0 | 
Base Properties/Coat/Roughness | <com.redshift3d.redshift4c4d.nodes.core.standardmaterial.coat_roughness | maxon::Float | Input | false | false | false | 0 | 1 | 0 | 
Base Properties/Coat/Samples | <com.redshift3d.redshift4c4d.nodes.core.standardmaterial.coat_samples | maxon::Int | Input | false | false | false | 0 | 65535 | 16 | 
Base Properties/Coat/Weight | <com.redshift3d.redshift4c4d.nodes.core.standardmaterial.coat_weight | maxon::Float | Input | false | false | false | 0 | 1 | 0 | 
Base Properties/Emission/Color | <com.redshift3d.redshift4c4d.nodes.core.standardmaterial.emission_color | maxon::Color64 | Input | false | false | false |  |  | (1,1,1) | 
Base Properties/Emission/Radiance (W/sr/m^2) | <com.redshift3d.redshift4c4d.nodes.core.standardmaterial.emission_weight | maxon::Float | Input | false | false | false |  |  | 0 | 
Base Properties/Geometry/Affects Emission | <com.redshift3d.redshift4c4d.nodes.core.standardmaterial.overallaffectsemission | maxon::Bool | Input | false | false | false |  |  | false | 
Base Properties/Geometry/Bump Map | <com.redshift3d.redshift4c4d.nodes.core.standardmaterial.bump_input | maxon::Vector64 | Input | false | false | false |  |  |  | 
Base Properties/Geometry/Opacity | <com.redshift3d.redshift4c4d.nodes.core.standardmaterial.opacity_color | maxon::Color64 | Input | false | false | false |  |  | (1,1,1) | 
Base Properties/Geometry/Overall Tint | <com.redshift3d.redshift4c4d.nodes.core.standardmaterial.overall_color | maxon::Color64 | Input | false | false | false |  |  | (1,1,1) | 
Base Properties/Geometry/Thin Walled | <com.redshift3d.redshift4c4d.nodes.core.standardmaterial.refr_thin_walled | maxon::Bool | Input | false | false | false |  |  | false | 
Base Properties/Reflection/Anisotropy | <com.redshift3d.redshift4c4d.nodes.core.standardmaterial.refl_aniso | maxon::Float | Input | false | false | false | 0 | 1 | 0 | 
Base Properties/Reflection/Color | <com.redshift3d.redshift4c4d.nodes.core.standardmaterial.refl_color | maxon::Color64 | Input | false | false | false |  |  | (1,1,1) | 
Base Properties/Reflection/IOR | <com.redshift3d.redshift4c4d.nodes.core.standardmaterial.refl_ior | maxon::Float | Input | false | false | false | 0 | 32 | 1.5 | 
Base Properties/Reflection/Rotation | <com.redshift3d.redshift4c4d.nodes.core.standardmaterial.refl_aniso_rotation | maxon::Float | Input | false | false | false | 0 | 1 | 0 | 
Base Properties/Reflection/Roughness | <com.redshift3d.redshift4c4d.nodes.core.standardmaterial.refl_roughness | maxon::Float | Input | false | false | false | 0 | 1 | 0.2 | 
Base Properties/Reflection/Samples | <com.redshift3d.redshift4c4d.nodes.core.standardmaterial.refl_samples | maxon::Int | Input | false | false | false | 0 | 65535 | 16 | 
Base Properties/Reflection/Weight | <com.redshift3d.redshift4c4d.nodes.core.standardmaterial.refl_weight | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Base Properties/Sheen/Color | <com.redshift3d.redshift4c4d.nodes.core.standardmaterial.sheen_color | maxon::Color64 | Input | false | false | false |  |  | (1,1,1) | 
Base Properties/Sheen/Roughness | <com.redshift3d.redshift4c4d.nodes.core.standardmaterial.sheen_roughness | maxon::Float | Input | false | false | false | 0 | 1 | 0.3 | 
Base Properties/Sheen/Samples | <com.redshift3d.redshift4c4d.nodes.core.standardmaterial.sheen_samples | maxon::Int | Input | false | false | false | 0 | 65535 | 64 | 
Base Properties/Sheen/Weight | <com.redshift3d.redshift4c4d.nodes.core.standardmaterial.sheen_weight | maxon::Float | Input | false | false | false | 0 | 1 | 0 | 
Base Properties/Subsurface/Anisotropy | <com.redshift3d.redshift4c4d.nodes.core.standardmaterial.ms_phase | maxon::Float | Input | false | false | false | -1 | 1 | 0 | 
Base Properties/Subsurface/Color | <com.redshift3d.redshift4c4d.nodes.core.standardmaterial.ms_color | maxon::Color64 | Input | false | false | false |  |  | (1,1,1) | 
Base Properties/Subsurface/Include Mode | <com.redshift3d.redshift4c4d.nodes.core.standardmaterial.ms_include_mode | maxon::Int | Input | false | false | true |  |  | 1 | All Objects = 0, Only Self = 1
Base Properties/Subsurface/Mode | <com.redshift3d.redshift4c4d.nodes.core.standardmaterial.ms_mode | maxon::Int | Input | false | false | true |  |  | 2 | Point-Based Diffusion = 0, Ray-Traced Diffusion = 1, Random Walk = 2
Base Properties/Subsurface/Radius (cm) | <com.redshift3d.redshift4c4d.nodes.core.standardmaterial.ms_radius | maxon::Color64 | Input | false | false | false |  |  | (1,1,1) | 
Base Properties/Subsurface/Samples | <com.redshift3d.redshift4c4d.nodes.core.standardmaterial.ms_samples | maxon::Int | Input | false | false | false | 1 | 65535 | 64 | 
Base Properties/Subsurface/Scale | <com.redshift3d.redshift4c4d.nodes.core.standardmaterial.ms_radius_scale | maxon::Float | Input | false | false | false | 0 | 100000 | 1 | 
Base Properties/Subsurface/Weight | <com.redshift3d.redshift4c4d.nodes.core.standardmaterial.ms_amount | maxon::Float | Input | false | false | false | 0 | 1 | 0 | 
Base Properties/Thin Film/IOR | <com.redshift3d.redshift4c4d.nodes.core.standardmaterial.thinfilm_ior | maxon::Float | Input | false | false | false | 0 | 100 | 1.5 | 
Base Properties/Thin Film/Thickness (nm) | <com.redshift3d.redshift4c4d.nodes.core.standardmaterial.thinfilm_thickness | maxon::Float | Input | false | false | false | 0 | 65535 | 0 | 
Base Properties/Transmission/Color | <com.redshift3d.redshift4c4d.nodes.core.standardmaterial.refr_color | maxon::Color64 | Input | false | false | false |  |  | (1,1,1) | 
Base Properties/Transmission/Depth (cm) | <com.redshift3d.redshift4c4d.nodes.core.standardmaterial.ss_depth | maxon::Float | Input | false | false | false | 0 | 65535 | 0 | 
Base Properties/Transmission/Dispersion (Abbe) | <com.redshift3d.redshift4c4d.nodes.core.standardmaterial.refr_abbe | maxon::Float | Input | false | false | false | 0 | 100 | 0 | 
Base Properties/Transmission/Extra Roughness | <com.redshift3d.redshift4c4d.nodes.core.standardmaterial.refr_roughness | maxon::Float | Input | false | false | false | -1 | 1 | 0 | 
Base Properties/Transmission/Samples | <com.redshift3d.redshift4c4d.nodes.core.standardmaterial.refr_samples | maxon::Int | Input | false | false | false | 0 | 65535 | 8 | 
Base Properties/Transmission/Samples | <com.redshift3d.redshift4c4d.nodes.core.standardmaterial.ss_samples | maxon::Int | Input | false | false | false | 1 | 65535 | 16 | 
Base Properties/Transmission/Scatter Anisotropy | <com.redshift3d.redshift4c4d.nodes.core.standardmaterial.ss_phase | maxon::Float | Input | false | false | false | -1 | 1 | 0 | 
Base Properties/Transmission/Scatter Color | <com.redshift3d.redshift4c4d.nodes.core.standardmaterial.ss_scatter_color | maxon::Color64 | Input | false | false | false |  |  | (0,0,0) | 
Base Properties/Transmission/Weight | <com.redshift3d.redshift4c4d.nodes.core.standardmaterial.refr_weight | maxon::Float | Input | false | false | false | 0 | 1 | 0 | 
Optimizations/Combined Trace Depth | <com.redshift3d.redshift4c4d.nodes.core.standardmaterial.combined_depth | maxon::Int | Input | false | false | false | 0 | 63 | 6 | 
Optimizations/Reflection/Cut-off Threshold | <com.redshift3d.redshift4c4d.nodes.core.standardmaterial.refl_cutoff | maxon::Float | Input | false | false | false | 0 | 1 | 0.01 | 
Optimizations/Reflection/Override Cut-off | <com.redshift3d.redshift4c4d.nodes.core.standardmaterial.refl_enablecutoff | maxon::Bool | Input | false | false | false |  |  | false | 
Optimizations/Reflection/Trace Depth | <com.redshift3d.redshift4c4d.nodes.core.standardmaterial.refl_depth | maxon::Int | Input | false | false | false | 0 | 63 | 3 | 
Optimizations/Trace Depth Overrides | <com.redshift3d.redshift4c4d.nodes.core.standardmaterial.depth_override | maxon::Bool | Input | false | false | false |  |  | false | 
Optimizations/Transmission/Cut-off Threshold | <com.redshift3d.redshift4c4d.nodes.core.standardmaterial.refr_cutoff | maxon::Float | Input | false | false | false | 0 | 1 | 0.01 | 
Optimizations/Transmission/Override Cut-off | <com.redshift3d.redshift4c4d.nodes.core.standardmaterial.refr_enablecutoff | maxon::Bool | Input | false | false | false |  |  | false | 
Optimizations/Transmission/Trace Depth | <com.redshift3d.redshift4c4d.nodes.core.standardmaterial.refr_depth | maxon::Int | Input | false | false | false | 0 | 63 | 5 | 
Outputs/outColor | >com.redshift3d.redshift4c4d.nodes.core.standardmaterial.outcolor | maxon::Color64 | Output | false | false | false |  |  | (0,0,0) | 

