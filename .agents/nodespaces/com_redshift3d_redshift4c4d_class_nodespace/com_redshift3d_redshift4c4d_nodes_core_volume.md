# Node Template: Volume

- **Node Space ID:** `com.redshift3d.redshift4c4d.class.nodespace`
- **Template ID:** `com.redshift3d.redshift4c4d.nodes.core.volume`
- **Template Name:** `Volume`

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
Node Category | net.maxon.node.base.category | maxon::InternedId | Attribute | false | false | true |  |  | primitives | distributions = distributions, operators = operators, geometries = geometries, patterns = patterns, primitives = primitives, effectors = effectors, fields = fields, functions = functions, structures = structures, geomodifiers = geomodifiers, geogenerators = geogenerators
Preview/Node | net.maxon.node.base.nodepreviewimage | maxon::ImageBaseRef | Attribute | false | false | false |  |  |  | 
Advanced/Density Remap Range/New Max | <com.redshift3d.redshift4c4d.nodes.core.volume.density_new_max | maxon::Float | Input | false | false | false |  |  | 1 | 
Advanced/Density Remap Range/New Min | <com.redshift3d.redshift4c4d.nodes.core.volume.density_new_min | maxon::Float | Input | false | false | false |  |  | 0 | 
Advanced/Density Remap Range/Old Max | <com.redshift3d.redshift4c4d.nodes.core.volume.density_old_max | maxon::Float | Input | false | false | false |  |  | 1 | 
Advanced/Density Remap Range/Old Min | <com.redshift3d.redshift4c4d.nodes.core.volume.density_old_min | maxon::Float | Input | false | false | false |  |  | 0 | 
Advanced/Emission Remap Range/New Max | <com.redshift3d.redshift4c4d.nodes.core.volume.emission_new_max | maxon::Float | Input | false | false | false |  |  | 1 | 
Advanced/Emission Remap Range/New Min | <com.redshift3d.redshift4c4d.nodes.core.volume.emission_new_min | maxon::Float | Input | false | false | false |  |  | 0 | 
Advanced/Emission Remap Range/Old Max | <com.redshift3d.redshift4c4d.nodes.core.volume.emission_old_max | maxon::Float | Input | false | false | false |  |  | 1 | 
Advanced/Emission Remap Range/Old Min | <com.redshift3d.redshift4c4d.nodes.core.volume.emission_old_min | maxon::Float | Input | false | false | false |  |  | 0 | 
Advanced/Multiscatter/Anisotropy Falloff | <com.redshift3d.redshift4c4d.nodes.core.volume.anisotropy_falloff | maxon::Float | Input | false | false | false | 0 | 10 | 1 | 
Advanced/Multiscatter/Extinction Falloff | <com.redshift3d.redshift4c4d.nodes.core.volume.extinction_falloff | maxon::Float | Input | false | false | false | 0 | 1 | 0.2 | 
Advanced/Multiscatter/Start Depth | <com.redshift3d.redshift4c4d.nodes.core.volume.start_depth | maxon::Int | Input | false | false | false | 0 | 31 | 1 | 
Advanced/Shadow Density Scale | <com.redshift3d.redshift4c4d.nodes.core.volume.shadow_density_scale | maxon::Float | Input | false | false | false |  |  | 1 | 
Basic/Absorption/Absorption Coefficient (1/cm) | <com.redshift3d.redshift4c4d.nodes.core.volume.absorption_coeff | maxon::Float | Input | false | false | false |  |  | 1 | 
Basic/Absorption/Absorption Remap Ramp | <com.redshift3d.redshift4c4d.nodes.core.volume.absorption_ramp | com.redshift3d.redshift4c4d.portbundle.gradient | Input | true | true | false |  |  |  | 
Basic/Absorption/Absorption Remap Ramp/Knot.1 | <com.redshift3d.redshift4c4d.nodes.core.volume.absorption_ramp/_0 | com.redshift3d.redshift4c4d.portbundle.gradient | Input | false | false | false |  |  |  | 
Basic/Absorption/Absorption Remap Ramp/Knot.1/Bias Position | <com.redshift3d.redshift4c4d.nodes.core.volume.absorption_ramp/_0/bias | maxon::Float | Input | false | false | false |  | 1 | 0.5 | 
Basic/Absorption/Absorption Remap Ramp/Knot.1/Color | <com.redshift3d.redshift4c4d.nodes.core.volume.absorption_ramp/_0/color | maxon::Color | Input | false | false | false |  |  | (1,1,1) | 
Basic/Absorption/Absorption Remap Ramp/Knot.1/Interpolation | <com.redshift3d.redshift4c4d.nodes.core.volume.absorption_ramp/_0/interpolation | maxon::InternedId | Input | false | false | true |  |  | smoothknot | Smooth = smoothknot, Cubic = cubicknot, Linear = linearknot, Step = none, Blend = blend, Cubic Bias = cubicbias
Basic/Absorption/Absorption Remap Ramp/Knot.1/Knot Position | <com.redshift3d.redshift4c4d.nodes.core.volume.absorption_ramp/_0/position | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Basic/Absorption/Absorption Remap Ramp/Knot.2 | <com.redshift3d.redshift4c4d.nodes.core.volume.absorption_ramp/_1 | com.redshift3d.redshift4c4d.portbundle.gradient | Input | false | false | false |  |  |  | 
Basic/Absorption/Absorption Remap Ramp/Knot.2/Bias Position | <com.redshift3d.redshift4c4d.nodes.core.volume.absorption_ramp/_1/bias | maxon::Float | Input | false | false | false |  | 1 | 0.5 | 
Basic/Absorption/Absorption Remap Ramp/Knot.2/Color | <com.redshift3d.redshift4c4d.nodes.core.volume.absorption_ramp/_1/color | maxon::Color | Input | false | false | false |  |  | (1,1,1) | 
Basic/Absorption/Absorption Remap Ramp/Knot.2/Interpolation | <com.redshift3d.redshift4c4d.nodes.core.volume.absorption_ramp/_1/interpolation | maxon::InternedId | Input | false | false | true |  |  | smoothknot | Smooth = smoothknot, Cubic = cubicknot, Linear = linearknot, Step = none, Blend = blend, Cubic Bias = cubicbias
Basic/Absorption/Absorption Remap Ramp/Knot.2/Knot Position | <com.redshift3d.redshift4c4d.nodes.core.volume.absorption_ramp/_1/position | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Basic/Absorption/Channel/Color Channel | <com.redshift3d.redshift4c4d.nodes.core.volume.absorption_color_name | maxon::String | Input | false | false | false |  |  |  | 
Basic/Absorption/Tint | <com.redshift3d.redshift4c4d.nodes.core.volume.absorption_tint | maxon::Color64 | Input | false | false | false |  |  | (1,1,1) | 
Basic/Emission/Channel/Channel | <com.redshift3d.redshift4c4d.nodes.core.volume.emission_name | maxon::String | Input | false | false | false |  |  |  | 
Basic/Emission/Channel/Color Channel | <com.redshift3d.redshift4c4d.nodes.core.volume.emission_color_name | maxon::String | Input | false | false | false |  |  |  | 
Basic/Emission/Color Mode | <com.redshift3d.redshift4c4d.nodes.core.volume.emission_mode | maxon::Int | Input | false | false | true |  |  | 0 | Multiply with ramp = 0, Multiply with temperature = 1, Replace = 2
Basic/Emission/Emission Mode | <com.redshift3d.redshift4c4d.nodes.core.volume.blackbody_mode | maxon::Int | Input | false | false | true |  |  | 0 | Blackbody = 0, Color Ramp = 1
Basic/Emission/Emission Remap Ramp | <com.redshift3d.redshift4c4d.nodes.core.volume.emission_ramp | com.redshift3d.redshift4c4d.portbundle.gradient | Input | true | true | false |  |  |  | 
Basic/Emission/Emission Remap Ramp/Knot.1 | <com.redshift3d.redshift4c4d.nodes.core.volume.emission_ramp/_0 | com.redshift3d.redshift4c4d.portbundle.gradient | Input | false | false | false |  |  |  | 
Basic/Emission/Emission Remap Ramp/Knot.1/Bias Position | <com.redshift3d.redshift4c4d.nodes.core.volume.emission_ramp/_0/bias | maxon::Float | Input | false | false | false |  | 1 | 0.5 | 
Basic/Emission/Emission Remap Ramp/Knot.1/Color | <com.redshift3d.redshift4c4d.nodes.core.volume.emission_ramp/_0/color | maxon::Color | Input | false | false | false |  |  | (1,1,1) | 
Basic/Emission/Emission Remap Ramp/Knot.1/Interpolation | <com.redshift3d.redshift4c4d.nodes.core.volume.emission_ramp/_0/interpolation | maxon::InternedId | Input | false | false | true |  |  | smoothknot | Smooth = smoothknot, Cubic = cubicknot, Linear = linearknot, Step = none, Blend = blend, Cubic Bias = cubicbias
Basic/Emission/Emission Remap Ramp/Knot.1/Knot Position | <com.redshift3d.redshift4c4d.nodes.core.volume.emission_ramp/_0/position | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Basic/Emission/Emission Remap Ramp/Knot.2 | <com.redshift3d.redshift4c4d.nodes.core.volume.emission_ramp/_1 | com.redshift3d.redshift4c4d.portbundle.gradient | Input | false | false | false |  |  |  | 
Basic/Emission/Emission Remap Ramp/Knot.2/Bias Position | <com.redshift3d.redshift4c4d.nodes.core.volume.emission_ramp/_1/bias | maxon::Float | Input | false | false | false |  | 1 | 0.5 | 
Basic/Emission/Emission Remap Ramp/Knot.2/Color | <com.redshift3d.redshift4c4d.nodes.core.volume.emission_ramp/_1/color | maxon::Color | Input | false | false | false |  |  | (1,1,1) | 
Basic/Emission/Emission Remap Ramp/Knot.2/Interpolation | <com.redshift3d.redshift4c4d.nodes.core.volume.emission_ramp/_1/interpolation | maxon::InternedId | Input | false | false | true |  |  | smoothknot | Smooth = smoothknot, Cubic = cubicknot, Linear = linearknot, Step = none, Blend = blend, Cubic Bias = cubicbias
Basic/Emission/Emission Remap Ramp/Knot.2/Knot Position | <com.redshift3d.redshift4c4d.nodes.core.volume.emission_ramp/_1/position | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Basic/Emission/Offset | <com.redshift3d.redshift4c4d.nodes.core.volume.blackbody_offset | maxon::Float | Input | false | false | false |  |  | 1 | 
Basic/Emission/Scale | <com.redshift3d.redshift4c4d.nodes.core.volume.emission_scale | maxon::Float | Input | false | false | false |  |  | 1 | 
Basic/Emission/Temperature | <com.redshift3d.redshift4c4d.nodes.core.volume.blackbody_temperature | maxon::Float | Input | false | false | false |  |  | 6500 | 
Basic/Emission/Tint | <com.redshift3d.redshift4c4d.nodes.core.volume.emission_tint | maxon::Color64 | Input | false | false | false |  |  | (1,1,1) | 
Basic/Scatter/Anisotropy | <com.redshift3d.redshift4c4d.nodes.core.volume.anisotropy | maxon::Float | Input | false | false | false | -1 | 1 | 0 | 
Basic/Scatter/Anisotropy Mode | <com.redshift3d.redshift4c4d.nodes.core.volume.anisotropy_mode | maxon::Int | Input | false | false | true |  |  | 0 | Henyey-Greenstein = 0, Jendersie d'Eon = 1
Basic/Scatter/Channel/Channel | <com.redshift3d.redshift4c4d.nodes.core.volume.density_name | maxon::String | Input | false | false | false |  |  |  | 
Basic/Scatter/Channel/Color Channel | <com.redshift3d.redshift4c4d.nodes.core.volume.scatter_color_name | maxon::String | Input | false | false | false |  |  |  | 
Basic/Scatter/Diameter | <com.redshift3d.redshift4c4d.nodes.core.volume.diameter | maxon::Float | Input | false | false | false | 0 | 50 | 5 | 
Basic/Scatter/Scatter Coefficient (1/cm) | <com.redshift3d.redshift4c4d.nodes.core.volume.scatter_coeff | maxon::Float | Input | false | false | false |  |  | 1 | 
Basic/Scatter/Scatter Remap Ramp | <com.redshift3d.redshift4c4d.nodes.core.volume.scatter_ramp | com.redshift3d.redshift4c4d.portbundle.gradient | Input | true | true | false |  |  |  | 
Basic/Scatter/Scatter Remap Ramp/Knot.1 | <com.redshift3d.redshift4c4d.nodes.core.volume.scatter_ramp/_0 | com.redshift3d.redshift4c4d.portbundle.gradient | Input | false | false | false |  |  |  | 
Basic/Scatter/Scatter Remap Ramp/Knot.1/Bias Position | <com.redshift3d.redshift4c4d.nodes.core.volume.scatter_ramp/_0/bias | maxon::Float | Input | false | false | false |  | 1 | 0.5 | 
Basic/Scatter/Scatter Remap Ramp/Knot.1/Color | <com.redshift3d.redshift4c4d.nodes.core.volume.scatter_ramp/_0/color | maxon::Color | Input | false | false | false |  |  | (1,1,1) | 
Basic/Scatter/Scatter Remap Ramp/Knot.1/Interpolation | <com.redshift3d.redshift4c4d.nodes.core.volume.scatter_ramp/_0/interpolation | maxon::InternedId | Input | false | false | true |  |  | smoothknot | Smooth = smoothknot, Cubic = cubicknot, Linear = linearknot, Step = none, Blend = blend, Cubic Bias = cubicbias
Basic/Scatter/Scatter Remap Ramp/Knot.1/Knot Position | <com.redshift3d.redshift4c4d.nodes.core.volume.scatter_ramp/_0/position | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Basic/Scatter/Scatter Remap Ramp/Knot.2 | <com.redshift3d.redshift4c4d.nodes.core.volume.scatter_ramp/_1 | com.redshift3d.redshift4c4d.portbundle.gradient | Input | false | false | false |  |  |  | 
Basic/Scatter/Scatter Remap Ramp/Knot.2/Bias Position | <com.redshift3d.redshift4c4d.nodes.core.volume.scatter_ramp/_1/bias | maxon::Float | Input | false | false | false |  | 1 | 0.5 | 
Basic/Scatter/Scatter Remap Ramp/Knot.2/Color | <com.redshift3d.redshift4c4d.nodes.core.volume.scatter_ramp/_1/color | maxon::Color | Input | false | false | false |  |  | (1,1,1) | 
Basic/Scatter/Scatter Remap Ramp/Knot.2/Interpolation | <com.redshift3d.redshift4c4d.nodes.core.volume.scatter_ramp/_1/interpolation | maxon::InternedId | Input | false | false | true |  |  | smoothknot | Smooth = smoothknot, Cubic = cubicknot, Linear = linearknot, Step = none, Blend = blend, Cubic Bias = cubicbias
Basic/Scatter/Scatter Remap Ramp/Knot.2/Knot Position | <com.redshift3d.redshift4c4d.nodes.core.volume.scatter_ramp/_1/position | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Basic/Scatter/Tint | <com.redshift3d.redshift4c4d.nodes.core.volume.scatter_tint | maxon::Color64 | Input | false | false | false |  |  | (1,1,1) | 
Outputs/outColor | >com.redshift3d.redshift4c4d.nodes.core.volume.outcolor | maxon::ColorA64 | Output | false | false | false |  |  | (0,0,0,1) | 

