# Node Template: Maxon Noise

- **Node Space ID:** `com.redshift3d.redshift4c4d.class.nodespace`
- **Template ID:** `com.redshift3d.redshift4c4d.nodes.core.maxonnoise`
- **Template Name:** `Maxon Noise`

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
Node Category | net.maxon.node.base.category | maxon::InternedId | Attribute | false | false | true |  |  | patterns | operators = operators, distributions = distributions, geometries = geometries, patterns = patterns, primitives = primitives, effectors = effectors, fields = fields, functions = functions, structures = structures, geomodifiers = geomodifiers, geogenerators = geogenerators
Preview/Node | net.maxon.node.base.nodepreviewimage | maxon::ImageBaseRef | Attribute | false | false | false |  |  |  | 
Inputs/Animation/Custom Time | <com.redshift3d.redshift4c4d.nodes.core.maxonnoise.animation_time | maxon::Float | Input | false | false | false |  |  | 0 | 
Inputs/Animation/Loop Period | <com.redshift3d.redshift4c4d.nodes.core.maxonnoise.animation_loop_period | maxon::Float | Input | false | false | false |  |  | 0 | 
Inputs/Animation/Speed | <com.redshift3d.redshift4c4d.nodes.core.maxonnoise.animation_speed | maxon::Float | Input | false | false | false |  |  | 0 | 
Inputs/Animation/Time Source | <com.redshift3d.redshift4c4d.nodes.core.maxonnoise.animation_source | maxon::Int | Input | false | false | true |  |  | 0 | Global = 0, Custom = 1
Inputs/General/Absolute | <com.redshift3d.redshift4c4d.nodes.core.maxonnoise.absolute | maxon::Bool | Input | false | false | false |  |  | false | 
Inputs/General/Color 1 | <com.redshift3d.redshift4c4d.nodes.core.maxonnoise.color1 | maxon::Color64 | Input | false | false | false |  |  | (0,0,0) | 
Inputs/General/Color 2 | <com.redshift3d.redshift4c4d.nodes.core.maxonnoise.color2 | maxon::Color64 | Input | false | false | false |  |  | (1,1,1) | 
Inputs/General/Exponent | <com.redshift3d.redshift4c4d.nodes.core.maxonnoise.exponent | maxon::Float | Input | false | false | false | 0.1 | 10 | 2 | 
Inputs/General/Gain | <com.redshift3d.redshift4c4d.nodes.core.maxonnoise.gain | maxon::Float | Input | false | false | false |  |  | 0.5 | 
Inputs/General/Lacunarity | <com.redshift3d.redshift4c4d.nodes.core.maxonnoise.lacunarity | maxon::Float | Input | false | false | false |  |  | 2.1 | 
Inputs/General/Octaves | <com.redshift3d.redshift4c4d.nodes.core.maxonnoise.octaves | maxon::Float | Input | false | false | false | 0 | 20 | 5 | 
Inputs/General/Seed | <com.redshift3d.redshift4c4d.nodes.core.maxonnoise.seed | maxon::Int | Input | false | false | false | -2147483647 | 2147483646 | 123 | 
Inputs/General/Type | <com.redshift3d.redshift4c4d.nodes.core.maxonnoise.noise_type | maxon::Int | Input | false | false | true |  |  | 13 | Ober = 15, Nutous = 14, Box noise = 1, Sema = 19, Cranal = 5, Blistered turbulence = 2, Displaced turbulence = 7, Pezo = 16, Dents = 6, Hama = 9, VL noise = 22, Stupl = 20, Naki = 12, FBM = 8, Turbulence = 21, Fire = 31, Poxo = 17, Noise = 13, Buya = 3, Mod noise = 11, Cell noise = 4, Luka = 10, Wavy turbulence = 23, Cell voronoi = 24, Displaced voronoi = 25, Sparse convolution = 26, Voronoi 1 = 27, Zada = 30, Voronoi 2 = 28, Voronoi 3 = 29, Electric = 32, Gaseous = 33, Ridged Multi Fractal = 34
Inputs/Input/Offset | <com.redshift3d.redshift4c4d.nodes.core.maxonnoise.coord_offset | maxon::Vector64 | Input | false | false | false |  |  | (0,0,0) | 
Inputs/Input/Overall Scale | <com.redshift3d.redshift4c4d.nodes.core.maxonnoise.coord_scale_global | maxon::Float | Input | false | false | false |  |  | 100 | 
Inputs/Input/Rotation | <com.redshift3d.redshift4c4d.nodes.core.maxonnoise.coord_rotation | maxon::Vector64 | Input | false | false | false |  |  | (0,0,0) | 
Inputs/Input/Scale | <com.redshift3d.redshift4c4d.nodes.core.maxonnoise.coord_scale | maxon::Vector64 | Input | false | false | false |  |  | (1,1,1) | 
Inputs/Input/Source | <com.redshift3d.redshift4c4d.nodes.core.maxonnoise.coord_source | maxon::Int | Input | false | false | true |  |  | 2 | UV/Vertex Attribute = 0, Object = 2, World = 3
Inputs/Input/UV Context | <com.redshift3d.redshift4c4d.nodes.core.maxonnoise.uv_context | RSC4D::UVContext | Input | false | false | false |  |  |  | 
Inputs/Input/Vertex Attribute Name | <com.redshift3d.redshift4c4d.nodes.core.maxonnoise.coord_attribute | maxon::String | Input | false | false | false |  |  |  | 
Inputs/Legacy_globalscale_obj | <com.redshift3d.redshift4c4d.nodes.core.maxonnoise.legacy_globalscale_obj | maxon::Float | Input | false | false | false |  |  | 0.1 | 
Inputs/Legacy_globalscale_uv | <com.redshift3d.redshift4c4d.nodes.core.maxonnoise.legacy_globalscale_uv | maxon::Float | Input | false | false | false |  |  | 42.6 | 
Inputs/Legacy_globalscale_world | <com.redshift3d.redshift4c4d.nodes.core.maxonnoise.legacy_globalscale_world | maxon::Float | Input | false | false | false |  |  | 0.1 | 
Inputs/Output/Brightness | <com.redshift3d.redshift4c4d.nodes.core.maxonnoise.brightness | maxon::Float | Input | false | false | false | -1 | 1 | 0 | 
Inputs/Output/Contrast | <com.redshift3d.redshift4c4d.nodes.core.maxonnoise.contrast | maxon::Float | Input | false | false | false | -1 | 1 | 0 | 
Inputs/Output/Cycles | <com.redshift3d.redshift4c4d.nodes.core.maxonnoise.cycles | maxon::Float | Input | false | false | false |  |  | 0 | 
Inputs/Output/High Clip | <com.redshift3d.redshift4c4d.nodes.core.maxonnoise.high_clip | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Inputs/Output/Low Clip | <com.redshift3d.redshift4c4d.nodes.core.maxonnoise.low_clip | maxon::Float | Input | false | false | false | 0 | 1 | 0 | 
Outputs/outColor | >com.redshift3d.redshift4c4d.nodes.core.maxonnoise.outcolor | maxon::Color64 | Output | false | false | false |  |  | (0,0,0) | 

