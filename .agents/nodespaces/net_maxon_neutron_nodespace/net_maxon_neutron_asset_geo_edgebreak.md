# Node Template: Edge Break

- **Node Space ID:** `net.maxon.neutron.nodespace`
- **Template ID:** `net.maxon.neutron.asset.geo.edgebreak`
- **Template Name:** `Edge Break`

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
Node Category | net.maxon.node.base.category | maxon::InternedId | Attribute | false | false | true |  |  | geomodifiers | distributions = distributions, operators = operators, geometries = geometries, patterns = patterns, primitives = primitives, effectors = effectors, fields = fields, functions = functions, structures = structures, geomodifiers = geomodifiers, geogenerators = geogenerators
Preview/Node | net.maxon.node.base.nodepreviewimage | maxon::ImageBaseRef | Attribute | false | false | false |  |  |  | 
Inputs/Break Angle | <inport@W_P2sYP8O1wrCBr9RUXTfN | maxon::Float64 | Input | false | false | false |  | 3.142 |  | 
Inputs/Geometry | <geometryin | maxon::GeometryObject | Input | false | false | false |  |  |  | 
Inputs/Outer Scope | <inport@TuwZQIZJJNsqkU7unpCkZK |  | Input | false | false | false |  |  |  | 
Inputs/Selection Output/Edges/Active Selection | <inport@dCo0eZ4NE5Dlqju$A1GCDM | maxon::Int64 | Input | false | false | true |  |  | 1 | Keep = 0, Break = 1
Inputs/Selection Output/Edges/Break | <inport@B_Y6mp$NM1mvYXogCEh1KI | maxon::String | Input | false | false | false |  |  |  | 
Inputs/Selection Output/Polygons/Active Selection | <inport@dVAm7weqChjv7iHIrmaFiN | maxon::Int64 | Input | false | false | true |  |  |  | Keep = 0, Break = 1
Inputs/Selection Output/Polygons/Break | <inport@TpsasVweKF6o_gihnXL8GK | maxon::String | Input | false | false | false |  |  |  | 
Outputs/Count | >outport@dcf6Yr09K1Et1cYh_Fdp_K | maxon::Int64 | Output | false | false | false |  |  |  | 
Outputs/Edge Selection | >outport@HIWzVkllPxYk0UF8o$f3dL | maxon::Array<maxon::Tuple<maxon::Int32, maxon::Int32>> | Output | false | false | false |  |  |  | 
Outputs/Geometry | >geometryout | maxon::GeometryObject | Output | false | false | false |  |  |  | 
Outputs/Polygon Selection | >outport@GmoLfa4MG5tsEHNAgKUqIN | maxon::Array<maxon::Int64> | Output | false | false | false |  |  |  | 

