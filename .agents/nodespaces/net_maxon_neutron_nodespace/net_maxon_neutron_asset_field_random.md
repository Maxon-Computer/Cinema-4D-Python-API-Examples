# Node Template: Random

- **Node Space ID:** `net.maxon.neutron.nodespace`
- **Template ID:** `net.maxon.neutron.asset.field.random`
- **Template Name:** `Random`

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
Object/Mode | <inport@MeZJW40ZA5Au9PqkT9Kykl | maxon::Int64 | Input | false | false | true |  |  |  | Random = 0, Noise = 1
Object/Noise Type | <inport@IStweTcFJV1rDK0w_4ELwg | maxon::Id | Input | false | false | true |  |  | net.maxon.render.rendernoiseclass.perlin | registry#net.maxon.render.registry.rendernoiseclasses = registry#net.maxon.render.registry.rendernoiseclasses
Object/Position | <net.maxon.neutron.parameter.position | maxon::Vector | Input | false | false | false |  |  |  | 
Object/Relative Scale | <f4k0G1SWNZZlGjmQuO3Uim | maxon::Vector64 | Input | false | false | false | (0,0,0) |  | (1,1,1) | 
Object/Scale | <inport@Av3PoKUTD1xggPjJDWDHR9 | maxon::Float64 | Input | false | false | false | 0 |  | 1 | 
Object/Seed | <inport@ENVRQCXUCJjoWWj$yKwSJr | maxon::UInt32 | Input | false | false | false |  |  | 12345 | 
Outputs/Field Strength | >net.maxon.neutron.result | maxon::Float64 | Output | false | false | false |  |  |  | 

