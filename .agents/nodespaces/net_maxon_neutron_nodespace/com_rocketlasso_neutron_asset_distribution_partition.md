# Node Template: Partition Distribution

- **Node Space ID:** `net.maxon.neutron.nodespace`
- **Template ID:** `com.rocketlasso.neutron.asset.distribution.partition`
- **Template Name:** `Partition Distribution`

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
Distribution/Aim Along | <in@bLtieByoAtTgzEz8GWdHrb | maxon::Int64 | Input | false | false | true |  |  | 0 | Match Plane = 0, X = 1, Y = 2, Z = 3, Random = 4
Distribution/Cloner Children | <clonerchildrenin | maxon::ArrayContainer<maxon::Matrix, maxon::Matrix, maxon::GeometryObject, maxon::GeometryObject, maxon::Range<maxon::Vector>, maxon::String> | Input | false | false | false |  |  |  | 
Distribution/Clones | <enum | maxon::Int64 | Input | false | false | true |  |  |  | Iterate = 0, Random = 1
Distribution/Cut Algorithm | <in@Tjh638vYPF7ihj8H7GtcU0 | maxon::Int64 | Input | false | false | true |  |  | 1 | Largest (Stable Geo Dependent) = 0, Simple = 1
Distribution/Cut Cap | <attr@Dkb1i7R5MxiqvhHTJQgQTc | maxon::Float64 | Input | false | false | false |  |  | 5000 | 
Distribution/Cut Iterations | <in@AnJOqEQgC9_qxvHSBum9Xy | maxon::Int64 | Input | false | false | false |  |  | 2 | 
Distribution/Cut Orientation | <in@TEQLMFsBPxes3lqDqoFOgx | maxon::Int64 | Input | false | false | true |  |  | 1 | Manual = 0, Alternating = 1, Longest Edge (Stable Geo Dependent) = 3
Distribution/Cuts | <in@Uh27iIUGAJlvImufXZTtj1 | maxon::Int64 | Input | false | false | false |  |  | 25 | 
Distribution/Direction | <in@ZWG6VxttCBahbIUiWpOYBg | maxon::Int64 | Input | false | false | true |  |  | 4 | -Z = 5, +X = 0, -X = 1, +Y = 2, -Y = 3, +Z = 4
Distribution/Gap | <float2 | maxon::Float64 | Input | false | false | false |  |  | 0 | 
Distribution/Global Cloner Matrix | <globalclonermatrixin | maxon::Matrix | Input | false | false | false |  |  |  | 
Distribution/Local Cloner Matrix | <localclonermatrixin | maxon::Matrix | Input | false | false | false |  |  |  | 
Distribution/Match Scale To | <in@O5tpWp95JJrqbIgjcliatr | maxon::Int64 | Input | false | false | true |  |  | 2 | None = 0, Width = 1, Height = 2, Constrained = 3, Scale To Fit = 4
Distribution/Orientation | <in@Tx_Hyeb5ARlgXrfX2dPMvf | maxon::Int64 | Input | false | false | true |  |  | 0 | Forward = 0, Backward = 1, Forward and Backward = 2
Distribution/Orientation H/W | <in@SXdLlLZ1Mdlh_J2ic4vy6x | maxon::Float64 | Input | false | false | false | 0 | 1 | 0.5 | 
Distribution/Pivot X | <in@Kbi7nR7qGxfkNcKD49NWoF | maxon::Float64 | Input | false | false | false |  |  | 0 | 
Distribution/Pivot Y | <in@b$oZKgGyGFqoNJ8qUrD5tE | maxon::Float64 | Input | false | false | false |  |  | 0 | 
Distribution/Pivot Z | <in@JSAuseKJLd6nj_7sma3OsF | maxon::Float64 | Input | false | false | false |  |  | 0 | 
Distribution/Random Animation/Animation Speed | <in@HoqhCVY5Jh2jJUK0Nvotpa | maxon::Float64 | Input | false | false | false |  | 1 | 0.5 | 
Distribution/Random Animation/Loop Period         | <in@TZpQgf2NNdlp77XXtpzxkY | maxon::TimeValue | Input | false | false | false |  |  | 0 | 
Distribution/Random Animation/Noise Frequency | <in@JuSf3DPRKFWks5YBsafZqf | maxon::Float64 | Input | false | false | false |  |  | 1 | 
Distribution/Random Animation/Override Time | <in@E$7EEHyDLV9iwDfd9QSqlb | maxon::Bool | Input | false | false | false |  |  | false | 
Distribution/Random Animation/Random Offset | <in@JSqLPVo6J5FrBstBHPCWCd | maxon::Float64 | Input | false | false | false |  | 1 | 0 | 
Distribution/Random Animation/Time | <in@GBQ_zQoZGRyuIqjJYJ4QLY | maxon::TimeValue | Input | false | false | false |  |  | 1 | 
Distribution/Random Density | <in@SCrmBdb0PhppKi7Fnctd_1 | maxon::Float64 | Input | false | false | false |  | 1 | 0.5 | 
Distribution/Random Scale Max | <in@dJ_V3kxqBh6sm5iDEGC3rK | maxon::Float64 | Input | false | false | false |  |  | 2 | 
Distribution/Random Scale Min | <float | maxon::Float64 | Input | false | false | false |  |  | 0.5 | 
Distribution/Randomize Cuts | <in@RoPwR3_vElqp_sjM0mToN3 | maxon::Float64 | Input | false | false | false |  | 1 | 0.5 | 
Distribution/Scale | <in@KO8ak3QtGlZmIf_1e3LgvL | maxon::Float64 | Input | false | false | false |  |  | 1 | 
Distribution/Scale Facing | <in@NlOOJ2sBFVdmLlyzxvWR6O | maxon::Int64 | Input | false | false | true |  |  | 0 | None = 0, Set = 1, Proportional = 2, Random = 3
Distribution/Scale Set | <in@Kr_MvVQjFpcgBuqDg2a7_7 | maxon::Float64 | Input | false | false | false |  |  | 50 | 
Distribution/Seed | <float1 | maxon::Float64 | Input | false | false | false |  |  | 12345 | 
Distribution/Size Height | <in@auID7Q$9MZdqgbiSZBXBju | maxon::Float64 | Input | false | false | false |  |  | 200 | 
Distribution/Size Width | <in@XkRwN7rSKhotR_aZFB_klt | maxon::Float64 | Input | false | false | false |  |  | 200 | 
Distribution/Spin | <in@AINrE_oJFZNtGn5Yitd1Ma | maxon::Int64 | Input | false | false | true |  |  | 0 | Auto = 0, Opposites = 1, Random = 2
Distribution/Subdivision Type | <in@G_EP_UCjFhonGAklp26ZDw | maxon::Int64 | Input | false | false | true |  |  | 0 | Single = 0, Double = 1, Quad = 2
Outputs/Distribution | >distdataout | maxon::ArrayContainer<maxon::Matrix64, maxon::Int64, maxon::Int64, maxon::Vector64, maxon::Color64, maxon::Int64> | Output | false | false | false |  |  |  | 

