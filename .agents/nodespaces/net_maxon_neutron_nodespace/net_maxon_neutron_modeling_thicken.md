# Node Template: Thicken

- **Node Space ID:** `net.maxon.neutron.nodespace`
- **Template ID:** `net.maxon.neutron.modeling.thicken`
- **Template Name:** `Thicken`

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
Clamp | net.maxon.command.modeling.thickennodecommand.thicknessclamp | maxon::Float | Attribute | false | false | false | 1 |  | 2.5 | 
End Cap | net.maxon.command.modeling.thickennodecommand.createendcap | maxon::Bool | Attribute | false | false | false |  |  | true | 
Filter Tags | net.maxon.node.base.filtertags | maxon::CString | Attribute | false | false | false |  |  |  | 
Mode | net.maxon.command.modeling.thickennodecommand.mode | maxon::Id | Attribute | false | false | true |  |  | basic | Basic = basic, Advanced = advanced
Node Category | net.maxon.node.base.category | maxon::InternedId | Attribute | false | false | true |  |  | geomodifiers | operators = operators, distributions = distributions, geometries = geometries, patterns = patterns, primitives = primitives, effectors = effectors, fields = fields, functions = functions, structures = structures, geomodifiers = geomodifiers, geogenerators = geogenerators
Optimize | net.maxon.command.modeling.thickennodecommand.optimize | maxon::Bool | Attribute | false | false | false |  |  | true | 
Perpendicular Boundary | net.maxon.command.modeling.thickennodecommand.perpendicularboundary | maxon::Float | Attribute | false | false | false |  | 3.142 |  | 
Position | net.maxon.command.modeling.thickennodecommand.position | maxon::Float | Attribute | false | false | false | -1 | 1 | 1 | 
Preserve Corners | net.maxon.command.modeling.thickennodecommand.preservecorners | maxon::Float | Attribute | false | false | false |  | 3.142 |  | 
Preview/Node | net.maxon.node.base.nodepreviewimage | maxon::ImageBaseRef | Attribute | false | false | false |  |  |  | 
Resolve Intersections | net.maxon.command.modeling.thickennodecommand.resolveintersections | maxon::Bool | Attribute | false | false | false |  |  | true | 
Shell | net.maxon.command.modeling.thickennodecommand.createshell | maxon::Bool | Attribute | false | false | false |  |  | true | 
Start Cap | net.maxon.command.modeling.thickennodecommand.createstartcap | maxon::Bool | Attribute | false | false | false |  |  | true | 
Subdivision | net.maxon.command.modeling.thickennodecommand.subdivision | maxon::Int | Attribute | false | false | false |  |  |  | 
Thickness | net.maxon.command.modeling.thickennodecommand.thickness | maxon::Float | Attribute | false | false | false |  |  | 10 | 
Inputs/Geometry | <geometryin |  | Input | false | false | false |  |  |  | 
Inputs/Selection | <selection |  | Input | false | false | false |  |  |  | 
Inputs/Selection String | <selectionstring | maxon::String | Input | false | false | false |  |  | default | 
Inputs/Type | <mode | maxon::InternedId | Input | false | false | true |  |  | polygons | Points = points, Edges = edges, Polygons = polygons
Outputs/Geometry | >geometryout |  | Output | false | false | false |  |  |  | 

