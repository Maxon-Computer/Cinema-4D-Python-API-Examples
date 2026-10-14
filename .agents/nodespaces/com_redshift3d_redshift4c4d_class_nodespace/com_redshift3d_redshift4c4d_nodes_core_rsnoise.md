# Node Template: Noise

- **Node Space ID:** `com.redshift3d.redshift4c4d.class.nodespace`
- **Template ID:** `com.redshift3d.redshift4c4d.nodes.core.rsnoise`
- **Template Name:** `Noise`

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
Color/General/Color 1 | <com.redshift3d.redshift4c4d.nodes.core.rsnoise.color1 | maxon::ColorA64 | Input | false | false | false |  |  | (0,0,0,1) | 
Color/General/Color 2 | <com.redshift3d.redshift4c4d.nodes.core.rsnoise.color2 | maxon::ColorA64 | Input | false | false | false |  |  | (1,1,1,1) | 
Color/General/Invert | <com.redshift3d.redshift4c4d.nodes.core.rsnoise.color_invert | maxon::Bool | Input | false | false | false |  |  | false | 
Color/Remap/Bias | <com.redshift3d.redshift4c4d.nodes.core.rsnoise.range_bias | maxon::Float | Input | false | false | false | 0 | 1 | 0.5 | 
Color/Remap/Max | <com.redshift3d.redshift4c4d.nodes.core.rsnoise.range_max | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Color/Remap/Min | <com.redshift3d.redshift4c4d.nodes.core.rsnoise.range_min | maxon::Float | Input | false | false | false |  |  | 0 | 
Coordinates/General/Offset | <com.redshift3d.redshift4c4d.nodes.core.rsnoise.coord_offset | maxon::Vector64 | Input | false | false | false |  |  | (0,0,0) | 
Coordinates/General/Overall Scale | <com.redshift3d.redshift4c4d.nodes.core.rsnoise.coord_scale_global | maxon::Float | Input | false | false | false |  |  | 0.1 | 
Coordinates/General/Scale | <com.redshift3d.redshift4c4d.nodes.core.rsnoise.coord_scale | maxon::Vector64 | Input | false | false | false |  |  | (4,4,4) | 
Coordinates/General/Source | <com.redshift3d.redshift4c4d.nodes.core.rsnoise.coord_source | maxon::Int | Input | false | false | true |  |  | 0 | Object Position = 0, Vertex Attribute = 1
Coordinates/General/Vertex Attribute Name | <com.redshift3d.redshift4c4d.nodes.core.rsnoise.coord_attribute | maxon::String | Input | false | false | false |  |  |  | 
Noise/General/Fractal/Turbulence/Amplitude Gain | <com.redshift3d.redshift4c4d.nodes.core.rsnoise.noise_gain | maxon::Float | Input | false | false | false |  |  | 2 | 
Noise/General/Fractal/Turbulence/Complexity | <com.redshift3d.redshift4c4d.nodes.core.rsnoise.noise_complexity | maxon::Int | Input | false | false | false | 0 | 32 | 3 | 
Noise/General/Fractal/Turbulence/Distortion | <com.redshift3d.redshift4c4d.nodes.core.rsnoise.distort | maxon::Float | Input | false | false | false |  |  | 0 | 
Noise/General/Fractal/Turbulence/Distortion Scale | <com.redshift3d.redshift4c4d.nodes.core.rsnoise.distort_scale | maxon::Float | Input | false | false | false |  |  | 0 | 
Noise/General/Fractal/Turbulence/Frequency Scale | <com.redshift3d.redshift4c4d.nodes.core.rsnoise.noise_scale | maxon::Float | Input | false | false | false |  |  | 2 | 
Noise/General/Fractal/Turbulence/Time/Constant Scale | <com.redshift3d.redshift4c4d.nodes.core.rsnoise.time_constant | maxon::Float | Input | false | false | false |  |  | 1 | 
Noise/General/Fractal/Turbulence/Time/Source | <com.redshift3d.redshift4c4d.nodes.core.rsnoise.time_source | maxon::Int | Input | false | false | true |  |  | 0 | None = 0, Constant = 1, User = 2
Noise/General/Fractal/Turbulence/Time/User Time | <com.redshift3d.redshift4c4d.nodes.core.rsnoise.time | maxon::Float | Input | false | false | false |  |  | 0 | 
Noise/General/Noise Type | <com.redshift3d.redshift4c4d.nodes.core.rsnoise.noise_type | maxon::Int | Input | false | false | true |  |  | 2 | Fractal = 2, Turbulence = 3, Cell = 0
Outputs/outColor | >com.redshift3d.redshift4c4d.nodes.core.rsnoise.outcolor | maxon::ColorA64 | Output | false | false | false |  |  | (0,0,0,1) | 

