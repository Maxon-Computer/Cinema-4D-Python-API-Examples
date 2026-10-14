# Node Template: Cone

- **Node Space ID:** `net.maxon.neutron.nodespace`
- **Template ID:** `net.maxon.neutron.node.primitive.cone`
- **Template Name:** `Cone`

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
Caps/Cap Segments | net.maxon.command.modeling.primitive.cone.cap.segment | maxon::Int | Attribute | false | false | false | 1 | 2000 | 1 | 
Caps/Caps | net.maxon.command.modeling.primitive.cone.caps.enable | maxon::Bool | Attribute | false | false | false |  |  | true | 
Caps/Fillet Segments | net.maxon.command.modeling.primitive.cone.cap.filletsegment | maxon::Int | Attribute | false | false | false | 1 | 2000 | 5 | 
Fillets/Bottom | net.maxon.command.modeling.primitive.cone.fillets.bottom | maxon::Bool | Attribute | false | false | false |  |  |  | 
Fillets/Height | net.maxon.command.modeling.primitive.cone.fillet.bottom.height | maxon::Float | Attribute | false | false | false |  |  | 50 | 
Fillets/Height | net.maxon.command.modeling.primitive.cone.fillet.top.height | maxon::Float | Attribute | false | false | false |  |  | 50 | 
Fillets/Radius | net.maxon.command.modeling.primitive.cone.fillet.bottom.radius | maxon::Float | Attribute | false | false | false |  |  | 5 | 
Fillets/Radius | net.maxon.command.modeling.primitive.cone.fillet.top.radius | maxon::Float | Attribute | false | false | false |  |  | 5 | 
Fillets/Top | net.maxon.command.modeling.primitive.cone.fillets.top | maxon::Bool | Attribute | false | false | false |  |  |  | 
Filter Tags | net.maxon.node.base.filtertags | maxon::CString | Attribute | false | false | false |  |  |  | 
Node Category | net.maxon.node.base.category | maxon::InternedId | Attribute | false | false | true |  |  | primitives | distributions = distributions, operators = operators, geometries = geometries, patterns = patterns, primitives = primitives, effectors = effectors, fields = fields, functions = functions, structures = structures, geomodifiers = geomodifiers, geogenerators = geogenerators
Object/Bottom Radius | net.maxon.command.modeling.primitive.cone.bottomradius | maxon::Float | Attribute | false | false | false |  |  | 50 | 
Object/Height | net.maxon.command.modeling.primitive.cone.height | maxon::Float | Attribute | false | false | false |  |  | 100 | 
Object/Height Segments | net.maxon.command.modeling.primitive.cone.heightsegment | maxon::Int | Attribute | false | false | false | 1 | 5000 | 1 | 
Object/Orientation | net.maxon.command.modeling.primitive.orientation.axis | maxon::Id | Attribute | false | false | true |  |  | ypos | +X = xpos, -Z = zneg, -X = xneg, +Y = ypos, -Y = yneg, +Z = zpos
Object/Rotation Segments | net.maxon.command.modeling.primitive.cone.rotationsegment | maxon::Int | Attribute | false | false | false | 3 | 5000 | 16 | 
Object/Top Radius | net.maxon.command.modeling.primitive.cone.topradius | maxon::Float | Attribute | false | false | false |  |  | 25 | 
Preview/Node | net.maxon.node.base.nodepreviewimage | maxon::ImageBaseRef | Attribute | false | false | false |  |  |  | 
Slice/From | net.maxon.command.modeling.primitive.slice.from | maxon::Float | Attribute | false | false | false |  |  |  | 
Slice/Regular Grid | net.maxon.command.modeling.primitive.slice.regulargrid | maxon::Bool | Attribute | false | false | false |  |  |  | 
Slice/Slice | net.maxon.command.modeling.primitive.slice.enable | maxon::Bool | Attribute | false | false | false |  |  | false | 
Slice/To | net.maxon.command.modeling.primitive.slice.to | maxon::Float | Attribute | false | false | false |  |  | 3.142 | 
Slice/Width | net.maxon.command.modeling.primitive.slice.gridsize | maxon::Float | Attribute | false | false | false | 0 |  | 10 | 
Outputs/Geometry | >geometryout | maxon::GeometryObject | Output | false | false | false |  |  |  | 

