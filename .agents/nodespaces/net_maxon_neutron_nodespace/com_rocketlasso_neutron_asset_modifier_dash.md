# Node Template: Dash Spline Modifier

- **Node Space ID:** `net.maxon.neutron.nodespace`
- **Template ID:** `com.rocketlasso.neutron.asset.modifier.dash`
- **Template Name:** `Dash Spline Modifier`

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
Object | <in@DOtjmUtRBBxo40LvipfQUY |  | Input | false | false | false |  |  |  | 
Object/ | <in@P4CE$66mIVfmz6Bs0BFcUd |  | Input | false | false | false |  |  |  | 
Object/ | <in@SCT5vdxsDxNh695S9MIE4b |  | Input | false | false | false |  |  |  | 
Object/Count | <attr.0d6bcc9918504e069956d18da64ddb1b | maxon::Int64 | Input | false | false | false | 1 |  | 50 | 
Object/Custom Group | <in@RAtV9iQkJF4qZv6A3AhF4Z |  | Input | false | false | false |  |  |  | 
Object/Dash | <in@HkfODTT2HlStfPEqa$dwfC | maxon::Bool | Input | true | true | false |  |  |  | 
Object/Dash/Dash.1 | <in@HkfODTT2HlStfPEqa$dwfC/_0 | maxon::Bool | Input | false | false | false |  |  |  | 
Object/Dash/Dash.2 | <in@HkfODTT2HlStfPEqa$dwfC/_2 | maxon::Bool | Input | false | false | false |  |  |  | 
Object/Dash/Dash.3 | <in@HkfODTT2HlStfPEqa$dwfC/_3 | maxon::Bool | Input | false | false | false |  |  |  | 
Object/Dash/Dash.4 | <in@HkfODTT2HlStfPEqa$dwfC/_4 | maxon::Bool | Input | false | false | false |  |  |  | 
Object/Dash/Dash.5 | <in@HkfODTT2HlStfPEqa$dwfC/_5 | maxon::Bool | Input | false | false | false |  |  |  | 
Object/Dash/Dash.6 | <in@HkfODTT2HlStfPEqa$dwfC/_1 | maxon::Bool | Input | false | false | false |  |  |  | 
Object/End Snap | <in@C0s48NdYIJFt39JSmCkCOE | maxon::Bool | Input | false | false | false |  |  |  | 
Object/Group | <attr.c1d799fdef3b4b67b8389ec4a1c6ffa6 |  | Input | false | false | false |  |  |  | 
Object/Group | <attr.dcefd6214f3740bfa84add96c6bf7ab9 |  | Input | false | false | false |  |  |  | 
Object/Group | <in@Mrnp4Cy1PpZnOkzH6xymtF |  | Input | false | false | false |  |  |  | 
Object/Group/Apply Per Segment | <attr.0c149b9abb574a9e8e32ba1f32153bbe | maxon::Bool | Input | false | false | false |  |  | true | 
Object/Group/Offset      | <attr.7bdd5755240a4c13b2e69be19eeea8f9 | maxon::Float64 | Input | false | false | false |  |  | 0 | 
Object/Group/Offset      | <attr.a8e02b8ada214d66b0ebe0bfaf94966b | maxon::Float64 | Input | false | false | false |  |  | 0 | 
Object/Group/Rate | <attr.536088c548964865b339b1f1fcfd81ef | maxon::Float64 | Input | false | false | false |  |  | 0 | 
Object/Group/Rate | <attr.ae35c772158446b9a2e5cde748ff8551 | maxon::Float64 | Input | false | false | false |  |  | 0 | 
Object/Invert  | <attr.a5f8a6d008b3428596580f49eb02219e | maxon::Bool | Input | false | false | false |  |  | 0 | 
Object/Length | <attr.b4a965a2905c495bbeece2d3d8913c9a | maxon::Float64 | Input | false | false | false | 1 |  | 10 | 
Object/Mode     | <attr.57718c8789274a92814d20ec1f66233a | maxon::Int64 | Input | false | false | true |  |  |  | Length = 0, Count = 1, Percentage = 2
Object/Pattern    | <in@BTYaVkKkMlxgyCJDZmsK$b | maxon::Int64 | Input | false | false | true |  |  | 1 | Percent = 1, Custom = 2
Object/Percent | <attr.bc04ab6d7d184446a22a205635e6ecd2 | maxon::Float64 | Input | false | false | false | 0 |  | 0.05 | 
Object/Random Group | <in@fCBLoevpM12s58enaP7bVa |  | Input | false | false | false |  |  |  | 
Object/Random Group/Per Segment | <attr.9afd11b5a0894d2e8931c48ceb3e1d02 | maxon::Bool | Input | false | false | false |  |  |  | 
Object/Random Group/Random | <in@bBdyl6bEHxqo29eiOxhIYd | maxon::Int64 | Input | false | false | false |  |  | 12345 | 
Object/Random Group/Subdivisons | <attr.4acb45136f744d62b376187f85d5746e | maxon::Int64 | Input | false | false | false |  |  |  | 
Object/Random Group/Visible | <in@U_HO_Qj1FV5rw2_okcJUPZ | maxon::Float64 | Input | false | false | false |  |  | 0.5 | 
Object/Segments | <attr.8d98366ce9b74845a32f17568f096fc4 | maxon::Bool | Input | false | false | false |  |  | true | 
Object/Snap | <in@NkuBTE6VElXobD3dW9IVKd | maxon::Bool | Input | false | false | false |  |  | true | 
Object/Step Group | <in@TQgNXdKzCdOoMVEWyMfief |  | Input | false | false | false |  |  |  | 
Object/Step Group/Visible     | <attr.5b7b3db5e9514862940e3a72844fb402 | maxon::Float64 | Input | false | false | false |  | 1 | 0.5 | 
Outputs/Geometry | >geometryout | maxon::GenericInstantiation<maxon::GeometryObject, maxon::StaticPolylinePlaceholder> | Output | false | false | false |  |  |  | 

