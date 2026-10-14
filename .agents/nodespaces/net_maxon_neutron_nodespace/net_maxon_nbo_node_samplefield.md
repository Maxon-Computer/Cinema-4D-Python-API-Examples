# Node Template: Sample Field

- **Node Space ID:** `net.maxon.neutron.nodespace`
- **Template ID:** `net.maxon.nbo.node.samplefield`
- **Template Name:** `Sample Field`

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
Node Category | net.maxon.node.base.category | maxon::InternedId | Attribute | false | false | true |  |  | functions | operators = operators, distributions = distributions, geometries = geometries, patterns = patterns, primitives = primitives, effectors = effectors, fields = fields, functions = functions, structures = structures, geomodifiers = geomodifiers, geogenerators = geogenerators
Preview/Node | net.maxon.node.base.nodepreviewimage | maxon::ImageBaseRef | Attribute | false | false | false |  |  |  | 
Field | <field | maxon::FieldListRef | Input | false | false | false |  |  |  | 
Global Matrix | <matrix | maxon::Matrix | Input | false | false | false |  |  |  | 
Inputs/Array Mode | <arraymode | maxon::Bool | Input | false | false | false |  |  |  | 
Inputs/Location | <location | net.maxon.nbo.portbundle.fieldlocation | Input | false | true | false |  |  |  | 
Inputs/Location/Local Direction | <location/direction | maxon::Vector | Input | false | false | false |  |  |  | 
Inputs/Location/Local Position | <location/position | maxon::Vector | Input | false | false | false |  |  |  | 
Inputs/Location/UVW | <location/uvw | maxon::Vector | Input | false | false | false |  |  |  | 
Outputs/Result/Color | >result/color | maxon::ColorA | Input | false | false | false |  |  |  | 
Outputs/Result/Deactivated | >result/deactivated | maxon::Bool | Input | false | false | false |  |  |  | 
Outputs/Result/Local Direction | >result/fielddirection | maxon::Vector | Input | false | false | false |  |  |  | 
Outputs/Result/Value | >result/value | maxon::Float | Input | false | false | false |  |  |  | 
Outputs/Result | >result | net.maxon.nbo.portbundle.fieldvalues | Output | false | true | false |  |  |  | 

