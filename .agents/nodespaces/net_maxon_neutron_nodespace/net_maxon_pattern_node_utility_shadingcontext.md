# Node Template: Get Shading Context

- **Node Space ID:** `net.maxon.neutron.nodespace`
- **Template ID:** `net.maxon.pattern.node.utility.shadingcontext`
- **Template Name:** `Get Shading Context`

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
Node Category | net.maxon.node.base.category | maxon::InternedId | Attribute | false | false | true |  |  | patterns | operators = operators, distributions = distributions, geometries = geometries, patterns = patterns, primitives = primitives, effectors = effectors, fields = fields, functions = functions, structures = structures, geomodifiers = geomodifiers, geogenerators = geogenerators
Preview/Node | net.maxon.node.base.nodepreviewimage | maxon::ImageBaseRef | Attribute | false | false | false |  |  |  | 
Context/Context | <context | maxon::ShadingContext | Input | false | false | false |  |  |  | 
Outputs/Context | >result | maxon::ShadingContext | Output | false | false | false |  |  |  | 
Outputs/Geometry/Barycentric | >barycentric | maxon::Vector | Output | false | false | false |  |  |  | 
Outputs/Geometry/Bitangent | >bitangent | maxon::Vector | Output | false | false | false |  |  |  | 
Outputs/Geometry/Geometry Normal | >geometrynormal | maxon::Vector | Output | false | false | false |  |  |  | 
Outputs/Geometry/Original Normal | >originalnormal | maxon::Vector | Output | false | false | false |  |  |  | 
Outputs/Geometry/Original UVW | >originaluvw | maxon::Vector | Output | false | false | false |  |  |  | 
Outputs/Geometry/Phong Normal | >phongnormal | maxon::Vector | Output | false | false | false |  |  |  | 
Outputs/Geometry/Position | >sampleposition | maxon::Vector | Output | false | false | false |  |  |  | 
Outputs/Geometry/Ray Direction | >raydirection | maxon::Vector | Output | false | false | false |  |  |  | 
Outputs/Geometry/Ray Origin | >rayorigin | maxon::Vector | Output | false | false | false |  |  |  | 
Outputs/Geometry/Tangent | >tangent | maxon::Vector | Output | false | false | false |  |  |  | 
Outputs/Geometry/UVW | >uvw | maxon::Vector | Output | false | false | false |  |  |  | 
Outputs/Geometry/Vertex A | >vertexa | maxon::Vector | Output | false | false | false |  |  |  | 
Outputs/Geometry/Vertex B | >vertexb | maxon::Vector | Output | false | false | false |  |  |  | 
Outputs/Geometry/Vertex C | >vertexc | maxon::Vector | Output | false | false | false |  |  |  | 
Outputs/Geometry/Vertex D | >vertexd | maxon::Vector | Output | false | false | false |  |  |  | 
Outputs/Pixel/Pixel | >pixel | maxon::Vector2d | Output | false | false | false |  |  |  | 
Outputs/Pixel/Render Resolution | >resolution | maxon::Vector2d | Output | false | false | false |  |  |  | 
Outputs/Pixel/Screen Position | >screen | maxon::Vector2d | Output | false | false | false |  |  |  | 
Outputs/Pixel/Sub Pixel | >subpixel | maxon::Vector2d | Output | false | false | false |  |  |  | 

