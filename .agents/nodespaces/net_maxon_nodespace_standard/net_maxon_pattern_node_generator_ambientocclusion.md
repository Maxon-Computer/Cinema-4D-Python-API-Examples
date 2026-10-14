# Node Template: Ambient Occlusion

- **Node Space ID:** `net.maxon.nodespace.standard`
- **Template ID:** `net.maxon.pattern.node.generator.ambientocclusion`
- **Template Name:** `Ambient Occlusion`

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
Inputs/Direction | <direction | maxon::Vector | Input | false | false | false |  |  | (0,1,0) | 
Inputs/Direction Blend | <directionblend | maxon::Float | Input | false | false | false |  | 1 |  | 
Inputs/Dispersion | <dispersion | maxon::Float | Input | false | false | false |  | 1 | 1 | 
Inputs/Ignore Objects | <ignore | maxon::InternedId | Input | false | false | true |  |  | none | None = none, Self = self, Others = other
Inputs/Invert Direction | <inverse | maxon::Bool | Input | false | false | false |  |  |  | 
Inputs/Max Ray Length | <maxlength | maxon::Float | Input | false | false | false |  |  | 100 | 
Inputs/Min Ray Length | <minlength | maxon::Float | Input | false | false | false |  |  |  | 
Inputs/Quality/Accuracy | <accuracy | maxon::Float | Input | false | false | false |  | 1 | 0.5 | 
Inputs/Quality/Max Samples | <maxsamples | maxon::Int | Input | false | false | false |  | 999999 | 64 | 
Inputs/Quality/Min Samples | <minsamples | maxon::Int | Input | false | false | false |  | 999999 | 8 | 
Outputs/Average Normal | >averagenormal | maxon::Vector | Output | false | false | false |  |  |  | 
Outputs/Occlusion | >occlusion | maxon::Float | Output | false | false | false |  |  |  | 

