# Node Template: Flightpath

- **Node Space ID:** `net.maxon.neutron.nodespace`
- **Template ID:** `net.maxon.neutron.asset.primitive.spline.flightpath`
- **Template Name:** `Flightpath`

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
Inputs/Auto Tangent | <inport@SkIc4psmMFKvReDpd0iJ_M | maxon::Bool | Input | false | false | false |  |  | true | 
Inputs/End Latitude | <inport@SO_c1BTwIB_lW2NtwSku3I | maxon::Float64 | Input | false | false | false | -1.571 | 1.571 | 0.795 | 
Inputs/End Longitude | <inport@OotxbewZCl3vkEl8dqEDdO | maxon::Float64 | Input | false | false | false |  |  | -2.141 | 
Inputs/Endpoint Angle | <inport@R7IvivZLPZqoakxvO9rNPO | maxon::Float64 | Input | false | false | false |  |  | 0.5 | 
Inputs/Endpoints Tangent | <inport@bIhpO8z9A9ygsiFdABPLAL | maxon::Float64 | Input | false | false | false |  |  | 1 | 
Inputs/Flight Radius | <inport@F3O$YaNfMBOsv9h$b01WXI | maxon::Float64 | Input | false | false | false |  |  | 55 | 
Inputs/Flight Tangents | <inport@d7HaVrnIGR2lDuWJzkKUNK | maxon::Float64 | Input | false | false | false |  |  | 10 | 
Inputs/Global Radius | <inport@VHRh4v1fHh3oqkiAEqi26J | maxon::Float64 | Input | false | false | false |  |  | 50 | 
Inputs/Start Latitude | <inport@fq491Vj3MxXuKsDI8TT2EM | maxon::Float64 | Input | false | false | false | -1.571 | 1.571 | 0.875 | 
Inputs/Start Longitude | <inport@fQTEV_L1MV5gn55e3DHdVL | maxon::Float64 | Input | false | false | false |  |  | 0.152 | 
Outputs/End | >outport@Bre3jx_XAtNlBD0d6CKfOs | maxon::Matrix64 | Output | false | false | false |  |  |  | 
Outputs/Geometry | >geometryout | maxon::GeometryObject | Output | false | false | false |  |  |  | 
Outputs/Start | >outport@IkR2hdZlLZpjSGpbGWmdns | maxon::Matrix64 | Output | false | false | false |  |  |  | 

