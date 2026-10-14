# Node Template: Wave

- **Node Space ID:** `net.maxon.neutron.nodespace`
- **Template ID:** `com.rocketlasso.neutron.asset.fui.wavy`
- **Template Name:** `Wave`

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
Node Category | net.maxon.node.base.category | maxon::InternedId | Attribute | false | false | true |  |  | primitives | distributions = distributions, operators = operators, geometries = geometries, patterns = patterns, primitives = primitives, effectors = effectors, fields = fields, functions = functions, structures = structures
Preview/Node | net.maxon.node.base.nodepreviewimage | maxon::ImageBaseRef | Attribute | false | false | false |  |  |  | 
Object/ | <attr.8ff21a3f4de94cadac4810d0d38c8758 |  | Input | false | false | false |  |  |  | 
Object/ | <attr.dbda3ac6021f49c4b6692d4aea415983 |  | Input | false | false | false |  |  |  | 
Object/ | <attr.fd6d33cbe1214ab5847e2b59e62eb584 |  | Input | false | false | false |  |  |  | 
Object/Alignment | <attr.b3eabefeed37439db3c3c836bd1a556e |  | Input | false | false | false |  |  |  | 
Object/Custom | <attr.ca498420f7354e83b50fe3bfa6b9be23 |  | Input | false | false | false |  |  |  | 
Object/Custom/Spline | <inport@HQ90WnJtG1olpfm1Gv9No3 | net.maxon.render.portbundle.spline | Input | false | true | false |  |  |  | 
Object/Custom/Spline/Link End Positions | <inport@HQ90WnJtG1olpfm1Gv9No3/linkendpositions | maxon::Bool | Input | false | false | false |  |  |  | 
Object/Custom/Spline/Link End Tangents | <inport@HQ90WnJtG1olpfm1Gv9No3/linkendtangents | maxon::Bool | Input | false | false | false |  |  |  | 
Object/Custom/Spline/Max | <inport@HQ90WnJtG1olpfm1Gv9No3/max | maxon::Vector2d | Input | false | false | false |  |  | (1,1) | 
Object/Custom/Spline/Min | <inport@HQ90WnJtG1olpfm1Gv9No3/min | maxon::Vector2d | Input | false | false | false |  |  |  | 
Object/Custom/Spline/Points | <inport@HQ90WnJtG1olpfm1Gv9No3/points | net.maxon.render.portbundle.splinepoint | Input | true | false | false |  |  |  | 
Object/Custom/Spline/Points/Point.1 | <inport@HQ90WnJtG1olpfm1Gv9No3/points/_0 | net.maxon.render.portbundle.splinepoint | Input | false | false | false |  |  |  | 
Object/Custom/Spline/Points/Point.1/Break Tangent | <inport@HQ90WnJtG1olpfm1Gv9No3/points/_0/breaktangent | maxon::Bool | Input | false | false | false |  |  |  | 
Object/Custom/Spline/Points/Point.1/Interpolation | <inport@HQ90WnJtG1olpfm1Gv9No3/points/_0/interpolation | maxon::InternedId | Input | false | false | true |  |  | spline | Spline = spline, Cubic = cubic, Linear = linear
Object/Custom/Spline/Points/Point.1/Keep Visual Angle | <inport@HQ90WnJtG1olpfm1Gv9No3/points/_0/keepvisualangle | maxon::Bool | Input | false | false | false |  |  |  | 
Object/Custom/Spline/Points/Point.1/Lock Angle | <inport@HQ90WnJtG1olpfm1Gv9No3/points/_0/lockangle | maxon::Bool | Input | false | false | false |  |  |  | 
Object/Custom/Spline/Points/Point.1/Lock Length | <inport@HQ90WnJtG1olpfm1Gv9No3/points/_0/locklength | maxon::Bool | Input | false | false | false |  |  |  | 
Object/Custom/Spline/Points/Point.1/Lock X | <inport@HQ90WnJtG1olpfm1Gv9No3/points/_0/lockx | maxon::Bool | Input | false | false | false |  |  |  | 
Object/Custom/Spline/Points/Point.1/Lock Y | <inport@HQ90WnJtG1olpfm1Gv9No3/points/_0/locky | maxon::Bool | Input | false | false | false |  |  |  | 
Object/Custom/Spline/Points/Point.1/Position X | <inport@HQ90WnJtG1olpfm1Gv9No3/points/_0/positionx | maxon::Float | Input | false | false | false |  |  | 0 | 
Object/Custom/Spline/Points/Point.1/Position Y | <inport@HQ90WnJtG1olpfm1Gv9No3/points/_0/positiony | maxon::Float | Input | false | false | false |  |  | 0 | 
Object/Custom/Spline/Points/Point.1/Tangent Left | <inport@HQ90WnJtG1olpfm1Gv9No3/points/_0/tangentleft | maxon::Vector2d | Input | false | false | false |  |  |  | 
Object/Custom/Spline/Points/Point.1/Tangent Right | <inport@HQ90WnJtG1olpfm1Gv9No3/points/_0/tangentright | maxon::Vector2d | Input | false | false | false |  |  |  | 
Object/Custom/Spline/Points/Point.2 | <inport@HQ90WnJtG1olpfm1Gv9No3/points/_1 | net.maxon.render.portbundle.splinepoint | Input | false | false | false |  |  |  | 
Object/Custom/Spline/Points/Point.2/Break Tangent | <inport@HQ90WnJtG1olpfm1Gv9No3/points/_1/breaktangent | maxon::Bool | Input | false | false | false |  |  |  | 
Object/Custom/Spline/Points/Point.2/Interpolation | <inport@HQ90WnJtG1olpfm1Gv9No3/points/_1/interpolation | maxon::InternedId | Input | false | false | true |  |  | spline | Spline = spline, Cubic = cubic, Linear = linear
Object/Custom/Spline/Points/Point.2/Keep Visual Angle | <inport@HQ90WnJtG1olpfm1Gv9No3/points/_1/keepvisualangle | maxon::Bool | Input | false | false | false |  |  |  | 
Object/Custom/Spline/Points/Point.2/Lock Angle | <inport@HQ90WnJtG1olpfm1Gv9No3/points/_1/lockangle | maxon::Bool | Input | false | false | false |  |  |  | 
Object/Custom/Spline/Points/Point.2/Lock Length | <inport@HQ90WnJtG1olpfm1Gv9No3/points/_1/locklength | maxon::Bool | Input | false | false | false |  |  |  | 
Object/Custom/Spline/Points/Point.2/Lock X | <inport@HQ90WnJtG1olpfm1Gv9No3/points/_1/lockx | maxon::Bool | Input | false | false | false |  |  |  | 
Object/Custom/Spline/Points/Point.2/Lock Y | <inport@HQ90WnJtG1olpfm1Gv9No3/points/_1/locky | maxon::Bool | Input | false | false | false |  |  |  | 
Object/Custom/Spline/Points/Point.2/Position X | <inport@HQ90WnJtG1olpfm1Gv9No3/points/_1/positionx | maxon::Float | Input | false | false | false |  |  | 0 | 
Object/Custom/Spline/Points/Point.2/Position Y | <inport@HQ90WnJtG1olpfm1Gv9No3/points/_1/positiony | maxon::Float | Input | false | false | false |  |  | 0 | 
Object/Custom/Spline/Points/Point.2/Tangent Left | <inport@HQ90WnJtG1olpfm1Gv9No3/points/_1/tangentleft | maxon::Vector2d | Input | false | false | false |  |  |  | 
Object/Custom/Spline/Points/Point.2/Tangent Right | <inport@HQ90WnJtG1olpfm1Gv9No3/points/_1/tangentright | maxon::Vector2d | Input | false | false | false |  |  |  | 
Object/Custom/Spline/Tension | <inport@HQ90WnJtG1olpfm1Gv9No3/tension | maxon::Float | Input | false | false | false |  | 1 | 1 | 
Object/Fade | <inport@ML6$Rk7SC1xpThsNeEvBow | net.maxon.render.portbundle.spline | Input | false | true | false |  |  |  | 
Object/Fade Offset | <attr.3e5aea4f286d475c80903bda3d5faa3e | maxon::Float64 | Input | false | false | false |  |  |  | 
Object/Fade/Link End Positions | <inport@ML6$Rk7SC1xpThsNeEvBow/linkendpositions | maxon::Bool | Input | false | false | false |  |  |  | 
Object/Fade/Link End Tangents | <inport@ML6$Rk7SC1xpThsNeEvBow/linkendtangents | maxon::Bool | Input | false | false | false |  |  |  | 
Object/Fade/Max | <inport@ML6$Rk7SC1xpThsNeEvBow/max | maxon::Vector2d | Input | false | false | false |  |  | (1,1) | 
Object/Fade/Min | <inport@ML6$Rk7SC1xpThsNeEvBow/min | maxon::Vector2d | Input | false | false | false |  |  |  | 
Object/Fade/Points | <inport@ML6$Rk7SC1xpThsNeEvBow/points | net.maxon.render.portbundle.splinepoint | Input | true | false | false |  |  |  | 
Object/Fade/Points/Point.1 | <inport@ML6$Rk7SC1xpThsNeEvBow/points/_0 | net.maxon.render.portbundle.splinepoint | Input | false | false | false |  |  |  | 
Object/Fade/Points/Point.1/Break Tangent | <inport@ML6$Rk7SC1xpThsNeEvBow/points/_0/breaktangent | maxon::Bool | Input | false | false | false |  |  |  | 
Object/Fade/Points/Point.1/Interpolation | <inport@ML6$Rk7SC1xpThsNeEvBow/points/_0/interpolation | maxon::InternedId | Input | false | false | true |  |  | spline | Spline = spline, Cubic = cubic, Linear = linear
Object/Fade/Points/Point.1/Keep Visual Angle | <inport@ML6$Rk7SC1xpThsNeEvBow/points/_0/keepvisualangle | maxon::Bool | Input | false | false | false |  |  |  | 
Object/Fade/Points/Point.1/Lock Angle | <inport@ML6$Rk7SC1xpThsNeEvBow/points/_0/lockangle | maxon::Bool | Input | false | false | false |  |  |  | 
Object/Fade/Points/Point.1/Lock Length | <inport@ML6$Rk7SC1xpThsNeEvBow/points/_0/locklength | maxon::Bool | Input | false | false | false |  |  |  | 
Object/Fade/Points/Point.1/Lock X | <inport@ML6$Rk7SC1xpThsNeEvBow/points/_0/lockx | maxon::Bool | Input | false | false | false |  |  |  | 
Object/Fade/Points/Point.1/Lock Y | <inport@ML6$Rk7SC1xpThsNeEvBow/points/_0/locky | maxon::Bool | Input | false | false | false |  |  |  | 
Object/Fade/Points/Point.1/Position X | <inport@ML6$Rk7SC1xpThsNeEvBow/points/_0/positionx | maxon::Float | Input | false | false | false |  |  | 0 | 
Object/Fade/Points/Point.1/Position Y | <inport@ML6$Rk7SC1xpThsNeEvBow/points/_0/positiony | maxon::Float | Input | false | false | false |  |  | 0 | 
Object/Fade/Points/Point.1/Tangent Left | <inport@ML6$Rk7SC1xpThsNeEvBow/points/_0/tangentleft | maxon::Vector2d | Input | false | false | false |  |  |  | 
Object/Fade/Points/Point.1/Tangent Right | <inport@ML6$Rk7SC1xpThsNeEvBow/points/_0/tangentright | maxon::Vector2d | Input | false | false | false |  |  |  | 
Object/Fade/Points/Point.2 | <inport@ML6$Rk7SC1xpThsNeEvBow/points/_1 | net.maxon.render.portbundle.splinepoint | Input | false | false | false |  |  |  | 
Object/Fade/Points/Point.2/Break Tangent | <inport@ML6$Rk7SC1xpThsNeEvBow/points/_1/breaktangent | maxon::Bool | Input | false | false | false |  |  |  | 
Object/Fade/Points/Point.2/Interpolation | <inport@ML6$Rk7SC1xpThsNeEvBow/points/_1/interpolation | maxon::InternedId | Input | false | false | true |  |  | spline | Spline = spline, Cubic = cubic, Linear = linear
Object/Fade/Points/Point.2/Keep Visual Angle | <inport@ML6$Rk7SC1xpThsNeEvBow/points/_1/keepvisualangle | maxon::Bool | Input | false | false | false |  |  |  | 
Object/Fade/Points/Point.2/Lock Angle | <inport@ML6$Rk7SC1xpThsNeEvBow/points/_1/lockangle | maxon::Bool | Input | false | false | false |  |  |  | 
Object/Fade/Points/Point.2/Lock Length | <inport@ML6$Rk7SC1xpThsNeEvBow/points/_1/locklength | maxon::Bool | Input | false | false | false |  |  |  | 
Object/Fade/Points/Point.2/Lock X | <inport@ML6$Rk7SC1xpThsNeEvBow/points/_1/lockx | maxon::Bool | Input | false | false | false |  |  |  | 
Object/Fade/Points/Point.2/Lock Y | <inport@ML6$Rk7SC1xpThsNeEvBow/points/_1/locky | maxon::Bool | Input | false | false | false |  |  |  | 
Object/Fade/Points/Point.2/Position X | <inport@ML6$Rk7SC1xpThsNeEvBow/points/_1/positionx | maxon::Float | Input | false | false | false |  |  | 0 | 
Object/Fade/Points/Point.2/Position Y | <inport@ML6$Rk7SC1xpThsNeEvBow/points/_1/positiony | maxon::Float | Input | false | false | false |  |  | 0 | 
Object/Fade/Points/Point.2/Tangent Left | <inport@ML6$Rk7SC1xpThsNeEvBow/points/_1/tangentleft | maxon::Vector2d | Input | false | false | false |  |  |  | 
Object/Fade/Points/Point.2/Tangent Right | <inport@ML6$Rk7SC1xpThsNeEvBow/points/_1/tangentright | maxon::Vector2d | Input | false | false | false |  |  |  | 
Object/Fade/Tension | <inport@ML6$Rk7SC1xpThsNeEvBow/tension | maxon::Float | Input | false | false | false |  | 1 | 1 | 
Object/Frequency | <attr.a7fef17170824daa93f57123037a3172 | maxon::Float64 | Input | false | false | false |  |  | 8 | 
Object/Height | <attr.2b62db01e28e4f968a472cd1ddff55ca | maxon::Float64 | Input | false | false | false |  |  | 50 | 
Object/Horizontal | <attr.b1d588774a48480ca7eaba58d71a06d1 | maxon::Float64 | Input | false | false | false |  |  |  | 
Object/Noise | <attr.a1657b31f17546acb32a8e1f705c262f |  | Input | false | false | false |  |  |  | 
Object/Noise/Noise | <attr.8a144a37a82e4ea1b3ed0124b3485203 |  | Input | false | false | false |  |  |  | 
Object/Noise/Noise Scale | <attr.492a1886040f4f519a20530287bc14fe | maxon::Float64 | Input | false | false | false |  |  | 1 | 
Object/Noise/Noise Type | <inport@TphvDWTjC5ErxgfkGlVRBz | maxon::Id | Input | false | false | true |  |  | net.maxon.render.rendernoiseclass.perlin | registry#net.maxon.render.registry.rendernoiseclasses = registry#net.maxon.render.registry.rendernoiseclasses
Object/Noise/Points | <attr.6ef1e057ea7348c0bbc7931314a370d9 | maxon::Int64 | Input | false | false | false | 2 | 9999999 | 100 | 
Object/Noise/Seed | <attr.04e1f867035644c882a7a6f368768e65 | maxon::Int64 | Input | false | false | false |  |  | 12345 | 
Object/Offset | <attr.2b09935b47f84df7ac31e520a6bd990d |  | Input | false | false | false |  |  |  | 
Object/Offset | <attr.73a86af271214893b9b9606edd00a884 |  | Input | false | false | false |  |  |  | 
Object/Offset/Offset | <attr.2fa0db8681814d0eaad1a61020c6f87b | maxon::Float64 | Input | false | false | false |  |  |  | 
Object/Offset/Period(F)     | <attr.0807e2599d78460485db75e4e8da90ec | maxon::Float64 | Input | false | false | false |  |  |  | 
Object/Plane | <attr.63ba8d316a5c496dbff31c00a97ccc3a | maxon::Int64 | Input | false | false | true |  |  | 0 | XY = 0, ZY = 1, XZ = 2
Object/Points | <attr.c32fe399efe04fc3910e4210b8b73015 | maxon::Int64 | Input | false | false | false | 2 | 9999999 | 24 | 
Object/Random | <attr.adbe12fd234044aea2d850ad14c112dd |  | Input | false | false | false |  |  |  | 
Object/Random/Points       | <attr.f203341e4fb64ffb8c18e59a6a486bff | maxon::Int64 | Input | false | false | false | 2 | 9999999 | 24 | 
Object/Random/Random | <attr.ec79ef40644a48e8878546d9736f9bb4 |  | Input | false | false | false |  |  |  | 
Object/Random/Seed | <attr.d1c0a8c35120489695d69aacd016741d | maxon::Int64 | Input | false | false | false |  |  | 12345 | 
Object/Ratio | <attr.0ebe57a45dcd484c8d8a2abef1013526 | maxon::Float64 | Input | false | false | false |  |  | 0.75 | 
Object/Ratio | <attr.a33abd25ddb84b6b940887878d505407 | maxon::Float64 | Input | false | false | false |  |  | 0.5 | 
Object/Ratio 2 | <attr.b14208cbc19b4769ad5995cd04e0cc30 | maxon::Float64 | Input | false | false | false |  |  | 0.5 | 
Object/RoundingGroup | <attr.50ee537b83824ce696a2b517c223ede3 |  | Input | false | false | false |  |  |  | 
Object/RoundingGroup/ | <attr.ede9494ce63c44478201ff77b8be73e3 |  | Input | false | false | false |  |  |  | 
Object/RoundingGroup/Radius | <attr.543026249db34bcf83e9027e92f71c32 | maxon::Float64 | Input | false | false | false |  |  | 10 | 
Object/RoundingGroup/Rounding | <attr.e99be792d5494cf8a6dfb4993417a62d | maxon::Bool | Input | false | false | false |  |  |  | 
Object/Vertical | <attr.9840754372454e639c974be8ccb0b507 | maxon::Float64 | Input | false | false | false |  |  |  | 
Object/Wave | <attr.f6132e913d28452db8d12e25bc7cd7f8 | maxon::Int64 | Input | false | false | true |  |  |  | Sin = 0, Cos = 1, Triangle = 2, Bounce = 6, SawTooth = 3, Square = 4, Crank = 5, Noise = 7, Random = 8, Custom = 9
Object/Width | <attr.44db82f8bf1b436180215d9292fe6293 | maxon::Float64 | Input | false | false | false |  |  | 400 | 
Outputs/Geometry | >geometryout | maxon::GeometryObject | Output | false | false | false |  |  |  | 

