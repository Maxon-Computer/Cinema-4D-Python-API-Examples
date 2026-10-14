# Node Template: Distorter

- **Node Space ID:** `com.redshift3d.redshift4c4d.class.nodespace`
- **Template ID:** `com.redshift3d.redshift4c4d.nodes.core.distorter`
- **Template Name:** `Distorter`

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
Shader/Amount | <com.redshift3d.redshift4c4d.nodes.core.distorter.inamount | maxon::Float | Input | false | false | false | -2147483648 | 2147483648 | 1 | 
Shader/Delta | <com.redshift3d.redshift4c4d.nodes.core.distorter.indelta | maxon::Float | Input | false | false | false | 0 | 2147483648 | 1 | 
Shader/Distorter | <com.redshift3d.redshift4c4d.nodes.core.distorter.distorter | maxon::ColorA64 | Input | false | false | false |  |  | (0,0,0,1) | 
Shader/Step | <com.redshift3d.redshift4c4d.nodes.core.distorter.instep | maxon::Float | Input | false | false | false | 0 | 10 | 1 | 
Shader/Texture | <com.redshift3d.redshift4c4d.nodes.core.distorter.texture | maxon::ColorA64 | Input | false | false | false |  |  | (0,0,0,1) | 
Shader/Type | <com.redshift3d.redshift4c4d.nodes.core.distorter.intype | maxon::Int | Input | false | false | true |  |  | 0 | Directional = 0, Bidirectional = 1, Flow Field = 2
Shader/Wrap | <com.redshift3d.redshift4c4d.nodes.core.distorter.inwrap | maxon::Int | Input | false | false | true |  |  | 1 | None = 0, Cycle = 1, Clamp = 2, Seamless = 3
Shader/X | <com.redshift3d.redshift4c4d.nodes.core.distorter.inx | maxon::Float | Input | false | false | false | -2147483648 | 2147483648 | 0.1 | 
Shader/Y | <com.redshift3d.redshift4c4d.nodes.core.distorter.iny | maxon::Float | Input | false | false | false | -2147483648 | 2147483648 | 0.1 | 
Shader/Z | <com.redshift3d.redshift4c4d.nodes.core.distorter.inz | maxon::Float | Input | false | false | false | -2147483648 | 2147483648 | 0.1 | 
Outputs/outColor | >com.redshift3d.redshift4c4d.nodes.core.distorter.outcolor | maxon::ColorA64 | Output | false | false | false |  |  | (0,0,0,1) | 

