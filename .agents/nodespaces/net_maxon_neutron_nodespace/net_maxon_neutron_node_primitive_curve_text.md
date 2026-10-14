# Node Template: Text

- **Node Space ID:** `net.maxon.neutron.nodespace`
- **Template ID:** `net.maxon.neutron.node.primitive.curve.text`
- **Template Name:** `Text`

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
Node Category | net.maxon.node.base.category | maxon::InternedId | Attribute | false | false | true |  |  | primitives | distributions = distributions, operators = operators, geometries = geometries, patterns = patterns, primitives = primitives, effectors = effectors, fields = fields, functions = functions, structures = structures
Object/Align | net.maxon.command.modeling.primitive.curve.text.align | maxon::InternedId | Attribute | false | false | true |  |  | left | Left = left, Middle = middle, Right = right
Object/Axis 00 | net.maxon.command.modeling.primitive.curve.text.varaxis00 | maxon::Float | Attribute | false | false | false | 1 | 1000 | 500 | 
Object/Axis 01 | net.maxon.command.modeling.primitive.curve.text.varaxis01 | maxon::Float | Attribute | false | false | false | 1 | 1000 | 500 | 
Object/Axis 02 | net.maxon.command.modeling.primitive.curve.text.varaxis02 | maxon::Float | Attribute | false | false | false | 1 | 1000 | 500 | 
Object/Axis 03 | net.maxon.command.modeling.primitive.curve.text.varaxis03 | maxon::Float | Attribute | false | false | false | 1 | 1000 | 500 | 
Object/Axis 04 | net.maxon.command.modeling.primitive.curve.text.varaxis04 | maxon::Float | Attribute | false | false | false | 1 | 1000 | 500 | 
Object/Axis 05 | net.maxon.command.modeling.primitive.curve.text.varaxis05 | maxon::Float | Attribute | false | false | false | 1 | 1000 | 500 | 
Object/Axis 06 | net.maxon.command.modeling.primitive.curve.text.varaxis06 | maxon::Float | Attribute | false | false | false | 1 | 1000 | 500 | 
Object/Axis 07 | net.maxon.command.modeling.primitive.curve.text.varaxis07 | maxon::Float | Attribute | false | false | false | 1 | 1000 | 500 | 
Object/Axis 08 | net.maxon.command.modeling.primitive.curve.text.varaxis08 | maxon::Float | Attribute | false | false | false | 1 | 1000 | 500 | 
Object/Axis 09 | net.maxon.command.modeling.primitive.curve.text.varaxis09 | maxon::Float | Attribute | false | false | false | 1 | 1000 | 500 | 
Object/Font | net.maxon.command.modeling.primitive.curve.text.font | maxon::OSFontDefinition | Attribute | false | false | false |  |  |  | 
Object/Height | net.maxon.command.modeling.primitive.curve.text.height | maxon::Float | Attribute | false | false | false |  |  | 200 | 
Object/Horizontal Spacing | net.maxon.command.modeling.primitive.curve.text.hspacing | maxon::Float | Attribute | false | false | false |  |  | 0 | 
Object/Merge Segments | net.maxon.command.modeling.primitive.curve.text.mergesegments | maxon::Bool | Attribute | false | false | false |  |  |  | 
Object/Plane | net.maxon.command.modeling.primitive.orientationplane.plane | maxon::InternedId | Attribute | false | false | true |  |  | xy | XY = xy, ZY = zy, XZ = xz
Object/Reverse | net.maxon.command.modeling.primitive.orientationplane.reverse | maxon::Bool | Attribute | false | false | false |  |  |  | 
Object/Standard Style | net.maxon.command.modeling.primitive.curve.text.variablefontstandardstyle | maxon::Int | Attribute | false | false | false |  |  | 1 | 
Object/Text Spline | net.maxon.command.modeling.primitive.curve.text.text | maxon::String | Attribute | false | false | false |  |  | Text | 
Object/Use Variable Font | net.maxon.command.modeling.primitive.curve.text.usevariablefont | maxon::Bool | Attribute | false | false | false |  |  |  | 
Object/Variable Font | net.maxon.command.modeling.primitive.curve.text.variablefontfilename | maxon::Url | Attribute | false | false | false |  |  |  | 
Object/Vertical Spacing | net.maxon.command.modeling.primitive.curve.text.vspacing | maxon::Float | Attribute | false | false | false |  |  |  | 
Preview/Node | net.maxon.node.base.nodepreviewimage | maxon::ImageBaseRef | Attribute | false | false | false |  |  |  | 
VariableFontData | net.maxon.command.modeling.primitive.curve.text.variablefontdata | maxon::DataDictionary | Attribute | false | false | false |  |  |  | 
Outputs/Geometry | >geometryout | maxon::GeometryObject | Output | false | false | false |  |  |  | 

