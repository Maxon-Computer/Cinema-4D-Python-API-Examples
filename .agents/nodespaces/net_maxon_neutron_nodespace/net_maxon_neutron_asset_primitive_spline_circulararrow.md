# Node Template: Circular Arrow

- **Node Space ID:** `net.maxon.neutron.nodespace`
- **Template ID:** `net.maxon.neutron.asset.primitive.spline.circulararrow`
- **Template Name:** `Circular Arrow`

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
Node Category | net.maxon.node.base.category | maxon::InternedId | Attribute | false | false | true |  |  | functions | operators = operators, distributions = distributions, geometries = geometries, patterns = patterns, primitives = primitives, effectors = effectors, fields = fields, functions = functions, structures = structures
Preview/Node | net.maxon.node.base.nodepreviewimage | maxon::ImageBaseRef | Attribute | false | false | false |  |  |  | 
Inputs/End | <inport@DGazm4BKA13jHbNA220zF6 | maxon::Int64 | Input | false | false | false |  |  | 1 | 
Inputs/End Angle | <inport@EiBn_vr0NR9hxF401Cd3O$ | maxon::Float64 | Input | false | false | false |  |  | 1.571 | 
Inputs/End Shape | <inport@TCLHMl6UM9mhzX$eWF4DS7 | maxon::Array<maxon::Vector64> | Input | false | false | false |  |  |  | 
Inputs/Outer Scope | <inport@eHhU8EWQO5ssGy05$Vp4m_ |  | Input | false | false | false |  |  |  | 
Inputs/Own End | <inport@L5kHUEkVD1hp4SukDhgs0$ | maxon::Bool | Input | false | false | false |  |  |  | 
Inputs/Own Tip | <inport@b9bQtBgyGhDr9WZqEXJyH6 | maxon::Bool | Input | false | false | false |  |  |  | 
Inputs/Precision | <inport@S45y4iVMEJ5mU0L45Z6JR$ | maxon::Float64 | Input | false | false | false |  | 1.571 | 0.087 | 
Inputs/Radius | <inport@U2f8ie8tKtIlLIyoSF_mn9 | maxon::Float64 | Input | false | false | false |  |  | 50 | 
Inputs/Start Angle | <inport@ARYNcN0jJlHq_XgJa2lTi_ | maxon::Float64 | Input | false | false | false |  |  |  | 
Inputs/Tip | <inport@An4JvBzyOtGgPVoljaK6e$ | maxon::Int64 | Input | false | false | false |  |  |  | 
Inputs/Tip Shape | <inport@Ct2e1EnOEJaiEY4f9m9r7$ | maxon::Array<maxon::Vector64> | Input | false | false | false |  |  |  | 
Inputs/Width | <inport@fpfbfx_BMNlikLb$AKSthH | maxon::Float64 | Input | false | false | false |  |  | 10 | 
Outputs/Geometry | >geometryout | maxon::GeometryObject | Output | false | false | false |  |  |  | 

