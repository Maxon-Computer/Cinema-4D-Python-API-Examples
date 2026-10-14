# Node Template: IES Light

- **Node Space ID:** `com.redshift3d.redshift4c4d.class.nodespace`
- **Template ID:** `com.redshift3d.redshift4c4d.nodes.core.light_ies`
- **Template Name:** `IES Light`

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
General/Color/Color | <com.redshift3d.redshift4c4d.nodes.core.light_ies.color | maxon::Color64 | Input | false | false | false |  |  | (1,1,1) | 
General/Color/Mode | <com.redshift3d.redshift4c4d.nodes.core.light_ies.colormode | maxon::Int | Input | false | false | true |  |  | 0 | Color = 0, Temperature = 1
General/Color/Temperature | <com.redshift3d.redshift4c4d.nodes.core.light_ies.temperature | maxon::Float | Input | false | false | false | 1000 | 20000 | 6500 | 
General/IES Profile | <com.redshift3d.redshift4c4d.nodes.core.light_ies.profile | com.redshift3d.redshift4c4d.portbundle.file | Input | false | true | false |  |  |  | 
General/IES Profile/Animation | <com.redshift3d.redshift4c4d.nodes.core.light_ies.profile/animation | maxon::Int | Input | false | false | true |  |  |  | Off = 0, Simple = 1, Loop = 2, Ping-Pong = 3
General/IES Profile/Color Space | <com.redshift3d.redshift4c4d.nodes.core.light_ies.profile/colorspace | maxon::String | Input | false | false | false |  |  |  | 
General/IES Profile/Frame End | <com.redshift3d.redshift4c4d.nodes.core.light_ies.profile/frameend | maxon::Int | Input | false | false | false |  |  |  | 
General/IES Profile/Frame Rate | <com.redshift3d.redshift4c4d.nodes.core.light_ies.profile/framerate | maxon::Int | Input | false | false | false |  |  | 30 | 
General/IES Profile/Frame Start | <com.redshift3d.redshift4c4d.nodes.core.light_ies.profile/framestart | maxon::Int | Input | false | false | false |  |  |  | 
General/IES Profile/Layer | <com.redshift3d.redshift4c4d.nodes.core.light_ies.profile/layerset | maxon::LayerSet | Input | false | false | false |  |  |  | 
General/IES Profile/Loops | <com.redshift3d.redshift4c4d.nodes.core.light_ies.profile/loops | maxon::Int | Input | false | false | false |  |  |  | 
General/IES Profile/Path | <com.redshift3d.redshift4c4d.nodes.core.light_ies.profile/path | maxon::Url | Input | false | false | false |  |  |  | 
General/IES Profile/Range End | <com.redshift3d.redshift4c4d.nodes.core.light_ies.profile/rangeend | maxon::TimeValue | Input | false | false | false |  |  |  | 
General/IES Profile/Range Start | <com.redshift3d.redshift4c4d.nodes.core.light_ies.profile/rangestart | maxon::TimeValue | Input | false | false | false |  |  |  | 
General/IES Profile/Start Offset | <com.redshift3d.redshift4c4d.nodes.core.light_ies.profile/startoffset | maxon::Int | Input | false | false | false |  |  |  | 
General/IES Profile/Timing | <com.redshift3d.redshift4c4d.nodes.core.light_ies.profile/timing | maxon::Int | Input | false | false | true |  |  |  | Time = 1, Frame = 0, Range = 2
General/Intensity/Exposure | <com.redshift3d.redshift4c4d.nodes.core.light_ies.exposure | maxon::Float | Input | false | false | false |  |  | 0 | 
General/Intensity/Intensity | <com.redshift3d.redshift4c4d.nodes.core.light_ies.overridevalue | maxon::Float | Input | false | false | false |  |  | 0 | 
General/Intensity/Intensity Multiplier | <com.redshift3d.redshift4c4d.nodes.core.light_ies.multiplier | maxon::Float | Input | false | false | false |  |  | 1 | 
General/Intensity/Mode | <com.redshift3d.redshift4c4d.nodes.core.light_ies.intensitymode | maxon::Int | Input | false | false | true |  |  | 0 | From IES File = 0, Override = 1
General/Intensity/Unit | <com.redshift3d.redshift4c4d.nodes.core.light_ies.overrideunit | maxon::Int | Input | false | false | true |  |  | 1 | Lumens (lm) = 1, Candelas (cd) = 5
General/On | <com.redshift3d.redshift4c4d.nodes.core.light_ies.on | maxon::Bool | Input | false | false | false |  |  | true | 
Shadow/Enable | <com.redshift3d.redshift4c4d.nodes.core.light_ies.shadow | maxon::Bool | Input | false | false | false |  |  | true | 
Shadow/Samples | <com.redshift3d.redshift4c4d.nodes.core.light_ies.samplingoverrides_numshadowsamples | maxon::Int | Input | false | false | false | 0 | 4096 | 8 | 
Shadow/Softness | <com.redshift3d.redshift4c4d.nodes.core.light_ies.samplingoverrides_shadowsamplesscale | maxon::Float | Input | false | false | false |  |  | 0 | 
Shadow/Transparency | <com.redshift3d.redshift4c4d.nodes.core.light_ies.shadowtransparency | maxon::Float | Input | false | false | false | 0 | 1 | 0 | 
Outputs/lightColor_shadowAmount | >com.redshift3d.redshift4c4d.nodes.core.light_ies.lightcolor_shadowamount | maxon::ColorA64 | Output | false | false | false |  |  | (0,0,0,1) | 

