# Node Template: Random Selection

- **Node Space ID:** `net.maxon.neutron.nodespace`
- **Template ID:** `net.maxon.neutron.asset.geo.randomselection`
- **Template Name:** `Random Selection`

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
Node Category | net.maxon.node.base.category | maxon::InternedId | Attribute | false | false | true |  |  | functions | operators = operators, distributions = distributions, geometries = geometries, patterns = patterns, primitives = primitives, effectors = effectors, fields = fields, functions = functions, structures = structures, geomodifiers = geomodifiers, geogenerators = geogenerators
Preview/Node | net.maxon.node.base.nodepreviewimage | maxon::ImageBaseRef | Attribute | false | false | false |  |  |  | 
Inputs/Chance | <inport@WWlpJ4tlH1kpF8$HYILQn4 | maxon::Float64 | Input | false | false | false |  | 1 | 0.5 | 
Inputs/Geometry | <geometryin | maxon::GeometryObject | Input | false | false | false |  |  |  | 
Inputs/Invert | <in@MUdl1BDiG9Uu0Vx$_2WEqQ | maxon::Bool | Input | false | false | false |  |  |  | 
Inputs/Mode | <inport@fjMMNrovDRakRxKIQrAHkj | maxon::Int64 | Input | false | false | true |  |  | 0 | Points = 1, Edges = 2, Polygons = 0
Inputs/Seed | <inport@W7ihSMVTPdzv4bNdTrr_8_ | maxon::Int64 | Input | false | false | false |  |  | 12345 | 
Inputs/Store Selection | <in@C8eFp8A3PpekVdMg1CCWhr | maxon::String | Input | false | false | false |  |  |  | 
Outputs/Edge Selection | >outport@aRRpjkYwFdFhAfAvFy74XM | maxon::Array<maxon::Tuple<maxon::Int32, maxon::Int32>> | Output | false | false | false |  |  |  | 
Outputs/Geometry | >geometryout | maxon::GeometryObject | Output | false | false | false |  |  |  | 
Outputs/Selection | >arrayout@OltDd3JfE9PtLrKWg9S9W9 | maxon::Array<maxon::Int64> | Output | false | false | false |  |  |  | 

