# Node Template: Architectural

- **Node Space ID:** `com.redshift3d.redshift4c4d.class.nodespace`
- **Template ID:** `com.redshift3d.redshift4c4d.nodes.core.architectural`
- **Template Name:** `Architectural`

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
Ambient Occlusion/Ambient Color | <com.redshift3d.redshift4c4d.nodes.core.architectural.ao_ambient | maxon::Color64 | Input | false | false | false |  |  | (1,1,1) | 
Ambient Occlusion/Apply Camera Exposure Compensation | <com.redshift3d.redshift4c4d.nodes.core.architectural.ao_compensateforexposure | maxon::Bool | Input | false | false | false |  |  | true | 
Ambient Occlusion/Apply To Incandescence | <com.redshift3d.redshift4c4d.nodes.core.architectural.ao_applytoincandescence | maxon::Bool | Input | false | false | false |  |  | true | 
Ambient Occlusion/Combine Mode | <com.redshift3d.redshift4c4d.nodes.core.architectural.ao_combinemode | maxon::Int | Input | false | false | true |  |  | 1 | Add = 0, Multiply = 1
Ambient Occlusion/Enable | <com.redshift3d.redshift4c4d.nodes.core.architectural.ao_on | maxon::Bool | Input | false | false | false |  |  | false | 
Ambient Occlusion/Falloff | <com.redshift3d.redshift4c4d.nodes.core.architectural.ao_falloff | maxon::Float | Input | false | false | false | 0 | 65536 | 1 | 
Ambient Occlusion/Invert Normal | <com.redshift3d.redshift4c4d.nodes.core.architectural.ao_invert | maxon::Bool | Input | false | false | false |  |  | false | 
Ambient Occlusion/Max Distance | <com.redshift3d.redshift4c4d.nodes.core.architectural.ao_distance | maxon::Float | Input | false | false | false |  |  | 0 | 
Ambient Occlusion/Samples | <com.redshift3d.redshift4c4d.nodes.core.architectural.ao_samples | maxon::Int | Input | false | false | false | 0 | 65535 | 16 | 
Ambient Occlusion/Shadow Color | <com.redshift3d.redshift4c4d.nodes.core.architectural.ao_dark | maxon::Color64 | Input | false | false | false |  |  | (0.2,0.2,0.2) | 
Ambient Occlusion/Spread | <com.redshift3d.redshift4c4d.nodes.core.architectural.ao_spread | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Illumination/Diffuse/Color | <com.redshift3d.redshift4c4d.nodes.core.architectural.diffuse | maxon::Color64 | Input | false | false | false |  |  | (0.5,0.5,0.5) | 
Illumination/Diffuse/Disable Diffuse Bump Mapping | <com.redshift3d.redshift4c4d.nodes.core.architectural.no_diffuse_bump | maxon::Bool | Input | false | false | false |  |  | false | 
Illumination/Diffuse/Roughness | <com.redshift3d.redshift4c4d.nodes.core.architectural.diffuse_roughness | maxon::Float | Input | false | false | false | 0 | 1 | 0 | 
Illumination/Diffuse/Weight | <com.redshift3d.redshift4c4d.nodes.core.architectural.diffuse_weight | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Illumination/Translucency/Color | <com.redshift3d.redshift4c4d.nodes.core.architectural.refr_trans_color | maxon::Color64 | Input | false | false | false |  |  | (0.5,0.5,0.5) | 
Illumination/Translucency/Enable | <com.redshift3d.redshift4c4d.nodes.core.architectural.refr_translucency | maxon::Bool | Input | false | false | false |  |  | false | 
Illumination/Translucency/Weight | <com.redshift3d.redshift4c4d.nodes.core.architectural.refr_trans_weight | maxon::Float | Input | false | false | false | 0 | 1 | 0 | 
Miscellaneous/Add Bump Input To Material Bump | <com.redshift3d.redshift4c4d.nodes.core.architectural.additional_bump_mode | maxon::Bool | Input | false | false | false |  |  | false | 
Miscellaneous/Bump Map | <com.redshift3d.redshift4c4d.nodes.core.architectural.bump_input | maxon::Vector64 | Input | false | false | false |  |  |  | 
Miscellaneous/Cutout Opacity | <com.redshift3d.redshift4c4d.nodes.core.architectural.cutout_opacity | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Miscellaneous/Incandescence/Color | <com.redshift3d.redshift4c4d.nodes.core.architectural.additional_color | maxon::Color64 | Input | false | false | false |  |  | (0,0,0) | 
Miscellaneous/Incandescence/Scale | <com.redshift3d.redshift4c4d.nodes.core.architectural.incandescent_scale | maxon::Float | Input | false | false | false | 0 | 1000000 | 1 | 
Miscellaneous/Propagate Background Alpha Channel | <com.redshift3d.redshift4c4d.nodes.core.architectural.propagate_alpha | maxon::Bool | Input | false | false | false |  |  | true | 
Optimizations/Enable Trace Depth Overrides | <com.redshift3d.redshift4c4d.nodes.core.architectural.depth_override | maxon::Bool | Input | false | false | false |  |  | false | 
Optimizations/Reflection/Cut-off Override/Enable | <com.redshift3d.redshift4c4d.nodes.core.architectural.refl_enablecutoff | maxon::Bool | Input | false | false | false |  |  | false | 
Optimizations/Reflection/Cut-off Override/Threshold | <com.redshift3d.redshift4c4d.nodes.core.architectural.refl_cutoff | maxon::Float | Input | false | false | false | 0 | 1 | 0.01 | 
Optimizations/Reflection/Max Trace Depth | <com.redshift3d.redshift4c4d.nodes.core.architectural.refl_depth | maxon::Int | Input | false | false | false | 0 | 63 | 3 | 
Optimizations/Reflection/Specular Highlights Only | <com.redshift3d.redshift4c4d.nodes.core.architectural.refl_hl_only | maxon::Bool | Input | false | false | false |  |  | false | 
Optimizations/Reflection/Turn off Weak Internal Reflections | <com.redshift3d.redshift4c4d.nodes.core.architectural.skip_inside_refl | maxon::Bool | Input | false | false | false |  |  | true | 
Optimizations/Refraction/Cut-off Override/Enable | <com.redshift3d.redshift4c4d.nodes.core.architectural.refr_enablecutoff | maxon::Bool | Input | false | false | false |  |  | false | 
Optimizations/Refraction/Cut-off Override/Threshold | <com.redshift3d.redshift4c4d.nodes.core.architectural.refr_cutoff | maxon::Float | Input | false | false | false | 0 | 1 | 0.01 | 
Optimizations/Refraction/Max Combined Trace Depth | <com.redshift3d.redshift4c4d.nodes.core.architectural.combined_depth | maxon::Int | Input | false | false | false | 0 | 63 | 6 | 
Optimizations/Refraction/Max Trace Depth | <com.redshift3d.redshift4c4d.nodes.core.architectural.refr_depth | maxon::Int | Input | false | false | false | 0 | 63 | 5 | 
Reflection/Common Parameters/Anisotropy/Amount | <com.redshift3d.redshift4c4d.nodes.core.architectural.anisotropy | maxon::Float | Input | false | false | false | -1 | 1 | 0 | 
Reflection/Common Parameters/Anisotropy/Rotation | <com.redshift3d.redshift4c4d.nodes.core.architectural.anisotropy_rotation | maxon::Float | Input | false | false | false | 0 | 1 | 0 | 
Reflection/Common Parameters/Anisotropy/Surface Orientation | <com.redshift3d.redshift4c4d.nodes.core.architectural.anisotropy_orientation | maxon::Int | Input | false | false | true |  |  | 2 | None = 2, From Tangent Channel = 1
Reflection/Common Parameters/Anisotropy/Tangent Channel | <com.redshift3d.redshift4c4d.nodes.core.architectural.anisotropy_tangentchannel | maxon::String | Input | false | false | false |  |  |  | 
Reflection/Common Parameters/Anisotropy/UV Channel | <com.redshift3d.redshift4c4d.nodes.core.architectural.anisotropy_uvchannel | maxon::String | Input | false | false | false |  |  |  | 
Reflection/Common Parameters/Highlight vs Reflection Balance | <com.redshift3d.redshift4c4d.nodes.core.architectural.hl_vs_refl_balance | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Reflection/Common Parameters/Metal Material | <com.redshift3d.redshift4c4d.nodes.core.architectural.refl_is_metal | maxon::Bool | Input | false | false | false |  |  | false | 
Reflection/Primary Reflection/BRDF | <com.redshift3d.redshift4c4d.nodes.core.architectural.refl_brdf | maxon::Int | Input | false | false | true |  |  | 0 | Beckmann (Cook-Torrance) = 0, Ashikhmin-Shirley (legacy) = 65536, GGX = 1, Ashikhmin-Shirley = 2
Reflection/Primary Reflection/Color | <com.redshift3d.redshift4c4d.nodes.core.architectural.refl_color | maxon::Color64 | Input | false | false | false |  |  | (1,1,1) | 
Reflection/Primary Reflection/Disable Bump Mapping | <com.redshift3d.redshift4c4d.nodes.core.architectural.no_refl0_bump | maxon::Bool | Input | false | false | false |  |  | false | 
Reflection/Primary Reflection/Fresnel/Curve Falloff | <com.redshift3d.redshift4c4d.nodes.core.architectural.brdf_curve | maxon::Float | Input | false | false | false | 0.1 | 1000 | 5 | 
Reflection/Primary Reflection/Fresnel/Extinction Coefficient (k) | <com.redshift3d.redshift4c4d.nodes.core.architectural.brdf_extinction_coeff | maxon::Float | Input | false | false | false | 0 | 100 | 0 | 
Reflection/Primary Reflection/Fresnel/Facing Reflectivity | <com.redshift3d.redshift4c4d.nodes.core.architectural.brdf_0_degree_refl | maxon::Float | Input | false | false | false | 0 | 1 | 0.2 | 
Reflection/Primary Reflection/Fresnel/IOR | <com.redshift3d.redshift4c4d.nodes.core.architectural.brdf_fresnel_ior | maxon::Float | Input | false | false | false | 0 | 20 | 1.4 | 
Reflection/Primary Reflection/Fresnel/Lock to Refraction IOR | <com.redshift3d.redshift4c4d.nodes.core.architectural.brdf_fresnel_lockior | maxon::Bool | Input | false | false | false |  |  | true | 
Reflection/Primary Reflection/Fresnel/Medium Type | <com.redshift3d.redshift4c4d.nodes.core.architectural.brdf_fresnel_type | maxon::Int | Input | false | false | true |  |  | 0 | Dielectric = 0, Conductor = 1
Reflection/Primary Reflection/Fresnel/Perpendicular Reflectivity | <com.redshift3d.redshift4c4d.nodes.core.architectural.brdf_90_degree_refl | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Reflection/Primary Reflection/Fresnel/Use Index of Refraction | <com.redshift3d.redshift4c4d.nodes.core.architectural.brdf_fresnel | maxon::Bool | Input | false | false | false |  |  | true | 
Reflection/Primary Reflection/Glossiness | <com.redshift3d.redshift4c4d.nodes.core.architectural.refl_gloss | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Reflection/Primary Reflection/Samples | <com.redshift3d.redshift4c4d.nodes.core.architectural.refl_gloss_samples | maxon::Int | Input | false | false | false | 0 | 65535 | 8 | 
Reflection/Primary Reflection/Weight | <com.redshift3d.redshift4c4d.nodes.core.architectural.reflectivity | maxon::Float | Input | false | false | false | 0 | 1 | 0.6 | 
Refraction/Fog/Distance (cm) | <com.redshift3d.redshift4c4d.nodes.core.architectural.refr_falloff_dist | maxon::Float | Input | false | false | false |  |  | 0 | 
Refraction/Fog/Enable | <com.redshift3d.redshift4c4d.nodes.core.architectural.refr_falloff_on | maxon::Bool | Input | false | false | false |  |  | false | 
Refraction/Fog/End Color | <com.redshift3d.redshift4c4d.nodes.core.architectural.refr_falloff_color | maxon::Color64 | Input | false | false | false |  |  | (0,0,0) | 
Refraction/Fog/Use End Color | <com.redshift3d.redshift4c4d.nodes.core.architectural.refr_falloff_color_on | maxon::Bool | Input | false | false | false |  |  | false | 
Refraction/Refraction/Allow Global Volume Scattering | <com.redshift3d.redshift4c4d.nodes.core.architectural.global_vol_scatter | maxon::Bool | Input | false | false | false |  |  | true | 
Refraction/Refraction/Color | <com.redshift3d.redshift4c4d.nodes.core.architectural.refr_color | maxon::Color64 | Input | false | false | false |  |  | (1,1,1) | 
Refraction/Refraction/Disable Bump Mapping | <com.redshift3d.redshift4c4d.nodes.core.architectural.no_refr_bump | maxon::Bool | Input | false | false | false |  |  | false | 
Refraction/Refraction/Enable Refractive Caustics | <com.redshift3d.redshift4c4d.nodes.core.architectural.do_refractive_caustics | maxon::Bool | Input | false | false | false |  |  | false | 
Refraction/Refraction/Glossiness | <com.redshift3d.redshift4c4d.nodes.core.architectural.refr_gloss | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Refraction/Refraction/Index of Refraction | <com.redshift3d.redshift4c4d.nodes.core.architectural.refr_ior | maxon::Float | Input | false | false | false | 0 | 100 | 1.4 | 
Refraction/Refraction/Samples | <com.redshift3d.redshift4c4d.nodes.core.architectural.refr_gloss_samples | maxon::Int | Input | false | false | false | 0 | 65535 | 8 | 
Refraction/Refraction/Thin Walled | <com.redshift3d.redshift4c4d.nodes.core.architectural.thin_walled | maxon::Bool | Input | false | false | false |  |  | false | 
Refraction/Refraction/Weight | <com.redshift3d.redshift4c4d.nodes.core.architectural.transparency | maxon::Float | Input | false | false | false | 0 | 1 | 0 | 
Secondary Reflection/Secondary Reflection/BRDF | <com.redshift3d.redshift4c4d.nodes.core.architectural.refl_base_brdf | maxon::Int | Input | false | false | true |  |  | 0 | Beckmann (Cook-Torrance) = 0, Ashikhmin-Shirley (legacy) = 65536, GGX = 1, Ashikhmin-Shirley = 2
Secondary Reflection/Secondary Reflection/Color | <com.redshift3d.redshift4c4d.nodes.core.architectural.refl_base_color | maxon::Color64 | Input | false | false | false |  |  | (1,0.3,0) | 
Secondary Reflection/Secondary Reflection/Disable Bump Mapping | <com.redshift3d.redshift4c4d.nodes.core.architectural.no_refl1_bump | maxon::Bool | Input | false | false | false |  |  | false | 
Secondary Reflection/Secondary Reflection/Fresnel/Curve Falloff | <com.redshift3d.redshift4c4d.nodes.core.architectural.brdf_base_curve | maxon::Float | Input | false | false | false | 0.1 | 1000 | 5 | 
Secondary Reflection/Secondary Reflection/Fresnel/Extinction Coefficient (k) | <com.redshift3d.redshift4c4d.nodes.core.architectural.brdf_base_extinction_coeff | maxon::Float | Input | false | false | false | 0 | 100 | 0 | 
Secondary Reflection/Secondary Reflection/Fresnel/Facing Reflectivity | <com.redshift3d.redshift4c4d.nodes.core.architectural.brdf_base_0_degree_refl | maxon::Float | Input | false | false | false | 0 | 1 | 0.2 | 
Secondary Reflection/Secondary Reflection/Fresnel/IOR | <com.redshift3d.redshift4c4d.nodes.core.architectural.brdf_base_fresnel_ior | maxon::Float | Input | false | false | false | 1 | 20 | 1.4 | 
Secondary Reflection/Secondary Reflection/Fresnel/Lock to Refraction IOR | <com.redshift3d.redshift4c4d.nodes.core.architectural.brdf_base_fresnel_lockior | maxon::Bool | Input | false | false | false |  |  | true | 
Secondary Reflection/Secondary Reflection/Fresnel/Medium Type | <com.redshift3d.redshift4c4d.nodes.core.architectural.brdf_base_fresnel_type | maxon::Int | Input | false | false | true |  |  | 0 | Dielectric = 0, Conductor = 1
Secondary Reflection/Secondary Reflection/Fresnel/Perpendicular Reflectivity | <com.redshift3d.redshift4c4d.nodes.core.architectural.brdf_base_90_degree_refl | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Secondary Reflection/Secondary Reflection/Fresnel/Use Index of Refraction | <com.redshift3d.redshift4c4d.nodes.core.architectural.brdf_base_fresnel | maxon::Bool | Input | false | false | false |  |  | true | 
Secondary Reflection/Secondary Reflection/Glossiness | <com.redshift3d.redshift4c4d.nodes.core.architectural.refl_base_gloss | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Secondary Reflection/Secondary Reflection/Samples | <com.redshift3d.redshift4c4d.nodes.core.architectural.refl_base_gloss_samples | maxon::Int | Input | false | false | false | 0 | 65535 | 8 | 
Secondary Reflection/Secondary Reflection/Weight | <com.redshift3d.redshift4c4d.nodes.core.architectural.refl_base | maxon::Float | Input | false | false | false | 0 | 1 | 0 | 
Outputs/outColor | >com.redshift3d.redshift4c4d.nodes.core.architectural.outcolor | maxon::Color64 | Output | false | false | false |  |  | (0,0,0) | 

