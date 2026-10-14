# Node Template: Distance

- **Node Space ID:** `com.redshift3d.redshift4c4d.class.nodespace`
- **Template ID:** `com.redshift3d.redshift4c4d.nodes.core.distance`
- **Template Name:** `Distance`

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
Inputs/General/Color Far | <com.redshift3d.redshift4c4d.nodes.core.distance.colorfar | maxon::ColorA64 | Input | false | false | false |  |  | (1,1,1,1) | 
Inputs/General/Color Near | <com.redshift3d.redshift4c4d.nodes.core.distance.colornear | maxon::ColorA64 | Input | false | false | false |  |  | (0,0,0,1) | 
Inputs/General/Distance Far | <com.redshift3d.redshift4c4d.nodes.core.distance.distancefar | maxon::Float | Input | false | false | false | 0 | 2147483648 | 100 | 
Inputs/General/Distance Near | <com.redshift3d.redshift4c4d.nodes.core.distance.distancenear | maxon::Float | Input | false | false | false | 0 | 2147483648 | 0 | 
Inputs/General/Include Backside | <com.redshift3d.redshift4c4d.nodes.core.distance.includebackside | maxon::Bool | Input | false | false | false |  |  | false | 
Inputs/General/Include Mode | <com.redshift3d.redshift4c4d.nodes.core.distance.includemode | maxon::Int | Input | false | false | true |  |  | 0 | All Except Self = 0, Only Self = 1, All = 2, Trace Set = 3
Inputs/General/Normalize to Range | <com.redshift3d.redshift4c4d.nodes.core.distance.normalizetorange | maxon::Bool | Input | false | false | false |  |  | false | 
Inputs/General/Samples | <com.redshift3d.redshift4c4d.nodes.core.distance.numsamples | maxon::Int | Input | false | false | false | 1 | 65535 | 256 | 
Inputs/General/Trace Set Mode | <com.redshift3d.redshift4c4d.nodes.core.distance.traceset.mode | maxon::Int | Input | false | false | true |  |  | 1 | Include = 0, Exclude = 1
Inputs/General/Trace Set Objects | <com.redshift3d.redshift4c4d.nodes.core.distance.traceset | maxon::DataDictionary | Input | false | false | false |  |  |  | 
Inputs/Interior Controls/Color Far | <com.redshift3d.redshift4c4d.nodes.core.distance.colorinteriorfar | maxon::ColorA64 | Input | false | false | false |  |  | (1,1,1,1) | 
Inputs/Interior Controls/Color Near | <com.redshift3d.redshift4c4d.nodes.core.distance.colorinteriornear | maxon::ColorA64 | Input | false | false | false |  |  | (0,0,0,1) | 
Inputs/Interior Controls/Enable | <com.redshift3d.redshift4c4d.nodes.core.distance.enableinterior | maxon::Bool | Input | false | false | false |  |  | false | 
Inputs/Interior Controls/Solid | <com.redshift3d.redshift4c4d.nodes.core.distance.solidinterior | maxon::Int | Input | false | false | true |  |  | 0 | Off = 0, Inside = 1, Outside = 2, Both = 3
Outputs/outColor | >com.redshift3d.redshift4c4d.nodes.core.distance.outcolor | maxon::ColorA64 | Output | false | false | false |  |  | (0,0,0,1) | 
Outputs/outDirection | >com.redshift3d.redshift4c4d.nodes.core.distance.outdirection | maxon::Vector64 | Output | false | false | false |  |  | (0,0,0) | 
Outputs/outDistance | >com.redshift3d.redshift4c4d.nodes.core.distance.outdistance | maxon::Float | Output | false | false | false |  |  | 0 | 

