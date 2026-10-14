# Node Template: Geoposition on Equirectangular

- **Node Space ID:** `net.maxon.neutron.nodespace`
- **Template ID:** `net.maxon.neutron.asset.math.geopositiononequirectangular`
- **Template Name:** `Geoposition on Equirectangular`

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
Node Category | net.maxon.node.base.category | maxon::InternedId | Attribute | false | false | true |  |  | functions | operators = operators, distributions = distributions, geometries = geometries, patterns = patterns, primitives = primitives, effectors = effectors, fields = fields, functions = functions, structures = structures, geomodifiers = geomodifiers, geogenerators = geogenerators
Preview/Node | net.maxon.node.base.nodepreviewimage | maxon::ImageBaseRef | Attribute | false | false | false |  |  |  | 
Inputs/Lat (Deg) | <inport@TDY54mJpIdIkGHI8qSbMS9 | maxon::Float64 | Input | false | false | false |  |  | -999999 | 
Inputs/Latitude | <inport@YukCBETuE9wsy_Nq3pslI3 | maxon::Float64 | Input | false | false | false | -1.571 | 1.571 |  | 
Inputs/Long (Deg) | <inport@N7lSdfapGZQljYaracz_j7 | maxon::Float64 | Input | false | false | false |  |  | -999999 | 
Inputs/Longitude | <inport@c$4g$ZkzO5Pr0D2gAQEXe3 | maxon::Float64 | Input | false | false | false | -3.142 | 3.142 |  | 
Inputs/Size | <inport@BhmQthWfCF2nnG9$NVGo56 | maxon::Vector2d64 | Input | false | false | false |  |  | (50,100) | 
Outputs/Matrix | >out@e7PHVWtfBRbgBPjNAOlLC9 | maxon::Matrix64 | Output | false | false | false |  |  |  | 
Outputs/UV | >outport@f6DkkXrNClWvFRvSJPI9k3 | maxon::Vector2d64 | Output | false | false | false |  |  |  | 

