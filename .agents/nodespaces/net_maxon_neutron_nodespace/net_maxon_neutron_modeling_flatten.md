# Node Template: Flatten

- **Node Space ID:** `net.maxon.neutron.nodespace`
- **Template ID:** `net.maxon.neutron.modeling.flatten`
- **Template Name:** `Flatten`

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
Inputs/Individual Islands | net.maxon.command.modeling.flatten.individualislands | maxon::Bool | Attribute | false | false | false |  |  | true | 
Inputs/Mode | net.maxon.command.modeling.flatten.method | maxon::Int | Attribute | false | false | true |  |  | 1 | Best Fit = 1, Normal = 3, Axis = 4
Inputs/Normal | net.maxon.command.modeling.flatten.normal | maxon::Vector | Attribute | false | false | false |  |  | (0,1,0) | 
Inputs/Position | net.maxon.command.modeling.flatten.planeposition | maxon::Float | Attribute | false | false | false |  | 1 | 0.5 | 
Inputs/Position | net.maxon.command.modeling.flatten.position | maxon::Vector | Attribute | false | false | false |  |  |  | 
Inputs/Strength | net.maxon.command.modeling.flatten.weight | maxon::Float | Attribute | false | false | false |  | 1 | 1 | 
Inputs/Use Axis Position | net.maxon.command.modeling.flatten.useaxisposition | maxon::Bool | Attribute | false | false | false |  |  |  | 
Inputs/Use Outline Only | net.maxon.command.modeling.flatten.outlineonly | maxon::Bool | Attribute | false | false | false |  |  |  | 
Node Category | net.maxon.node.base.category | maxon::InternedId | Attribute | false | false | true |  |  | geomodifiers | distributions = distributions, operators = operators, geometries = geometries, patterns = patterns, primitives = primitives, effectors = effectors, fields = fields, functions = functions, structures = structures, geomodifiers = geomodifiers, geogenerators = geogenerators
Preview/Node | net.maxon.node.base.nodepreviewimage | maxon::ImageBaseRef | Attribute | false | false | false |  |  |  | 
Inputs/Geometry | <geometryin |  | Input | false | false | false |  |  |  | 
Inputs/Selection | <selection |  | Input | false | false | false |  |  |  | 
Inputs/Selection String | <selectionstring | maxon::String | Input | false | false | false |  |  | default | 
Inputs/Type | <mode | maxon::InternedId | Input | false | false | true |  |  | polygons | Points = points, Edges = edges, Polygons = polygons
Outputs/Geometry | >geometryout |  | Output | false | false | false |  |  |  | 

