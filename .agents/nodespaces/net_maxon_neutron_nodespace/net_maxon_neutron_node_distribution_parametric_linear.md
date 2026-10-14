# Node Template: Linear

- **Node Space ID:** `net.maxon.neutron.nodespace`
- **Template ID:** `net.maxon.neutron.node.distribution.parametric.linear`
- **Template Name:** `Linear`

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
Node Category | net.maxon.node.base.category | maxon::InternedId | Attribute | false | false | true |  |  | distributions | distributions = distributions, operators = operators, geometries = geometries, patterns = patterns, primitives = primitives, effectors = effectors, fields = fields, functions = functions, structures = structures, geomodifiers = geomodifiers, geogenerators = geogenerators
Preview/Node | net.maxon.node.base.nodepreviewimage | maxon::ImageBaseRef | Attribute | false | false | false |  |  |  | 
Operator/Count | <countin | maxon::Int | Input | false | false | false | 0 |  | 20 | 
Operator/Position Step | <positionstepin | maxon::Vector | Input | false | false | false |  |  | (150,150,150) | 
Operator/Rotation Order | <rotationorderin | maxon::Int | Input | false | false | true |  |  |  | Global YXZ = 0, Global YZX = 1, Global XZY = 4, Global  ZYX = 2, Global  ZXY = 3, Global XYZ = 5, Local YXZ = 3, Local ZXY = 0, Local YZX = 4, Local XZY = 1, Local ZYX = 5, Local XYZ = 2
Operator/Rotation Step | <rotationstepin | maxon::Vector | Input | false | false | false | (-62.832,-62.832,-62.832) | (62.832,62.832,62.832) | (0,0,0) | 
Operator/Sample Offset | <offsetin | maxon::Int | Input | false | false | false | 0 |  | 0 | 
Operator/Scale Step | <scalestepin | maxon::Vector | Input | false | false | false | (-100,-100,-100) | (100,100,100) | (1,1,1) | 
Operator/Step Ratio | <stepsizein | maxon::Float | Input | false | false | false | -1000 | 1000 | 1 | 
Outputs/Distribution | >distdataout |  | Output | false | false | false |  |  |  | 

