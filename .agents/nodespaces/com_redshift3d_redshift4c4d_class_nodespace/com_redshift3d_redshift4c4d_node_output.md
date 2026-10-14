# Node Template: Output

- **Node Space ID:** `com.redshift3d.redshift4c4d.class.nodespace`
- **Template ID:** `com.redshift3d.redshift4c4d.node.output`
- **Template Name:** `Output`

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
Node Category | net.maxon.node.base.category | maxon::InternedId | Attribute | false | false | true |  |  | effectors | operators = operators, distributions = distributions, geometries = geometries, patterns = patterns, primitives = primitives, effectors = effectors, fields = fields, functions = functions, structures = structures, geomodifiers = geomodifiers, geogenerators = geogenerators
Preview/Node | net.maxon.node.base.nodepreviewimage | maxon::ImageBaseRef | Attribute | false | false | false |  |  |  | 
Inputs/Contour | <com.redshift3d.redshift4c4d.node.output.contour | maxon::ColorA | Input | false | false | false |  |  |  | 
Inputs/Displacement | <com.redshift3d.redshift4c4d.node.output.displacement | maxon::Vector | Input | false | false | false |  |  |  | 
Inputs/Environment | <com.redshift3d.redshift4c4d.node.output.environment | maxon::ColorA | Input | false | false | false |  |  |  | 
Inputs/Light | <com.redshift3d.redshift4c4d.node.output.light | maxon::ColorA | Input | false | false | false |  |  |  | 
Inputs/Options/Material ID | <com.redshift3d.redshift4c4d.node.output.materialid | maxon::Int64 | Input | false | false | false |  | 65535 |  | 
Inputs/Surface | <com.redshift3d.redshift4c4d.node.output.surface | maxon::ColorA | Input | false | false | false |  |  |  | 
Inputs/UV Context | <com.redshift3d.redshift4c4d.node.output.rs_uv_context | RSC4D::UVContext | Input | false | false | false |  |  |  | 
Inputs/Viewport | <com.redshift3d.redshift4c4d.node.output.viewport | maxon::ColorA | Input | false | false | false |  |  |  | 
Inputs/Volume | <com.redshift3d.redshift4c4d.node.output.volume | maxon::ColorA | Input | false | false | false |  |  |  | 

