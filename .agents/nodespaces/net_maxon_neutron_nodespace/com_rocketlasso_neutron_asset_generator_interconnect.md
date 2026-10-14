# Node Template: Interconnect

- **Node Space ID:** `net.maxon.neutron.nodespace`
- **Template ID:** `com.rocketlasso.neutron.asset.generator.interconnect`
- **Template Name:** `Interconnect`

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
Inputs/Object Child/Color | <object/color | maxon::Color | Attribute | false | false | false |  |  | (1,1,1) | 
Inputs/Object Child/Geometry | <object/geometry | maxon::GeometryObject | Attribute | false | false | false |  |  |  | 
Inputs/Object Child/Global Matrix | <object/globalmatrix | maxon::Matrix | Attribute | false | false | false |  |  |  | 
Inputs/Object Child/Matrix | <object/matrix | maxon::Matrix | Attribute | false | false | false |  |  |  | 
Inputs/Object Child/Name | <object/objectname | maxon::String | Attribute | false | false | false |  |  |  | 
Node Category | net.maxon.node.base.category | maxon::InternedId | Attribute | false | false | true |  |  | primitives | distributions = distributions, operators = operators, geometries = geometries, patterns = patterns, primitives = primitives, effectors = effectors, fields = fields, functions = functions, structures = structures
Preview/Node | net.maxon.node.base.nodepreviewimage | maxon::ImageBaseRef | Attribute | false | false | false |  |  |  | 
Inputs/Global Capsule Matrix | <globalmatin | maxon::Matrix64 | Input | false | false | false |  |  |  | 
Inputs/Local Capsule Matrix | <localmatin | maxon::Matrix64 | Input | false | false | false |  |  |  | 
Inputs/Object Child | <object | net.maxon.neutron.portbundle.objectinput | Input | false | true | false |  |  |  | 
Inputs/Objects Children | <objectchildren | maxon::ArrayContainer<maxon::GeometryObject, maxon::Matrix64, maxon::Matrix64, maxon::ColorA64, maxon::String> | Input | false | false | false |  |  |  | 
Object/Break at Junctions | <bool3 | maxon::Bool | Input | false | false | false |  |  | false | 
Object/Closed | <bool4 | maxon::Bool | Input | false | false | false |  |  | false | 
Object/Continuous Connection | <bool7 | maxon::Bool | Input | false | false | false |  |  | true | 
Object/Count | <float | maxon::Float64 | Input | false | false | false |  |  | 1 | 
Object/Count | <integer | maxon::Int64 | Input | false | false | false |  |  | 10 | 
Object/Count Mismatch | <enum2 | maxon::Int64 | Input | false | false | true |  |  | 1 | Use Lowest = 0, Use Highest = 1
Object/Count Mode | <enum | maxon::Int64 | Input | false | false | true |  |  | 1 | Percentage = 1, Count = 0
Object/Direction | <enum6 | maxon::Int64 | Input | false | false | true |  |  |  | Normals = 0, Absolute Normals = 1, Auto = 2
Object/Explode Segments | <bool | maxon::Bool | Input | false | false | false |  |  | true | 
Object/Initial Shuffle | <float4 | maxon::Float64 | Input | false | false | false |  | 1 | 0 | 
Object/Interconnect | <enum4 | maxon::Int64 | Input | false | false | true |  |  |  | Points = 0, Polygons = 1
Object/Random Direction | <in@CBLxKUzDDV_hsWgdDmX1y6 | maxon::Float64 | Input | false | false | false |  | 1 | 0 | 
Object/Random Strength | <float5 | maxon::Float64 | Input | false | false | false |  |  | 0 | 
Object/Remove Duplicates | <bool1 | maxon::Bool | Input | false | false | false |  |  | false | 
Object/Reverse Sequence | <bool2 | maxon::Bool | Input | false | false | false |  |  | false | 
Object/Scale | <enum3 | maxon::Int64 | Input | false | false | true |  |  |  | Distance = 0, Absolute = 1
Object/Seed | <float2 | maxon::Float64 | Input | false | false | false |  |  | 12345 | 
Object/Selection | <string | maxon::String | Input | false | false | false |  |  | All | 
Object/Shuffle | <float3 | maxon::Float64 | Input | false | false | false |  |  | 1 | 
Object/Shuffle Indexes | <enum1 | maxon::Int64 | Input | false | false | true |  |  |  | None = 0, All Objects = 1, First Object = 2, Last Object = 3
Object/Step Indexes | <integer1 | maxon::Int64 | Input | false | false | false |  |  |  | 
Object/Surplus | <enum5 | maxon::Int64 | Input | false | false | true |  |  | 1 | Bundle Indexes = 0, Repeat Indexes = 1
Object/Tangents | <float1 | maxon::Float64 | Input | false | false | false |  |  | 0.5 | 
Object/Tangents | <in@VQy8afBdOtQjhiV7lsGM7n | maxon::Float64 | Input | false | false | false |  |  | 20 | 
Object/Tangents | <in@dX8icFmrIBfsRvRoz7fbf7 | maxon::Int64 | Input | false | false | true |  |  |  | None = 0, All Objects = 1, First Object = 2, Last Object = 3
Outputs/Geometry | >geometryout | maxon::GeometryObject | Output | false | false | false |  |  |  | 

