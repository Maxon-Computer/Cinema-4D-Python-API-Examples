# Node Template: Car Paint

- **Node Space ID:** `com.redshift3d.redshift4c4d.class.nodespace`
- **Template ID:** `com.redshift3d.redshift4c4d.nodes.core.carpaint`
- **Template Name:** `Car Paint`

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
Advanced/Bump/Add Bump Input To Material Bump | <com.redshift3d.redshift4c4d.nodes.core.carpaint.additional_bump_mode | maxon::Bool | Input | false | false | false |  |  | false | 
Advanced/Bump/Bump Map | <com.redshift3d.redshift4c4d.nodes.core.carpaint.bump_input | maxon::Vector64 | Input | false | false | false |  |  |  | 
Advanced/Bump/Disable Base Layer Bump Mapping | <com.redshift3d.redshift4c4d.nodes.core.carpaint.no_baselayer_bump | maxon::Bool | Input | false | false | false |  |  | false | 
Advanced/Bump/Disable Clear Coat Bump Mapping | <com.redshift3d.redshift4c4d.nodes.core.carpaint.no_clearcoat_bump | maxon::Bool | Input | false | false | false |  |  | false | 
Advanced/Cut-off Override/Enable | <com.redshift3d.redshift4c4d.nodes.core.carpaint.refl_enablecutoff | maxon::Bool | Input | false | false | false |  |  | false | 
Advanced/Cut-off Override/Threshold | <com.redshift3d.redshift4c4d.nodes.core.carpaint.refl_cutoff | maxon::Float | Input | false | false | false | 0 | 1 | 0.005 | 
Advanced/Enable Trace Depth Overrides | <com.redshift3d.redshift4c4d.nodes.core.carpaint.depth_override | maxon::Bool | Input | false | false | false |  |  | false | 
Advanced/Max Reflection Trace Depth | <com.redshift3d.redshift4c4d.nodes.core.carpaint.refl_depth | maxon::Int | Input | false | false | false | 0 | 63 | 3 | 
Base Layer Diffuse/Edge Falloff/Color | <com.redshift3d.redshift4c4d.nodes.core.carpaint.edge_color | maxon::Color64 | Input | false | false | false |  |  | (0,0,0) | 
Base Layer Diffuse/Edge Falloff/Curve Factor | <com.redshift3d.redshift4c4d.nodes.core.carpaint.edge_color_bias | maxon::Float | Input | false | false | false | 0 | 1000 | 0.9 | 
Base Layer Diffuse/Pigment Color | <com.redshift3d.redshift4c4d.nodes.core.carpaint.base_color | maxon::Color64 | Input | false | false | false |  |  | (0.8,0.1,0) | 
Base Layer Diffuse/Weight | <com.redshift3d.redshift4c4d.nodes.core.carpaint.diffuse_weight | maxon::Float | Input | false | false | false |  |  | 0.5 | 
Base Layer Specular/Fresnel Control/Curve Factor | <com.redshift3d.redshift4c4d.nodes.core.carpaint.spec_curvefactor | maxon::Float | Input | false | false | false | 0.1 | 1000 | 5 | 
Base Layer Specular/Fresnel Control/Facing Reflectivity | <com.redshift3d.redshift4c4d.nodes.core.carpaint.spec_facingweight | maxon::Float | Input | false | false | false | 0 | 1 | 0.1 | 
Base Layer Specular/Fresnel Control/Perpendicular Reflectivity | <com.redshift3d.redshift4c4d.nodes.core.carpaint.spec_perpweight | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Base Layer Specular/General/BRDF | <com.redshift3d.redshift4c4d.nodes.core.carpaint.spec_brdf | maxon::Int | Input | false | false | true |  |  | 0 | Beckmann (Cook-Torrance) = 0, Ashikhmin-Shirley (legacy) = 65536, GGX = 1, Ashikhmin-Shirley = 2
Base Layer Specular/General/Color | <com.redshift3d.redshift4c4d.nodes.core.carpaint.spec_color | maxon::Color64 | Input | false | false | false |  |  | (1,1,1) | 
Base Layer Specular/General/Glossiness | <com.redshift3d.redshift4c4d.nodes.core.carpaint.spec_gloss | maxon::Float | Input | false | false | false | 0 | 1 | 0.2 | 
Base Layer Specular/General/Highlights Only | <com.redshift3d.redshift4c4d.nodes.core.carpaint.spec_norefl | maxon::Bool | Input | false | false | false |  |  | false | 
Base Layer Specular/General/Samples | <com.redshift3d.redshift4c4d.nodes.core.carpaint.spec_samples | maxon::Int | Input | false | false | false | 0 | 65535 | 32 | 
Base Layer Specular/General/Weight | <com.redshift3d.redshift4c4d.nodes.core.carpaint.spec_weight | maxon::Float | Input | false | false | false |  |  | 0.3 | 
Clear Coat Reflection/Fresnel Control/Curve Factor | <com.redshift3d.redshift4c4d.nodes.core.carpaint.clearcoat_curvefactor | maxon::Float | Input | false | false | false | 0.1 | 1000 | 7 | 
Clear Coat Reflection/Fresnel Control/Facing Reflectivity | <com.redshift3d.redshift4c4d.nodes.core.carpaint.clearcoat_facingweight | maxon::Float | Input | false | false | false | 0 | 1 | 0.05 | 
Clear Coat Reflection/Fresnel Control/Perpendicular Reflectivity | <com.redshift3d.redshift4c4d.nodes.core.carpaint.clearcoat_perpweight | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Clear Coat Reflection/General/BRDF | <com.redshift3d.redshift4c4d.nodes.core.carpaint.clearcoat_brdf | maxon::Int | Input | false | false | true |  |  | 0 | Beckmann (Cook-Torrance) = 0, Ashikhmin-Shirley (legacy) = 65536, GGX = 1, Ashikhmin-Shirley = 2
Clear Coat Reflection/General/Color | <com.redshift3d.redshift4c4d.nodes.core.carpaint.clearcoat_color | maxon::Color64 | Input | false | false | false |  |  | (1,1,1) | 
Clear Coat Reflection/General/Glossiness | <com.redshift3d.redshift4c4d.nodes.core.carpaint.clearcoat_gloss | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Clear Coat Reflection/General/Samples | <com.redshift3d.redshift4c4d.nodes.core.carpaint.clearcoat_samples | maxon::Int | Input | false | false | false | 0 | 65535 | 16 | 
Clear Coat Reflection/General/Weight | <com.redshift3d.redshift4c4d.nodes.core.carpaint.clearcoat_weight | maxon::Float | Input | false | false | false | 0 | 1 | 0.5 | 
Metallic Flakes/Definition/Decay Distance | <com.redshift3d.redshift4c4d.nodes.core.carpaint.flake_decay | maxon::Float | Input | false | false | false |  |  | 500 | 
Metallic Flakes/Definition/Density | <com.redshift3d.redshift4c4d.nodes.core.carpaint.flake_density | maxon::Float | Input | false | false | false |  |  | 0.4 | 
Metallic Flakes/Definition/Scale | <com.redshift3d.redshift4c4d.nodes.core.carpaint.flake_scale | maxon::Float | Input | false | false | false |  |  | 0.005 | 
Metallic Flakes/Definition/Variation | <com.redshift3d.redshift4c4d.nodes.core.carpaint.flake_strength | maxon::Float | Input | false | false | false |  |  | 0.5 | 
Metallic Flakes/Reflection/Fresnel Control/Curve Factor | <com.redshift3d.redshift4c4d.nodes.core.carpaint.flake_curvefactor | maxon::Float | Input | false | false | false | 0.1 | 1000 | 10 | 
Metallic Flakes/Reflection/Fresnel Control/Facing Reflectivity | <com.redshift3d.redshift4c4d.nodes.core.carpaint.flake_facingweight | maxon::Float | Input | false | false | false | 0 | 1 | 0.8 | 
Metallic Flakes/Reflection/Fresnel Control/Perpendicular Reflectivity | <com.redshift3d.redshift4c4d.nodes.core.carpaint.flake_perpweight | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Metallic Flakes/Reflection/General/Color | <com.redshift3d.redshift4c4d.nodes.core.carpaint.flake_color | maxon::Color64 | Input | false | false | false |  |  | (1,1,1) | 
Metallic Flakes/Reflection/General/Glossiness | <com.redshift3d.redshift4c4d.nodes.core.carpaint.flake_gloss | maxon::Float | Input | false | false | false | 0 | 1 | 0.3 | 
Metallic Flakes/Reflection/General/Highlights Only | <com.redshift3d.redshift4c4d.nodes.core.carpaint.flake_norefl | maxon::Bool | Input | false | false | false |  |  | false | 
Metallic Flakes/Reflection/General/Samples | <com.redshift3d.redshift4c4d.nodes.core.carpaint.flake_samples | maxon::Int | Input | false | false | false | 0 | 65535 | 16 | 
Metallic Flakes/Reflection/General/Weight | <com.redshift3d.redshift4c4d.nodes.core.carpaint.flake_weight | maxon::Float | Input | false | false | false |  |  | 1 | 
Outputs/outColor | >com.redshift3d.redshift4c4d.nodes.core.carpaint.outcolor | maxon::Color64 | Output | false | false | false |  |  | (0,0,0) | 

