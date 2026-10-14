# Node Template: Smooth Geometry

- **Node Space ID:** `net.maxon.neutron.nodespace`
- **Template ID:** `net.maxon.neutron.asset.geo.smoothgeometry`
- **Template Name:** `Smooth Geometry`

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
Node Category | net.maxon.node.base.category | maxon::InternedId | Attribute | false | false | true |  |  | functions | distributions = distributions, operators = operators, geometries = geometries, patterns = patterns, primitives = primitives, effectors = effectors, fields = fields, functions = functions, structures = structures, geomodifiers = geomodifiers, geogenerators = geogenerators
Preview/Node | net.maxon.node.base.nodepreviewimage | maxon::ImageBaseRef | Attribute | false | false | false |  |  |  | 
Inputs/Geometry | <geometryin | maxon::GeometryObject | Input | false | false | false |  |  |  | 
Inputs/Iterations | <inport@ViNX8$ArAdBoQ9EIQ94UDv | maxon::Int64 | Input | false | false | false | 1 |  | 10 | 
Inputs/Jiggle | <inport@Pc2rDUZaC9StP48Xs5C0wI | maxon::Bool | Input | false | false | false |  |  | false | 
Inputs/Min Separation | <inport@NRc1QUp0GZ0mifOe4B6kCJ | maxon::Float64 | Input | false | false | false |  |  | 10 | 
Inputs/Mode | <inport@T2Fha_baAxMpWQifA32SpP | maxon::Int64 | Input | false | false | true |  |  |  | Average = 0, Relax = 1
Inputs/Selection String | <inport@fkgj2MG1GVpnKOCYsYjvy$ | maxon::String | Input | false | false | false |  |  | default | 
Inputs/Strength | <inport@bNewcgPyBdZpEzPD4QBWGp | maxon::Float64 | Input | false | false | false | 0 | 1 | 1 | 
Inputs/X | <inport@Cg8bQczdL9_kVtLv_JEvtP | maxon::Bool | Input | false | false | false |  |  | true | 
Inputs/Y | <inport@Iocfqy44F90lkb3_lWnOwM | maxon::Bool | Input | false | false | false |  |  | true | 
Inputs/Z | <inport@acoatecCMtMip9z7VV5NmO | maxon::Bool | Input | false | false | false |  |  | true | 
Outputs/Geometry | >geometryout | maxon::GeometryObject | Output | false | false | false |  |  |  | 

