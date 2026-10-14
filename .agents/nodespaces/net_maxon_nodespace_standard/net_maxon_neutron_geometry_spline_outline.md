# Node Template: Outline Spline

- **Node Space ID:** `net.maxon.nodespace.standard`
- **Template ID:** `net.maxon.neutron.geometry.spline.outline`
- **Template Name:** `Outline Spline`

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
Node Category | net.maxon.node.base.category | maxon::InternedId | Attribute | false | false | true |  |  | geogenerators | distributions = distributions, operators = operators, geometries = geometries, patterns = patterns, primitives = primitives, effectors = effectors, fields = fields, functions = functions, structures = structures, geomodifiers = geomodifiers, geogenerators = geogenerators
Preview/Node | net.maxon.node.base.nodepreviewimage | maxon::ImageBaseRef | Attribute | false | false | false |  |  |  | 
Inputs/Align | <alignin | maxon::Float | Input | false | false | false | -1 | 1 | 1 | 
Inputs/Caps (On Open Splines)/End | <capendin | maxon::InternedId | Input | false | false | true | -1 | 1 | linear | Off = off, Linear = linear, Round = round
Inputs/Caps (On Open Splines)/Start | <capstartin | maxon::InternedId | Input | false | false | true | -1 | 1 | linear | Off = off, Linear = linear, Round = round
Inputs/Geometry | <geometryin | maxon::GeometryObject | Input | false | false | false |  |  |  | 
Inputs/Output | <outputin | maxon::InternedId | Input | false | false | true | -1 | 1 | all | All = all, Inside = inside, Outside = outside
Inputs/Plane | <planein | maxon::InternedId | Input | false | false | true | -1 | 1 | auto | Auto = auto, XY (Up: Z+) = xy, ZY (Up: X+) = zy, XZ (Up: Y+) = xz
Inputs/Thickness | <thicknessin | maxon::Float | Input | false | false | false |  |  | 1 | 
Inputs/Thickness Map | <thicknessmapin | maxon::String | Input | false | false | false |  |  |  | 
Selections/End | <selendenablein | maxon::Bool | Input | false | false | false |  |  |  | 
Selections/End | <selendnamein | maxon::String | Input | false | false | false |  |  | end | 
Selections/Inside | <selinsideenablein | maxon::Bool | Input | false | false | false |  |  |  | 
Selections/Inside | <selinsidenamein | maxon::String | Input | false | false | false |  |  | inside | 
Selections/Outside | <seloutsideenablein | maxon::Bool | Input | false | false | false |  |  |  | 
Selections/Outside | <seloutsidenamein | maxon::String | Input | false | false | false |  |  | outside | 
Selections/Start | <selstartenablein | maxon::Bool | Input | false | false | false |  |  |  | 
Selections/Start | <selstartnamein | maxon::String | Input | false | false | false |  |  | start | 
Outputs/Geometry | >geometryout | maxon::GeometryObject | Output | false | false | false |  |  |  | 

