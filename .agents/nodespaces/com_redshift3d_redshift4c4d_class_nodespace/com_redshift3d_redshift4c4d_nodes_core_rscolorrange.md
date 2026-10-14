# Node Template: Color Change Range

- **Node Space ID:** `com.redshift3d.redshift4c4d.class.nodespace`
- **Template ID:** `com.redshift3d.redshift4c4d.nodes.core.rscolorrange`
- **Template Name:** `Color Change Range`

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
Node Category | net.maxon.node.base.category | maxon::InternedId | Attribute | false | false | true |  |  | functions | operators = operators, distributions = distributions, geometries = geometries, patterns = patterns, primitives = primitives, effectors = effectors, fields = fields, functions = functions, structures = structures, geomodifiers = geomodifiers, geogenerators = geogenerators
Preview/Node | net.maxon.node.base.nodepreviewimage | maxon::ImageBaseRef | Attribute | false | false | false |  |  |  | 
Inputs/Apply To Alpha | <com.redshift3d.redshift4c4d.nodes.core.rscolorrange.applytoalpha | maxon::Bool | Input | false | false | false |  |  | false | 
Inputs/Clamp To New Range | <com.redshift3d.redshift4c4d.nodes.core.rscolorrange.clamp | maxon::Bool | Input | false | false | false |  |  | true | 
Inputs/Input | <com.redshift3d.redshift4c4d.nodes.core.rscolorrange.input | maxon::ColorA64 | Input | false | false | false |  |  | (0,0,0,1) | 
Inputs/New Range Max | <com.redshift3d.redshift4c4d.nodes.core.rscolorrange.new_max | maxon::ColorA64 | Input | false | false | false |  |  | (1,1,1,1) | 
Inputs/New Range Min | <com.redshift3d.redshift4c4d.nodes.core.rscolorrange.new_min | maxon::ColorA64 | Input | false | false | false |  |  | (0,0,0,1) | 
Inputs/Old Range Max | <com.redshift3d.redshift4c4d.nodes.core.rscolorrange.old_max | maxon::ColorA64 | Input | false | false | false |  |  | (1,1,1,1) | 
Inputs/Old Range Min | <com.redshift3d.redshift4c4d.nodes.core.rscolorrange.old_min | maxon::ColorA64 | Input | false | false | false |  |  | (0,0,0,1) | 
Outputs/outColor | >com.redshift3d.redshift4c4d.nodes.core.rscolorrange.outcolor | maxon::ColorA64 | Output | false | false | false |  |  | (0,0,0,1) | 

