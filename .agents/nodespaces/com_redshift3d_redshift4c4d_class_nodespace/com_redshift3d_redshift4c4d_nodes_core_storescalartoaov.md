# Node Template: Store Scalar To AOV

- **Node Space ID:** `com.redshift3d.redshift4c4d.class.nodespace`
- **Template ID:** `com.redshift3d.redshift4c4d.nodes.core.storescalartoaov`
- **Template Name:** `Store Scalar To AOV`

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
Basic/Show Preview | net.maxon.node.base.displaypreview | maxon::Bool | Attribute | false | false | false |  |  | false | 
Filter Tags | net.maxon.node.base.filtertags | maxon::CString | Attribute | false | false | false |  |  |  | 
Node Category | net.maxon.node.base.category | maxon::InternedId | Attribute | false | false | true |  |  | structures | distributions = distributions, operators = operators, geometries = geometries, patterns = patterns, primitives = primitives, effectors = effectors, fields = fields, functions = functions, structures = structures, geomodifiers = geomodifiers, geogenerators = geogenerators
Preview/Node | net.maxon.node.base.nodepreviewimage | maxon::ImageBaseRef | Attribute | false | false | false |  |  |  | 
Inputs/AOV 0/AOV Input 0 | <com.redshift3d.redshift4c4d.nodes.core.storescalartoaov.aov_input0 | maxon::Float | Input | false | false | false |  |  | 0 | 
Inputs/AOV 0/AOV Name 0 | <com.redshift3d.redshift4c4d.nodes.core.storescalartoaov.aov_name0 | maxon::String | Input | false | false | false |  |  |  | 
Inputs/AOV 1/AOV Input 1 | <com.redshift3d.redshift4c4d.nodes.core.storescalartoaov.aov_input1 | maxon::Float | Input | false | false | false |  |  | 0 | 
Inputs/AOV 1/AOV Name 1 | <com.redshift3d.redshift4c4d.nodes.core.storescalartoaov.aov_name1 | maxon::String | Input | false | false | false |  |  |  | 
Inputs/AOV 2/AOV Input 2 | <com.redshift3d.redshift4c4d.nodes.core.storescalartoaov.aov_input2 | maxon::Float | Input | false | false | false |  |  | 0 | 
Inputs/AOV 2/AOV Name 2 | <com.redshift3d.redshift4c4d.nodes.core.storescalartoaov.aov_name2 | maxon::String | Input | false | false | false |  |  |  | 
Inputs/AOV 3/AOV Input 3 | <com.redshift3d.redshift4c4d.nodes.core.storescalartoaov.aov_input3 | maxon::Float | Input | false | false | false |  |  | 0 | 
Inputs/AOV 3/AOV Name 3 | <com.redshift3d.redshift4c4d.nodes.core.storescalartoaov.aov_name3 | maxon::String | Input | false | false | false |  |  |  | 
Inputs/AOV 4/AOV Input 4 | <com.redshift3d.redshift4c4d.nodes.core.storescalartoaov.aov_input4 | maxon::Float | Input | false | false | false |  |  | 0 | 
Inputs/AOV 4/AOV Name 4 | <com.redshift3d.redshift4c4d.nodes.core.storescalartoaov.aov_name4 | maxon::String | Input | false | false | false |  |  |  | 
Inputs/AOV 5/AOV Input 5 | <com.redshift3d.redshift4c4d.nodes.core.storescalartoaov.aov_input5 | maxon::Float | Input | false | false | false |  |  | 0 | 
Inputs/AOV 5/AOV Name 5 | <com.redshift3d.redshift4c4d.nodes.core.storescalartoaov.aov_name5 | maxon::String | Input | false | false | false |  |  |  | 
Inputs/AOV 6/AOV Input 6 | <com.redshift3d.redshift4c4d.nodes.core.storescalartoaov.aov_input6 | maxon::Float | Input | false | false | false |  |  | 0 | 
Inputs/AOV 6/AOV Name 6 | <com.redshift3d.redshift4c4d.nodes.core.storescalartoaov.aov_name6 | maxon::String | Input | false | false | false |  |  |  | 
Inputs/AOV 7/AOV Input 7 | <com.redshift3d.redshift4c4d.nodes.core.storescalartoaov.aov_input7 | maxon::Float | Input | false | false | false |  |  | 0 | 
Inputs/AOV 7/AOV Name 7 | <com.redshift3d.redshift4c4d.nodes.core.storescalartoaov.aov_name7 | maxon::String | Input | false | false | false |  |  |  | 
Inputs/Beauty Input | <com.redshift3d.redshift4c4d.nodes.core.storescalartoaov.beauty_input | maxon::ColorA64 | Input | false | false | false |  |  | (0,0,0,1) | 
Outputs/outColor | >com.redshift3d.redshift4c4d.nodes.core.storescalartoaov.outcolor | maxon::ColorA64 | Output | false | false | false |  |  | (0,0,0,1) | 

