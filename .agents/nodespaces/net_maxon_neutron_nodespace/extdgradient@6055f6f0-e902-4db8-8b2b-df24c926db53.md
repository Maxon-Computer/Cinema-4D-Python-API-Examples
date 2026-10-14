# Node Template: Gradient

- **Node Space ID:** `net.maxon.neutron.nodespace`
- **Template ID:** `extdgradient@6055f6f0-e902-4db8-8b2b-df24c926db53`
- **Template Name:** `Gradient`

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
Context/Context | <inport@Db_e4UipLRTryEINg2hafI | maxon::ShadingContext | Input | false | false | false |  |  |  | 
Inputs/Blending Space | <inport@Tv4Af3MhA5mqyP1P82osrC | maxon::InternedId | Input | false | false | true |  |  | linear | Linear = linear, sRGB = srgb
Inputs/Distortion/Color | <inport@d_YWIjFHJ51rfxBI66lefC | maxon::Color64 | Input | false | false | false |  |  |  | 
Inputs/Distortion/Distortion | <inport@N1DoUpr6GJZrp1geaEo7hD | maxon::Bool | Input | false | false | false |  |  |  | 
Inputs/Distortion/Strength | <inport@YFI16g1kN5ZibgNUg$fLFB | maxon::Float64 | Input | false | false | false |  |  | 0 | 
Inputs/Gradient | <inport@4Q7FT7wVIdXg0BV$4nhiRC | net.maxon.render.portbundle.gradient | Input | true | true | false |  |  |  | 
Inputs/Gradient/Knot.1 | <inport@4Q7FT7wVIdXg0BV$4nhiRC/DHerTpxvNd5iqRxnXefim$ | net.maxon.render.portbundle.gradient | Input | false | false | false |  |  |  | 
Inputs/Gradient/Knot.1/Bias Position | <inport@4Q7FT7wVIdXg0BV$4nhiRC/DHerTpxvNd5iqRxnXefim$/bias | maxon::Float | Input | false | false | false |  | 1 | 0.5 | 
Inputs/Gradient/Knot.1/Color | <inport@4Q7FT7wVIdXg0BV$4nhiRC/DHerTpxvNd5iqRxnXefim$/color | maxon::ColorA | Input | false | false | false |  |  | (1,1,1,1) | 
Inputs/Gradient/Knot.1/Interpolation | <inport@4Q7FT7wVIdXg0BV$4nhiRC/DHerTpxvNd5iqRxnXefim$/interpolation | maxon::InternedId | Input | false | false | true |  |  | smoothknot | Smooth = smoothknot, Cubic = cubicknot, Cubic Bias = cubicbias, Linear = linearknot, Step = none, Blend = blend
Inputs/Gradient/Knot.1/Knot Position | <inport@4Q7FT7wVIdXg0BV$4nhiRC/DHerTpxvNd5iqRxnXefim$/position | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Inputs/Gradient/Knot.2 | <inport@4Q7FT7wVIdXg0BV$4nhiRC/ECFw1B0qBxxmUfdUonedGA | net.maxon.render.portbundle.gradient | Input | false | false | false |  |  |  | 
Inputs/Gradient/Knot.2/Bias Position | <inport@4Q7FT7wVIdXg0BV$4nhiRC/ECFw1B0qBxxmUfdUonedGA/bias | maxon::Float | Input | false | false | false |  | 1 | 0.5 | 
Inputs/Gradient/Knot.2/Color | <inport@4Q7FT7wVIdXg0BV$4nhiRC/ECFw1B0qBxxmUfdUonedGA/color | maxon::ColorA | Input | false | false | false |  |  | (1,1,1,1) | 
Inputs/Gradient/Knot.2/Interpolation | <inport@4Q7FT7wVIdXg0BV$4nhiRC/ECFw1B0qBxxmUfdUonedGA/interpolation | maxon::InternedId | Input | false | false | true |  |  | smoothknot | Smooth = smoothknot, Cubic = cubicknot, Cubic Bias = cubicbias, Linear = linearknot, Step = none, Blend = blend
Inputs/Gradient/Knot.2/Knot Position | <inport@4Q7FT7wVIdXg0BV$4nhiRC/ECFw1B0qBxxmUfdUonedGA/position | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Inputs/Position | <inport@7tur9_CEBVUl9A7ZFkTAoC | maxon::Float64 | Input | false | false | false |  |  |  | 
Inputs/Projection/Corners | <inport@XxsRT4tiM5kiMHHctgiTwA | maxon::Int64 | Input | false | false | false |  |  | 3 | 
Inputs/Projection/Flip | <inport@pHnSH7$_O19rWdyaxJ8JBD | maxon::Bool | Input | false | false | false |  |  |  | 
Inputs/Projection/Local Length | <inport@7XKJQOleAdutmY3C6nG5ZD | maxon::Vector2d64 | Input | false | false | false |  |  | (1,1) | 
Inputs/Projection/Local Offset | <inport@slm6K63uKZGtS$hktwL13D | maxon::Vector2d64 | Input | false | false | false |  |  |  | 
Inputs/Projection/Local Pivot | <inport@4cpZiTT2GJaozmlta9C2yD | maxon::Vector2d64 | Input | false | false | false |  |  | (0.5,0.5) | 
Inputs/Projection/Local Repetitions | <inport@1RZwyklZNN1ngNAkopqSHA | maxon::Vector2d64 | Input | false | false | false |  |  | (1,1) | 
Inputs/Projection/Local Rotation | <inport@xY2ofPa9OZxl9DdeJ0v5SC | maxon::Float64 | Input | false | false | false |  |  |  | 
Inputs/Projection/Mirror | <inport@b1L7nEddJdHkxuc4arqEbD | maxon::Bool | Input | false | false | false |  |  |  | 
Inputs/Projection/Mode | <inport@8CNbr3avDlgtyaJAIiUkND | maxon::InternedId | Input | false | false | true |  |  | angular | Angular = angular, Circular = circular, Radial = radial, Box = box, Star = star, N-Angle = n_angle
Inputs/Projection/Repeat | <inport@t7OamZZDFldsOKObpbro3A | maxon::Bool | Input | false | false | false |  |  |  | 
Inputs/Projection/Repetitions | <inport@OQSqc_QmCtqqCrY6Ydp$pB | maxon::Float64 | Input | false | false | false |  |  | 1 | 
Inputs/Projection/Rotation | <inport@$3_zz0dRPVSgumLFMYzLWC | maxon::Float64 | Input | false | false | false |  |  |  | 
Outputs/Result | >result@pdpWS2SKIxYho08mURfn3D | maxon::ColorA64 | Output | false | false | false |  |  |  | 

