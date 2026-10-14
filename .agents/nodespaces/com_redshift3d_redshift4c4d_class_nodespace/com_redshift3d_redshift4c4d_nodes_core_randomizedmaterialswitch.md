# Node Template: Random Material Switch

- **Node Space ID:** `com.redshift3d.redshift4c4d.class.nodespace`
- **Template ID:** `com.redshift3d.redshift4c4d.nodes.core.randomizedmaterialswitch`
- **Template Name:** `Random Material Switch`

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
General/Randomizer Source/Input ID Mode | <com.redshift3d.redshift4c4d.nodes.core.randomizedmaterialswitch.ininputid | maxon::Int | Input | false | false | true |  |  | 2 | Object ID = 0, Name ID = 2, UserData ID = 4
General/Randomizer Source/User Data | <com.redshift3d.redshift4c4d.nodes.core.randomizedmaterialswitch.inuserdata | maxon::Int | Input | false | false | false |  |  | 0 | 
General/Shader Switch Jitter/Seed | <com.redshift3d.redshift4c4d.nodes.core.randomizedmaterialswitch.infloatseed | maxon::Int | Input | false | false | false |  |  | 123 | 
General/Shader Switch Jitter/Shaders | <com.redshift3d.redshift4c4d.nodes.core.randomizedmaterialswitch.shaders | com.redshift3d.redshift4c4d.nodes.core.randomizedmaterialswitch.struct.shaders | Input | true | true | false |  |  |  | 
General/Shader Switch Jitter/Shaders/Shaders.1 | <com.redshift3d.redshift4c4d.nodes.core.randomizedmaterialswitch.shaders/_0 | com.redshift3d.redshift4c4d.nodes.core.randomizedmaterialswitch.struct.shaders | Input | false | false | false |  |  |  | 
General/Shader Switch Jitter/Shaders/Shaders.1/Material | <com.redshift3d.redshift4c4d.nodes.core.randomizedmaterialswitch.shaders/_0/com.redshift3d.redshift4c4d.nodes.core.randomizedmaterialswitch.struct.shaders.shader_input | maxon::Color64 | Input | false | false | false |  |  | (0,0,0) | 
General/Shader Switch Jitter/Shaders/Shaders.1/Weight | <com.redshift3d.redshift4c4d.nodes.core.randomizedmaterialswitch.shaders/_0/com.redshift3d.redshift4c4d.nodes.core.randomizedmaterialswitch.struct.shaders.shader_weight | maxon::Float | Input | false | false | false | 0 | 100 | 1 | 
General/Shader Switch Jitter/Shaders/Shaders.2 | <com.redshift3d.redshift4c4d.nodes.core.randomizedmaterialswitch.shaders/_1 | com.redshift3d.redshift4c4d.nodes.core.randomizedmaterialswitch.struct.shaders | Input | false | false | false |  |  |  | 
General/Shader Switch Jitter/Shaders/Shaders.2/Material | <com.redshift3d.redshift4c4d.nodes.core.randomizedmaterialswitch.shaders/_1/com.redshift3d.redshift4c4d.nodes.core.randomizedmaterialswitch.struct.shaders.shader_input | maxon::Color64 | Input | false | false | false |  |  | (0,0,0) | 
General/Shader Switch Jitter/Shaders/Shaders.2/Weight | <com.redshift3d.redshift4c4d.nodes.core.randomizedmaterialswitch.shaders/_1/com.redshift3d.redshift4c4d.nodes.core.randomizedmaterialswitch.struct.shaders.shader_weight | maxon::Float | Input | false | false | false | 0 | 100 | 1 | 
Tint Jitter/General/Enabled | <com.redshift3d.redshift4c4d.nodes.core.randomizedmaterialswitch.incoljitterenabled | maxon::Bool | Input | false | false | false |  |  | false | 
Tint Jitter/General/Hue Seed | <com.redshift3d.redshift4c4d.nodes.core.randomizedmaterialswitch.inhueseed | maxon::Int | Input | false | false | false |  |  | 123 | 
Tint Jitter/General/Hue Variation Max | <com.redshift3d.redshift4c4d.nodes.core.randomizedmaterialswitch.inhuevarmax | maxon::Float | Input | false | false | false | -360 | 360 | 1 | 
Tint Jitter/General/Hue Variation Min | <com.redshift3d.redshift4c4d.nodes.core.randomizedmaterialswitch.inhuevarmin | maxon::Float | Input | false | false | false | -360 | 360 | 0 | 
Tint Jitter/General/Saturation Seed | <com.redshift3d.redshift4c4d.nodes.core.randomizedmaterialswitch.insaturationseed | maxon::Int | Input | false | false | false |  |  | 123 | 
Tint Jitter/General/Saturation Variation Max | <com.redshift3d.redshift4c4d.nodes.core.randomizedmaterialswitch.insaturationvarmax | maxon::Float | Input | false | false | false | -1 | 1 | 1 | 
Tint Jitter/General/Saturation Variation Min | <com.redshift3d.redshift4c4d.nodes.core.randomizedmaterialswitch.insaturationvarmin | maxon::Float | Input | false | false | false | -1 | 1 | 0 | 
Tint Jitter/General/Tint Color | <com.redshift3d.redshift4c4d.nodes.core.randomizedmaterialswitch.incolor | maxon::Color64 | Input | false | false | false |  |  | (0.5,0.5,0.5) | 
Tint Jitter/General/Value Seed | <com.redshift3d.redshift4c4d.nodes.core.randomizedmaterialswitch.invalueseed | maxon::Int | Input | false | false | false |  |  | 123 | 
Tint Jitter/General/Value Variation Max | <com.redshift3d.redshift4c4d.nodes.core.randomizedmaterialswitch.invaluevarmax | maxon::Float | Input | false | false | false | -1 | 1 | 1 | 
Tint Jitter/General/Value Variation Min | <com.redshift3d.redshift4c4d.nodes.core.randomizedmaterialswitch.invaluevarmin | maxon::Float | Input | false | false | false | -1 | 1 | 0 | 
Outputs/out | >com.redshift3d.redshift4c4d.nodes.core.randomizedmaterialswitch.out | maxon::Color64 | Output | false | false | false |  |  | (0,0,0) | 

