# Node Template: Sample Noise

- **Node Space ID:** `net.maxon.nodespace.standard`
- **Template ID:** `net.maxon.node.noise`
- **Template Name:** `Sample Noise`

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
Inputs/2D value | <twod | maxon::Bool | Input | false | false | false |  |  | false | 
Inputs/Absolute Value | <absolute | maxon::Bool | Input | false | false | false |  |  | false | 
Inputs/Exponent | <exponent | maxon::Float | Input | false | false | false | 0.1 | 5 | 2 | 
Inputs/Gain | <gain | maxon::Float | Input | false | false | false | 0.1 | 4 | 0.5 | 
Inputs/Input | <value | maxon::Vector | Input | false | false | false |  |  |  | 
Inputs/Lacunarity | <lacunarity | maxon::Float | Input | false | false | false | 0.1 | 10 | 2.1 | 
Inputs/Noise Type | <noisetype | maxon::Id | Input | false | false | true |  |  | net.maxon.render.rendernoiseclass.perlin | registry#net.maxon.render.registry.rendernoiseclasses = registry#net.maxon.render.registry.rendernoiseclasses
Inputs/Octaves | <octaves | maxon::Float | Input | false | false | false |  | 20 | 6 | 
Inputs/Scale | <scale | maxon::Float | Input | false | false | false |  |  | 10 | 
Inputs/Seed | <seed | maxon::Int | Input | false | false | false |  |  | 123 | 
Inputs/Time | <time | maxon::Float | Input | false | false | false |  |  |  | 
Outputs/Result | >result | maxon::Float | Output | false | false | false |  |  |  | 

