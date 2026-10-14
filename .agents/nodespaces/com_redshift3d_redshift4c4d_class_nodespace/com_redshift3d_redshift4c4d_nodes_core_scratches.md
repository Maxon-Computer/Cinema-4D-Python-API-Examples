# Node Template: Scratches

- **Node Space ID:** `com.redshift3d.redshift4c4d.class.nodespace`
- **Template ID:** `com.redshift3d.redshift4c4d.nodes.core.scratches`
- **Template Name:** `Scratches`

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
Shader/Base Specular/Anisotropy | <com.redshift3d.redshift4c4d.nodes.core.scratches.inbaseanisotropy | maxon::Float | Input | false | false | false | 0 | 1 | 0 | 
Shader/Base Specular/Rotation | <com.redshift3d.redshift4c4d.nodes.core.scratches.inbaserotation | maxon::Float | Input | false | false | false | 0 | 1 | 0 | 
Shader/Base Specular/Roughness | <com.redshift3d.redshift4c4d.nodes.core.scratches.inbaseroughness | maxon::Float | Input | false | false | false | 0 | 1 | 0.3 | 
Shader/Distance Behavior/Fade | <com.redshift3d.redshift4c4d.nodes.core.scratches.indistancefadescratches | maxon::Bool | Input | false | false | false |  |  | true | 
Shader/Distance Behavior/Start Fade Density | <com.redshift3d.redshift4c4d.nodes.core.scratches.indistancefadescratchesstart | maxon::Float | Input | false | false | false | 0 | 2147483648 | 100 | 
Shader/Distance Behavior/Stop Fade Density | <com.redshift3d.redshift4c4d.nodes.core.scratches.indistancefadescratchesstop | maxon::Float | Input | false | false | false | 0 | 2147483648 | 300 | 
Shader/General Properties/Bump Strength | <com.redshift3d.redshift4c4d.nodes.core.scratches.innormalintensity | maxon::Float | Input | false | false | false | -1 | 1 | 1 | 
Shader/General Properties/Coord. Space | <com.redshift3d.redshift4c4d.nodes.core.scratches.incoordinatespace | maxon::Int | Input | false | false | true |  |  | 1 | World = 0, Object = 1, UV = 2
Shader/General Properties/Density | <com.redshift3d.redshift4c4d.nodes.core.scratches.indensity | maxon::Float | Input | false | false | false | 0 | 2147483648 | 0.5 | 
Shader/General Properties/Mask | <com.redshift3d.redshift4c4d.nodes.core.scratches.inmask | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Shader/General Properties/Physical Size | <com.redshift3d.redshift4c4d.nodes.core.scratches.inphysicalsize | maxon::Bool | Input | false | false | false |  |  | true | 
Shader/General Properties/Scratch Canvas Size | <com.redshift3d.redshift4c4d.nodes.core.scratches.inscratchcanvassize | maxon::Float | Input | false | false | false | 0 | 2147483648 | 10 | 
Shader/General Properties/Seed | <com.redshift3d.redshift4c4d.nodes.core.scratches.inseed | maxon::Int | Input | false | false | false | -2147483647 | 2147483646 | 123 | 
Shader/General Properties/Triplanar Blend Curve | <com.redshift3d.redshift4c4d.nodes.core.scratches.intriplanarblendcurve | maxon::Float | Input | false | false | false |  |  | 5 | 
Shader/General Properties/UV Canvas Size | <com.redshift3d.redshift4c4d.nodes.core.scratches.inuvcanvassize | maxon::Float | Input | false | false | false | 0 | 2147483648 | 100 | 
Shader/General Properties/UV Channel | <com.redshift3d.redshift4c4d.nodes.core.scratches.tspace_id | maxon::String | Input | false | false | false |  |  |  | 
Shader/General Properties/UV Context | <com.redshift3d.redshift4c4d.nodes.core.scratches.uv_context | RSC4D::UVContext | Input | false | false | false |  |  |  | 
Shader/Scratch Direction/Bias | <com.redshift3d.redshift4c4d.nodes.core.scratches.inscratchanglecorrelation | maxon::Float | Input | false | false | false | 0 | 1 | 0.95 | 
Shader/Scratch Direction/Offset | <com.redshift3d.redshift4c4d.nodes.core.scratches.inscratchanglerotation | maxon::Float | Input | false | false | false |  |  | 0 | 
Shader/Scratch Direction/Steps | <com.redshift3d.redshift4c4d.nodes.core.scratches.inscratchanglebincount | maxon::Int | Input | false | false | false | -2147483647 | 2147483646 | 0 | 
Shader/Scratch Direction/Strays | <com.redshift3d.redshift4c4d.nodes.core.scratches.inscratchangleblend | maxon::Float | Input | false | false | false | 0 | 1 | 0.05 | 
Shader/Scratch Shape/Curve Max | <com.redshift3d.redshift4c4d.nodes.core.scratches.inscratchcurvaturemax | maxon::Float | Input | false | false | false | 0 | 1 | 0.1 | 
Shader/Scratch Shape/Curve Min | <com.redshift3d.redshift4c4d.nodes.core.scratches.inscratchcurvaturemin | maxon::Float | Input | false | false | false | 0 | 1 | 0 | 
Shader/Scratch Shape/Length | <com.redshift3d.redshift4c4d.nodes.core.scratches.inscratchlength | maxon::Float | Input | false | false | false |  |  | 100 | 
Shader/Scratch Shape/Random Length | <com.redshift3d.redshift4c4d.nodes.core.scratches.inscratchlengthrandom | maxon::Float | Input | false | false | false | 0 | 100 | 50 | 
Shader/Scratch Shape/Random Width | <com.redshift3d.redshift4c4d.nodes.core.scratches.inscratchwidthrandom | maxon::Float | Input | false | false | false | 0 | 100 | 50 | 
Shader/Scratch Shape/Taper | <com.redshift3d.redshift4c4d.nodes.core.scratches.inscratchwidthtaper | maxon::Float | Input | false | false | false | 0 | 1 | 0.1 | 
Shader/Scratch Shape/Width | <com.redshift3d.redshift4c4d.nodes.core.scratches.inscratchwidth | maxon::Float | Input | false | false | false |  |  | 1 | 
Shader/Scratch Specular/Max Anisotropy | <com.redshift3d.redshift4c4d.nodes.core.scratches.inscratchanisotropymax | maxon::Float | Input | false | false | false | 0 | 1 | 0.95 | 
Shader/Scratch Specular/Max Roughness | <com.redshift3d.redshift4c4d.nodes.core.scratches.inscratchroughnessmax | maxon::Float | Input | false | false | false | 0 | 1 | 0.5 | 
Shader/Scratch Specular/Min Anisotropy | <com.redshift3d.redshift4c4d.nodes.core.scratches.inscratchanisotropymin | maxon::Float | Input | false | false | false | 0 | 1 | 0.8 | 
Shader/Scratch Specular/Min Roughness | <com.redshift3d.redshift4c4d.nodes.core.scratches.inscratchroughnessmin | maxon::Float | Input | false | false | false | 0 | 1 | 0.3 | 
Outputs/outAnisotropy | >com.redshift3d.redshift4c4d.nodes.core.scratches.outanisotropy | maxon::Float | Output | false | false | false |  |  | 0 | 
Outputs/outAnisotropyRotation | >com.redshift3d.redshift4c4d.nodes.core.scratches.outanisotropyrotation | maxon::Float | Output | false | false | false |  |  | 0 | 
Outputs/outAnisotropyTangent | >com.redshift3d.redshift4c4d.nodes.core.scratches.outanisotropytangent | maxon::Vector64 | Output | false | false | false |  |  | (0,0,0) | 
Outputs/outBump | >com.redshift3d.redshift4c4d.nodes.core.scratches.outbump | maxon::Vector64 | Output | false | false | false |  |  | (0,0,0) | 
Outputs/outRoughness | >com.redshift3d.redshift4c4d.nodes.core.scratches.outroughness | maxon::Float | Output | false | false | false |  |  | 0 | 
Outputs/outScratchColor | >com.redshift3d.redshift4c4d.nodes.core.scratches.outscratchcolor | maxon::Color64 | Output | false | false | false |  |  | (0,0,0) | 
Outputs/outScratchMask | >com.redshift3d.redshift4c4d.nodes.core.scratches.outscratchmask | maxon::Float | Output | false | false | false |  |  | 0 | 

