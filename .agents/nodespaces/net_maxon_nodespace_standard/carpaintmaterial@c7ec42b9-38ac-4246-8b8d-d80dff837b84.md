# Node Template: Car Paint Material

- **Node Space ID:** `net.maxon.nodespace.standard`
- **Template ID:** `carpaintmaterial@c7ec42b9-38ac-4246-8b8d-d80dff837b84`
- **Template Name:** `Car Paint Material`

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
Base/Base Color | <inport@XI0iAcdBLBXgwfNBh0$7vk | maxon::Color64 | Input | false | false | false |  |  | (0.319,0.029,0.02) | 
Base/Color Shift | <inport@aIuM50pxO9wtp$HAcT50d1 | maxon::Float64 | Input | false | false | false |  | 1 | 0.1 | 
Base/Roughness | <inport@dbekr83oLtrnzdbLyavMCK | maxon::Float64 | Input | false | false | false |  | 1 | 0.5 | 
Context/Context | <inport@daSLH4AiDp$nHt86qptkhx | maxon::ShadingContext | Input | false | false | false |  |  |  | 
Flakes/Density | <inport@Ctv0ZL_OFxEpaJnGn_IgYM | maxon::Float64 | Input | false | false | false |  | 10 | 0.3 | 
Flakes/Scale | <inport@ZjxtdSaQMRAnj9NZU83iAI | maxon::Float64 | Input | false | false | false |  | 5 | 0.05 | 
Flakes/Strength | <inport@c0vwwwrTLJ1lugbCQuacWI | maxon::Float64 | Input | false | false | false |  | 1 | 0.4 | 
Gloss/Fresnel | <inport@bIlHtyjVH9rg$kTGZopRLP | maxon::Float64 | Input | false | false | false |  | 1 | 0.4 | 
Gloss/Strength | <inport@NtR597kCI90m$c4LPbjYqI | maxon::Float64 | Input | false | false | false |  | 1 | 0.5 | 
Gloss/Temperature | <inport@HRWOD8U5I1ovsnL0DSauyK | maxon::Float64 | Input | false | false | false | -1 | 1 | 0.15 | 

