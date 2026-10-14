# Node Template: Profile

- **Node Space ID:** `net.maxon.neutron.nodespace`
- **Template ID:** `net.maxon.neutron.node.primitive.curve.profile`
- **Template Name:** `Profile`

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
Object/Height | net.maxon.command.modeling.primitive.curve.profile.height | maxon::Float | Attribute | false | false | false |  |  | 200 | 
Object/Plane | net.maxon.command.modeling.primitive.orientationplane.plane | maxon::InternedId | Attribute | false | false | true |  |  | xy | XY = xy, ZY = zy, XZ = xz
Object/Reverse | net.maxon.command.modeling.primitive.orientationplane.reverse | maxon::Bool | Attribute | false | false | false |  |  |  | 
Object/Type | net.maxon.command.modeling.primitive.curve.profile.type | maxon::InternedId | Attribute | false | false | true |  |  | h | H Shape = h, L Shape = l, T Shape = t, U Shape = u, Z Shape = z
Object/b | net.maxon.command.modeling.primitive.curve.profile.b | maxon::Float | Attribute | false | false | false |  |  | 100 | 
Object/s | net.maxon.command.modeling.primitive.curve.profile.s | maxon::Float | Attribute | false | false | false | 0 | 0 | 20 | 
Object/t | net.maxon.command.modeling.primitive.curve.profile.tee | maxon::Float | Attribute | false | false | false |  |  | 20 | 
Preview/Node | net.maxon.node.base.nodepreviewimage | maxon::ImageBaseRef | Attribute | false | false | false |  |  |  | 
Outputs/Geometry | >geometryout | maxon::GeometryObject | Output | false | false | false |  |  |  | 

