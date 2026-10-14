# Node Template: Stairs

- **Node Space ID:** `net.maxon.neutron.nodespace`
- **Template ID:** `com.rocketlasso.neutron.asset.stairs`
- **Template Name:** `Stairs`

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
Node Category | net.maxon.node.base.category | maxon::InternedId | Attribute | false | false | true |  |  | primitives | operators = operators, distributions = distributions, geometries = geometries, patterns = patterns, primitives = primitives, effectors = effectors, fields = fields, functions = functions, structures = structures
Preview/Node | net.maxon.node.base.nodepreviewimage | maxon::ImageBaseRef | Attribute | false | false | false |  |  |  | 
Object/ | <attr.1c7348b505e9403b9609710de9fbec5a |  | Input | false | false | false |  |  |  | 
Object/ | <attr.b6db728a6f4e4ec0a6e37bbf8cef42c0 |  | Input | false | false | false |  |  |  | 
Object/Bevel 1 | <attr.6331fbbb98b34f87b2cc077589634b2b | maxon::Float64 | Input | false | false | false |  |  | 0 | 
Object/Bevel 2 | <attr.d3383de40adc4d1e9bc276e68b81037c | maxon::Float64 | Input | false | false | false |  |  | 0 | 
Object/Count | <attr.c9b2b822a10045fa8e331d29d35e8024 | maxon::Int64 | Input | false | false | false | 1 | 9999999 | 3 | 
Object/Depth | <attr.1ce51f834db8496bbf880d26af2f19e4 | maxon::Float64 | Input | false | false | false |  |  | 48 | 
Object/Depth | <attr.fae8991306de4f9d915e5c0742e8f29b | maxon::Float64 | Input | false | false | false |  |  | 48 | 
Object/Height | <attr.33426239f31349f48c3f39cb0e5ee09d | maxon::Float64 | Input | false | false | false |  |  | 12 | 
Object/Plane | <attr.60e362a8f6b441af995b5e6166dcd15f | maxon::Int64 | Input | false | false | true |  |  | 2 | Z- = 3, X+ = 0, X- = 1, Y+ = 4, Y- = 5, Z+ = 2
Object/Riser Thickness | <attr.41663296398e4773a45b53b5ac2423d3 | maxon::Float64 | Input | false | false | false |  |  | 0 | 
Object/Spread | <attr.176457bfb39349018d3ce7adebd8d8f1 | maxon::Float64 | Input | false | false | false |  |  | 1 | 
Object/Spread | <attr.b7ddf949967749a1bf709bda62bd7ed0 | maxon::Float64 | Input | false | false | false |  |  | 1 | 
Object/Step | <attr.037d991980ae4625b572fd41069dabfe |  | Input | false | false | false |  |  |  | 
Object/Step Count | <attr.bf66272deb6640a38e8f0365521276ab | maxon::Int64 | Input | false | false | false |  | 9999999 | 10 | 
Object/Step Depth | <attr.cd669e4763d4467993acedebbe2218cd | maxon::Float64 | Input | false | false | false |  |  | 35 | 
Object/Step Extend | <attr.3997f1d7d4284e1da9afc5a8b854fb50 | maxon::Float64 | Input | false | false | false | 0 |  | 0 | 
Object/Step Height | <attr.f1cc7fb5361e49929345c1c8e02c4aa3 | maxon::Float64 | Input | false | false | false |  |  | 16 | 
Object/Step Nose | <attr.38900e6a44fc46819a35e133a8606a3b | maxon::Float64 | Input | false | false | false |  |  | 0 | 
Object/Step Thickness | <attr.abb83adcb5fe4d0aa74703e7631ae2f8 | maxon::Float64 | Input | false | false | false |  |  | 2 | 
Object/Step Widen | <attr.5561ddfd6b4f4fcfac98ccdcca68f2a8 | maxon::Float64 | Input | false | false | false |  |  | 0 | 
Object/Subdivide | <attr.ad69f8ca8e644f288b9e2df5eff65540 | maxon::Bool | Input | false | false | false |  |  |  | 
Object/Support | <attr.4dd7e2a696954429b8b6d7d24f7d1d1c |  | Input | false | false | false |  |  |  | 
Object/Thickness | <attr.3ea98640f54c42fbad08c978b8cee1cd | maxon::Float64 | Input | false | false | false |  |  | 3 | 
Object/Thickness | <attr.634262c197c747b4914600736e3ceca7 | maxon::Float64 | Input | false | false | false |  |  | 8 | 
Object/Type | <attr.e9287fde950b4b76bb8b634357380cea | maxon::Int64 | Input | false | false | true |  |  | 1 | Solid = 0, Stringer = 1, None = 2
Object/Wall String | <attr.cb831460a4a84feeb03c416c54a180ab | maxon::Int64 | Input | false | false | true |  |  |  | None = 0, Both = 1, Left = 2, Right = 3
Object/Wall String  | <attr.638f3819cfc84d1fb0bf0d43a8d6d63c |  | Input | false | false | false |  |  |  | 
Object/Width | <attr.fc7a3f76b35f413686a30f859f3c5758 | maxon::Float64 | Input | false | false | false |  |  | 240 | 
Selections/C1 | <in@eiYfcpVAPVZpno34XQo3xA | maxon::String | Input | false | false | false |  |  | C1 | 
Selections/C2 | <in@SdWBuPPUCFfrZ2nJG67FVD | maxon::String | Input | false | false | false |  |  | C2 | 
Selections/R1 | <in@ekI6Zt9JMhgj3yNkljmocA | maxon::String | Input | false | false | false |  |  | R1 | 
Selections/R2 | <in@RtRR80uaLVtopQUnMxjptG | maxon::String | Input | false | false | false |  |  | R2 | 
Selections/Risers | <in@G6vkj_rFB9DhoSAKO$HBgE | maxon::String | Input | false | false | false |  |  | Risers | 
Selections/S | <in@LOveswQlKJok7qQ8nAv9dF | maxon::String | Input | false | false | false |  |  | S | 
Selections/Steps | <in@GmEqs6uYDtyiwznd5e7HPB | maxon::String | Input | false | false | false |  |  | Steps | 
Selections/Stringers | <in@b$fJlIk9D1jrnnFOtRhPIE | maxon::String | Input | false | false | false |  |  | Stringers | 
Selections/Wall Stringers | <in@ZMRoqDRhCBtkHD6JfqwL5F | maxon::String | Input | false | false | false |  |  | Wall Stringers | 
Outputs/Geometry | >geometryout | maxon::GeometryObject | Output | false | false | false |  |  |  | 

