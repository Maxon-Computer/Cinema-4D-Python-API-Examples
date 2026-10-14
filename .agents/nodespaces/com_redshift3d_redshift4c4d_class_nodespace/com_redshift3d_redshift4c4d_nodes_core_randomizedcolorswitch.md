# Node Template: Random Color Switch

- **Node Space ID:** `com.redshift3d.redshift4c4d.class.nodespace`
- **Template ID:** `com.redshift3d.redshift4c4d.nodes.core.randomizedcolorswitch`
- **Template Name:** `Random Color Switch`

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
Color Jitter/General/Enabled | <com.redshift3d.redshift4c4d.nodes.core.randomizedcolorswitch.incoljitterenabled | maxon::Bool | Input | false | false | false |  |  | false | 
Color Jitter/General/Hue Seed | <com.redshift3d.redshift4c4d.nodes.core.randomizedcolorswitch.inhueseed | maxon::Int | Input | false | false | false |  |  | 123 | 
Color Jitter/General/Hue Variation Max | <com.redshift3d.redshift4c4d.nodes.core.randomizedcolorswitch.inhuevarmax | maxon::Float | Input | false | false | false | -360 | 360 | 1 | 
Color Jitter/General/Hue Variation Min | <com.redshift3d.redshift4c4d.nodes.core.randomizedcolorswitch.inhuevarmin | maxon::Float | Input | false | false | false | -360 | 360 | 0 | 
Color Jitter/General/Saturation Seed | <com.redshift3d.redshift4c4d.nodes.core.randomizedcolorswitch.insaturationseed | maxon::Int | Input | false | false | false |  |  | 123 | 
Color Jitter/General/Saturation Variation Max | <com.redshift3d.redshift4c4d.nodes.core.randomizedcolorswitch.insaturationvarmax | maxon::Float | Input | false | false | false | -1 | 1 | 1 | 
Color Jitter/General/Saturation Variation Min | <com.redshift3d.redshift4c4d.nodes.core.randomizedcolorswitch.insaturationvarmin | maxon::Float | Input | false | false | false | -1 | 1 | 0 | 
Color Jitter/General/Value Seed | <com.redshift3d.redshift4c4d.nodes.core.randomizedcolorswitch.invalueseed | maxon::Int | Input | false | false | false |  |  | 123 | 
Color Jitter/General/Value Variation Max | <com.redshift3d.redshift4c4d.nodes.core.randomizedcolorswitch.invaluevarmax | maxon::Float | Input | false | false | false | -1 | 1 | 1 | 
Color Jitter/General/Value Variation Min | <com.redshift3d.redshift4c4d.nodes.core.randomizedcolorswitch.invaluevarmin | maxon::Float | Input | false | false | false | -1 | 1 | 0 | 
General/Randomizer Source/Input ID Mode | <com.redshift3d.redshift4c4d.nodes.core.randomizedcolorswitch.ininputid | maxon::Int | Input | false | false | true |  |  | 2 | Object ID = 0, Name ID = 2, UserData ID = 4
General/Randomizer Source/User Data | <com.redshift3d.redshift4c4d.nodes.core.randomizedcolorswitch.inuserdata | maxon::Int | Input | false | false | false |  |  | 0 | 
General/Shader Switch Jitter/Seed | <com.redshift3d.redshift4c4d.nodes.core.randomizedcolorswitch.infloatseed | maxon::Int | Input | false | false | false |  |  | 123 | 
General/Shader Switch Jitter/Shaders | <com.redshift3d.redshift4c4d.nodes.core.randomizedcolorswitch.shaders | com.redshift3d.redshift4c4d.nodes.core.randomizedcolorswitch.struct.shaders | Input | true | true | false |  |  |  | 
General/Shader Switch Jitter/Shaders/Shaders.1 | <com.redshift3d.redshift4c4d.nodes.core.randomizedcolorswitch.shaders/_0 | com.redshift3d.redshift4c4d.nodes.core.randomizedcolorswitch.struct.shaders | Input | false | false | false |  |  |  | 
General/Shader Switch Jitter/Shaders/Shaders.1/Color | <com.redshift3d.redshift4c4d.nodes.core.randomizedcolorswitch.shaders/_0/com.redshift3d.redshift4c4d.nodes.core.randomizedcolorswitch.struct.shaders.shader_input | maxon::Color64 | Input | false | false | false |  |  | (1,1,1) | 
General/Shader Switch Jitter/Shaders/Shaders.1/Weight | <com.redshift3d.redshift4c4d.nodes.core.randomizedcolorswitch.shaders/_0/com.redshift3d.redshift4c4d.nodes.core.randomizedcolorswitch.struct.shaders.shader_weight | maxon::Float | Input | false | false | false | 0 | 100 | 1 | 
General/Shader Switch Jitter/Shaders/Shaders.2 | <com.redshift3d.redshift4c4d.nodes.core.randomizedcolorswitch.shaders/_1 | com.redshift3d.redshift4c4d.nodes.core.randomizedcolorswitch.struct.shaders | Input | false | false | false |  |  |  | 
General/Shader Switch Jitter/Shaders/Shaders.2/Color | <com.redshift3d.redshift4c4d.nodes.core.randomizedcolorswitch.shaders/_1/com.redshift3d.redshift4c4d.nodes.core.randomizedcolorswitch.struct.shaders.shader_input | maxon::Color64 | Input | false | false | false |  |  | (1,1,1) | 
General/Shader Switch Jitter/Shaders/Shaders.2/Weight | <com.redshift3d.redshift4c4d.nodes.core.randomizedcolorswitch.shaders/_1/com.redshift3d.redshift4c4d.nodes.core.randomizedcolorswitch.struct.shaders.shader_weight | maxon::Float | Input | false | false | false | 0 | 100 | 1 | 
Outputs/outColor | >com.redshift3d.redshift4c4d.nodes.core.randomizedcolorswitch.outcolor | maxon::Color64 | Output | false | false | false |  |  | (0,0,0) | 

