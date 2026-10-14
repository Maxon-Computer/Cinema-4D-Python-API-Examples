# Node Template: To Barycentric

- **Node Space ID:** `net.maxon.nodespace.standard`
- **Template ID:** `net.maxon.asset.math.tobarycentric`
- **Template Name:** `To Barycentric`

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
Inputs/A | <inport@dflUqNboJtQpUHjAt_2dAX | maxon::Vector64 | Input | false | false | false |  |  |  | 
Inputs/B | <inport@BftKTFprNdBh6pHmco2H1W | maxon::Vector64 | Input | false | false | false |  |  | (0,0,1) | 
Inputs/C | <inport@QfWkCy5VIpDoJPU6zPhkkW | maxon::Vector64 | Input | false | false | false |  |  | (1,0,1) | 
Inputs/Position | <inport@Q3usVO2fFFJmwSqjBwNxOW | maxon::Vector64 | Input | false | false | false |  |  |  | 
Outputs/Barycentric | >outport@TnkvuQUYEB3kcESTCgWfbS | maxon::Vector64 | Output | false | false | false |  |  |  | 
Outputs/Distance | >outport@QoJnIFz4ARFtPj8ibC0XxW | maxon::Float64 | Output | false | false | false |  |  |  | 
Outputs/Inside Tri | >outport@ZN14KddWDtCiB5_7AzST3G | maxon::Bool | Output | false | false | false |  |  |  | 

