# Node Template: Commandline Text

- **Node Space ID:** `net.maxon.neutron.nodespace`
- **Template ID:** `net.maxon.neutron.asset.op.commandlinetext`
- **Template Name:** `Commandline Text`

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
Inputs/Object/Matrix | <objectinput/matrix | maxon::Matrix | Attribute | false | false | false |  |  |  | 
Node Category | net.maxon.node.base.category | maxon::InternedId | Attribute | false | false | true |  |  | functions | distributions = distributions, operators = operators, geometries = geometries, patterns = patterns, primitives = primitives, effectors = effectors, fields = fields, functions = functions, structures = structures, geomodifiers = geomodifiers, geogenerators = geogenerators
Outputs/Object/Matrix | >matrixout/matrix | maxon::Matrix | Attribute | false | false | false |  |  |  | 
Outputs/Op/Geometry | >net.maxon.neutron.op.output/geometry | maxon::GeometryObject | Attribute | false | false | false |  |  |  | 
Outputs/Op/Matrix | >net.maxon.neutron.op.output/matrix | maxon::Matrix | Attribute | false | false | false |  |  |  | 
Preview/Node | net.maxon.node.base.nodepreviewimage | maxon::ImageBaseRef | Attribute | false | false | false |  |  |  | 
Basic/Bypass | <net.maxon.node.bypassable.bypass | maxon::Bool | Input | false | false | false |  |  |  | 
Basic/Children | <net.maxon.neutron.op.objectbase.children | net.maxon.neutron.portbundle.object | Input | true | false | false |  |  |  | 
Coord/Matrix | <net.maxon.neutron.op.objectbase.matrix | maxon::Matrix64 | Input | false | false | false |  |  |  | 
Inputs/Object | <objectinput | net.maxon.neutron.portbundle.object | Input | false | true | false |  |  |  | 
Inputs/Object/Parent Matrix | <objectinput/parentmatrix |  | Input | false | false | false |  |  |  | 
Inputs/Object/Position | <objectinput/translation |  | Input | false | false | false |  |  |  | 
Inputs/Object/Rotation/Scale/Shear | <objectinput/sqrmatrix |  | Input | false | false | false |  |  |  | 
Inputs/Object/Scope | <objectinput/domain |  | Input | false | false | false |  |  |  | 
Inputs/Op | <net.maxon.neutron.op.input | net.maxon.neutron.portbundle.object | Input | false | true | false |  |  |  | 
Inputs/Op/Position | <net.maxon.neutron.op.input/translation |  | Input | false | false | false |  |  |  | 
Inputs/Op/Rotation/Scale/Shear | <net.maxon.neutron.op.input/sqrmatrix |  | Input | false | false | false |  |  |  | 
Inputs/Op/Scope | <net.maxon.neutron.op.input/domain |  | Input | false | false | false |  |  |  | 
Object/Align | <inport@J1gGcMp0PFMiiNk6JJe8hM | maxon::InternedId | Input | false | false | true |  |  | left | Left = left, Middle = middle, Right = right
Object/Argument | <inport@LxTMeQddOdTi44qBckzrIL | maxon::String | Input | false | false | false |  |  | my_data | 
Object/Default | <inport@aRNZXftnCFNiHPblgkGjiJ | maxon::String | Input | false | false | false |  |  | <empty> | 
Object/Font | <inport@d$6KFti7BBJkzznTHQsUAI | maxon::OSFontDefinition | Input | false | false | false |  |  |  | 
Object/Height | <inport@GyNFeVsNIdhobqlaFM8rWO | maxon::Float64 | Input | false | false | false |  |  | 200 | 
Object/Horizontal Spacing | <inport@MUV5KZ5bJdigKI22pvpDJI | maxon::Float64 | Input | false | false | false |  |  | 0 | 
Object/Plane | <inport@PbnO635IIJuuX8SDQnZ27N | maxon::InternedId | Input | false | false | true |  |  | xy | XY = xy, ZY = zy, XZ = xz
Object/Reverse | <inport@bpPd0g2AJVRjm2n_UAyz5O | maxon::Bool | Input | false | false | false |  |  |  | 
Object/Vertical Spacing | <inport@b8Cscm8sG9AhCUB11q3vAP | maxon::Float64 | Input | false | false | false |  |  |  | 
Outputs/Object/Parent Matrix | >matrixout/parentmatrix |  | Input | false | false | false |  |  |  | 
Outputs/Object/Position | >matrixout/translation |  | Input | false | false | false |  |  |  | 
Outputs/Object/Rotation/Scale/Shear | >matrixout/sqrmatrix |  | Input | false | false | false |  |  |  | 
Outputs/Object/Scope | >matrixout/domain |  | Input | false | false | false |  |  |  | 
Outputs/Op/Children | >net.maxon.neutron.op.output/children |  | Input | false | false | false |  |  |  | 
Outputs/Op/Parent Matrix | >net.maxon.neutron.op.output/parentmatrix |  | Input | false | false | false |  |  |  | 
Outputs/Op/Position | >net.maxon.neutron.op.output/translation |  | Input | false | false | false |  |  |  | 
Outputs/Op/Rotation/Scale/Shear | >net.maxon.neutron.op.output/sqrmatrix |  | Input | false | false | false |  |  |  | 
Outputs/Op/Scope | >net.maxon.neutron.op.output/domain |  | Input | false | false | false |  |  |  | 
Outputs/Object | >matrixout | net.maxon.neutron.portbundle.object | Output | false | true | false |  |  |  | 
Outputs/Op | >net.maxon.neutron.op.output | net.maxon.neutron.portbundle.object | Output | false | true | false |  |  |  | 
Outputs/Output | >children.out |  | Output | false | false | false |  |  |  | 

