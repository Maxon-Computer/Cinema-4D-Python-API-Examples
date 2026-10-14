# Node Template: Effector Op

- **Node Space ID:** `net.maxon.neutron.nodespace`
- **Template ID:** `net.maxon.neutron.op.effector`
- **Template Name:** `Effector Op`

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
Basic/Show Tag | net.maxon.neutron.showtag | maxon::Bool | Attribute | false | false | false |  |  |  | 
Filter Tags | net.maxon.node.base.filtertags | maxon::CString | Attribute | false | false | false |  |  |  | 
Inputs/Op/Matrix | <net.maxon.neutron.op.input/matrix | maxon::Matrix | Attribute | false | false | false |  |  |  | 
Node Category | net.maxon.node.base.category | maxon::InternedId | Attribute | false | false | true |  |  | functions | operators = operators, distributions = distributions, geometries = geometries, patterns = patterns, primitives = primitives, effectors = effectors, fields = fields, functions = functions, structures = structures, geomodifiers = geomodifiers, geogenerators = geogenerators
Operator/Field/Matrix | <effectorfield/matrix | maxon::Matrix | Attribute | false | false | false |  |  |  | 
Outputs/Op/Matrix | >net.maxon.neutron.op.output/matrix | maxon::Matrix | Attribute | false | false | false |  |  |  | 
Preview/Node | net.maxon.node.base.nodepreviewimage | maxon::ImageBaseRef | Attribute | false | false | false |  |  |  | 
Basic/Bypass | <net.maxon.node.bypassable.bypass | maxon::Bool | Input | false | false | false |  |  |  | 
Coord/Effector Matrix | <effectormatrix |  | Input | false | false | false |  |  |  | 
Inputs/Op | <net.maxon.neutron.op.input | net.maxon.neutron.portbundle.object | Input | false | true | false |  |  |  | 
Inputs/Op/Parent Matrix | <net.maxon.neutron.op.input/parentmatrix |  | Input | false | false | false |  |  |  | 
Operator/Apply To Children | <effectorchildren | maxon::Bool | Input | false | false | false |  |  | true | 
Operator/Effector Type | <effectortype | maxon::nodes::NodeOrTemplate | Input | false | false | true |  |  | (nullptr,net.maxon.neutron.effector.function/,(nullptr)) | node#net.maxon.neutron.effector.base = node#net.maxon.neutron.effector.base
Operator/Field | <effectorfield | net.maxon.neutron.portbundle.object | Input | false | true | false |  |  |  | 
Operator/Field Space | <effectorglobalfield | maxon::Bool | Input | false | false | false |  |  |  | 
Operator/Field/Parent Matrix | <effectorfield/parentmatrix |  | Input | false | false | false |  |  |  | 
Operator/Parameters | <parametersin |  | Input | false | false | false |  |  |  | 
Operator/Transform Mode | <effectormode |  | Input | false | false | false |  |  |  | 
Outputs/Op/Parent Matrix | >net.maxon.neutron.op.output/parentmatrix |  | Input | false | false | false |  |  |  | 
Outputs/Op | >net.maxon.neutron.op.output | net.maxon.neutron.portbundle.object | Output | false | true | false |  |  |  | 

