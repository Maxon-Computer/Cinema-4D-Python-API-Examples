# Node Template: Chamfer

- **Node Space ID:** `net.maxon.neutron.nodespace`
- **Template ID:** `net.maxon.neutron.modeling.chamfer`
- **Template Name:** `Chamfer`

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
Inputs/Basic/Ending | net.maxon.command.modeling.chamfer.ending | maxon::InternedId | Attribute | false | false | true |  |  | default | Default = default, Extend = extend, Inset = inset
Inputs/Basic/Limit | net.maxon.command.modeling.chamfer.limit | maxon::Bool | Attribute | false | false | false |  |  |  | 
Inputs/Basic/Max Angle | net.maxon.command.modeling.chamfer.maxangle | maxon::Float | Attribute | false | false | false |  | 3.142 | 0.698 | 
Inputs/Basic/Mitering | net.maxon.command.modeling.chamfer.mitering | maxon::InternedId | Attribute | false | false | true |  |  | default | Default = default, Uniform = uniform, Radial = radial, Patch = patch
Inputs/Basic/Mode | net.maxon.command.modeling.chamfer.mode | maxon::InternedId | Attribute | false | false | true |  |  | fixed | Fixed Distance = fixed, Radial = radial, Proportional = proportional
Inputs/Basic/Partial Rounding | net.maxon.command.modeling.chamfer.partialrounding | maxon::InternedId | Attribute | false | false | true |  |  | none | None = none, Full = full, Convex = convex
Inputs/Basic/Size | net.maxon.command.modeling.chamfer.size | maxon::Float | Attribute | false | false | false |  |  | 10 | 
Inputs/Basic/Subdivision | net.maxon.command.modeling.chamfer.subdivision | maxon::Int | Attribute | false | false | false |  |  |  | 
Inputs/Basic/Type | net.maxon.command.modeling.chamfer.type | maxon::InternedId | Attribute | false | false | true |  |  | chamfer | Chamfer = chamfer, Solid = solid
Inputs/Basic/Use Angle | net.maxon.command.modeling.chamfer.useangle | maxon::Bool | Attribute | false | false | false |  |  | true | 
Inputs/Shaping/Constant Cross Section | net.maxon.datatype.modeling.shaping.comstantsection | maxon::Bool | Attribute | false | false | false |  |  | true | 
Inputs/Shaping/Depth | net.maxon.datatype.modeling.shaping.absolutedepth | maxon::Float | Attribute | false | false | false |  |  | 10 | 
Inputs/Shaping/Depth | net.maxon.datatype.modeling.shaping.depth | maxon::Float | Attribute | false | false | false |  |  | 1 | 
Inputs/Shaping/Profile Plane | net.maxon.datatype.modeling.shaping.profileplane | maxon::InternedId | Attribute | false | false | true |  |  | xy | XY = xy, XZ = xz, ZY = zy
Inputs/Shaping/Shape | net.maxon.datatype.modeling.shaping.shape | maxon::InternedId | Attribute | false | false | true |  |  | round | Round = round, User = user, Profile = profile
Inputs/Shaping/Spline | net.maxon.datatype.modeling.shaping.spline | maxon::SplineMapper | Attribute | false | false | false |  |  | net.maxon.interface.splinemapper@0x000002B652C58E00 | 
Inputs/Shaping/Symmetry | net.maxon.datatype.modeling.shaping.symmetry | maxon::Bool | Attribute | false | false | false |  |  | true | 
Inputs/Shaping/Tension | net.maxon.datatype.modeling.shaping.tension | maxon::Float | Attribute | false | false | false |  |  | 1 | 
Inputs/Topology/Corner N-gons | net.maxon.datatype.modeling.topology.cornerngon | maxon::Bool | Attribute | false | false | false |  |  |  | 
Inputs/Topology/Rounding N-gons | net.maxon.datatype.modeling.topology.roundingngon | maxon::Bool | Attribute | false | false | false |  |  |  | 
Inputs/Topology/Shading Break Miters  | net.maxon.datatype.modeling.topology.mitershadingbreaks | maxon::Bool | Attribute | false | false | false |  |  |  | 
Inputs/Topology/Shading Break Rounding | net.maxon.datatype.modeling.topology.roundingshadingbreaks | maxon::Bool | Attribute | false | false | false |  |  |  | 
Node Category | net.maxon.node.base.category | maxon::InternedId | Attribute | false | false | true |  |  | geomodifiers | distributions = distributions, operators = operators, geometries = geometries, patterns = patterns, primitives = primitives, effectors = effectors, fields = fields, functions = functions, structures = structures, geomodifiers = geomodifiers, geogenerators = geogenerators
Preview/Node | net.maxon.node.base.nodepreviewimage | maxon::ImageBaseRef | Attribute | false | false | false |  |  |  | 
Inputs/Geometry | <geometryin |  | Input | false | false | false |  |  |  | 
Inputs/Selection | <selection |  | Input | false | false | false |  |  |  | 
Inputs/Selection String | <selectionstring | maxon::String | Input | false | false | false |  |  | default | 
Inputs/Type | <mode | maxon::InternedId | Input | false | false | true |  |  | polygons | Points = points, Edges = edges, Polygons = polygons
Outputs/Geometry | >geometryout |  | Output | false | false | false |  |  |  | 

