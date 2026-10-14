# Node Template: OpenPBR Material

- **Node Space ID:** `com.redshift3d.redshift4c4d.class.nodespace`
- **Template ID:** `com.redshift3d.redshift4c4d.nodes.core.openpbrmaterial`
- **Template Name:** `OpenPBR Material`

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
Base Properties/Base/Color | <com.redshift3d.redshift4c4d.nodes.core.openpbrmaterial.base_color | maxon::Color64 | Input | false | false | false |  |  | (0.8,0.8,0.8) | 
Base Properties/Base/Diffuse Roughness | <com.redshift3d.redshift4c4d.nodes.core.openpbrmaterial.base_diffuse_roughness | maxon::Float | Input | false | false | false | 0 | 1 | 0 | 
Base Properties/Base/Metalness | <com.redshift3d.redshift4c4d.nodes.core.openpbrmaterial.base_metalness | maxon::Float | Input | false | false | false | 0 | 1 | 0 | 
Base Properties/Base/Weight | <com.redshift3d.redshift4c4d.nodes.core.openpbrmaterial.base_weight | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Base Properties/Coat/Anisotropy | <com.redshift3d.redshift4c4d.nodes.core.openpbrmaterial.coat_roughness_anisotropy | maxon::Float | Input | false | false | false | 0 | 1 | 0 | 
Base Properties/Coat/Anisotropy Tangent | <com.redshift3d.redshift4c4d.nodes.core.openpbrmaterial.geometry_coat_tangent | maxon::Vector64 | Input | false | false | false |  |  |  | 
Base Properties/Coat/Bump Map | <com.redshift3d.redshift4c4d.nodes.core.openpbrmaterial.geometry_coat_normal | maxon::Vector64 | Input | false | false | false |  |  |  | 
Base Properties/Coat/Color | <com.redshift3d.redshift4c4d.nodes.core.openpbrmaterial.coat_color | maxon::Color64 | Input | false | false | false |  |  | (1,1,1) | 
Base Properties/Coat/Darkening | <com.redshift3d.redshift4c4d.nodes.core.openpbrmaterial.coat_darkening | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Base Properties/Coat/IOR | <com.redshift3d.redshift4c4d.nodes.core.openpbrmaterial.coat_ior | maxon::Float | Input | false | false | false | 0 | 32 | 1.6 | 
Base Properties/Coat/Roughness | <com.redshift3d.redshift4c4d.nodes.core.openpbrmaterial.coat_roughness | maxon::Float | Input | false | false | false | 0 | 1 | 0 | 
Base Properties/Coat/Weight | <com.redshift3d.redshift4c4d.nodes.core.openpbrmaterial.coat_weight | maxon::Float | Input | false | false | false | 0 | 1 | 0 | 
Base Properties/Emission/Color | <com.redshift3d.redshift4c4d.nodes.core.openpbrmaterial.emission_color | maxon::Color64 | Input | false | false | false |  |  | (1,1,1) | 
Base Properties/Emission/Luminance (cd/m^2) | <com.redshift3d.redshift4c4d.nodes.core.openpbrmaterial.emission_luminance | maxon::Float | Input | false | false | false | 0 | 2147483648 | 0 | 
Base Properties/Fuzz/Color | <com.redshift3d.redshift4c4d.nodes.core.openpbrmaterial.fuzz_color | maxon::Color64 | Input | false | false | false |  |  | (1,1,1) | 
Base Properties/Fuzz/Roughness | <com.redshift3d.redshift4c4d.nodes.core.openpbrmaterial.fuzz_roughness | maxon::Float | Input | false | false | false | 0 | 1 | 0.5 | 
Base Properties/Fuzz/Weight | <com.redshift3d.redshift4c4d.nodes.core.openpbrmaterial.fuzz_weight | maxon::Float | Input | false | false | false | 0 | 1 | 0 | 
Base Properties/Geometry/Bump Map | <com.redshift3d.redshift4c4d.nodes.core.openpbrmaterial.geometry_normal | maxon::Vector64 | Input | false | false | false |  |  |  | 
Base Properties/Geometry/Opacity | <com.redshift3d.redshift4c4d.nodes.core.openpbrmaterial.geometry_opacity | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Base Properties/Geometry/Thin Walled | <com.redshift3d.redshift4c4d.nodes.core.openpbrmaterial.geometry_thin_walled | maxon::Bool | Input | false | false | false |  |  | false | 
Base Properties/Specular/Anisotropy | <com.redshift3d.redshift4c4d.nodes.core.openpbrmaterial.specular_roughness_anisotropy | maxon::Float | Input | false | false | false | 0 | 1 | 0 | 
Base Properties/Specular/Anisotropy Tangent | <com.redshift3d.redshift4c4d.nodes.core.openpbrmaterial.geometry_tangent | maxon::Vector64 | Input | false | false | false |  |  |  | 
Base Properties/Specular/Color | <com.redshift3d.redshift4c4d.nodes.core.openpbrmaterial.specular_color | maxon::Color64 | Input | false | false | false |  |  | (1,1,1) | 
Base Properties/Specular/IOR | <com.redshift3d.redshift4c4d.nodes.core.openpbrmaterial.specular_ior | maxon::Float | Input | false | false | false | 0 | 32 | 1.5 | 
Base Properties/Specular/Roughness | <com.redshift3d.redshift4c4d.nodes.core.openpbrmaterial.specular_roughness | maxon::Float | Input | false | false | false | 0 | 1 | 0.3 | 
Base Properties/Specular/Weight | <com.redshift3d.redshift4c4d.nodes.core.openpbrmaterial.specular_weight | maxon::Float | Input | false | false | false | 0 | 65535 | 1 | 
Base Properties/Subsurface/Anisotropy | <com.redshift3d.redshift4c4d.nodes.core.openpbrmaterial.subsurface_scatter_anisotropy | maxon::Float | Input | false | false | false | -1 | 1 | 0 | 
Base Properties/Subsurface/Color | <com.redshift3d.redshift4c4d.nodes.core.openpbrmaterial.subsurface_color | maxon::Color64 | Input | false | false | false |  |  | (0.8,0.8,0.8) | 
Base Properties/Subsurface/Radius (cm) | <com.redshift3d.redshift4c4d.nodes.core.openpbrmaterial.subsurface_radius | maxon::Float | Input | false | false | false | 0 | 100000 | 1 | 
Base Properties/Subsurface/Radius Scale | <com.redshift3d.redshift4c4d.nodes.core.openpbrmaterial.subsurface_radius_scale | maxon::Color64 | Input | false | false | false |  |  | (1.373,0.438,0.2) | 
Base Properties/Subsurface/Weight | <com.redshift3d.redshift4c4d.nodes.core.openpbrmaterial.subsurface_weight | maxon::Float | Input | false | false | false | 0 | 1 | 0 | 
Base Properties/Thin Film/IOR | <com.redshift3d.redshift4c4d.nodes.core.openpbrmaterial.thin_film_ior | maxon::Float | Input | false | false | false | 0 | 32 | 1.4 | 
Base Properties/Thin Film/Thickness (μm) | <com.redshift3d.redshift4c4d.nodes.core.openpbrmaterial.thin_film_thickness | maxon::Float | Input | false | false | false | 0 | 65535 | 0.5 | 
Base Properties/Thin Film/Weight | <com.redshift3d.redshift4c4d.nodes.core.openpbrmaterial.thin_film_weight | maxon::Float | Input | false | false | false | 0 | 1 | 0 | 
Base Properties/Transmission/Anisotropy | <com.redshift3d.redshift4c4d.nodes.core.openpbrmaterial.transmission_scatter_anisotropy | maxon::Float | Input | false | false | false | -1 | 1 | 0 | 
Base Properties/Transmission/Color | <com.redshift3d.redshift4c4d.nodes.core.openpbrmaterial.transmission_color | maxon::Color64 | Input | false | false | false |  |  | (1,1,1) | 
Base Properties/Transmission/Depth (cm) | <com.redshift3d.redshift4c4d.nodes.core.openpbrmaterial.transmission_depth | maxon::Float | Input | false | false | false | 0 | 65535 | 0 | 
Base Properties/Transmission/Dispersion (Abbe) | <com.redshift3d.redshift4c4d.nodes.core.openpbrmaterial.transmission_dispersion_abbe_number | maxon::Float | Input | false | false | false | 0 | 100 | 20 | 
Base Properties/Transmission/Dispersion Weight | <com.redshift3d.redshift4c4d.nodes.core.openpbrmaterial.transmission_dispersion_scale | maxon::Float | Input | false | false | false | 0 | 1 | 0 | 
Base Properties/Transmission/Scatter | <com.redshift3d.redshift4c4d.nodes.core.openpbrmaterial.transmission_scatter | maxon::Color64 | Input | false | false | false |  |  | (0,0,0) | 
Base Properties/Transmission/Weight | <com.redshift3d.redshift4c4d.nodes.core.openpbrmaterial.transmission_weight | maxon::Float | Input | false | false | false | 0 | 1 | 0 | 
Redshift Advanced/Coat/Direct Scale | <com.redshift3d.redshift4c4d.nodes.core.openpbrmaterial.rs_coat_direct | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Redshift Advanced/Coat/Indirect Scale | <com.redshift3d.redshift4c4d.nodes.core.openpbrmaterial.rs_coat_indirect | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Redshift Advanced/Coat/Samples | <com.redshift3d.redshift4c4d.nodes.core.openpbrmaterial.rs_coat_samples | maxon::Int | Input | false | false | false | 0 | 65535 | 64 | 
Redshift Advanced/Diffuse/Direct Scale | <com.redshift3d.redshift4c4d.nodes.core.openpbrmaterial.rs_base_diffuse_direct | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Redshift Advanced/Diffuse/Indirect Scale | <com.redshift3d.redshift4c4d.nodes.core.openpbrmaterial.rs_base_diffuse_indirect | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Redshift Advanced/Fuzz/Direct Scale | <com.redshift3d.redshift4c4d.nodes.core.openpbrmaterial.rs_fuzz_direct | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Redshift Advanced/Fuzz/Indirect Scale | <com.redshift3d.redshift4c4d.nodes.core.openpbrmaterial.rs_fuzz_indirect | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Redshift Advanced/Fuzz/Samples | <com.redshift3d.redshift4c4d.nodes.core.openpbrmaterial.rs_fuzz_samples | maxon::Int | Input | false | false | false | 0 | 65535 | 64 | 
Redshift Advanced/Reflection/Direct Scale | <com.redshift3d.redshift4c4d.nodes.core.openpbrmaterial.rs_specular_direct | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Redshift Advanced/Reflection/End Color | <com.redshift3d.redshift4c4d.nodes.core.openpbrmaterial.rs_specular_endmode | maxon::Int | Input | false | false | true |  |  | 1 | Environment = 0, Diffuse = 1
Redshift Advanced/Reflection/Indirect Scale | <com.redshift3d.redshift4c4d.nodes.core.openpbrmaterial.rs_specular_indirect | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Redshift Advanced/Reflection/Samples | <com.redshift3d.redshift4c4d.nodes.core.openpbrmaterial.rs_specular_samples | maxon::Int | Input | false | false | false | 0 | 65535 | 64 | 
Redshift Advanced/Subsurface/Include Mode | <com.redshift3d.redshift4c4d.nodes.core.openpbrmaterial.rs_subsurface_include_mode | maxon::Int | Input | false | false | true |  |  | 1 | All Objects = 0, Only Self = 1
Redshift Advanced/Subsurface/Mode | <com.redshift3d.redshift4c4d.nodes.core.openpbrmaterial.rs_subsurface_mode | maxon::Int | Input | false | false | true |  |  | 2 | Point-Based Diffusion = 0, Ray-Traced Diffusion = 1, Random Walk = 2
Redshift Advanced/Subsurface/Samples | <com.redshift3d.redshift4c4d.nodes.core.openpbrmaterial.rs_subsurface_samples | maxon::Int | Input | false | false | false | 1 | 65535 | 64 | 
Redshift Advanced/Transmission/Block Volumes In SSS Mediums | <com.redshift3d.redshift4c4d.nodes.core.openpbrmaterial.rs_transmission_block_volumes | maxon::Bool | Input | false | false | false |  |  | true | 
Redshift Advanced/Transmission/Direct Scale | <com.redshift3d.redshift4c4d.nodes.core.openpbrmaterial.rs_transmission_direct | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Redshift Advanced/Transmission/Fresnel Affects Shadow | <com.redshift3d.redshift4c4d.nodes.core.openpbrmaterial.rs_shadow_affected_by_fresnel_mode | maxon::Int | Input | false | false | true |  |  | 2 | Off = 0, On = 1, On (no internal reflection) = 2
Redshift Advanced/Transmission/Opacity Affects Alpha Channel | <com.redshift3d.redshift4c4d.nodes.core.openpbrmaterial.rs_transmission_affects_alpha | maxon::Bool | Input | false | false | false |  |  | true | 
Redshift Advanced/Transmission/Samples | <com.redshift3d.redshift4c4d.nodes.core.openpbrmaterial.rs_transmission_samples | maxon::Int | Input | false | false | false | 0 | 65535 | 64 | 
Redshift Advanced/Transmission/Scatter Samples | <com.redshift3d.redshift4c4d.nodes.core.openpbrmaterial.rs_transmission_scatter_samples | maxon::Int | Input | false | false | false | 1 | 65535 | 64 | 
Redshift Advanced/Transmission/Shadow Opacity | <com.redshift3d.redshift4c4d.nodes.core.openpbrmaterial.rs_shadow_opacity | maxon::Float | Input | false | false | false | -1 | 1 | 0 | 
Redshift Advanced/UV Context | <com.redshift3d.redshift4c4d.nodes.core.openpbrmaterial.rs_uv_context | RSC4D::UVContext | Input | false | false | false |  |  |  | 
Redshift Optimizations/Combined Trace Depth | <com.redshift3d.redshift4c4d.nodes.core.openpbrmaterial.rs_combined_depth | maxon::Int | Input | false | false | false | 0 | 63 | 6 | 
Redshift Optimizations/Reflection/Cut-off Threshold | <com.redshift3d.redshift4c4d.nodes.core.openpbrmaterial.rs_specular_cutoff | maxon::Float | Input | false | false | false | 0 | 1 | 0.01 | 
Redshift Optimizations/Reflection/Override Cut-off | <com.redshift3d.redshift4c4d.nodes.core.openpbrmaterial.rs_specular_enablecutoff | maxon::Bool | Input | false | false | false |  |  | false | 
Redshift Optimizations/Reflection/Trace Depth | <com.redshift3d.redshift4c4d.nodes.core.openpbrmaterial.rs_specular_depth | maxon::Int | Input | false | false | false | 0 | 63 | 3 | 
Redshift Optimizations/Trace Depth Overrides | <com.redshift3d.redshift4c4d.nodes.core.openpbrmaterial.rs_depth_override | maxon::Bool | Input | false | false | false |  |  | false | 
Redshift Optimizations/Transmission/Cut-off Threshold | <com.redshift3d.redshift4c4d.nodes.core.openpbrmaterial.rs_transmission_cutoff | maxon::Float | Input | false | false | false | 0 | 1 | 0.01 | 
Redshift Optimizations/Transmission/Override Cut-off | <com.redshift3d.redshift4c4d.nodes.core.openpbrmaterial.rs_transmission_enablecutoff | maxon::Bool | Input | false | false | false |  |  | false | 
Redshift Optimizations/Transmission/Trace Depth | <com.redshift3d.redshift4c4d.nodes.core.openpbrmaterial.rs_transmission_depth | maxon::Int | Input | false | false | false | 0 | 63 | 5 | 
Outputs/outColor | >com.redshift3d.redshift4c4d.nodes.core.openpbrmaterial.outcolor | maxon::Color64 | Output | false | false | false |  |  | (0,0,0) | 

