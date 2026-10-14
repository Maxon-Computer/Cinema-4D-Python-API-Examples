# Node Template: Flakes

- **Node Space ID:** `com.redshift3d.redshift4c4d.class.nodespace`
- **Template ID:** `com.redshift3d.redshift4c4d.nodes.core.flakes`
- **Template Name:** `Flakes`

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
Shader/3D Flakes/Depth | <com.redshift3d.redshift4c4d.nodes.core.flakes.indepth | maxon::Float | Input | false | false | false | 0 | 2147483648 | 0 | 
Shader/3D Flakes/IOR | <com.redshift3d.redshift4c4d.nodes.core.flakes.inior | maxon::Float | Input | false | false | false | 0 | 3 | 1.5 | 
Shader/3D Flakes/Step Size | <com.redshift3d.redshift4c4d.nodes.core.flakes.instepsize | maxon::Float | Input | false | false | false | 0 | 2147483648 | 0 | 
Shader/Basic Properties/Coord Space | <com.redshift3d.redshift4c4d.nodes.core.flakes.incoordinatespace | maxon::Int | Input | false | false | true |  |  | 1 | World = 0, Object = 1, UV = 2
Shader/Basic Properties/Density | <com.redshift3d.redshift4c4d.nodes.core.flakes.indensity | maxon::Float | Input | false | false | false | 0 | 1 | 0.8 | 
Shader/Basic Properties/Flakes Size | <com.redshift3d.redshift4c4d.nodes.core.flakes.inflakesize | maxon::Float | Input | false | false | false | 0 | 1 | 0.5 | 
Shader/Basic Properties/Pattern | <com.redshift3d.redshift4c4d.nodes.core.flakes.inpattern | maxon::Int | Input | false | false | true |  |  | 0 | Voronoi = 0, Dots = 1
Shader/Basic Properties/Randomize | <com.redshift3d.redshift4c4d.nodes.core.flakes.inrandomize | maxon::Float | Input | false | false | false | 0 | 1 | 0.5 | 
Shader/Basic Properties/Scale | <com.redshift3d.redshift4c4d.nodes.core.flakes.inscale | maxon::Float | Input | false | false | false | 0 | 2147483648 | 1 | 
Shader/Basic Properties/Seed | <com.redshift3d.redshift4c4d.nodes.core.flakes.inseed | maxon::Int | Input | false | false | false |  |  | 123 | 
Shader/Basic Properties/Size Variance | <com.redshift3d.redshift4c4d.nodes.core.flakes.invariance | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Shader/Basic Properties/UV Channel | <com.redshift3d.redshift4c4d.nodes.core.flakes.tspace_id | maxon::String | Input | false | false | false |  |  |  | 
Shader/Basic Properties/UV Context | <com.redshift3d.redshift4c4d.nodes.core.flakes.uv_context | RSC4D::UVContext | Input | false | false | false |  |  |  | 
Shader/Distance Behavior/Blend Maximum | <com.redshift3d.redshift4c4d.nodes.core.flakes.inflakesmaximum | maxon::Float | Input | false | false | false | 0 | 2147483648 | 2000 | 
Shader/Distance Behavior/Blend Minimum | <com.redshift3d.redshift4c4d.nodes.core.flakes.inflakesminimum | maxon::Float | Input | false | false | false | 0 | 2147483648 | 1000 | 
Outputs/outAlpha | >com.redshift3d.redshift4c4d.nodes.core.flakes.outalpha | maxon::Float | Output | false | false | false |  |  | 0 | 
Outputs/outFlakesBlend | >com.redshift3d.redshift4c4d.nodes.core.flakes.outflakesblend | maxon::Float | Output | false | false | false |  |  | 0 | 
Outputs/outFlakesID | >com.redshift3d.redshift4c4d.nodes.core.flakes.outflakesid | maxon::Float | Output | false | false | false |  |  | 0 | 
Outputs/outNormal | >com.redshift3d.redshift4c4d.nodes.core.flakes.outnormal | maxon::Vector64 | Output | false | false | false |  |  | (0,0,0) | 

