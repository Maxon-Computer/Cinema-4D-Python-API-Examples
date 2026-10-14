# Node Template: Dome Light

- **Node Space ID:** `com.redshift3d.redshift4c4d.class.nodespace`
- **Template ID:** `com.redshift3d.redshift4c4d.nodes.core.light_dome`
- **Template Name:** `Dome Light`

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
Node Category | net.maxon.node.base.category | maxon::InternedId | Attribute | false | false | true |  |  | operators | distributions = distributions, operators = operators, geometries = geometries, patterns = patterns, primitives = primitives, effectors = effectors, fields = fields, functions = functions, structures = structures, geomodifiers = geomodifiers, geogenerators = geogenerators
Preview/Node | net.maxon.node.base.nodepreviewimage | maxon::ImageBaseRef | Attribute | false | false | false |  |  |  | 
Back-Plate/Apply Camera Exposure Compensation | <com.redshift3d.redshift4c4d.nodes.core.light_dome.applyexposurecompensation | maxon::Bool | Input | false | false | false |  |  | false | 
Back-Plate/Back-plate Aspect Ratio | <com.redshift3d.redshift4c4d.nodes.core.light_dome.backplateaspect | maxon::Int | Input | false | false | true |  |  | 0 | Texture = 0, Render = 1
Back-Plate/Enabled | <com.redshift3d.redshift4c4d.nodes.core.light_dome.backplateenabled | maxon::Bool | Input | false | false | false |  |  | false | 
Back-Plate/Gamma Override/Custom Gamma | <com.redshift3d.redshift4c4d.nodes.core.light_dome.tex1_gamma | maxon::Float | Input | false | false | false |  |  | 1 | 
Back-Plate/Map | <com.redshift3d.redshift4c4d.nodes.core.light_dome.tex1 | com.redshift3d.redshift4c4d.portbundle.file | Input | false | true | false |  |  |  | 
Back-Plate/Map/Animation | <com.redshift3d.redshift4c4d.nodes.core.light_dome.tex1/animation | maxon::Int | Input | false | false | true |  |  |  | Off = 0, Simple = 1, Loop = 2, Ping-Pong = 3
Back-Plate/Map/Color Space | <com.redshift3d.redshift4c4d.nodes.core.light_dome.tex1/colorspace | maxon::String | Input | false | false | false |  |  |  | 
Back-Plate/Map/Frame End | <com.redshift3d.redshift4c4d.nodes.core.light_dome.tex1/frameend | maxon::Int | Input | false | false | false |  |  |  | 
Back-Plate/Map/Frame Rate | <com.redshift3d.redshift4c4d.nodes.core.light_dome.tex1/framerate | maxon::Int | Input | false | false | false |  |  | 30 | 
Back-Plate/Map/Frame Start | <com.redshift3d.redshift4c4d.nodes.core.light_dome.tex1/framestart | maxon::Int | Input | false | false | false |  |  |  | 
Back-Plate/Map/Layer | <com.redshift3d.redshift4c4d.nodes.core.light_dome.tex1/layerset | maxon::LayerSet | Input | false | false | false |  |  |  | 
Back-Plate/Map/Loops | <com.redshift3d.redshift4c4d.nodes.core.light_dome.tex1/loops | maxon::Int | Input | false | false | false |  |  |  | 
Back-Plate/Map/Path | <com.redshift3d.redshift4c4d.nodes.core.light_dome.tex1/path | maxon::Url | Input | false | false | false |  |  |  | 
Back-Plate/Map/Range End | <com.redshift3d.redshift4c4d.nodes.core.light_dome.tex1/rangeend | maxon::TimeValue | Input | false | false | false |  |  |  | 
Back-Plate/Map/Range Start | <com.redshift3d.redshift4c4d.nodes.core.light_dome.tex1/rangestart | maxon::TimeValue | Input | false | false | false |  |  |  | 
Back-Plate/Map/Start Offset | <com.redshift3d.redshift4c4d.nodes.core.light_dome.tex1/startoffset | maxon::Int | Input | false | false | false |  |  |  | 
Back-Plate/Map/Timing | <com.redshift3d.redshift4c4d.nodes.core.light_dome.tex1/timing | maxon::Int | Input | false | false | true |  |  |  | Time = 1, Frame = 0, Range = 2
General/Custom Gamma | <com.redshift3d.redshift4c4d.nodes.core.light_dome.tex0_gamma | maxon::Float | Input | false | false | false |  |  | 1 | 
General/Dome Map | <com.redshift3d.redshift4c4d.nodes.core.light_dome.tex0 | com.redshift3d.redshift4c4d.portbundle.file | Input | false | true | false |  |  |  | 
General/Dome Map/Animation | <com.redshift3d.redshift4c4d.nodes.core.light_dome.tex0/animation | maxon::Int | Input | false | false | true |  |  |  | Off = 0, Simple = 1, Loop = 2, Ping-Pong = 3
General/Dome Map/Color Space | <com.redshift3d.redshift4c4d.nodes.core.light_dome.tex0/colorspace | maxon::String | Input | false | false | false |  |  |  | 
General/Dome Map/Frame End | <com.redshift3d.redshift4c4d.nodes.core.light_dome.tex0/frameend | maxon::Int | Input | false | false | false |  |  |  | 
General/Dome Map/Frame Rate | <com.redshift3d.redshift4c4d.nodes.core.light_dome.tex0/framerate | maxon::Int | Input | false | false | false |  |  | 30 | 
General/Dome Map/Frame Start | <com.redshift3d.redshift4c4d.nodes.core.light_dome.tex0/framestart | maxon::Int | Input | false | false | false |  |  |  | 
General/Dome Map/Layer | <com.redshift3d.redshift4c4d.nodes.core.light_dome.tex0/layerset | maxon::LayerSet | Input | false | false | false |  |  |  | 
General/Dome Map/Loops | <com.redshift3d.redshift4c4d.nodes.core.light_dome.tex0/loops | maxon::Int | Input | false | false | false |  |  |  | 
General/Dome Map/Path | <com.redshift3d.redshift4c4d.nodes.core.light_dome.tex0/path | maxon::Url | Input | false | false | false |  |  |  | 
General/Dome Map/Range End | <com.redshift3d.redshift4c4d.nodes.core.light_dome.tex0/rangeend | maxon::TimeValue | Input | false | false | false |  |  |  | 
General/Dome Map/Range Start | <com.redshift3d.redshift4c4d.nodes.core.light_dome.tex0/rangestart | maxon::TimeValue | Input | false | false | false |  |  |  | 
General/Dome Map/Start Offset | <com.redshift3d.redshift4c4d.nodes.core.light_dome.tex0/startoffset | maxon::Int | Input | false | false | false |  |  |  | 
General/Dome Map/Timing | <com.redshift3d.redshift4c4d.nodes.core.light_dome.tex0/timing | maxon::Int | Input | false | false | true |  |  |  | Time = 1, Frame = 0, Range = 2
General/Environment Alpha Channel Replace/Alpha | <com.redshift3d.redshift4c4d.nodes.core.light_dome.alphareplacevalue | maxon::Float | Input | false | false | false |  |  | 0 | 
General/Environment Alpha Channel Replace/Enable | <com.redshift3d.redshift4c4d.nodes.core.light_dome.alphareplaceenable | maxon::Bool | Input | false | false | false |  |  | false | 
General/Intensity Multiplier | <com.redshift3d.redshift4c4d.nodes.core.light_dome.multiplier | maxon::Float | Input | false | false | false |  |  | 1 | 
General/Map Source | <com.redshift3d.redshift4c4d.nodes.core.light_dome.mapsource | maxon::Int | Input | false | false | true |  |  | 0 | Texture = 0, Shader = 1
General/Map Type | <com.redshift3d.redshift4c4d.nodes.core.light_dome.envtype | maxon::Int | Input | false | false | true |  |  | 0 | Spherical = 0, Hemispherical = 1, Mirror Ball = 2, Angular = 3
General/On | <com.redshift3d.redshift4c4d.nodes.core.light_dome.on | maxon::Bool | Input | false | false | false |  |  | true | 
General/Shader | <com.redshift3d.redshift4c4d.nodes.core.light_dome.mapshader | maxon::Color64 | Input | false | false | false |  |  |  | 
General/Shadow/Enable | <com.redshift3d.redshift4c4d.nodes.core.light_dome.shadow | maxon::Bool | Input | false | false | false |  |  | true | 
General/Shadow/Transparency | <com.redshift3d.redshift4c4d.nodes.core.light_dome.shadowtransparency | maxon::Float | Input | false | false | false | 0 | 1 | 0 | 
General/Tint | <com.redshift3d.redshift4c4d.nodes.core.light_dome.color | maxon::Color64 | Input | false | false | false |  |  | (1,1,1) | 
Outputs/lightColor_shadowAmount | >com.redshift3d.redshift4c4d.nodes.core.light_dome.lightcolor_shadowamount | maxon::ColorA64 | Output | false | false | false |  |  | (0,0,0,1) | 

