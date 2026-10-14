# Node Template: Quad Remesh

- **Node Space ID:** `net.maxon.neutron.nodespace`
- **Template ID:** `net.maxon.neutron.modeling.quadremesh`
- **Template Name:** `Quad Remesh`

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
Inputs/Adaptive | net.maxon.command.modeling.quadremesh.adaptive | maxon::Bool | Attribute | false | false | false |  |  | false | 
Inputs/Adaptiveness | net.maxon.command.modeling.quadremesh.adaptiveness | maxon::Float | Attribute | false | false | false | 0 | 1 | 0.5 | 
Inputs/Density Map | net.maxon.command.modeling.quadremesh.densitymapname | maxon::String | Attribute | false | false | false |  |  |  | 
Inputs/Density Scale | net.maxon.command.modeling.quadremesh.densityscale | maxon::Float | Attribute | false | false | false | 0.25 | 4 | 2 | 
Inputs/Detect Hard Edges | net.maxon.command.modeling.quadremesh.detecthardedge | maxon::Bool | Attribute | false | false | false |  |  | true | 
Inputs/Polygon Scale | net.maxon.command.modeling.quadremesh.polygonscale | maxon::Float | Attribute | false | false | false | 0.01 | 100 | 1 | 
Inputs/Polygon Target Mode | net.maxon.command.modeling.quadremesh.absolutepolygoncount | maxon::InternedId | Attribute | false | false | true |  |  | meshdensity | Polygon Count = polygoncount, Mesh Density = meshdensity
Inputs/Symmetric X | net.maxon.command.modeling.quadremesh.symmetricx | maxon::Bool | Attribute | false | false | false |  |  |  | 
Inputs/Symmetric Y | net.maxon.command.modeling.quadremesh.symmetricy | maxon::Bool | Attribute | false | false | false |  |  |  | 
Inputs/Symmetric Z | net.maxon.command.modeling.quadremesh.symmetricz | maxon::Bool | Attribute | false | false | false |  |  |  | 
Inputs/Target Polygons | net.maxon.command.modeling.quadremesh.targetpolygons | maxon::Int32 | Attribute | false | false | false | 1 | 50000000 | 2000 | 
Inputs/Transfer Attributes | net.maxon.command.modeling.quadremesh.transferattributes | maxon::Bool | Attribute | false | false | false |  |  |  | 
Node Category | net.maxon.node.base.category | maxon::InternedId | Attribute | false | false | true |  |  | geomodifiers | distributions = distributions, operators = operators, geometries = geometries, patterns = patterns, primitives = primitives, effectors = effectors, fields = fields, functions = functions, structures = structures, geomodifiers = geomodifiers, geogenerators = geogenerators
Preview/Node | net.maxon.node.base.nodepreviewimage | maxon::ImageBaseRef | Attribute | false | false | false |  |  |  | 
Inputs/Geometry | <geometryin |  | Input | false | false | false |  |  |  | 
Outputs/Geometry | >geometryout |  | Output | false | false | false |  |  |  | 

