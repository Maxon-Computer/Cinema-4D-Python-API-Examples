# Node Template: Gold Material

- **Node Space ID:** `net.maxon.nodespace.standard`
- **Template ID:** `goldmaterial@2efa3a34-f5c3-4b7c-938a-1e051180ee8c`
- **Template Name:** `Gold Material`

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
Base/Base Color | <inport@RS7_ehlmBZklzaq5xaJXrf | maxon::ColorA64 | Input | false | false | false |  |  | (0.523,0.471,0.277,1) | 
Base/Grain | <inport@BDVFQrXmLx5uYBafh8Exma | maxon::Float64 | Input | false | false | false |  | 1 | 0.2 | 
Deformation/Damage | <inport@YVggX_7JNN6tsB35bjaohL | maxon::Float64 | Input | false | false | false | 0 | 1 | 0.5 | 
Deformation/Folding | <inport@Vv69xfSmOlUnhg0GzK3IJK | maxon::Float64 | Input | false | false | false | 0 | 1 | 0 | 
Deformation/Octaves | <inport@dtMXUqMWKRsogXt3dYrgBf | maxon::Float64 | Input | false | false | false | 1 | 20 | 5 | 
Deformation/Strength | <inport@ATnO4mvQHJnnCfovv1q0Nc | maxon::Float64 | Input | false | false | false | 0 | 1 | 0.15 | 
Patina/Color | <inport@WtQs2UHiN9Epz61aIRi4Ea | maxon::ColorA64 | Input | false | false | false |  |  | (0.012,0.012,0.01,1) | 
Patina/Strength | <inport@WO8G8SmHJBekw5vvb9L8cf | maxon::Float64 | Input | false | false | false |  | 1 | 0 | 
Reflectance/Roughness | <inport@Z9paS9QeHB0jpXwzygSUqd | maxon::Float64 | Input | false | false | false |  | 1 | 0.12 | 
Reflectance/Strength | <inport@Uueys6fGJ9_gCE7WG6bSAY | maxon::Float64 | Input | false | false | false |  | 1 | 0.9 | 
Variation/Seed | <inport@X1T7v68ZGBhqo2lXMiVYfb | maxon::UInt32 | Input | false | false | false |  |  | 170 | 

