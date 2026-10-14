# Node Template: Camera Map

- **Node Space ID:** `com.redshift3d.redshift4c4d.class.nodespace`
- **Template ID:** `com.redshift3d.redshift4c4d.nodes.core.cameramap`
- **Template Name:** `Camera Map`

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
Inputs/Camera/Camera Picker | <com.redshift3d.redshift4c4d.nodes.core.cameramap.camerapicker | maxon::Uuid | Input | false | false | false |  |  |  | 
Inputs/Image/Alpha Channel Replace/Alpha | <com.redshift3d.redshift4c4d.nodes.core.cameramap.alphareplacevalue | maxon::Float | Input | false | false | false |  |  | 0 | 
Inputs/Image/Alpha Channel Replace/Enable | <com.redshift3d.redshift4c4d.nodes.core.cameramap.alphareplaceenable | maxon::Bool | Input | false | false | false |  |  | false | 
Inputs/Image/Custom Gamma | <com.redshift3d.redshift4c4d.nodes.core.cameramap.tex0_gamma | maxon::Float | Input | false | false | false |  |  | 1 | 
Inputs/Image/Map | <com.redshift3d.redshift4c4d.nodes.core.cameramap.tex0 | com.redshift3d.redshift4c4d.portbundle.file | Input | false | true | false |  |  |  | 
Inputs/Image/Map/Animation | <com.redshift3d.redshift4c4d.nodes.core.cameramap.tex0/animation | maxon::Int | Input | false | false | true |  |  |  | Off = 0, Simple = 1, Loop = 2, Ping-Pong = 3
Inputs/Image/Map/Color Space | <com.redshift3d.redshift4c4d.nodes.core.cameramap.tex0/colorspace | maxon::String | Input | false | false | false |  |  |  | 
Inputs/Image/Map/Frame End | <com.redshift3d.redshift4c4d.nodes.core.cameramap.tex0/frameend | maxon::Int | Input | false | false | false |  |  |  | 
Inputs/Image/Map/Frame Rate | <com.redshift3d.redshift4c4d.nodes.core.cameramap.tex0/framerate | maxon::Int | Input | false | false | false |  |  | 30 | 
Inputs/Image/Map/Frame Start | <com.redshift3d.redshift4c4d.nodes.core.cameramap.tex0/framestart | maxon::Int | Input | false | false | false |  |  |  | 
Inputs/Image/Map/Layer | <com.redshift3d.redshift4c4d.nodes.core.cameramap.tex0/layerset | maxon::LayerSet | Input | false | false | false |  |  |  | 
Inputs/Image/Map/Loops | <com.redshift3d.redshift4c4d.nodes.core.cameramap.tex0/loops | maxon::Int | Input | false | false | false |  |  |  | 
Inputs/Image/Map/Path | <com.redshift3d.redshift4c4d.nodes.core.cameramap.tex0/path | maxon::Url | Input | false | false | false |  |  |  | 
Inputs/Image/Map/Range End | <com.redshift3d.redshift4c4d.nodes.core.cameramap.tex0/rangeend | maxon::TimeValue | Input | false | false | false |  |  |  | 
Inputs/Image/Map/Range Start | <com.redshift3d.redshift4c4d.nodes.core.cameramap.tex0/rangestart | maxon::TimeValue | Input | false | false | false |  |  |  | 
Inputs/Image/Map/Start Offset | <com.redshift3d.redshift4c4d.nodes.core.cameramap.tex0/startoffset | maxon::Int | Input | false | false | false |  |  |  | 
Inputs/Image/Map/Timing | <com.redshift3d.redshift4c4d.nodes.core.cameramap.tex0/timing | maxon::Int | Input | false | false | true |  |  |  | Time = 1, Frame = 0, Range = 2
Inputs/Image/Scaling/Apply Camera Exposure Compensation | <com.redshift3d.redshift4c4d.nodes.core.cameramap.applyexposurecompensation | maxon::Bool | Input | false | false | false |  |  | false | 
Inputs/Image/Scaling/Aspect Ratio | <com.redshift3d.redshift4c4d.nodes.core.cameramap.backplateaspect | maxon::Int | Input | false | false | true |  |  | 0 | Texture = 0, Render = 1
Inputs/Image/Scaling/Match Render Size | <com.redshift3d.redshift4c4d.nodes.core.cameramap.per_pixel_match | maxon::Bool | Input | false | false | false |  |  | false | 
Inputs/Reflection/Offscreen/Off-screen Color | <com.redshift3d.redshift4c4d.nodes.core.cameramap.offscreen_color | maxon::ColorA64 | Input | false | false | false |  |  | (0,0,0,0) | 
Inputs/Reflection/Offscreen/Off-screen is Environment | <com.redshift3d.redshift4c4d.nodes.core.cameramap.offscreen_is_environment | maxon::Bool | Input | false | false | false |  |  | true | 
Inputs/Reflection/Offscreen/Reflection is Environment | <com.redshift3d.redshift4c4d.nodes.core.cameramap.reflection_is_environment | maxon::Bool | Input | false | false | false |  |  | false | 
Outputs/outColor | >com.redshift3d.redshift4c4d.nodes.core.cameramap.outcolor | maxon::ColorA64 | Output | false | false | false |  |  | (0,0,0,1) | 

