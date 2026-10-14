# Node Template: Physical Light

- **Node Space ID:** `com.redshift3d.redshift4c4d.class.nodespace`
- **Template ID:** `com.redshift3d.redshift4c4d.nodes.core.light`
- **Template Name:** `Physical Light`

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
Node Category | net.maxon.node.base.category | maxon::InternedId | Attribute | false | false | true |  |  | operators | operators = operators, distributions = distributions, geometries = geometries, patterns = patterns, primitives = primitives, effectors = effectors, fields = fields, functions = functions, structures = structures, geomodifiers = geomodifiers, geogenerators = geogenerators
Preview/Node | net.maxon.node.base.nodepreviewimage | maxon::ImageBaseRef | Attribute | false | false | false |  |  |  | 
Inputs/Attenuation/Fall-off Angle | <com.redshift3d.redshift4c4d.nodes.core.light.spotconefalloffangle | maxon::Float | Input | false | false | false | 0 | 180 | 5 | 
Inputs/Attenuation/Fall-off Curve | <com.redshift3d.redshift4c4d.nodes.core.light.spotconefalloffcurve | maxon::Float | Input | false | false | false | 0 | 100 | 1 | 
Inputs/Decay/Falloff Start | <com.redshift3d.redshift4c4d.nodes.core.light.falloffstart | maxon::Float | Input | false | false | false |  |  | 0 | 
Inputs/Decay/Falloff Stop | <com.redshift3d.redshift4c4d.nodes.core.light.falloffstop | maxon::Float | Input | false | false | false |  |  | 100 | 
Inputs/Decay/Type | <com.redshift3d.redshift4c4d.nodes.core.light.decaytype | maxon::Int | Input | false | false | true |  |  | 0 | Inverse-square = 0, None = 1, Linear = 2
Inputs/General/Color | <com.redshift3d.redshift4c4d.nodes.core.light.color | maxon::ColorA64 | Input | false | false | false |  |  | (1,1,1,1) | 
Inputs/General/Exposure | <com.redshift3d.redshift4c4d.nodes.core.light.exposure | maxon::Float | Input | false | false | false |  |  | 0 | 
Inputs/General/Intensity Multiplier | <com.redshift3d.redshift4c4d.nodes.core.light.intensity | maxon::Float | Input | false | false | false |  |  | 100 | 
Inputs/General/Luminous Efficacy (lm/W) | <com.redshift3d.redshift4c4d.nodes.core.light.lumensperwatt | maxon::Float | Input | false | false | false |  |  | 17 | 
Inputs/General/Mode | <com.redshift3d.redshift4c4d.nodes.core.light.colormode | maxon::Int | Input | false | false | true |  |  | 0 | Color = 0, Temperature = 1, Temperature And Color = 2
Inputs/General/On | <com.redshift3d.redshift4c4d.nodes.core.light.on | maxon::Bool | Input | false | false | false |  |  | true | 
Inputs/General/Opacity | <com.redshift3d.redshift4c4d.nodes.core.light.opacity | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Inputs/General/Temperature | <com.redshift3d.redshift4c4d.nodes.core.light.temperature | maxon::Float | Input | false | false | false | 1000 | 20000 | 6500 | 
Inputs/General/Unit Type | <com.redshift3d.redshift4c4d.nodes.core.light.unitstype | maxon::Int | Input | false | false | true |  |  | 0 | Image = 0, Lumens (lm) = 1, Nits (cd/m^2) = 2, Watts (W) = 3, Radiance (W/sr/m^2) = 4, Candelas (cd) = 5, Luminous Exitance (lm/m^2) = 6
Inputs/General/Use Alpha from Color Texture | <com.redshift3d.redshift4c4d.nodes.core.light.usealpha | maxon::Bool | Input | false | false | false |  |  | false | 
Inputs/Shadow/Enable | <com.redshift3d.redshift4c4d.nodes.core.light.shadow | maxon::Bool | Input | false | false | false |  |  | true | 
Inputs/Shadow/Samples | <com.redshift3d.redshift4c4d.nodes.core.light.samplingoverrides_numshadowsamples | maxon::Int | Input | false | false | false | 0 | 4096 | 8 | 
Inputs/Shadow/Softness | <com.redshift3d.redshift4c4d.nodes.core.light.samplingoverrides_shadowsamplesscale | maxon::Float | Input | false | false | false |  |  | 0 | 
Inputs/Shadow/Transparency | <com.redshift3d.redshift4c4d.nodes.core.light.shadowtransparency | maxon::Float | Input | false | false | false | 0 | 1 | 0 | 
Outputs/lightColor_shadowAmount | >com.redshift3d.redshift4c4d.nodes.core.light.lightcolor_shadowamount | maxon::ColorA64 | Output | false | false | false |  |  | (0,0,0,1) | 

