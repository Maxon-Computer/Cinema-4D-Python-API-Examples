# Node Template: Square Star

- **Node Space ID:** `net.maxon.neutron.nodespace`
- **Template ID:** `com.github.plugincafe.maxon_assets_nodal_utility.primitive.curve.squarestar`
- **Template Name:** `Square Star`

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
Object/Plane | <inport@KyF0lC6tDhNtoee9j2ITqz | maxon::Int64 | Input | false | false | true |  |  |  | XY = 0, ZY = 1, XZ = 2
Object/Radius | <inport@V1gK20HtI5TsWz6YfMxvLt | maxon::Float64 | Input | false | false | false |  |  | 100 | 
Object/Reverse | <inport@V6_s2h53BFGr0wS2dpm4N0 | maxon::Bool | Input | false | false | false |  |  |  | 
Object/Rounding | <inport@X9c$aeaePVYgLNK3GVlPZz | maxon::Float64 | Input | false | false | false |  |  | 0 | 
Object/Sides | <inport@Ka_FigTCHBbqzGHgcYNphq | maxon::Int64 | Input | false | false | false |  |  | 6 | 
Object/Thickness | <inport@V5as3YUOM9ylLtGOvPBMso | maxon::Float64 | Input | false | false | false |  |  | 20 | 
Outputs/Geometry | >geometryout | maxon::GeometryObject | Output | false | false | false |  |  |  | 

