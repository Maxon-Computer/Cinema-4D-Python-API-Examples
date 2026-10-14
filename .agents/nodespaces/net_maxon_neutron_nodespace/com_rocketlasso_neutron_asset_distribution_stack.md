# Node Template: Stack Distribution

- **Node Space ID:** `net.maxon.neutron.nodespace`
- **Template ID:** `com.rocketlasso.neutron.asset.distribution.stack`
- **Template Name:** `Stack Distribution`

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
Distribution/Aim Along (Z) | <in@BwUR86hVD9jg3IRca9akSI | maxon::Int64 | Input | false | false | true |  |  | 0 | Match Direction = 0, X = 1, Y = 2, Z = 3, Random = 4
Distribution/Cloner Children | <clonerchildrenin | maxon::ArrayContainer<maxon::Matrix, maxon::Matrix, maxon::GeometryObject, maxon::GeometryObject, maxon::Range<maxon::Vector>, maxon::String> | Input | false | false | false |  |  |  | 
Distribution/Clones | <enum | maxon::Int64 | Input | false | false | true |  |  |  | Iterate = 0, Random = 1
Distribution/Count | <integer | maxon::Int64 | Input | false | false | false |  | 9999999 | 25 | 
Distribution/Direction | <enum1 | maxon::Int64 | Input | false | false | true |  |  | 0 | +X = 0, -Z = 5, -X = 1, +Y = 2, -Y = 3, +Z = 4
Distribution/Gap | <float2 | maxon::Float64 | Input | false | false | false |  |  |  | 
Distribution/Global Cloner Matrix | <globalclonermatrixin | maxon::Matrix | Input | false | false | false |  |  |  | 
Distribution/Length | <float6 | maxon::Float64 | Input | false | false | false |  |  | 600 | 
Distribution/Local Cloner Matrix | <localclonermatrixin | maxon::Matrix | Input | false | false | false |  |  |  | 
Distribution/Max Count | <in@Q98p16U3JtKnxCgqo2qEsX | maxon::Int64 | Input | false | false | false |  | 9999999 | 5000 | 
Distribution/Offset | <integer1 | maxon::Int64 | Input | false | false | false |  |  |  | 
Distribution/Orientation | <in@bPSH2UmcGx2qm$_CWyiydM | maxon::Int64 | Input | false | false | true |  |  | 0 | Forward = 0, Backward = 1, Forward and Backward = 2
Distribution/Pivot X | <float | maxon::Float64 | Input | false | false | false |  |  | 0 | 
Distribution/Pivot Y | <in@f4FdQS5NAdBkHro0Kewhdy | maxon::Float64 | Input | false | false | false |  |  | 1 | 
Distribution/Pivot Z | <in@D0jTfewdBZ0l2nMqt7$obx | maxon::Float64 | Input | false | false | false |  |  | 0 | 
Distribution/Random Scale | <float5 | maxon::Float64 | Input | false | false | false | -1 |  |  | 
Distribution/Scale Source | <in@bsmwrCvBDVBpKQPoiLPDpj | maxon::Int64 | Input | false | false | true |  |  | 2 | Bounding Box Inner Radius = 0, Bounding Box Outer Radius = 1, Bounding Box "Direction Z" = 2
Distribution/Scaling Axis | <enum3 | maxon::Int64 | Input | false | false | true |  |  |  | Direction = 0, Uniform = 1
Distribution/Seed | <float1 | maxon::Float64 | Input | false | false | false |  |  | 12345 | 
Distribution/Spin | <in@Lv7f3vbOPhnkUbYQfp55CN | maxon::Int64 | Input | false | false | true |  |  | 0 | Auto = 0, Opposites = 1, Random = 2
Distribution/Stack | <enum2 | maxon::Int64 | Input | false | false | true |  |  |  | Count = 0, Length = 1
Distribution/Stretch to Fill | <bool | maxon::Bool | Input | false | false | false |  |  | true | 
Outputs/Distribution | >distdataout | maxon::ArrayContainer<maxon::Matrix64, maxon::Int64, maxon::Int64, maxon::Vector64, maxon::Color64, maxon::Int64> | Output | false | false | false |  |  |  | 

