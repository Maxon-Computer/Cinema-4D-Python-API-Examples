# Node Template: Ray Switch

- **Node Space ID:** `com.redshift3d.redshift4c4d.class.nodespace`
- **Template ID:** `com.redshift3d.redshift4c4d.nodes.core.rayswitch`
- **Template Name:** `Ray Switch`

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
Node Category | net.maxon.node.base.category | maxon::InternedId | Attribute | false | false | true |  |  | structures | operators = operators, distributions = distributions, geometries = geometries, patterns = patterns, primitives = primitives, effectors = effectors, fields = fields, functions = functions, structures = structures, geomodifiers = geomodifiers, geogenerators = geogenerators
Preview/Node | net.maxon.node.base.nodepreviewimage | maxon::ImageBaseRef | Attribute | false | false | false |  |  |  | 
Inputs/Camera/Back-face Color | <com.redshift3d.redshift4c4d.nodes.core.rayswitch.cameracolorback | maxon::ColorA64 | Input | false | false | false |  |  | (0.5,0.5,0.5,1) | 
Inputs/Camera/Color | <com.redshift3d.redshift4c4d.nodes.core.rayswitch.cameracolor | maxon::ColorA64 | Input | false | false | false |  |  | (1,1,1,1) | 
Inputs/Camera/Enable Front/Back | <com.redshift3d.redshift4c4d.nodes.core.rayswitch.cameraswitchfrontback | maxon::Bool | Input | false | false | false |  |  | false | 
Inputs/GI/Back-face Color | <com.redshift3d.redshift4c4d.nodes.core.rayswitch.gicolorback | maxon::ColorA64 | Input | false | false | false |  |  | (0,0,0.5,1) | 
Inputs/GI/Color | <com.redshift3d.redshift4c4d.nodes.core.rayswitch.gicolor | maxon::ColorA64 | Input | false | false | false |  |  | (0,0,1,1) | 
Inputs/GI/Enable | <com.redshift3d.redshift4c4d.nodes.core.rayswitch.giswitch | maxon::Bool | Input | false | false | false |  |  | false | 
Inputs/GI/Enable Front/Back | <com.redshift3d.redshift4c4d.nodes.core.rayswitch.giswitchfrontback | maxon::Bool | Input | false | false | false |  |  | false | 
Inputs/Reflection/Back-face Color | <com.redshift3d.redshift4c4d.nodes.core.rayswitch.reflectioncolorback | maxon::ColorA64 | Input | false | false | false |  |  | (0.5,0,0,1) | 
Inputs/Reflection/Color | <com.redshift3d.redshift4c4d.nodes.core.rayswitch.reflectioncolor | maxon::ColorA64 | Input | false | false | false |  |  | (1,0,0,1) | 
Inputs/Reflection/Enable | <com.redshift3d.redshift4c4d.nodes.core.rayswitch.reflectionswitch | maxon::Bool | Input | false | false | false |  |  | false | 
Inputs/Reflection/Enable Front/Back | <com.redshift3d.redshift4c4d.nodes.core.rayswitch.reflectionswitchfrontback | maxon::Bool | Input | false | false | false |  |  | false | 
Inputs/Refraction/Back-face Color | <com.redshift3d.redshift4c4d.nodes.core.rayswitch.refractioncolorback | maxon::ColorA64 | Input | false | false | false |  |  | (0,0.5,0,1) | 
Inputs/Refraction/Color | <com.redshift3d.redshift4c4d.nodes.core.rayswitch.refractioncolor | maxon::ColorA64 | Input | false | false | false |  |  | (0,1,0,1) | 
Inputs/Refraction/Enable | <com.redshift3d.redshift4c4d.nodes.core.rayswitch.refractionswitch | maxon::Bool | Input | false | false | false |  |  | false | 
Inputs/Refraction/Enable Front/Back | <com.redshift3d.redshift4c4d.nodes.core.rayswitch.refractionswitchfrontback | maxon::Bool | Input | false | false | false |  |  | false | 
Outputs/outColor | >com.redshift3d.redshift4c4d.nodes.core.rayswitch.outcolor | maxon::ColorA64 | Output | false | false | false |  |  | (0,0,0,1) | 

