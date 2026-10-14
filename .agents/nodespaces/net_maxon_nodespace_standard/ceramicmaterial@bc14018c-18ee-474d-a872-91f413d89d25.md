# Node Template: Ceramic Material

- **Node Space ID:** `net.maxon.nodespace.standard`
- **Template ID:** `ceramicmaterial@bc14018c-18ee-474d-a872-91f413d89d25`
- **Template Name:** `Ceramic Material`

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
Base/Color | <inport@NCp9FVDiBRmqjbnNXTd4SY | maxon::Color64 | Input | false | false | false |  |  | (0.692,0.584,0.386) | 
Base/Flakes | <inport@FgET98jXIVsnG0$DXaBaSZ | maxon::Float64 | Input | false | false | false |  | 1 | 0.4 | 
Base/Grain | <inport@PJICK1o6EVwqIhmOys8cXb | maxon::Float64 | Input | false | false | false | 0 | 1 | 0.5 | 
Reflectance/Irregularities | <inport@JtPteJMxK5hvC2BrKKNUHd | maxon::Float64 | Input | false | false | false |  | 1 | 0.5 | 
Reflectance/Reflectance | <inport@GoQPnO_PJVSmY$EfYMUjh9 | maxon::Bool | Input | false | false | false |  |  | false | 
Reflectance/Roughness | <inport@HL8TM6pkLdxsL7l$S3n0xe | maxon::Float64 | Input | false | false | false | 0 | 1 | 0.2 | 
Reflectance/Strength | <inport@dUeQ2mHFOVYvUdD6rTw6we | maxon::Float64 | Input | false | false | false | 0 | 1 | 0.1 | 
Variation/Seed | <inport@QtgCQox2IZYgspoWYBns9e | maxon::UInt32 | Input | false | false | false |  |  | 200 | 

