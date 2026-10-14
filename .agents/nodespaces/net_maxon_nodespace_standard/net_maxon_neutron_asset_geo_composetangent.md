# Node Template: Compose Tangent

- **Node Space ID:** `net.maxon.nodespace.standard`
- **Template ID:** `net.maxon.neutron.asset.geo.composetangent`
- **Template Name:** `Compose Tangent`

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
Inputs/Incoming | <in@N3A1l_QqHpkkBBktsj8_BI | maxon::Vector64 | Input | false | false | false |  |  |  | 
Inputs/Incoming Length | <in@d$x4N6m6LRFokBFG7waKf1 | maxon::Float64 | Input | false | false | false |  |  | 1 | 
Inputs/Mode | <in@PUQLxTc3N9KgdqUb1Evpo1 | maxon::Int64 | Input | false | false | true |  |  |  | Standard = 0, Length = 1
Inputs/Outgoing | <in@Mmh6Ws0KDlojfYKrGUVz2L | maxon::Vector64 | Input | false | false | false |  |  |  | 
Inputs/Outgoing Length | <in@GRohLYE7KV5hxKIFMUM503 | maxon::Float64 | Input | false | false | false |  |  | 1 | 
Outputs/Tangent | >out@FcI7rmpzM1ynBPIYN$5fIL | maxon::Tuple<maxon::Vector64, maxon::Vector64> | Output | false | false | false |  |  |  | 

