# Node Template: BSDF

- **Node Space ID:** `net.maxon.nodespace.standard`
- **Template ID:** `net.maxon.render.node.bsdf`
- **Template Name:** `BSDF`

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
Node Category | net.maxon.node.base.category | maxon::InternedId | Attribute | false | false | true |  |  | patterns | distributions = distributions, operators = operators, geometries = geometries, patterns = patterns, primitives = primitives, effectors = effectors, fields = fields, functions = functions, structures = structures, geomodifiers = geomodifiers, geogenerators = geogenerators
Preview/Node | net.maxon.node.base.nodepreviewimage | maxon::ImageBaseRef | Attribute | false | false | false |  |  |  | 
Context/Context | <context | maxon::ShadingContext | Input | false | false | false |  |  |  | 
Inputs/Anisotropy | <anisotropy | maxon::Float | Input | false | false | false |  | 1 | 0.25 | 
Inputs/BSDF Type | <bsdftype | maxon::InternedId | Input | false | false | true |  |  | orennayerbrdf | Diffuse = orennayerbrdf, Beckmann = beckmannbrdf, GGX = ggxbrdf, Phong = phongbrdf, Ward = wardbrdf, Anisotropic = anisotropicbrdf
Inputs/Color | <color | maxon::ColorA | Input | false | false | false |  |  | (0.604,0.604,0.604,1) | 
Inputs/Conductor Absorption | <conductorabs | maxon::Vector | Input | false | false | false |  |  | (8.313,6.288,4.984) | 
Inputs/Conductor IOR | <conductorior | maxon::Vector | Input | false | false | false |  |  | (1.444,0.858,0.528) | 
Inputs/Dielectric IOR | <dielectricior | maxon::Float | Input | false | false | false | 1 | 5 | 1.575 | 
Inputs/Fresnel | <fresneltype | maxon::InternedId | Input | false | false | true |  |  | none | None = none, Conductor = conductor, Dielectric = dielectric
Inputs/Fresnel Strength | <fresnelstrength | maxon::Float | Input | false | false | false |  | 1 | 1 | 
Inputs/Intensity | <reflectionstrength | maxon::Float | Input | false | false | false |  | 100000000000000000000 | 1 | 
Inputs/Normal | <normal | maxon::Vector | Input | false | false | false |  |  |  | 
Inputs/Normal Strength | <normalstrength | maxon::Float | Input | false | false | false |  | 1 | 1 | 
Inputs/Opaque | <opaquefresnel | maxon::Bool | Input | false | false | false |  |  | false | 
Inputs/Orientation | <orientation | maxon::Float | Input | false | false | false |  |  |  | 
Inputs/Roughness | <roughness | maxon::Float | Input | false | false | false |  | 1 | 0 | 
Inputs/Sampling Subdivision | <samplesubdiv | maxon::Float | Input | false | false | false | 0 | 16 | 4 | 
Outputs/Result | >result | maxon::BSDFLayer | Output | false | false | false |  |  |  | 

