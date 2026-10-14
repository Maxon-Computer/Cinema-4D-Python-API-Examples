# Node Template: Transform

- **Node Space ID:** `net.maxon.neutron.nodespace`
- **Template ID:** `transform@677a4ca8-f5c5-4aba-b194-cfa18ac96f88`
- **Template Name:** `Transform`

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
Node Category | net.maxon.node.base.category | maxon::InternedId | Attribute | false | false | true |  |  | functions | distributions = distributions, operators = operators, geometries = geometries, patterns = patterns, primitives = primitives, effectors = effectors, fields = fields, functions = functions, structures = structures, geomodifiers = geomodifiers, geogenerators = geogenerators
Preview/Node | net.maxon.node.base.nodepreviewimage | maxon::ImageBaseRef | Attribute | false | false | false |  |  |  | 
Context/Context | <context@RpsJ_Z_DCBduEHpwqeKJw$ | maxon::ShadingContext | Input | false | false | false |  |  |  | 
Inputs/Color | <result@Rcrm_YbXM5CiOe0rM2ahv9 | maxon::ColorA64 | Input | false | false | false |  |  |  | 
Inputs/Decal U | <localdecalu@OKA7_OlYIBjnBE32yT8jp8 | maxon::Bool | Input | false | false | false |  |  | false | 
Inputs/Decal V | <localdecalv@Rxj7wmwhKZXlJ7596At4h7 | maxon::Bool | Input | false | false | false |  |  | false | 
Inputs/Length | <locallength@dssJynSSDZ_n$VEnjon_x8 | maxon::Vector2d64 | Input | false | false | false |  |  | (1,1) | 
Inputs/Mode U | <localmodeu@dCPqul$LDZ6pV3JiWbZog7 | maxon::InternedId | Input | false | false | true |  |  | extend | Clamp = clamp, Repeat = repeat, Extend = extend, Mirror = mirror
Inputs/Mode V | <localmodev@QV$yVn1bKZZg0S0IbY_kp$ | maxon::InternedId | Input | false | false | true |  |  | extend | Clamp = clamp, Repeat = repeat, Extend = extend, Mirror = mirror
Inputs/Offset | <localoffset@Chn6RUruLt7nq58DJO3dx8 | maxon::Vector2d64 | Input | false | false | false |  |  |  | 
Inputs/Pivot | <localpivot@K5tlN15pAxTuGp$LPuaw_7 | maxon::Vector2d64 | Input | false | false | false |  |  | (0.5,0.5) | 
Inputs/Repetitions | <localrepetitions@UFb0_oRRCFZjHpPdaKLVB4 | maxon::Vector2d64 | Input | false | false | false |  |  | (1,1) | 
Inputs/Rotation | <localrotation@GsyKwrjuCllvdsU9C2rVs_ | maxon::Float64 | Input | false | false | false |  |  |  | 
Outputs/Result | >passthrough@UI7W98YcIlUuKwdU6JYQC7 | maxon::ColorA64 | Output | false | false | false |  |  |  | 

