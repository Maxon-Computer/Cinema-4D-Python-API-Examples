# Node Template: Texture

- **Node Space ID:** `com.redshift3d.redshift4c4d.class.nodespace`
- **Template ID:** `com.redshift3d.redshift4c4d.nodes.core.texturesampler`
- **Template Name:** `Texture`

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
Adjust/Alpha Is Luminance | <com.redshift3d.redshift4c4d.nodes.core.texturesampler.alpha_is_luminance | maxon::Bool | Input | false | false | false |  |  | false | 
Adjust/Alpha Multiplier | <com.redshift3d.redshift4c4d.nodes.core.texturesampler.alpha_multiplier | maxon::Float | Input | false | false | false |  |  | 1 | 
Adjust/Alpha Offset | <com.redshift3d.redshift4c4d.nodes.core.texturesampler.alpha_offset | maxon::Float | Input | false | false | false |  |  | 0 | 
Adjust/Color Multiplier | <com.redshift3d.redshift4c4d.nodes.core.texturesampler.color_multiplier | maxon::Color64 | Input | false | false | false |  |  | (1,1,1) | 
Adjust/Color Offset | <com.redshift3d.redshift4c4d.nodes.core.texturesampler.color_offset | maxon::Color64 | Input | false | false | false |  |  | (0,0,0) | 
Adjust/Default/Invalid Color | <com.redshift3d.redshift4c4d.nodes.core.texturesampler.invalid_color | maxon::ColorA64 | Input | false | false | false |  |  | (0,0,0,0) | 
Advanced/Bicubic Filtering | <com.redshift3d.redshift4c4d.nodes.core.texturesampler.filter_bicubic | maxon::Bool | Input | false | false | false |  |  | false | 
Advanced/Filter Enable | <com.redshift3d.redshift4c4d.nodes.core.texturesampler.filter_enable_type | maxon::Int | Input | false | false | true |  |  | 2 | Magnification/Minification = 2, None = 0, Magnification = 1
Advanced/Mip Bias | <com.redshift3d.redshift4c4d.nodes.core.texturesampler.mip_bias | maxon::Float | Input | false | false | false | -32 | 32 | 0 | 
Advanced/Override UVs For Tone-Mapping | <com.redshift3d.redshift4c4d.nodes.core.texturesampler.tone_map_enable | maxon::Bool | Input | false | false | false |  |  | false | 
Advanced/Prefer Sharp Filtering | <com.redshift3d.redshift4c4d.nodes.core.texturesampler.prefer_sharp | maxon::Bool | Input | false | false | false |  |  | true | 
General/Image/Custom Gamma | <com.redshift3d.redshift4c4d.nodes.core.texturesampler.tex0_gamma | maxon::Float | Input | false | false | false |  |  | 1 | 
General/Image/Filename | <com.redshift3d.redshift4c4d.nodes.core.texturesampler.tex0 | com.redshift3d.redshift4c4d.portbundle.file | Input | false | true | false |  |  |  | 
General/Image/Filename/Animation | <com.redshift3d.redshift4c4d.nodes.core.texturesampler.tex0/animation | maxon::Int | Input | false | false | true |  |  |  | Off = 0, Simple = 1, Loop = 2, Ping-Pong = 3
General/Image/Filename/Color Space | <com.redshift3d.redshift4c4d.nodes.core.texturesampler.tex0/colorspace | maxon::String | Input | false | false | false |  |  |  | 
General/Image/Filename/Frame End | <com.redshift3d.redshift4c4d.nodes.core.texturesampler.tex0/frameend | maxon::Int | Input | false | false | false |  |  |  | 
General/Image/Filename/Frame Rate | <com.redshift3d.redshift4c4d.nodes.core.texturesampler.tex0/framerate | maxon::Int | Input | false | false | false |  |  | 30 | 
General/Image/Filename/Frame Start | <com.redshift3d.redshift4c4d.nodes.core.texturesampler.tex0/framestart | maxon::Int | Input | false | false | false |  |  |  | 
General/Image/Filename/Layer | <com.redshift3d.redshift4c4d.nodes.core.texturesampler.tex0/layerset | maxon::LayerSet | Input | false | false | false |  |  |  | 
General/Image/Filename/Loops | <com.redshift3d.redshift4c4d.nodes.core.texturesampler.tex0/loops | maxon::Int | Input | false | false | false |  |  |  | 
General/Image/Filename/Path | <com.redshift3d.redshift4c4d.nodes.core.texturesampler.tex0/path | maxon::Url | Input | false | false | false |  |  |  | 
General/Image/Filename/Range End | <com.redshift3d.redshift4c4d.nodes.core.texturesampler.tex0/rangeend | maxon::TimeValue | Input | false | false | false |  |  |  | 
General/Image/Filename/Range Start | <com.redshift3d.redshift4c4d.nodes.core.texturesampler.tex0/rangestart | maxon::TimeValue | Input | false | false | false |  |  |  | 
General/Image/Filename/Start Offset | <com.redshift3d.redshift4c4d.nodes.core.texturesampler.tex0/startoffset | maxon::Int | Input | false | false | false |  |  |  | 
General/Image/Filename/Timing | <com.redshift3d.redshift4c4d.nodes.core.texturesampler.tex0/timing | maxon::Int | Input | false | false | true |  |  |  | Frame = 0, Time = 1, Range = 2
General/UV/Mirror U | <com.redshift3d.redshift4c4d.nodes.core.texturesampler.mirroru | maxon::Bool | Input | false | false | false |  |  | false | 
General/UV/Mirror V | <com.redshift3d.redshift4c4d.nodes.core.texturesampler.mirrorv | maxon::Bool | Input | false | false | false |  |  | false | 
General/UV/Remap/Offset | <com.redshift3d.redshift4c4d.nodes.core.texturesampler.offset | maxon::Vector2d64 | Input | false | false | false |  |  | (0,0) | 
General/UV/Remap/Rotate | <com.redshift3d.redshift4c4d.nodes.core.texturesampler.rotate | maxon::Float | Input | false | false | false | 0 | 360 | 0 | 
General/UV/Remap/Scale | <com.redshift3d.redshift4c4d.nodes.core.texturesampler.scale | maxon::Vector2d64 | Input | false | false | false |  |  | (1,1) | 
General/UV/Remap/UV Context | <com.redshift3d.redshift4c4d.nodes.core.texturesampler.uv_context | RSC4D::UVContext | Input | false | false | false |  |  |  | 
General/UV/UV Channel | <com.redshift3d.redshift4c4d.nodes.core.texturesampler.tspace_id | maxon::String | Input | false | false | false |  |  |  | 
General/UV/Wrap U | <com.redshift3d.redshift4c4d.nodes.core.texturesampler.wrapu | maxon::Bool | Input | false | false | false |  |  | true | 
General/UV/Wrap V | <com.redshift3d.redshift4c4d.nodes.core.texturesampler.wrapv | maxon::Bool | Input | false | false | false |  |  | true | 
Outputs/outColor | >com.redshift3d.redshift4c4d.nodes.core.texturesampler.outcolor | maxon::ColorA64 | Output | false | false | false |  |  | (0,0,0,1) | 

