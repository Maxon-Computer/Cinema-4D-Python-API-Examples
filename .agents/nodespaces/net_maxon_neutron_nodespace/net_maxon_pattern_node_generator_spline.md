# Node Template: Spline Mapper

- **Node Space ID:** `net.maxon.neutron.nodespace`
- **Template ID:** `net.maxon.pattern.node.generator.spline`
- **Template Name:** `Spline Mapper`

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
Inputs/Input | <input | maxon::Float | Input | false | false | false |  | 1 |  | 
Inputs/Spline | <spline | net.maxon.render.portbundle.spline | Input | false | true | false |  |  |  | 
Inputs/Spline/Link End Positions | <spline/linkendpositions | maxon::Bool | Input | false | false | false |  |  |  | 
Inputs/Spline/Link End Tangents | <spline/linkendtangents | maxon::Bool | Input | false | false | false |  |  |  | 
Inputs/Spline/Max | <spline/max | maxon::Vector2d | Input | false | false | false |  |  | (1,1) | 
Inputs/Spline/Min | <spline/min | maxon::Vector2d | Input | false | false | false |  |  |  | 
Inputs/Spline/Points | <spline/points | net.maxon.render.portbundle.splinepoint | Input | true | false | false |  |  |  | 
Inputs/Spline/Points/Point.1 | <spline/points/_0 | net.maxon.render.portbundle.splinepoint | Input | false | false | false |  |  |  | 
Inputs/Spline/Points/Point.1/Break Tangent | <spline/points/_0/breaktangent | maxon::Bool | Input | false | false | false |  |  |  | 
Inputs/Spline/Points/Point.1/Interpolation | <spline/points/_0/interpolation | maxon::InternedId | Input | false | false | true |  |  | spline | Spline = spline, Cubic = cubic, Linear = linear
Inputs/Spline/Points/Point.1/Keep Visual Angle | <spline/points/_0/keepvisualangle | maxon::Bool | Input | false | false | false |  |  |  | 
Inputs/Spline/Points/Point.1/Lock Angle | <spline/points/_0/lockangle | maxon::Bool | Input | false | false | false |  |  |  | 
Inputs/Spline/Points/Point.1/Lock Length | <spline/points/_0/locklength | maxon::Bool | Input | false | false | false |  |  |  | 
Inputs/Spline/Points/Point.1/Lock X | <spline/points/_0/lockx | maxon::Bool | Input | false | false | false |  |  |  | 
Inputs/Spline/Points/Point.1/Lock Y | <spline/points/_0/locky | maxon::Bool | Input | false | false | false |  |  |  | 
Inputs/Spline/Points/Point.1/Position X | <spline/points/_0/positionx | maxon::Float | Input | false | false | false |  |  | 0 | 
Inputs/Spline/Points/Point.1/Position Y | <spline/points/_0/positiony | maxon::Float | Input | false | false | false |  |  | 0 | 
Inputs/Spline/Points/Point.1/Tangent Left | <spline/points/_0/tangentleft | maxon::Vector2d | Input | false | false | false |  |  |  | 
Inputs/Spline/Points/Point.1/Tangent Right | <spline/points/_0/tangentright | maxon::Vector2d | Input | false | false | false |  |  |  | 
Inputs/Spline/Points/Point.2 | <spline/points/_1 | net.maxon.render.portbundle.splinepoint | Input | false | false | false |  |  |  | 
Inputs/Spline/Points/Point.2/Break Tangent | <spline/points/_1/breaktangent | maxon::Bool | Input | false | false | false |  |  |  | 
Inputs/Spline/Points/Point.2/Interpolation | <spline/points/_1/interpolation | maxon::InternedId | Input | false | false | true |  |  | spline | Spline = spline, Cubic = cubic, Linear = linear
Inputs/Spline/Points/Point.2/Keep Visual Angle | <spline/points/_1/keepvisualangle | maxon::Bool | Input | false | false | false |  |  |  | 
Inputs/Spline/Points/Point.2/Lock Angle | <spline/points/_1/lockangle | maxon::Bool | Input | false | false | false |  |  |  | 
Inputs/Spline/Points/Point.2/Lock Length | <spline/points/_1/locklength | maxon::Bool | Input | false | false | false |  |  |  | 
Inputs/Spline/Points/Point.2/Lock X | <spline/points/_1/lockx | maxon::Bool | Input | false | false | false |  |  |  | 
Inputs/Spline/Points/Point.2/Lock Y | <spline/points/_1/locky | maxon::Bool | Input | false | false | false |  |  |  | 
Inputs/Spline/Points/Point.2/Position X | <spline/points/_1/positionx | maxon::Float | Input | false | false | false |  |  | 0 | 
Inputs/Spline/Points/Point.2/Position Y | <spline/points/_1/positiony | maxon::Float | Input | false | false | false |  |  | 0 | 
Inputs/Spline/Points/Point.2/Tangent Left | <spline/points/_1/tangentleft | maxon::Vector2d | Input | false | false | false |  |  |  | 
Inputs/Spline/Points/Point.2/Tangent Right | <spline/points/_1/tangentright | maxon::Vector2d | Input | false | false | false |  |  |  | 
Inputs/Spline/Tension | <spline/tension | maxon::Float | Input | false | false | false |  | 1 | 1 | 
Outputs/Left Tangents | >tangentsleftout | maxon::Array<maxon::Vector2d> | Output | false | false | false |  |  |  | 
Outputs/Points | >pointsout | maxon::Array<maxon::Vector2d> | Output | false | false | false |  |  |  | 
Outputs/Result | >result | maxon::Float | Output | false | false | false |  |  |  | 
Outputs/Right Tangents | >tangentsrightout | maxon::Array<maxon::Vector2d> | Output | false | false | false |  |  |  | 

