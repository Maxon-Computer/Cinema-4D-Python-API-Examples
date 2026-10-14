# Node Template: Slider

- **Node Space ID:** `net.maxon.nodespace.standard`
- **Template ID:** `net.maxon.asset.utility.slider`
- **Template Name:** `Slider`

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
Input | net.maxon.node.groupwithports.input |  | Attribute | false | false | false |  |  |  | 
Node Category | net.maxon.node.base.category | maxon::InternedId | Attribute | false | false | true |  |  | functions | operators = operators, distributions = distributions, geometries = geometries, patterns = patterns, primitives = primitives, effectors = effectors, fields = fields, functions = functions, structures = structures, geomodifiers = geomodifiers, geogenerators = geogenerators
Preview/Node | net.maxon.node.base.nodepreviewimage | maxon::ImageBaseRef | Attribute | false | false | false |  |  |  | 
Inputs/Step Size | <inport@XF$19GngABUqtuOh7DCy7P | maxon::Int64 | Input | false | false | true |  |  |  | 0.01% = 0, 0.1% = 1, 1% = 2
Inputs/Value | <inport@RuPl2WRiMRjjD11wSR5NtN | maxon::Float64 | Input | false | false | false |  |  |  | 
Inputs/Value | <inport@T8qbMUtKFJ1rT1j3MATv0L | maxon::Float64 | Input | false | false | false |  |  |  | 
Inputs/Value | <inport@YIfClrTQBZCjOeVi2XdP2O | maxon::Float64 | Input | false | false | false |  |  |  | 
Outputs/Output | >net.maxon.node.groupwithports.output | maxon::Float64 | Output | false | false | false |  |  |  | 

