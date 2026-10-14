# Node Template: Matte-Shadow Catcher

- **Node Space ID:** `com.redshift3d.redshift4c4d.class.nodespace`
- **Template ID:** `com.redshift3d.redshift4c4d.nodes.core.matteshadow`
- **Template Name:** `Matte-Shadow Catcher`

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
Basic/Show Preview | net.maxon.node.base.displaypreview | maxon::Bool | Attribute | false | false | false |  |  | false | 
Filter Tags | net.maxon.node.base.filtertags | maxon::CString | Attribute | false | false | false |  |  |  | 
Node Category | net.maxon.node.base.category | maxon::InternedId | Attribute | false | false | true |  |  | primitives | operators = operators, distributions = distributions, geometries = geometries, patterns = patterns, primitives = primitives, effectors = effectors, fields = fields, functions = functions, structures = structures, geomodifiers = geomodifiers, geogenerators = geogenerators
Preview/Node | net.maxon.node.base.nodepreviewimage | maxon::ImageBaseRef | Attribute | false | false | false |  |  |  | 
Ambient Occlusion/Enable | <com.redshift3d.redshift4c4d.nodes.core.matteshadow.ao_on | maxon::Bool | Input | false | false | false |  |  | false | 
Ambient Occlusion/Max Distance | <com.redshift3d.redshift4c4d.nodes.core.matteshadow.ao_distance | maxon::Float | Input | false | false | false |  |  | 0 | 
Ambient Occlusion/Samples | <com.redshift3d.redshift4c4d.nodes.core.matteshadow.ao_samples | maxon::Int | Input | false | false | false | 0 | 65535 | 16 | 
Ambient Occlusion/Shadow Color | <com.redshift3d.redshift4c4d.nodes.core.matteshadow.ao_dark | maxon::Color64 | Input | false | false | false |  |  | (0,0,0) | 
Bump/Bump Map | <com.redshift3d.redshift4c4d.nodes.core.matteshadow.bump_input | maxon::Vector64 | Input | false | false | false |  |  |  | 
General/Base/Background Color | <com.redshift3d.redshift4c4d.nodes.core.matteshadow.background | maxon::ColorA64 | Input | false | false | false |  |  | (0,0,0,0) | 
General/Base/Background Is Environment | <com.redshift3d.redshift4c4d.nodes.core.matteshadow.backgroundisenv | maxon::Bool | Input | false | false | false |  |  | false | 
General/Base/Emissive Color | <com.redshift3d.redshift4c4d.nodes.core.matteshadow.emissive_color | maxon::Color64 | Input | false | false | false |  |  | (0,0,0) | 
General/Base/Emissive Scale | <com.redshift3d.redshift4c4d.nodes.core.matteshadow.emissive_scale | maxon::Float | Input | false | false | false |  |  | 1 | 
General/Illumination/Diffuse/Catch Diffuse | <com.redshift3d.redshift4c4d.nodes.core.matteshadow.catch_diffuse | maxon::Bool | Input | false | false | false |  |  | false | 
General/Illumination/Diffuse/Color | <com.redshift3d.redshift4c4d.nodes.core.matteshadow.diffuse | maxon::Color64 | Input | false | false | false |  |  | (0.5,0.5,0.5) | 
General/Illumination/Diffuse/Weight | <com.redshift3d.redshift4c4d.nodes.core.matteshadow.diffuse_weight | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
General/Illumination/Shadows/Ambient Color | <com.redshift3d.redshift4c4d.nodes.core.matteshadow.ambient | maxon::Color64 | Input | false | false | false |  |  | (0,0,0) | 
General/Illumination/Shadows/Catch Shadows | <com.redshift3d.redshift4c4d.nodes.core.matteshadow.catch_shadows | maxon::Bool | Input | false | false | false |  |  | true | 
General/Illumination/Shadows/Factor in Light Angle | <com.redshift3d.redshift4c4d.nodes.core.matteshadow.use_dot_nl | maxon::Bool | Input | false | false | false |  |  | true | 
General/Illumination/Shadows/Saturation | <com.redshift3d.redshift4c4d.nodes.core.matteshadow.saturation | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
General/Illumination/Shadows/Shadow Color | <com.redshift3d.redshift4c4d.nodes.core.matteshadow.shadows | maxon::ColorA64 | Input | false | false | false |  |  | (0,0,0,1) | 
General/Illumination/Shadows/Transparency | <com.redshift3d.redshift4c4d.nodes.core.matteshadow.transparency | maxon::Float | Input | false | false | false | 0 | 1 | 0 | 
Reflections/Attenuation/Distance (cm) | <com.redshift3d.redshift4c4d.nodes.core.matteshadow.refl_max_dist | maxon::Float | Input | false | false | false |  |  | 0 | 
Reflections/Attenuation/Enable | <com.redshift3d.redshift4c4d.nodes.core.matteshadow.refl_fog_enable | maxon::Bool | Input | false | false | false |  |  | false | 
Reflections/BRDF | <com.redshift3d.redshift4c4d.nodes.core.matteshadow.refl_brdf | maxon::Int | Input | false | false | true |  |  | 0 | Beckmann (Cook-Torrance) = 0, Ashikhmin-Shirley (legacy) = 65536, GGX = 1, Ashikhmin-Shirley = 2
Reflections/Catch Reflections | <com.redshift3d.redshift4c4d.nodes.core.matteshadow.refl_enabled | maxon::Bool | Input | false | false | false |  |  | false | 
Reflections/Color | <com.redshift3d.redshift4c4d.nodes.core.matteshadow.refl_color | maxon::ColorA64 | Input | false | false | false |  |  | (1,1,1,1) | 
Reflections/Glossiness | <com.redshift3d.redshift4c4d.nodes.core.matteshadow.refl_glossiness | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Reflections/Samples | <com.redshift3d.redshift4c4d.nodes.core.matteshadow.refl_samples | maxon::Int | Input | false | false | false | 0 | 65535 | 8 | 
Reflections/Weight | <com.redshift3d.redshift4c4d.nodes.core.matteshadow.reflectivity | maxon::Float | Input | false | false | false | 0 | 1 | 0.6 | 
Outputs/out | >com.redshift3d.redshift4c4d.nodes.core.matteshadow.out | maxon::Color64 | Output | false | false | false |  |  | (0,0,0) | 

