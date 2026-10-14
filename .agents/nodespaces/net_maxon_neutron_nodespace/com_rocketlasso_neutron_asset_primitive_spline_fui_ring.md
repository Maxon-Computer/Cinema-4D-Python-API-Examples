# Node Template: FUI Ring

- **Node Space ID:** `net.maxon.neutron.nodespace`
- **Template ID:** `com.rocketlasso.neutron.asset.primitive.spline.fui.ring`
- **Template Name:** `FUI Ring`

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
Preview/Node | net.maxon.node.base.nodepreviewimage | maxon::ImageBaseRef | Attribute | false | false | false |  |  |  | 
Object/Angle Group/End Angle | <HjXMkopuOZElyyfE2m$WSU | maxon::Float64 | Input | false | false | false |  | 6.283 | 6.283 | 
Object/Angle Group/Start Angle | <dwdkmhE0AR_sSCOgh9UlNT | maxon::Float64 | Input | false | false | false | 0 | 6.283 | 0 | 
Object/Count | <fedpVOGGA5kgDnLv3km8AQ | maxon::Float64 | Input | false | false | false |  | 9999999 | 8 | 
Object/Gaps | <MW_ePf9nKV8jLKFvlml_f4 | maxon::Float64 | Input | false | false | false |  |  | 10 | 
Object/Mode | <eZj8alzuExjkGSUkYmmriU | maxon::Int64 | Input | false | false | true |  |  | 0 | Ring = 0, Invert = 1, Full = 2
Object/Plane          | <HGBy8nXlFZIgQ_upNJBy6b | maxon::Int64 | Input | false | false | true |  |  |  | XY = 0, ZY = 1, XZ = 2
Object/Radius | <attr.db14e37167a9485a8e2f570dff399f9d | maxon::Float64 | Input | false | false | false |  |  | 10 | 
Object/Radius        | <XmiyA1rPCt8v2EGZXPOQ6V | maxon::Float64 | Input | false | false | false |  |  | 150 | 
Object/Rounding | <attr.61687700ff6e453b82b6fdb2b0058a14 | maxon::Bool | Input | false | false | false |  |  |  | 
Object/Seed | <cO86FAyYBF6jc5HjrzmwEV | maxon::Float64 | Input | false | false | false |  |  | 12345 | 
Object/Shift | <MSVdJU7YCt5rJTY13I1iNA | maxon::Float64 | Input | false | false | false | -1 |  | 0 | 
Object/Size | <fq2GLd6AKlFnboiq2L_AGX | maxon::Float64 | Input | false | false | false |  |  | 0 | 
Object/Speed Group/Loop Point(F) | <XWcFCqHNK1KlNU4ad40x1T | maxon::Float64 | Input | false | false | false |  |  | 0 | 
Object/Speed Group/Offset         | <TXVYN3UlLJsgdSANhtpZK6 | maxon::Float64 | Input | false | false | false | 0 | 6.283 | 0 | 
Object/Thickness | <TRECA1ieNlgvOjC1HsbMA8 | maxon::Float64 | Input | false | false | false |  |  | 0 | 
Object/Thickness | <U$EF6uqPFpytL8mXbw4tY8 | maxon::Float64 | Input | false | false | false |  |  | 100 | 
Outputs/Geometry | >geometryout | maxon::GeometryObject | Output | false | false | false |  |  |  | 

