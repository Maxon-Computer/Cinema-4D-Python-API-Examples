# Node Template: Edge Distribution

- **Node Space ID:** `net.maxon.neutron.nodespace`
- **Template ID:** `com.rocketlasso.neutron.asset.distribution.edge`
- **Template Name:** `Edge Distribution`

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
Color/Color | <color1 | maxon::Color64 | Input | false | false | false |  |  | (0.312,0.116,0.1) | 
Color/Color | <in@Wur$W$COHlRl2xBwtXtLcF | maxon::Color64 | Input | false | false | false |  |  | (0.312,0.116,0.1) | 
Color/Gradient | <in@bY97i0ObOpzm5azFbOCs2J | net.maxon.render.portbundle.gradient | Input | true | true | false |  |  |  | 
Color/Gradient | <in@dwle1zR8CFirIS3mdCwznl | net.maxon.render.portbundle.gradient | Input | true | true | false |  |  |  | 
Color/Gradient/Knot.1 | <in@bY97i0ObOpzm5azFbOCs2J/_0 | net.maxon.render.portbundle.gradient | Input | false | false | false |  |  |  | 
Color/Gradient/Knot.1 | <in@dwle1zR8CFirIS3mdCwznl/_0 | net.maxon.render.portbundle.gradient | Input | false | false | false |  |  |  | 
Color/Gradient/Knot.1/Bias Position | <in@bY97i0ObOpzm5azFbOCs2J/_0/bias | maxon::Float | Input | false | false | false |  | 1 | 0.5 | 
Color/Gradient/Knot.1/Bias Position | <in@dwle1zR8CFirIS3mdCwznl/_0/bias | maxon::Float | Input | false | false | false |  | 1 | 0.5 | 
Color/Gradient/Knot.1/Color | <in@bY97i0ObOpzm5azFbOCs2J/_0/color | maxon::ColorA | Input | false | false | false |  |  | (1,1,1,1) | 
Color/Gradient/Knot.1/Color | <in@dwle1zR8CFirIS3mdCwznl/_0/color | maxon::ColorA | Input | false | false | false |  |  | (1,1,1,1) | 
Color/Gradient/Knot.1/Interpolation | <in@bY97i0ObOpzm5azFbOCs2J/_0/interpolation | maxon::InternedId | Input | false | false | true |  |  | smoothknot | Smooth = smoothknot, Cubic = cubicknot, Cubic Bias = cubicbias, Linear = linearknot, Step = none, Blend = blend
Color/Gradient/Knot.1/Interpolation | <in@dwle1zR8CFirIS3mdCwznl/_0/interpolation | maxon::InternedId | Input | false | false | true |  |  | smoothknot | Smooth = smoothknot, Cubic = cubicknot, Cubic Bias = cubicbias, Linear = linearknot, Step = none, Blend = blend
Color/Gradient/Knot.1/Knot Position | <in@bY97i0ObOpzm5azFbOCs2J/_0/position | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Color/Gradient/Knot.1/Knot Position | <in@dwle1zR8CFirIS3mdCwznl/_0/position | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Color/Gradient/Knot.2 | <in@bY97i0ObOpzm5azFbOCs2J/_2 | net.maxon.render.portbundle.gradient | Input | false | false | false |  |  |  | 
Color/Gradient/Knot.2 | <in@dwle1zR8CFirIS3mdCwznl/_2 | net.maxon.render.portbundle.gradient | Input | false | false | false |  |  |  | 
Color/Gradient/Knot.2/Bias Position | <in@bY97i0ObOpzm5azFbOCs2J/_2/bias | maxon::Float | Input | false | false | false |  | 1 | 0.5 | 
Color/Gradient/Knot.2/Bias Position | <in@dwle1zR8CFirIS3mdCwznl/_2/bias | maxon::Float | Input | false | false | false |  | 1 | 0.5 | 
Color/Gradient/Knot.2/Color | <in@bY97i0ObOpzm5azFbOCs2J/_2/color | maxon::ColorA | Input | false | false | false |  |  | (1,1,1,1) | 
Color/Gradient/Knot.2/Color | <in@dwle1zR8CFirIS3mdCwznl/_2/color | maxon::ColorA | Input | false | false | false |  |  | (1,1,1,1) | 
Color/Gradient/Knot.2/Interpolation | <in@bY97i0ObOpzm5azFbOCs2J/_2/interpolation | maxon::InternedId | Input | false | false | true |  |  | smoothknot | Smooth = smoothknot, Cubic = cubicknot, Cubic Bias = cubicbias, Linear = linearknot, Step = none, Blend = blend
Color/Gradient/Knot.2/Interpolation | <in@dwle1zR8CFirIS3mdCwznl/_2/interpolation | maxon::InternedId | Input | false | false | true |  |  | smoothknot | Smooth = smoothknot, Cubic = cubicknot, Cubic Bias = cubicbias, Linear = linearknot, Step = none, Blend = blend
Color/Gradient/Knot.2/Knot Position | <in@bY97i0ObOpzm5azFbOCs2J/_2/position | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Color/Gradient/Knot.2/Knot Position | <in@dwle1zR8CFirIS3mdCwznl/_2/position | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Color/Gradient/Knot.3 | <in@bY97i0ObOpzm5azFbOCs2J/_3 | net.maxon.render.portbundle.gradient | Input | false | false | false |  |  |  | 
Color/Gradient/Knot.3 | <in@dwle1zR8CFirIS3mdCwznl/_3 | net.maxon.render.portbundle.gradient | Input | false | false | false |  |  |  | 
Color/Gradient/Knot.3/Bias Position | <in@bY97i0ObOpzm5azFbOCs2J/_3/bias | maxon::Float | Input | false | false | false |  | 1 | 0.5 | 
Color/Gradient/Knot.3/Bias Position | <in@dwle1zR8CFirIS3mdCwznl/_3/bias | maxon::Float | Input | false | false | false |  | 1 | 0.5 | 
Color/Gradient/Knot.3/Color | <in@bY97i0ObOpzm5azFbOCs2J/_3/color | maxon::ColorA | Input | false | false | false |  |  | (1,1,1,1) | 
Color/Gradient/Knot.3/Color | <in@dwle1zR8CFirIS3mdCwznl/_3/color | maxon::ColorA | Input | false | false | false |  |  | (1,1,1,1) | 
Color/Gradient/Knot.3/Interpolation | <in@bY97i0ObOpzm5azFbOCs2J/_3/interpolation | maxon::InternedId | Input | false | false | true |  |  | smoothknot | Smooth = smoothknot, Cubic = cubicknot, Cubic Bias = cubicbias, Linear = linearknot, Step = none, Blend = blend
Color/Gradient/Knot.3/Interpolation | <in@dwle1zR8CFirIS3mdCwznl/_3/interpolation | maxon::InternedId | Input | false | false | true |  |  | smoothknot | Smooth = smoothknot, Cubic = cubicknot, Cubic Bias = cubicbias, Linear = linearknot, Step = none, Blend = blend
Color/Gradient/Knot.3/Knot Position | <in@bY97i0ObOpzm5azFbOCs2J/_3/position | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Color/Gradient/Knot.3/Knot Position | <in@dwle1zR8CFirIS3mdCwznl/_3/position | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Color/Gradient/Knot.4 | <in@bY97i0ObOpzm5azFbOCs2J/_4 | net.maxon.render.portbundle.gradient | Input | false | false | false |  |  |  | 
Color/Gradient/Knot.4 | <in@dwle1zR8CFirIS3mdCwznl/_4 | net.maxon.render.portbundle.gradient | Input | false | false | false |  |  |  | 
Color/Gradient/Knot.4/Bias Position | <in@bY97i0ObOpzm5azFbOCs2J/_4/bias | maxon::Float | Input | false | false | false |  | 1 | 0.5 | 
Color/Gradient/Knot.4/Bias Position | <in@dwle1zR8CFirIS3mdCwznl/_4/bias | maxon::Float | Input | false | false | false |  | 1 | 0.5 | 
Color/Gradient/Knot.4/Color | <in@bY97i0ObOpzm5azFbOCs2J/_4/color | maxon::ColorA | Input | false | false | false |  |  | (1,1,1,1) | 
Color/Gradient/Knot.4/Color | <in@dwle1zR8CFirIS3mdCwznl/_4/color | maxon::ColorA | Input | false | false | false |  |  | (1,1,1,1) | 
Color/Gradient/Knot.4/Interpolation | <in@bY97i0ObOpzm5azFbOCs2J/_4/interpolation | maxon::InternedId | Input | false | false | true |  |  | smoothknot | Smooth = smoothknot, Cubic = cubicknot, Cubic Bias = cubicbias, Linear = linearknot, Step = none, Blend = blend
Color/Gradient/Knot.4/Interpolation | <in@dwle1zR8CFirIS3mdCwznl/_4/interpolation | maxon::InternedId | Input | false | false | true |  |  | smoothknot | Smooth = smoothknot, Cubic = cubicknot, Cubic Bias = cubicbias, Linear = linearknot, Step = none, Blend = blend
Color/Gradient/Knot.4/Knot Position | <in@bY97i0ObOpzm5azFbOCs2J/_4/position | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Color/Gradient/Knot.4/Knot Position | <in@dwle1zR8CFirIS3mdCwznl/_4/position | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Color/Gradient/Knot.5 | <in@bY97i0ObOpzm5azFbOCs2J/_8 | net.maxon.render.portbundle.gradient | Input | false | false | false |  |  |  | 
Color/Gradient/Knot.5 | <in@dwle1zR8CFirIS3mdCwznl/_8 | net.maxon.render.portbundle.gradient | Input | false | false | false |  |  |  | 
Color/Gradient/Knot.5/Bias Position | <in@bY97i0ObOpzm5azFbOCs2J/_8/bias | maxon::Float | Input | false | false | false |  | 1 | 0.5 | 
Color/Gradient/Knot.5/Bias Position | <in@dwle1zR8CFirIS3mdCwznl/_8/bias | maxon::Float | Input | false | false | false |  | 1 | 0.5 | 
Color/Gradient/Knot.5/Color | <in@bY97i0ObOpzm5azFbOCs2J/_8/color | maxon::ColorA | Input | false | false | false |  |  | (1,1,1,1) | 
Color/Gradient/Knot.5/Color | <in@dwle1zR8CFirIS3mdCwznl/_8/color | maxon::ColorA | Input | false | false | false |  |  | (1,1,1,1) | 
Color/Gradient/Knot.5/Interpolation | <in@bY97i0ObOpzm5azFbOCs2J/_8/interpolation | maxon::InternedId | Input | false | false | true |  |  | smoothknot | Smooth = smoothknot, Cubic = cubicknot, Cubic Bias = cubicbias, Linear = linearknot, Step = none, Blend = blend
Color/Gradient/Knot.5/Interpolation | <in@dwle1zR8CFirIS3mdCwznl/_8/interpolation | maxon::InternedId | Input | false | false | true |  |  | smoothknot | Smooth = smoothknot, Cubic = cubicknot, Cubic Bias = cubicbias, Linear = linearknot, Step = none, Blend = blend
Color/Gradient/Knot.5/Knot Position | <in@bY97i0ObOpzm5azFbOCs2J/_8/position | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Color/Gradient/Knot.5/Knot Position | <in@dwle1zR8CFirIS3mdCwznl/_8/position | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Color/Gradient/Knot.6 | <in@bY97i0ObOpzm5azFbOCs2J/_10 | net.maxon.render.portbundle.gradient | Input | false | false | false |  |  |  | 
Color/Gradient/Knot.6 | <in@dwle1zR8CFirIS3mdCwznl/_10 | net.maxon.render.portbundle.gradient | Input | false | false | false |  |  |  | 
Color/Gradient/Knot.6/Bias Position | <in@bY97i0ObOpzm5azFbOCs2J/_10/bias | maxon::Float | Input | false | false | false |  | 1 | 0.5 | 
Color/Gradient/Knot.6/Bias Position | <in@dwle1zR8CFirIS3mdCwznl/_10/bias | maxon::Float | Input | false | false | false |  | 1 | 0.5 | 
Color/Gradient/Knot.6/Color | <in@bY97i0ObOpzm5azFbOCs2J/_10/color | maxon::ColorA | Input | false | false | false |  |  | (1,1,1,1) | 
Color/Gradient/Knot.6/Color | <in@dwle1zR8CFirIS3mdCwznl/_10/color | maxon::ColorA | Input | false | false | false |  |  | (1,1,1,1) | 
Color/Gradient/Knot.6/Interpolation | <in@bY97i0ObOpzm5azFbOCs2J/_10/interpolation | maxon::InternedId | Input | false | false | true |  |  | smoothknot | Smooth = smoothknot, Cubic = cubicknot, Cubic Bias = cubicbias, Linear = linearknot, Step = none, Blend = blend
Color/Gradient/Knot.6/Interpolation | <in@dwle1zR8CFirIS3mdCwznl/_10/interpolation | maxon::InternedId | Input | false | false | true |  |  | smoothknot | Smooth = smoothknot, Cubic = cubicknot, Cubic Bias = cubicbias, Linear = linearknot, Step = none, Blend = blend
Color/Gradient/Knot.6/Knot Position | <in@bY97i0ObOpzm5azFbOCs2J/_10/position | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Color/Gradient/Knot.6/Knot Position | <in@dwle1zR8CFirIS3mdCwznl/_10/position | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Color/Gradient/Knot.7 | <in@bY97i0ObOpzm5azFbOCs2J/_11 | net.maxon.render.portbundle.gradient | Input | false | false | false |  |  |  | 
Color/Gradient/Knot.7 | <in@dwle1zR8CFirIS3mdCwznl/_11 | net.maxon.render.portbundle.gradient | Input | false | false | false |  |  |  | 
Color/Gradient/Knot.7/Bias Position | <in@bY97i0ObOpzm5azFbOCs2J/_11/bias | maxon::Float | Input | false | false | false |  | 1 | 0.5 | 
Color/Gradient/Knot.7/Bias Position | <in@dwle1zR8CFirIS3mdCwznl/_11/bias | maxon::Float | Input | false | false | false |  | 1 | 0.5 | 
Color/Gradient/Knot.7/Color | <in@bY97i0ObOpzm5azFbOCs2J/_11/color | maxon::ColorA | Input | false | false | false |  |  | (1,1,1,1) | 
Color/Gradient/Knot.7/Color | <in@dwle1zR8CFirIS3mdCwznl/_11/color | maxon::ColorA | Input | false | false | false |  |  | (1,1,1,1) | 
Color/Gradient/Knot.7/Interpolation | <in@bY97i0ObOpzm5azFbOCs2J/_11/interpolation | maxon::InternedId | Input | false | false | true |  |  | smoothknot | Smooth = smoothknot, Cubic = cubicknot, Cubic Bias = cubicbias, Linear = linearknot, Step = none, Blend = blend
Color/Gradient/Knot.7/Interpolation | <in@dwle1zR8CFirIS3mdCwznl/_11/interpolation | maxon::InternedId | Input | false | false | true |  |  | smoothknot | Smooth = smoothknot, Cubic = cubicknot, Cubic Bias = cubicbias, Linear = linearknot, Step = none, Blend = blend
Color/Gradient/Knot.7/Knot Position | <in@bY97i0ObOpzm5azFbOCs2J/_11/position | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Color/Gradient/Knot.7/Knot Position | <in@dwle1zR8CFirIS3mdCwznl/_11/position | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Color/Gradient/Knot.8 | <in@bY97i0ObOpzm5azFbOCs2J/_12 | net.maxon.render.portbundle.gradient | Input | false | false | false |  |  |  | 
Color/Gradient/Knot.8 | <in@dwle1zR8CFirIS3mdCwznl/_12 | net.maxon.render.portbundle.gradient | Input | false | false | false |  |  |  | 
Color/Gradient/Knot.8/Bias Position | <in@bY97i0ObOpzm5azFbOCs2J/_12/bias | maxon::Float | Input | false | false | false |  | 1 | 0.5 | 
Color/Gradient/Knot.8/Bias Position | <in@dwle1zR8CFirIS3mdCwznl/_12/bias | maxon::Float | Input | false | false | false |  | 1 | 0.5 | 
Color/Gradient/Knot.8/Color | <in@bY97i0ObOpzm5azFbOCs2J/_12/color | maxon::ColorA | Input | false | false | false |  |  | (1,1,1,1) | 
Color/Gradient/Knot.8/Color | <in@dwle1zR8CFirIS3mdCwznl/_12/color | maxon::ColorA | Input | false | false | false |  |  | (1,1,1,1) | 
Color/Gradient/Knot.8/Interpolation | <in@bY97i0ObOpzm5azFbOCs2J/_12/interpolation | maxon::InternedId | Input | false | false | true |  |  | smoothknot | Smooth = smoothknot, Cubic = cubicknot, Cubic Bias = cubicbias, Linear = linearknot, Step = none, Blend = blend
Color/Gradient/Knot.8/Interpolation | <in@dwle1zR8CFirIS3mdCwznl/_12/interpolation | maxon::InternedId | Input | false | false | true |  |  | smoothknot | Smooth = smoothknot, Cubic = cubicknot, Cubic Bias = cubicbias, Linear = linearknot, Step = none, Blend = blend
Color/Gradient/Knot.8/Knot Position | <in@bY97i0ObOpzm5azFbOCs2J/_12/position | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Color/Gradient/Knot.8/Knot Position | <in@dwle1zR8CFirIS3mdCwznl/_12/position | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Color/Gradient/Knot.9 | <in@bY97i0ObOpzm5azFbOCs2J/_5 | net.maxon.render.portbundle.gradient | Input | false | false | false |  |  |  | 
Color/Gradient/Knot.9 | <in@dwle1zR8CFirIS3mdCwznl/_5 | net.maxon.render.portbundle.gradient | Input | false | false | false |  |  |  | 
Color/Gradient/Knot.9/Bias Position | <in@bY97i0ObOpzm5azFbOCs2J/_5/bias | maxon::Float | Input | false | false | false |  | 1 | 0.5 | 
Color/Gradient/Knot.9/Bias Position | <in@dwle1zR8CFirIS3mdCwznl/_5/bias | maxon::Float | Input | false | false | false |  | 1 | 0.5 | 
Color/Gradient/Knot.9/Color | <in@bY97i0ObOpzm5azFbOCs2J/_5/color | maxon::ColorA | Input | false | false | false |  |  | (1,1,1,1) | 
Color/Gradient/Knot.9/Color | <in@dwle1zR8CFirIS3mdCwznl/_5/color | maxon::ColorA | Input | false | false | false |  |  | (1,1,1,1) | 
Color/Gradient/Knot.9/Interpolation | <in@bY97i0ObOpzm5azFbOCs2J/_5/interpolation | maxon::InternedId | Input | false | false | true |  |  | smoothknot | Smooth = smoothknot, Cubic = cubicknot, Cubic Bias = cubicbias, Linear = linearknot, Step = none, Blend = blend
Color/Gradient/Knot.9/Interpolation | <in@dwle1zR8CFirIS3mdCwznl/_5/interpolation | maxon::InternedId | Input | false | false | true |  |  | smoothknot | Smooth = smoothknot, Cubic = cubicknot, Cubic Bias = cubicbias, Linear = linearknot, Step = none, Blend = blend
Color/Gradient/Knot.9/Knot Position | <in@bY97i0ObOpzm5azFbOCs2J/_5/position | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Color/Gradient/Knot.9/Knot Position | <in@dwle1zR8CFirIS3mdCwznl/_5/position | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Color/Gradient/Knot.10 | <in@bY97i0ObOpzm5azFbOCs2J/_6 | net.maxon.render.portbundle.gradient | Input | false | false | false |  |  |  | 
Color/Gradient/Knot.10 | <in@dwle1zR8CFirIS3mdCwznl/_6 | net.maxon.render.portbundle.gradient | Input | false | false | false |  |  |  | 
Color/Gradient/Knot.10/Bias Position | <in@bY97i0ObOpzm5azFbOCs2J/_6/bias | maxon::Float | Input | false | false | false |  | 1 | 0.5 | 
Color/Gradient/Knot.10/Bias Position | <in@dwle1zR8CFirIS3mdCwznl/_6/bias | maxon::Float | Input | false | false | false |  | 1 | 0.5 | 
Color/Gradient/Knot.10/Color | <in@bY97i0ObOpzm5azFbOCs2J/_6/color | maxon::ColorA | Input | false | false | false |  |  | (1,1,1,1) | 
Color/Gradient/Knot.10/Color | <in@dwle1zR8CFirIS3mdCwznl/_6/color | maxon::ColorA | Input | false | false | false |  |  | (1,1,1,1) | 
Color/Gradient/Knot.10/Interpolation | <in@bY97i0ObOpzm5azFbOCs2J/_6/interpolation | maxon::InternedId | Input | false | false | true |  |  | smoothknot | Smooth = smoothknot, Cubic = cubicknot, Cubic Bias = cubicbias, Linear = linearknot, Step = none, Blend = blend
Color/Gradient/Knot.10/Interpolation | <in@dwle1zR8CFirIS3mdCwznl/_6/interpolation | maxon::InternedId | Input | false | false | true |  |  | smoothknot | Smooth = smoothknot, Cubic = cubicknot, Cubic Bias = cubicbias, Linear = linearknot, Step = none, Blend = blend
Color/Gradient/Knot.10/Knot Position | <in@bY97i0ObOpzm5azFbOCs2J/_6/position | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Color/Gradient/Knot.10/Knot Position | <in@dwle1zR8CFirIS3mdCwznl/_6/position | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Color/Gradient/Knot.11 | <in@bY97i0ObOpzm5azFbOCs2J/_7 | net.maxon.render.portbundle.gradient | Input | false | false | false |  |  |  | 
Color/Gradient/Knot.11 | <in@dwle1zR8CFirIS3mdCwznl/_7 | net.maxon.render.portbundle.gradient | Input | false | false | false |  |  |  | 
Color/Gradient/Knot.11/Bias Position | <in@bY97i0ObOpzm5azFbOCs2J/_7/bias | maxon::Float | Input | false | false | false |  | 1 | 0.5 | 
Color/Gradient/Knot.11/Bias Position | <in@dwle1zR8CFirIS3mdCwznl/_7/bias | maxon::Float | Input | false | false | false |  | 1 | 0.5 | 
Color/Gradient/Knot.11/Color | <in@bY97i0ObOpzm5azFbOCs2J/_7/color | maxon::ColorA | Input | false | false | false |  |  | (1,1,1,1) | 
Color/Gradient/Knot.11/Color | <in@dwle1zR8CFirIS3mdCwznl/_7/color | maxon::ColorA | Input | false | false | false |  |  | (1,1,1,1) | 
Color/Gradient/Knot.11/Interpolation | <in@bY97i0ObOpzm5azFbOCs2J/_7/interpolation | maxon::InternedId | Input | false | false | true |  |  | smoothknot | Smooth = smoothknot, Cubic = cubicknot, Cubic Bias = cubicbias, Linear = linearknot, Step = none, Blend = blend
Color/Gradient/Knot.11/Interpolation | <in@dwle1zR8CFirIS3mdCwznl/_7/interpolation | maxon::InternedId | Input | false | false | true |  |  | smoothknot | Smooth = smoothknot, Cubic = cubicknot, Cubic Bias = cubicbias, Linear = linearknot, Step = none, Blend = blend
Color/Gradient/Knot.11/Knot Position | <in@bY97i0ObOpzm5azFbOCs2J/_7/position | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Color/Gradient/Knot.11/Knot Position | <in@dwle1zR8CFirIS3mdCwznl/_7/position | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Color/Gradient/Knot.12 | <in@bY97i0ObOpzm5azFbOCs2J/_9 | net.maxon.render.portbundle.gradient | Input | false | false | false |  |  |  | 
Color/Gradient/Knot.12 | <in@dwle1zR8CFirIS3mdCwznl/_9 | net.maxon.render.portbundle.gradient | Input | false | false | false |  |  |  | 
Color/Gradient/Knot.12/Bias Position | <in@bY97i0ObOpzm5azFbOCs2J/_9/bias | maxon::Float | Input | false | false | false |  | 1 | 0.5 | 
Color/Gradient/Knot.12/Bias Position | <in@dwle1zR8CFirIS3mdCwznl/_9/bias | maxon::Float | Input | false | false | false |  | 1 | 0.5 | 
Color/Gradient/Knot.12/Color | <in@bY97i0ObOpzm5azFbOCs2J/_9/color | maxon::ColorA | Input | false | false | false |  |  | (1,1,1,1) | 
Color/Gradient/Knot.12/Color | <in@dwle1zR8CFirIS3mdCwznl/_9/color | maxon::ColorA | Input | false | false | false |  |  | (1,1,1,1) | 
Color/Gradient/Knot.12/Interpolation | <in@bY97i0ObOpzm5azFbOCs2J/_9/interpolation | maxon::InternedId | Input | false | false | true |  |  | smoothknot | Smooth = smoothknot, Cubic = cubicknot, Cubic Bias = cubicbias, Linear = linearknot, Step = none, Blend = blend
Color/Gradient/Knot.12/Interpolation | <in@dwle1zR8CFirIS3mdCwznl/_9/interpolation | maxon::InternedId | Input | false | false | true |  |  | smoothknot | Smooth = smoothknot, Cubic = cubicknot, Cubic Bias = cubicbias, Linear = linearknot, Step = none, Blend = blend
Color/Gradient/Knot.12/Knot Position | <in@bY97i0ObOpzm5azFbOCs2J/_9/position | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Color/Gradient/Knot.12/Knot Position | <in@dwle1zR8CFirIS3mdCwznl/_9/position | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Color/Gradient/Knot.13 | <in@bY97i0ObOpzm5azFbOCs2J/_1 | net.maxon.render.portbundle.gradient | Input | false | false | false |  |  |  | 
Color/Gradient/Knot.13 | <in@dwle1zR8CFirIS3mdCwznl/_1 | net.maxon.render.portbundle.gradient | Input | false | false | false |  |  |  | 
Color/Gradient/Knot.13/Bias Position | <in@bY97i0ObOpzm5azFbOCs2J/_1/bias | maxon::Float | Input | false | false | false |  | 1 | 0.5 | 
Color/Gradient/Knot.13/Bias Position | <in@dwle1zR8CFirIS3mdCwznl/_1/bias | maxon::Float | Input | false | false | false |  | 1 | 0.5 | 
Color/Gradient/Knot.13/Color | <in@bY97i0ObOpzm5azFbOCs2J/_1/color | maxon::ColorA | Input | false | false | false |  |  | (1,1,1,1) | 
Color/Gradient/Knot.13/Color | <in@dwle1zR8CFirIS3mdCwznl/_1/color | maxon::ColorA | Input | false | false | false |  |  | (1,1,1,1) | 
Color/Gradient/Knot.13/Interpolation | <in@bY97i0ObOpzm5azFbOCs2J/_1/interpolation | maxon::InternedId | Input | false | false | true |  |  | smoothknot | Smooth = smoothknot, Cubic = cubicknot, Cubic Bias = cubicbias, Linear = linearknot, Step = none, Blend = blend
Color/Gradient/Knot.13/Interpolation | <in@dwle1zR8CFirIS3mdCwznl/_1/interpolation | maxon::InternedId | Input | false | false | true |  |  | smoothknot | Smooth = smoothknot, Cubic = cubicknot, Cubic Bias = cubicbias, Linear = linearknot, Step = none, Blend = blend
Color/Gradient/Knot.13/Knot Position | <in@bY97i0ObOpzm5azFbOCs2J/_1/position | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Color/Gradient/Knot.13/Knot Position | <in@dwle1zR8CFirIS3mdCwznl/_1/position | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Color/Sample Mode | <enum5 | maxon::Int64 | Input | false | false | true |  |  |  | Constant = 0, Linear = 1, Random = 2
Color/Sample Mode | <in@Hb68hCFXDhEsQJB4ze7YNH | maxon::Int64 | Input | false | false | true |  |  |  | Constant = 0, Linear = 1, Random = 2
Edges/Align Clone | <in@BWVidrjQH55jF5VKQwGjxN | maxon::Bool | Input | false | false | false |  |  | true | 
Edges/Animation Speed | <in@e26USF7oPt5hySsVi0AQLM | maxon::Float64 | Input | false | false | false |  |  | 0 | 
Edges/Center Bias | <in@XTRiyTZ0OtJkpWlJZH_sZP | maxon::Float64 | Input | false | false | false | -1 | 1 | 0 | 
Edges/Cloner Children | <clonerchildrenin | maxon::ArrayContainer<maxon::Matrix, maxon::Matrix, maxon::GeometryObject, maxon::GeometryObject, maxon::Range<maxon::Vector>, maxon::String> | Input | false | false | false |  |  |  | 
Edges/Clones | <enum | maxon::Int64 | Input | false | false | true |  |  |  | Iterate = 0, Random = 1
Edges/Count | <integer | maxon::Int64 | Input | false | false | false |  |  | 10 | 
Edges/Distribution | <in@AbtDZZ4rFJiowiOY53rd5a | maxon::Int64 | Input | false | false | true |  |  |  | Count = 0, Step = 1, Object = 2
Edges/Extra Gap | <in@K4NpVxh1DJMvayXKfhmXnM | maxon::Float64 | Input | false | false | false |  |  |  | 
Edges/Gap | <float2 | maxon::Float64 | Input | false | false | false |  |  |  | 
Edges/Global Cloner Matrix | <globalclonermatrixin | maxon::Matrix | Input | false | false | false |  |  |  | 
Edges/Invert | <bool2 | maxon::Bool | Input | false | false | false |  |  | true | 
Edges/Local Cloner Matrix | <localclonermatrixin | maxon::Matrix | Input | false | false | false |  |  |  | 
Edges/Max Angle | <in@I5qL1TruElZixIyqZnuE_s | maxon::Float64 | Input | false | false | false |  | 3.142 | 3.142 | 
Edges/Min Angle | <float3 | maxon::Float64 | Input | false | false | false |  | 3.142 | 0 | 
Edges/Objects Children | <objectchildren | maxon::ArrayContainer<maxon::GeometryObject, maxon::Matrix64, maxon::Matrix64, maxon::ColorA64, maxon::String> | Input | false | false | false |  |  |  | 
Edges/Offset Mode | <in@K$h20v8bFFVn4ywuyCcz3J | maxon::Int64 | Input | false | false | true |  |  | 1 | Absolute = 0, Object = 1
Edges/Outline | <in@cfEM5olJHZhgrVjzOUNuzk | maxon::Bool | Input | false | false | false |  |  | true | 
Edges/Override Scale | <float5 | maxon::Float64 | Input | false | false | false | 0 |  | 1 | 
Edges/Pinch | <in@L_gMKPkVAJxrjkYXglCrCE | maxon::Float64 | Input | false | false | false |  |  |  | 
Edges/PreRotate | <vector | maxon::Vector64 | Input | false | false | false |  |  |  | 
Edges/Randomness | <in@eAiLCvCVL5mlee8VR3QI7J | maxon::Float64 | Input | false | false | false |  |  | 0 | 
Edges/Return Edges | <in@Y4nFYv9CNFvl0VaQZ3a2F_ | maxon::Bool | Input | false | false | false |  |  | true | 
Edges/Scaling Axis | <enum3 | maxon::Int64 | Input | false | false | true |  |  |  | Direction = 0, Uniform = 1
Edges/Scaling Axis | <in@JSvVKSzEPJomWO18$v$99M | maxon::Int64 | Input | false | false | true |  |  | 1 | Direction = 0, Uniform = 1
Edges/Seed | <float1 | maxon::Float64 | Input | false | false | false |  |  | 12345 | 
Edges/Selection | <string | maxon::String | Input | false | false | false |  |  |  | 
Edges/Spacing | <in@C_RM2EFJO53qWRU2uFRHVL | maxon::Int64 | Input | false | false | true |  |  |  | Scale Geometry = 0, Even Gaps = 1, End Cap Gaps = 2, Remainder Gap = 3
Edges/Start/End Bias | <in@M34mS_p4GRig2zSQRJYrQK | maxon::Float64 | Input | false | false | false | -1 | 1 | 0 | 
Edges/Step | <float6 | maxon::Float64 | Input | false | false | false |  |  | 5 | 
Edges/Surface Offset | <in@JRm9J3vsPJfrv9MUEaed2P | maxon::Float64 | Input | false | false | false |  |  | 0 | 
Edges/Surface Offset | <in@VKzb3E0JF5wmAIxCP8etVk | maxon::Float64 | Input | false | false | false |  |  | 0 | 
Points/Enable Points | <bool3 | maxon::Bool | Input | false | false | false |  |  | true | 
Points/Return Points | <in@IHwR8XYYDZhowOFYFA21M4 | maxon::Bool | Input | false | false | false |  |  | true | 
Points/Scale | <float4 | maxon::Float64 | Input | false | false | false |  |  | 1 | 
Points/Selection | <in@GIkd48IwPZju3MU006N9tF | maxon::String | Input | false | false | false |  |  |  | 
Outputs/Distribution | >distdataout | maxon::ArrayContainer<maxon::Matrix64, maxon::Int64, maxon::Int64, maxon::Vector64, maxon::Color64, maxon::Int64> | Output | false | false | false |  |  |  | 

