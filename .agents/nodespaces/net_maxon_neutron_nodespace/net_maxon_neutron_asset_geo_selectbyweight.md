# Node Template: Select by Weight

- **Node Space ID:** `net.maxon.neutron.nodespace`
- **Template ID:** `net.maxon.neutron.asset.geo.selectbyweight`
- **Template Name:** `Select by Weight`

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
Node Category | net.maxon.node.base.category | maxon::InternedId | Attribute | false | false | true |  |  | geomodifiers | operators = operators, distributions = distributions, geometries = geometries, patterns = patterns, primitives = primitives, effectors = effectors, fields = fields, functions = functions, structures = structures, geomodifiers = geomodifiers, geogenerators = geogenerators
Preview/Node | net.maxon.node.base.nodepreviewimage | maxon::ImageBaseRef | Attribute | false | false | false |  |  |  | 
Inputs/Geometry | <geometryin | maxon::GeometryObject | Input | false | false | false |  |  |  | 
Inputs/Max | <inport@cRVb7CrmGFxmmT0$bzpAyL | maxon::Float64 | Input | false | false | false |  |  | 0.7 | 
Inputs/Min | <inport@KCBDixjGGxNqGG5Mco08XI | maxon::Float64 | Input | false | false | false |  |  | 0.3 | 
Inputs/Mode | <inport@QX1IlPSJF1vsYN$M3PMdDO | maxon::Int64 | Input | false | false | true |  |  |  | Compare = 0, In Range = 1
Inputs/Name | <inport@PoPCio7kPNqjtOU1Cxm$ZN | maxon::String | Input | false | false | false |  |  |  | 
Inputs/Operation | <inport@BATUEHFqJZ2mrmLBfq5cBM | maxon::Id | Input | false | false | true |  |  | gt | Greater Than = gt, Less Than = lt, Greater Or Equal = ge, Less Or Equal = le, Equals = eq, Not Equals = ne
Inputs/Value | <inport@IRZ697UbPpIowM3HddOe0O | maxon::Float64 | Input | false | false | false |  |  | 0.5 | 
Outputs/Geometry | >geometryout | maxon::GeometryObject | Output | false | false | false |  |  |  | 

