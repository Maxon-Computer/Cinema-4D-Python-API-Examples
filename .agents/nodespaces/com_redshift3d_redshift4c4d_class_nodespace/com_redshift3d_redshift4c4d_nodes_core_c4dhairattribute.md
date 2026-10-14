# Node Template: C4D Hair Attributes

- **Node Space ID:** `com.redshift3d.redshift4c4d.class.nodespace`
- **Template ID:** `com.redshift3d.redshift4c4d.nodes.core.c4dhairattribute`
- **Template Name:** `C4D Hair Attributes`

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
Node Category | net.maxon.node.base.category | maxon::InternedId | Attribute | false | false | true |  |  | structures | distributions = distributions, operators = operators, geometries = geometries, patterns = patterns, primitives = primitives, effectors = effectors, fields = fields, functions = functions, structures = structures, geomodifiers = geomodifiers, geogenerators = geogenerators
Preview/Node | net.maxon.node.base.nodepreviewimage | maxon::ImageBaseRef | Attribute | false | false | false |  |  |  | 
Outputs/outColor | >com.redshift3d.redshift4c4d.nodes.core.c4dhairattribute.outcolor | maxon::Color64 | Output | false | false | false |  |  | (0,0,0) | 
Outputs/outPReflColor | >com.redshift3d.redshift4c4d.nodes.core.c4dhairattribute.outpreflcolor | maxon::Color64 | Output | false | false | false |  |  | (0,0,0) | 
Outputs/outStdMatDiffuseWeight | >com.redshift3d.redshift4c4d.nodes.core.c4dhairattribute.outstdmatdiffuseweight | maxon::Float | Output | false | false | false |  |  | 0 | 
Outputs/outStdMatIReflGloss | >com.redshift3d.redshift4c4d.nodes.core.c4dhairattribute.outstdmatireflgloss | maxon::Float | Output | false | false | false |  |  | 0 | 
Outputs/outStdMatIReflWeight | >com.redshift3d.redshift4c4d.nodes.core.c4dhairattribute.outstdmatireflweight | maxon::Float | Output | false | false | false |  |  | 0 | 
Outputs/outStdMatPReflGloss | >com.redshift3d.redshift4c4d.nodes.core.c4dhairattribute.outstdmatpreflgloss | maxon::Float | Output | false | false | false |  |  | 0 | 
Outputs/outStdMatPReflWeight | >com.redshift3d.redshift4c4d.nodes.core.c4dhairattribute.outstdmatpreflweight | maxon::Float | Output | false | false | false |  |  | 0 | 
Outputs/outStdMatTranslucencyWeight | >com.redshift3d.redshift4c4d.nodes.core.c4dhairattribute.outstdmattranslucencyweight | maxon::Float | Output | false | false | false |  |  | 0 | 
Outputs/outTranslucencyColor | >com.redshift3d.redshift4c4d.nodes.core.c4dhairattribute.outtranslucencycolor | maxon::Color64 | Output | false | false | false |  |  | (0,0,0) | 
Outputs/outTransparencyWeight | >com.redshift3d.redshift4c4d.nodes.core.c4dhairattribute.outtransparencyweight | maxon::Float | Output | false | false | false |  |  | 0 | 
Outputs/outUV | >com.redshift3d.redshift4c4d.nodes.core.c4dhairattribute.outuv | maxon::Vector2d64 | Output | false | false | false |  |  | (0,0) | 

