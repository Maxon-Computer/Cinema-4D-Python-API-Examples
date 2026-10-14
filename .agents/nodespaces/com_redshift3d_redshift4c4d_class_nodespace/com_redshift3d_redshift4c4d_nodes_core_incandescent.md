# Node Template: Incandescent

- **Node Space ID:** `com.redshift3d.redshift4c4d.class.nodespace`
- **Template ID:** `com.redshift3d.redshift4c4d.nodes.core.incandescent`
- **Template Name:** `Incandescent`

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
AOVs/Affect Emission AOV | <com.redshift3d.redshift4c4d.nodes.core.incandescent.affectemissionaov | maxon::Bool | Input | false | false | false |  |  | true | 
Illumination/Alpha/Additive Blend | <com.redshift3d.redshift4c4d.nodes.core.incandescent.additive_blend | maxon::Bool | Input | false | false | false |  |  | false | 
Illumination/Alpha/Alpha | <com.redshift3d.redshift4c4d.nodes.core.incandescent.alpha | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Illumination/Alpha/Alpha Mode | <com.redshift3d.redshift4c4d.nodes.core.incandescent.alphamode | maxon::Int | Input | false | false | true |  |  | 1 | Replace = 0, Ray-Traced Opacity = 1
Illumination/Alpha/Transparent Shadows | <com.redshift3d.redshift4c4d.nodes.core.incandescent.transparentshadows | maxon::Bool | Input | false | false | false |  |  | false | 
Illumination/Apply Camera Exposure Compensation | <com.redshift3d.redshift4c4d.nodes.core.incandescent.applyexposurecompensation | maxon::Bool | Input | false | false | false |  |  | false | 
Illumination/Color | <com.redshift3d.redshift4c4d.nodes.core.incandescent.color | maxon::Color64 | Input | false | false | false |  |  | (1,1,1) | 
Illumination/Double-Sided | <com.redshift3d.redshift4c4d.nodes.core.incandescent.doublesided | maxon::Bool | Input | false | false | false |  |  | true | 
Illumination/Mode | <com.redshift3d.redshift4c4d.nodes.core.incandescent.colormode | maxon::Int | Input | false | false | true |  |  | 0 | Color = 0, Temperature = 1
Illumination/Radiance (W/sr/m^2) | <com.redshift3d.redshift4c4d.nodes.core.incandescent.intensity | maxon::Float | Input | false | false | false | 0 | 200000 | 1 | 
Illumination/Temperature | <com.redshift3d.redshift4c4d.nodes.core.incandescent.temperature | maxon::Float | Input | false | false | false | 1000 | 20000 | 6500 | 
Ray Type Intensity Multipliers/GI | <com.redshift3d.redshift4c4d.nodes.core.incandescent.giscale | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Ray Type Intensity Multipliers/Reflection | <com.redshift3d.redshift4c4d.nodes.core.incandescent.reflectscale | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Ray Type Intensity Multipliers/Refraction | <com.redshift3d.redshift4c4d.nodes.core.incandescent.refractscale | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Outputs/outColor | >com.redshift3d.redshift4c4d.nodes.core.incandescent.outcolor | maxon::Color64 | Output | false | false | false |  |  | (0,0,0) | 

