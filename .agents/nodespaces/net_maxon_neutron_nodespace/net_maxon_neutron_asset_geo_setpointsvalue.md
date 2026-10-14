# Node Template: Set Points Value

- **Node Space ID:** `net.maxon.neutron.nodespace`
- **Template ID:** `net.maxon.neutron.asset.geo.setpointsvalue`
- **Template Name:** `Set Points Value`

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
Node Category | net.maxon.node.base.category | maxon::InternedId | Attribute | false | false | true |  |  | geomodifiers | distributions = distributions, operators = operators, geometries = geometries, patterns = patterns, primitives = primitives, effectors = effectors, fields = fields, functions = functions, structures = structures, geomodifiers = geomodifiers, geogenerators = geogenerators
Preview/Node | net.maxon.node.base.nodepreviewimage | maxon::ImageBaseRef | Attribute | false | false | false |  |  |  | 
Inputs/Axis/Center on | <in@MHGqcsJlLJii6$jps2azGx | maxon::Int64 | Input | false | false | true |  |  | 1 | All = 0, Selected = 1
Inputs/Axis/Mode X | <in@L6jz$DyOBZDvvTmFaEvsuO | maxon::Int64 | Input | false | false | true |  |  |  | Leave = 0, Set = 1, Center = 2, Quantize = 3
Inputs/Axis/Mode Y | <in@GLLVVQqBLdbjG$m8NB7FoO | maxon::Int64 | Input | false | false | true |  |  |  | Leave = 0, Set = 1, Center = 2, Quantize = 3
Inputs/Axis/Mode Z | <in@RewCHvNXDJDtBkJYQhKj5O | maxon::Int64 | Input | false | false | true |  |  |  | Leave = 0, Set = 1, Center = 2, Quantize = 3
Inputs/Axis/Quantize X | <in@CVp$XHCUGpJtIfrWJrSqWe | maxon::Float64 | Input | false | false | false |  |  | 10 | 
Inputs/Axis/Quantize Y | <in@GAwTyH6wCl_thYJsz2XEqf | maxon::Float64 | Input | false | false | false |  |  | 10 | 
Inputs/Axis/Quantize Z | <in@OqyOTDRPH5bg6Hwv2rBqFZ | maxon::Float64 | Input | false | false | false |  |  | 10 | 
Inputs/Axis/Set X | <in@f4yrlPKeDhGrABlzD5fqKJ | maxon::Float64 | Input | false | false | false |  |  | 0 | 
Inputs/Axis/Set Y | <in@T5kxX9CbNdYh571cslh9UJ | maxon::Float64 | Input | false | false | false |  |  | 0 | 
Inputs/Axis/Set Z | <in@Q58h9NGPClTjdqcbhZ1wnL | maxon::Float64 | Input | false | false | false |  |  | 0 | 
Inputs/Geometry | <geometryin | maxon::GeometryObject | Input | false | false | false |  |  |  | 
Inputs/Global Capsule Matrix | <globalmatin | maxon::Matrix64 | Input | false | false | false |  |  |  | 
Inputs/Global Object Matrix | <objectmatrix | maxon::Matrix64 | Input | false | false | false |  |  |  | 
Inputs/High Clip | <in@XvMVIkv5OFxqjL4QxKmOE6 | maxon::Float64 | Input | false | false | false |  | 1 | 0.75 | 
Inputs/Local Capsule Matrix | <localmatin | maxon::Matrix64 | Input | false | false | false |  |  |  | 
Inputs/Local Modifier Matrix | <modifiermatrix | maxon::Matrix64 | Input | false | false | false |  |  |  | 
Inputs/Local Object Matrix | <localobjectmatrix | maxon::Matrix64 | Input | false | false | false |  |  |  | 
Inputs/Low Clip | <in@fc_I8Jq0KJot11NIuyEfE8 | maxon::Float64 | Input | false | false | false |  | 1 | 0.25 | 
Inputs/Selection/Reference | <in@b9tRE66DC9Ssewd$17W2nO | maxon::InternedId | Input | false | false | true |  |  | points | Points = points, Edges = edges, Polygons = polygons
Inputs/Selection/Selection String | <in@OVB0xlpABpYrB1cAxQl1UI | maxon::String | Input | false | false | false |  |  | default | 
Inputs/Smooth | <in@N9FbwdP$Np0ut8MVMF5954 | maxon::Bool | Input | false | false | false |  |  |  | 
Inputs/Test Global Matrix | <in@KuXGwGlEBdQgIA_s$R_4oL | maxon::Matrix64 | Input | false | false | false |  |  |  | 
Outputs/Geometry | >geometryout | maxon::GeometryObject | Output | false | false | false |  |  |  | 

