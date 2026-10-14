# Node Template: Rock Material

- **Node Space ID:** `net.maxon.nodespace.standard`
- **Template ID:** `rockmaterial@629f3c89-7b68-411e-a7cd-4a8d4de72328`
- **Template Name:** `Rock Material`

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
Base/Coarse Grain | <inport@IJoBJz0ZKJXh6j0IoKQntz | maxon::Float64 | Input | false | false | false | 0 | 1 | 0.25 | 
Base/Color | <inport@T25UMaYzJBtmgQE6212q22 | maxon::Color64 | Input | false | false | false |  |  | (0.171,0.165,0.136) | 
Base/Fine Grain | <inport@WHJlrldVIJanFiVCHf2T6x | maxon::Float64 | Input | false | false | false | 0 | 1 | 0.25 | 
Base/Large Structure | <inport@U4nXYP6ZE52o7o9WVb8Gpz | maxon::Float64 | Input | false | false | false | 0 | 1 | 0.5 | 
Deformation/Deformation | <inport@KNIYVKBRAF2nvGGI0nA9Qy | maxon::Float64 | Input | false | false | false | -1 | 1 | 0.2 | 
Reflectance/Reflectance | <inport@XsVM5CnWPtjrnD8e0MB$jK | maxon::Bool | Input | false | false | false |  |  | false | 
Reflectance/Strength | <inport@SFfM9r5TG9Muef2jK69wXq | maxon::Float64 | Input | false | false | false |  | 1 | 0.4 | 
Variation/Seed | <inport@V7XpsRDcPJokRLg$vttfIx | maxon::UInt32 | Input | false | false | false |  |  | 200 | 

