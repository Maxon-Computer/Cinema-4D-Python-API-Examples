# Node Template: Angle to DMS

- **Node Space ID:** `net.maxon.neutron.nodespace`
- **Template ID:** `net.maxon.neutron.asset.math.angletodms`
- **Template Name:** `Angle to DMS`

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
Inputs/Angle | <x@FzG5uiTOFBqrC7xpum4Q4T | maxon::Float64 | Input | false | false | false |  |  |  | 
Inputs/Type | <inport@DFLfz0O_FxUqEvgrUCrN9T | maxon::Int64 | Input | false | false | true |  |  |  | Latitude = 0, Longitude = 1
Outputs/Degree | >out@Gy6ZKJJvGhyiBYUH$U52MQ | maxon::Float64 | Output | false | false | false |  |  |  | 
Outputs/Minutes | >out@acUb8pb4FxEku3iPbkzK6S | maxon::Float64 | Output | false | false | false |  |  |  | 
Outputs/Seconds | >out@PyruEzFBAtolWzztDbejYX | maxon::Float64 | Output | false | false | false |  |  |  | 
Outputs/String | >outport@L45CMT7hGloso90VNvBfbV | maxon::String | Output | false | false | false |  |  |  | 

