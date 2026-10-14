# Node Template: TriPlanar

- **Node Space ID:** `com.redshift3d.redshift4c4d.class.nodespace`
- **Template ID:** `com.redshift3d.redshift4c4d.nodes.core.triplanar`
- **Template Name:** `TriPlanar`

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
Inputs/Coordinates/Offset | <com.redshift3d.redshift4c4d.nodes.core.triplanar.offset | maxon::Vector64 | Input | false | false | false |  |  | (0,0,0) | 
Inputs/Coordinates/Projection Space Type | <com.redshift3d.redshift4c4d.nodes.core.triplanar.projspacetype | maxon::Int | Input | false | false | true |  |  | 1 | World = 0, Object = 1, Reference = 2
Inputs/Coordinates/Rotation | <com.redshift3d.redshift4c4d.nodes.core.triplanar.rotation | maxon::Vector64 | Input | false | false | false |  |  | (0,0,0) | 
Inputs/Coordinates/Scale | <com.redshift3d.redshift4c4d.nodes.core.triplanar.scale | maxon::Vector64 | Input | false | false | false |  |  | (0.01,0.01,0.01) | 
Inputs/Coordinates/World Space Unit | <com.redshift3d.redshift4c4d.nodes.core.triplanar.worldspaceunit | maxon::Int | Input | false | false | true |  |  | 65536 | Centimeters = 2, Kilometers = 0, Automatic = 65536, Meters = 1, Millimeters = 3, Feet = 8, Micrometers = 4, Miles = 6, Nanometers = 5, Yards = 7, Inches = 9
Inputs/IsLeftHanded | <com.redshift3d.redshift4c4d.nodes.core.triplanar.islefthanded | maxon::Bool | Input | false | false | false |  |  | true | 
Inputs/Texture/Blend Amount | <com.redshift3d.redshift4c4d.nodes.core.triplanar.blendamount | maxon::Float | Input | false | false | false | 0 | 1 | 0.1 | 
Inputs/Texture/Blend Curve | <com.redshift3d.redshift4c4d.nodes.core.triplanar.blendcurve | maxon::Float | Input | false | false | false | 1 | 100 | 2 | 
Inputs/Texture/Image X | <com.redshift3d.redshift4c4d.nodes.core.triplanar.imagex | maxon::ColorA64 | Input | false | false | false |  |  | (1,0,0,1) | 
Inputs/Texture/Image Y | <com.redshift3d.redshift4c4d.nodes.core.triplanar.imagey | maxon::ColorA64 | Input | false | false | false |  |  | (0,1,0,1) | 
Inputs/Texture/Image Z | <com.redshift3d.redshift4c4d.nodes.core.triplanar.imagez | maxon::ColorA64 | Input | false | false | false |  |  | (0,0,1,1) | 
Inputs/Texture/Same Image On Each Axis | <com.redshift3d.redshift4c4d.nodes.core.triplanar.sameimageoneachaxis | maxon::Bool | Input | false | false | false |  |  | true | 
Inputs/YIsUp | <com.redshift3d.redshift4c4d.nodes.core.triplanar.yisup | maxon::Bool | Input | false | false | false |  |  | true | 
Outputs/outColor | >com.redshift3d.redshift4c4d.nodes.core.triplanar.outcolor | maxon::ColorA64 | Output | false | false | false |  |  | (0,0,0,1) | 

