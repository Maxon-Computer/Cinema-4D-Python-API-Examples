# Node Template: Spline Bead Distribution

- **Node Space ID:** `net.maxon.neutron.nodespace`
- **Template ID:** `com.rocketlasso.neutron.asset.distribution.bead`
- **Template Name:** `Spline Bead Distribution`

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
Color/Sample Mode | <enum5 | maxon::Int64 | Input | false | false | true |  |  |  | Constant = 0, Linear = 1, Random = 2
Distribution/Align | <in@VjfHylJKDNugsxARA8klHl | maxon::Bool | Input | false | false | false |  |  | true | 
Distribution/Bias | <in@Xm2U4TNQM1Klbcns7O9MNp | maxon::Float64 | Input | false | false | false |  |  | 0 | 
Distribution/Cloner Children | <clonerchildrenin | maxon::ArrayContainer<maxon::Matrix, maxon::Matrix, maxon::GeometryObject, maxon::GeometryObject, maxon::Range<maxon::Vector>, maxon::String> | Input | false | false | false |  |  |  | 
Distribution/Clones | <enum | maxon::Int64 | Input | false | false | true |  |  |  | Iterate = 0, Random = 1
Distribution/Enable Rail         | <bool4 | maxon::Bool | Input | false | false | false |  |  | false | 
Distribution/End | <in@X0wNN3SZLlPg1kzY_B8_pq | maxon::Float64 | Input | false | false | false |  | 1 | 1 | 
Distribution/Fill Gap | <in@BHmwxxukLN8r4yha1gnXDJ | maxon::Int64 | Input | false | false | true |  |  | 2 | None = 0, Fill = 1, Full = 2
Distribution/Gap | <float2 | maxon::Float64 | Input | false | false | false |  |  | 0 | 
Distribution/Global Cloner Matrix | <globalclonermatrixin | maxon::Matrix | Input | false | false | false |  |  |  | 
Distribution/Group/Scale To Rail | <in@XHCczmm8ABHtoxuoQLnhou | maxon::Bool | Input | false | false | false |  |  | false | 
Distribution/Group/Target                 | <bool | maxon::Bool | Input | false | false | false |  |  | false | 
Distribution/Local Cloner Matrix | <localclonermatrixin | maxon::Matrix | Input | false | false | false |  |  |  | 
Distribution/Max Count | <integer | maxon::Int64 | Input | false | false | false |  |  | 5000 | 
Distribution/Objects Children | <objectchildren | maxon::ArrayContainer<maxon::GeometryObject, maxon::Matrix64, maxon::Matrix64, maxon::ColorA64, maxon::String> | Input | false | false | false |  |  |  | 
Distribution/Offset | <in@ANSgh1knANNiv$ge7QD0Yq | maxon::Float64 | Input | false | false | false |  |  | 0 | 
Distribution/Offset | <integer1 | maxon::Int64 | Input | false | false | false |  |  |  | 
Distribution/Per Segment | <in@bj$f4dVbHhasrCdkNvnsDh | maxon::Bool | Input | false | false | false |  |  | true | 
Distribution/Random Scale | <float5 | maxon::Float64 | Input | false | false | false | -1 |  |  | 
Distribution/Remap Strength/Spline | <in@D2AK215GPpOmWMKrP7qNdu | net.maxon.render.portbundle.spline | Input | false | true | false |  |  |  | 
Distribution/Remap Strength/Spline/Link End Positions | <in@D2AK215GPpOmWMKrP7qNdu/linkendpositions | maxon::Bool | Input | false | false | false |  |  |  | 
Distribution/Remap Strength/Spline/Link End Tangents | <in@D2AK215GPpOmWMKrP7qNdu/linkendtangents | maxon::Bool | Input | false | false | false |  |  |  | 
Distribution/Remap Strength/Spline/Max | <in@D2AK215GPpOmWMKrP7qNdu/max | maxon::Vector2d | Input | false | false | false |  |  | (1,1) | 
Distribution/Remap Strength/Spline/Min | <in@D2AK215GPpOmWMKrP7qNdu/min | maxon::Vector2d | Input | false | false | false |  |  |  | 
Distribution/Remap Strength/Spline/Points | <in@D2AK215GPpOmWMKrP7qNdu/points | net.maxon.render.portbundle.splinepoint | Input | true | false | false |  |  |  | 
Distribution/Remap Strength/Spline/Points/Point.1 | <in@D2AK215GPpOmWMKrP7qNdu/points/_0 | net.maxon.render.portbundle.splinepoint | Input | false | false | false |  |  |  | 
Distribution/Remap Strength/Spline/Points/Point.1/Break Tangent | <in@D2AK215GPpOmWMKrP7qNdu/points/_0/breaktangent | maxon::Bool | Input | false | false | false |  |  |  | 
Distribution/Remap Strength/Spline/Points/Point.1/Interpolation | <in@D2AK215GPpOmWMKrP7qNdu/points/_0/interpolation | maxon::InternedId | Input | false | false | true |  |  | spline | Spline = spline, Cubic = cubic, Linear = linear
Distribution/Remap Strength/Spline/Points/Point.1/Keep Visual Angle | <in@D2AK215GPpOmWMKrP7qNdu/points/_0/keepvisualangle | maxon::Bool | Input | false | false | false |  |  |  | 
Distribution/Remap Strength/Spline/Points/Point.1/Lock Angle | <in@D2AK215GPpOmWMKrP7qNdu/points/_0/lockangle | maxon::Bool | Input | false | false | false |  |  |  | 
Distribution/Remap Strength/Spline/Points/Point.1/Lock Length | <in@D2AK215GPpOmWMKrP7qNdu/points/_0/locklength | maxon::Bool | Input | false | false | false |  |  |  | 
Distribution/Remap Strength/Spline/Points/Point.1/Lock X | <in@D2AK215GPpOmWMKrP7qNdu/points/_0/lockx | maxon::Bool | Input | false | false | false |  |  |  | 
Distribution/Remap Strength/Spline/Points/Point.1/Lock Y | <in@D2AK215GPpOmWMKrP7qNdu/points/_0/locky | maxon::Bool | Input | false | false | false |  |  |  | 
Distribution/Remap Strength/Spline/Points/Point.1/Position X | <in@D2AK215GPpOmWMKrP7qNdu/points/_0/positionx | maxon::Float | Input | false | false | false |  |  | 0 | 
Distribution/Remap Strength/Spline/Points/Point.1/Position Y | <in@D2AK215GPpOmWMKrP7qNdu/points/_0/positiony | maxon::Float | Input | false | false | false |  |  | 0 | 
Distribution/Remap Strength/Spline/Points/Point.1/Tangent Left | <in@D2AK215GPpOmWMKrP7qNdu/points/_0/tangentleft | maxon::Vector2d | Input | false | false | false |  |  |  | 
Distribution/Remap Strength/Spline/Points/Point.1/Tangent Right | <in@D2AK215GPpOmWMKrP7qNdu/points/_0/tangentright | maxon::Vector2d | Input | false | false | false |  |  |  | 
Distribution/Remap Strength/Spline/Points/Point.2 | <in@D2AK215GPpOmWMKrP7qNdu/points/_1 | net.maxon.render.portbundle.splinepoint | Input | false | false | false |  |  |  | 
Distribution/Remap Strength/Spline/Points/Point.2/Break Tangent | <in@D2AK215GPpOmWMKrP7qNdu/points/_1/breaktangent | maxon::Bool | Input | false | false | false |  |  |  | 
Distribution/Remap Strength/Spline/Points/Point.2/Interpolation | <in@D2AK215GPpOmWMKrP7qNdu/points/_1/interpolation | maxon::InternedId | Input | false | false | true |  |  | spline | Spline = spline, Cubic = cubic, Linear = linear
Distribution/Remap Strength/Spline/Points/Point.2/Keep Visual Angle | <in@D2AK215GPpOmWMKrP7qNdu/points/_1/keepvisualangle | maxon::Bool | Input | false | false | false |  |  |  | 
Distribution/Remap Strength/Spline/Points/Point.2/Lock Angle | <in@D2AK215GPpOmWMKrP7qNdu/points/_1/lockangle | maxon::Bool | Input | false | false | false |  |  |  | 
Distribution/Remap Strength/Spline/Points/Point.2/Lock Length | <in@D2AK215GPpOmWMKrP7qNdu/points/_1/locklength | maxon::Bool | Input | false | false | false |  |  |  | 
Distribution/Remap Strength/Spline/Points/Point.2/Lock X | <in@D2AK215GPpOmWMKrP7qNdu/points/_1/lockx | maxon::Bool | Input | false | false | false |  |  |  | 
Distribution/Remap Strength/Spline/Points/Point.2/Lock Y | <in@D2AK215GPpOmWMKrP7qNdu/points/_1/locky | maxon::Bool | Input | false | false | false |  |  |  | 
Distribution/Remap Strength/Spline/Points/Point.2/Position X | <in@D2AK215GPpOmWMKrP7qNdu/points/_1/positionx | maxon::Float | Input | false | false | false |  |  | 0 | 
Distribution/Remap Strength/Spline/Points/Point.2/Position Y | <in@D2AK215GPpOmWMKrP7qNdu/points/_1/positiony | maxon::Float | Input | false | false | false |  |  | 0 | 
Distribution/Remap Strength/Spline/Points/Point.2/Tangent Left | <in@D2AK215GPpOmWMKrP7qNdu/points/_1/tangentleft | maxon::Vector2d | Input | false | false | false |  |  |  | 
Distribution/Remap Strength/Spline/Points/Point.2/Tangent Right | <in@D2AK215GPpOmWMKrP7qNdu/points/_1/tangentright | maxon::Vector2d | Input | false | false | false |  |  |  | 
Distribution/Remap Strength/Spline/Tension | <in@D2AK215GPpOmWMKrP7qNdu/tension | maxon::Float | Input | false | false | false |  | 1 | 1 | 
Distribution/Scaling Axis | <enum3 | maxon::Int64 | Input | false | false | true |  |  | 1 | Direction = 0, Uniform = 1
Distribution/Seed | <float1 | maxon::Float64 | Input | false | false | false |  |  | 12345 | 
Distribution/Shift Object | <float | maxon::Float64 | Input | false | false | false |  |  | 1 | 
Distribution/Start | <in@bweMq1qLD9Vk7efolkeMfv | maxon::Float64 | Input | false | false | false |  | 1 | 0 | 
Distribution/Transition Ends | <bool3 | maxon::Bool | Input | false | false | false |  |  | true | 
Outputs/Distribution | >distdataout | maxon::ArrayContainer<maxon::Matrix64, maxon::Int64, maxon::Int64, maxon::Vector64, maxon::Color64, maxon::Int64> | Output | false | false | false |  |  |  | 

