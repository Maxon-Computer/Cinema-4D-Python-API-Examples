# Node Template: Scalar Ramp

- **Node Space ID:** `com.redshift3d.redshift4c4d.class.nodespace`
- **Template ID:** `com.redshift3d.redshift4c4d.nodes.core.rsscalarramp`
- **Template Name:** `Scalar Ramp`

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
Node Category | net.maxon.node.base.category | maxon::InternedId | Attribute | false | false | true |  |  | patterns | distributions = distributions, operators = operators, geometries = geometries, patterns = patterns, primitives = primitives, effectors = effectors, fields = fields, functions = functions, structures = structures, geomodifiers = geomodifiers, geogenerators = geogenerators
Preview/Node | net.maxon.node.base.nodepreviewimage | maxon::ImageBaseRef | Attribute | false | false | false |  |  |  | 
General/Input/Adjust/Exposure | <com.redshift3d.redshift4c4d.nodes.core.rsscalarramp.exposure | maxon::Float | Input | false | false | false |  |  | 0 | 
General/Input/Adjust/Invert | <com.redshift3d.redshift4c4d.nodes.core.rsscalarramp.inputinvert | maxon::Bool | Input | false | false | false |  |  | false | 
General/Input/Adjust/New Range Max | <com.redshift3d.redshift4c4d.nodes.core.rsscalarramp.new_max | maxon::Float | Input | false | false | false |  |  | 1 | 
General/Input/Adjust/New Range Min | <com.redshift3d.redshift4c4d.nodes.core.rsscalarramp.new_min | maxon::Float | Input | false | false | false |  |  | 0 | 
General/Input/Adjust/Noise Amount | <com.redshift3d.redshift4c4d.nodes.core.rsscalarramp.noise | maxon::Float | Input | false | false | false |  |  | 0 | 
General/Input/Adjust/Noise Frequency | <com.redshift3d.redshift4c4d.nodes.core.rsscalarramp.noisefreq | maxon::Float | Input | false | false | false |  |  | 1 | 
General/Input/Adjust/Old Range Max | <com.redshift3d.redshift4c4d.nodes.core.rsscalarramp.old_max | maxon::Float | Input | false | false | false |  |  | 1 | 
General/Input/Adjust/Old Range Min | <com.redshift3d.redshift4c4d.nodes.core.rsscalarramp.old_min | maxon::Float | Input | false | false | false |  |  | 0 | 
General/Input/Alt Input | <com.redshift3d.redshift4c4d.nodes.core.rsscalarramp.input | maxon::Float | Input | false | false | false |  |  | 0 | 
General/Input/Mapping | <com.redshift3d.redshift4c4d.nodes.core.rsscalarramp.inputmapping | maxon::Int | Input | false | false | true |  |  | 0 | Vertical = 0, Horizontal = 1, Diagonal = 2, Radial = 3, Circular = 4
General/Input/Source | <com.redshift3d.redshift4c4d.nodes.core.rsscalarramp.inputsource | maxon::Int | Input | false | false | true |  |  | 2 | UV Map = 0, Alt = 1, Auto = 2
General/Input/Texture Space | <com.redshift3d.redshift4c4d.nodes.core.rsscalarramp.tspace_id | maxon::String | Input | false | false | false |  |  |  | 
General/Input/UV Context | <com.redshift3d.redshift4c4d.nodes.core.rsscalarramp.uv_context | RSC4D::UVContext | Input | false | false | false |  |  |  | 
General/Ramp/Interpolation Type | <com.redshift3d.redshift4c4d.nodes.core.rsscalarramp.ramp_interp | maxon::Int | Input | false | false | true |  |  | 1 | Step = 0, Linear = 1, Smooth = 2, Spline = 3
General/Ramp/Ramp | <com.redshift3d.redshift4c4d.nodes.core.rsscalarramp.ramp | net.maxon.render.portbundle.spline | Input | false | true | false |  |  |  | 
General/Ramp/Ramp/Link End Positions | <com.redshift3d.redshift4c4d.nodes.core.rsscalarramp.ramp/linkendpositions | maxon::Bool | Input | false | false | false |  |  |  | 
General/Ramp/Ramp/Link End Tangents | <com.redshift3d.redshift4c4d.nodes.core.rsscalarramp.ramp/linkendtangents | maxon::Bool | Input | false | false | false |  |  |  | 
General/Ramp/Ramp/Max | <com.redshift3d.redshift4c4d.nodes.core.rsscalarramp.ramp/max | maxon::Vector2d | Input | false | false | false |  |  | (1,1) | 
General/Ramp/Ramp/Min | <com.redshift3d.redshift4c4d.nodes.core.rsscalarramp.ramp/min | maxon::Vector2d | Input | false | false | false |  |  |  | 
General/Ramp/Ramp/Points | <com.redshift3d.redshift4c4d.nodes.core.rsscalarramp.ramp/points | net.maxon.render.portbundle.splinepoint | Input | true | false | false |  |  |  | 
General/Ramp/Ramp/Points/Point.1 | <com.redshift3d.redshift4c4d.nodes.core.rsscalarramp.ramp/points/_0 | net.maxon.render.portbundle.splinepoint | Input | false | false | false |  |  |  | 
General/Ramp/Ramp/Points/Point.1/Break Tangent | <com.redshift3d.redshift4c4d.nodes.core.rsscalarramp.ramp/points/_0/breaktangent | maxon::Bool | Input | false | false | false |  |  |  | 
General/Ramp/Ramp/Points/Point.1/Interpolation | <com.redshift3d.redshift4c4d.nodes.core.rsscalarramp.ramp/points/_0/interpolation | maxon::InternedId | Input | false | false | true |  |  | spline | Spline = spline, Cubic = cubic, Linear = linear
General/Ramp/Ramp/Points/Point.1/Keep Visual Angle | <com.redshift3d.redshift4c4d.nodes.core.rsscalarramp.ramp/points/_0/keepvisualangle | maxon::Bool | Input | false | false | false |  |  |  | 
General/Ramp/Ramp/Points/Point.1/Lock Angle | <com.redshift3d.redshift4c4d.nodes.core.rsscalarramp.ramp/points/_0/lockangle | maxon::Bool | Input | false | false | false |  |  |  | 
General/Ramp/Ramp/Points/Point.1/Lock Length | <com.redshift3d.redshift4c4d.nodes.core.rsscalarramp.ramp/points/_0/locklength | maxon::Bool | Input | false | false | false |  |  |  | 
General/Ramp/Ramp/Points/Point.1/Lock X | <com.redshift3d.redshift4c4d.nodes.core.rsscalarramp.ramp/points/_0/lockx | maxon::Bool | Input | false | false | false |  |  |  | 
General/Ramp/Ramp/Points/Point.1/Lock Y | <com.redshift3d.redshift4c4d.nodes.core.rsscalarramp.ramp/points/_0/locky | maxon::Bool | Input | false | false | false |  |  |  | 
General/Ramp/Ramp/Points/Point.1/Position X | <com.redshift3d.redshift4c4d.nodes.core.rsscalarramp.ramp/points/_0/positionx | maxon::Float | Input | false | false | false |  |  | 0 | 
General/Ramp/Ramp/Points/Point.1/Position Y | <com.redshift3d.redshift4c4d.nodes.core.rsscalarramp.ramp/points/_0/positiony | maxon::Float | Input | false | false | false |  |  | 0 | 
General/Ramp/Ramp/Points/Point.1/Tangent Left | <com.redshift3d.redshift4c4d.nodes.core.rsscalarramp.ramp/points/_0/tangentleft | maxon::Vector2d | Input | false | false | false |  |  |  | 
General/Ramp/Ramp/Points/Point.1/Tangent Right | <com.redshift3d.redshift4c4d.nodes.core.rsscalarramp.ramp/points/_0/tangentright | maxon::Vector2d | Input | false | false | false |  |  |  | 
General/Ramp/Ramp/Points/Point.2 | <com.redshift3d.redshift4c4d.nodes.core.rsscalarramp.ramp/points/_1 | net.maxon.render.portbundle.splinepoint | Input | false | false | false |  |  |  | 
General/Ramp/Ramp/Points/Point.2/Break Tangent | <com.redshift3d.redshift4c4d.nodes.core.rsscalarramp.ramp/points/_1/breaktangent | maxon::Bool | Input | false | false | false |  |  |  | 
General/Ramp/Ramp/Points/Point.2/Interpolation | <com.redshift3d.redshift4c4d.nodes.core.rsscalarramp.ramp/points/_1/interpolation | maxon::InternedId | Input | false | false | true |  |  | spline | Spline = spline, Cubic = cubic, Linear = linear
General/Ramp/Ramp/Points/Point.2/Keep Visual Angle | <com.redshift3d.redshift4c4d.nodes.core.rsscalarramp.ramp/points/_1/keepvisualangle | maxon::Bool | Input | false | false | false |  |  |  | 
General/Ramp/Ramp/Points/Point.2/Lock Angle | <com.redshift3d.redshift4c4d.nodes.core.rsscalarramp.ramp/points/_1/lockangle | maxon::Bool | Input | false | false | false |  |  |  | 
General/Ramp/Ramp/Points/Point.2/Lock Length | <com.redshift3d.redshift4c4d.nodes.core.rsscalarramp.ramp/points/_1/locklength | maxon::Bool | Input | false | false | false |  |  |  | 
General/Ramp/Ramp/Points/Point.2/Lock X | <com.redshift3d.redshift4c4d.nodes.core.rsscalarramp.ramp/points/_1/lockx | maxon::Bool | Input | false | false | false |  |  |  | 
General/Ramp/Ramp/Points/Point.2/Lock Y | <com.redshift3d.redshift4c4d.nodes.core.rsscalarramp.ramp/points/_1/locky | maxon::Bool | Input | false | false | false |  |  |  | 
General/Ramp/Ramp/Points/Point.2/Position X | <com.redshift3d.redshift4c4d.nodes.core.rsscalarramp.ramp/points/_1/positionx | maxon::Float | Input | false | false | false |  |  | 0 | 
General/Ramp/Ramp/Points/Point.2/Position Y | <com.redshift3d.redshift4c4d.nodes.core.rsscalarramp.ramp/points/_1/positiony | maxon::Float | Input | false | false | false |  |  | 0 | 
General/Ramp/Ramp/Points/Point.2/Tangent Left | <com.redshift3d.redshift4c4d.nodes.core.rsscalarramp.ramp/points/_1/tangentleft | maxon::Vector2d | Input | false | false | false |  |  |  | 
General/Ramp/Ramp/Points/Point.2/Tangent Right | <com.redshift3d.redshift4c4d.nodes.core.rsscalarramp.ramp/points/_1/tangentright | maxon::Vector2d | Input | false | false | false |  |  |  | 
General/Ramp/Ramp/Tension | <com.redshift3d.redshift4c4d.nodes.core.rsscalarramp.ramp/tension | maxon::Float | Input | false | false | false |  | 1 | 1 | 
Outputs/out | >com.redshift3d.redshift4c4d.nodes.core.rsscalarramp.out | maxon::Float | Output | false | false | false |  |  | 0 | 

