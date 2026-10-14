# Node Template: Geometry Property Set

- **Node Space ID:** `net.maxon.neutron.nodespace`
- **Template ID:** `net.maxon.neutron.geometry.set_property`
- **Template Name:** `Geometry Property Set`

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
Node Category | net.maxon.node.base.category | maxon::InternedId | Attribute | false | false | true |  |  | geometries | operators = operators, distributions = distributions, geometries = geometries, patterns = patterns, primitives = primitives, effectors = effectors, fields = fields, functions = functions, structures = structures
Preview/Node | net.maxon.node.base.nodepreviewimage | maxon::ImageBaseRef | Attribute | false | false | false |  |  |  | 
Inputs/Array | <array |  | Input | false | false | false |  |  |  | 
Inputs/Array Mode | <arraymode | maxon::Bool | Input | false | false | false |  |  | true | 
Inputs/Domain | <domain |  | Input | false | false | false |  |  |  | 
Inputs/Fallback | <fallbackmodein | maxon::Id | Input | false | false | true |  |  | none | None = none, Default = default, Custom = custom
Inputs/Fallback Value | <fallbackvaluein | maxon::Generic | Input | false | false | false |  |  |  | 
Inputs/Geometry | <geometryin |  | Input | false | false | false |  |  |  | 
Inputs/Iteration | <iteration |  | Input | false | false | false |  |  |  | 
Inputs/Name | <accessorname | maxon::String | Input | false | false | false |  |  |  | 
Inputs/Optimize Topology | <rebuildtopology | maxon::Bool | Input | false | false | false |  |  |  | 
Inputs/Overwrite | <newdataset | maxon::Bool | Input | false | false | false |  |  | true | 
Inputs/Topology | <topology |  | Input | false | false | false |  |  |  | 
Inputs/Type | <accessortype | maxon::Id | Input | false | false | true |  |  | net.maxon.geometryabstraction.accessortypes.attributes.data3d | Positions = net.maxon.geometryabstraction.accessortypes.attributes.data3d, Normals = net.maxon.geometryabstraction.accessortypes.attributes.normal, UVs = net.maxon.geometryabstraction.accessortypes.attributes.uv, Color Alphas = net.maxon.geometryabstraction.accessortypes.attributes.colora, Weights = net.maxon.geometryabstraction.accessortypes.attributes.weight, Tangents = net.maxon.geometryabstraction.accessortypes.attributes.tangent3d, Corners = net.maxon.geometryabstraction.accessortypes.attributes.corner
Outputs/Geometry | >geometryout |  | Output | false | false | false |  |  |  | 

