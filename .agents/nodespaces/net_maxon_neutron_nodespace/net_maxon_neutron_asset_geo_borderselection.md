# Node Template: Border Selection

- **Node Space ID:** `net.maxon.neutron.nodespace`
- **Template ID:** `net.maxon.neutron.asset.geo.borderselection`
- **Template Name:** `Border Selection`

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
Inputs/Edges Output/Active Selection | <inport@QJRRIQaTBFSm4dZiB8rm5M | maxon::Int64 | Input | false | false | true |  |  | 1 | Keep = 0, Border = 1
Inputs/Edges Output/Border | <inport@FEkeN3tAIhas$W4LLD3XLK | maxon::String | Input | false | false | false |  |  |  | 
Inputs/Geometry | <geometryin | maxon::GeometryObject | Input | false | false | false |  |  |  | 
Inputs/Polygons Output/Active Selection | <inport@LV1qHXlnEdGonyeEXKESAI | maxon::Int64 | Input | false | false | true |  |  |  | Keep = 0, Border = 1
Inputs/Polygons Output/Border | <inport@JlQvVyQmEVAjFe_ROvI8yM | maxon::String | Input | false | false | false |  |  |  | 
Outputs/Count | >outport@EqwgQcFMIpcuYMdc9mVSRt | maxon::Int64 | Output | false | false | false |  |  |  | 
Outputs/Edge Selection | >outport@bKaAUusRKlDjnbmyyeyU_I | maxon::Array<maxon::Tuple<maxon::Int32, maxon::Int32>> | Output | false | false | false |  |  |  | 
Outputs/Geometry | >geometryout | maxon::GeometryObject | Output | false | false | false |  |  |  | 
Outputs/Polygon Selection | >outport@V7rv3VCOA5jjIAGeHN9AGM | maxon::Array<maxon::Int32> | Output | false | false | false |  |  |  | 

