# Node Template: Falloff

- **Node Space ID:** `net.maxon.nodespace.standard`
- **Template ID:** `falloff@ae7af06f-520c-4315-9f65-ae00da8f28a5`
- **Template Name:** `Falloff`

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
Inputs/Gradient/Dir Mode | <inport@$hiyCcICJ1EnNKqBXWUdOp | maxon::Int64 | Input | false | false | true |  |  |  | Forward = 0, Backward = 1, Both = 2
Inputs/Gradient/Direction | <inport@d6dFhDd9M9dld325c9oWxq | maxon::Vector64 | Input | false | false | false |  |  | (0,1,0) | 
Inputs/Gradient/Gradient | <inport@RjnkYsxTOxGtWbYoCinGqA | net.maxon.render.portbundle.gradient | Input | true | true | false |  |  |  | 
Inputs/Gradient/Gradient/Knot.1 | <inport@RjnkYsxTOxGtWbYoCinGqA/_0 | net.maxon.render.portbundle.gradient | Input | false | false | false |  |  |  | 
Inputs/Gradient/Gradient/Knot.1/Bias Position | <inport@RjnkYsxTOxGtWbYoCinGqA/_0/bias | maxon::Float | Input | false | false | false |  | 1 | 0.5 | 
Inputs/Gradient/Gradient/Knot.1/Color | <inport@RjnkYsxTOxGtWbYoCinGqA/_0/color | maxon::ColorA | Input | false | false | false |  |  | (1,1,1,1) | 
Inputs/Gradient/Gradient/Knot.1/Interpolation | <inport@RjnkYsxTOxGtWbYoCinGqA/_0/interpolation | maxon::InternedId | Input | false | false | true |  |  | smoothknot | Smooth = smoothknot, Cubic = cubicknot, Cubic Bias = cubicbias, Linear = linearknot, Step = none, Blend = blend
Inputs/Gradient/Gradient/Knot.1/Knot Position | <inport@RjnkYsxTOxGtWbYoCinGqA/_0/position | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Inputs/Gradient/Gradient/Knot.2 | <inport@RjnkYsxTOxGtWbYoCinGqA/_1 | net.maxon.render.portbundle.gradient | Input | false | false | false |  |  |  | 
Inputs/Gradient/Gradient/Knot.2/Bias Position | <inport@RjnkYsxTOxGtWbYoCinGqA/_1/bias | maxon::Float | Input | false | false | false |  | 1 | 0.5 | 
Inputs/Gradient/Gradient/Knot.2/Color | <inport@RjnkYsxTOxGtWbYoCinGqA/_1/color | maxon::ColorA | Input | false | false | false |  |  | (1,1,1,1) | 
Inputs/Gradient/Gradient/Knot.2/Interpolation | <inport@RjnkYsxTOxGtWbYoCinGqA/_1/interpolation | maxon::InternedId | Input | false | false | true |  |  | smoothknot | Smooth = smoothknot, Cubic = cubicknot, Cubic Bias = cubicbias, Linear = linearknot, Step = none, Blend = blend
Inputs/Gradient/Gradient/Knot.2/Knot Position | <inport@RjnkYsxTOxGtWbYoCinGqA/_1/position | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Inputs/Gradient/Mode | <hxaNGokrBF_uAFInftJG52 | maxon::Int64 | Input | false | false | true |  |  |  | Front = 0, Front Transparency = 1, Back = 2, Front and Back = 4, Back Transparency = 3, Direction = 5
Outputs/Result | >outport@UM5VgXJiGRitnCEfvqnHh2 | maxon::Color64 | Output | false | false | false |  |  |  | 

