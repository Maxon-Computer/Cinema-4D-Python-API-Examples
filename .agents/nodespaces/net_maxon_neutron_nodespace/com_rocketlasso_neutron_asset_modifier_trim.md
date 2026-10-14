# Node Template: Trim Spline Modifier

- **Node Space ID:** `net.maxon.neutron.nodespace`
- **Template ID:** `com.rocketlasso.neutron.asset.modifier.trim`
- **Template Name:** `Trim Spline Modifier`

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
Node Category | net.maxon.node.base.category | maxon::InternedId | Attribute | false | false | true |  |  | geomodifiers | distributions = distributions, operators = operators, geometries = geometries, patterns = patterns, primitives = primitives, effectors = effectors, fields = fields, functions = functions, structures = structures, geomodifiers = geomodifiers, geogenerators = geogenerators
Preview/Node | net.maxon.node.base.nodepreviewimage | maxon::ImageBaseRef | Attribute | false | false | false |  |  |  | 
Inputs/Geometry | <geometryin | maxon::GeometryObject | Input | false | false | false |  |  | 0 | 
Object/ | <in@KJVepIejMZlpGgWwllan$9 |  | Input | false | false | false |  |  |  | 
Object/ | <in@P4CE$66mIVfmz6Bs0BFcUd |  | Input | false | false | false |  |  |  | 
Object/End | <attr.187f589b831f4eff9e38e5ecd868cc63 | maxon::Float64 | Input | false | false | false |  | 1 | 1 | 
Object/From End | <in@b8RtdYS6IVCsKVkngqOIoq | maxon::Float64 | Input | false | false | false |  | 0 | 0 | 
Object/From Start | <in@MO0RC05KE1ymamZ1PWxNCs | maxon::Float64 | Input | false | false | false |  | 0 |  | 
Object/Group Clamp (Percentage) | <in@J$T4JMD2ERYqms$ZWYNyvs |  | Input | false | false | false |  |  |  | 
Object/Group Clamp (Percentage)/Clamp Max | <in@cwaEia05CdYuOIEgmh7tjr | maxon::Float64 | Input | false | false | false |  | 1 | 1 | 
Object/Group Clamp (Percentage)/Clamp Min     | <in@OVSOECv6FdKrKyUbrGMJtt | maxon::Float64 | Input | false | false | false |  | 1 |  | 
Object/Group Offset (Percentage) | <attr.dcefd6214f3740bfa84add96c6bf7ab9 |  | Input | false | false | false |  |  |  | 
Object/Group Offset (Percentage)/Offset            | <attr.a8e02b8ada214d66b0ebe0bfaf94966b | maxon::Float64 | Input | false | false | false |  |  | 0 | 
Object/Group Offset (Percentage)/Rate | <attr.536088c548964865b339b1f1fcfd81ef | maxon::Float64 | Input | false | false | false |  |  | 0 | 
Object/Group Offset (Trim) | <in@AiD5t9r2P9rmikOBF_uSLq |  | Input | false | false | false |  |  |  | 
Object/Group Offset (Trim)/          Rate | <in@f8RLLNKZLxxi74MRNs$Uoq | maxon::Float64 | Input | false | false | false |  |  | 0 | 
Object/Group Offset (Trim)/Offset            | <in@U92oQzjJIp5iO$yE_GGzKp | maxon::Float64 | Input | false | false | false |  |  | 0 | 
Object/Invert             | <attr.a5f8a6d008b3428596580f49eb02219e | maxon::Bool | Input | false | false | false |  |  |  | 
Object/Limit              | <in@M5aCL38xDxki9kcl4ZdWE9 | maxon::Int64 | Input | false | false | true |  |  | 1 | Loop = 1, Custom = 2
Object/Mode | <in@Jb4SDQOcONBuFLXKnaDv9t | maxon::Int64 | Input | false | false | true |  |  | 1 | Length = 0, Percentage = 1
Object/Per Segment | <in@fArpbVPAOZVj2G1ZBZDlfo | maxon::Bool | Input | false | false | false |  |  | 0 | 
Object/Start | <attr.6ef8d78186b7484f95e835802e19e7e3 | maxon::Float64 | Input | false | false | false |  | 1 | 0 | 
Object | >out@MDrHyj0yNJ6qxC1ulG8T3J |  | Output | false | false | false |  |  |  | 
Outputs/Geometry | >geometryout | maxon::GeometryObject | Output | false | false | false |  |  |  | 

