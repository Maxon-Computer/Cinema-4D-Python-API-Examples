# Node Template: Shader Switch

- **Node Space ID:** `com.redshift3d.redshift4c4d.class.nodespace`
- **Template ID:** `com.redshift3d.redshift4c4d.nodes.core.rsshaderswitch`
- **Template Name:** `Shader Switch`

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
Node Category | net.maxon.node.base.category | maxon::InternedId | Attribute | false | false | true |  |  | structures | distributions = distributions, operators = operators, geometries = geometries, patterns = patterns, primitives = primitives, effectors = effectors, fields = fields, functions = functions, structures = structures, geomodifiers = geomodifiers, geogenerators = geogenerators
Preview/Node | net.maxon.node.base.nodepreviewimage | maxon::ImageBaseRef | Attribute | false | false | false |  |  |  | 
Inputs/Default Shader | <com.redshift3d.redshift4c4d.nodes.core.rsshaderswitch.default_shader | maxon::ColorA64 | Input | false | false | false |  |  | (1,1,1,1) | 
Inputs/Offset | <com.redshift3d.redshift4c4d.nodes.core.rsshaderswitch.selector_offset | maxon::Int | Input | false | false | false | -2147483647 | 2147483646 | 0 | 
Inputs/Shader 0 | <com.redshift3d.redshift4c4d.nodes.core.rsshaderswitch.shader0 | maxon::ColorA64 | Input | false | false | false |  |  | (1,1,1,1) | 
Inputs/Shader 1 | <com.redshift3d.redshift4c4d.nodes.core.rsshaderswitch.shader1 | maxon::ColorA64 | Input | false | false | false |  |  | (1,1,1,1) | 
Inputs/Shader 2 | <com.redshift3d.redshift4c4d.nodes.core.rsshaderswitch.shader2 | maxon::ColorA64 | Input | false | false | false |  |  | (1,1,1,1) | 
Inputs/Shader 3 | <com.redshift3d.redshift4c4d.nodes.core.rsshaderswitch.shader3 | maxon::ColorA64 | Input | false | false | false |  |  | (1,1,1,1) | 
Inputs/Shader 4 | <com.redshift3d.redshift4c4d.nodes.core.rsshaderswitch.shader4 | maxon::ColorA64 | Input | false | false | false |  |  | (1,1,1,1) | 
Inputs/Shader 5 | <com.redshift3d.redshift4c4d.nodes.core.rsshaderswitch.shader5 | maxon::ColorA64 | Input | false | false | false |  |  | (1,1,1,1) | 
Inputs/Shader 6 | <com.redshift3d.redshift4c4d.nodes.core.rsshaderswitch.shader6 | maxon::ColorA64 | Input | false | false | false |  |  | (1,1,1,1) | 
Inputs/Shader 7 | <com.redshift3d.redshift4c4d.nodes.core.rsshaderswitch.shader7 | maxon::ColorA64 | Input | false | false | false |  |  | (1,1,1,1) | 
Inputs/Shader 8 | <com.redshift3d.redshift4c4d.nodes.core.rsshaderswitch.shader8 | maxon::ColorA64 | Input | false | false | false |  |  | (1,1,1,1) | 
Inputs/Shader 9 | <com.redshift3d.redshift4c4d.nodes.core.rsshaderswitch.shader9 | maxon::ColorA64 | Input | false | false | false |  |  | (1,1,1,1) | 
Inputs/Shader Selector | <com.redshift3d.redshift4c4d.nodes.core.rsshaderswitch.selector | maxon::Int | Input | false | false | false | -2147483647 | 2147483646 | 0 | 
Outputs/outClosure | >com.redshift3d.redshift4c4d.nodes.core.rsshaderswitch.outclosure | maxon::Color64 | Output | false | false | false |  |  | (0,0,0) | 
Outputs/outColor | >com.redshift3d.redshift4c4d.nodes.core.rsshaderswitch.outcolor | maxon::ColorA64 | Output | false | false | false |  |  | (0,0,0,1) | 

