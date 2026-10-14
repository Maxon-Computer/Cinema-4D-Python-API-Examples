# Node Template: Greeble

- **Node Space ID:** `net.maxon.neutron.nodespace`
- **Template ID:** `net.maxon.neutron.asset.geo.greeble`
- **Template Name:** `Greeble`

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
Inputs/Extrusion/Max Island Angle | <inport@JnOwzEZRGp4pTXfQ2ideli | maxon::Float64 | Input | false | false | false |  | 3.142 | 0.087 | 
Inputs/Extrusion/Maximum Extrusion | <inport@NIKxFrePKZVh0iu8uuTLYm | maxon::Float64 | Input | false | false | false |  |  | 20 | 
Inputs/Extrusion/Minimum Extrusion | <inport@X44Ug2rZAF$m8oabLryPjl | maxon::Float64 | Input | false | false | false |  |  | -5 | 
Inputs/Extrusion/Taper | <inport@aITi8Xb0F5TrFSSNBE2iii | maxon::Float64 | Input | false | false | false |  |  | 0.05 | 
Inputs/Geometry | <geometryin | maxon::GeometryObject | Input | false | false | false |  |  |  | 
Inputs/Initial Subdivision | <inport@Jx3NbnjKA1YoUi6IFV1uVg | maxon::Int32 | Input | false | false | false | 0 | 5 | 1 | 
Inputs/Iterations | <inport@FV3k7h$iNxjnDEK7U5PXfn | maxon::Int64 | Input | false | false | false | 1 | 10 | 2 | 
Inputs/Noise/Method | <inport@Q6DGjjt3JZsmvwrKDaA_UB | maxon::Int64 | Input | false | false | true |  |  | 1 | Noise Selection = 0, Interpolated Mesh+Weight = 1
Inputs/Noise/Noise Type | <inport@Cayka8R5NVAlc$IcO3geLm | maxon::Id | Input | false | false | true |  |  | net.maxon.render.rendernoiseclass.perlin | registry#net.maxon.render.registry.rendernoiseclasses = registry#net.maxon.render.registry.rendernoiseclasses
Inputs/Noise/Scale | <inport@Ic3xO1fEGF4psO3Nghlysn | maxon::Float64 | Input | false | false | false |  | 1 | 0.25 | 
Inputs/Noise/Threshold | <inport@RXAoFu3BABJk$zZYbJu75h | maxon::Float64 | Input | false | false | false |  | 1 | 0.6 | 
Inputs/Noise/Use Weight Map | <inport@K0YVTsaNOxXgIb1QZhtvPF | maxon::Bool | Input | false | false | false |  |  |  | 
Inputs/Noise/Weight Map | <inport@BWF1FnosA1GqfoG7a3P9DC | maxon::String | Input | false | false | false |  |  |  | 
Inputs/Seed | <inport@UZpq$IKrHNcobdwIrF40Hh |  | Input | false | false | false |  |  |  | 
Inputs/Selection String | <inport@FaiqnfoSLhakgwRrxJ60EC | maxon::String | Input | false | false | false |  |  | default | 
Outputs/Geometry | >geometryout | maxon::GeometryObject | Output | false | false | false |  |  |  | 

