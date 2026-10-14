# Node Template: AO

- **Node Space ID:** `com.redshift3d.redshift4c4d.class.nodespace`
- **Template ID:** `com.redshift3d.redshift4c4d.nodes.core.ambientocclusion`
- **Template Name:** `AO`

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
Node Category | net.maxon.node.base.category | maxon::InternedId | Attribute | false | false | true |  |  | patterns | operators = operators, distributions = distributions, geometries = geometries, patterns = patterns, primitives = primitives, effectors = effectors, fields = fields, functions = functions, structures = structures, geomodifiers = geomodifiers, geogenerators = geogenerators
Preview/Node | net.maxon.node.base.nodepreviewimage | maxon::ImageBaseRef | Attribute | false | false | false |  |  |  | 
Inputs/General/Bias | <com.redshift3d.redshift4c4d.nodes.core.ambientocclusion.bias | maxon::Vector64 | Input | false | false | false |  |  | (0,0,0) | 
Inputs/General/Bias Mode | <com.redshift3d.redshift4c4d.nodes.core.ambientocclusion.biasmode | maxon::Int | Input | false | false | true |  |  | 0 | World Space = 2, None = 0, Object Space = 1
Inputs/General/Bright | <com.redshift3d.redshift4c4d.nodes.core.ambientocclusion.bright | maxon::ColorA64 | Input | false | false | false |  |  | (1,1,1,1) | 
Inputs/General/Consider Same Object Only | <com.redshift3d.redshift4c4d.nodes.core.ambientocclusion.sameobjectonly | maxon::Bool | Input | false | false | false |  |  | false | 
Inputs/General/Dark | <com.redshift3d.redshift4c4d.nodes.core.ambientocclusion.dark | maxon::ColorA64 | Input | false | false | false |  |  | (0,0,0,1) | 
Inputs/General/Falloff | <com.redshift3d.redshift4c4d.nodes.core.ambientocclusion.falloff | maxon::Float | Input | false | false | false | 0 | 65536 | 1 | 
Inputs/General/Invert Normal | <com.redshift3d.redshift4c4d.nodes.core.ambientocclusion.invert | maxon::Bool | Input | false | false | false |  |  | false | 
Inputs/General/Max Distance | <com.redshift3d.redshift4c4d.nodes.core.ambientocclusion.maxdistance | maxon::Float | Input | false | false | false | 0 | 1000000 | 0 | 
Inputs/General/Occlusion in Alpha | <com.redshift3d.redshift4c4d.nodes.core.ambientocclusion.occlusioninalpha | maxon::Bool | Input | false | false | false |  |  | false | 
Inputs/General/Output Mode | <com.redshift3d.redshift4c4d.nodes.core.ambientocclusion.outputmode | maxon::Int | Input | false | false | true |  |  | 0 | Sampled Environment = 1, Occlusion = 0, Return Bent Normals (World Space) = 2, Return Bent Normals (Object Space) = 3
Inputs/General/Reflective | <com.redshift3d.redshift4c4d.nodes.core.ambientocclusion.reflective | maxon::Bool | Input | false | false | false |  |  | false | 
Inputs/General/Samples | <com.redshift3d.redshift4c4d.nodes.core.ambientocclusion.numsamples | maxon::Int | Input | false | false | false | 1 | 65535 | 16 | 
Inputs/General/Spread | <com.redshift3d.redshift4c4d.nodes.core.ambientocclusion.spread | maxon::Float | Input | false | false | false | 0 | 1 | 0.8 | 
Outputs/out | >com.redshift3d.redshift4c4d.nodes.core.ambientocclusion.out | maxon::ColorA64 | Output | false | false | false |  |  | (0,0,0,1) | 

