# Node Template: Pavement

- **Node Space ID:** `com.redshift3d.redshift4c4d.class.nodespace`
- **Template ID:** `com.redshift3d.redshift4c4d.nodes.core.pavement`
- **Template Name:** `Pavement`

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
Shader/Dimensions/Scale | <com.redshift3d.redshift4c4d.nodes.core.pavement.scaleinput | maxon::Float | Input | false | false | false | 0 | 2147483648 | 1 | 
Shader/Dimensions/Seed | <com.redshift3d.redshift4c4d.nodes.core.pavement.seedinput | maxon::Int | Input | false | false | false |  |  | 123 | 
Shader/Dimensions/UV Channel | <com.redshift3d.redshift4c4d.nodes.core.pavement.tspace_id | maxon::String | Input | false | false | false |  |  |  | 
Shader/Dimensions/UV Context | <com.redshift3d.redshift4c4d.nodes.core.pavement.uv_context | RSC4D::UVContext | Input | false | false | false |  |  |  | 
Shader/Gap Color/Contrast Grain | <com.redshift3d.redshift4c4d.nodes.core.pavement.contrastgraininput | maxon::Bool | Input | false | false | false |  |  | false | 
Shader/Gap Color/Gap Color | <com.redshift3d.redshift4c4d.nodes.core.pavement.gapcolorinput | com.redshift3d.redshift4c4d.portbundle.gradient | Input | true | true | false |  |  |  | 
Shader/Gap Color/Gap Color/Knot.1 | <com.redshift3d.redshift4c4d.nodes.core.pavement.gapcolorinput/_0 | com.redshift3d.redshift4c4d.portbundle.gradient | Input | false | false | false |  |  |  | 
Shader/Gap Color/Gap Color/Knot.1/Bias Position | <com.redshift3d.redshift4c4d.nodes.core.pavement.gapcolorinput/_0/bias | maxon::Float | Input | false | false | false |  | 1 | 0.5 | 
Shader/Gap Color/Gap Color/Knot.1/Color | <com.redshift3d.redshift4c4d.nodes.core.pavement.gapcolorinput/_0/color | maxon::Color | Input | false | false | false |  |  | (1,1,1) | 
Shader/Gap Color/Gap Color/Knot.1/Interpolation | <com.redshift3d.redshift4c4d.nodes.core.pavement.gapcolorinput/_0/interpolation | maxon::InternedId | Input | false | false | true |  |  | smoothknot | Smooth = smoothknot, Cubic = cubicknot, Linear = linearknot, Step = none, Blend = blend, Cubic Bias = cubicbias
Shader/Gap Color/Gap Color/Knot.1/Knot Position | <com.redshift3d.redshift4c4d.nodes.core.pavement.gapcolorinput/_0/position | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Shader/Gap Color/Gap Color/Knot.2 | <com.redshift3d.redshift4c4d.nodes.core.pavement.gapcolorinput/_1 | com.redshift3d.redshift4c4d.portbundle.gradient | Input | false | false | false |  |  |  | 
Shader/Gap Color/Gap Color/Knot.2/Bias Position | <com.redshift3d.redshift4c4d.nodes.core.pavement.gapcolorinput/_1/bias | maxon::Float | Input | false | false | false |  | 1 | 0.5 | 
Shader/Gap Color/Gap Color/Knot.2/Color | <com.redshift3d.redshift4c4d.nodes.core.pavement.gapcolorinput/_1/color | maxon::Color | Input | false | false | false |  |  | (1,1,1) | 
Shader/Gap Color/Gap Color/Knot.2/Interpolation | <com.redshift3d.redshift4c4d.nodes.core.pavement.gapcolorinput/_1/interpolation | maxon::InternedId | Input | false | false | true |  |  | smoothknot | Smooth = smoothknot, Cubic = cubicknot, Linear = linearknot, Step = none, Blend = blend, Cubic Bias = cubicbias
Shader/Gap Color/Gap Color/Knot.2/Knot Position | <com.redshift3d.redshift4c4d.nodes.core.pavement.gapcolorinput/_1/position | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Shader/Gap Color/Grainy Gaps | <com.redshift3d.redshift4c4d.nodes.core.pavement.grainygapsinput | maxon::Float | Input | false | false | false | 0 | 1 | 0.3 | 
Shader/Gaps/Crookedness | <com.redshift3d.redshift4c4d.nodes.core.pavement.crookednessinput | maxon::Float | Input | false | false | false | 0 | 2147483648 | 0.05 | 
Shader/Gaps/Crookedness Scale | <com.redshift3d.redshift4c4d.nodes.core.pavement.crookednessscaleinput | maxon::Float | Input | false | false | false | 0 | 2147483648 | 1 | 
Shader/Gaps/Softness | <com.redshift3d.redshift4c4d.nodes.core.pavement.softinput | maxon::Float | Input | false | false | false | 0 | 2 | 0.15 | 
Shader/Gaps/Width | <com.redshift3d.redshift4c4d.nodes.core.pavement.widthinput | maxon::Float | Input | false | false | false | 0.01 | 1 | 0.08 | 
Shader/Smudgy Color/Smudgy Color | <com.redshift3d.redshift4c4d.nodes.core.pavement.smudgycolorinput | com.redshift3d.redshift4c4d.portbundle.gradient | Input | true | true | false |  |  |  | 
Shader/Smudgy Color/Smudgy Color/Knot.1 | <com.redshift3d.redshift4c4d.nodes.core.pavement.smudgycolorinput/_0 | com.redshift3d.redshift4c4d.portbundle.gradient | Input | false | false | false |  |  |  | 
Shader/Smudgy Color/Smudgy Color/Knot.1/Bias Position | <com.redshift3d.redshift4c4d.nodes.core.pavement.smudgycolorinput/_0/bias | maxon::Float | Input | false | false | false |  | 1 | 0.5 | 
Shader/Smudgy Color/Smudgy Color/Knot.1/Color | <com.redshift3d.redshift4c4d.nodes.core.pavement.smudgycolorinput/_0/color | maxon::Color | Input | false | false | false |  |  | (1,1,1) | 
Shader/Smudgy Color/Smudgy Color/Knot.1/Interpolation | <com.redshift3d.redshift4c4d.nodes.core.pavement.smudgycolorinput/_0/interpolation | maxon::InternedId | Input | false | false | true |  |  | smoothknot | Smooth = smoothknot, Cubic = cubicknot, Linear = linearknot, Step = none, Blend = blend, Cubic Bias = cubicbias
Shader/Smudgy Color/Smudgy Color/Knot.1/Knot Position | <com.redshift3d.redshift4c4d.nodes.core.pavement.smudgycolorinput/_0/position | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Shader/Smudgy Color/Smudgy Color/Knot.2 | <com.redshift3d.redshift4c4d.nodes.core.pavement.smudgycolorinput/_1 | com.redshift3d.redshift4c4d.portbundle.gradient | Input | false | false | false |  |  |  | 
Shader/Smudgy Color/Smudgy Color/Knot.2/Bias Position | <com.redshift3d.redshift4c4d.nodes.core.pavement.smudgycolorinput/_1/bias | maxon::Float | Input | false | false | false |  | 1 | 0.5 | 
Shader/Smudgy Color/Smudgy Color/Knot.2/Color | <com.redshift3d.redshift4c4d.nodes.core.pavement.smudgycolorinput/_1/color | maxon::Color | Input | false | false | false |  |  | (1,1,1) | 
Shader/Smudgy Color/Smudgy Color/Knot.2/Interpolation | <com.redshift3d.redshift4c4d.nodes.core.pavement.smudgycolorinput/_1/interpolation | maxon::InternedId | Input | false | false | true |  |  | smoothknot | Smooth = smoothknot, Cubic = cubicknot, Linear = linearknot, Step = none, Blend = blend, Cubic Bias = cubicbias
Shader/Smudgy Color/Smudgy Color/Knot.2/Knot Position | <com.redshift3d.redshift4c4d.nodes.core.pavement.smudgycolorinput/_1/position | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Shader/Smudgy Color/Smudgy Edges | <com.redshift3d.redshift4c4d.nodes.core.pavement.smudgyedgesinput | maxon::Float | Input | false | false | false | 0 | 1 | 0.8 | 
Shader/Smudgy Color/Smudgy Edges Size | <com.redshift3d.redshift4c4d.nodes.core.pavement.smudgyedgessizeinput | maxon::Float | Input | false | false | false | 0 | 1 | 0.45 | 
Shader/Stone Color/Fine Structure | <com.redshift3d.redshift4c4d.nodes.core.pavement.finestructureinput | maxon::Float | Input | false | false | false | 0 | 1 | 0.15 | 
Shader/Stone Color/Rough Structure | <com.redshift3d.redshift4c4d.nodes.core.pavement.roughstructureinput | maxon::Float | Input | false | false | false | 0 | 1 | 0.5 | 
Shader/Stone Color/Stone Color | <com.redshift3d.redshift4c4d.nodes.core.pavement.stonecolorinput | com.redshift3d.redshift4c4d.portbundle.gradient | Input | true | true | false |  |  |  | 
Shader/Stone Color/Stone Color/Knot.1 | <com.redshift3d.redshift4c4d.nodes.core.pavement.stonecolorinput/_0 | com.redshift3d.redshift4c4d.portbundle.gradient | Input | false | false | false |  |  |  | 
Shader/Stone Color/Stone Color/Knot.1/Bias Position | <com.redshift3d.redshift4c4d.nodes.core.pavement.stonecolorinput/_0/bias | maxon::Float | Input | false | false | false |  | 1 | 0.5 | 
Shader/Stone Color/Stone Color/Knot.1/Color | <com.redshift3d.redshift4c4d.nodes.core.pavement.stonecolorinput/_0/color | maxon::Color | Input | false | false | false |  |  | (1,1,1) | 
Shader/Stone Color/Stone Color/Knot.1/Interpolation | <com.redshift3d.redshift4c4d.nodes.core.pavement.stonecolorinput/_0/interpolation | maxon::InternedId | Input | false | false | true |  |  | smoothknot | Smooth = smoothknot, Cubic = cubicknot, Linear = linearknot, Step = none, Blend = blend, Cubic Bias = cubicbias
Shader/Stone Color/Stone Color/Knot.1/Knot Position | <com.redshift3d.redshift4c4d.nodes.core.pavement.stonecolorinput/_0/position | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Shader/Stone Color/Stone Color/Knot.2 | <com.redshift3d.redshift4c4d.nodes.core.pavement.stonecolorinput/_1 | com.redshift3d.redshift4c4d.portbundle.gradient | Input | false | false | false |  |  |  | 
Shader/Stone Color/Stone Color/Knot.2/Bias Position | <com.redshift3d.redshift4c4d.nodes.core.pavement.stonecolorinput/_1/bias | maxon::Float | Input | false | false | false |  | 1 | 0.5 | 
Shader/Stone Color/Stone Color/Knot.2/Color | <com.redshift3d.redshift4c4d.nodes.core.pavement.stonecolorinput/_1/color | maxon::Color | Input | false | false | false |  |  | (1,1,1) | 
Shader/Stone Color/Stone Color/Knot.2/Interpolation | <com.redshift3d.redshift4c4d.nodes.core.pavement.stonecolorinput/_1/interpolation | maxon::InternedId | Input | false | false | true |  |  | smoothknot | Smooth = smoothknot, Cubic = cubicknot, Linear = linearknot, Step = none, Blend = blend, Cubic Bias = cubicbias
Shader/Stone Color/Stone Color/Knot.2/Knot Position | <com.redshift3d.redshift4c4d.nodes.core.pavement.stonecolorinput/_1/position | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Outputs/outColor | >com.redshift3d.redshift4c4d.nodes.core.pavement.outcolor | maxon::Color64 | Output | false | false | false |  |  | (0,0,0) | 
Outputs/outDisplacementColor | >com.redshift3d.redshift4c4d.nodes.core.pavement.outdisplacementcolor | maxon::Color64 | Output | false | false | false |  |  | (0,0,0) | 
Outputs/outGapMask | >com.redshift3d.redshift4c4d.nodes.core.pavement.outgapmask | maxon::Float | Output | false | false | false |  |  | 0 | 

