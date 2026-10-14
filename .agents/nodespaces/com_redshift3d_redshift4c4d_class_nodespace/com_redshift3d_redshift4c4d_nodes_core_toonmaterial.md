# Node Template: Toon Material

- **Node Space ID:** `com.redshift3d.redshift4c4d.class.nodespace`
- **Template ID:** `com.redshift3d.redshift4c4d.nodes.core.toonmaterial`
- **Template Name:** `Toon Material`

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
Advanced/Base Indirect Scale | <com.redshift3d.redshift4c4d.nodes.core.toonmaterial.base_indirect | maxon::Float | Input | false | false | false | 0 | 1 | 0 | 
Advanced/Base Shadow Opacity | <com.redshift3d.redshift4c4d.nodes.core.toonmaterial.base_shadow_opacity | maxon::Float | Input | false | false | false | -1 | 1 | 0 | 
Advanced/Energy Compensation Mode | <com.redshift3d.redshift4c4d.nodes.core.toonmaterial.energy_comp_mode | maxon::Int | Input | false | false | true |  |  | 1 | None = 0, Use Fresnel = 1, No Fresnel = 2
Advanced/Reflection End Color | <com.redshift3d.redshift4c4d.nodes.core.toonmaterial.refl_endmode | maxon::Int | Input | false | false | true |  |  | 1 | Environment = 0, Base = 1
Advanced/Reflection Indirect Scale | <com.redshift3d.redshift4c4d.nodes.core.toonmaterial.refl_indirect | maxon::Float | Input | false | false | false | 0 | 1 | 0 | 
Advanced/Reflection Shadow Opacity | <com.redshift3d.redshift4c4d.nodes.core.toonmaterial.refl_shadow_opacity | maxon::Float | Input | false | false | false | -1 | 1 | 0 | 
Advanced/Semi-Transparency Rays Include Self | <com.redshift3d.redshift4c4d.nodes.core.toonmaterial.trans_include_self | maxon::Bool | Input | false | false | false |  |  | true | 
Advanced/UV Context | <com.redshift3d.redshift4c4d.nodes.core.toonmaterial.uv_context | RSC4D::UVContext | Input | false | false | false |  |  |  | 
General Properties/Base/Color | <com.redshift3d.redshift4c4d.nodes.core.toonmaterial.base_color | maxon::Color64 | Input | false | false | false |  |  | (1,1,1) | 
General Properties/Base/Tonemap | <com.redshift3d.redshift4c4d.nodes.core.toonmaterial.base_tone_map | maxon::Color64 | Input | false | false | false |  |  |  | 
General Properties/Base/Tonemap Mode | <com.redshift3d.redshift4c4d.nodes.core.toonmaterial.base_tone_map_mode | maxon::Int | Input | false | false | true |  |  | 1 | Light and Shadow = 0, Light and Opaque Shadow = 1
General Properties/Base/Weight | <com.redshift3d.redshift4c4d.nodes.core.toonmaterial.base_weight | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
General Properties/Emission/Color | <com.redshift3d.redshift4c4d.nodes.core.toonmaterial.emission_color | maxon::Color64 | Input | false | false | false |  |  | (1,1,1) | 
General Properties/Emission/Radiance (W/sr/m^2) | <com.redshift3d.redshift4c4d.nodes.core.toonmaterial.emission_weight | maxon::Float | Input | false | false | false |  |  | 0 | 
General Properties/Geometry/Bump Map | <com.redshift3d.redshift4c4d.nodes.core.toonmaterial.bump_input | maxon::Vector64 | Input | false | false | false |  |  |  | 
General Properties/Geometry/Opacity | <com.redshift3d.redshift4c4d.nodes.core.toonmaterial.opacity_color | maxon::Color64 | Input | false | false | false |  |  | (1,1,1) | 
General Properties/Geometry/Opacity Affects Emission | <com.redshift3d.redshift4c4d.nodes.core.toonmaterial.opacity_affects_emission | maxon::Bool | Input | false | false | false |  |  | true | 
General Properties/Geometry/Opacity Affects Reflection | <com.redshift3d.redshift4c4d.nodes.core.toonmaterial.opacity_affects_refl | maxon::Bool | Input | false | false | false |  |  | true | 
General Properties/Geometry/Opacity Affects Rim | <com.redshift3d.redshift4c4d.nodes.core.toonmaterial.opacity_affects_rim | maxon::Bool | Input | false | false | false |  |  | true | 
General Properties/Reflection/Color | <com.redshift3d.redshift4c4d.nodes.core.toonmaterial.refl_color | maxon::Color64 | Input | false | false | false |  |  | (1,1,1) | 
General Properties/Reflection/Fresnel Enabled | <com.redshift3d.redshift4c4d.nodes.core.toonmaterial.refl_use_fresnel | maxon::Bool | Input | false | false | false |  |  | true | 
General Properties/Reflection/IOR | <com.redshift3d.redshift4c4d.nodes.core.toonmaterial.refl_ior | maxon::Float | Input | false | false | false | 0 | 32 | 1.5 | 
General Properties/Reflection/Light List | <com.redshift3d.redshift4c4d.nodes.core.toonmaterial.refl_light_list | maxon::DataDictionary | Input | false | false | false |  |  |  | 
General Properties/Reflection/Roughness/Width | <com.redshift3d.redshift4c4d.nodes.core.toonmaterial.refl_roughness | maxon::Float | Input | false | false | false | 0 | 1 | 0.2 | 
General Properties/Reflection/Samples | <com.redshift3d.redshift4c4d.nodes.core.toonmaterial.refl_samples | maxon::Int | Input | false | false | false | 0 | 65535 | 16 | 
General Properties/Reflection/Tonemap | <com.redshift3d.redshift4c4d.nodes.core.toonmaterial.refl_tone_map | maxon::Color64 | Input | false | false | false |  |  |  | 
General Properties/Reflection/Tonemap Layer Mask | <com.redshift3d.redshift4c4d.nodes.core.toonmaterial.refl_mask_tone_map | maxon::Color64 | Input | false | false | false |  |  |  | 
General Properties/Reflection/Tonemap Mode | <com.redshift3d.redshift4c4d.nodes.core.toonmaterial.refl_tone_map_mode | maxon::Int | Input | false | false | true |  |  | 1 | Light and Shadow = 0, Light and Opaque Shadow = 1, Stylized = 2
General Properties/Reflection/Weight | <com.redshift3d.redshift4c4d.nodes.core.toonmaterial.refl_weight | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
General Properties/Rim/Color | <com.redshift3d.redshift4c4d.nodes.core.toonmaterial.rim_color | maxon::Color64 | Input | false | false | false |  |  | (1,1,1) | 
General Properties/Rim/Light | <com.redshift3d.redshift4c4d.nodes.core.toonmaterial.rim_light_list | maxon::DataDictionary | Input | false | false | false |  |  |  | 
General Properties/Rim/Softness | <com.redshift3d.redshift4c4d.nodes.core.toonmaterial.rim_softness | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
General Properties/Rim/Spread | <com.redshift3d.redshift4c4d.nodes.core.toonmaterial.rim_spread | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
General Properties/Rim/Tonemap | <com.redshift3d.redshift4c4d.nodes.core.toonmaterial.rim_tone_map | maxon::Color64 | Input | false | false | false |  |  |  | 
General Properties/Rim/Weight | <com.redshift3d.redshift4c4d.nodes.core.toonmaterial.rim_weight | maxon::Float | Input | false | false | false | 0 | 1 | 0 | 
General Properties/Rim/Width | <com.redshift3d.redshift4c4d.nodes.core.toonmaterial.rim_width | maxon::Float | Input | false | false | false | 0 | 1 | 0.2 | 
Optimizations/Enable Trace Depth Overrides | <com.redshift3d.redshift4c4d.nodes.core.toonmaterial.depth_override | maxon::Bool | Input | false | false | false |  |  | false | 
Optimizations/Reflection/Cut-off Override Enable | <com.redshift3d.redshift4c4d.nodes.core.toonmaterial.refl_enablecutoff | maxon::Bool | Input | false | false | false |  |  | false | 
Optimizations/Reflection/Cut-off Threshold | <com.redshift3d.redshift4c4d.nodes.core.toonmaterial.refl_cutoff | maxon::Float | Input | false | false | false | 0 | 1 | 0.01 | 
Optimizations/Reflection/Trace Depth | <com.redshift3d.redshift4c4d.nodes.core.toonmaterial.refl_depth | maxon::Int | Input | false | false | false | 0 | 63 | 3 | 
Outputs/outColor | >com.redshift3d.redshift4c4d.nodes.core.toonmaterial.outcolor | maxon::Color64 | Output | false | false | false |  |  | (0,0,0) | 

