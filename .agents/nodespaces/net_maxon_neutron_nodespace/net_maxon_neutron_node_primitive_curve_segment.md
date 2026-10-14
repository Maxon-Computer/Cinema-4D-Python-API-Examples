# Node Template: Segment

- **Node Space ID:** `net.maxon.neutron.nodespace`
- **Template ID:** `net.maxon.neutron.node.primitive.curve.segment`
- **Template Name:** `Segment`

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
Object/End Angle | net.maxon.command.modeling.primitive.curve.segment.endangle | maxon::Float | Attribute | false | false | false | 0 |  | 3.142 | 
Object/End Strength | net.maxon.command.modeling.primitive.curve.segment.endstrength | maxon::Float | Attribute | false | false | false |  |  | 50 | 
Object/Length | net.maxon.command.modeling.primitive.curve.segment.length | maxon::Float | Attribute | false | false | false |  |  | 100 | 
Object/Mode | net.maxon.command.modeling.primitive.curve.segment.curvetype | maxon::InternedId | Attribute | false | false | true |  |  | linear | Linear = linear, Bezier = bezier
Object/Offset | net.maxon.command.modeling.primitive.curve.segment.offset | maxon::Float | Attribute | false | false | false |  |  |  | 
Object/Plane | net.maxon.command.modeling.primitive.orientationplane.plane | maxon::InternedId | Attribute | false | false | true |  |  | xy | XY = xy, ZY = zy, XZ = xz
Object/Point Count | net.maxon.command.modeling.primitive.curve.segment.count | maxon::Int | Attribute | false | false | false | 2 |  | 2 | 
Object/Reverse | net.maxon.command.modeling.primitive.orientationplane.reverse | maxon::Bool | Attribute | false | false | false |  |  |  | 
Object/Start Angle | net.maxon.command.modeling.primitive.curve.segment.startangle | maxon::Float | Attribute | false | false | false | 0 | 0 | 0 | 
Object/Start Strength | net.maxon.command.modeling.primitive.curve.segment.startstrength | maxon::Float | Attribute | false | false | false |  |  | 50 | 
Preview/Node | net.maxon.node.base.nodepreviewimage | maxon::ImageBaseRef | Attribute | false | false | false |  |  |  | 
Outputs/Geometry | >geometryout | maxon::GeometryObject | Output | false | false | false |  |  |  | 

