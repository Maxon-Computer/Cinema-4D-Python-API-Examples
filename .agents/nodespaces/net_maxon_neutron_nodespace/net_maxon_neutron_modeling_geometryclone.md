# Node Template: Geometry Clone

- **Node Space ID:** `net.maxon.neutron.nodespace`
- **Template ID:** `net.maxon.neutron.modeling.geometryclone`
- **Template Name:** `Geometry Clone`

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
Inputs/Axis | net.maxon.command.modeling.clone.axis | maxon::InternedId | Attribute | false | false | true |  |  | y | X = x, Y = y, Z = z
Inputs/Clones | net.maxon.command.modeling.clone.clonecount | maxon::Int32 | Attribute | false | false | false | 0 | 100000 | 1 | 
Inputs/Holes | net.maxon.command.modeling.clone.holes | maxon::Float | Attribute | false | false | false |  | 1 |  | 
Inputs/Move Var. | net.maxon.command.modeling.clone.movevariance | maxon::Vector | Attribute | false | false | false |  |  |  | 
Inputs/Offset | net.maxon.command.modeling.clone.offset | maxon::Float | Attribute | false | false | false |  |  |  | 
Inputs/Rotation | net.maxon.command.modeling.clone.rotation | maxon::Float | Attribute | false | false | false |  |  |  | 
Inputs/Rotation Var | net.maxon.command.modeling.clone.rotationvariance | maxon::Vector | Attribute | false | false | false |  |  |  | 
Inputs/Scale | net.maxon.command.modeling.clone.scale | maxon::Float | Attribute | false | false | false |  | 1 | 1 | 
Inputs/Scale Var. | net.maxon.command.modeling.clone.scalevariance | maxon::Vector | Attribute | false | false | false |  |  | (1,1,1) | 
Inputs/Uniform Scale | net.maxon.command.modeling.clone.uniformscale | maxon::Bool | Attribute | false | false | false |  |  | true | 
Node Category | net.maxon.node.base.category | maxon::InternedId | Attribute | false | false | true |  |  | geomodifiers | distributions = distributions, operators = operators, geometries = geometries, patterns = patterns, primitives = primitives, effectors = effectors, fields = fields, functions = functions, structures = structures, geomodifiers = geomodifiers, geogenerators = geogenerators
Preview/Node | net.maxon.node.base.nodepreviewimage | maxon::ImageBaseRef | Attribute | false | false | false |  |  |  | 
Inputs/Geometry | <geometryin |  | Input | false | false | false |  |  |  | 
Inputs/Selection | <selection |  | Input | false | false | false |  |  |  | 
Inputs/Selection String | <selectionstring | maxon::String | Input | false | false | false |  |  | default | 
Inputs/Type | <mode | maxon::InternedId | Input | false | false | true |  |  | polygons | Points = points, Edges = edges, Polygons = polygons
Outputs/Geometry | >geometryout |  | Output | false | false | false |  |  |  | 

