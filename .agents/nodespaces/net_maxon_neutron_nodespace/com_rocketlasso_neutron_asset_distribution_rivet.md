# Node Template: Rivet Distribution

- **Node Space ID:** `net.maxon.neutron.nodespace`
- **Template ID:** `com.rocketlasso.neutron.asset.distribution.rivet`
- **Template Name:** `Rivet Distribution`

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
Color/Color | <color1 | maxon::Color64 | Input | false | false | false |  |  | (0.312,0.116,0.1) | 
Color/Color | <in@Wur$W$COHlRl2xBwtXtLcF | maxon::Color64 | Input | false | false | false |  |  | (0.312,0.116,0.1) | 
Color/Gradient | <in@PqX_wG1PEh5nSYruwgFJNt | net.maxon.render.portbundle.gradient | Input | true | true | false |  |  |  | 
Color/Gradient/Knot.1 | <in@PqX_wG1PEh5nSYruwgFJNt/_0 | net.maxon.render.portbundle.gradient | Input | false | false | false |  |  |  | 
Color/Gradient/Knot.1/Bias Position | <in@PqX_wG1PEh5nSYruwgFJNt/_0/bias | maxon::Float | Input | false | false | false |  | 1 | 0.5 | 
Color/Gradient/Knot.1/Color | <in@PqX_wG1PEh5nSYruwgFJNt/_0/color | maxon::ColorA | Input | false | false | false |  |  | (1,1,1,1) | 
Color/Gradient/Knot.1/Interpolation | <in@PqX_wG1PEh5nSYruwgFJNt/_0/interpolation | maxon::InternedId | Input | false | false | true |  |  | smoothknot | Smooth = smoothknot, Cubic = cubicknot, Cubic Bias = cubicbias, Linear = linearknot, Step = none, Blend = blend
Color/Gradient/Knot.1/Knot Position | <in@PqX_wG1PEh5nSYruwgFJNt/_0/position | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Color/Gradient/Knot.2 | <in@PqX_wG1PEh5nSYruwgFJNt/_2 | net.maxon.render.portbundle.gradient | Input | false | false | false |  |  |  | 
Color/Gradient/Knot.2/Bias Position | <in@PqX_wG1PEh5nSYruwgFJNt/_2/bias | maxon::Float | Input | false | false | false |  | 1 | 0.5 | 
Color/Gradient/Knot.2/Color | <in@PqX_wG1PEh5nSYruwgFJNt/_2/color | maxon::ColorA | Input | false | false | false |  |  | (1,1,1,1) | 
Color/Gradient/Knot.2/Interpolation | <in@PqX_wG1PEh5nSYruwgFJNt/_2/interpolation | maxon::InternedId | Input | false | false | true |  |  | smoothknot | Smooth = smoothknot, Cubic = cubicknot, Cubic Bias = cubicbias, Linear = linearknot, Step = none, Blend = blend
Color/Gradient/Knot.2/Knot Position | <in@PqX_wG1PEh5nSYruwgFJNt/_2/position | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Color/Gradient/Knot.3 | <in@PqX_wG1PEh5nSYruwgFJNt/_3 | net.maxon.render.portbundle.gradient | Input | false | false | false |  |  |  | 
Color/Gradient/Knot.3/Bias Position | <in@PqX_wG1PEh5nSYruwgFJNt/_3/bias | maxon::Float | Input | false | false | false |  | 1 | 0.5 | 
Color/Gradient/Knot.3/Color | <in@PqX_wG1PEh5nSYruwgFJNt/_3/color | maxon::ColorA | Input | false | false | false |  |  | (1,1,1,1) | 
Color/Gradient/Knot.3/Interpolation | <in@PqX_wG1PEh5nSYruwgFJNt/_3/interpolation | maxon::InternedId | Input | false | false | true |  |  | smoothknot | Smooth = smoothknot, Cubic = cubicknot, Cubic Bias = cubicbias, Linear = linearknot, Step = none, Blend = blend
Color/Gradient/Knot.3/Knot Position | <in@PqX_wG1PEh5nSYruwgFJNt/_3/position | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Color/Gradient/Knot.4 | <in@PqX_wG1PEh5nSYruwgFJNt/_4 | net.maxon.render.portbundle.gradient | Input | false | false | false |  |  |  | 
Color/Gradient/Knot.4/Bias Position | <in@PqX_wG1PEh5nSYruwgFJNt/_4/bias | maxon::Float | Input | false | false | false |  | 1 | 0.5 | 
Color/Gradient/Knot.4/Color | <in@PqX_wG1PEh5nSYruwgFJNt/_4/color | maxon::ColorA | Input | false | false | false |  |  | (1,1,1,1) | 
Color/Gradient/Knot.4/Interpolation | <in@PqX_wG1PEh5nSYruwgFJNt/_4/interpolation | maxon::InternedId | Input | false | false | true |  |  | smoothknot | Smooth = smoothknot, Cubic = cubicknot, Cubic Bias = cubicbias, Linear = linearknot, Step = none, Blend = blend
Color/Gradient/Knot.4/Knot Position | <in@PqX_wG1PEh5nSYruwgFJNt/_4/position | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Color/Gradient/Knot.5 | <in@PqX_wG1PEh5nSYruwgFJNt/_8 | net.maxon.render.portbundle.gradient | Input | false | false | false |  |  |  | 
Color/Gradient/Knot.5/Bias Position | <in@PqX_wG1PEh5nSYruwgFJNt/_8/bias | maxon::Float | Input | false | false | false |  | 1 | 0.5 | 
Color/Gradient/Knot.5/Color | <in@PqX_wG1PEh5nSYruwgFJNt/_8/color | maxon::ColorA | Input | false | false | false |  |  | (1,1,1,1) | 
Color/Gradient/Knot.5/Interpolation | <in@PqX_wG1PEh5nSYruwgFJNt/_8/interpolation | maxon::InternedId | Input | false | false | true |  |  | smoothknot | Smooth = smoothknot, Cubic = cubicknot, Cubic Bias = cubicbias, Linear = linearknot, Step = none, Blend = blend
Color/Gradient/Knot.5/Knot Position | <in@PqX_wG1PEh5nSYruwgFJNt/_8/position | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Color/Gradient/Knot.6 | <in@PqX_wG1PEh5nSYruwgFJNt/_10 | net.maxon.render.portbundle.gradient | Input | false | false | false |  |  |  | 
Color/Gradient/Knot.6/Bias Position | <in@PqX_wG1PEh5nSYruwgFJNt/_10/bias | maxon::Float | Input | false | false | false |  | 1 | 0.5 | 
Color/Gradient/Knot.6/Color | <in@PqX_wG1PEh5nSYruwgFJNt/_10/color | maxon::ColorA | Input | false | false | false |  |  | (1,1,1,1) | 
Color/Gradient/Knot.6/Interpolation | <in@PqX_wG1PEh5nSYruwgFJNt/_10/interpolation | maxon::InternedId | Input | false | false | true |  |  | smoothknot | Smooth = smoothknot, Cubic = cubicknot, Cubic Bias = cubicbias, Linear = linearknot, Step = none, Blend = blend
Color/Gradient/Knot.6/Knot Position | <in@PqX_wG1PEh5nSYruwgFJNt/_10/position | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Color/Gradient/Knot.7 | <in@PqX_wG1PEh5nSYruwgFJNt/_11 | net.maxon.render.portbundle.gradient | Input | false | false | false |  |  |  | 
Color/Gradient/Knot.7/Bias Position | <in@PqX_wG1PEh5nSYruwgFJNt/_11/bias | maxon::Float | Input | false | false | false |  | 1 | 0.5 | 
Color/Gradient/Knot.7/Color | <in@PqX_wG1PEh5nSYruwgFJNt/_11/color | maxon::ColorA | Input | false | false | false |  |  | (1,1,1,1) | 
Color/Gradient/Knot.7/Interpolation | <in@PqX_wG1PEh5nSYruwgFJNt/_11/interpolation | maxon::InternedId | Input | false | false | true |  |  | smoothknot | Smooth = smoothknot, Cubic = cubicknot, Cubic Bias = cubicbias, Linear = linearknot, Step = none, Blend = blend
Color/Gradient/Knot.7/Knot Position | <in@PqX_wG1PEh5nSYruwgFJNt/_11/position | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Color/Gradient/Knot.8 | <in@PqX_wG1PEh5nSYruwgFJNt/_12 | net.maxon.render.portbundle.gradient | Input | false | false | false |  |  |  | 
Color/Gradient/Knot.8/Bias Position | <in@PqX_wG1PEh5nSYruwgFJNt/_12/bias | maxon::Float | Input | false | false | false |  | 1 | 0.5 | 
Color/Gradient/Knot.8/Color | <in@PqX_wG1PEh5nSYruwgFJNt/_12/color | maxon::ColorA | Input | false | false | false |  |  | (1,1,1,1) | 
Color/Gradient/Knot.8/Interpolation | <in@PqX_wG1PEh5nSYruwgFJNt/_12/interpolation | maxon::InternedId | Input | false | false | true |  |  | smoothknot | Smooth = smoothknot, Cubic = cubicknot, Cubic Bias = cubicbias, Linear = linearknot, Step = none, Blend = blend
Color/Gradient/Knot.8/Knot Position | <in@PqX_wG1PEh5nSYruwgFJNt/_12/position | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Color/Gradient/Knot.9 | <in@PqX_wG1PEh5nSYruwgFJNt/_5 | net.maxon.render.portbundle.gradient | Input | false | false | false |  |  |  | 
Color/Gradient/Knot.9/Bias Position | <in@PqX_wG1PEh5nSYruwgFJNt/_5/bias | maxon::Float | Input | false | false | false |  | 1 | 0.5 | 
Color/Gradient/Knot.9/Color | <in@PqX_wG1PEh5nSYruwgFJNt/_5/color | maxon::ColorA | Input | false | false | false |  |  | (1,1,1,1) | 
Color/Gradient/Knot.9/Interpolation | <in@PqX_wG1PEh5nSYruwgFJNt/_5/interpolation | maxon::InternedId | Input | false | false | true |  |  | smoothknot | Smooth = smoothknot, Cubic = cubicknot, Cubic Bias = cubicbias, Linear = linearknot, Step = none, Blend = blend
Color/Gradient/Knot.9/Knot Position | <in@PqX_wG1PEh5nSYruwgFJNt/_5/position | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Color/Gradient/Knot.10 | <in@PqX_wG1PEh5nSYruwgFJNt/_6 | net.maxon.render.portbundle.gradient | Input | false | false | false |  |  |  | 
Color/Gradient/Knot.10/Bias Position | <in@PqX_wG1PEh5nSYruwgFJNt/_6/bias | maxon::Float | Input | false | false | false |  | 1 | 0.5 | 
Color/Gradient/Knot.10/Color | <in@PqX_wG1PEh5nSYruwgFJNt/_6/color | maxon::ColorA | Input | false | false | false |  |  | (1,1,1,1) | 
Color/Gradient/Knot.10/Interpolation | <in@PqX_wG1PEh5nSYruwgFJNt/_6/interpolation | maxon::InternedId | Input | false | false | true |  |  | smoothknot | Smooth = smoothknot, Cubic = cubicknot, Cubic Bias = cubicbias, Linear = linearknot, Step = none, Blend = blend
Color/Gradient/Knot.10/Knot Position | <in@PqX_wG1PEh5nSYruwgFJNt/_6/position | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Color/Gradient/Knot.11 | <in@PqX_wG1PEh5nSYruwgFJNt/_7 | net.maxon.render.portbundle.gradient | Input | false | false | false |  |  |  | 
Color/Gradient/Knot.11/Bias Position | <in@PqX_wG1PEh5nSYruwgFJNt/_7/bias | maxon::Float | Input | false | false | false |  | 1 | 0.5 | 
Color/Gradient/Knot.11/Color | <in@PqX_wG1PEh5nSYruwgFJNt/_7/color | maxon::ColorA | Input | false | false | false |  |  | (1,1,1,1) | 
Color/Gradient/Knot.11/Interpolation | <in@PqX_wG1PEh5nSYruwgFJNt/_7/interpolation | maxon::InternedId | Input | false | false | true |  |  | smoothknot | Smooth = smoothknot, Cubic = cubicknot, Cubic Bias = cubicbias, Linear = linearknot, Step = none, Blend = blend
Color/Gradient/Knot.11/Knot Position | <in@PqX_wG1PEh5nSYruwgFJNt/_7/position | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Color/Gradient/Knot.12 | <in@PqX_wG1PEh5nSYruwgFJNt/_9 | net.maxon.render.portbundle.gradient | Input | false | false | false |  |  |  | 
Color/Gradient/Knot.12/Bias Position | <in@PqX_wG1PEh5nSYruwgFJNt/_9/bias | maxon::Float | Input | false | false | false |  | 1 | 0.5 | 
Color/Gradient/Knot.12/Color | <in@PqX_wG1PEh5nSYruwgFJNt/_9/color | maxon::ColorA | Input | false | false | false |  |  | (1,1,1,1) | 
Color/Gradient/Knot.12/Interpolation | <in@PqX_wG1PEh5nSYruwgFJNt/_9/interpolation | maxon::InternedId | Input | false | false | true |  |  | smoothknot | Smooth = smoothknot, Cubic = cubicknot, Cubic Bias = cubicbias, Linear = linearknot, Step = none, Blend = blend
Color/Gradient/Knot.12/Knot Position | <in@PqX_wG1PEh5nSYruwgFJNt/_9/position | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Color/Gradient/Knot.13 | <in@PqX_wG1PEh5nSYruwgFJNt/_1 | net.maxon.render.portbundle.gradient | Input | false | false | false |  |  |  | 
Color/Gradient/Knot.13/Bias Position | <in@PqX_wG1PEh5nSYruwgFJNt/_1/bias | maxon::Float | Input | false | false | false |  | 1 | 0.5 | 
Color/Gradient/Knot.13/Color | <in@PqX_wG1PEh5nSYruwgFJNt/_1/color | maxon::ColorA | Input | false | false | false |  |  | (1,1,1,1) | 
Color/Gradient/Knot.13/Interpolation | <in@PqX_wG1PEh5nSYruwgFJNt/_1/interpolation | maxon::InternedId | Input | false | false | true |  |  | smoothknot | Smooth = smoothknot, Cubic = cubicknot, Cubic Bias = cubicbias, Linear = linearknot, Step = none, Blend = blend
Color/Gradient/Knot.13/Knot Position | <in@PqX_wG1PEh5nSYruwgFJNt/_1/position | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Color/Gradient2 | <in@dGMtYWONNtyu6rT8Bak9pC | net.maxon.render.portbundle.gradient | Input | true | true | false |  |  |  | 
Color/Gradient2/Knot.1 | <in@dGMtYWONNtyu6rT8Bak9pC/_0 | net.maxon.render.portbundle.gradient | Input | false | false | false |  |  |  | 
Color/Gradient2/Knot.1/Bias Position | <in@dGMtYWONNtyu6rT8Bak9pC/_0/bias | maxon::Float | Input | false | false | false |  | 1 | 0.5 | 
Color/Gradient2/Knot.1/Color | <in@dGMtYWONNtyu6rT8Bak9pC/_0/color | maxon::ColorA | Input | false | false | false |  |  | (1,1,1,1) | 
Color/Gradient2/Knot.1/Interpolation | <in@dGMtYWONNtyu6rT8Bak9pC/_0/interpolation | maxon::InternedId | Input | false | false | true |  |  | smoothknot | Smooth = smoothknot, Cubic = cubicknot, Cubic Bias = cubicbias, Linear = linearknot, Step = none, Blend = blend
Color/Gradient2/Knot.1/Knot Position | <in@dGMtYWONNtyu6rT8Bak9pC/_0/position | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Color/Gradient2/Knot.2 | <in@dGMtYWONNtyu6rT8Bak9pC/_2 | net.maxon.render.portbundle.gradient | Input | false | false | false |  |  |  | 
Color/Gradient2/Knot.2/Bias Position | <in@dGMtYWONNtyu6rT8Bak9pC/_2/bias | maxon::Float | Input | false | false | false |  | 1 | 0.5 | 
Color/Gradient2/Knot.2/Color | <in@dGMtYWONNtyu6rT8Bak9pC/_2/color | maxon::ColorA | Input | false | false | false |  |  | (1,1,1,1) | 
Color/Gradient2/Knot.2/Interpolation | <in@dGMtYWONNtyu6rT8Bak9pC/_2/interpolation | maxon::InternedId | Input | false | false | true |  |  | smoothknot | Smooth = smoothknot, Cubic = cubicknot, Cubic Bias = cubicbias, Linear = linearknot, Step = none, Blend = blend
Color/Gradient2/Knot.2/Knot Position | <in@dGMtYWONNtyu6rT8Bak9pC/_2/position | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Color/Gradient2/Knot.3 | <in@dGMtYWONNtyu6rT8Bak9pC/_3 | net.maxon.render.portbundle.gradient | Input | false | false | false |  |  |  | 
Color/Gradient2/Knot.3/Bias Position | <in@dGMtYWONNtyu6rT8Bak9pC/_3/bias | maxon::Float | Input | false | false | false |  | 1 | 0.5 | 
Color/Gradient2/Knot.3/Color | <in@dGMtYWONNtyu6rT8Bak9pC/_3/color | maxon::ColorA | Input | false | false | false |  |  | (1,1,1,1) | 
Color/Gradient2/Knot.3/Interpolation | <in@dGMtYWONNtyu6rT8Bak9pC/_3/interpolation | maxon::InternedId | Input | false | false | true |  |  | smoothknot | Smooth = smoothknot, Cubic = cubicknot, Cubic Bias = cubicbias, Linear = linearknot, Step = none, Blend = blend
Color/Gradient2/Knot.3/Knot Position | <in@dGMtYWONNtyu6rT8Bak9pC/_3/position | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Color/Gradient2/Knot.4 | <in@dGMtYWONNtyu6rT8Bak9pC/_4 | net.maxon.render.portbundle.gradient | Input | false | false | false |  |  |  | 
Color/Gradient2/Knot.4/Bias Position | <in@dGMtYWONNtyu6rT8Bak9pC/_4/bias | maxon::Float | Input | false | false | false |  | 1 | 0.5 | 
Color/Gradient2/Knot.4/Color | <in@dGMtYWONNtyu6rT8Bak9pC/_4/color | maxon::ColorA | Input | false | false | false |  |  | (1,1,1,1) | 
Color/Gradient2/Knot.4/Interpolation | <in@dGMtYWONNtyu6rT8Bak9pC/_4/interpolation | maxon::InternedId | Input | false | false | true |  |  | smoothknot | Smooth = smoothknot, Cubic = cubicknot, Cubic Bias = cubicbias, Linear = linearknot, Step = none, Blend = blend
Color/Gradient2/Knot.4/Knot Position | <in@dGMtYWONNtyu6rT8Bak9pC/_4/position | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Color/Gradient2/Knot.5 | <in@dGMtYWONNtyu6rT8Bak9pC/_8 | net.maxon.render.portbundle.gradient | Input | false | false | false |  |  |  | 
Color/Gradient2/Knot.5/Bias Position | <in@dGMtYWONNtyu6rT8Bak9pC/_8/bias | maxon::Float | Input | false | false | false |  | 1 | 0.5 | 
Color/Gradient2/Knot.5/Color | <in@dGMtYWONNtyu6rT8Bak9pC/_8/color | maxon::ColorA | Input | false | false | false |  |  | (1,1,1,1) | 
Color/Gradient2/Knot.5/Interpolation | <in@dGMtYWONNtyu6rT8Bak9pC/_8/interpolation | maxon::InternedId | Input | false | false | true |  |  | smoothknot | Smooth = smoothknot, Cubic = cubicknot, Cubic Bias = cubicbias, Linear = linearknot, Step = none, Blend = blend
Color/Gradient2/Knot.5/Knot Position | <in@dGMtYWONNtyu6rT8Bak9pC/_8/position | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Color/Gradient2/Knot.6 | <in@dGMtYWONNtyu6rT8Bak9pC/_10 | net.maxon.render.portbundle.gradient | Input | false | false | false |  |  |  | 
Color/Gradient2/Knot.6/Bias Position | <in@dGMtYWONNtyu6rT8Bak9pC/_10/bias | maxon::Float | Input | false | false | false |  | 1 | 0.5 | 
Color/Gradient2/Knot.6/Color | <in@dGMtYWONNtyu6rT8Bak9pC/_10/color | maxon::ColorA | Input | false | false | false |  |  | (1,1,1,1) | 
Color/Gradient2/Knot.6/Interpolation | <in@dGMtYWONNtyu6rT8Bak9pC/_10/interpolation | maxon::InternedId | Input | false | false | true |  |  | smoothknot | Smooth = smoothknot, Cubic = cubicknot, Cubic Bias = cubicbias, Linear = linearknot, Step = none, Blend = blend
Color/Gradient2/Knot.6/Knot Position | <in@dGMtYWONNtyu6rT8Bak9pC/_10/position | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Color/Gradient2/Knot.7 | <in@dGMtYWONNtyu6rT8Bak9pC/_11 | net.maxon.render.portbundle.gradient | Input | false | false | false |  |  |  | 
Color/Gradient2/Knot.7/Bias Position | <in@dGMtYWONNtyu6rT8Bak9pC/_11/bias | maxon::Float | Input | false | false | false |  | 1 | 0.5 | 
Color/Gradient2/Knot.7/Color | <in@dGMtYWONNtyu6rT8Bak9pC/_11/color | maxon::ColorA | Input | false | false | false |  |  | (1,1,1,1) | 
Color/Gradient2/Knot.7/Interpolation | <in@dGMtYWONNtyu6rT8Bak9pC/_11/interpolation | maxon::InternedId | Input | false | false | true |  |  | smoothknot | Smooth = smoothknot, Cubic = cubicknot, Cubic Bias = cubicbias, Linear = linearknot, Step = none, Blend = blend
Color/Gradient2/Knot.7/Knot Position | <in@dGMtYWONNtyu6rT8Bak9pC/_11/position | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Color/Gradient2/Knot.8 | <in@dGMtYWONNtyu6rT8Bak9pC/_12 | net.maxon.render.portbundle.gradient | Input | false | false | false |  |  |  | 
Color/Gradient2/Knot.8/Bias Position | <in@dGMtYWONNtyu6rT8Bak9pC/_12/bias | maxon::Float | Input | false | false | false |  | 1 | 0.5 | 
Color/Gradient2/Knot.8/Color | <in@dGMtYWONNtyu6rT8Bak9pC/_12/color | maxon::ColorA | Input | false | false | false |  |  | (1,1,1,1) | 
Color/Gradient2/Knot.8/Interpolation | <in@dGMtYWONNtyu6rT8Bak9pC/_12/interpolation | maxon::InternedId | Input | false | false | true |  |  | smoothknot | Smooth = smoothknot, Cubic = cubicknot, Cubic Bias = cubicbias, Linear = linearknot, Step = none, Blend = blend
Color/Gradient2/Knot.8/Knot Position | <in@dGMtYWONNtyu6rT8Bak9pC/_12/position | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Color/Gradient2/Knot.9 | <in@dGMtYWONNtyu6rT8Bak9pC/_5 | net.maxon.render.portbundle.gradient | Input | false | false | false |  |  |  | 
Color/Gradient2/Knot.9/Bias Position | <in@dGMtYWONNtyu6rT8Bak9pC/_5/bias | maxon::Float | Input | false | false | false |  | 1 | 0.5 | 
Color/Gradient2/Knot.9/Color | <in@dGMtYWONNtyu6rT8Bak9pC/_5/color | maxon::ColorA | Input | false | false | false |  |  | (1,1,1,1) | 
Color/Gradient2/Knot.9/Interpolation | <in@dGMtYWONNtyu6rT8Bak9pC/_5/interpolation | maxon::InternedId | Input | false | false | true |  |  | smoothknot | Smooth = smoothknot, Cubic = cubicknot, Cubic Bias = cubicbias, Linear = linearknot, Step = none, Blend = blend
Color/Gradient2/Knot.9/Knot Position | <in@dGMtYWONNtyu6rT8Bak9pC/_5/position | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Color/Gradient2/Knot.10 | <in@dGMtYWONNtyu6rT8Bak9pC/_6 | net.maxon.render.portbundle.gradient | Input | false | false | false |  |  |  | 
Color/Gradient2/Knot.10/Bias Position | <in@dGMtYWONNtyu6rT8Bak9pC/_6/bias | maxon::Float | Input | false | false | false |  | 1 | 0.5 | 
Color/Gradient2/Knot.10/Color | <in@dGMtYWONNtyu6rT8Bak9pC/_6/color | maxon::ColorA | Input | false | false | false |  |  | (1,1,1,1) | 
Color/Gradient2/Knot.10/Interpolation | <in@dGMtYWONNtyu6rT8Bak9pC/_6/interpolation | maxon::InternedId | Input | false | false | true |  |  | smoothknot | Smooth = smoothknot, Cubic = cubicknot, Cubic Bias = cubicbias, Linear = linearknot, Step = none, Blend = blend
Color/Gradient2/Knot.10/Knot Position | <in@dGMtYWONNtyu6rT8Bak9pC/_6/position | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Color/Gradient2/Knot.11 | <in@dGMtYWONNtyu6rT8Bak9pC/_7 | net.maxon.render.portbundle.gradient | Input | false | false | false |  |  |  | 
Color/Gradient2/Knot.11/Bias Position | <in@dGMtYWONNtyu6rT8Bak9pC/_7/bias | maxon::Float | Input | false | false | false |  | 1 | 0.5 | 
Color/Gradient2/Knot.11/Color | <in@dGMtYWONNtyu6rT8Bak9pC/_7/color | maxon::ColorA | Input | false | false | false |  |  | (1,1,1,1) | 
Color/Gradient2/Knot.11/Interpolation | <in@dGMtYWONNtyu6rT8Bak9pC/_7/interpolation | maxon::InternedId | Input | false | false | true |  |  | smoothknot | Smooth = smoothknot, Cubic = cubicknot, Cubic Bias = cubicbias, Linear = linearknot, Step = none, Blend = blend
Color/Gradient2/Knot.11/Knot Position | <in@dGMtYWONNtyu6rT8Bak9pC/_7/position | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Color/Gradient2/Knot.12 | <in@dGMtYWONNtyu6rT8Bak9pC/_9 | net.maxon.render.portbundle.gradient | Input | false | false | false |  |  |  | 
Color/Gradient2/Knot.12/Bias Position | <in@dGMtYWONNtyu6rT8Bak9pC/_9/bias | maxon::Float | Input | false | false | false |  | 1 | 0.5 | 
Color/Gradient2/Knot.12/Color | <in@dGMtYWONNtyu6rT8Bak9pC/_9/color | maxon::ColorA | Input | false | false | false |  |  | (1,1,1,1) | 
Color/Gradient2/Knot.12/Interpolation | <in@dGMtYWONNtyu6rT8Bak9pC/_9/interpolation | maxon::InternedId | Input | false | false | true |  |  | smoothknot | Smooth = smoothknot, Cubic = cubicknot, Cubic Bias = cubicbias, Linear = linearknot, Step = none, Blend = blend
Color/Gradient2/Knot.12/Knot Position | <in@dGMtYWONNtyu6rT8Bak9pC/_9/position | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Color/Gradient2/Knot.13 | <in@dGMtYWONNtyu6rT8Bak9pC/_1 | net.maxon.render.portbundle.gradient | Input | false | false | false |  |  |  | 
Color/Gradient2/Knot.13/Bias Position | <in@dGMtYWONNtyu6rT8Bak9pC/_1/bias | maxon::Float | Input | false | false | false |  | 1 | 0.5 | 
Color/Gradient2/Knot.13/Color | <in@dGMtYWONNtyu6rT8Bak9pC/_1/color | maxon::ColorA | Input | false | false | false |  |  | (1,1,1,1) | 
Color/Gradient2/Knot.13/Interpolation | <in@dGMtYWONNtyu6rT8Bak9pC/_1/interpolation | maxon::InternedId | Input | false | false | true |  |  | smoothknot | Smooth = smoothknot, Cubic = cubicknot, Cubic Bias = cubicbias, Linear = linearknot, Step = none, Blend = blend
Color/Gradient2/Knot.13/Knot Position | <in@dGMtYWONNtyu6rT8Bak9pC/_1/position | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Color/Sample Mode | <enum5 | maxon::Int64 | Input | false | false | true |  |  |  | Constant = 0, Linear = 1, Random = 2
Color/Sample Mode | <in@Hb68hCFXDhEsQJB4ze7YNH | maxon::Int64 | Input | false | false | true |  |  |  | Constant = 0, Linear = 1, Random = 2
Distributions/Align Clone | <in@BWVidrjQH55jF5VKQwGjxN | maxon::Bool | Input | false | false | false |  |  | true | 
Distributions/Both Edges | <bool1 | maxon::Bool | Input | false | false | false |  |  | true | 
Distributions/Cloner Children | <clonerchildrenin | maxon::ArrayContainer<maxon::Matrix, maxon::Matrix, maxon::GeometryObject, maxon::GeometryObject, maxon::Range<maxon::Vector>, maxon::String> | Input | false | false | false |  |  |  | 
Distributions/Clones | <enum | maxon::Int64 | Input | false | false | true |  |  |  | Iterate = 0, Random = 1
Distributions/Corner | <in@ZESPZ8PrG1VsT1zcyUWgKh | maxon::Bool | Input | false | false | false |  |  | true | 
Distributions/Count | <integer | maxon::Int64 | Input | false | false | false |  |  | 5 | 
Distributions/Distribution | <in@AbtDZZ4rFJiowiOY53rd5a | maxon::Int64 | Input | false | false | true |  |  |  | Count = 0, Step = 1
Distributions/Global Cloner Matrix | <globalclonermatrixin | maxon::Matrix | Input | false | false | false |  |  |  | 
Distributions/Interconnect | <in@NDAEAUSkI5xg_GNGUwd2ER | maxon::Bool | Input | false | false | false |  |  | true | 
Distributions/Local Cloner Matrix | <localclonermatrixin | maxon::Matrix | Input | false | false | false |  |  |  | 
Distributions/Max Steps | <integer2 | maxon::Int64 | Input | false | false | false |  |  | 100 | 
Distributions/Objects Children | <objectchildren | maxon::ArrayContainer<maxon::GeometryObject, maxon::Matrix64, maxon::Matrix64, maxon::ColorA64, maxon::String> | Input | false | false | false |  |  |  | 
Distributions/Offset | <float7 | maxon::Float64 | Input | false | false | false |  |  | 5 | 
Distributions/Offset | <in@eAiLCvCVL5mlee8VR3QI7J | maxon::Float64 | Input | false | false | false |  |  | 0.15 | 
Distributions/Offset Mode | <in@K$h20v8bFFVn4ywuyCcz3J | maxon::Int64 | Input | false | false | true |  |  | 1 | Absolute = 0, Object = 1
Distributions/Offset Mode | <in@bblKgFG6EBqpN0bTxXBRJV | maxon::Int64 | Input | false | false | true |  |  |  | Percentage = 0, Absolute = 1
Distributions/Pinch | <in@L_gMKPkVAJxrjkYXglCrCE | maxon::Float64 | Input | false | false | false |  |  |  | 
Distributions/Position Jitter | <float | maxon::Float64 | Input | false | false | false |  |  | 0 | 
Distributions/PreRotate | <in@CEUbstcXBBTpPgHy_AkI9s | maxon::Vector64 | Input | false | false | false |  |  |  | 
Distributions/Return | <in@cgmAGAWvA1yme5m0JWuADU | maxon::Int64 | Input | false | false | true |  |  | 0 | All = 0, Even = 1, Odd = 2, Alternating = 3, Random = 4
Distributions/Scale | <in@F4IX8SDcGFZq52oIlEM7RW | maxon::Float64 | Input | false | false | false |  |  | 0.5 | 
Distributions/Scaling Axis | <in@JSvVKSzEPJomWO18$v$99M | maxon::Int64 | Input | false | false | true |  |  | 1 | Direction = 0, Uniform = 1
Distributions/Seed | <float1 | maxon::Float64 | Input | false | false | false |  |  | 12345 | 
Distributions/Selection | <string | maxon::String | Input | false | false | false |  |  |  | 
Distributions/Spacing | <in@C_RM2EFJO53qWRU2uFRHVL | maxon::Int64 | Input | false | false | true |  |  |  | Scale All = 0, Even Gaps = 1, End Gaps = 2
Distributions/Spin | <float2 | maxon::Float64 | Input | false | false | false |  |  | 0 | 
Distributions/Spin | <in@b9UhbtjuF9jpldZT$BH3cT | maxon::Float64 | Input | false | false | false |  |  | 0 | 
Distributions/Spin Jitter | <in@Q3qmS1OMIN7rTqc8IpNQky | maxon::Float64 | Input | false | false | false |  |  | 0 | 
Distributions/Step | <float6 | maxon::Float64 | Input | false | false | false | 0.01 |  | 10 | 
Distributions/Subdivision | <integer3 | maxon::Int64 | Input | false | false | false |  |  | 0 | 
Distributions/Surface Offset | <in@JRm9J3vsPJfrv9MUEaed2P | maxon::Float64 | Input | false | false | false |  |  | 0 | 
Distributions/Surface Offset(B) | <integer1 | maxon::Float64 | Input | false | false | false |  |  |  | 
Outputs/Distribution | >distdataout | maxon::ArrayContainer<maxon::Matrix64, maxon::Int64, maxon::Int64, maxon::Vector64, maxon::Color64, maxon::Int64> | Output | false | false | false |  |  |  | 
Outputs/Result | >out@JyIMSlZXF5wim0NvjLHLZD | maxon::Matrix64 | Output | false | false | false |  |  |  | 

