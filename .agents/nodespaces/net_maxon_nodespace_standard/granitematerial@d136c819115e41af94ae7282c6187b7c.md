# Node Template: Granite Material

- **Node Space ID:** `net.maxon.nodespace.standard`
- **Template ID:** `granitematerial@d136c819115e41af94ae7282c6187b7c`
- **Template Name:** `Granite Material`

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
Base/Color | <inport@HDn_Pn7xCZ_hfWiCg$kXg5 | maxon::Color64 | Input | false | false | false |  |  | (0.38,0.336,0.203) | 
Base/Fine Grain | <inport@LR_GDlANKx8oO3NMEIuvC6 | maxon::Float64 | Input | false | false | false | 0 | 1 | 0.35 | 
Crystals/Large Crystal Opacity | <inport@Ql5ZXSagLFgoCgspwK2UM_ | maxon::Float64 | Input | false | false | false | 0 | 1 | 0.2 | 
Crystals/Large Crystals Color | <inport@SgySIk72Bt0nOmjYK9RsR8 | maxon::Color64 | Input | false | false | false |  |  | (0.233,0.14,0.069) | 
Crystals/Small Crystals Color | <inport@EVkx$Z6DMpsj3iB_Owkqb7 | maxon::Color64 | Input | false | false | false |  |  | (0.023,0.036,0.04) | 
Crystals/Small Crystals Opacity | <inport@ab$Vy16iIxdsZzsY4IySE7 | maxon::Float64 | Input | false | false | false | 0 | 1 | 0.2 | 
Flakes/Density | <inport@dEIaDQVgERitP_7f8IFOg8 | maxon::Float64 | Input | false | false | false |  | 1 | 0.6 | 
Flakes/Intensity | <inport@fAkjIoYzAN1qxWJPDUb0_$ | maxon::Float64 | Input | false | false | false |  | 1 | 0.1 | 
Flakes/Scale | <inport@Rojj$PekOBhiNf7KJlUoK_ | maxon::Float64 | Input | false | false | false | 0.01 | 1000 | 0.02 | 
Reflectance/Intensity | <inport@DvS2IjV0OVgsjg8qu47J_6 | maxon::Float64 | Input | false | false | false | 0 | 1 | 0.4 | 
Reflectance/Reflectance | <inport@TghN$kVjIxno_CaPbZKJw4 | maxon::Bool | Input | false | false | false |  |  | true | 
Reflectance/Roughness | <inport@WwtccU1_IdQky4ZvpzI8Q6 | maxon::Float64 | Input | false | false | false |  | 1 | 0.08 | 
Variation/Seed | <inport@Fkjul_gLGBfpppn1ySvVK9 | maxon::Int32 | Input | false | false | false |  |  | 250 | 

