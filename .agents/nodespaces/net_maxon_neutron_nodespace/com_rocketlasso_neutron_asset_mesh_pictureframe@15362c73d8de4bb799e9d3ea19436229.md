# Node Template: Picture Frame

- **Node Space ID:** `net.maxon.neutron.nodespace`
- **Template ID:** `com.rocketlasso.neutron.asset.mesh.pictureframe@15362c73d8de4bb799e9d3ea19436229`
- **Template Name:** `Picture Frame`

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
Node Category | net.maxon.node.base.category | maxon::InternedId | Attribute | false | false | true |  |  | primitives | operators = operators, distributions = distributions, geometries = geometries, patterns = patterns, primitives = primitives, effectors = effectors, fields = fields, functions = functions, structures = structures
Preview/Node | net.maxon.node.base.nodepreviewimage | maxon::ImageBaseRef | Attribute | false | false | false |  |  |  | 
Object/Angle | <float2 | maxon::Float64 | Input | false | false | false |  | 1.571 | 0.436 | 
Object/Aspect Ratio | <vector2d | maxon::Vector2d64 | Input | false | false | false |  |  | (5,7) | 
Object/Bevel Frame | <float3 | maxon::Float64 | Input | false | false | false |  | 1 | 0 | 
Object/Bevel Frame | <in@b6GwYboLDJ1iRa2T1A9e_N | maxon::Float64 | Input | false | false | false |  |  | 0.1 | 
Object/Depth | <size_z | maxon::Float64 | Input | false | false | false |  |  | 2 | 
Object/Height | <size_x | maxon::Float64 | Input | false | false | false |  |  | 42 | 
Object/Height Front | <in@ULsNT$zFDF6v6SGh0C1cBO | maxon::Float64 | Input | false | false | false |  |  | 2 | 
Object/Height Rear | <in@WgYKYCa$ApNusUc9YOPsdM | maxon::Float64 | Input | false | false | false |  |  | 100 | 
Object/Measure From | <in@A8Up3DMILZynodisWwYHlk | maxon::Int64 | Input | false | false | true |  |  | 0 | Picture = 0, Frame = 1
Object/Orientation | <enum1 | maxon::Int64 | Input | false | false | true |  |  | 5 | -Z = 5, +X = 0, -X = 1, +Y = 2, -Y = 3, +Z = 4
Object/Pegs | <bool1 | maxon::Bool | Input | false | false | false |  |  | false | 
Object/Picture | <bool2 | maxon::Bool | Input | false | false | false |  |  | true | 
Object/Radius | <float4 | maxon::Float64 | Input | false | false | false |  |  | 1 | 
Object/Size | <enum3 | maxon::Int64 | Input | false | false | true |  |  | 0 | Width & Height = 2, Width = 0, Height = 1
Object/Size | <float | maxon::Float64 | Input | false | false | false |  |  | 0 | 
Object/Style | <enum | maxon::Int64 | Input | false | false | true |  |  | 5 | Simple = 0, Style 2 = 1, Style 3 = 2, Style 4 = 3, Style 5 = 5, Shadow Box = 4
Object/Thickness | <float1 | maxon::Float64 | Input | false | false | false |  |  | 3 | 
Object/Thickness | <in@Wp_F0z8mApGqVmDqkfuGDi | maxon::Float64 | Input | false | false | false |  |  | 0.1 | 
Object/Thickness | <in@YpygJWH1Pdjqt7uqWu0LPl | maxon::Float64 | Input | false | false | false |  |  | 0 | 
Object/UV Break | <float5 | maxon::Float64 | Input | false | false | false |  |  |  | 
Object/UV Mode | <enum2 | maxon::Int64 | Input | false | false | true |  |  |  | Fill = 0, Crop = 1
Object/Width | <size_y | maxon::Float64 | Input | false | false | false |  |  | 59.4 | 
Selections/Accent | <in@dxye6swqDdhtRat76x1q_$ | maxon::String | Input | false | false | false |  |  | Accent | 
Selections/Frame | <attr@K69mX7WtH9pu$TbGeBLusM | maxon::String | Input | false | false | false |  |  | Frame | 
Selections/Glass | <in@Lws99Z7uMZEg16OGplGYWg | maxon::String | Input | false | false | false |  |  | Glass | 
Selections/Matte | <attr@fE74HOaiIlKnc6zFdunVHK | maxon::String | Input | false | false | false |  |  | Matte | 
Selections/Picture | <string | maxon::String | Input | false | false | false |  |  | Picture | 
Outputs/Geometry | >geometryout | maxon::GeometryObject | Output | false | false | false |  |  |  | 

