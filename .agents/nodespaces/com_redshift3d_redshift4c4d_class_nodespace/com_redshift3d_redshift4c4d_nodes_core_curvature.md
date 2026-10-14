# Node Template: Curvature

- **Node Space ID:** `com.redshift3d.redshift4c4d.class.nodespace`
- **Template ID:** `com.redshift3d.redshift4c4d.nodes.core.curvature`
- **Template Name:** `Curvature`

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
Node Category | net.maxon.node.base.category | maxon::InternedId | Attribute | false | false | true |  |  | patterns | distributions = distributions, operators = operators, geometries = geometries, patterns = patterns, primitives = primitives, effectors = effectors, fields = fields, functions = functions, structures = structures, geomodifiers = geomodifiers, geogenerators = geogenerators
Preview/Node | net.maxon.node.base.nodepreviewimage | maxon::ImageBaseRef | Attribute | false | false | false |  |  |  | 
General/Consider Same Object Only | <com.redshift3d.redshift4c4d.nodes.core.curvature.sameobjectonly | maxon::Bool | Input | false | false | false |  |  | false | 
General/Mode | <com.redshift3d.redshift4c4d.nodes.core.curvature.mode | maxon::Int | Input | false | false | true |  |  | 2 | Convex (AL Curvature) = 0, Concave (AL Curvature) = 1, Convex = 2, Concave = 3
General/Num Samples | <com.redshift3d.redshift4c4d.nodes.core.curvature.numsamples | maxon::Int | Input | false | false | false | 0 | 65535 | 16 | 
General/Radius | <com.redshift3d.redshift4c4d.nodes.core.curvature.radius | maxon::Float | Input | false | false | false |  |  | 0.5 | 
Remap/Bias/Bias | <com.redshift3d.redshift4c4d.nodes.core.curvature.bias | maxon::Float | Input | false | false | false |  |  | 0.5 | 
Remap/Bias/Gain | <com.redshift3d.redshift4c4d.nodes.core.curvature.gain | maxon::Float | Input | false | false | false |  |  | 0.5 | 
Remap/Contrast/Contrast | <com.redshift3d.redshift4c4d.nodes.core.curvature.contrastval | maxon::Float | Input | false | false | false |  |  | 1 | 
Remap/Contrast/Pivot | <com.redshift3d.redshift4c4d.nodes.core.curvature.contrastpivot | maxon::Float | Input | false | false | false |  |  | 0 | 
Remap/Input Range/Max | <com.redshift3d.redshift4c4d.nodes.core.curvature.inputmax | maxon::Float | Input | false | false | false |  |  | 1 | 
Remap/Input Range/Min | <com.redshift3d.redshift4c4d.nodes.core.curvature.inputmin | maxon::Float | Input | false | false | false |  |  | 0 | 
Remap/Output Range/Clamp Enable | <com.redshift3d.redshift4c4d.nodes.core.curvature.clampenable | maxon::Bool | Input | false | false | false |  |  | false | 
Remap/Output Range/Clamp Expand | <com.redshift3d.redshift4c4d.nodes.core.curvature.clampexpand | maxon::Bool | Input | false | false | false |  |  | false | 
Remap/Output Range/Clamp Max | <com.redshift3d.redshift4c4d.nodes.core.curvature.clampmax | maxon::Float | Input | false | false | false |  |  | 1 | 
Remap/Output Range/Clamp Min | <com.redshift3d.redshift4c4d.nodes.core.curvature.clampmin | maxon::Float | Input | false | false | false |  |  | 0 | 
Remap/Output Range/Max | <com.redshift3d.redshift4c4d.nodes.core.curvature.outputmax | maxon::Float | Input | false | false | false |  |  | 1 | 
Remap/Output Range/Min | <com.redshift3d.redshift4c4d.nodes.core.curvature.outputmin | maxon::Float | Input | false | false | false |  |  | 0 | 
Outputs/out | >com.redshift3d.redshift4c4d.nodes.core.curvature.out | maxon::Float | Output | false | false | false |  |  | 0 | 

