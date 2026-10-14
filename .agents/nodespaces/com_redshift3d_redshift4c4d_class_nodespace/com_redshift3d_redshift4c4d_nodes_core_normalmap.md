# Node Template: Normal Map

- **Node Space ID:** `com.redshift3d.redshift4c4d.class.nodespace`
- **Template ID:** `com.redshift3d.redshift4c4d.nodes.core.normalmap`
- **Template Name:** `Normal Map`

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
Advanced/Alternate/U | <com.redshift3d.redshift4c4d.nodes.core.normalmap.alt_x | maxon::Bool | Input | false | false | false |  |  | false | 
Advanced/Alternate/V | <com.redshift3d.redshift4c4d.nodes.core.normalmap.alt_y | maxon::Bool | Input | false | false | false |  |  | false | 
Advanced/Elliptical Filtering/Maximum Eccentricity | <com.redshift3d.redshift4c4d.nodes.core.normalmap.eccmax | maxon::Float | Input | false | false | false | 1 | 32 | 8 | 
Advanced/Legacy Normal Map Technique | <com.redshift3d.redshift4c4d.nodes.core.normalmap.legacynormalmap | maxon::Bool | Input | false | false | false |  |  | false | 
Advanced/Repeats/Texture Repeats | <com.redshift3d.redshift4c4d.nodes.core.normalmap.repeats | maxon::Vector2d64 | Input | false | false | false |  |  | (1,1) | 
Advanced/Repeats/Wrap U | <com.redshift3d.redshift4c4d.nodes.core.normalmap.wrapu | maxon::Bool | Input | false | false | false |  |  | true | 
Advanced/Repeats/Wrap V | <com.redshift3d.redshift4c4d.nodes.core.normalmap.wrapv | maxon::Bool | Input | false | false | false |  |  | true | 
Advanced/UV Remap/Maximum | <com.redshift3d.redshift4c4d.nodes.core.normalmap.max_uv | maxon::Vector2d64 | Input | false | false | false |  |  | (1,1) | 
Advanced/UV Remap/Minimum | <com.redshift3d.redshift4c4d.nodes.core.normalmap.min_uv | maxon::Vector2d64 | Input | false | false | false |  |  | (0,0) | 
General/Tangents/Tangents | <com.redshift3d.redshift4c4d.nodes.core.normalmap.tangents | maxon::String | Input | false | false | false |  |  |  | 
General/Texture/Flip Normal Y | <com.redshift3d.redshift4c4d.nodes.core.normalmap.flipy | maxon::Bool | Input | false | false | false |  |  | false | 
General/Texture/Map | <com.redshift3d.redshift4c4d.nodes.core.normalmap.tex0 | com.redshift3d.redshift4c4d.portbundle.file | Input | false | true | false |  |  |  | 
General/Texture/Map/Animation | <com.redshift3d.redshift4c4d.nodes.core.normalmap.tex0/animation | maxon::Int | Input | false | false | true |  |  |  | Off = 0, Simple = 1, Loop = 2, Ping-Pong = 3
General/Texture/Map/Color Space | <com.redshift3d.redshift4c4d.nodes.core.normalmap.tex0/colorspace | maxon::String | Input | false | false | false |  |  |  | 
General/Texture/Map/Frame End | <com.redshift3d.redshift4c4d.nodes.core.normalmap.tex0/frameend | maxon::Int | Input | false | false | false |  |  |  | 
General/Texture/Map/Frame Rate | <com.redshift3d.redshift4c4d.nodes.core.normalmap.tex0/framerate | maxon::Int | Input | false | false | false |  |  | 30 | 
General/Texture/Map/Frame Start | <com.redshift3d.redshift4c4d.nodes.core.normalmap.tex0/framestart | maxon::Int | Input | false | false | false |  |  |  | 
General/Texture/Map/Layer | <com.redshift3d.redshift4c4d.nodes.core.normalmap.tex0/layerset | maxon::LayerSet | Input | false | false | false |  |  |  | 
General/Texture/Map/Loops | <com.redshift3d.redshift4c4d.nodes.core.normalmap.tex0/loops | maxon::Int | Input | false | false | false |  |  |  | 
General/Texture/Map/Path | <com.redshift3d.redshift4c4d.nodes.core.normalmap.tex0/path | maxon::Url | Input | false | false | false |  |  |  | 
General/Texture/Map/Range End | <com.redshift3d.redshift4c4d.nodes.core.normalmap.tex0/rangeend | maxon::TimeValue | Input | false | false | false |  |  |  | 
General/Texture/Map/Range Start | <com.redshift3d.redshift4c4d.nodes.core.normalmap.tex0/rangestart | maxon::TimeValue | Input | false | false | false |  |  |  | 
General/Texture/Map/Start Offset | <com.redshift3d.redshift4c4d.nodes.core.normalmap.tex0/startoffset | maxon::Int | Input | false | false | false |  |  |  | 
General/Texture/Map/Timing | <com.redshift3d.redshift4c4d.nodes.core.normalmap.tex0/timing | maxon::Int | Input | false | false | true |  |  |  | Time = 1, Frame = 0, Range = 2
General/Texture/Scale Normal | <com.redshift3d.redshift4c4d.nodes.core.normalmap.scale | maxon::Float | Input | false | false | false |  |  | 1 | 
General/Texture/Texture Space | <com.redshift3d.redshift4c4d.nodes.core.normalmap.tspace_id | maxon::String | Input | false | false | false |  |  |  | 
General/Texture/Unbiased Normals | <com.redshift3d.redshift4c4d.nodes.core.normalmap.unbiasednormalmap | maxon::Bool | Input | false | false | false |  |  | false | 
Outputs/outDisplacementVector | >com.redshift3d.redshift4c4d.nodes.core.normalmap.outdisplacementvector | maxon::Vector64 | Output | false | false | false |  |  | (0,0,0) | 

