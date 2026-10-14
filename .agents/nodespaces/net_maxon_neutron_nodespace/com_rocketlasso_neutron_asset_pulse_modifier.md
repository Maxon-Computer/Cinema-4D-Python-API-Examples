# Node Template: Pulse Spline Modifier

- **Node Space ID:** `net.maxon.neutron.nodespace`
- **Template ID:** `com.rocketlasso.neutron.asset.pulse.modifier`
- **Template Name:** `Pulse Spline Modifier`

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
Node Category | net.maxon.node.base.category | maxon::InternedId | Attribute | false | false | true |  |  | geomodifiers | operators = operators, distributions = distributions, geometries = geometries, patterns = patterns, primitives = primitives, effectors = effectors, fields = fields, functions = functions, structures = structures, geomodifiers = geomodifiers, geogenerators = geogenerators
Preview/Node | net.maxon.node.base.nodepreviewimage | maxon::ImageBaseRef | Attribute | false | false | false |  |  |  | 
Inputs/Geometry | <geometryin | maxon::GeometryObject | Input | false | false | false |  |  |  | 
Inputs/Input | <in@MUBybSpuDhThroypAcQm9I |  | Input | false | false | false |  |  |  | 
Object/Length | <in@K0dfe$czCNEgQCsZxKLwHb |  | Input | false | false | false |  |  |  | 
Object/Length Group/Length Variation      | <in@EP0Vy4ikMFwok8BdevMhwJ | maxon::Float64 | Input | false | false | false |  |  | 0 | 
Object/Length Group/Length Variation      | <in@dS35k5MYApZjzINpYYAtht | maxon::Float64 | Input | false | false | false |  | 1 | 0 | 
Object/Length Group/Total Length | <in@Eg8d8Fw1LdMl7lx1yeO_6J | maxon::Float64 | Input | false | false | false |  |  | 100 | 
Object/Length Group/Total Length | <in@I88Xaf6zPVGnUa75gC2Nhn | maxon::Float64 | Input | false | false | false |  | 1 | 0.25 | 
Object/Mode | <in@TUg4MiPHCBbgZqHTemGlJm | maxon::Int64 | Input | false | false | true |  |  | 1 | Pulse = 1, Continuous = 0, One Shot = 2
Object/Seed                          | <in@JQhngQhZJ1vqtcnhKoh6Ti | maxon::Float64 | Input | false | false | false |  |  | 12345 | 
Object/Start & End | <in@NU2$$uJZARNqOWe_VNJ0sb |  | Input | false | false | false |  |  |  | 
Object/StartEnd Group/ | <in@QZ6mAJdCOJ7sxXaF$EpVSl |  | Input | false | false | false |  |  |  | 
Object/StartEnd Group/ | <in@RWvdiaCDE5IkQEH18gO3Xd |  | Input | false | false | false |  |  |  | 
Object/StartEnd Group/ | <in@Yw0RhB0YFddnkGFs8T8gPc |  | Input | false | false | false |  |  |  | 
Object/StartEnd Group/Delay Loop | <in@Fpbop94qIl7jjqOKBP$bXg | maxon::TimeValue | Input | false | false | false |  |  | 0 | 
Object/StartEnd Group/End By | <in@bdA9SvC4AZhnW8C3baw5Zh | maxon::TimeValue | Input | false | false | false |  |  | 333300.0 ms | 
Object/StartEnd Group/Loop Point | <in@RdTkS3hELdntG7smfW5wfZ | maxon::TimeValue | Input | false | false | false |  |  | 1000.0 ms | 
Object/StartEnd Group/Movement | <in@ZvSHlX68Al5qEBgFQBJQ1Y |  | Input | false | false | false |  |  |  | 
Object/StartEnd Group/Movement Per Sec | <in@LD6ngRUqP9lp05GyZhNZ_K | maxon::Float64 | Input | false | false | false |  |  | 200 | 
Object/StartEnd Group/Override Time | <in@C3eqD4rECFBqi2pzNFZkc0 | maxon::Bool | Input | false | false | false |  |  |  | 
Object/StartEnd Group/Randomize Per Loop | <in@ILlgrlYPNV2l2PkOwEC0cZ | maxon::Bool | Input | false | false | false |  |  |  | 
Object/StartEnd Group/Reverse | <in@VTXHNmjDP5AmG6Ps6t__8l | maxon::Float64 | Input | false | false | false |  | 1 |  | 
Object/StartEnd Group/Speed Variation | <in@Kc6I393zBlamrGW2z1H9QI | maxon::Float64 | Input | false | false | false |  |  |  | 
Object/StartEnd Group/Start Randomize       | <in@DdeMmR3LLBEgePuueXYbgf | maxon::TimeValue | Input | false | false | false |  |  | 0.0 ns | 
Object/StartEnd Group/Start Time | <in@cl8aSsCkCxLm4znVKYnSdi | maxon::TimeValue | Input | false | false | false |  |  |  | 
Object/StartEnd Group/Time Offset               | <in@OdWcr0gfHVylR90D0ONudb | maxon::TimeValue | Input | false | false | false |  |  | 0.0 ns | 
Object/StartEnd Group/Variation | <in@ENh1SeotN1$rEbDSZJ715g | maxon::Float64 | Input | false | false | false |  | 1 | 0 | 
Object/Units | <in@bkUG0QLpKF5mRrNemJ_fWP | maxon::Int64 | Input | false | false | true |  |  |  | Percent = 0, Length = 1
Weights/ | <in@T08XMgFmOpQl1b6DboqmUm |  | Input | false | false | false |  |  |  | 
Weights/Mapping | <in@U1iLFRR2JV6o1m$8FxzB5a | maxon::Int64 | Input | false | false | true |  |  | 0 | All 0%-100% = 0, Relative to Longest (Aligned On 0%) = 1, Relative to Longest (Aligned On 100%) = 3, Subsequent = 2
Weights/Weights | <in@aBj4aMDgL5Ams0BX02foLi | maxon::Int64 | Input | false | false | true |  |  | 1 | Tags = 0, Raw Spline = 1
Weights/Weights Tags/Growth | <in@NDW59tA5E1JtXhSTC8cUlj | maxon::String | Input | false | false | false |  |  | Growth | 
Outputs/Geometry | >geometryout | maxon::GeometryObject | Output | false | false | false |  |  |  | 

