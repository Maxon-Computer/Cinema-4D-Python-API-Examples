# Node Template: Grid

- **Node Space ID:** `net.maxon.neutron.nodespace`
- **Template ID:** `com.rocketlasso.neutron.asset.primitive.spline.grid`
- **Template Name:** `Grid`

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
Node Category | net.maxon.node.base.category | maxon::InternedId | Attribute | false | false | true |  |  | functions | operators = operators, distributions = distributions, geometries = geometries, patterns = patterns, primitives = primitives, effectors = effectors, fields = fields, functions = functions, structures = structures, geomodifiers = geomodifiers, geogenerators = geogenerators
Preview/Node | net.maxon.node.base.nodepreviewimage | maxon::ImageBaseRef | Attribute | false | false | false |  |  |  | 
Grid/Cells | <Cj8LTDoHEhfsRKta6KMSO1 | maxon::Vector64 | Input | false | false | false | (0,0,0) |  | (10,0,10) | 
Grid/Gap | <IL1L_UbzBR3ncElYwQW3Fx | maxon::Float64 | Input | false | false | false |  |  | 0 | 
Grid/Mode | <ZnwjpNWqI98jkIsuD3SDEx | maxon::Int64 | Input | false | false | true |  |  | 1 | Per-Step = 0, Endpoint = 1
Grid/Return | <YSaLUytyOpmsohF9CVJABx | maxon::Int64 | Input | false | false | true |  |  |  | Full = 0, Inside = 1, Outside = 2
Grid/Reverse | <Ej$ELi7tLh9vrrK1IUhFVx | maxon::Bool | Input | false | false | false |  |  |  | 
Grid/Size | <D8Hu8podJ9RqblJiOKv3Bz | maxon::Vector64 | Input | false | false | false |  |  | (400,400,400) | 
Grid/Type | <Q6GK3BNmBNxoTQc44e4H1z | maxon::Int64 | Input | false | false | true |  |  | 2 | Segment = 1, Line = 2, Box = 0
Outputs/Geometry | >geometryout | maxon::GeometryObject | Output | false | false | false |  |  |  | 

