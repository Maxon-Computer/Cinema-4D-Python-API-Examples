# Node Template: Sprite

- **Node Space ID:** `com.redshift3d.redshift4c4d.class.nodespace`
- **Template ID:** `com.redshift3d.redshift4c4d.nodes.core.sprite`
- **Template Name:** `Sprite`

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
Node Category | net.maxon.node.base.category | maxon::InternedId | Attribute | false | false | true |  |  | primitives | operators = operators, distributions = distributions, geometries = geometries, patterns = patterns, primitives = primitives, effectors = effectors, fields = fields, functions = functions, structures = structures, geomodifiers = geomodifiers, geogenerators = geogenerators
Preview/Node | net.maxon.node.base.nodepreviewimage | maxon::ImageBaseRef | Attribute | false | false | false |  |  |  | 
Inputs/Shader Input/Shader | <com.redshift3d.redshift4c4d.nodes.core.sprite.input | maxon::ColorA64 | Input | false | false | false |  |  |  | 
Inputs/Stencil/Custom Gamma | <com.redshift3d.redshift4c4d.nodes.core.sprite.tex0_gamma | maxon::Float | Input | false | false | false |  |  | 1 | 
Inputs/Stencil/Image Name | <com.redshift3d.redshift4c4d.nodes.core.sprite.tex0 | com.redshift3d.redshift4c4d.portbundle.file | Input | false | true | false |  |  |  | 
Inputs/Stencil/Image Name/Animation | <com.redshift3d.redshift4c4d.nodes.core.sprite.tex0/animation | maxon::Int | Input | false | false | true |  |  |  | Off = 0, Simple = 1, Loop = 2, Ping-Pong = 3
Inputs/Stencil/Image Name/Color Space | <com.redshift3d.redshift4c4d.nodes.core.sprite.tex0/colorspace | maxon::String | Input | false | false | false |  |  |  | 
Inputs/Stencil/Image Name/Frame End | <com.redshift3d.redshift4c4d.nodes.core.sprite.tex0/frameend | maxon::Int | Input | false | false | false |  |  |  | 
Inputs/Stencil/Image Name/Frame Rate | <com.redshift3d.redshift4c4d.nodes.core.sprite.tex0/framerate | maxon::Int | Input | false | false | false |  |  | 30 | 
Inputs/Stencil/Image Name/Frame Start | <com.redshift3d.redshift4c4d.nodes.core.sprite.tex0/framestart | maxon::Int | Input | false | false | false |  |  |  | 
Inputs/Stencil/Image Name/Layer | <com.redshift3d.redshift4c4d.nodes.core.sprite.tex0/layerset | maxon::LayerSet | Input | false | false | false |  |  |  | 
Inputs/Stencil/Image Name/Loops | <com.redshift3d.redshift4c4d.nodes.core.sprite.tex0/loops | maxon::Int | Input | false | false | false |  |  |  | 
Inputs/Stencil/Image Name/Path | <com.redshift3d.redshift4c4d.nodes.core.sprite.tex0/path | maxon::Url | Input | false | false | false |  |  |  | 
Inputs/Stencil/Image Name/Range End | <com.redshift3d.redshift4c4d.nodes.core.sprite.tex0/rangeend | maxon::TimeValue | Input | false | false | false |  |  |  | 
Inputs/Stencil/Image Name/Range Start | <com.redshift3d.redshift4c4d.nodes.core.sprite.tex0/rangestart | maxon::TimeValue | Input | false | false | false |  |  |  | 
Inputs/Stencil/Image Name/Start Offset | <com.redshift3d.redshift4c4d.nodes.core.sprite.tex0/startoffset | maxon::Int | Input | false | false | false |  |  |  | 
Inputs/Stencil/Image Name/Timing | <com.redshift3d.redshift4c4d.nodes.core.sprite.tex0/timing | maxon::Int | Input | false | false | true |  |  |  | Frame = 0, Time = 1, Range = 2
Inputs/Stencil/Opacity Calculation | <com.redshift3d.redshift4c4d.nodes.core.sprite.mode | maxon::Int | Input | false | false | true |  |  | 0 | From Color Intensity = 0, From Alpha = 1
Inputs/Stencil/Stencil Opacity Threshold | <com.redshift3d.redshift4c4d.nodes.core.sprite.threshold | maxon::Float | Input | false | false | false | 0 | 1 | 0.5 | 
Inputs/Stencil/Stencil Shader | <com.redshift3d.redshift4c4d.nodes.core.sprite.bake_shader_input | maxon::Color64 | Input | false | false | false |  |  |  | 
Inputs/Stencil/Stencil Size | <com.redshift3d.redshift4c4d.nodes.core.sprite.bake_width | maxon::Int | Input | false | false | false | 2 | 16384 | 512 | 
Inputs/Stencil/Texture Repeats | <com.redshift3d.redshift4c4d.nodes.core.sprite.repeats | maxon::Vector2d64 | Input | false | false | false |  |  | (1,1) | 
Inputs/Stencil/UV Channel | <com.redshift3d.redshift4c4d.nodes.core.sprite.tspace_id | maxon::String | Input | false | false | false |  |  |  | 
Outputs/outColor | >com.redshift3d.redshift4c4d.nodes.core.sprite.outcolor | maxon::Color64 | Output | false | false | false |  |  | (0,0,0) | 

