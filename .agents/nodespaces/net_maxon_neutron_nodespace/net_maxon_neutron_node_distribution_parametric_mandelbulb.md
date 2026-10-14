# Node Template: Mandelbulb

- **Node Space ID:** `net.maxon.neutron.nodespace`
- **Template ID:** `net.maxon.neutron.node.distribution.parametric.mandelbulb`
- **Template Name:** `Mandelbulb`

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
Node Category | net.maxon.node.base.category | maxon::InternedId | Attribute | false | false | true |  |  | distributions | distributions = distributions, operators = operators, geometries = geometries, patterns = patterns, primitives = primitives, effectors = effectors, fields = fields, functions = functions, structures = structures, geomodifiers = geomodifiers, geogenerators = geogenerators
Preview/Node | net.maxon.node.base.nodepreviewimage | maxon::ImageBaseRef | Attribute | false | false | false |  |  |  | 
Operator/Inner Softness | <maxiterationin | maxon::Int | Input | false | false | false | 1 | 999 | 32 | 
Operator/Iterations | <iterationsseparator |  | Input | false | false | false |  |  |  | 
Operator/Outer Softness | <miniterationin | maxon::Int | Input | false | false | false | 0 | 999 | 8 | 
Operator/Power | <powerin | maxon::Float | Input | false | false | false |  |  | 4 | 
Operator/Sample Count | <samplecountin | maxon::Vector | Input | false | false | false |  | (99999999,99999999,99999999) | (10,10,10) | 
Operator/Sample Offset | <sampleoffsetin | maxon::Vector | Input | false | false | false |  | (99999999,99999999,0) | (150,150,150) | 
Operator/Scale | <scalein | maxon::Bool | Input | false | false | false |  |  | true | 
Operator/Stop Threshold | <stopthresholdin | maxon::Float | Input | false | false | false |  | 9999999 | 128 | 
Outputs/Distribution | >distdataout |  | Output | false | false | false |  |  |  | 

