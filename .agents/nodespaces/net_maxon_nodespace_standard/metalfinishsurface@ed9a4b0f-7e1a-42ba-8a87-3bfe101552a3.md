# Node Template: Metal Finish Surface

- **Node Space ID:** `net.maxon.nodespace.standard`
- **Template ID:** `metalfinishsurface@ed9a4b0f-7e1a-42ba-8a87-3bfe101552a3`
- **Template Name:** `Metal Finish Surface`

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
Inputs/Anodizing | <inport@PfdIxEIWMpAlhmsQ2SN2NP | maxon::Float64 | Input | false | false | false |  | 1 | 0.05 | 
Inputs/Base Color | <inport@RvYYbeakCpyrD_MTg6iiyM | maxon::Color64 | Input | false | false | false |  |  | (0.4,0.419,0.448) | 
Inputs/Contrast | <inport@dVNh06AFDlsrd0um7uWCVV | maxon::Float64 | Input | false | false | false |  | 1 | 0 | 
Inputs/Dirt | <inport@e6e27qkMKVttppGdQETxYX | maxon::Float64 | Input | false | false | false | 0 | 1 | 0.5 | 
Inputs/Dirt Radius | <inport@chL9oIy5MlOh_Po5AlgUwT | maxon::Float64 | Input | false | false | false |  | 100000 | 150 | 
Inputs/Finish | <inport@bP_FqlBZEJ2tMNRzGfUfdP | maxon::Int64 | Input | false | false | true |  |  | 2 | Sand Blasted = 0, Cast = 1, Galvanized = 2, Corrugated = 3, Embossed Diamond = 4, Embossed Dots = 5, Embossed Grid = 6
Inputs/Scratches | <inport@HXsG5KXzOFOhblu7CvvMuR | maxon::Float64 | Input | false | false | false |  | 1 | 0.2 | 
Outputs/Color | >outport@a1REK6hrLtNsnkFYaPdylP | maxon::ColorA64 | Output | false | false | false |  |  |  | 

