# Node Template: Patterns Generator

- **Node Space ID:** `net.maxon.neutron.nodespace`
- **Template ID:** `patternsgenerator@5c4b27ac-dfe2-4fe5-8e14-2e689feb6583`
- **Template Name:** `Patterns Generator`

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
Context | <inport@Jw3ydEg9EhAtIw$hpQvHzQ | maxon::ShadingContext | Input | false | false | false |  |  |  | 
Inputs/Color | <inport@L_qRjrBBHRIj26AicGDd0h | net.maxon.render.portbundle.gradient | Input | true | true | false |  |  |  | 
Inputs/Color/Knot.1 | <inport@L_qRjrBBHRIj26AicGDd0h/_0 | net.maxon.render.portbundle.gradient | Input | false | false | false |  |  |  | 
Inputs/Color/Knot.1/Bias Position | <inport@L_qRjrBBHRIj26AicGDd0h/_0/bias | maxon::Float | Input | false | false | false |  | 1 | 0.5 | 
Inputs/Color/Knot.1/Color | <inport@L_qRjrBBHRIj26AicGDd0h/_0/color | maxon::ColorA | Input | false | false | false |  |  | (1,1,1,1) | 
Inputs/Color/Knot.1/Interpolation | <inport@L_qRjrBBHRIj26AicGDd0h/_0/interpolation | maxon::InternedId | Input | false | false | true |  |  | smoothknot | Smooth = smoothknot, Cubic = cubicknot, Cubic Bias = cubicbias, Linear = linearknot, Step = none, Blend = blend
Inputs/Color/Knot.1/Knot Position | <inport@L_qRjrBBHRIj26AicGDd0h/_0/position | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Inputs/Color/Knot.2 | <inport@L_qRjrBBHRIj26AicGDd0h/_1 | net.maxon.render.portbundle.gradient | Input | false | false | false |  |  |  | 
Inputs/Color/Knot.2/Bias Position | <inport@L_qRjrBBHRIj26AicGDd0h/_1/bias | maxon::Float | Input | false | false | false |  | 1 | 0.5 | 
Inputs/Color/Knot.2/Color | <inport@L_qRjrBBHRIj26AicGDd0h/_1/color | maxon::ColorA | Input | false | false | false |  |  | (1,1,1,1) | 
Inputs/Color/Knot.2/Interpolation | <inport@L_qRjrBBHRIj26AicGDd0h/_1/interpolation | maxon::InternedId | Input | false | false | true |  |  | smoothknot | Smooth = smoothknot, Cubic = cubicknot, Cubic Bias = cubicbias, Linear = linearknot, Step = none, Blend = blend
Inputs/Color/Knot.2/Knot Position | <inport@L_qRjrBBHRIj26AicGDd0h/_1/position | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Inputs/Hollow | <inport@L2i9szALFtOlshir6rZkgi | maxon::Bool | Input | false | false | false |  |  | true | 
Inputs/Hollow Radius | <inport@AJkoQ78yFNMsP4yepdQVgj | maxon::Float64 | Input | false | false | false |  | 1 | 0.95 | 
Inputs/Pattern Type | <inport@fOVG$_VDDR_s3KBDoQkDh3 | maxon::Int64 | Input | false | false | true |  |  | 1 | Circles = 0, Squares = 1, Triangles = 2, Stars = 3
Inputs/Repetitions | <inport@Fk0XmegiOpggbpTsmtbsik | maxon::Int64 | Input | false | false | false | 1 | 80 | 2 | 
Inputs/Rotation | <inport@W7adEQwVIBqhDpVgRhAAbl | maxon::Float64 | Input | false | false | false |  | 1.571 | 0.785 | 
Inputs/Scale | <inport@MPD6Pfp9AFDgrTehfXfnri | maxon::Float64 | Input | false | false | false | 0 | 1 | 0.7 | 
Inputs/Softness | <inport@R8S_stNsHlqkRWXIMC$oHj | maxon::Float64 | Input | false | false | false |  | 1 | 0.02 | 
Inputs/Sub Level | <inport@PvWCB2ciHtEgFfQx3LvUly | maxon::Bool | Input | false | false | false |  |  | true | 
Inputs/Sub Level Hollow | <inport@M9QK8TxdLpsrMpo$XNQoAm | maxon::Bool | Input | false | false | false |  |  | false | 
Inputs/Sub Level Hollow Radius | <inport@GCfbNXCVJ5LqEHWSZITqyg | maxon::Float64 | Input | false | false | false |  | 1 | 0.5 | 
Inputs/Sub Level Mix | <inport@QwhqvsUMOxPtHFwY_$NGoi | maxon::Int64 | Input | false | false | true |  |  | 2 | Multiply = 0, Add = 2, Substract = 1
Inputs/Sub Level Pattern Type | <inport@crUIwRdNGtGrSbEtojmr1N | maxon::Int64 | Input | false | false | true |  |  | 1 | Circles = 0, Squares = 1, Triangles = 2, Stars = 3
Outputs/Result | >result@cry7z8vWElaik$AJm6Udcn | maxon::ColorA64 | Output | false | false | false |  |  |  | 

