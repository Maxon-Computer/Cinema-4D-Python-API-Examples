# Node Template: Basic Gradient

- **Node Space ID:** `net.maxon.neutron.nodespace`
- **Template ID:** `net.maxon.pattern.node.generator.gradient`
- **Template Name:** `Basic Gradient`

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
Node Category | net.maxon.node.base.category | maxon::InternedId | Attribute | false | false | true |  |  | patterns | distributions = distributions, operators = operators, geometries = geometries, patterns = patterns, primitives = primitives, effectors = effectors, fields = fields, functions = functions, structures = structures, geomodifiers = geomodifiers, geogenerators = geogenerators
Preview/Node | net.maxon.node.base.nodepreviewimage | maxon::ImageBaseRef | Attribute | false | false | false |  |  |  | 
Context/Context | <context | maxon::ShadingContext | Input | false | false | false |  |  |  | 
Context/Local Context | <contextlocal | maxon::ShadingContext | Input | false | false | false |  |  |  | 
Inputs/Blending Space | <colorspace | maxon::InternedId | Input | false | false | true |  |  | linear | Linear = linear, sRGB = srgb
Inputs/Gradient | <gradient | net.maxon.render.portbundle.gradient | Input | true | true | false |  |  |  | 
Inputs/Gradient/Knot.1 | <gradient/_0 | net.maxon.render.portbundle.gradient | Input | false | false | false |  |  |  | 
Inputs/Gradient/Knot.1/Bias Position | <gradient/_0/bias | maxon::Float | Input | false | false | false |  | 1 | 0.5 | 
Inputs/Gradient/Knot.1/Color | <gradient/_0/color | maxon::ColorA | Input | false | false | false |  |  | (1,1,1,1) | 
Inputs/Gradient/Knot.1/Interpolation | <gradient/_0/interpolation | maxon::InternedId | Input | false | false | true |  |  | smoothknot | Smooth = smoothknot, Cubic = cubicknot, Cubic Bias = cubicbias, Linear = linearknot, Step = none, Blend = blend
Inputs/Gradient/Knot.1/Knot Position | <gradient/_0/position | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Inputs/Gradient/Knot.2 | <gradient/_1 | net.maxon.render.portbundle.gradient | Input | false | false | false |  |  |  | 
Inputs/Gradient/Knot.2/Bias Position | <gradient/_1/bias | maxon::Float | Input | false | false | false |  | 1 | 0.5 | 
Inputs/Gradient/Knot.2/Color | <gradient/_1/color | maxon::ColorA | Input | false | false | false |  |  | (1,1,1,1) | 
Inputs/Gradient/Knot.2/Interpolation | <gradient/_1/interpolation | maxon::InternedId | Input | false | false | true |  |  | smoothknot | Smooth = smoothknot, Cubic = cubicknot, Cubic Bias = cubicbias, Linear = linearknot, Step = none, Blend = blend
Inputs/Gradient/Knot.2/Knot Position | <gradient/_1/position | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Inputs/Position | <input | maxon::Float | Input | false | false | false |  |  |  | 
Outputs/Result | >result | maxon::ColorA | Output | false | false | false |  |  |  | 

