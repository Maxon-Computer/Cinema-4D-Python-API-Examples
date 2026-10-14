# Node Template: Principled Hair

- **Node Space ID:** `com.redshift3d.redshift4c4d.class.nodespace`
- **Template ID:** `com.redshift3d.redshift4c4d.nodes.core.hair2`
- **Template Name:** `Principled Hair`

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
Advanced/Combined Trace Depth | <com.redshift3d.redshift4c4d.nodes.core.hair2.combined_depth | maxon::Int | Input | false | false | false | 0 | 63 | 6 | 
Advanced/Enable Trace Depth Overrides | <com.redshift3d.redshift4c4d.nodes.core.hair2.depth_override | maxon::Bool | Input | false | false | false |  |  | false | 
Advanced/Trace Depth | <com.redshift3d.redshift4c4d.nodes.core.hair2.refl_depth | maxon::Int | Input | false | false | false | 1 | 63 | 4 | 
General/Color/Albedo | <com.redshift3d.redshift4c4d.nodes.core.hair2.albedo | maxon::Color64 | Input | false | false | false |  |  | (0.9,0.5,0.2) | 
General/Color/Albedo Mix | <com.redshift3d.redshift4c4d.nodes.core.hair2.albedomix | maxon::Float | Input | false | false | false | 0 | 1 | 0 | 
General/Color/Melanin | <com.redshift3d.redshift4c4d.nodes.core.hair2.melanin | maxon::Float | Input | false | false | false |  |  | 0.5 | 
General/Color/Melanin Redness | <com.redshift3d.redshift4c4d.nodes.core.hair2.pheomelanin | maxon::Float | Input | false | false | false |  |  | 0.5 | 
General/Diffuse Contribution/Diffuse Albedo | <com.redshift3d.redshift4c4d.nodes.core.hair2.diffuse_albedo | maxon::Color64 | Input | false | false | false |  |  | (1,1,1) | 
General/Diffuse Contribution/Diffuse Amount | <com.redshift3d.redshift4c4d.nodes.core.hair2.diffuse_amount | maxon::Float | Input | false | false | false | 0 | 1 | 0 | 
General/Reflection/Transmission/Angle shift | <com.redshift3d.redshift4c4d.nodes.core.hair2.alpha | maxon::Float | Input | false | false | false | -15 | 15 | 3 | 
General/Reflection/Transmission/IOR | <com.redshift3d.redshift4c4d.nodes.core.hair2.ior | maxon::Float | Input | false | false | false | 1 | 2 | 1.55 | 
General/Reflection/Transmission/Roughness | <com.redshift3d.redshift4c4d.nodes.core.hair2.roughness_l | maxon::Float | Input | false | false | false | 0 | 1 | 0.3 | 
General/Reflection/Transmission/Roughness (radial) | <com.redshift3d.redshift4c4d.nodes.core.hair2.roughness_a | maxon::Float | Input | false | false | false | 0 | 1 | 0.3 | 
General/Reflection/Transmission/Samples | <com.redshift3d.redshift4c4d.nodes.core.hair2.samples | maxon::Int | Input | false | false | false | 0 | 65535 | 128 | 
General/Reflection/Transmission/Tint | <com.redshift3d.redshift4c4d.nodes.core.hair2.tint | maxon::Color64 | Input | false | false | false |  |  | (1,1,1) | 
General/Variation/Glint Size | <com.redshift3d.redshift4c4d.nodes.core.hair2.glintsize | maxon::Float | Input | false | false | false | 0 | 65535 | 1024 | 
General/Variation/Glint Strength | <com.redshift3d.redshift4c4d.nodes.core.hair2.glintstrength | maxon::Float | Input | false | false | false | 0 | 1 | 0 | 
General/Variation/Melanin Redness Var. | <com.redshift3d.redshift4c4d.nodes.core.hair2.pheomelaninvar | maxon::Float | Input | false | false | false | 0 | 1 | 0 | 
General/Variation/Melanin Var. | <com.redshift3d.redshift4c4d.nodes.core.hair2.melaninvar | maxon::Float | Input | false | false | false | 0 | 1 | 0 | 
General/Variation/Roughness (radial) Var. | <com.redshift3d.redshift4c4d.nodes.core.hair2.roughnessavar | maxon::Float | Input | false | false | false | 0 | 1 | 0 | 
General/Variation/Roughness Var. | <com.redshift3d.redshift4c4d.nodes.core.hair2.roughnesslvar | maxon::Float | Input | false | false | false | 0 | 1 | 0 | 
General/Variation/Stray Hair Albedo | <com.redshift3d.redshift4c4d.nodes.core.hair2.strayalbedo | maxon::Color64 | Input | false | false | false |  |  | (0.9,0.5,0.2) | 
General/Variation/Stray Hair Fraction | <com.redshift3d.redshift4c4d.nodes.core.hair2.strayfraction | maxon::Float | Input | false | false | false | 0 | 1 | 0 | 
General/Variation/Variation Seed | <com.redshift3d.redshift4c4d.nodes.core.hair2.varseed | maxon::Float | Input | false | false | false | 0 | 65535 | 0 | 
Outputs/outColor | >com.redshift3d.redshift4c4d.nodes.core.hair2.outcolor | maxon::Color64 | Output | false | false | false |  |  | (0,0,0) | 

