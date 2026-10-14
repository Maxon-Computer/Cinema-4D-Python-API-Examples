# Node Template: Lathe Line

- **Node Space ID:** `net.maxon.neutron.nodespace`
- **Template ID:** `net.maxon.neutron.modeling.latheline`
- **Template Name:** `Lathe Line`

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
Caps/Caps/Cap Type | net.maxon.datatype.modeling.caps.type | maxon::Id | Attribute | false | false | true |  |  | ngon | N-gons = ngon, Triangles = tri, Quadrangles = quad, Delaunay = delaunay, Regular Grid = regular
Caps/Caps/End Cap | net.maxon.datatype.modeling.caps.enableend | maxon::Bool | Attribute | false | false | false |  |  | true | 
Caps/Caps/Profile Main/Avoid Self Intersections | net.maxon.datatype.modeling.profileshaping.avoidselefintersection | maxon::Bool | Attribute | false | false | false |  |  | true | 
Caps/Caps/Profile Main/Break Phong Rounding | net.maxon.datatype.modeling.profileshaping.breakphong | maxon::Bool | Attribute | false | false | false |  |  | true | 
Caps/Caps/Profile Main/End Bevel/Curve | net.maxon.datatype.modeling.profileshaping.secondary.curve | maxon::SplineMapper | Attribute | false | false | false |  |  | net.maxon.interface.splinemapper@0x000002B652C56E80 | 
Caps/Caps/Profile Main/End Bevel/Extended Shape | net.maxon.datatype.modeling.profileshaping.secondary.extrudeshape | maxon::Bool | Attribute | false | false | false |  |  |  | 
Caps/Caps/Profile Main/End Bevel/Height | net.maxon.datatype.modeling.profileshaping.secondary.height | maxon::Float | Attribute | false | false | false | -3.142 | 3.142 | 0 | 
Caps/Caps/Profile Main/End Bevel/Max Shape Height | net.maxon.datatype.modeling.profileshaping.secondary.absolutedepth | maxon::Float | Attribute | false | false | false | -1 | 1 | 5 | 
Caps/Caps/Profile Main/End Bevel/Segments | net.maxon.datatype.modeling.profileshaping.secondary.segments | maxon::Int | Attribute | false | false | false | 1 |  | 1 | 
Caps/Caps/Profile Main/End Bevel/Shape | net.maxon.datatype.modeling.profileshaping.secondary.shape | maxon::Id | Attribute | false | false | true |  |  | round | Round = round, Solid = solid, Curve = curve, Step = step
Caps/Caps/Profile Main/End Bevel/Shape Depth | net.maxon.datatype.modeling.profileshaping.secondary.depth | maxon::Float | Attribute | false | false | false | -1 | 1 | 1 | 
Caps/Caps/Profile Main/End Bevel/Size | net.maxon.datatype.modeling.profileshaping.secondary.offset | maxon::Float | Attribute | false | false | false |  |  | 0 | 
Caps/Caps/Profile Main/End Bevel/Tension | net.maxon.datatype.modeling.profileshaping.secondary.tension | maxon::Float | Attribute | false | false | false | -1 | 1 | 1 | 
Caps/Caps/Profile Main/End Bevel/Use Absolute Value | net.maxon.datatype.modeling.profileshaping.secondary.absolutevalue | maxon::Bool | Attribute | false | false | false |  |  |  | 
Caps/Caps/Profile Main/Separated Bevel Control | net.maxon.datatype.modeling.profileshaping.separated | maxon::Bool | Attribute | false | false | false |  |  |  | 
Caps/Caps/Profile Main/Start Bevel/Curve | net.maxon.datatype.modeling.profileshaping.primary.curve | maxon::SplineMapper | Attribute | false | false | false |  |  | net.maxon.interface.splinemapper@0x000002B652C56380 | 
Caps/Caps/Profile Main/Start Bevel/Extended Shape | net.maxon.datatype.modeling.profileshaping.primary.extrudeshape | maxon::Bool | Attribute | false | false | false |  |  |  | 
Caps/Caps/Profile Main/Start Bevel/Height | net.maxon.datatype.modeling.profileshaping.primary.height | maxon::Float | Attribute | false | false | false | -3.142 | 3.142 | 0 | 
Caps/Caps/Profile Main/Start Bevel/Max Shape Height | net.maxon.datatype.modeling.profileshaping.primary.absolutedepth | maxon::Float | Attribute | false | false | false | -1 | 1 | 5 | 
Caps/Caps/Profile Main/Start Bevel/Segments | net.maxon.datatype.modeling.profileshaping.primary.segments | maxon::Int | Attribute | false | false | false | 1 |  | 1 | 
Caps/Caps/Profile Main/Start Bevel/Shape | net.maxon.datatype.modeling.profileshaping.primary.shape | maxon::Id | Attribute | false | false | true |  |  | round | Round = round, Solid = solid, Curve = curve, Step = step
Caps/Caps/Profile Main/Start Bevel/Shape Depth | net.maxon.datatype.modeling.profileshaping.primary.depth | maxon::Float | Attribute | false | false | false | -1 | 1 | 1 | 
Caps/Caps/Profile Main/Start Bevel/Size | net.maxon.datatype.modeling.profileshaping.primary.offset | maxon::Float | Attribute | false | false | false |  |  | 0 | 
Caps/Caps/Profile Main/Start Bevel/Tension | net.maxon.datatype.modeling.profileshaping.primary.tension | maxon::Float | Attribute | false | false | false | -1 | 1 | 1 | 
Caps/Caps/Profile Main/Start Bevel/Use Absolute Value | net.maxon.datatype.modeling.profileshaping.primary.absolutevalue | maxon::Bool | Attribute | false | false | false |  |  |  | 
Caps/Caps/Start Cap | net.maxon.datatype.modeling.caps.enablestart | maxon::Bool | Attribute | false | false | false |  |  | true | 
Caps/Caps/Tessellation/Gradient | net.maxon.datatype.modeling.caps.meshing.gradient | maxon::Float | Attribute | false | false | false |  |  | 0.1 | 
Caps/Caps/Tessellation/Max Size Factor | net.maxon.datatype.modeling.caps.meshing.sizefactor | maxon::Float | Attribute | false | false | false |  |  | 1 | 
Caps/Caps/Tessellation/Quad Dominant | net.maxon.datatype.modeling.caps.meshing.quads | maxon::Bool | Attribute | false | false | false |  |  |  | 
Caps/Caps/Tessellation/Size | net.maxon.datatype.modeling.caps.gridsize | maxon::Float | Attribute | false | false | false |  |  | 10 | 
Filter Tags | net.maxon.node.base.filtertags | maxon::CString | Attribute | false | false | false |  |  |  | 
Inputs/Angle | net.maxon.command.modeling.lathesplines.rotationangle | maxon::Float | Attribute | false | false | false |  |  | 6.283 | 
Inputs/Flip Normals | net.maxon.command.modeling.lathesplines.flipnormals | maxon::Bool | Attribute | false | false | false |  |  |  | 
Inputs/Movement | net.maxon.command.modeling.lathesplines.movement | maxon::Float | Attribute | false | false | false |  |  |  | 
Inputs/Scaling | net.maxon.command.modeling.lathesplines.scaling | maxon::Float | Attribute | false | false | false |  |  | 1 | 
Inputs/Subdivision | net.maxon.command.modeling.lathesplines.subdivision | maxon::Int | Attribute | false | false | false | 1 |  | 24 | 
Node Category | net.maxon.node.base.category | maxon::InternedId | Attribute | false | false | true |  |  | geogenerators | operators = operators, distributions = distributions, geometries = geometries, patterns = patterns, primitives = primitives, effectors = effectors, fields = fields, functions = functions, structures = structures, geomodifiers = geomodifiers, geogenerators = geogenerators
Preview/Node | net.maxon.node.base.nodepreviewimage | maxon::ImageBaseRef | Attribute | false | false | false |  |  |  | 
Inputs/Geometry | <geometryin |  | Input | false | false | false |  |  |  | 
Inputs/Matrix | <matrix | maxon::Matrix | Input | false | false | false |  |  |  | 
Outputs/Geometry | >geometryout |  | Output | false | false | false |  |  |  | 

