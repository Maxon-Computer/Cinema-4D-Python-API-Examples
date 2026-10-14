# Node Template: Displacement

- **Node Space ID:** `com.redshift3d.redshift4c4d.class.nodespace`
- **Template ID:** `com.redshift3d.redshift4c4d.nodes.core.displacement`
- **Template Name:** `Displacement`

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
Node Category | net.maxon.node.base.category | maxon::InternedId | Attribute | false | false | true |  |  | structures | operators = operators, distributions = distributions, geometries = geometries, patterns = patterns, primitives = primitives, effectors = effectors, fields = fields, functions = functions, structures = structures, geomodifiers = geomodifiers, geogenerators = geogenerators
Preview/Node | net.maxon.node.base.nodepreviewimage | maxon::ImageBaseRef | Attribute | false | false | false |  |  |  | 
Inputs/Change Range/New Range Max | <com.redshift3d.redshift4c4d.nodes.core.displacement.newrange_max | maxon::Float | Input | false | false | false |  |  | 1 | 
Inputs/Change Range/New Range Min | <com.redshift3d.redshift4c4d.nodes.core.displacement.newrange_min | maxon::Float | Input | false | false | false |  |  | 0 | 
Inputs/Change Range/Old Range Max | <com.redshift3d.redshift4c4d.nodes.core.displacement.oldrange_max | maxon::Float | Input | false | false | false |  |  | 1 | 
Inputs/Change Range/Old Range Min | <com.redshift3d.redshift4c4d.nodes.core.displacement.oldrange_min | maxon::Float | Input | false | false | false |  |  | 0 | 
Inputs/Tangents/Tangents Channel | <com.redshift3d.redshift4c4d.nodes.core.displacement.tangents | maxon::String | Input | false | false | false |  |  |  | 
Inputs/Texture/Map Encoding | <com.redshift3d.redshift4c4d.nodes.core.displacement.map_encoding | maxon::Int | Input | false | false | true |  |  | 2 | Vector = 0, Height Field = 2
Inputs/Texture/Scale | <com.redshift3d.redshift4c4d.nodes.core.displacement.scale | maxon::Float | Input | false | false | false |  |  | 1 | 
Inputs/Texture/Space Type | <com.redshift3d.redshift4c4d.nodes.core.displacement.space_type | maxon::Int | Input | false | false | true |  |  | 1 | Object = 1, Tangent = 2
Inputs/Texture/TexMap | <com.redshift3d.redshift4c4d.nodes.core.displacement.texmap | maxon::Color64 | Input | false | false | false |  |  |  | 
Inputs/Tspace_id | <com.redshift3d.redshift4c4d.nodes.core.displacement.tspace_id | maxon::String | Input | false | false | false |  |  |  | 
Inputs/UV Context | <com.redshift3d.redshift4c4d.nodes.core.displacement.uv_context | RSC4D::UVContext | Input | false | false | false |  |  |  | 
Outputs/out | >com.redshift3d.redshift4c4d.nodes.core.displacement.out | maxon::Vector64 | Output | false | false | false |  |  | (0,0,0) | 

