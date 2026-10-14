# Node Template: Great Circle Distance

- **Node Space ID:** `net.maxon.neutron.nodespace`
- **Template ID:** `net.maxon.neutron.asset.math.geopositionstocircledistance`
- **Template Name:** `Great Circle Distance`

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
Inputs/Latitude A | <out@HY_516P_DFqoEOPtW6P5Ek | maxon::Float64 | Input | false | false | false | -1.571 | 1.571 |  | 
Inputs/Latitude B | <out@IUZYAxZCKZ_pV8tzM86y6i | maxon::Float64 | Input | false | false | false | -1.571 | 1.571 |  | 
Inputs/Longitude A | <out@W2KxQwzICBzoPubICBtCpg | maxon::Float64 | Input | false | false | false | -3.142 | 3.142 |  | 
Inputs/Longitude B | <out@Y8dNjDd2OdXvtEFDJ5JH5g | maxon::Float64 | Input | false | false | false | -3.142 | 3.142 |  | 
Inputs/Radius | <out@BXhfgq_vItJk9OQ3AmjlOg | maxon::Float64 | Input | false | false | false |  |  | 50 | 
Outputs/Result | >out@XbXWyPnBHdClZ8qsKdzvUg | maxon::Float64 | Output | false | false | false |  |  |  | 

