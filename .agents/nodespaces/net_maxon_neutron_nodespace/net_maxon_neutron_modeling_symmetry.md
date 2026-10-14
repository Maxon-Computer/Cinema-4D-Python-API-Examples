# Node Template: Symmetry

- **Node Space ID:** `net.maxon.neutron.nodespace`
- **Template ID:** `net.maxon.neutron.modeling.symmetry`
- **Template Name:** `Symmetry`

## Attributes

See `.agents/nodes.md` for an overview of Nodes API skills. Not all attributes and ports have a min, max, or default value. Enum values are listed in the form label = value, labe = value, label = value. I.e., if a user asks you to set the an enum attribute or port to "Foo" (citing an UI label), you must search for the label "Foo" in the enum values and use the corresponding value in your code. If a user asks you to set an attribute or port to a value that is not listed in the enum values, you must respond with an error message.

Name | ID  | Data Type | Parameter Type | isVariadic | isNested | isEnum | Min Value | Max Value | Default Value | Enum Values
---- | --- | --------- | -------------- | ---------- | -------- | ------ | --------- | --------- | ------------- | -----------
Axis | net.maxon.command.modeling.symmetrynodecommand.radialaxis | maxon::Id | Attribute | false | false | true |  |  | y | X = x, Y = y, Z = z
Basic/Asset Version | net.maxon.node.base.assetversion | maxon::Id | Attribute | false | false | true |  |  |  | Latest = latest
Basic/Color | net.maxon.node.base.color | maxon::Color | Attribute | false | false | false |  |  |  | 
Basic/Comment | net.maxon.node.base.comment | maxon::String | Attribute | false | false | false |  |  |  | 
Basic/Display Comment | net.maxon.node.base.displaycomment | maxon::Bool | Attribute | false | false | false |  |  |  | 
Basic/Name | net.maxon.node.base.name | maxon::String | Attribute | false | false | false |  |  |  | 
Basic/Ports Display | net.maxon.node.base.portdisplay | maxon::Id | Attribute | false | false | true |  |  | all | Collapsed = none, Connected = connected, Expanded = all
Basic/Show Preview | net.maxon.node.base.displaypreview | maxon::Bool | Attribute | false | false | false |  |  | true | 
Cut Along Plane | net.maxon.command.modeling.symmetrynodecommand.cutalongplane | maxon::Bool | Attribute | false | false | false |  |  | true | 
Dissolve | net.maxon.command.modeling.symmetrynodecommand.dissolve | maxon::Bool | Attribute | false | false | false |  |  |  | 
Filter Tags | net.maxon.node.base.filtertags | maxon::CString | Attribute | false | false | false |  |  |  | 
Mirror | net.maxon.command.modeling.symmetrynodecommand.radialmirror | maxon::Bool | Attribute | false | false | false |  |  | true | 
Node Category | net.maxon.node.base.category | maxon::InternedId | Attribute | false | false | true |  |  | geomodifiers | operators = operators, distributions = distributions, geometries = geometries, patterns = patterns, primitives = primitives, effectors = effectors, fields = fields, functions = functions, structures = structures, geomodifiers = geomodifiers, geogenerators = geogenerators
Position | net.maxon.command.modeling.symmetrynodecommand.position | maxon::Vector | Attribute | false | false | false |  |  |  | 
Preview/Node | net.maxon.node.base.nodepreviewimage | maxon::ImageBaseRef | Attribute | false | false | false |  |  |  | 
Remove Outside | net.maxon.command.modeling.symmetrynodecommand.removeoutside | maxon::Bool | Attribute | false | false | false |  |  | true | 
Rotation | net.maxon.command.modeling.symmetrynodecommand.rotation | maxon::Vector | Attribute | false | false | false | (-6.283,-6.283,-6.283) | (6.283,6.283,6.283) |  | 
Rotation Offset | net.maxon.command.modeling.symmetrynodecommand.radialrotationoffset | maxon::Float | Attribute | false | false | false | -6.283 | 6.283 |  | 
Slice Count | net.maxon.command.modeling.symmetrynodecommand.radialslicecount | maxon::Int | Attribute | false | false | false | 2 |  | 6 | 
Source Slice | net.maxon.command.modeling.symmetrynodecommand.radialsourceslice | maxon::Int | Attribute | false | false | false |  |  |  | 
Tolerance | net.maxon.command.modeling.symmetrynodecommand.tolerance | maxon::Float | Attribute | false | false | false |  |  | 1 | 
Type | net.maxon.command.modeling.symmetrynodecommand.type | maxon::Id | Attribute | false | false | true |  |  | planar | Planar = planar, Radial = radial
Weld Seam | net.maxon.command.modeling.symmetrynodecommand.weldseam | maxon::Bool | Attribute | false | false | false |  |  | true | 
X | net.maxon.command.modeling.symmetrynodecommand.planaraxisx | maxon::Id | Attribute | false | false | true |  |  | postoneg | Off = off, + to - = postoneg, - to + = negtopos
Y | net.maxon.command.modeling.symmetrynodecommand.planaraxisy | maxon::Id | Attribute | false | false | true |  |  | off | Off = off, + to - = postoneg, - to + = negtopos
Z | net.maxon.command.modeling.symmetrynodecommand.planaraxisz | maxon::Id | Attribute | false | false | true |  |  | off | Off = off, + to - = postoneg, - to + = negtopos
Inputs/Geometry | <geometryin |  | Input | false | false | false |  |  |  | 
Outputs/Geometry | >geometryout |  | Output | false | false | false |  |  |  | 

