# Node Template: Material Op

- **Node Space ID:** `net.maxon.neutron.nodespace`
- **Template ID:** `net.maxon.nbo.op.material`
- **Template Name:** `Material Op`

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
Basic/Show Tag | net.maxon.neutron.showtag | maxon::Bool | Attribute | false | false | false |  |  | true | 
Filter Tags | net.maxon.node.base.filtertags | maxon::CString | Attribute | false | false | false |  |  |  | 
Node Category | net.maxon.node.base.category | maxon::InternedId | Attribute | false | false | true |  |  | functions | operators = operators, distributions = distributions, geometries = geometries, patterns = patterns, primitives = primitives, effectors = effectors, fields = fields, functions = functions, structures = structures, geomodifiers = geomodifiers, geogenerators = geogenerators
Preview/Node | net.maxon.node.base.nodepreviewimage | maxon::ImageBaseRef | Attribute | false | false | false |  |  |  | 
Basic/Bypass | <net.maxon.node.bypassable.bypass | maxon::Bool | Input | false | false | false |  |  |  | 
Coord/Position | <position | maxon::Vector | Input | false | false | false |  |  |  | 
Coord/Rotation | <rotation | maxon::Vector | Input | false | false | false |  |  |  | 
Coord/Size | <size | maxon::Vector | Input | false | false | false |  |  | (100,100,100) | 
Inputs/Op | <net.maxon.neutron.op.input | net.maxon.neutron.portbundle.object | Input | false | true | false |  |  |  | 
Inputs/Op/Material | <net.maxon.neutron.op.input/material | maxon::DataDictionary | Input | false | false | false |  |  |  | 
Operator/Length | <length | maxon::Vector2d | Input | false | false | false |  |  | (1,1) | 
Operator/Material | <material | maxon::nbo::ParametrizedMaterial | Input | false | false | false |  |  |  | 
Operator/Offset | <offset | maxon::Vector2d | Input | false | false | false |  |  |  | 
Operator/Projection | <projection | maxon::Int | Input | false | false | true |  |  |  | Spherical = 0, Cylindrical = 1, Flat = 2, Cubic = 3, Frontal = 4, UVW Mapping = 6, Spatial = 5, Shrink Wrapping = 7
Operator/Repetitions | <repetitions | maxon::Vector2d | Input | false | false | false |  |  |  | 
Operator/Seamless | <seamless | maxon::Bool | Input | false | false | false |  |  |  | 
Operator/Selection | <selection | maxon::String | Input | false | false | false |  |  |  | 
Operator/Side | <side | maxon::Int | Input | false | false | true |  |  |  | Both = 0, Front = 1, Back = 2
Operator/Tile | <tile | maxon::Bool | Input | false | false | false |  |  | true | 
Operator/Use UVW for Bump | <uvwforbump | maxon::Bool | Input | false | false | false |  |  | true | 
Outputs/Op/Material | >net.maxon.neutron.op.output/material | maxon::DataDictionary | Input | false | false | false |  |  |  | 
Outputs/Op | >net.maxon.neutron.op.output | net.maxon.neutron.portbundle.object | Output | false | true | false |  |  |  | 

