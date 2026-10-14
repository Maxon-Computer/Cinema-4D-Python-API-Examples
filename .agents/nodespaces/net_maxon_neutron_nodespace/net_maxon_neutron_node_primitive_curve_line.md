# Node Template: Line

- **Node Space ID:** `net.maxon.neutron.nodespace`
- **Template ID:** `net.maxon.neutron.node.primitive.curve.line`
- **Template Name:** `Line`

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
Inputs/Global Capsule Matrix | <globalmatin | maxon::Matrix64 | Input | false | false | false |  |  |  | 
Inputs/Local Capsule Matrix | <localmatin | maxon::Matrix64 | Input | false | false | false |  |  |  | 
Object/Align | <in@Rc1kRx8yINYhOTucYHw66e | maxon::Int64 | Input | false | false | true |  |  | 0 | Start = 0, Center = 1, End = 2
Object/Axis | <in@V6CK6409At$nVPdo$dVLSY | maxon::Int64 | Input | false | false | true |  |  |  | X = 0, Y = 1, Z = 2
Object/Direction | <vector2 | maxon::Vector64 | Input | false | false | false |  |  | (1,0,0) | 
Object/End | <vector1 | maxon::Vector64 | Input | false | false | false |  |  | (100,0,0) | 
Object/Length | <float | maxon::Float64 | Input | false | false | false |  |  | 100 | 
Object/Mode | <in@VZWfCo7CP9kugibJ_ULAOZ | maxon::Int64 | Input | false | false | true |  |  |  | Basic = 0, Ends = 2, Direction = 1, Step = 3
Object/Point Count | <integer | maxon::Int64 | Input | false | false | false |  |  | 2 | 
Object/Reverse | <bool | maxon::Bool | Input | false | false | false |  |  | false | 
Object/Start | <vector | maxon::Vector64 | Input | false | false | false |  |  | (0,0,0) | 
Object/Step | <vector3 | maxon::Vector64 | Input | false | false | false |  |  | (50,0,0) | 
Object/Step Count | <integer1 | maxon::Int64 | Input | false | false | false |  |  | 2 | 
Outputs/Point Positions | >out@LIbCZrAbAl7tP3YlZHeBSe | maxon::Array<maxon::Vector64> | Output | false | false | false |  |  |  | 
Outputs/Spline | >geometryout | maxon::GeometryObject | Output | false | false | false |  |  |  | 

