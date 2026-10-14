# Node Template: Tonemap Pattern

- **Node Space ID:** `com.redshift3d.redshift4c4d.class.nodespace`
- **Template ID:** `com.redshift3d.redshift4c4d.nodes.core.tonemappattern`
- **Template Name:** `Tonemap Pattern`

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
Basic/Show Preview | net.maxon.node.base.displaypreview | maxon::Bool | Attribute | false | false | false |  |  | false | 
Filter Tags | net.maxon.node.base.filtertags | maxon::CString | Attribute | false | false | false |  |  |  | 
Node Category | net.maxon.node.base.category | maxon::InternedId | Attribute | false | false | true |  |  | patterns | operators = operators, distributions = distributions, geometries = geometries, patterns = patterns, primitives = primitives, effectors = effectors, fields = fields, functions = functions, structures = structures, geomodifiers = geomodifiers, geogenerators = geogenerators
Preview/Node | net.maxon.node.base.nodepreviewimage | maxon::ImageBaseRef | Attribute | false | false | false |  |  |  | 
General/Background Color | <com.redshift3d.redshift4c4d.nodes.core.tonemappattern.color2 | maxon::Color64 | Input | false | false | false |  |  | (1,1,1) | 
General/Intensity Override | <com.redshift3d.redshift4c4d.nodes.core.tonemappattern.intensityoverride | maxon::Float | Input | false | false | false |  |  |  | 
General/Offset X | <com.redshift3d.redshift4c4d.nodes.core.tonemappattern.offsetx | maxon::Float | Input | false | false | false | 0 | 2147483648 | 0 | 
General/Offset Y | <com.redshift3d.redshift4c4d.nodes.core.tonemappattern.offsety | maxon::Float | Input | false | false | false | 0 | 2147483648 | 0 | 
General/Pattern | <com.redshift3d.redshift4c4d.nodes.core.tonemappattern.pattern | maxon::Int | Input | false | false | true |  |  | 0 | Halftone = 0, Sine Waves = 1, Grid = 2, Cross Hatch = 3, Custom = 4
General/Pattern Color | <com.redshift3d.redshift4c4d.nodes.core.tonemappattern.color1 | maxon::Color64 | Input | false | false | false |  |  | (0,0,0) | 
General/Rotation | <com.redshift3d.redshift4c4d.nodes.core.tonemappattern.rotation | maxon::Float | Input | false | false | false | 0 | 360 | 0 | 
General/Scale | <com.redshift3d.redshift4c4d.nodes.core.tonemappattern.scale | maxon::Float | Input | false | false | false | 0 | 2147483648 | 1 | 
General/Scale Height | <com.redshift3d.redshift4c4d.nodes.core.tonemappattern.scaleheight | maxon::Float | Input | false | false | false | 0 | 2147483648 | 1 | 
General/Scale Width | <com.redshift3d.redshift4c4d.nodes.core.tonemappattern.scalewidth | maxon::Float | Input | false | false | false | 0 | 2147483648 | 1 | 
General/Tile Scale Bias | <com.redshift3d.redshift4c4d.nodes.core.tonemappattern.tilescalebias | maxon::Float | Input | false | false | false |  |  | 0 | 
Randomization/Per-Tile Randomization/Hue Variation Max | <com.redshift3d.redshift4c4d.nodes.core.tonemappattern.randomhuemax | maxon::Float | Input | false | false | false | -360 | 360 | 0 | 
Randomization/Per-Tile Randomization/Hue Variation Min | <com.redshift3d.redshift4c4d.nodes.core.tonemappattern.randomhuemin | maxon::Float | Input | false | false | false | -360 | 360 | 0 | 
Randomization/Per-Tile Randomization/Offset Variation | <com.redshift3d.redshift4c4d.nodes.core.tonemappattern.randomoffset | maxon::Float | Input | false | false | false | 0 | 2147483648 | 0 | 
Randomization/Per-Tile Randomization/Rotation Variation | <com.redshift3d.redshift4c4d.nodes.core.tonemappattern.randomrotation | maxon::Float | Input | false | false | false | 0 | 1 | 0 | 
Randomization/Per-Tile Randomization/Saturation Variation Max | <com.redshift3d.redshift4c4d.nodes.core.tonemappattern.randomsaturationmax | maxon::Float | Input | false | false | false | -1 | 1 | 0 | 
Randomization/Per-Tile Randomization/Saturation Variation Min | <com.redshift3d.redshift4c4d.nodes.core.tonemappattern.randomsaturationmin | maxon::Float | Input | false | false | false | -1 | 1 | 0 | 
Randomization/Per-Tile Randomization/Scale Variation | <com.redshift3d.redshift4c4d.nodes.core.tonemappattern.randomscale | maxon::Float | Input | false | false | false | 0 | 2147483648 | 0 | 
Randomization/Per-Tile Randomization/Seed | <com.redshift3d.redshift4c4d.nodes.core.tonemappattern.randomseed | maxon::Int | Input | false | false | false |  |  | 123 | 
Randomization/Per-Tile Randomization/Value Variation Max | <com.redshift3d.redshift4c4d.nodes.core.tonemappattern.randomvaluemax | maxon::Float | Input | false | false | false | -1 | 1 | 0 | 
Randomization/Per-Tile Randomization/Value Variation Min | <com.redshift3d.redshift4c4d.nodes.core.tonemappattern.randomvaluemin | maxon::Float | Input | false | false | false | -1 | 1 | 0 | 
Outputs/outColor | >com.redshift3d.redshift4c4d.nodes.core.tonemappattern.outcolor | maxon::Color64 | Output | false | false | false |  |  | (0,0,0) | 

