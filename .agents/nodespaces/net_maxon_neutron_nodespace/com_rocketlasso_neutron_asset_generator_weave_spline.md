# Node Template: Weave Spline Generator

- **Node Space ID:** `net.maxon.neutron.nodespace`
- **Template ID:** `com.rocketlasso.neutron.asset.generator.weave.spline`
- **Template Name:** `Weave Spline Generator`

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
Inputs/Object Child/Geometry | <object/geometry | maxon::GeometryObject | Attribute | false | false | false |  |  |  | 
Inputs/Object Child/Global Matrix | <object/globalmatrix | maxon::Matrix | Attribute | false | false | false |  |  |  | 
Inputs/Object Child/Matrix | <object/matrix | maxon::Matrix | Attribute | false | false | false |  |  |  | 
Node Category | net.maxon.node.base.category | maxon::InternedId | Attribute | false | false | true |  |  | functions | distributions = distributions, operators = operators, geometries = geometries, patterns = patterns, primitives = primitives, effectors = effectors, fields = fields, functions = functions, structures = structures, geomodifiers = geomodifiers, geogenerators = geogenerators
Preview/Node | net.maxon.node.base.nodepreviewimage | maxon::ImageBaseRef | Attribute | false | false | false |  |  |  | 
Inputs/Global Capsule Matrix | <globalmatin | maxon::Matrix64 | Input | false | false | false |  |  |  | 
Inputs/Local Capsule Matrix | <localmatin | maxon::Matrix64 | Input | false | false | false |  |  |  | 
Inputs/Object Child | <object | net.maxon.neutron.portbundle.objectinput | Input | false | true | false |  |  |  | 
Object/Flip Weave Orientation | <bool1 | maxon::Bool | Input | false | false | false |  |  | true | 
Object/Inset Horizontal | <integer | maxon::Int64 | Input | false | false | false |  |  | 1 | 
Object/Inset Vertical | <integer1 | maxon::Int64 | Input | false | false | false |  |  | 1 | 
Object/Invert | <bool2 | maxon::Bool | Input | false | false | false |  |  | false | 
Object/Offset Step | <in@EYvkBDHzB9Nt93lGLDxMkQ | maxon::Int64 | Input | false | false | false | 0 |  | 0 | 
Object/Pattern Type | <enum | maxon::Int64 | Input | false | false | true |  |  |  | Plain Weave = 0, Twill Weave = 1, Hatch Weave = 2, Crowfoot Weave = 3, 5 Harness Weave = 5, 8 Harness Weave = 4
Object/Peak Horizontal | <in@MO05icuQFlqs1F3ts2RHVX | maxon::Float64 | Input | false | false | false |  |  | 1 | 
Object/Peak Vertical | <float1 | maxon::Float64 | Input | false | false | false |  |  | 1 | 
Object/Pinch Horizontal | <float2 | maxon::Float64 | Input | false | false | false |  |  | 0.5 | 
Object/Pinch Vertical | <in@Uj1B3Vx9AN6lYqxjgcmQxb | maxon::Float64 | Input | false | false | false |  |  | 0.5 | 
Object/Point Selection | <in@Pf5Bf2i9FlMndY9V8u2goV | maxon::String | Input | false | false | false |  |  |  | 
Object/Rail Offset | <float | maxon::Float64 | Input | false | false | false |  |  |  | 
Object/Remove Last Closed Point | <bool | maxon::Bool | Input | false | false | false |  |  | true | 
Object/Return Direction | <enum2 | maxon::Int64 | Input | false | false | true |  |  |  | Horizontal = 1, Vertical = 2, Both = 0
Object/Smooth Iteration | <integer3 | maxon::Int64 | Input | false | false | false |  |  | 0 | 
Object/Subdivide | <integer2 | maxon::Int64 | Input | false | false | false |  |  | 0 | 
Object/Surface Offset | <float3 | maxon::Float64 | Input | false | false | false |  |  |  | 
Randomize/Edge Fade | <float6 | maxon::Float64 | Input | false | false | false |  |  | 1 | 
Randomize/Noise Scale | <float5 | maxon::Float64 | Input | false | false | false |  |  | 20 | 
Randomize/Randomize | <float4 | maxon::Float64 | Input | false | false | false |  |  | 0 | 
Randomize/Relative Scale | <vector | maxon::Vector64 | Input | false | false | false |  |  | (0.5,1,0.5) | 
Randomize/Seed | <integer4 | maxon::Int64 | Input | false | false | false |  |  | 12345 | 
Randomize/Smooth Iterations | <integer5 | maxon::Int64 | Input | false | false | false |  |  | 1 | 
Outputs/Geometry | >geometryout | maxon::GeometryObject | Output | false | false | false |  |  |  | 

