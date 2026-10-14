# Node Template: Scatter

- **Node Space ID:** `net.maxon.neutron.nodespace`
- **Template ID:** `net.maxon.pattern.node.generator.scatter`
- **Template Name:** `Scatter`

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
Inputs/Density | <peritemdensity | maxon::Float | Input | false | false | false |  | 1 | 1 | 
Inputs/Max Splat Count | <count | maxon::UInt32 | Input | false | false | false |  | 999999999 | 100 | 
Inputs/Per Splat/Random Rotation | <peritemrandomrotation | maxon::Float | Input | false | false | false |  | 6.283 | 0 | 
Inputs/Per Splat/Random Scale | <peritemrandomscale | maxon::Vector2d | Input | false | false | false |  |  | (0,0) | 
Inputs/Per Splat/Random Scale | <peritemrandomscaleuniform | maxon::Float | Input | false | false | false |  |  |  | 
Inputs/Per Splat/Rotation | <peritemrotation | maxon::Float | Input | false | false | false |  |  | 0 | 
Inputs/Per Splat/Scale | <peritemscale | maxon::Vector2d | Input | false | false | false |  |  | (0.1,0.1) | 
Inputs/Per Splat/Shape | <peritemshape | maxon::Float | Input | false | false | false |  |  |  | 
Inputs/Per Splat/Skip Probability | <peritemskipprobability | maxon::Float | Input | false | false | false |  | 1 |  | 
Inputs/Per Splat/Uniform Scale | <peritemuniformscale | maxon::Bool | Input | false | false | false |  |  | true | 
Inputs/Remove Overlapping Splats | <removeoverlaps | maxon::Bool | Input | false | false | false |  |  |  | 
Inputs/Repeat Splats at Edges | <tile | maxon::Bool | Input | false | false | false |  |  |  | 
Inputs/Seed | <seed | maxon::UInt32 | Input | false | false | false |  |  | 12345 | 
Outputs/Center | >center | maxon::Vector2d | Output | false | false | false |  |  |  | 
Outputs/Context | >resultcontext | maxon::ShadingContext | Output | false | false | false |  |  |  | 
Outputs/Index | >index | maxon::Int | Output | false | false | false |  |  |  | 
Outputs/Mask | >mask | maxon::Bool | Output | false | false | false |  |  |  | 

