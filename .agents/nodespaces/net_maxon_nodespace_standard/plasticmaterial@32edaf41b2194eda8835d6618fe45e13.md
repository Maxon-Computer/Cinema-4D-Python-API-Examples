# Node Template: Plastic Material

- **Node Space ID:** `net.maxon.nodespace.standard`
- **Template ID:** `plasticmaterial@32edaf41b2194eda8835d6618fe45e13`
- **Template Name:** `Plastic Material`

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
Base/Color | <inport@cq6U_ShMPNMn2SoueQnbrg | maxon::Color64 | Input | false | false | false |  |  | (0.123,0.182,0.448) | 
Base/Dirt | <inport@BPsafprfMFrl35zVqXGWnk | maxon::Float64 | Input | false | false | false |  | 1 | 0.5 | 
Base/Roughness | <inport@P$7qnEhhFxSgpHDotkBsDh | maxon::Float64 | Input | false | false | false |  | 1 | 0.3 | 
Base/Structure | <inport@J0BFIgmMK1Ulhy3O13NAPh | maxon::Float64 | Input | false | false | false |  | 1 | 0.3 | 
Base/Type | <inport@WTyAnVRrDd4ms4fKf7zWOl | maxon::Int64 | Input | false | false | true |  |  | 2 | Polystyrene = 0, Polyurethane = 1, ABS = 2
Deformation/Deformation | <inport@SzUxKt8mDVYpDlM$e2d2Ik | maxon::Float64 | Input | false | false | false | -1 | 1 | 0.05 | 
Reflectance/Intensity | <inport@eMHXSM1_ORtlsqG1Z0JLvl | maxon::Float64 | Input | false | false | false | 0 | 1 | 0.08 | 
Reflectance/Reflectance | <inport@Em68lSTjAFck5Jq69aRN3m | maxon::Bool | Input | false | false | false |  |  | true | 
Variation/Seed | <inport@CurLxMisJJqoJ1qBdKFp5k | maxon::UInt32 | Input | false | false | false |  |  | 300 | 

