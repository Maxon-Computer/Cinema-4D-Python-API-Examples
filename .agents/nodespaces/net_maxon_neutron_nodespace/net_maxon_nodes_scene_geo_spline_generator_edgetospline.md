# Node Template: Edge to Spline

- **Node Space ID:** `net.maxon.neutron.nodespace`
- **Template ID:** `net.maxon.nodes.scene.geo.spline.generator.edgetospline`
- **Template Name:** `Edge to Spline`

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
Inputs/Child Mesh/Color | <net.maxon.nodes.scene.geo.spline.generator.edgetospline.childmesh/color | maxon::Color | Attribute | false | false | false |  |  | (1,1,1) | 
Inputs/Child Mesh/Geometry | <net.maxon.nodes.scene.geo.spline.generator.edgetospline.childmesh/geometry | maxon::GeometryObject | Attribute | false | false | false |  |  |  | 
Inputs/Child Mesh/Global Matrix | <net.maxon.nodes.scene.geo.spline.generator.edgetospline.childmesh/globalmatrix | maxon::Matrix | Attribute | false | false | false |  |  |  | 
Inputs/Child Mesh/Matrix | <net.maxon.nodes.scene.geo.spline.generator.edgetospline.childmesh/matrix | maxon::Matrix | Attribute | false | false | false |  |  |  | 
Inputs/Child Mesh/Name | <net.maxon.nodes.scene.geo.spline.generator.edgetospline.childmesh/objectname | maxon::String | Attribute | false | false | false |  |  |  | 
Node Category | net.maxon.node.base.category | maxon::InternedId | Attribute | false | false | true |  |  | primitives | operators = operators, distributions = distributions, geometries = geometries, patterns = patterns, primitives = primitives, effectors = effectors, fields = fields, functions = functions, structures = structures
Preview/Node | net.maxon.node.base.nodepreviewimage | maxon::ImageBaseRef | Attribute | false | false | false |  |  |  | 
Inputs/Child Mesh | <net.maxon.nodes.scene.geo.spline.generator.edgetospline.childmesh | net.maxon.neutron.portbundle.objectinput | Input | false | true | false |  |  |  | 
Inputs/Global Capsule Matrix | <globalmatin | maxon::Matrix64 | Input | false | false | false |  |  |  | 
Inputs/Local Capsule Matrix | <localmatin | maxon::Matrix64 | Input | false | false | false |  |  |  | 
Object/Mode | <net.maxon.nodes.scene.geo.spline.generator.edgetospline.mode | maxon::Int64 | Input | false | false | true |  |  | 1 | Points = 0, Edges = 1, Polygons = 2
Object/Reverse | <net.maxon.nodes.scene.geo.spline.generator.edgetospline.reverse | maxon::Bool | Input | false | false | false |  |  | false | 
Object/Selection String | <net.maxon.nodes.scene.geo.spline.generator.edgetospline.selectionstring | maxon::String | Input | false | false | false |  |  | all | 
Outputs/Geometry | >geometryout | maxon::GeometryObject | Output | false | false | false |  |  |  | 

