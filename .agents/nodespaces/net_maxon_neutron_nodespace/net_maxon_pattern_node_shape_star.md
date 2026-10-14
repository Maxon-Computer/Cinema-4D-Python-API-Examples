# Node Template: Star

- **Node Space ID:** `net.maxon.neutron.nodespace`
- **Template ID:** `net.maxon.pattern.node.shape.star`
- **Template Name:** `Star`

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
Context/Context | <context | maxon::ShadingContext | Input | false | false | false |  |  |  | 
Context/Local Context | <contextlocal | maxon::ShadingContext | Input | false | false | false |  |  |  | 
Inputs/Cutout | <cutout | maxon::Float | Input | false | false | false |  |  | 0.5 | 
Inputs/Exterior | <exterior | maxon::ColorA | Input | false | false | false |  |  | (0,0,0,1) | 
Inputs/Fill | <fill | maxon::ColorA | Input | false | false | false |  |  | (1,1,1,1) | 
Inputs/Inner Softness | <innersoftness | maxon::Float | Input | false | false | false |  | 100 | 0 | 
Inputs/Outer Softness | <outersoftness | maxon::Float | Input | false | false | false |  | 100 | 0 | 
Inputs/Scale | <scale | maxon::Float | Input | false | false | false | 0 | 100000 | 0.5 | 
Inputs/Spikes | <spikes | maxon::Int | Input | false | false | false | 3 | 100000 | 6 | 
Outputs/Distance | >distance | maxon::Float | Output | false | false | false |  |  |  | 
Outputs/Mask | >mask | maxon::Float | Output | false | false | false |  |  |  | 
Outputs/Result | >result | maxon::ColorA | Output | false | false | false |  |  |  | 

