# Node Template: Set Color

- **Node Space ID:** `net.maxon.neutron.nodespace`
- **Template ID:** `net.maxon.neutron.asset.geo.setcolor`
- **Template Name:** `Set Color`

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
Inputs/Blend | <in@IngCvWGVBhipooT6TS9H0A | maxon::Float64 | Input | false | false | false |  | 1 | 1 | 
Inputs/Default Value | <in@PFlqX1W7JxHiO1lBr7sAX$ | maxon::ColorA64 | Input | false | false | false |  |  | (1,1,1,1) | 
Inputs/Geometry | <geometryin | maxon::GeometryObject | Input | false | false | false |  |  |  | 
Inputs/Global Capsule Matrix | <globalmatin | maxon::Matrix64 | Input | false | false | false |  |  |  | 
Inputs/Global Object Matrix | <objectmatrix | maxon::Matrix64 | Input | false | false | false |  |  |  | 
Inputs/Local Capsule Matrix | <localmatin | maxon::Matrix64 | Input | false | false | false |  |  |  | 
Inputs/Local Modifier Matrix | <modifiermatrix | maxon::Matrix64 | Input | false | false | false |  |  |  | 
Inputs/Local Object Matrix | <localobjectmatrix | maxon::Matrix64 | Input | false | false | false |  |  |  | 
Inputs/Mode | <in@aivcLqAgGRPs1vzjiKlyA4 | maxon::Int64 | Input | false | false | true |  |  | 2 | Value = 0, Random = 1, Position = 2
Inputs/Operation | <in@O4E$$VutDJsupycqpP9jcG | maxon::Int64 | Input | false | false | true |  |  |  | Subtract = 3, Replace = 0, Multiply = 1, Add = 2, Normal = 4
Inputs/Random Alpha | <attr@HS3sec9BMVvhmRM_TB$nEC | maxon::Bool | Input | false | false | false |  |  |  | 
Inputs/Seed | <in@NVBHAh9YEdWgkKnm3wEtv9 | maxon::Int64 | Input | false | false | false |  |  | 12345 | 
Inputs/Selection Port | <in@OoG5WFZjO9Av_$w5ncjfW8 | maxon::PairSelection | Input | false | false | false |  |  |  | 
Inputs/Selection Port | <in@VKG$tzYCIRymfbZMKzaqU5 | maxon::Array<maxon::Int64> | Input | false | false | false |  |  |  | 
Inputs/Selection String | <in@FkL5iKWdPlYtSyttx5yNR8 | maxon::String | Input | false | false | false |  |  | default | 
Inputs/Target | <in@KrWkVpssDBSgmaPGGIb_G4 | maxon::Int64 | Input | false | false | true |  |  | 1 | Points = 0, Vertexes = 1
Inputs/Type | <in@ds$rL08YPNYhvY3ogkHVo5 | maxon::Int64 | Input | false | false | true |  |  | 2 | Points = 0, Edges = 1, Polygons = 2
Inputs/Value | <in@dt$$furANNdqc8V$DucpU7 | maxon::ColorA64 | Input | false | false | false |  |  | (0,0.033,1,1) | 
Inputs/Vertex Color | <in@WzxkCEy9MV5iXX_VkLgg95 | maxon::String | Input | false | false | false |  |  | Vertex Color | 
Outputs/Geometry | >geometryout | maxon::GeometryObject | Output | false | false | false |  |  |  | 

