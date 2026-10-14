# Node Template: Fresnel

- **Node Space ID:** `com.redshift3d.redshift4c4d.class.nodespace`
- **Template ID:** `com.redshift3d.redshift4c4d.nodes.core.fresnel`
- **Template Name:** `Fresnel`

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
Node Category | net.maxon.node.base.category | maxon::InternedId | Attribute | false | false | true |  |  | patterns | distributions = distributions, operators = operators, geometries = geometries, patterns = patterns, primitives = primitives, effectors = effectors, fields = fields, functions = functions, structures = structures, geomodifiers = geomodifiers, geogenerators = geogenerators
Preview/Node | net.maxon.node.base.nodepreviewimage | maxon::ImageBaseRef | Attribute | false | false | false |  |  |  | 
General/Falloff Color/Bump Map | <com.redshift3d.redshift4c4d.nodes.core.fresnel.bump_input | maxon::Vector64 | Input | false | false | false |  |  |  | 
General/Falloff Color/Curve Falloff | <com.redshift3d.redshift4c4d.nodes.core.fresnel.user_curve | maxon::Float | Input | false | false | false | 0 | 100 | 5 | 
General/Falloff Color/Facing Color | <com.redshift3d.redshift4c4d.nodes.core.fresnel.facing_color | maxon::Color64 | Input | false | false | false |  |  | (0,0,0) | 
General/Falloff Color/IOR/Correct Facing Color Intensity | <com.redshift3d.redshift4c4d.nodes.core.fresnel.correct_intensity | maxon::Bool | Input | false | false | false |  |  | true | 
General/Falloff Color/IOR/Extinction Coefficient (k) | <com.redshift3d.redshift4c4d.nodes.core.fresnel.extinction_coeff | maxon::Float | Input | false | false | false |  |  | 0 | 
General/Falloff Color/IOR/Index of Refraction | <com.redshift3d.redshift4c4d.nodes.core.fresnel.ior | maxon::Float | Input | false | false | false | 0 | 100 | 1.4 | 
General/Falloff Color/IOR/Medium Type | <com.redshift3d.redshift4c4d.nodes.core.fresnel.fresnel_type | maxon::Int | Input | false | false | true |  |  | 0 | Dielectric = 0, Conductor = 1
General/Falloff Color/Perpendicular Color | <com.redshift3d.redshift4c4d.nodes.core.fresnel.perp_color | maxon::Color64 | Input | false | false | false |  |  | (1,1,1) | 
General/Falloff Color/Use Index of Refraction | <com.redshift3d.redshift4c4d.nodes.core.fresnel.fresnel_useior | maxon::Bool | Input | false | false | false |  |  | true | 
Outputs/outColor | >com.redshift3d.redshift4c4d.nodes.core.fresnel.outcolor | maxon::Color64 | Output | false | false | false |  |  | (0,0,0) | 

