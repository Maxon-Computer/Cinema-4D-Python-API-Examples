# Node Template: Circle

- **Node Space ID:** `net.maxon.neutron.nodespace`
- **Template ID:** `net.maxon.neutron.node.primitive.curve.circle`
- **Template Name:** `Circle`

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
Object/Ellipse | net.maxon.command.modeling.primitive.curve.circle.ellipse | maxon::Bool | Attribute | false | false | false |  |  |  | 
Object/Inner Radius | net.maxon.command.modeling.primitive.curve.circle.inner | maxon::Float | Attribute | false | false | false | 0 |  | 100 | 
Object/Plane | net.maxon.command.modeling.primitive.orientationplane.plane | maxon::InternedId | Attribute | false | false | true |  |  | xy | XY = xy, ZY = zy, XZ = xz
Object/Radius | net.maxon.command.modeling.primitive.curve.circle.radius | maxon::Float | Attribute | false | false | false | 0 |  | 200 | 
Object/Radius Y | net.maxon.command.modeling.primitive.curve.circle.radiusy | maxon::Float | Attribute | false | false | false | 0 |  | 200 | 
Object/Reverse | net.maxon.command.modeling.primitive.orientationplane.reverse | maxon::Bool | Attribute | false | false | false |  |  |  | 
Object/Ring | net.maxon.command.modeling.primitive.curve.circle.ring | maxon::Bool | Attribute | false | false | false |  |  |  | 
Preview/Node | net.maxon.node.base.nodepreviewimage | maxon::ImageBaseRef | Attribute | false | false | false |  |  |  | 
Outputs/Geometry | >geometryout | maxon::GeometryObject | Output | false | false | false |  |  |  | 

