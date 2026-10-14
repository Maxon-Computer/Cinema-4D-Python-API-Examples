# Node Template: Standard Volume

- **Node Space ID:** `com.redshift3d.redshift4c4d.class.nodespace`
- **Template ID:** `com.redshift3d.redshift4c4d.nodes.core.standardvolume`
- **Template Name:** `Standard Volume`

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
Basic/Advanced/Shadow Density Scale | <com.redshift3d.redshift4c4d.nodes.core.standardvolume.shadow_density_scale | maxon::Float | Input | false | false | false |  |  | 1 | 
Basic/Displacement/Scale | <com.redshift3d.redshift4c4d.nodes.core.standardvolume.displacement | maxon::Vector64 | Input | false | false | false |  |  | (0,0,0) | 
Basic/Emission/Channel/Channel | <com.redshift3d.redshift4c4d.nodes.core.standardvolume.emission_name | maxon::String | Input | false | false | false |  |  |  | 
Basic/Emission/Color | <com.redshift3d.redshift4c4d.nodes.core.standardvolume.emission_tint | maxon::Color64 | Input | false | false | false |  |  | (1,1,1) | 
Basic/Emission/Emission Mode | <com.redshift3d.redshift4c4d.nodes.core.standardvolume.blackbody_mode | maxon::Int | Input | false | false | true |  |  | 0 | Blackbody = 0, Color = 1
Basic/Emission/Offset | <com.redshift3d.redshift4c4d.nodes.core.standardvolume.blackbody_offset | maxon::Float | Input | false | false | false |  |  | 1 | 
Basic/Emission/Scale | <com.redshift3d.redshift4c4d.nodes.core.standardvolume.emission_scale | maxon::Float | Input | false | false | false |  |  | 0 | 
Basic/Emission/Temperature | <com.redshift3d.redshift4c4d.nodes.core.standardvolume.blackbody_temperature | maxon::Float | Input | false | false | false |  |  | 6500 | 
Basic/Multiscatter/Anisotropy Falloff | <com.redshift3d.redshift4c4d.nodes.core.standardvolume.anisotropy_falloff | maxon::Float | Input | false | false | false | 0 | 10 | 1 | 
Basic/Multiscatter/Extinction Falloff | <com.redshift3d.redshift4c4d.nodes.core.standardvolume.extinction_falloff | maxon::Float | Input | false | false | false | 0 | 1 | 0.2 | 
Basic/Multiscatter/Start Depth | <com.redshift3d.redshift4c4d.nodes.core.standardvolume.start_depth | maxon::Int | Input | false | false | false | 0 | 31 | 1 | 
Basic/Scatter/Anisotropy | <com.redshift3d.redshift4c4d.nodes.core.standardvolume.anisotropy | maxon::Float | Input | false | false | false | -1 | 1 | 0 | 
Basic/Scatter/Anisotropy Mode | <com.redshift3d.redshift4c4d.nodes.core.standardvolume.anisotropy_mode | maxon::Int | Input | false | false | true |  |  | 0 | Henyey-Greenstein = 0, Jendersie d'Eon = 1
Basic/Scatter/Color | <com.redshift3d.redshift4c4d.nodes.core.standardvolume.scatter_color | maxon::Color64 | Input | false | false | false |  |  | (1,1,1) | 
Basic/Scatter/Diameter | <com.redshift3d.redshift4c4d.nodes.core.standardvolume.diameter | maxon::Float | Input | false | false | false | 0 | 50 | 5 | 
Basic/Scatter/Scale | <com.redshift3d.redshift4c4d.nodes.core.standardvolume.scatter_scale | maxon::Float | Input | false | false | false |  |  | 1 | 
Basic/Transparency/Color | <com.redshift3d.redshift4c4d.nodes.core.standardvolume.transmittance_color | maxon::Color64 | Input | false | false | false |  |  | (0.5,0.5,0.5) | 
Basic/Transparency/Depth (cm) | <com.redshift3d.redshift4c4d.nodes.core.standardvolume.depth | maxon::Float | Input | false | false | false |  |  | 1 | 
Basic/Volume/Channel/Channel | <com.redshift3d.redshift4c4d.nodes.core.standardvolume.density_name | maxon::String | Input | false | false | false |  |  |  | 
Basic/Volume/Density | <com.redshift3d.redshift4c4d.nodes.core.standardvolume.density | maxon::Float | Input | false | false | false |  |  | 1 | 
Outputs/outColor | >com.redshift3d.redshift4c4d.nodes.core.standardvolume.outcolor | maxon::ColorA64 | Output | false | false | false |  |  | (0,0,0,1) | 

