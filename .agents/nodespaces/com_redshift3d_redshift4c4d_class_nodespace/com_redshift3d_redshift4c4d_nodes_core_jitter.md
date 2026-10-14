# Node Template: Jitter

- **Node Space ID:** `com.redshift3d.redshift4c4d.class.nodespace`
- **Template ID:** `com.redshift3d.redshift4c4d.nodes.core.jitter`
- **Template Name:** `Jitter`

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
Shader/Color Jitter/Color | <com.redshift3d.redshift4c4d.nodes.core.jitter.incolor | maxon::Color64 | Input | false | false | false |  |  | (0,0,0) | 
Shader/Color Jitter/Hue Seed | <com.redshift3d.redshift4c4d.nodes.core.jitter.inhueseed | maxon::Int | Input | false | false | false |  |  | 123 | 
Shader/Color Jitter/Hue Variation Max | <com.redshift3d.redshift4c4d.nodes.core.jitter.inhuevarmax | maxon::Float | Input | false | false | false | -360 | 360 | 1 | 
Shader/Color Jitter/Hue Variation Min | <com.redshift3d.redshift4c4d.nodes.core.jitter.inhuevarmin | maxon::Float | Input | false | false | false | -360 | 360 | 0 | 
Shader/Color Jitter/Saturation Seed | <com.redshift3d.redshift4c4d.nodes.core.jitter.insaturationseed | maxon::Int | Input | false | false | false |  |  | 123 | 
Shader/Color Jitter/Saturation Variation Max | <com.redshift3d.redshift4c4d.nodes.core.jitter.insaturationvarmax | maxon::Float | Input | false | false | false | -1 | 1 | 1 | 
Shader/Color Jitter/Saturation Variation Min | <com.redshift3d.redshift4c4d.nodes.core.jitter.insaturationvarmin | maxon::Float | Input | false | false | false | -1 | 1 | 0 | 
Shader/Color Jitter/Value Seed | <com.redshift3d.redshift4c4d.nodes.core.jitter.invalueseed | maxon::Int | Input | false | false | false |  |  | 123 | 
Shader/Color Jitter/Value Variation Max | <com.redshift3d.redshift4c4d.nodes.core.jitter.invaluevarmax | maxon::Float | Input | false | false | false | -1 | 1 | 1 | 
Shader/Color Jitter/Value Variation Min | <com.redshift3d.redshift4c4d.nodes.core.jitter.invaluevarmin | maxon::Float | Input | false | false | false | -1 | 1 | 0 | 
Shader/Float Jitter/Float Max | <com.redshift3d.redshift4c4d.nodes.core.jitter.infloatmax | maxon::Float | Input | false | false | false |  |  | 0 | 
Shader/Float Jitter/Float Min | <com.redshift3d.redshift4c4d.nodes.core.jitter.infloatmin | maxon::Float | Input | false | false | false |  |  | 0 | 
Shader/Float Jitter/Float Seed | <com.redshift3d.redshift4c4d.nodes.core.jitter.infloatseed | maxon::Int | Input | false | false | false |  |  | 123 | 
Shader/General/Input ID Mode | <com.redshift3d.redshift4c4d.nodes.core.jitter.ininputid | maxon::Int | Input | false | false | true |  |  | 2 | Object ID = 0, Name ID = 2, UserData ID = 4
Shader/General/User Data | <com.redshift3d.redshift4c4d.nodes.core.jitter.inuserdata | maxon::Int | Input | false | false | false |  |  | 0 | 
Shader/Integer Jitter/Integer Max | <com.redshift3d.redshift4c4d.nodes.core.jitter.inintegermax | maxon::Int | Input | false | false | false | -2147483647 | 2147483646 | 0 | 
Shader/Integer Jitter/Integer Min | <com.redshift3d.redshift4c4d.nodes.core.jitter.inintegermin | maxon::Int | Input | false | false | false | -2147483647 | 2147483646 | 0 | 
Shader/Integer Jitter/Integer Seed | <com.redshift3d.redshift4c4d.nodes.core.jitter.inintegerseed | maxon::Int | Input | false | false | false |  |  | 123 | 
Outputs/outColor | >com.redshift3d.redshift4c4d.nodes.core.jitter.outcolor | maxon::Color64 | Output | false | false | false |  |  | (0,0,0) | 
Outputs/outFloat | >com.redshift3d.redshift4c4d.nodes.core.jitter.outfloat | maxon::Float | Output | false | false | false |  |  | 0 | 
Outputs/outInt | >com.redshift3d.redshift4c4d.nodes.core.jitter.outint | maxon::Int | Output | false | false | false |  |  | 0 | 

