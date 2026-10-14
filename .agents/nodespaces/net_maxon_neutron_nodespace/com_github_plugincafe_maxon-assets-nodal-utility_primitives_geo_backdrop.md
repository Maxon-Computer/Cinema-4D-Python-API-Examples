# Node Template: Backdrop

- **Node Space ID:** `net.maxon.neutron.nodespace`
- **Template ID:** `com.github.plugincafe.maxon-assets-nodal-utility.primitives.geo.backdrop`
- **Template Name:** `Backdrop`

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
Inputs | net.maxon.node.base.group.inputs |  | Attribute | false | false | false |  |  |  | 
Node Category | net.maxon.node.base.category | maxon::InternedId | Attribute | false | false | true |  |  | primitives | distributions = distributions, operators = operators, geometries = geometries, patterns = patterns, primitives = primitives, effectors = effectors, fields = fields, functions = functions, structures = structures
Object | net.maxon.node.base.group.object |  | Attribute | false | false | false |  |  |  | 
Outputs | net.maxon.node.base.group.outputs |  | Attribute | false | false | false |  |  |  | 
Preview/Node | net.maxon.node.base.nodepreviewimage | maxon::ImageBaseRef | Attribute | false | false | false |  |  |  | 
Object/ | <attr_a23e643219984bfd86eb6d37ae323837 |  | Input | false | false | false |  |  |  | 
Object/Depth | <in@en7jlL5mFZ1vluQJCGwRpT | maxon::Float64 | Input | false | false | false |  | 1000 | 200 | 
Object/Drop | <in@aiUdUFLXNFdqGbS_1dXDjQ | maxon::Float64 | Input | false | false | false |  | 1000 | 0 | 
Object/Extension | <in@Vo1YsBFmDNUnOT5n9y22sW | maxon::Float64 | Input | false | false | false |  | 1000 | 100 | 
Object/Height | <in@czgj$HHpP9BkK_jcCClw5R | maxon::Float64 | Input | false | false | false |  | 1000 | 300 | 
Object/Overhang | <in@aq8aCxNJGhDpRalwSZHBfX | maxon::Float64 | Input | false | false | false |  | 1000 | 0 | 
Object/Rounding | <in@MSR3Ej51Mpvt3442HPWART | maxon::Float64 | Input | false | false | false |  |  | 50 | 
Object/Subdivision | <attr_40dfc807bc124f1489ec85a342dae0a1 |  | Input | false | false | false |  |  |  | 
Object/Subdivision/Angle | <in@L9XsRguMIFogP1REejmFCw | maxon::Float64 | Input | false | false | false |  | 1.571 | 0.087 | 
Object/Subdivision/Length | <attr_5ed31bd21bc94e5c984997c8e8fea840 | maxon::Float64 | Input | false | false | false |  |  | 20 | 
Object/Tilt | <in@K7e8fFG7FlgrtKICwni$HR | maxon::Float64 | Input | false | false | false |  |  |  | 
Object/UVs | <attr_a82f785614f84209a2c466f2c17210a2 |  | Input | false | false | false |  |  |  | 
Object/UVs/Fit Mode | <in@by3iKJqQD5WmvA8uIs1t20 | maxon::Int64 | Input | false | false | true |  |  | 2 | Fill = 0, Contain = 1, Cover = 2, Tile Size = 3
Object/UVs/Tile Size | <in@WeEiAK_PJZXn4QlsywE0GW | maxon::Float64 | Input | false | false | false |  |  | 300 | 
Object/Width | <attr_bd4d2a2b15c347b39e3e6264d09233b2 | maxon::Float64 | Input | false | false | false |  |  | 600 | 
Outputs/Geometry | >geometryout | maxon::GeometryObject | Output | false | false | false |  |  |  | 

