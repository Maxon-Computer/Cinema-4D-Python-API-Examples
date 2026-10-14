# Node Template: Material Blender

- **Node Space ID:** `com.redshift3d.redshift4c4d.class.nodespace`
- **Template ID:** `com.redshift3d.redshift4c4d.nodes.core.materialblender`
- **Template Name:** `Material Blender`

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
Node Category | net.maxon.node.base.category | maxon::InternedId | Attribute | false | false | true |  |  | primitives | operators = operators, distributions = distributions, geometries = geometries, patterns = patterns, primitives = primitives, effectors = effectors, fields = fields, functions = functions, structures = structures, geomodifiers = geomodifiers, geogenerators = geogenerators
Preview/Node | net.maxon.node.base.nodepreviewimage | maxon::ImageBaseRef | Attribute | false | false | false |  |  |  | 
Inputs/Base Material/Color | <com.redshift3d.redshift4c4d.nodes.core.materialblender.basecolor | maxon::Color64 | Input | false | false | false |  |  |  | 
Inputs/Layer 1/Additive | <com.redshift3d.redshift4c4d.nodes.core.materialblender.additivemode1 | maxon::Bool | Input | false | false | false |  |  | false | 
Inputs/Layer 1/Blend Color | <com.redshift3d.redshift4c4d.nodes.core.materialblender.blendcolor1 | maxon::Color64 | Input | false | false | false |  |  | (0,0,0) | 
Inputs/Layer 1/Material Color | <com.redshift3d.redshift4c4d.nodes.core.materialblender.layercolor1 | maxon::Color64 | Input | false | false | false |  |  |  | 
Inputs/Layer 2/Additive | <com.redshift3d.redshift4c4d.nodes.core.materialblender.additivemode2 | maxon::Bool | Input | false | false | false |  |  | false | 
Inputs/Layer 2/Blend Color | <com.redshift3d.redshift4c4d.nodes.core.materialblender.blendcolor2 | maxon::Color64 | Input | false | false | false |  |  | (0,0,0) | 
Inputs/Layer 2/Material Color | <com.redshift3d.redshift4c4d.nodes.core.materialblender.layercolor2 | maxon::Color64 | Input | false | false | false |  |  |  | 
Inputs/Layer 3/Additive | <com.redshift3d.redshift4c4d.nodes.core.materialblender.additivemode3 | maxon::Bool | Input | false | false | false |  |  | false | 
Inputs/Layer 3/Blend Color | <com.redshift3d.redshift4c4d.nodes.core.materialblender.blendcolor3 | maxon::Color64 | Input | false | false | false |  |  | (0,0,0) | 
Inputs/Layer 3/Material Color | <com.redshift3d.redshift4c4d.nodes.core.materialblender.layercolor3 | maxon::Color64 | Input | false | false | false |  |  |  | 
Inputs/Layer 4/Additive | <com.redshift3d.redshift4c4d.nodes.core.materialblender.additivemode4 | maxon::Bool | Input | false | false | false |  |  | false | 
Inputs/Layer 4/Blend Color | <com.redshift3d.redshift4c4d.nodes.core.materialblender.blendcolor4 | maxon::Color64 | Input | false | false | false |  |  | (0,0,0) | 
Inputs/Layer 4/Material Color | <com.redshift3d.redshift4c4d.nodes.core.materialblender.layercolor4 | maxon::Color64 | Input | false | false | false |  |  |  | 
Inputs/Layer 5/Additive | <com.redshift3d.redshift4c4d.nodes.core.materialblender.additivemode5 | maxon::Bool | Input | false | false | false |  |  | false | 
Inputs/Layer 5/Blend Color | <com.redshift3d.redshift4c4d.nodes.core.materialblender.blendcolor5 | maxon::Color64 | Input | false | false | false |  |  | (0,0,0) | 
Inputs/Layer 5/Material Color | <com.redshift3d.redshift4c4d.nodes.core.materialblender.layercolor5 | maxon::Color64 | Input | false | false | false |  |  |  | 
Inputs/Layer 6/Additive | <com.redshift3d.redshift4c4d.nodes.core.materialblender.additivemode6 | maxon::Bool | Input | false | false | false |  |  | false | 
Inputs/Layer 6/Blend Color | <com.redshift3d.redshift4c4d.nodes.core.materialblender.blendcolor6 | maxon::Color64 | Input | false | false | false |  |  | (0,0,0) | 
Inputs/Layer 6/Material Color | <com.redshift3d.redshift4c4d.nodes.core.materialblender.layercolor6 | maxon::Color64 | Input | false | false | false |  |  |  | 
Outputs/out | >com.redshift3d.redshift4c4d.nodes.core.materialblender.out | maxon::Color64 | Output | false | false | false |  |  | (0,0,0) | 

