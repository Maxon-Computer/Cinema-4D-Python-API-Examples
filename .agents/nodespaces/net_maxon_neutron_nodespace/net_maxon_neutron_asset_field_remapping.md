# Node Template: Field Remap

- **Node Space ID:** `net.maxon.neutron.nodespace`
- **Template ID:** `net.maxon.neutron.asset.field.remapping`
- **Template Name:** `Field Remap`

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
Node Category | net.maxon.node.base.category | maxon::InternedId | Attribute | false | false | true |  |  | functions | distributions = distributions, operators = operators, geometries = geometries, patterns = patterns, primitives = primitives, effectors = effectors, fields = fields, functions = functions, structures = structures, geomodifiers = geomodifiers, geogenerators = geogenerators
Preview/Node | net.maxon.node.base.nodepreviewimage | maxon::ImageBaseRef | Attribute | false | false | false |  |  |  | 
Inputs/Inner Offset | <inport@PrMoJllWDN2oUvz2Fu62l_ | maxon::Float64 | Input | false | false | false |  |  |  | 
Inputs/Input | <out@V1Eaj0l3A5xk381Ev0pb7X | maxon::Float64 | Input | false | false | false |  |  |  | 
Inputs/Output Max | <inport@JJbE1aTdKdPjcjJsibaQJR | maxon::Float64 | Input | false | false | false |  | 1 | 1 | 
Inputs/Output Min | <inport@V1kkG9tVBhsg4Iz8nLI3XV | maxon::Float64 | Input | false | false | false |  | 1 | 0 | 
Inputs/Strength | <inport@YxWZ9VJhNxFgf4PRIJLMTW | maxon::Float64 | Input | false | false | false |  | 1 | 1 | 
Outputs/Result | >out@Wi3V2kkkDJ_lTLQmzlUJDW | maxon::Float64 | Output | false | false | false |  |  |  | 

