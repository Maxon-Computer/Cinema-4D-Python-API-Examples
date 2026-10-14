# Node Template: SSS

- **Node Space ID:** `com.redshift3d.redshift4c4d.class.nodespace`
- **Template ID:** `com.redshift3d.redshift4c4d.nodes.core.subsurfacescatter`
- **Template Name:** `SSS`

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
Bump Mapping/Add Bump Input To Material Bump | <com.redshift3d.redshift4c4d.nodes.core.subsurfacescatter.additional_bump_mode | maxon::Bool | Input | false | false | false |  |  | false | 
Bump Mapping/Bump Map | <com.redshift3d.redshift4c4d.nodes.core.subsurfacescatter.bump_input | maxon::Vector64 | Input | false | false | false |  |  |  | 
Diffuse and Sub-Surface Scattering Layers/Diffuse Amount | <com.redshift3d.redshift4c4d.nodes.core.subsurfacescatter.diffuse_amount | maxon::Float | Input | false | false | false | 0 | 1 | 0 | 
Diffuse and Sub-Surface Scattering Layers/Disable Diffuse Bump Mapping | <com.redshift3d.redshift4c4d.nodes.core.subsurfacescatter.no_diffuse_bump | maxon::Bool | Input | false | false | false |  |  | false | 
Diffuse and Sub-Surface Scattering Layers/Sub-Surface/Include Mode | <com.redshift3d.redshift4c4d.nodes.core.subsurfacescatter.include_mode | maxon::Int | Input | false | false | true |  |  | 1 | All Objects = 0, Only Self = 1
Diffuse and Sub-Surface Scattering Layers/Sub-Surface/Mode | <com.redshift3d.redshift4c4d.nodes.core.subsurfacescatter.mode | maxon::Int | Input | false | false | true |  |  | 1 | Point-Based = 0, Ray-Traced = 1
Diffuse and Sub-Surface Scattering Layers/Sub-Surface/Samples | <com.redshift3d.redshift4c4d.nodes.core.subsurfacescatter.samples | maxon::Int | Input | false | false | false | 1 | 65535 | 64 | 
Diffuse and Sub-Surface Scattering Layers/Sub-Surface/Scatter Color | <com.redshift3d.redshift4c4d.nodes.core.subsurfacescatter.scatter_color | maxon::Color64 | Input | false | false | false |  |  | (0.5,0.5,0.5) | 
Diffuse and Sub-Surface Scattering Layers/Sub-Surface/Scatter Radius (cm) | <com.redshift3d.redshift4c4d.nodes.core.subsurfacescatter.scatter_radius | maxon::Float | Input | false | false | false |  |  | 2 | 
Diffuse and Sub-Surface Scattering Layers/Sub-Surface/Single Scattering/Enable | <com.redshift3d.redshift4c4d.nodes.core.subsurfacescatter.singlescatter_on | maxon::Bool | Input | false | false | false |  |  | false | 
Diffuse and Sub-Surface Scattering Layers/Sub-Surface/Single Scattering/Override Coefficients | <com.redshift3d.redshift4c4d.nodes.core.subsurfacescatter.ss_overridecoeffs | maxon::Bool | Input | false | false | false |  |  | false | 
Diffuse and Sub-Surface Scattering Layers/Sub-Surface/Single Scattering/Phase | <com.redshift3d.redshift4c4d.nodes.core.subsurfacescatter.phase | maxon::Float | Input | false | false | false | -1 | 1 | 0 | 
Diffuse and Sub-Surface Scattering Layers/Sub-Surface/Single Scattering/Samples | <com.redshift3d.redshift4c4d.nodes.core.subsurfacescatter.ss_samples | maxon::Int | Input | false | false | false | 1 | 65535 | 16 | 
Diffuse and Sub-Surface Scattering Layers/Sub-Surface/Single Scattering/Scatter Amount | <com.redshift3d.redshift4c4d.nodes.core.subsurfacescatter.ss_amount | maxon::Float | Input | false | false | false | 0 | 65535 | 0 | 
Diffuse and Sub-Surface Scattering Layers/Sub-Surface/Single Scattering/Thickness (cm) | <com.redshift3d.redshift4c4d.nodes.core.subsurfacescatter.ss_thickness | maxon::Float | Input | false | false | false | 0 | 65535 | 0 | 
Diffuse and Sub-Surface Scattering Layers/Sub-Surface/Single Scattering/Transmittance | <com.redshift3d.redshift4c4d.nodes.core.subsurfacescatter.ss_transmittance | maxon::Color64 | Input | false | false | false |  |  | (1,1,1) | 
Diffuse and Sub-Surface Scattering Layers/Sub-Surface/Sub-Surface Color | <com.redshift3d.redshift4c4d.nodes.core.subsurfacescatter.sub_surface_color | maxon::Color64 | Input | false | false | false |  |  | (0.5,0.5,0.5) | 
General Parameters/IOR | <com.redshift3d.redshift4c4d.nodes.core.subsurfacescatter.ior | maxon::Float | Input | false | false | false | 0 | 4 | 1.3 | 
General Parameters/Preset | <com.redshift3d.redshift4c4d.nodes.core.subsurfacescatter.preset | maxon::Int | Input | false | false | true |  |  | 0 | Custom = 0, Skin (brown) = 1, Skin (pink) = 2, Skin (yellow) = 3, Milk (skimmed) = 4, Milk (whole) = 5, Marble (white) = 6, Ketchup = 7, Cream = 8, Potato = 9, Spectralon = 10
General Parameters/Scale | <com.redshift3d.redshift4c4d.nodes.core.subsurfacescatter.scale | maxon::Float | Input | false | false | false | 0 | 100000 | 100 | 
Optimizations/Disable Single Scattering Transparency | <com.redshift3d.redshift4c4d.nodes.core.subsurfacescatter.ss_notransparency | maxon::Bool | Input | false | false | false |  |  | true | 
Optimizations/Enable Trace Depth Overrides | <com.redshift3d.redshift4c4d.nodes.core.subsurfacescatter.depth_override | maxon::Bool | Input | false | false | false |  |  | false | 
Optimizations/Reflection/Cut-off Override/Enable | <com.redshift3d.redshift4c4d.nodes.core.subsurfacescatter.refl_enablecutoff | maxon::Bool | Input | false | false | false |  |  | false | 
Optimizations/Reflection/Cut-off Override/Threshold | <com.redshift3d.redshift4c4d.nodes.core.subsurfacescatter.refl_cutoff | maxon::Float | Input | false | false | false | 0 | 1 | 0.01 | 
Optimizations/Reflection/Max Trace Depth | <com.redshift3d.redshift4c4d.nodes.core.subsurfacescatter.refl_depth | maxon::Int | Input | false | false | false | 0 | 63 | 3 | 
Optimizations/Reflection/Specular Highlights Only | <com.redshift3d.redshift4c4d.nodes.core.subsurfacescatter.refl_hl_only | maxon::Bool | Input | false | false | false |  |  | false | 
Optimizations/Reflection/Turn off Weak Internal Reflections | <com.redshift3d.redshift4c4d.nodes.core.subsurfacescatter.skip_inside_refl | maxon::Bool | Input | false | false | false |  |  | true | 
Optimizations/Single Scatter Refraction/Cut-off Override/Enable | <com.redshift3d.redshift4c4d.nodes.core.subsurfacescatter.refr_enablecutoff | maxon::Bool | Input | false | false | false |  |  | false | 
Optimizations/Single Scatter Refraction/Cut-off Override/Threshold | <com.redshift3d.redshift4c4d.nodes.core.subsurfacescatter.refr_cutoff | maxon::Float | Input | false | false | false | 0 | 1 | 0.01 | 
Optimizations/Single Scatter Refraction/Max Trace Depth | <com.redshift3d.redshift4c4d.nodes.core.subsurfacescatter.refr_depth | maxon::Int | Input | false | false | false | 0 | 63 | 1 | 
Reflections/General/BRDF | <com.redshift3d.redshift4c4d.nodes.core.subsurfacescatter.refl_brdf | maxon::Int | Input | false | false | true |  |  | 0 | Beckmann (Cook-Torrance) = 0, GGX = 1, Ashikhmin-Shirley = 2
Reflections/General/Color | <com.redshift3d.redshift4c4d.nodes.core.subsurfacescatter.refl_color | maxon::Color64 | Input | false | false | false |  |  | (1,1,1) | 
Reflections/General/Disable Reflection Bump Mapping | <com.redshift3d.redshift4c4d.nodes.core.subsurfacescatter.no_refl_bump | maxon::Bool | Input | false | false | false |  |  | false | 
Reflections/General/Fresnel/Curve Falloff | <com.redshift3d.redshift4c4d.nodes.core.subsurfacescatter.refl_fresnel_curve | maxon::Float | Input | false | false | false | 0.1 | 1000 | 5 | 
Reflections/General/Fresnel/Enable | <com.redshift3d.redshift4c4d.nodes.core.subsurfacescatter.enablefresnel | maxon::Bool | Input | false | false | false |  |  | true | 
Reflections/General/Fresnel/Facing Reflectivity | <com.redshift3d.redshift4c4d.nodes.core.subsurfacescatter.refl_fresnel_0_degree_refl | maxon::Float | Input | false | false | false | 0 | 1 | 0.2 | 
Reflections/General/Fresnel/Perpendicular Reflectivity | <com.redshift3d.redshift4c4d.nodes.core.subsurfacescatter.refl_fresnel_90_degree_refl | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Reflections/General/Fresnel/Use Index of Refraction | <com.redshift3d.redshift4c4d.nodes.core.subsurfacescatter.refl_fresnel_useior | maxon::Bool | Input | false | false | false |  |  | true | 
Reflections/General/Glossiness | <com.redshift3d.redshift4c4d.nodes.core.subsurfacescatter.refl_gloss | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Reflections/General/Samples | <com.redshift3d.redshift4c4d.nodes.core.subsurfacescatter.refl_gloss_samples | maxon::Int | Input | false | false | false | 0 | 65535 | 8 | 
Reflections/General/Weight | <com.redshift3d.redshift4c4d.nodes.core.subsurfacescatter.reflectivity | maxon::Float | Input | false | false | false | 0 | 1 | 0.1 | 
Outputs/outColor | >com.redshift3d.redshift4c4d.nodes.core.subsurfacescatter.outcolor | maxon::Color64 | Output | false | false | false |  |  | (0,0,0) | 

