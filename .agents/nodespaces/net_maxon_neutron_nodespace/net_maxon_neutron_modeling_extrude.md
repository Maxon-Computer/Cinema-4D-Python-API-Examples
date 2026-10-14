# Node Template: Extrude

- **Node Space ID:** `net.maxon.neutron.nodespace`
- **Template ID:** `net.maxon.neutron.modeling.extrude`
- **Template Name:** `Extrude`

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
Inputs/Main Group/Create Ngons | net.maxon.command.modeling.extrude.base.createngons | maxon::Bool | Attribute | false | false | false |  |  |  | 
Inputs/Main Group/Edges/Rotation | net.maxon.command.modeling.extrude.base.rotation | maxon::Float | Attribute | false | false | false |  |  |  | 
Inputs/Main Group/Inset | net.maxon.command.modeling.extrude.base.inset | maxon::Float | Attribute | false | false | false |  |  | 100 | 
Inputs/Main Group/Inset Variation | net.maxon.command.modeling.extrude.base.insetvar | maxon::Float | Attribute | false | false | false |  |  | 0 | 
Inputs/Main Group/Offset | net.maxon.command.modeling.extrude.base.offset | maxon::Float | Attribute | false | false | false |  |  | 20 | 
Inputs/Main Group/Offset Variation | net.maxon.command.modeling.extrude.base.offsetvar | maxon::Float | Attribute | false | false | false |  |  | 0 | 
Inputs/Main Group/Per Step | net.maxon.command.modeling.extrude.base.perstep | maxon::Bool | Attribute | false | false | false |  |  |  | 
Inputs/Main Group/Polygons/Create Caps | net.maxon.command.modeling.extrude.createcaps | maxon::Bool | Attribute | false | false | false |  |  |  | 
Inputs/Main Group/Polygons/Max Angle | net.maxon.command.modeling.extrude.base.maxangle | maxon::Float | Attribute | false | false | false |  | 3.142 | 1.553 | 
Inputs/Main Group/Polygons/Use Islands | net.maxon.command.modeling.extrude.base.useislands | maxon::Bool | Attribute | false | false | false |  |  |  | 
Inputs/Main Group/Subdivision | net.maxon.command.modeling.extrude.base.subdivisions | maxon::Int | Attribute | false | false | false |  |  |  | 
Node Category | net.maxon.node.base.category | maxon::InternedId | Attribute | false | false | true |  |  | geomodifiers | operators = operators, distributions = distributions, geometries = geometries, patterns = patterns, primitives = primitives, effectors = effectors, fields = fields, functions = functions, structures = structures, geomodifiers = geomodifiers, geogenerators = geogenerators
Preview/Node | net.maxon.node.base.nodepreviewimage | maxon::ImageBaseRef | Attribute | false | false | false |  |  |  | 
Inputs/Geometry | <geometryin |  | Input | false | false | false |  |  |  | 
Inputs/Selection | <selection |  | Input | false | false | false |  |  |  | 
Inputs/Selection String | <selectionstring | maxon::String | Input | false | false | false |  |  | default | 
Inputs/Type | <mode | maxon::InternedId | Input | false | false | true |  |  | polygons | Points = points, Edges = edges, Polygons = polygons
Outputs/Geometry | >geometryout |  | Output | false | false | false |  |  |  | 

