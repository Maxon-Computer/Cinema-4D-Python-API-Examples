# Node Template: Catenary Spline Modifier

- **Node Space ID:** `net.maxon.neutron.nodespace`
- **Template ID:** `com.rocketlasso.neutron.asset.modifier.catenary`
- **Template Name:** `Catenary Spline Modifier`

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
Inputs/Geometry | <geometryin | maxon::GenericInstantiation<maxon::GeometryObject, maxon::StaticMeshPlaceholder, maxon::StaticPolylinePlaceholder, maxon::StaticCurvePlaceholder> | Input | false | false | false |  |  |  | 
Inputs/Global Capsule Matrix | <globalmatin | maxon::Matrix64 | Input | false | false | false |  |  |  | 
Inputs/Global Object Matrix | <objectmatrix | maxon::Matrix64 | Input | false | false | false |  |  |  | 
Inputs/Local Capsule Matrix | <localmatin | maxon::Matrix64 | Input | false | false | false |  |  |  | 
Inputs/Local Modifier Matrix | <modifiermatrix | maxon::Matrix64 | Input | false | false | false |  |  |  | 
Inputs/Local Object Matrix | <localobjectmatrix | maxon::Matrix64 | Input | false | false | false |  |  |  | 
Object | <in@DeLA4WYpAp_j6eU507fxSg |  | Input | false | false | false |  |  |  | 
Object/Bias | <in@VTdhja6tHZ1kOGcC$N$mFg | maxon::Float64 | Input | false | false | false |  |  | 0 | 
Object/Breaks | <in@M5z9hbPkGZfuf6uqIuOeTk | maxon::Int64 | Input | false | false | true |  |  | 1 | Per Segment = 0, Per Point = 1
Object/Gravity | <in@BTQ3RH$OMt8hZrjN_fbq3g | maxon::Int64 | Input | false | false | true |  |  | 2 | Global = 2, Local = 0, Spherical = 1
Object/Group/Pin Selection | <attr@VwJMQ4WSDFpqKQ42NbgBhl | maxon::String | Input | false | false | false |  |  | Pin | 
Object/Group/Vertex Map | <attr@aVUJAtAbONphY162clYBA3 | maxon::Bool | Input | false | false | false |  |  |  | 
Object/Length | <attr@Pp2qpyV2ARsve2blRCJjdG | maxon::Float64 | Input | false | false | false |  |  | 400 | 
Object/Mode (Hidden) | <in@VEnF_EM0LJzqEjLaEQWtkm | maxon::Int64 | Input | false | false | true |  |  | 0 | Simulate = 0, Bezier = 1
Object/Sag | <attr@dYHPgAanI5kqzCSDLO_ZNi | maxon::Float64 | Input | false | false | false |  |  | 1 | 
Object/Sag | <in@cQUIWnVILtxnWIuoodg2bB | maxon::Int64 | Input | false | false | true |  |  | 0 | Automatic = 0, Fixed = 1
Object/Seed | <attr@dIXx2I4pKFfphS26$65mLn | maxon::Int64 | Input | false | false | false |  |  | 12345 | 
Object/Step | <attr@P7QQO3YfBBynJQ7nNcH0kn | maxon::Float64 | Input | false | false | false |  |  | 1 | 
Object/Variation | <attr@PWeb2iOLIt0obhFYpvzDci | maxon::Float64 | Input | false | false | false |  |  |  | 
Outputs/Geometry | >geometryout | maxon::GeometryObject | Output | false | false | false |  |  |  | 

