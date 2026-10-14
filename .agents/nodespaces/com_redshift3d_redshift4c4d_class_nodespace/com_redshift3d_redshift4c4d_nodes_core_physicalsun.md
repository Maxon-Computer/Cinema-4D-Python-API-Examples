# Node Template: Sun Light

- **Node Space ID:** `com.redshift3d.redshift4c4d.class.nodespace`
- **Template ID:** `com.redshift3d.redshift4c4d.nodes.core.physicalsun`
- **Template Name:** `Sun Light`

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
Inputs/Atmosphere/Horizon Height | <com.redshift3d.redshift4c4d.nodes.core.physicalsun.horizon_height | maxon::Float | Input | false | false | false |  |  | 0 | 
Inputs/Atmosphere/Ozone | <com.redshift3d.redshift4c4d.nodes.core.physicalsun.ozone | maxon::Float | Input | false | false | false | 0 | 1 | 0.35 | 
Inputs/Atmosphere/Turbidity | <com.redshift3d.redshift4c4d.nodes.core.physicalsun.haze | maxon::Float | Input | false | false | false |  |  | 2 | 
Inputs/Color Adjustment/Red-Blue Shift | <com.redshift3d.redshift4c4d.nodes.core.physicalsun.redblueshift | maxon::Float | Input | false | false | false |  |  | 0 | 
Inputs/Color Adjustment/Saturation | <com.redshift3d.redshift4c4d.nodes.core.physicalsun.saturation | maxon::Float | Input | false | false | false |  |  | 1 | 
Inputs/Color Adjustment/Saturation Affects Color Adjustments | <com.redshift3d.redshift4c4d.nodes.core.physicalsun.saturation_affects_color_adjustments | maxon::Bool | Input | false | false | false |  |  | true | 
Inputs/Color Adjustment/Tint | <com.redshift3d.redshift4c4d.nodes.core.physicalsun.tint | maxon::Color64 | Input | false | false | false |  |  | (1,1,1) | 
Inputs/General/Intensity Multiplier | <com.redshift3d.redshift4c4d.nodes.core.physicalsun.multiplier | maxon::Float | Input | false | false | false |  |  | 1 | 
Inputs/General/Model | <com.redshift3d.redshift4c4d.nodes.core.physicalsun.model | maxon::Int | Input | false | false | true |  |  | 0 | PRG Clear Sky = 0, Legacy = 1
Inputs/General/On | <com.redshift3d.redshift4c4d.nodes.core.physicalsun.on | maxon::Bool | Input | false | false | false |  |  | true | 
Inputs/General/RGB Unit Conversion | <com.redshift3d.redshift4c4d.nodes.core.physicalsun.rgb_unit_conversion | maxon::Color64 | Input | false | false | false |  |  | (0.318,0.318,0.318) | 
Inputs/General/Sun Disk Scale | <com.redshift3d.redshift4c4d.nodes.core.physicalsun.sun_disk_scale | maxon::Float | Input | false | false | false |  |  | 1 | 
Inputs/General/Use Non-Physical Intensity | <com.redshift3d.redshift4c4d.nodes.core.physicalsun.usenonphysicalintensity | maxon::Bool | Input | false | false | false |  |  | false | 
Inputs/Mia_compatibility | <com.redshift3d.redshift4c4d.nodes.core.physicalsun.mia_compatibility | maxon::Bool | Input | false | false | false |  |  | false | 
Inputs/Photon/Automatic_photon_energy | <com.redshift3d.redshift4c4d.nodes.core.physicalsun.automatic_photon_energy | maxon::Bool | Input | false | false | false |  |  | true | 
Inputs/Photon/Photon_bbox_max | <com.redshift3d.redshift4c4d.nodes.core.physicalsun.photon_bbox_max | maxon::Vector64 | Input | false | false | false |  |  | (0,0,0) | 
Inputs/Photon/Photon_bbox_min | <com.redshift3d.redshift4c4d.nodes.core.physicalsun.photon_bbox_min | maxon::Vector64 | Input | false | false | false |  |  | (0,0,0) | 
Inputs/Shadow/Samples | <com.redshift3d.redshift4c4d.nodes.core.physicalsun.samplingoverrides_numshadowsamples | maxon::Int | Input | false | false | false | 0 | 4096 | 8 | 
Inputs/Shadow/Softness | <com.redshift3d.redshift4c4d.nodes.core.physicalsun.samplingoverrides_shadowsamplesscale | maxon::Float | Input | false | false | false |  |  | 1 | 
Inputs/Shadow/Transparency | <com.redshift3d.redshift4c4d.nodes.core.physicalsun.shadowtransparency | maxon::Float | Input | false | false | false | 0 | 1 | 0 | 
Inputs/Y_is_up | <com.redshift3d.redshift4c4d.nodes.core.physicalsun.y_is_up | maxon::Bool | Input | false | false | false |  |  | true | 
Outputs/lightColor_shadowAmount | >com.redshift3d.redshift4c4d.nodes.core.physicalsun.lightcolor_shadowamount | maxon::ColorA64 | Output | false | false | false |  |  | (0,0,0,1) | 

