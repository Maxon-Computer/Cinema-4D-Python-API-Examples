# Node Template: Image

- **Node Space ID:** `net.maxon.nodespace.standard`
- **Template ID:** `net.maxon.pattern.node.generator.image`
- **Template Name:** `Image`

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
Context/Context | <context | maxon::ShadingContext | Input | false | false | false |  |  |  | 
Inputs/Across tiles | <sampleacrosstiles | maxon::Bool | Input | false | false | false |  |  | false | 
Inputs/Alpha | <alpha | maxon::InternedId | Input | false | false | true |  |  | straight | None = none, Premultiplied = premultiplied, Premultiplied (Image Color Space) = premultipliedcolorspace, Straight = straight
Inputs/Animation/Movie Time | <movietime | maxon::TimeValue | Input | false | false | false |  |  |  | 
Inputs/Animation/Playback End | <playbackend | maxon::TimeValue | Input | false | false | false |  |  | 100000000.0 ms | 
Inputs/Animation/Playback Mode | <playbackmode | maxon::InternedId | Input | false | false | true |  |  | loop | Once = once, Loop = loop, Ping-Pong = pingpong
Inputs/Animation/Playback Start | <playbackstart | maxon::TimeValue | Input | false | false | false |  |  |  | 
Inputs/Blur | <blur | maxon::Float | Input | false | false | false |  | 1 | 0 | 
Inputs/Default Color | <defaultcolor | maxon::ColorA | Input | false | false | false |  |  |  | 
Inputs/File | <url | maxon::Url | Input | false | false | false |  |  |  | 
Inputs/Image Sequence/End Frame | <frameend | maxon::Int | Input | false | false | false |  |  |  | 
Inputs/Image Sequence/Frame Rate | <framerate | maxon::Float | Input | false | false | false |  |  | 30 | 
Inputs/Image Sequence/Start Frame | <framestart | maxon::Int | Input | false | false | false |  |  |  | 
Inputs/Interpolation | <interpolation | maxon::InternedId | Input | false | false | true |  |  | rip | RIP = rip, MIP = mip, SAT = sat, Bicubic = bicubic, Linear = linear, None = none
Inputs/Layer Set | <layerset | maxon::LayerSet | Input | false | false | false |  |  |  | 
Inputs/Mode | <mode | maxon::InternedId | Input | false | false | true |  |  | default | Force 32 Bit = force32bit, Default = default, Raw (Ignore Color Profile) = raw
Outputs/Image Height | >height | maxon::Float | Output | false | false | false |  |  |  | 
Outputs/Image Width | >width | maxon::Float | Output | false | false | false |  |  |  | 
Outputs/Movie FPS | >fps | maxon::Float | Output | false | false | false |  |  |  | 
Outputs/Movie Length | >length | maxon::TimeValue | Output | false | false | false |  |  |  | 
Outputs/Result | >result | maxon::ColorA | Output | false | false | false |  |  |  | 

