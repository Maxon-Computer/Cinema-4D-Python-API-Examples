# Node Template: Hair

- **Node Space ID:** `com.redshift3d.redshift4c4d.class.nodespace`
- **Template ID:** `com.redshift3d.redshift4c4d.nodes.core.hair`
- **Template Name:** `Hair`

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
Advanced/Balance Diffuse/Reflection Energy | <com.redshift3d.redshift4c4d.nodes.core.hair.balanceenergy | maxon::Bool | Input | false | false | false |  |  | true | 
Advanced/Combined Trace Depth | <com.redshift3d.redshift4c4d.nodes.core.hair.combined_depth | maxon::Int | Input | false | false | false | 0 | 16 | 16 | 
Advanced/Enable Trace Depth Overrides | <com.redshift3d.redshift4c4d.nodes.core.hair.depth_override | maxon::Bool | Input | false | false | false |  |  | false | 
Advanced/Reflection/Cut-off Override/Enable | <com.redshift3d.redshift4c4d.nodes.core.hair.refl_enablecutoff | maxon::Bool | Input | false | false | false |  |  | false | 
Advanced/Reflection/Cut-off Override/Threshold | <com.redshift3d.redshift4c4d.nodes.core.hair.refl_cutoff | maxon::Float | Input | false | false | false | 0 | 1 | 0.01 | 
Advanced/Reflection/Trace Depth | <com.redshift3d.redshift4c4d.nodes.core.hair.refl_depth | maxon::Int | Input | false | false | false | 1 | 63 | 1 | 
Advanced/ShaveCompatibility | <com.redshift3d.redshift4c4d.nodes.core.hair.shavecompatibility | maxon::Bool | Input | false | false | false |  |  | false | 
Advanced/Transparency/Trace Depth | <com.redshift3d.redshift4c4d.nodes.core.hair.trans_depth | maxon::Int | Input | false | false | false | 1 | 255 | 16 | 
Advanced/Transparency/Transparency Cut-off Override/Enable | <com.redshift3d.redshift4c4d.nodes.core.hair.trans_enablecutoff | maxon::Bool | Input | false | false | false |  |  | false | 
Advanced/Transparency/Transparency Cut-off Override/Threshold | <com.redshift3d.redshift4c4d.nodes.core.hair.trans_cutoff | maxon::Float | Input | false | false | false | 0 | 1 | 0.01 | 
General/Diffuse/Color | <com.redshift3d.redshift4c4d.nodes.core.hair.diffuse_color | maxon::Color64 | Input | false | false | false |  |  | (1,0.5,0.2) | 
General/Diffuse/Translucency Weight | <com.redshift3d.redshift4c4d.nodes.core.hair.diffusetrans_weight | maxon::Float | Input | false | false | false | 0 | 1 | 0 | 
General/Diffuse/Weight | <com.redshift3d.redshift4c4d.nodes.core.hair.diffuse_weight | maxon::Float | Input | false | false | false | 0 | 1 | 0 | 
General/Internal Reflection/Color | <com.redshift3d.redshift4c4d.nodes.core.hair.irefl_color | maxon::Color64 | Input | false | false | false |  |  | (1,0.5,0.2) | 
General/Internal Reflection/Glossiness | <com.redshift3d.redshift4c4d.nodes.core.hair.irefl_gloss | maxon::Float | Input | false | false | false | 0 | 1 | 0.6 | 
General/Internal Reflection/Highlights Only | <com.redshift3d.redshift4c4d.nodes.core.hair.irefl_norefl | maxon::Bool | Input | false | false | false |  |  | false | 
General/Internal Reflection/Samples | <com.redshift3d.redshift4c4d.nodes.core.hair.irefl_samples | maxon::Int | Input | false | false | false | 0 | 65535 | 16 | 
General/Internal Reflection/Weight | <com.redshift3d.redshift4c4d.nodes.core.hair.irefl_weight | maxon::Float | Input | false | false | false |  |  | 0.5 | 
General/Primary Reflection/Angular Shift | <com.redshift3d.redshift4c4d.nodes.core.hair.angularshift | maxon::Float | Input | false | false | false | -10 | 10 | -5 | 
General/Primary Reflection/Color | <com.redshift3d.redshift4c4d.nodes.core.hair.refl_color | maxon::Color64 | Input | false | false | false |  |  | (1,1,1) | 
General/Primary Reflection/Enable Fresnel | <com.redshift3d.redshift4c4d.nodes.core.hair.applyfresnel | maxon::Bool | Input | false | false | false |  |  | false | 
General/Primary Reflection/Glossiness | <com.redshift3d.redshift4c4d.nodes.core.hair.refl_gloss | maxon::Float | Input | false | false | false | 0 | 1 | 0.85 | 
General/Primary Reflection/Highlights Only | <com.redshift3d.redshift4c4d.nodes.core.hair.refl_norefl | maxon::Bool | Input | false | false | false |  |  | false | 
General/Primary Reflection/IOR | <com.redshift3d.redshift4c4d.nodes.core.hair.ior | maxon::Float | Input | false | false | false | 1 | 100 | 1.55 | 
General/Primary Reflection/Samples | <com.redshift3d.redshift4c4d.nodes.core.hair.refl_samples | maxon::Int | Input | false | false | false | 0 | 65535 | 16 | 
General/Primary Reflection/Weight | <com.redshift3d.redshift4c4d.nodes.core.hair.refl_weight | maxon::Float | Input | false | false | false |  |  | 0.1 | 
General/Transmission/Color | <com.redshift3d.redshift4c4d.nodes.core.hair.trans_color | maxon::Color64 | Input | false | false | false |  |  | (1,0.5,0.2) | 
General/Transmission/Length Glossiness | <com.redshift3d.redshift4c4d.nodes.core.hair.trans_lgloss | maxon::Float | Input | false | false | false | 0 | 1 | 0.9 | 
General/Transmission/Weight | <com.redshift3d.redshift4c4d.nodes.core.hair.trans_weight | maxon::Float | Input | false | false | false |  |  | 0.5 | 
General/Transmission/Width Glossiness | <com.redshift3d.redshift4c4d.nodes.core.hair.trans_wgloss | maxon::Float | Input | false | false | false | 0 | 1 | 0.5 | 
Transparency/Transparency/Color | <com.redshift3d.redshift4c4d.nodes.core.hair.transp_color | maxon::Color64 | Input | false | false | false |  |  | (1,1,1) | 
Transparency/Transparency/Weight | <com.redshift3d.redshift4c4d.nodes.core.hair.transp_weight | maxon::Float | Input | false | false | false | 0 | 1 | 0 | 
Outputs/outColor | >com.redshift3d.redshift4c4d.nodes.core.hair.outcolor | maxon::Color64 | Output | false | false | false |  |  | (0,0,0) | 

