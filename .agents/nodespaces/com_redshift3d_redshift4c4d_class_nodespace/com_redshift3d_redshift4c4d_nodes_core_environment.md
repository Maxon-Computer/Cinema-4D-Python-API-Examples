# Node Template: Environment

- **Node Space ID:** `com.redshift3d.redshift4c4d.class.nodespace`
- **Template ID:** `com.redshift3d.redshift4c4d.nodes.core.environment`
- **Template Name:** `Environment`

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
Back-Plate/Adjust Hue/Sat/Exp/Exposure | <com.redshift3d.redshift4c4d.nodes.core.environment.tex1_exp | maxon::Float | Input | false | false | false |  |  | 0 | 
Back-Plate/Adjust Hue/Sat/Exp/Hue | <com.redshift3d.redshift4c4d.nodes.core.environment.tex1_hue | maxon::Float | Input | false | false | false | 0 | 360 | 0 | 
Back-Plate/Adjust Hue/Sat/Exp/Saturation | <com.redshift3d.redshift4c4d.nodes.core.environment.tex1_sat | maxon::Float | Input | false | false | false | 0 | 1000 | 100 | 
Back-Plate/Apply Camera Exposure Compensation | <com.redshift3d.redshift4c4d.nodes.core.environment.applyexposurecompensation | maxon::Bool | Input | false | false | false |  |  | false | 
Back-Plate/Back-plate Aspect Ratio | <com.redshift3d.redshift4c4d.nodes.core.environment.backplateaspect | maxon::Int | Input | false | false | true |  |  | 0 | Texture = 0, Render = 1
Back-Plate/Custom Gamma | <com.redshift3d.redshift4c4d.nodes.core.environment.tex1_gamma | maxon::Float | Input | false | false | false |  |  | 1 | 
Back-Plate/Enabled | <com.redshift3d.redshift4c4d.nodes.core.environment.backplateenabled | maxon::Bool | Input | false | false | false |  |  | false | 
Back-Plate/Map | <com.redshift3d.redshift4c4d.nodes.core.environment.tex1 | com.redshift3d.redshift4c4d.portbundle.file | Input | false | true | false |  |  |  | 
Back-Plate/Map/Animation | <com.redshift3d.redshift4c4d.nodes.core.environment.tex1/animation | maxon::Int | Input | false | false | true |  |  |  | Off = 0, Simple = 1, Loop = 2, Ping-Pong = 3
Back-Plate/Map/Color Space | <com.redshift3d.redshift4c4d.nodes.core.environment.tex1/colorspace | maxon::String | Input | false | false | false |  |  |  | 
Back-Plate/Map/Frame End | <com.redshift3d.redshift4c4d.nodes.core.environment.tex1/frameend | maxon::Int | Input | false | false | false |  |  |  | 
Back-Plate/Map/Frame Rate | <com.redshift3d.redshift4c4d.nodes.core.environment.tex1/framerate | maxon::Int | Input | false | false | false |  |  | 30 | 
Back-Plate/Map/Frame Start | <com.redshift3d.redshift4c4d.nodes.core.environment.tex1/framestart | maxon::Int | Input | false | false | false |  |  |  | 
Back-Plate/Map/Layer | <com.redshift3d.redshift4c4d.nodes.core.environment.tex1/layerset | maxon::LayerSet | Input | false | false | false |  |  |  | 
Back-Plate/Map/Loops | <com.redshift3d.redshift4c4d.nodes.core.environment.tex1/loops | maxon::Int | Input | false | false | false |  |  |  | 
Back-Plate/Map/Path | <com.redshift3d.redshift4c4d.nodes.core.environment.tex1/path | maxon::Url | Input | false | false | false |  |  |  | 
Back-Plate/Map/Range End | <com.redshift3d.redshift4c4d.nodes.core.environment.tex1/rangeend | maxon::TimeValue | Input | false | false | false |  |  |  | 
Back-Plate/Map/Range Start | <com.redshift3d.redshift4c4d.nodes.core.environment.tex1/rangestart | maxon::TimeValue | Input | false | false | false |  |  |  | 
Back-Plate/Map/Start Offset | <com.redshift3d.redshift4c4d.nodes.core.environment.tex1/startoffset | maxon::Int | Input | false | false | false |  |  |  | 
Back-Plate/Map/Timing | <com.redshift3d.redshift4c4d.nodes.core.environment.tex1/timing | maxon::Int | Input | false | false | true |  |  |  | Time = 1, Frame = 0, Range = 2
General/Adjust/Alpha Channel Replace/Alpha | <com.redshift3d.redshift4c4d.nodes.core.environment.alphareplacevalue | maxon::Float | Input | false | false | false | 0 | 1 | 0 | 
General/Adjust/Alpha Channel Replace/Enable | <com.redshift3d.redshift4c4d.nodes.core.environment.alphareplaceenable | maxon::Bool | Input | false | false | false |  |  | false | 
General/Adjust/GI Affects Matte Objects | <com.redshift3d.redshift4c4d.nodes.core.environment.giaffectsmatteshadow | maxon::Bool | Input | false | false | false |  |  | false | 
General/Adjust/Ray Type Intensity Multipliers/Background/Refraction | <com.redshift3d.redshift4c4d.nodes.core.environment.background_intensity | maxon::Float | Input | false | false | false |  |  | 1 | 
General/Adjust/Ray Type Intensity Multipliers/GI | <com.redshift3d.redshift4c4d.nodes.core.environment.fg_intensity | maxon::Float | Input | false | false | false |  |  | 1 | 
General/Adjust/Ray Type Intensity Multipliers/Reflections | <com.redshift3d.redshift4c4d.nodes.core.environment.reflection_intensity | maxon::Float | Input | false | false | false |  |  | 1 | 
General/Adjust/Transform | <com.redshift3d.redshift4c4d.nodes.core.environment.placementmatrix | maxon::Matrix64 | Input | false | false | false |  |  | ((0,0,0),((0,0,1),(0,1,0),(-1,0,0))) | 
General/Projection Rotation/Rotation (X) | <com.redshift3d.redshift4c4d.nodes.core.environment.rotation_x | maxon::Float | Input | false | false | false | -360 | 360 | 0 | 
General/Projection Rotation/Rotation (Y) | <com.redshift3d.redshift4c4d.nodes.core.environment.rotation_y | maxon::Float | Input | false | false | false | -360 | 360 | 0 | 
General/Projection Rotation/Rotation (Z) | <com.redshift3d.redshift4c4d.nodes.core.environment.rotation_z | maxon::Float | Input | false | false | false | -360 | 360 | 0 | 
General/Texture/Adjust Hue/Sat/Exp/Exposure | <com.redshift3d.redshift4c4d.nodes.core.environment.tex0_exp | maxon::Float | Input | false | false | false |  |  | 0 | 
General/Texture/Adjust Hue/Sat/Exp/Hue | <com.redshift3d.redshift4c4d.nodes.core.environment.tex0_hue | maxon::Float | Input | false | false | false | 0 | 360 | 0 | 
General/Texture/Adjust Hue/Sat/Exp/Saturation | <com.redshift3d.redshift4c4d.nodes.core.environment.tex0_sat | maxon::Float | Input | false | false | false | 0 | 1000 | 100 | 
General/Texture/Custom Gamma | <com.redshift3d.redshift4c4d.nodes.core.environment.tex0_gamma | maxon::Float | Input | false | false | false |  |  | 1 | 
General/Texture/Map | <com.redshift3d.redshift4c4d.nodes.core.environment.tex0 | com.redshift3d.redshift4c4d.portbundle.file | Input | false | true | false |  |  |  | 
General/Texture/Map/Animation | <com.redshift3d.redshift4c4d.nodes.core.environment.tex0/animation | maxon::Int | Input | false | false | true |  |  |  | Off = 0, Simple = 1, Loop = 2, Ping-Pong = 3
General/Texture/Map/Color Space | <com.redshift3d.redshift4c4d.nodes.core.environment.tex0/colorspace | maxon::String | Input | false | false | false |  |  |  | 
General/Texture/Map/Frame End | <com.redshift3d.redshift4c4d.nodes.core.environment.tex0/frameend | maxon::Int | Input | false | false | false |  |  |  | 
General/Texture/Map/Frame Rate | <com.redshift3d.redshift4c4d.nodes.core.environment.tex0/framerate | maxon::Int | Input | false | false | false |  |  | 30 | 
General/Texture/Map/Frame Start | <com.redshift3d.redshift4c4d.nodes.core.environment.tex0/framestart | maxon::Int | Input | false | false | false |  |  |  | 
General/Texture/Map/Layer | <com.redshift3d.redshift4c4d.nodes.core.environment.tex0/layerset | maxon::LayerSet | Input | false | false | false |  |  |  | 
General/Texture/Map/Loops | <com.redshift3d.redshift4c4d.nodes.core.environment.tex0/loops | maxon::Int | Input | false | false | false |  |  |  | 
General/Texture/Map/Path | <com.redshift3d.redshift4c4d.nodes.core.environment.tex0/path | maxon::Url | Input | false | false | false |  |  |  | 
General/Texture/Map/Range End | <com.redshift3d.redshift4c4d.nodes.core.environment.tex0/rangeend | maxon::TimeValue | Input | false | false | false |  |  |  | 
General/Texture/Map/Range Start | <com.redshift3d.redshift4c4d.nodes.core.environment.tex0/rangestart | maxon::TimeValue | Input | false | false | false |  |  |  | 
General/Texture/Map/Start Offset | <com.redshift3d.redshift4c4d.nodes.core.environment.tex0/startoffset | maxon::Int | Input | false | false | false |  |  |  | 
General/Texture/Map/Timing | <com.redshift3d.redshift4c4d.nodes.core.environment.tex0/timing | maxon::Int | Input | false | false | true |  |  |  | Time = 1, Frame = 0, Range = 2
General/Texture/Projection Mode | <com.redshift3d.redshift4c4d.nodes.core.environment.mode | maxon::Int | Input | false | false | true |  |  | 0 | Spherical = 0, Cylindrical = 1, Cubic Strip = 2, Cube Cross Sideways = 3, Cube Cross = 4
General/Texture/Texture Mode | <com.redshift3d.redshift4c4d.nodes.core.environment.texmode | maxon::Int | Input | false | false | true |  |  | 0 | Default = 0, Ray Switch = 1
Ray Switch/Texture Background/Refraction/Adjust Hue/Sat/Exp/Exposure | <com.redshift3d.redshift4c4d.nodes.core.environment.tex2_exp | maxon::Float | Input | false | false | false |  |  | 0 | 
Ray Switch/Texture Background/Refraction/Adjust Hue/Sat/Exp/Hue | <com.redshift3d.redshift4c4d.nodes.core.environment.tex2_hue | maxon::Float | Input | false | false | false | 0 | 360 | 0 | 
Ray Switch/Texture Background/Refraction/Adjust Hue/Sat/Exp/Saturation | <com.redshift3d.redshift4c4d.nodes.core.environment.tex2_sat | maxon::Float | Input | false | false | false | 0 | 1000 | 100 | 
Ray Switch/Texture Background/Refraction/Custom Gamma | <com.redshift3d.redshift4c4d.nodes.core.environment.tex2_gamma | maxon::Float | Input | false | false | false |  |  | 1 | 
Ray Switch/Texture Background/Refraction/Map | <com.redshift3d.redshift4c4d.nodes.core.environment.tex2 | com.redshift3d.redshift4c4d.portbundle.file | Input | false | true | false |  |  |  | 
Ray Switch/Texture Background/Refraction/Map/Animation | <com.redshift3d.redshift4c4d.nodes.core.environment.tex2/animation | maxon::Int | Input | false | false | true |  |  |  | Off = 0, Simple = 1, Loop = 2, Ping-Pong = 3
Ray Switch/Texture Background/Refraction/Map/Color Space | <com.redshift3d.redshift4c4d.nodes.core.environment.tex2/colorspace | maxon::String | Input | false | false | false |  |  |  | 
Ray Switch/Texture Background/Refraction/Map/Frame End | <com.redshift3d.redshift4c4d.nodes.core.environment.tex2/frameend | maxon::Int | Input | false | false | false |  |  |  | 
Ray Switch/Texture Background/Refraction/Map/Frame Rate | <com.redshift3d.redshift4c4d.nodes.core.environment.tex2/framerate | maxon::Int | Input | false | false | false |  |  | 30 | 
Ray Switch/Texture Background/Refraction/Map/Frame Start | <com.redshift3d.redshift4c4d.nodes.core.environment.tex2/framestart | maxon::Int | Input | false | false | false |  |  |  | 
Ray Switch/Texture Background/Refraction/Map/Layer | <com.redshift3d.redshift4c4d.nodes.core.environment.tex2/layerset | maxon::LayerSet | Input | false | false | false |  |  |  | 
Ray Switch/Texture Background/Refraction/Map/Loops | <com.redshift3d.redshift4c4d.nodes.core.environment.tex2/loops | maxon::Int | Input | false | false | false |  |  |  | 
Ray Switch/Texture Background/Refraction/Map/Path | <com.redshift3d.redshift4c4d.nodes.core.environment.tex2/path | maxon::Url | Input | false | false | false |  |  |  | 
Ray Switch/Texture Background/Refraction/Map/Range End | <com.redshift3d.redshift4c4d.nodes.core.environment.tex2/rangeend | maxon::TimeValue | Input | false | false | false |  |  |  | 
Ray Switch/Texture Background/Refraction/Map/Range Start | <com.redshift3d.redshift4c4d.nodes.core.environment.tex2/rangestart | maxon::TimeValue | Input | false | false | false |  |  |  | 
Ray Switch/Texture Background/Refraction/Map/Start Offset | <com.redshift3d.redshift4c4d.nodes.core.environment.tex2/startoffset | maxon::Int | Input | false | false | false |  |  |  | 
Ray Switch/Texture Background/Refraction/Map/Timing | <com.redshift3d.redshift4c4d.nodes.core.environment.tex2/timing | maxon::Int | Input | false | false | true |  |  |  | Time = 1, Frame = 0, Range = 2
Ray Switch/Texture Background/Refraction/Projection Mode | <com.redshift3d.redshift4c4d.nodes.core.environment.moderefract | maxon::Int | Input | false | false | true |  |  | 0 | Spherical = 0, Cylindrical = 1, Cubic Strip = 2, Cube Cross Sideways = 3, Cube Cross = 4
Ray Switch/Texture GI/Adjust Hue/Sat/Exp/Exposure | <com.redshift3d.redshift4c4d.nodes.core.environment.tex4_exp | maxon::Float | Input | false | false | false |  |  | 0 | 
Ray Switch/Texture GI/Adjust Hue/Sat/Exp/Hue | <com.redshift3d.redshift4c4d.nodes.core.environment.tex4_hue | maxon::Float | Input | false | false | false | 0 | 360 | 0 | 
Ray Switch/Texture GI/Adjust Hue/Sat/Exp/Saturation | <com.redshift3d.redshift4c4d.nodes.core.environment.tex4_sat | maxon::Float | Input | false | false | false | 0 | 1000 | 100 | 
Ray Switch/Texture GI/Custom Gamma | <com.redshift3d.redshift4c4d.nodes.core.environment.tex4_gamma | maxon::Float | Input | false | false | false |  |  | 1 | 
Ray Switch/Texture GI/Map | <com.redshift3d.redshift4c4d.nodes.core.environment.tex4 | com.redshift3d.redshift4c4d.portbundle.file | Input | false | true | false |  |  |  | 
Ray Switch/Texture GI/Map/Animation | <com.redshift3d.redshift4c4d.nodes.core.environment.tex4/animation | maxon::Int | Input | false | false | true |  |  |  | Off = 0, Simple = 1, Loop = 2, Ping-Pong = 3
Ray Switch/Texture GI/Map/Color Space | <com.redshift3d.redshift4c4d.nodes.core.environment.tex4/colorspace | maxon::String | Input | false | false | false |  |  |  | 
Ray Switch/Texture GI/Map/Frame End | <com.redshift3d.redshift4c4d.nodes.core.environment.tex4/frameend | maxon::Int | Input | false | false | false |  |  |  | 
Ray Switch/Texture GI/Map/Frame Rate | <com.redshift3d.redshift4c4d.nodes.core.environment.tex4/framerate | maxon::Int | Input | false | false | false |  |  | 30 | 
Ray Switch/Texture GI/Map/Frame Start | <com.redshift3d.redshift4c4d.nodes.core.environment.tex4/framestart | maxon::Int | Input | false | false | false |  |  |  | 
Ray Switch/Texture GI/Map/Layer | <com.redshift3d.redshift4c4d.nodes.core.environment.tex4/layerset | maxon::LayerSet | Input | false | false | false |  |  |  | 
Ray Switch/Texture GI/Map/Loops | <com.redshift3d.redshift4c4d.nodes.core.environment.tex4/loops | maxon::Int | Input | false | false | false |  |  |  | 
Ray Switch/Texture GI/Map/Path | <com.redshift3d.redshift4c4d.nodes.core.environment.tex4/path | maxon::Url | Input | false | false | false |  |  |  | 
Ray Switch/Texture GI/Map/Range End | <com.redshift3d.redshift4c4d.nodes.core.environment.tex4/rangeend | maxon::TimeValue | Input | false | false | false |  |  |  | 
Ray Switch/Texture GI/Map/Range Start | <com.redshift3d.redshift4c4d.nodes.core.environment.tex4/rangestart | maxon::TimeValue | Input | false | false | false |  |  |  | 
Ray Switch/Texture GI/Map/Start Offset | <com.redshift3d.redshift4c4d.nodes.core.environment.tex4/startoffset | maxon::Int | Input | false | false | false |  |  |  | 
Ray Switch/Texture GI/Map/Timing | <com.redshift3d.redshift4c4d.nodes.core.environment.tex4/timing | maxon::Int | Input | false | false | true |  |  |  | Time = 1, Frame = 0, Range = 2
Ray Switch/Texture GI/Projection Mode | <com.redshift3d.redshift4c4d.nodes.core.environment.modegi | maxon::Int | Input | false | false | true |  |  | 0 | Spherical = 0, Cylindrical = 1, Cubic Strip = 2, Cube Cross Sideways = 3, Cube Cross = 4
Ray Switch/Texture Reflections/Adjust Hue/Sat/Exp/Exposure | <com.redshift3d.redshift4c4d.nodes.core.environment.tex3_exp | maxon::Float | Input | false | false | false |  |  | 0 | 
Ray Switch/Texture Reflections/Adjust Hue/Sat/Exp/Hue | <com.redshift3d.redshift4c4d.nodes.core.environment.tex3_hue | maxon::Float | Input | false | false | false | 0 | 360 | 0 | 
Ray Switch/Texture Reflections/Adjust Hue/Sat/Exp/Saturation | <com.redshift3d.redshift4c4d.nodes.core.environment.tex3_sat | maxon::Float | Input | false | false | false | 0 | 1000 | 100 | 
Ray Switch/Texture Reflections/Custom Gamma | <com.redshift3d.redshift4c4d.nodes.core.environment.tex3_gamma | maxon::Float | Input | false | false | false |  |  | 1 | 
Ray Switch/Texture Reflections/Map | <com.redshift3d.redshift4c4d.nodes.core.environment.tex3 | com.redshift3d.redshift4c4d.portbundle.file | Input | false | true | false |  |  |  | 
Ray Switch/Texture Reflections/Map/Animation | <com.redshift3d.redshift4c4d.nodes.core.environment.tex3/animation | maxon::Int | Input | false | false | true |  |  |  | Off = 0, Simple = 1, Loop = 2, Ping-Pong = 3
Ray Switch/Texture Reflections/Map/Color Space | <com.redshift3d.redshift4c4d.nodes.core.environment.tex3/colorspace | maxon::String | Input | false | false | false |  |  |  | 
Ray Switch/Texture Reflections/Map/Frame End | <com.redshift3d.redshift4c4d.nodes.core.environment.tex3/frameend | maxon::Int | Input | false | false | false |  |  |  | 
Ray Switch/Texture Reflections/Map/Frame Rate | <com.redshift3d.redshift4c4d.nodes.core.environment.tex3/framerate | maxon::Int | Input | false | false | false |  |  | 30 | 
Ray Switch/Texture Reflections/Map/Frame Start | <com.redshift3d.redshift4c4d.nodes.core.environment.tex3/framestart | maxon::Int | Input | false | false | false |  |  |  | 
Ray Switch/Texture Reflections/Map/Layer | <com.redshift3d.redshift4c4d.nodes.core.environment.tex3/layerset | maxon::LayerSet | Input | false | false | false |  |  |  | 
Ray Switch/Texture Reflections/Map/Loops | <com.redshift3d.redshift4c4d.nodes.core.environment.tex3/loops | maxon::Int | Input | false | false | false |  |  |  | 
Ray Switch/Texture Reflections/Map/Path | <com.redshift3d.redshift4c4d.nodes.core.environment.tex3/path | maxon::Url | Input | false | false | false |  |  |  | 
Ray Switch/Texture Reflections/Map/Range End | <com.redshift3d.redshift4c4d.nodes.core.environment.tex3/rangeend | maxon::TimeValue | Input | false | false | false |  |  |  | 
Ray Switch/Texture Reflections/Map/Range Start | <com.redshift3d.redshift4c4d.nodes.core.environment.tex3/rangestart | maxon::TimeValue | Input | false | false | false |  |  |  | 
Ray Switch/Texture Reflections/Map/Start Offset | <com.redshift3d.redshift4c4d.nodes.core.environment.tex3/startoffset | maxon::Int | Input | false | false | false |  |  |  | 
Ray Switch/Texture Reflections/Map/Timing | <com.redshift3d.redshift4c4d.nodes.core.environment.tex3/timing | maxon::Int | Input | false | false | true |  |  |  | Time = 1, Frame = 0, Range = 2
Ray Switch/Texture Reflections/Projection Mode | <com.redshift3d.redshift4c4d.nodes.core.environment.modereflect | maxon::Int | Input | false | false | true |  |  | 0 | Spherical = 0, Cylindrical = 1, Cubic Strip = 2, Cube Cross Sideways = 3, Cube Cross = 4
Outputs/outColor | >com.redshift3d.redshift4c4d.nodes.core.environment.outcolor | maxon::ColorA64 | Output | false | false | false |  |  | (0,0,0,1) | 

