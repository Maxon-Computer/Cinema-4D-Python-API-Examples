# Node Template: State

- **Node Space ID:** `com.redshift3d.redshift4c4d.class.nodespace`
- **Template ID:** `com.redshift3d.redshift4c4d.nodes.core.state`
- **Template Name:** `State`

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
General/Bounce Level Type | <com.redshift3d.redshift4c4d.nodes.core.state.bounceleveltype | maxon::Int | Input | false | false | true |  |  | 0 | All = 0, Refraction = 1, Reflection = 2, Diffuse = 3, Scatter = 4, Transparency = 5
General/Show Ray-Facing Normals | <com.redshift3d.redshift4c4d.nodes.core.state.showrayfacingnormals | maxon::Bool | Input | false | false | false |  |  | true | 
General/Tangent Space | <com.redshift3d.redshift4c4d.nodes.core.state.tangents | maxon::String | Input | false | false | false |  |  |  | 
General/Texture Space | <com.redshift3d.redshift4c4d.nodes.core.state.tspace_id | maxon::String | Input | false | false | false |  |  |  | 
General/Transform Space | <com.redshift3d.redshift4c4d.nodes.core.state.trans_space | maxon::Int | Input | false | false | true |  |  | 0 | World = 0, Object = 1, Camera = 2, Reference Object = 3
Outputs/bitangent | >com.redshift3d.redshift4c4d.nodes.core.state.bitangent | maxon::Vector64 | Output | false | false | false |  |  | (0,0,0) | 
Outputs/normal | >com.redshift3d.redshift4c4d.nodes.core.state.normal | maxon::Vector64 | Output | false | false | false |  |  | (0,0,0) | 
Outputs/normal_geom | >com.redshift3d.redshift4c4d.nodes.core.state.normal_geom | maxon::Vector64 | Output | false | false | false |  |  | (0,0,0) | 
Outputs/normal_nobump | >com.redshift3d.redshift4c4d.nodes.core.state.normal_nobump | maxon::Vector64 | Output | false | false | false |  |  | (0,0,0) | 
Outputs/raybouncelevel | >com.redshift3d.redshift4c4d.nodes.core.state.raybouncelevel | maxon::Int | Output | false | false | false |  |  | 0 | 
Outputs/raydirection | >com.redshift3d.redshift4c4d.nodes.core.state.raydirection | maxon::Vector64 | Output | false | false | false |  |  | (0,0,0) | 
Outputs/raylength | >com.redshift3d.redshift4c4d.nodes.core.state.raylength | maxon::Float | Output | false | false | false |  |  | 0 | 
Outputs/rayorigin | >com.redshift3d.redshift4c4d.nodes.core.state.rayorigin | maxon::Vector64 | Output | false | false | false |  |  | (0,0,0) | 
Outputs/rayposition | >com.redshift3d.redshift4c4d.nodes.core.state.rayposition | maxon::Vector64 | Output | false | false | false |  |  | (0,0,0) | 
Outputs/tangent | >com.redshift3d.redshift4c4d.nodes.core.state.tangent | maxon::Vector64 | Output | false | false | false |  |  | (0,0,0) | 
Outputs/uvwcoord | >com.redshift3d.redshift4c4d.nodes.core.state.uvwcoord | maxon::Vector64 | Output | false | false | false |  |  | (0,0,0) | 

