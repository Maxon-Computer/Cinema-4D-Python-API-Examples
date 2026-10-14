# Node Template: Points Modifier

- **Node Space ID:** `net.maxon.neutron.nodespace`
- **Template ID:** `net.maxon.neutron.geometry.pointsmodifier`
- **Template Name:** `Points Modifier`

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
Node Category | net.maxon.node.base.category | maxon::InternedId | Attribute | false | false | true |  |  | geometries | operators = operators, distributions = distributions, geometries = geometries, patterns = patterns, primitives = primitives, effectors = effectors, fields = fields, functions = functions, structures = structures, geomodifiers = geomodifiers, geogenerators = geogenerators
Preview/Node | net.maxon.node.base.nodepreviewimage | maxon::ImageBaseRef | Attribute | false | false | false |  |  |  | 
Properties | net.maxon.neutron.geometry.pointsmodifier.properties |  | Attribute | false | false | false |  |  |  | 
Geometry | <geometryin | maxon::GeometryObject | Input | false | false | false |  |  |  | 
Inner Scope | <innerdomain |  | Input | false | false | false |  |  |  | 
Point/Edges | <pointin_edge |  | Input | false | false | false |  |  |  | 
Point/Index | <pointin_index |  | Input | false | false | false |  |  |  | 
Point/Neighbors | <pointin_neighbors |  | Input | false | false | false |  |  |  | 
Point/Polygons | <pointin_polygon |  | Input | false | false | false |  |  |  | 
Point/Position | <pointin_position |  | Input | false | false | false |  |  |  | 
Point/Ratio | <pointin_ratio |  | Input | false | false | false |  |  |  | 
Point/Selected | <pointin_selected |  | Input | false | false | false |  |  |  | 
Properties/Colors/Colors | <colors | maxon::String | Input | true | true | false |  |  |  | 
Properties/Colors/Colors/Colors.1 | <colors/_0 | maxon::String | Input | false | false | false |  |  |  | 
Properties/Normals/Normals | <normals | maxon::String | Input | true | true | false |  |  |  | 
Properties/Normals/Normals/Normals.1 | <normals/_0 | maxon::String | Input | false | false | false |  |  |  | 
Properties/Weights/Weights | <weights | maxon::String | Input | true | true | false |  |  |  | 
Properties/Weights/Weights/Weights.1 | <weights/_0 | maxon::String | Input | false | false | false |  |  |  | 
Selection/Matching | <selectionstringin | maxon::String | Input | false | false | false |  |  | default | 
Selection/Only Iterate Selected | <iterateselected | maxon::Bool | Input | false | false | false |  |  |  | 
Selection/Select | <selectionmodein | maxon::InternedId | Input | false | false | false |  |  |  | 
Selection/Selection | <selectionin |  | Input | false | false | false |  |  |  | 
Geometry | >geometryout | maxon::GeometryObject | Output | false | false | false |  |  |  | 
Point Count | >pointcount |  | Output | false | false | false |  |  |  | 
Point/Position | >pointout_position |  | Output | false | false | false |  |  |  | 

