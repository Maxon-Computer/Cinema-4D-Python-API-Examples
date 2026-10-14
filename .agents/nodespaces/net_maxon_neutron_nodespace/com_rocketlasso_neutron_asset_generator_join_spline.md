# Node Template: Join Spline

- **Node Space ID:** `net.maxon.neutron.nodespace`
- **Template ID:** `com.rocketlasso.neutron.asset.generator.join.spline`
- **Template Name:** `Join Spline`

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
Inputs/Objects Children | <objectchildren | maxon::ArrayContainer<maxon::GeometryObject, maxon::Matrix64, maxon::Matrix64, maxon::ColorA64, maxon::String> | Input | false | false | false |  |  |  | 
Object/Chamfer | <bool5 | maxon::Bool | Input | false | false | false |  |  | false | 
Object/Chamfer Radius | <float1 | maxon::Float64 | Input | false | false | false |  |  | 5 | 
Object/Close Spline | <bool2 | maxon::Bool | Input | false | false | false |  |  | true | 
Object/Connect Either End | <bool4 | maxon::Bool | Input | false | false | false |  |  | true | 
Object/Explode Segments | <bool | maxon::Bool | Input | false | false | false |  |  | true | 
Object/Flat | <bool6 | maxon::Bool | Input | false | false | false |  |  | false | 
Object/Join | <enum1 | maxon::Int64 | Input | false | false | true |  |  |  | Next = 0, Closest = 1
Object/Max | <in@cuHEu_YkIx1oLZX9ryd0Au | maxon::Float64 | Input | false | false | false |  |  | 10 | 
Object/Min | <float | maxon::Float64 | Input | false | false | false |  |  |  | 
Object/Mode | <enum | maxon::Int64 | Input | false | false | true |  |  |  | Stack = 0, Bridge = 1
Object/Tangents | <float2 | maxon::Float64 | Input | false | false | false |  |  | 0 | 
Object/Weld | <bool1 | maxon::Bool | Input | false | false | false |  |  | true | 
Selections/Select Bridges | <in@I0IdQLnhDNwh0cLKmMA04f | maxon::Bool | Input | false | false | false |  |  | false | 
Selections/Select Welds | <bool3 | maxon::Bool | Input | false | false | false |  |  | false | 
Selections/Selection Bridges | <in@Zd8iUsOJO1fsym4wj8uefe | maxon::String | Input | false | false | false |  |  | Bridges | 
Selections/Selection Welds | <string | maxon::String | Input | false | false | false |  |  | Welds | 
Outputs/Geometry | >geometryout | maxon::GeometryObject | Output | false | false | false |  |  |  | 

