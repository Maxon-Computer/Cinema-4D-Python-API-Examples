# Node Template: Ramp

- **Node Space ID:** `com.redshift3d.redshift4c4d.class.nodespace`
- **Template ID:** `com.redshift3d.redshift4c4d.nodes.core.rsramp`
- **Template Name:** `Ramp`

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
Node Category | net.maxon.node.base.category | maxon::InternedId | Attribute | false | false | true |  |  | patterns | operators = operators, distributions = distributions, geometries = geometries, patterns = patterns, primitives = primitives, effectors = effectors, fields = fields, functions = functions, structures = structures, geomodifiers = geomodifiers, geogenerators = geogenerators
Preview/Node | net.maxon.node.base.nodepreviewimage | maxon::ImageBaseRef | Attribute | false | false | false |  |  |  | 
General/Input/Adjust/Exposure | <com.redshift3d.redshift4c4d.nodes.core.rsramp.exposure | maxon::Float | Input | false | false | false |  |  | 0 | 
General/Input/Adjust/Invert | <com.redshift3d.redshift4c4d.nodes.core.rsramp.inputinvert | maxon::Bool | Input | false | false | false |  |  | false | 
General/Input/Adjust/New Range Max | <com.redshift3d.redshift4c4d.nodes.core.rsramp.new_max | maxon::Float | Input | false | false | false |  |  | 1 | 
General/Input/Adjust/New Range Min | <com.redshift3d.redshift4c4d.nodes.core.rsramp.new_min | maxon::Float | Input | false | false | false |  |  | 0 | 
General/Input/Adjust/Noise Amount | <com.redshift3d.redshift4c4d.nodes.core.rsramp.noise | maxon::Float | Input | false | false | false |  |  | 0 | 
General/Input/Adjust/Noise Frequency | <com.redshift3d.redshift4c4d.nodes.core.rsramp.noisefreq | maxon::Float | Input | false | false | false |  |  | 1 | 
General/Input/Adjust/Old Range Max | <com.redshift3d.redshift4c4d.nodes.core.rsramp.old_max | maxon::Float | Input | false | false | false |  |  | 1 | 
General/Input/Adjust/Old Range Min | <com.redshift3d.redshift4c4d.nodes.core.rsramp.old_min | maxon::Float | Input | false | false | false |  |  | 0 | 
General/Input/Alt Input | <com.redshift3d.redshift4c4d.nodes.core.rsramp.input | maxon::Float | Input | false | false | false |  |  | 0 | 
General/Input/Mapping | <com.redshift3d.redshift4c4d.nodes.core.rsramp.inputmapping | maxon::Int | Input | false | false | true |  |  | 0 | Vertical = 0, Horizontal = 1, Diagonal = 2, Circular = 4, Radial = 3
General/Input/Source | <com.redshift3d.redshift4c4d.nodes.core.rsramp.inputsource | maxon::Int | Input | false | false | true |  |  | 2 | UV Map = 0, Alt = 1, Auto = 2
General/Input/Texture Space | <com.redshift3d.redshift4c4d.nodes.core.rsramp.tspace_id | maxon::String | Input | false | false | false |  |  |  | 
General/Input/UV Context | <com.redshift3d.redshift4c4d.nodes.core.rsramp.uv_context | RSC4D::UVContext | Input | false | false | false |  |  |  | 
General/Ramp/Interpolation Type | <com.redshift3d.redshift4c4d.nodes.core.rsramp.ramp_interp | maxon::Int | Input | false | false | true |  |  | 1 | Step = 0, Linear = 1, Smooth = 2, Spline = 3
General/Ramp/Ramp | <com.redshift3d.redshift4c4d.nodes.core.rsramp.ramp | com.redshift3d.redshift4c4d.portbundle.gradient | Input | true | true | false |  |  |  | 
General/Ramp/Ramp/Knot.1 | <com.redshift3d.redshift4c4d.nodes.core.rsramp.ramp/_0 | com.redshift3d.redshift4c4d.portbundle.gradient | Input | false | false | false |  |  |  | 
General/Ramp/Ramp/Knot.1/Bias Position | <com.redshift3d.redshift4c4d.nodes.core.rsramp.ramp/_0/bias | maxon::Float | Input | false | false | false |  | 1 | 0.5 | 
General/Ramp/Ramp/Knot.1/Color | <com.redshift3d.redshift4c4d.nodes.core.rsramp.ramp/_0/color | maxon::Color | Input | false | false | false |  |  | (1,1,1) | 
General/Ramp/Ramp/Knot.1/Interpolation | <com.redshift3d.redshift4c4d.nodes.core.rsramp.ramp/_0/interpolation | maxon::InternedId | Input | false | false | true |  |  | smoothknot | Smooth = smoothknot, Cubic = cubicknot, Linear = linearknot, Step = none, Blend = blend, Cubic Bias = cubicbias
General/Ramp/Ramp/Knot.1/Knot Position | <com.redshift3d.redshift4c4d.nodes.core.rsramp.ramp/_0/position | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
General/Ramp/Ramp/Knot.2 | <com.redshift3d.redshift4c4d.nodes.core.rsramp.ramp/_1 | com.redshift3d.redshift4c4d.portbundle.gradient | Input | false | false | false |  |  |  | 
General/Ramp/Ramp/Knot.2/Bias Position | <com.redshift3d.redshift4c4d.nodes.core.rsramp.ramp/_1/bias | maxon::Float | Input | false | false | false |  | 1 | 0.5 | 
General/Ramp/Ramp/Knot.2/Color | <com.redshift3d.redshift4c4d.nodes.core.rsramp.ramp/_1/color | maxon::Color | Input | false | false | false |  |  | (1,1,1) | 
General/Ramp/Ramp/Knot.2/Interpolation | <com.redshift3d.redshift4c4d.nodes.core.rsramp.ramp/_1/interpolation | maxon::InternedId | Input | false | false | true |  |  | smoothknot | Smooth = smoothknot, Cubic = cubicknot, Linear = linearknot, Step = none, Blend = blend, Cubic Bias = cubicbias
General/Ramp/Ramp/Knot.2/Knot Position | <com.redshift3d.redshift4c4d.nodes.core.rsramp.ramp/_1/position | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Outputs/outColor | >com.redshift3d.redshift4c4d.nodes.core.rsramp.outcolor | maxon::Color64 | Output | false | false | false |  |  | (0,0,0) | 

