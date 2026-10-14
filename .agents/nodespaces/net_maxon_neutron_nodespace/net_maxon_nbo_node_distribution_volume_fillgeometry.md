# Node Template: Volume Voxel Fill

- **Node Space ID:** `net.maxon.neutron.nodespace`
- **Template ID:** `net.maxon.nbo.node.distribution.volume.fillgeometry`
- **Template Name:** `Volume Voxel Fill`

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
Operator/Alignment/Align | <alignin | maxon::Bool | Input | false | false | false |  |  | false | 
Operator/Alignment/Up Vector | <upvectorin | maxon::Id | Input | false | false | true |  |  | ypos | enum#net.maxon.neutron.datatype.enum.alignaxis = enum#net.maxon.neutron.datatype.enum.alignaxis
Operator/Random/Fill | <fillfactorin | maxon::Float | Input | false | false | false |  | 1 | 0.1 | 
Operator/Random/Randomize | <randomenablein | maxon::Bool | Input | false | false | false |  |  |  | 
Operator/Random/Seed | <seedin | maxon::Int | Input | false | false | false |  | 100 | 12345 | 
Operator/Volume/Geometry | <geometryin | maxon::GeometryObject | Input | false | false | false |  |  |  | 
Operator/Volume/Interior Filter | <filterratio | maxon::Float | Input | false | false | false |  | 10 | 1 | 
Operator/Volume/Voxel Size | <voxelsizein | maxon::Float | Input | false | false | false | 0 |  | 5 | 
Outputs/Distribution | >distdataout |  | Output | false | false | false |  |  |  | 

