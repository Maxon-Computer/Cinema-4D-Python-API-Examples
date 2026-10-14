# Node Template: Tube

- **Node Space ID:** `net.maxon.neutron.nodespace`
- **Template ID:** `net.maxon.neutron.node.primitive.tube`
- **Template Name:** `Tube`

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
Fillet/Enable | net.maxon.command.modeling.primitive.fillets.enable | maxon::Bool | Attribute | false | false | false |  |  |  | 
Fillet/Radius | net.maxon.command.modeling.primitive.fillets.radius | maxon::Float | Attribute | false | false | false |  |  | 5 | 
Fillet/Segments | net.maxon.command.modeling.primitive.fillets.segment | maxon::Int | Attribute | false | false | false |  |  | 5 | 
Filter Tags | net.maxon.node.base.filtertags | maxon::CString | Attribute | false | false | false |  |  |  | 
Node Category | net.maxon.node.base.category | maxon::InternedId | Attribute | false | false | true |  |  | primitives | operators = operators, distributions = distributions, geometries = geometries, patterns = patterns, primitives = primitives, effectors = effectors, fields = fields, functions = functions, structures = structures, geomodifiers = geomodifiers, geogenerators = geogenerators
Object/Cap Segments | net.maxon.command.modeling.primitive.tube.segment | maxon::Int | Attribute | false | false | false | 1 | 5000 | 1 | 
Object/Height | net.maxon.command.modeling.primitive.tube.height | maxon::Float | Attribute | false | false | false |  |  | 100 | 
Object/Height Segments | net.maxon.command.modeling.primitive.tube.heightsegment | maxon::Int | Attribute | false | false | false | 1 | 5000 | 1 | 
Object/Inner Radius | net.maxon.command.modeling.primitive.tube.innerradius | maxon::Float | Attribute | false | false | false |  |  | 25 | 
Object/Orientation | net.maxon.command.modeling.primitive.orientation.axis | maxon::Id | Attribute | false | false | true |  |  | ypos | -Z = zneg, +X = xpos, -X = xneg, +Y = ypos, -Y = yneg, +Z = zpos
Object/Outer Radius | net.maxon.command.modeling.primitive.tube.outerradius | maxon::Float | Attribute | false | false | false |  |  | 50 | 
Object/Rotation Segments | net.maxon.command.modeling.primitive.tube.rotationsegment | maxon::Int | Attribute | false | false | false | 3 | 5000 | 16 | 
Preview/Node | net.maxon.node.base.nodepreviewimage | maxon::ImageBaseRef | Attribute | false | false | false |  |  |  | 
Slice/From | net.maxon.command.modeling.primitive.slice.from | maxon::Float | Attribute | false | false | false |  |  |  | 
Slice/Regular Grid | net.maxon.command.modeling.primitive.slice.regulargrid | maxon::Bool | Attribute | false | false | false |  |  |  | 
Slice/Slice | net.maxon.command.modeling.primitive.slice.enable | maxon::Bool | Attribute | false | false | false |  |  | false | 
Slice/To | net.maxon.command.modeling.primitive.slice.to | maxon::Float | Attribute | false | false | false |  |  | 3.142 | 
Slice/Width | net.maxon.command.modeling.primitive.slice.gridsize | maxon::Float | Attribute | false | false | false | 0 |  | 10 | 
Outputs/Geometry | >geometryout | maxon::GeometryObject | Output | false | false | false |  |  |  | 

