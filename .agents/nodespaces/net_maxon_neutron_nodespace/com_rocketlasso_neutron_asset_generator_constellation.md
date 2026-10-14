# Node Template: Constellation

- **Node Space ID:** `net.maxon.neutron.nodespace`
- **Template ID:** `com.rocketlasso.neutron.asset.generator.constellation`
- **Template Name:** `Constellation`

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
Basic/Show Tag | net.maxon.neutron.showtag | maxon::Bool | Attribute | false | false | false |  |  |  | 
Filter Tags | net.maxon.node.base.filtertags | maxon::CString | Attribute | false | false | false |  |  |  | 
Inputs/Object/Matrix | <objectinput/matrix | maxon::Matrix | Attribute | false | false | false |  |  |  | 
Node Category | net.maxon.node.base.category | maxon::InternedId | Attribute | false | false | true |  |  | functions | operators = operators, distributions = distributions, geometries = geometries, patterns = patterns, primitives = primitives, effectors = effectors, fields = fields, functions = functions, structures = structures, geomodifiers = geomodifiers, geogenerators = geogenerators
Object/Children/Object Bundle.1/Color | <in@KG8f$_KBBRto0PkVC2K9GR/_0/color | maxon::Color | Attribute | false | false | false |  |  | (1,1,1) | 
Object/Children/Object Bundle.1/Geometry | <in@KG8f$_KBBRto0PkVC2K9GR/_0/geometry | maxon::GeometryObject | Attribute | false | false | false |  |  |  | 
Object/Children/Object Bundle.1/Matrix | <in@KG8f$_KBBRto0PkVC2K9GR/_0/matrix | maxon::Matrix | Attribute | false | false | false |  |  |  | 
Object/Children/Object Bundle.2/Color | <in@KG8f$_KBBRto0PkVC2K9GR/_1/color | maxon::Color | Attribute | false | false | false |  |  | (1,1,1) | 
Object/Children/Object Bundle.2/Geometry | <in@KG8f$_KBBRto0PkVC2K9GR/_1/geometry | maxon::GeometryObject | Attribute | false | false | false |  |  |  | 
Object/Children/Object Bundle.2/Matrix | <in@KG8f$_KBBRto0PkVC2K9GR/_1/matrix | maxon::Matrix | Attribute | false | false | false |  |  |  | 
Object/Point Source/Color | <object/color | maxon::Color | Attribute | false | false | false |  |  | (1,1,1) | 
Object/Point Source/Geometry | <object/geometry | maxon::GeometryObject | Attribute | false | false | false |  |  |  | 
Object/Point Source/Global Matrix | <object/globalmatrix | maxon::Matrix | Attribute | false | false | false |  |  |  | 
Object/Point Source/Matrix | <object/matrix | maxon::Matrix | Attribute | false | false | false |  |  |  | 
Object/Point Source/Name | <object/objectname | maxon::String | Attribute | false | false | false |  |  |  | 
Outputs/Object/Matrix | >matrixout/matrix | maxon::Matrix | Attribute | false | false | false |  |  |  | 
Preview/Node | net.maxon.node.base.nodepreviewimage | maxon::ImageBaseRef | Attribute | false | false | false |  |  |  | 
Basic/Bypass | <net.maxon.node.bypassable.bypass | maxon::Bool | Input | false | false | false |  |  |  | 
Basic/Children | <net.maxon.neutron.op.objectbase.children | net.maxon.neutron.portbundle.object | Input | true | false | false |  |  |  | 
Color/Connection Color  | <enum1 | maxon::Int64 | Input | false | false | true |  |  | 0 | Gradient = 0, Point Color = 1, Particle Color = 2
Color/Gradient | <in@JhFkiodNDJnkvTK0dqmsiR | net.maxon.render.portbundle.gradient | Input | true | true | false |  |  |  | 
Color/Gradient Point | <in@OAP9898KPFBmM_TAJWjVJq | net.maxon.render.portbundle.gradient | Input | true | true | false |  |  |  | 
Color/Gradient Point/Knot.1 | <in@OAP9898KPFBmM_TAJWjVJq/_0 | net.maxon.render.portbundle.gradient | Input | false | false | false |  |  |  | 
Color/Gradient Point/Knot.1/Bias Position | <in@OAP9898KPFBmM_TAJWjVJq/_0/bias | maxon::Float | Input | false | false | false |  | 1 | 0.5 | 
Color/Gradient Point/Knot.1/Color | <in@OAP9898KPFBmM_TAJWjVJq/_0/color | maxon::ColorA | Input | false | false | false |  |  | (1,1,1,1) | 
Color/Gradient Point/Knot.1/Interpolation | <in@OAP9898KPFBmM_TAJWjVJq/_0/interpolation | maxon::InternedId | Input | false | false | true |  |  | smoothknot | Smooth = smoothknot, Cubic = cubicknot, Cubic Bias = cubicbias, Linear = linearknot, Step = none, Blend = blend
Color/Gradient Point/Knot.1/Knot Position | <in@OAP9898KPFBmM_TAJWjVJq/_0/position | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Color/Gradient Point/Knot.2 | <in@OAP9898KPFBmM_TAJWjVJq/_3 | net.maxon.render.portbundle.gradient | Input | false | false | false |  |  |  | 
Color/Gradient Point/Knot.2/Bias Position | <in@OAP9898KPFBmM_TAJWjVJq/_3/bias | maxon::Float | Input | false | false | false |  | 1 | 0.5 | 
Color/Gradient Point/Knot.2/Color | <in@OAP9898KPFBmM_TAJWjVJq/_3/color | maxon::ColorA | Input | false | false | false |  |  | (1,1,1,1) | 
Color/Gradient Point/Knot.2/Interpolation | <in@OAP9898KPFBmM_TAJWjVJq/_3/interpolation | maxon::InternedId | Input | false | false | true |  |  | smoothknot | Smooth = smoothknot, Cubic = cubicknot, Cubic Bias = cubicbias, Linear = linearknot, Step = none, Blend = blend
Color/Gradient Point/Knot.2/Knot Position | <in@OAP9898KPFBmM_TAJWjVJq/_3/position | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Color/Gradient Point/Knot.3 | <in@OAP9898KPFBmM_TAJWjVJq/_7 | net.maxon.render.portbundle.gradient | Input | false | false | false |  |  |  | 
Color/Gradient Point/Knot.3/Bias Position | <in@OAP9898KPFBmM_TAJWjVJq/_7/bias | maxon::Float | Input | false | false | false |  | 1 | 0.5 | 
Color/Gradient Point/Knot.3/Color | <in@OAP9898KPFBmM_TAJWjVJq/_7/color | maxon::ColorA | Input | false | false | false |  |  | (1,1,1,1) | 
Color/Gradient Point/Knot.3/Interpolation | <in@OAP9898KPFBmM_TAJWjVJq/_7/interpolation | maxon::InternedId | Input | false | false | true |  |  | smoothknot | Smooth = smoothknot, Cubic = cubicknot, Cubic Bias = cubicbias, Linear = linearknot, Step = none, Blend = blend
Color/Gradient Point/Knot.3/Knot Position | <in@OAP9898KPFBmM_TAJWjVJq/_7/position | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Color/Gradient/Knot.1 | <in@JhFkiodNDJnkvTK0dqmsiR/_0 | net.maxon.render.portbundle.gradient | Input | false | false | false |  |  |  | 
Color/Gradient/Knot.1/Bias Position | <in@JhFkiodNDJnkvTK0dqmsiR/_0/bias | maxon::Float | Input | false | false | false |  | 1 | 0.5 | 
Color/Gradient/Knot.1/Color | <in@JhFkiodNDJnkvTK0dqmsiR/_0/color | maxon::ColorA | Input | false | false | false |  |  | (1,1,1,1) | 
Color/Gradient/Knot.1/Interpolation | <in@JhFkiodNDJnkvTK0dqmsiR/_0/interpolation | maxon::InternedId | Input | false | false | true |  |  | smoothknot | Smooth = smoothknot, Cubic = cubicknot, Cubic Bias = cubicbias, Linear = linearknot, Step = none, Blend = blend
Color/Gradient/Knot.1/Knot Position | <in@JhFkiodNDJnkvTK0dqmsiR/_0/position | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Color/Gradient/Knot.2 | <in@JhFkiodNDJnkvTK0dqmsiR/_2 | net.maxon.render.portbundle.gradient | Input | false | false | false |  |  |  | 
Color/Gradient/Knot.2/Bias Position | <in@JhFkiodNDJnkvTK0dqmsiR/_2/bias | maxon::Float | Input | false | false | false |  | 1 | 0.5 | 
Color/Gradient/Knot.2/Color | <in@JhFkiodNDJnkvTK0dqmsiR/_2/color | maxon::ColorA | Input | false | false | false |  |  | (1,1,1,1) | 
Color/Gradient/Knot.2/Interpolation | <in@JhFkiodNDJnkvTK0dqmsiR/_2/interpolation | maxon::InternedId | Input | false | false | true |  |  | smoothknot | Smooth = smoothknot, Cubic = cubicknot, Cubic Bias = cubicbias, Linear = linearknot, Step = none, Blend = blend
Color/Gradient/Knot.2/Knot Position | <in@JhFkiodNDJnkvTK0dqmsiR/_2/position | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Color/Gradient/Knot.3 | <in@JhFkiodNDJnkvTK0dqmsiR/_5 | net.maxon.render.portbundle.gradient | Input | false | false | false |  |  |  | 
Color/Gradient/Knot.3/Bias Position | <in@JhFkiodNDJnkvTK0dqmsiR/_5/bias | maxon::Float | Input | false | false | false |  | 1 | 0.5 | 
Color/Gradient/Knot.3/Color | <in@JhFkiodNDJnkvTK0dqmsiR/_5/color | maxon::ColorA | Input | false | false | false |  |  | (1,1,1,1) | 
Color/Gradient/Knot.3/Interpolation | <in@JhFkiodNDJnkvTK0dqmsiR/_5/interpolation | maxon::InternedId | Input | false | false | true |  |  | smoothknot | Smooth = smoothknot, Cubic = cubicknot, Cubic Bias = cubicbias, Linear = linearknot, Step = none, Blend = blend
Color/Gradient/Knot.3/Knot Position | <in@JhFkiodNDJnkvTK0dqmsiR/_5/position | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Color/Point Color | <in@B4LizPL$IZJs21DFzcS9CO | maxon::Int64 | Input | false | false | true |  |  | 0 | Gradient = 0, Point Color = 1, Particle Color = 2
Color/Vertex Color Map | <attr@SkKsAzozA5ApxxPQ4zVVCN | maxon::String | Input | false | false | false |  |  | Vertex Color | 
Color/Vertex Color Map | <string | maxon::String | Input | false | false | false |  |  | Vertex Color | 
Connections/Avoid Intersection | <bool5 | maxon::Bool | Input | false | false | false |  |  | false | 
Connections/Connection Radius | <float3 | maxon::Float64 | Input | false | false | false |  |  | 0.5 | 
Connections/Connections | <in@ahbjkTB6J1zvLLgKp2DHoj | net.maxon.render.portbundle.spline | Input | false | true | false |  |  |  | 
Connections/Connections/Link End Positions | <in@ahbjkTB6J1zvLLgKp2DHoj/linkendpositions | maxon::Bool | Input | false | false | false |  |  |  | 
Connections/Connections/Link End Tangents | <in@ahbjkTB6J1zvLLgKp2DHoj/linkendtangents | maxon::Bool | Input | false | false | false |  |  |  | 
Connections/Connections/Max | <in@ahbjkTB6J1zvLLgKp2DHoj/max | maxon::Vector2d | Input | false | false | false |  |  | (1,1) | 
Connections/Connections/Min | <in@ahbjkTB6J1zvLLgKp2DHoj/min | maxon::Vector2d | Input | false | false | false |  |  |  | 
Connections/Connections/Points | <in@ahbjkTB6J1zvLLgKp2DHoj/points | net.maxon.render.portbundle.splinepoint | Input | true | false | false |  |  |  | 
Connections/Connections/Points/Point.1 | <in@ahbjkTB6J1zvLLgKp2DHoj/points/_0 | net.maxon.render.portbundle.splinepoint | Input | false | false | false |  |  |  | 
Connections/Connections/Points/Point.1/Break Tangent | <in@ahbjkTB6J1zvLLgKp2DHoj/points/_0/breaktangent | maxon::Bool | Input | false | false | false |  |  |  | 
Connections/Connections/Points/Point.1/Interpolation | <in@ahbjkTB6J1zvLLgKp2DHoj/points/_0/interpolation | maxon::InternedId | Input | false | false | true |  |  | spline | Spline = spline, Cubic = cubic, Linear = linear
Connections/Connections/Points/Point.1/Keep Visual Angle | <in@ahbjkTB6J1zvLLgKp2DHoj/points/_0/keepvisualangle | maxon::Bool | Input | false | false | false |  |  |  | 
Connections/Connections/Points/Point.1/Lock Angle | <in@ahbjkTB6J1zvLLgKp2DHoj/points/_0/lockangle | maxon::Bool | Input | false | false | false |  |  |  | 
Connections/Connections/Points/Point.1/Lock Length | <in@ahbjkTB6J1zvLLgKp2DHoj/points/_0/locklength | maxon::Bool | Input | false | false | false |  |  |  | 
Connections/Connections/Points/Point.1/Lock X | <in@ahbjkTB6J1zvLLgKp2DHoj/points/_0/lockx | maxon::Bool | Input | false | false | false |  |  |  | 
Connections/Connections/Points/Point.1/Lock Y | <in@ahbjkTB6J1zvLLgKp2DHoj/points/_0/locky | maxon::Bool | Input | false | false | false |  |  |  | 
Connections/Connections/Points/Point.1/Position X | <in@ahbjkTB6J1zvLLgKp2DHoj/points/_0/positionx | maxon::Float | Input | false | false | false |  |  | 0 | 
Connections/Connections/Points/Point.1/Position Y | <in@ahbjkTB6J1zvLLgKp2DHoj/points/_0/positiony | maxon::Float | Input | false | false | false |  |  | 0 | 
Connections/Connections/Points/Point.1/Tangent Left | <in@ahbjkTB6J1zvLLgKp2DHoj/points/_0/tangentleft | maxon::Vector2d | Input | false | false | false |  |  |  | 
Connections/Connections/Points/Point.1/Tangent Right | <in@ahbjkTB6J1zvLLgKp2DHoj/points/_0/tangentright | maxon::Vector2d | Input | false | false | false |  |  |  | 
Connections/Connections/Points/Point.2 | <in@ahbjkTB6J1zvLLgKp2DHoj/points/_1 | net.maxon.render.portbundle.splinepoint | Input | false | false | false |  |  |  | 
Connections/Connections/Points/Point.2/Break Tangent | <in@ahbjkTB6J1zvLLgKp2DHoj/points/_1/breaktangent | maxon::Bool | Input | false | false | false |  |  |  | 
Connections/Connections/Points/Point.2/Interpolation | <in@ahbjkTB6J1zvLLgKp2DHoj/points/_1/interpolation | maxon::InternedId | Input | false | false | true |  |  | spline | Spline = spline, Cubic = cubic, Linear = linear
Connections/Connections/Points/Point.2/Keep Visual Angle | <in@ahbjkTB6J1zvLLgKp2DHoj/points/_1/keepvisualangle | maxon::Bool | Input | false | false | false |  |  |  | 
Connections/Connections/Points/Point.2/Lock Angle | <in@ahbjkTB6J1zvLLgKp2DHoj/points/_1/lockangle | maxon::Bool | Input | false | false | false |  |  |  | 
Connections/Connections/Points/Point.2/Lock Length | <in@ahbjkTB6J1zvLLgKp2DHoj/points/_1/locklength | maxon::Bool | Input | false | false | false |  |  |  | 
Connections/Connections/Points/Point.2/Lock X | <in@ahbjkTB6J1zvLLgKp2DHoj/points/_1/lockx | maxon::Bool | Input | false | false | false |  |  |  | 
Connections/Connections/Points/Point.2/Lock Y | <in@ahbjkTB6J1zvLLgKp2DHoj/points/_1/locky | maxon::Bool | Input | false | false | false |  |  |  | 
Connections/Connections/Points/Point.2/Position X | <in@ahbjkTB6J1zvLLgKp2DHoj/points/_1/positionx | maxon::Float | Input | false | false | false |  |  | 0 | 
Connections/Connections/Points/Point.2/Position Y | <in@ahbjkTB6J1zvLLgKp2DHoj/points/_1/positiony | maxon::Float | Input | false | false | false |  |  | 0 | 
Connections/Connections/Points/Point.2/Tangent Left | <in@ahbjkTB6J1zvLLgKp2DHoj/points/_1/tangentleft | maxon::Vector2d | Input | false | false | false |  |  |  | 
Connections/Connections/Points/Point.2/Tangent Right | <in@ahbjkTB6J1zvLLgKp2DHoj/points/_1/tangentright | maxon::Vector2d | Input | false | false | false |  |  |  | 
Connections/Connections/Tension | <in@ahbjkTB6J1zvLLgKp2DHoj/tension | maxon::Float | Input | false | false | false |  | 1 | 1 | 
Connections/Cylinder Segments | <integer | maxon::Int64 | Input | false | false | false | 3 | 5000 | 24 | 
Connections/Enable | <bool | maxon::Bool | Input | false | false | false |  |  | true | 
Connections/Far Radius | <float | maxon::Float64 | Input | false | false | false |  |  | 0 | 
Connections/Far Radius | <float@ASrmqDnXHdfjxbZL7sHJlp | maxon::Float64 | Input | false | false | false |  |  | 0 | 
Connections/Length | <enum | maxon::Int64 | Input | false | false | true |  |  |  | Full = 0, Scale = 1, Split Scale = 2
Connections/Mirror Geometry | <bool1 | maxon::Bool | Input | false | false | false |  |  | false | 
Connections/Pivot | <float8 | maxon::Float64 | Input | false | false | false |  |  | 0 | 
Connections/Radius | <in@QPwPOxQiHhboD_2GlWrahN | maxon::Float64 | Input | false | false | false |  |  | 3 | 
Connections/Radius Multiplier | <in@TUtseXFqEV7qyIHRjkAEHL | maxon::Float64 | Input | false | false | false |  |  | 1 | 
Connections/Radius RemapXXX | <in@THowl3ztPlcmxYTIGtLRzm | maxon::Bool | Input | false | false | false |  |  | false | 
Connections/Radius Source | <in@G3M5epaWM9Dlq2AB30VnuN | maxon::Int64 | Input | false | false | true |  |  |  | Distance = 0, Vertex Map = 1, Particle Radius = 2
Connections/Reference From | <in@LuQ_vwVBFJ4s73sKZd1IZm | maxon::Int64 | Input | false | false | true |  |  | 1 | Largest Point = 0, Smallest Point = 1
Connections/Vertex Map | <in@MqSy6xQmM56hNeLSUoPk0J | maxon::String | Input | false | false | false |  |  | Radius | 
Coord/Matrix | <net.maxon.neutron.op.objectbase.matrix | maxon::Matrix64 | Input | false | false | false |  |  |  | 
Inputs/Object | <objectinput | net.maxon.neutron.portbundle.object | Input | false | true | false |  |  |  | 
Inputs/Object/Parent Matrix | <objectinput/parentmatrix |  | Input | false | false | false |  |  |  | 
Inputs/Object/Position | <objectinput/translation |  | Input | false | false | false |  |  |  | 
Inputs/Object/Rotation/Scale/Shear | <objectinput/sqrmatrix |  | Input | false | false | false |  |  |  | 
Inputs/Object/Scope | <objectinput/domain |  | Input | false | false | false |  |  |  | 
Inputs/Op | <net.maxon.neutron.op.input | net.maxon.neutron.portbundle.object | Input | false | true | false |  |  |  | 
Inputs/Op/Position | <net.maxon.neutron.op.input/translation |  | Input | false | false | false |  |  |  | 
Inputs/Op/Rotation/Scale/Shear | <net.maxon.neutron.op.input/sqrmatrix |  | Input | false | false | false |  |  |  | 
Inputs/Op/Scope | <net.maxon.neutron.op.input/domain |  | Input | false | false | false |  |  |  | 
Object/Children | <in@KG8f$_KBBRto0PkVC2K9GR | net.maxon.neutron.portbundle.object | Input | true | true | false |  |  |  | 
Object/Children/Object Bundle.1 | <in@KG8f$_KBBRto0PkVC2K9GR/_0 | net.maxon.neutron.portbundle.object | Input | false | false | false |  |  |  | 
Object/Children/Object Bundle.1/Children | <in@KG8f$_KBBRto0PkVC2K9GR/_0/children |  | Input | false | false | false |  |  |  | 
Object/Children/Object Bundle.1/Filter | <in@KG8f$_KBBRto0PkVC2K9GR/_0/filter | maxon::Bool | Input | false | false | false |  |  |  | 
Object/Children/Object Bundle.1/Material | <in@KG8f$_KBBRto0PkVC2K9GR/_0/material | maxon::DataDictionary | Input | false | false | false |  |  |  | 
Object/Children/Object Bundle.1/Scope | <in@KG8f$_KBBRto0PkVC2K9GR/_0/domain |  | Input | false | false | false |  |  |  | 
Object/Children/Object Bundle.2 | <in@KG8f$_KBBRto0PkVC2K9GR/_1 | net.maxon.neutron.portbundle.object | Input | false | false | false |  |  |  | 
Object/Children/Object Bundle.2/Children | <in@KG8f$_KBBRto0PkVC2K9GR/_1/children |  | Input | false | false | false |  |  |  | 
Object/Children/Object Bundle.2/Filter | <in@KG8f$_KBBRto0PkVC2K9GR/_1/filter | maxon::Bool | Input | false | false | false |  |  |  | 
Object/Children/Object Bundle.2/Material | <in@KG8f$_KBBRto0PkVC2K9GR/_1/material | maxon::DataDictionary | Input | false | false | false |  |  |  | 
Object/Children/Object Bundle.2/Scope | <in@KG8f$_KBBRto0PkVC2K9GR/_1/domain |  | Input | false | false | false |  |  |  | 
Object/Connected | <float1 | maxon::Float64 | Input | false | false | false |  |  | 0 | 
Object/Final Output | <in@X4le01v3LNcjzQkEnt2t0M | maxon::Int64 | Input | false | false | true |  |  | 1 | Spline = 0, Mesh = 2, Instances = 1
Object/Point Source | <object | net.maxon.neutron.portbundle.objectinput | Input | false | true | false |  |  |  | 
Object/Search Distance | <float2 | maxon::Float64 | Input | false | false | false |  |  | 40 | 
Outputs/Object/Parent Matrix | >matrixout/parentmatrix |  | Input | false | false | false |  |  |  | 
Outputs/Object/Position | >matrixout/translation |  | Input | false | false | false |  |  |  | 
Outputs/Object/Rotation/Scale/Shear | >matrixout/sqrmatrix |  | Input | false | false | false |  |  |  | 
Outputs/Object/Scope | >matrixout/domain |  | Input | false | false | false |  |  |  | 
Outputs/Op/Children | >net.maxon.neutron.op.output/children |  | Input | false | false | false |  |  |  | 
Points/Enable | <in@QOJWSVT$DFGv6bTGftjLpU | maxon::Bool | Input | false | false | false |  |  | true | 
Points/Point Radius | <float6 | maxon::Float64 | Input | false | false | false |  |  | 2 | 
Points/Radius | <in@Mna7qok$EZFie_ypAgECnL | maxon::Float64 | Input | false | false | false |  |  | 3 | 
Points/Radius Multiplier | <float7 | maxon::Float64 | Input | false | false | false |  |  | 1 | 
Points/Radius Source | <in@Ag0N6ZQ6EhDud1FJShG0OM | maxon::Int64 | Input | false | false | true |  |  |  | Distance = 0, Vertex Map = 1, Particle Radius = 2
Points/Remap | <in@G$QgriWzMBHlKSzF4WjZBq | net.maxon.render.portbundle.spline | Input | false | true | false |  |  |  | 
Points/Remap RadiusXXX | <in@cIPk4ZeUGtAlmgvMxXTqNY | maxon::Bool | Input | false | false | false |  |  | false | 
Points/Remap/Link End Positions | <in@G$QgriWzMBHlKSzF4WjZBq/linkendpositions | maxon::Bool | Input | false | false | false |  |  |  | 
Points/Remap/Link End Tangents | <in@G$QgriWzMBHlKSzF4WjZBq/linkendtangents | maxon::Bool | Input | false | false | false |  |  |  | 
Points/Remap/Max | <in@G$QgriWzMBHlKSzF4WjZBq/max | maxon::Vector2d | Input | false | false | false |  |  | (1,1) | 
Points/Remap/Min | <in@G$QgriWzMBHlKSzF4WjZBq/min | maxon::Vector2d | Input | false | false | false |  |  |  | 
Points/Remap/Points | <in@G$QgriWzMBHlKSzF4WjZBq/points | net.maxon.render.portbundle.splinepoint | Input | true | false | false |  |  |  | 
Points/Remap/Points/Point.1 | <in@G$QgriWzMBHlKSzF4WjZBq/points/_0 | net.maxon.render.portbundle.splinepoint | Input | false | false | false |  |  |  | 
Points/Remap/Points/Point.1/Break Tangent | <in@G$QgriWzMBHlKSzF4WjZBq/points/_0/breaktangent | maxon::Bool | Input | false | false | false |  |  |  | 
Points/Remap/Points/Point.1/Interpolation | <in@G$QgriWzMBHlKSzF4WjZBq/points/_0/interpolation | maxon::InternedId | Input | false | false | true |  |  | spline | Spline = spline, Cubic = cubic, Linear = linear
Points/Remap/Points/Point.1/Keep Visual Angle | <in@G$QgriWzMBHlKSzF4WjZBq/points/_0/keepvisualangle | maxon::Bool | Input | false | false | false |  |  |  | 
Points/Remap/Points/Point.1/Lock Angle | <in@G$QgriWzMBHlKSzF4WjZBq/points/_0/lockangle | maxon::Bool | Input | false | false | false |  |  |  | 
Points/Remap/Points/Point.1/Lock Length | <in@G$QgriWzMBHlKSzF4WjZBq/points/_0/locklength | maxon::Bool | Input | false | false | false |  |  |  | 
Points/Remap/Points/Point.1/Lock X | <in@G$QgriWzMBHlKSzF4WjZBq/points/_0/lockx | maxon::Bool | Input | false | false | false |  |  |  | 
Points/Remap/Points/Point.1/Lock Y | <in@G$QgriWzMBHlKSzF4WjZBq/points/_0/locky | maxon::Bool | Input | false | false | false |  |  |  | 
Points/Remap/Points/Point.1/Position X | <in@G$QgriWzMBHlKSzF4WjZBq/points/_0/positionx | maxon::Float | Input | false | false | false |  |  | 0 | 
Points/Remap/Points/Point.1/Position Y | <in@G$QgriWzMBHlKSzF4WjZBq/points/_0/positiony | maxon::Float | Input | false | false | false |  |  | 0 | 
Points/Remap/Points/Point.1/Tangent Left | <in@G$QgriWzMBHlKSzF4WjZBq/points/_0/tangentleft | maxon::Vector2d | Input | false | false | false |  |  |  | 
Points/Remap/Points/Point.1/Tangent Right | <in@G$QgriWzMBHlKSzF4WjZBq/points/_0/tangentright | maxon::Vector2d | Input | false | false | false |  |  |  | 
Points/Remap/Points/Point.2 | <in@G$QgriWzMBHlKSzF4WjZBq/points/_1 | net.maxon.render.portbundle.splinepoint | Input | false | false | false |  |  |  | 
Points/Remap/Points/Point.2/Break Tangent | <in@G$QgriWzMBHlKSzF4WjZBq/points/_1/breaktangent | maxon::Bool | Input | false | false | false |  |  |  | 
Points/Remap/Points/Point.2/Interpolation | <in@G$QgriWzMBHlKSzF4WjZBq/points/_1/interpolation | maxon::InternedId | Input | false | false | true |  |  | spline | Spline = spline, Cubic = cubic, Linear = linear
Points/Remap/Points/Point.2/Keep Visual Angle | <in@G$QgriWzMBHlKSzF4WjZBq/points/_1/keepvisualangle | maxon::Bool | Input | false | false | false |  |  |  | 
Points/Remap/Points/Point.2/Lock Angle | <in@G$QgriWzMBHlKSzF4WjZBq/points/_1/lockangle | maxon::Bool | Input | false | false | false |  |  |  | 
Points/Remap/Points/Point.2/Lock Length | <in@G$QgriWzMBHlKSzF4WjZBq/points/_1/locklength | maxon::Bool | Input | false | false | false |  |  |  | 
Points/Remap/Points/Point.2/Lock X | <in@G$QgriWzMBHlKSzF4WjZBq/points/_1/lockx | maxon::Bool | Input | false | false | false |  |  |  | 
Points/Remap/Points/Point.2/Lock Y | <in@G$QgriWzMBHlKSzF4WjZBq/points/_1/locky | maxon::Bool | Input | false | false | false |  |  |  | 
Points/Remap/Points/Point.2/Position X | <in@G$QgriWzMBHlKSzF4WjZBq/points/_1/positionx | maxon::Float | Input | false | false | false |  |  | 0 | 
Points/Remap/Points/Point.2/Position Y | <in@G$QgriWzMBHlKSzF4WjZBq/points/_1/positiony | maxon::Float | Input | false | false | false |  |  | 0 | 
Points/Remap/Points/Point.2/Tangent Left | <in@G$QgriWzMBHlKSzF4WjZBq/points/_1/tangentleft | maxon::Vector2d | Input | false | false | false |  |  |  | 
Points/Remap/Points/Point.2/Tangent Right | <in@G$QgriWzMBHlKSzF4WjZBq/points/_1/tangentright | maxon::Vector2d | Input | false | false | false |  |  |  | 
Points/Remap/Tension | <in@G$QgriWzMBHlKSzF4WjZBq/tension | maxon::Float | Input | false | false | false |  | 1 | 1 | 
Points/Size Outer | <float5 | maxon::Float64 | Input | false | false | false |  |  | 0 | 
Points/Sphere Segments | <in@Ti5yRvwtH5glnZVIt0s7LP | maxon::Int64 | Input | false | false | false | 3 | 5000 | 24 | 
Points/Vertex Map | <in@LI$oCemcLplseGrowoEFAK | maxon::String | Input | false | false | false |  |  | Radius | 
Restrict/A [Point Selection] | <in@MFSfK60LDZFnx$wFV__0Up | maxon::String | Input | false | false | false |  |  | "A" | 
Restrict/B [Point Selection] | <in@Gh3YbO0FIhklJEKaoFhd5v | maxon::String | Input | false | false | false |  |  | "B" | 
Restrict/Don't Interconnect [Point Selection] | <strings | maxon::String | Input | false | false | false |  |  |  | 
Restrict/Max Connections | <integer1 | maxon::Int64 | Input | false | false | false |  |  | 50 | 
Restrict/Restrict | <bool3 | maxon::Bool | Input | false | false | false |  |  | true | 
Outputs/Edge Distribution | >out@Tdxwb2ktFtdtms5WvOdLd3 | maxon::ArrayContainer<maxon::Matrix64, maxon::Int64, maxon::Vector64, maxon::Color64> | Output | false | false | false |  |  |  | 
Outputs/Object | >matrixout | net.maxon.neutron.portbundle.object | Output | false | true | false |  |  |  | 
Outputs/Op | >net.maxon.neutron.op.output | net.maxon.neutron.portbundle.object | Output | false | true | false |  |  |  | 
Outputs/Output | >children.out |  | Output | false | false | false |  |  |  | 
Outputs/Point Distribution | >out@SEffpvcuJ1JnKxgiTU9P72 | maxon::ArrayContainer<maxon::Matrix64, maxon::Int64, maxon::Vector64, maxon::Color64> | Output | false | false | false |  |  |  | 

