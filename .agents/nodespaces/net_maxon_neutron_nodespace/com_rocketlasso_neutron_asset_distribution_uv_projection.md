# Node Template: UV Projection Distribution

- **Node Space ID:** `net.maxon.neutron.nodespace`
- **Template ID:** `com.rocketlasso.neutron.asset.distribution.uv.projection`
- **Template Name:** `UV Projection Distribution`

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
Color/Animate | <attr@IMFfyQiWAlcs44ZKbDMbrY | maxon::Int64 | Input | false | false | true |  |  |  | Frame = 0, Live = 1
Color/Color | <color1 | maxon::Color64 | Input | false | false | false |  |  | (0.312,0.116,0.1) | 
Color/Direction | <in@NNlcKpn2AFVn7PKXcxCVFM | maxon::Int64 | Input | false | false | true |  |  |  | U = 0, V = 1
Color/Frame | <time2 | maxon::TimeValue | Input | false | false | false |  |  |  | 
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
Color/Max Speed | <in@TVzxM$ToB5yrOY8fhotlZ1 | maxon::Float64 | Input | false | false | false |  |  | 0 | 
Color/Min Speed | <in@IEQEfw8QO9crGtZ_kcoyZ2 | maxon::Float64 | Input | false | false | false |  |  | 0 | 
Color/Offset | <time1 | maxon::TimeValue | Input | false | false | false |  |  |  | 
Color/Path | <url1 | maxon::Url | Input | false | false | false |  |  | asset:///file_5b6a5fe03176444c~.png?name=UV Test Grid.png&db=MaxonAssets.db (assets.maxon.net) | 
Color/Range | <in@HS_O0qeOCBUr3Q_dGGmfXr | maxon::Int64 | Input | false | false | true |  |  |  | Automatic = 0, Manual = 1
Color/Sample Mode | <enum5 | maxon::Int64 | Input | false | false | true |  |  |  | Constant = 0, Linear = 1, Random = 2, Speed = 3, UV (Image) = 4
Color/Sample UV | <enum1 | maxon::Int64 | Input | false | false | true |  |  |  | Origin = 0, Current = 1
Distributions/Align Clone | <in@BWVidrjQH55jF5VKQwGjxN | maxon::Bool | Input | false | false | false |  |  | true | 
Distributions/Animation/Alignment | <in@ElOrznrFKtag6N5oDKRh0F | maxon::Int64 | Input | false | false | true |  |  |  | Facing = 0, Direction of Travel = 1
Distributions/Animation/Animation | <in@eYBFzTlNKFvp_nRm_JTM6A | maxon::Int64 | Input | false | false | true |  |  |  | Deterministic = 0, Dependent = 1
Distributions/Animation/Facing | <in@C_AvoVPxLVPiG7BslVGo8H | maxon::Float64 | Input | false | false | false |  |  | 0 | 
Distributions/Animation/Friction | <in@DlB1_eUjBdhorPRMqrLFu7 | maxon::Float64 | Input | false | false | false |  |  | 0.1 | 
Distributions/Animation/Noise Scale | <in@AAVwMxV8BRQoBkDGlvT4PC | maxon::Float64 | Input | false | false | false |  |  | 0.75 | 
Distributions/Animation/Noise Speed | <in@BUe1RvLJC5wi6eka9fWMSH | maxon::Float64 | Input | false | false | false |  |  | 0.25 | 
Distributions/Animation/Noise Type | <in@IzY6ngOLNJAnfxfQ1u2X21 | maxon::Id | Input | false | false | true |  |  | net.maxon.render.rendernoiseclass.perlin | registry#net.maxon.render.registry.rendernoiseclasses = registry#net.maxon.render.registry.rendernoiseclasses
Distributions/Animation/Random Facing | <in@ZygQ_05xN9$lVaQ6KM1POA | maxon::Float64 | Input | false | false | false |  |  | 0 | 
Distributions/Animation/Speed Multiplier | <in@J5dmOJWIL5cjkrO81B5aUF | maxon::Float64 | Input | false | false | false |  |  | 1 | 
Distributions/Animation/Speed U | <float3 | maxon::Float64 | Input | false | false | false |  |  | 0 | 
Distributions/Animation/Speed V | <in@CjtAzgP3G5hsPwUfnfYnzB | maxon::Float64 | Input | false | false | false |  |  | 0.005 | 
Distributions/Animation/Speed Variation | <in@ZLvvjz7xGJukGENjjDYtuG | maxon::Float64 | Input | false | false | false |  |  | 0 | 
Distributions/Animation/Turbulence U | <in@Xu1vF6KKAtQuSNELnfv_F2 | maxon::Float64 | Input | false | false | false |  |  | 0 | 
Distributions/Animation/Turbulence V | <in@P4wmUmRPCdShXUPMzarBP$ | maxon::Float64 | Input | false | false | false |  |  | 0 | 
Distributions/Animation/Variance | <in@Q2WS9l7$PNBhXwHZwYMsUz | maxon::Float64 | Input | false | false | false |  |  |  | 
Distributions/Animation/Variation | <float | maxon::Float64 | Input | false | false | false |  |  | 0 | 
Distributions/Animation/Variation U | <in@WWxS$sbGAh6l9WDGr263KF | maxon::Float64 | Input | false | false | false |  |  | 0 | 
Distributions/Animation/Variation V | <in@FgOcNM3sLNfu8H1Ue8j19D | maxon::Float64 | Input | false | false | false |  |  | 0 | 
Distributions/Animation/Wind U | <in@dBau7BeFJpym8qmytlorUE | maxon::Float64 | Input | false | false | false |  |  | 0 | 
Distributions/Animation/Wind V | <in@LSovnVFPPh5tQ0wbhsexmG | maxon::Float64 | Input | false | false | false |  |  | 0 | 
Distributions/Both Edges | <bool1 | maxon::Bool | Input | false | false | false |  |  | true | 
Distributions/Cloner Children | <clonerchildrenin | maxon::ArrayContainer<maxon::Matrix, maxon::Matrix, maxon::GeometryObject, maxon::GeometryObject, maxon::Range<maxon::Vector>, maxon::String> | Input | false | false | false |  |  |  | 
Distributions/Clones | <enum | maxon::Int64 | Input | false | false | true |  |  |  | Iterate = 0, Random = 1
Distributions/Global Cloner Matrix | <globalclonermatrixin | maxon::Matrix | Input | false | false | false |  |  |  | 
Distributions/Local Cloner Matrix | <localclonermatrixin | maxon::Matrix | Input | false | false | false |  |  |  | 
Distributions/Loop Edges | <bool | maxon::Bool | Input | false | false | false |  |  | true | 
Distributions/Objects Children | <objectchildren | maxon::ArrayContainer<maxon::GeometryObject, maxon::Matrix64, maxon::Matrix64, maxon::ColorA64, maxon::String> | Input | false | false | false |  |  |  | 
Distributions/Objects Children | <objectchildren1 | maxon::ArrayContainer<maxon::GeometryObject, maxon::Matrix64, maxon::Matrix64, maxon::ColorA64, maxon::String> | Input | false | false | false |  |  |  | 
Distributions/Objects Children | <objectchildren2 | maxon::ArrayContainer<maxon::GeometryObject, maxon::Matrix64, maxon::Matrix64, maxon::ColorA64, maxon::String> | Input | false | false | false |  |  |  | 
Distributions/Offset Mode | <in@K$h20v8bFFVn4ywuyCcz3J | maxon::Int64 | Input | false | false | true |  |  | 1 | Absolute = 0, Object = 1
Distributions/PreRotate | <in@CEUbstcXBBTpPgHy_AkI9s | maxon::Vector64 | Input | false | false | false |  |  |  | 
Distributions/Seed | <float1 | maxon::Float64 | Input | false | false | false |  |  | 12345 | 
Distributions/Smooth | <bool2 | maxon::Bool | Input | false | false | false |  |  | true | 
Distributions/Strays                   | <in@OblYwmYuIFQtaeh7qFkhmD | maxon::Int64 | Input | false | false | true |  |  | 2 | Skip = 0, Origin = 1, Scale to 0 = 2
Distributions/Surface Offset | <in@JRm9J3vsPJfrv9MUEaed2P | maxon::Float64 | Input | false | false | false |  |  | 0 | 
Distributions/Surface Offset(B) | <integer1 | maxon::Float64 | Input | false | false | false |  |  |  | 
Distributions/Time Offset | <float4 | maxon::TimeValue | Input | false | false | false |  |  |  | 
Distributions/UV Placement/Count | <in@MhF199TMKJHrWil_ArCDcE | maxon::Int64 | Input | false | false | false |  |  | 1000 | 
Distributions/UV Placement/Count U | <in@C3eWFXT6KBHoNzxv00DM$F | maxon::Int64 | Input | false | false | false |  |  | 25 | 
Distributions/UV Placement/Count V | <in@f2uuTeAeBJ9gAa_E02009E | maxon::Int64 | Input | false | false | false |  |  | 25 | 
Distributions/UV Placement/Distribution | <in@bblKgFG6EBqpN0bTxXBRJV | maxon::Int64 | Input | false | false | true |  |  |  | Grid = 0, Random = 1
Distributions/UV Placement/Length U | <in@LyGbSSMDJZrjMSnRzVdoKB | maxon::Float64 | Input | false | false | false |  |  | 1 | 
Distributions/UV Placement/Length V | <in@BHP0pNkrDBvnfufDgy72vB | maxon::Float64 | Input | false | false | false |  |  | 1 | 
Distributions/UV Placement/OffSet V | <in@YQq_sTY7JVrvQJoxOzbdHF | maxon::Float64 | Input | false | false | false |  |  |  | 
Distributions/UV Placement/Offset  U | <in@UaChkJ$lCdpsZynAZQ9GQD | maxon::Float64 | Input | false | false | false |  |  |  | 
Distributions/UV Placement/Visibility | <in@F4IX8SDcGFZq52oIlEM7RW | maxon::Float64 | Input | false | false | false |  | 1 | 1 | 
Outputs/Distribution | >distdataout | maxon::ArrayContainer<maxon::Matrix64, maxon::Int64, maxon::Int64, maxon::Vector64, maxon::Color64, maxon::Int64> | Output | false | false | false |  |  |  | 

