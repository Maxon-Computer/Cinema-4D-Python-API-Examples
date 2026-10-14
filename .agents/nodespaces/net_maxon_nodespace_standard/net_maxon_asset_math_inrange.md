# Node Template: In Range

- **Node Space ID:** `net.maxon.nodespace.standard`
- **Template ID:** `net.maxon.asset.math.inrange`
- **Template Name:** `In Range`

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
Inputs/Epsilon | <inport@EEvHFgh$HV1qZs5_YSWBjb | maxon::Int64 | Input | false | false | true |  |  |  | Off = 0, On = 1
Inputs/Input | <inport@HjYyUbUfLZzjzLtUBgwtom | maxon::Vector64 | Input | false | false | false |  |  |  | 
Inputs/Max | <inport@Qo0si3IbHRXuHMkkPZjpwk | maxon::Vector64 | Input | false | false | false |  |  | (1,1,1) | 
Inputs/Min | <inport@El61cf2BJpOgL9ytEBrEqn | maxon::Vector64 | Input | false | false | false |  |  |  | 
Outputs/In Range | >outport@T9gE9yQdKd5iSJ5ZYwYz6h | maxon::Bool | Output | false | false | false |  |  |  | 
Outputs/Max Distance | >outport@NfJ2xfkALdBp1KGTMQDiul | maxon::Float64 | Output | false | false | false |  |  |  | 
Outputs/Min Distance | >outport@OME4GtezP9AtNNL2HTkVOh | maxon::Float64 | Output | false | false | false |  |  |  | 

