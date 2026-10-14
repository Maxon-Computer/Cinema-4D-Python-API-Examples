# Node Template: Portal Light

- **Node Space ID:** `com.redshift3d.redshift4c4d.class.nodespace`
- **Template ID:** `com.redshift3d.redshift4c4d.nodes.core.light_portal`
- **Template Name:** `Portal Light`

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
Inputs/Emit_direct_photons | <com.redshift3d.redshift4c4d.nodes.core.light_portal.emit_direct_photons | maxon::Bool | Input | false | false | false |  |  | false | 
Inputs/Environment_shader | <com.redshift3d.redshift4c4d.nodes.core.light_portal.environment_shader | maxon::ColorA64 | Input | false | false | false |  |  | (0,0,0,0) | 
Inputs/General/Exposure | <com.redshift3d.redshift4c4d.nodes.core.light_portal.exposure | maxon::Float | Input | false | false | false |  |  | 0 | 
Inputs/General/Intensity Multiplier | <com.redshift3d.redshift4c4d.nodes.core.light_portal.multiplier | maxon::Float | Input | false | false | false |  |  | 1 | 
Inputs/General/On | <com.redshift3d.redshift4c4d.nodes.core.light_portal.on | maxon::Bool | Input | false | false | false |  |  | true | 
Inputs/General/Portal Transparency | <com.redshift3d.redshift4c4d.nodes.core.light_portal.transparency | maxon::Color64 | Input | false | false | false |  |  | (1,1,1) | 
Inputs/General/Tint Color | <com.redshift3d.redshift4c4d.nodes.core.light_portal.tint_color | maxon::Color64 | Input | false | false | false |  |  | (1,1,1) | 
Inputs/Mia_compatibility | <com.redshift3d.redshift4c4d.nodes.core.light_portal.mia_compatibility | maxon::Bool | Input | false | false | false |  |  | false | 
Inputs/Reverse | <com.redshift3d.redshift4c4d.nodes.core.light_portal.reverse | maxon::Bool | Input | false | false | false |  |  | false | 
Inputs/Shadow/Enable Shadows | <com.redshift3d.redshift4c4d.nodes.core.light_portal.shadows | maxon::Bool | Input | false | false | false |  |  | true | 
Inputs/Shadow/Transparency | <com.redshift3d.redshift4c4d.nodes.core.light_portal.shadowtransparency | maxon::Float | Input | false | false | false | 0 | 1 | 0 | 
Inputs/Visible | <com.redshift3d.redshift4c4d.nodes.core.light_portal.visible | maxon::Bool | Input | false | false | false |  |  | false | 
Outputs/color_shadowAmount | >com.redshift3d.redshift4c4d.nodes.core.light_portal.color_shadowamount | maxon::ColorA64 | Output | false | false | false |  |  | (0,0,0,1) | 

