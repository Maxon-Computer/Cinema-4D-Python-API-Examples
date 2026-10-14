# Node Template: Unit Conversion

- **Node Space ID:** `com.redshift3d.redshift4c4d.class.nodespace`
- **Template ID:** `com.redshift3d.redshift4c4d.nodes.core.unitconversion`
- **Template Name:** `Unit Conversion`

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
Node Category | net.maxon.node.base.category | maxon::InternedId | Attribute | false | false | true |  |  | structures | operators = operators, distributions = distributions, geometries = geometries, patterns = patterns, primitives = primitives, effectors = effectors, fields = fields, functions = functions, structures = structures, geomodifiers = geomodifiers, geogenerators = geogenerators
Preview/Node | net.maxon.node.base.nodepreviewimage | maxon::ImageBaseRef | Attribute | false | false | false |  |  |  | 
Inputs/Length | <com.redshift3d.redshift4c4d.nodes.core.unitconversion.dynamicunitlength | maxon::Float | Input | false | false | false | 0 | 1000000 | 1 | 
Inputs/Length | <com.redshift3d.redshift4c4d.nodes.core.unitconversion.fixedunitlength | maxon::Float | Input | false | false | false | 0 | 1000000 | 1 | 
Inputs/Mode | <com.redshift3d.redshift4c4d.nodes.core.unitconversion.mode | maxon::Int | Input | false | false | true |  |  | 0 | Scene Units = 0, Fixed = 1
Inputs/Scalar Value | <com.redshift3d.redshift4c4d.nodes.core.unitconversion.scalarvalue | maxon::Float | Input | false | false | false |  |  | 1 | 
Inputs/Unit | <com.redshift3d.redshift4c4d.nodes.core.unitconversion.unit | maxon::Int | Input | false | false | true |  |  | 2 | Centimeters = 2, Kilometers = 0, Meters = 1, Millimeters = 3, Feet = 8, Micrometers = 4, Miles = 6, Nanometers = 5, Yards = 7, Inches = 9
Inputs/Vector Value | <com.redshift3d.redshift4c4d.nodes.core.unitconversion.vectorvalue | maxon::Vector64 | Input | false | false | false |  |  | (1,1,1) | 
Outputs/outScalar | >com.redshift3d.redshift4c4d.nodes.core.unitconversion.outscalar | maxon::Float | Output | false | false | false |  |  | 0 | 
Outputs/outVector | >com.redshift3d.redshift4c4d.nodes.core.unitconversion.outvector | maxon::Vector64 | Output | false | false | false |  |  | (0,0,0) | 

