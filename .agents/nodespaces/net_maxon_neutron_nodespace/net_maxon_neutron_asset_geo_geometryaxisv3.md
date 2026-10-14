# Node Template: Geometry Axis

- **Node Space ID:** `net.maxon.neutron.nodespace`
- **Template ID:** `net.maxon.neutron.asset.geo.geometryaxisv3`
- **Template Name:** `Geometry Axis`

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
Node Category | net.maxon.node.base.category | maxon::InternedId | Attribute | false | false | true |  |  | geomodifiers | operators = operators, distributions = distributions, geometries = geometries, patterns = patterns, primitives = primitives, effectors = effectors, fields = fields, functions = functions, structures = structures, geomodifiers = geomodifiers, geogenerators = geogenerators
Preview/Node | net.maxon.node.base.nodepreviewimage | maxon::ImageBaseRef | Attribute | false | false | false |  |  |  | 
Inputs/Affect X | <in@F7MjWexoPFrtx2YqtlKINq | maxon::Int64 | Input | false | false | true |  |  | 1 | 0 = 0, 1 = 1
Inputs/Affect Y | <in@MzDSs7J1FBNghzlL2VmjHq | maxon::Int64 | Input | false | false | true |  |  | 1 | 0 = 0, 1 = 1
Inputs/Affect Z | <in@SqO5ZSSAHZ0hyPeU$cZnjp | maxon::Int64 | Input | false | false | true |  |  | 1 | 0 = 0, 1 = 1
Inputs/Align X | <in@ZwY5Lp0pG1Wpo8KchyUq6p | maxon::Float64 | Input | false | false | false |  |  |  | 
Inputs/Align Y | <in@AORGkTlNC9sidD4DBLxbKt | maxon::Float64 | Input | false | false | false |  |  | -1 | 
Inputs/Align Z | <in@GzEMaPV8JxFntLatnXYvsq | maxon::Float64 | Input | false | false | false |  |  |  | 
Inputs/Center/Affect | <in@NMtTAuMUHN7ncKL7n7lbqv | maxon::Int64 | Input | false | false | true |  |  |  | All = 0, Selected = 1
Inputs/Geometry | <geometryin | maxon::GeometryObject | Input | false | false | false |  |  |  | 
Inputs/Global Capsule Matrix | <globalmatin | maxon::Matrix64 | Input | false | false | false |  |  |  | 
Inputs/Global Object Matrix | <objectmatrix | maxon::Matrix64 | Input | false | false | false |  |  |  | 
Inputs/Local Capsule Matrix | <localmatin | maxon::Matrix64 | Input | false | false | false |  |  |  | 
Inputs/Local Modifier Matrix | <modifiermatrix | maxon::Matrix64 | Input | false | false | false |  |  |  | 
Inputs/Local Object Matrix | <localobjectmatrix | maxon::Matrix64 | Input | false | false | false |  |  |  | 
Inputs/Offset | <in@flJKRSTsJB_gWcewzKMRuX | maxon::Vector64 | Input | false | false | false |  |  |  | 
Inputs/Reference | <in@G0ngyigHLxttkosmav8w5r | maxon::InternedId | Input | false | false | true |  |  | points | Points = points, Edges = edges, Polygons = polygons
Inputs/Selection String | <in@dD8jBUIzIlskvODZBqacKu | maxon::String | Input | false | false | false |  |  | all | 
Outputs/Geometry | >geometryout | maxon::GeometryObject | Output | false | false | false |  |  |  | 

