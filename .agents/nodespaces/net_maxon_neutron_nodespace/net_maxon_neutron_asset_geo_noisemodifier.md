# Node Template: Noise Modifier

- **Node Space ID:** `net.maxon.neutron.nodespace`
- **Template ID:** `net.maxon.neutron.asset.geo.noisemodifier`
- **Template Name:** `Noise Modifier`

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
Inputs/Global Capsule Matrix | <globalmatin | maxon::Matrix64 | Input | false | false | false |  |  |  | 
Inputs/Global Object Matrix | <objectmatrix | maxon::Matrix64 | Input | false | false | false |  |  |  | 
Inputs/Local Capsule Matrix | <localmatin | maxon::Matrix64 | Input | false | false | false |  |  |  | 
Inputs/Local Modifier Matrix | <modifiermatrix | maxon::Matrix64 | Input | false | false | false |  |  |  | 
Inputs/Local Object Matrix | <localobjectmatrix | maxon::Matrix64 | Input | false | false | false |  |  |  | 
Inputs/Main/Strength | <float1 | maxon::Float64 | Input | false | false | false |  |  | 1 | 
Inputs/Main/Weight | <in@XRh3B8dlBpft5b62lI7LJn | maxon::String | Input | false | false | false |  |  |  | 
Inputs/Mapping/Contrast | <in@N_I1bfeyFZdr3v3_VVWQ$4 | maxon::Float64 | Input | false | false | false | -1 | 1 | 0 | 
Inputs/Mapping/High Clip | <in@c0o13f4mFNhmAXNSiC8Gi$ | maxon::Float64 | Input | false | false | false |  | 1 | 1 | 
Inputs/Mapping/Low Clip | <in@AaN1u6goMx9mbu1vYdLOb$ | maxon::Float64 | Input | false | false | false |  | 1 | 0 | 
Inputs/Operation/Absolute Value | <in@Yu_2tcFSNFepYxsZe1cWy_ | maxon::Bool | Input | false | false | false |  |  | false | 
Inputs/Operation/Animated | <in@d$eKxb0$MpVgemUIzRVF99 | maxon::Int64 | Input | false | false | true |  |  |  | 0 = 0, 1 = 1
Inputs/Operation/Cycles | <in@RRkF6QYGFpFhXi0QmLO1Ei | maxon::Float64 | Input | false | false | false |  |  | 1 | 
Inputs/Operation/Exponent | <in@WIfULN3dHVVnXyjI3L25v9 | maxon::Float64 | Input | false | false | false | 0.1 | 5 | 2 | 
Inputs/Operation/Gain | <in@au__HSOhEtLn8P5JhfavN4 | maxon::Float64 | Input | false | false | false | 0.1 | 4 | 0.5 | 
Inputs/Operation/Global Scale | <in@CQvdwSsGPRxseTGx60Z0N_ | maxon::Float64 | Input | false | false | false |  |  | 1 | 
Inputs/Operation/Lacunarity | <float | maxon::Float64 | Input | false | false | false | 0.1 | 10 | 2.1 | 
Inputs/Operation/Mode | <in@GedBIswiHNKpdXBSILggx6 | maxon::Int64 | Input | false | false | true |  |  | 1 | Random = 0, Noise = 1
Inputs/Operation/Noise Type | <in@doQoQDwVCtTr5MUduYCwH9 | maxon::Id | Input | false | false | true |  |  | net.maxon.render.rendernoiseclass.perlin | registry#net.maxon.render.registry.rendernoiseclasses = registry#net.maxon.render.registry.rendernoiseclasses
Inputs/Operation/Octaves | <in@SIWkiskuKtYh1yn4DFbwd$ | maxon::Float64 | Input | false | false | false |  | 20 | 6 | 
Inputs/Operation/Relative Scale | <vector | maxon::Vector64 | Input | false | false | false |  |  | (1,1,1) | 
Inputs/Operation/Seed | <in@OWCxb6mvEZtv2CPT6wmfX_ | maxon::Int64 | Input | false | false | false |  |  | 12345 | 
Inputs/Operation/Speed | <in@Muds5oQEMROh8a8m95hAO7 | maxon::Float64 | Input | false | false | false |  |  |  | 
Inputs/Reference | <in@QVjQ1q1BGVeg$uVXW6b9d4 | maxon::InternedId | Input | false | false | true |  |  | points | Points = points, Edges = edges, Polygons = polygons
Inputs/Selection String | <in@IdZbRZtHK9youUG0qdf2I$ | maxon::String | Input | false | false | false |  |  | all | 
Inputs/Transform/Displacement | <bool | maxon::Bool | Input | false | false | false |  |  | true | 
Inputs/Transform/Min/Max/Max | <in@Mv_vMO6NAxPjsd1NXTyJLk | maxon::Float64 | Input | false | false | false |  |  | 1 | 
Inputs/Transform/Min/Max/Min | <in@HGAe8s2zJtsnLs1Ts$7NEm | maxon::Float64 | Input | false | false | false |  |  | -1 | 
Inputs/Transform/Modifier Space | <in@GpJpUHa5KVGpWXY4GPx44$ | maxon::Int64 | Input | false | false | true |  |  |  | Local = 0, Global = 1, Modifier = 2
Inputs/Transform/Offset | <float2 | maxon::Float64 | Input | false | false | false |  |  | 10 | 
Inputs/Transform/Offset | <in@Eof0ZHrjC9pnS0BRoTiXo4 | maxon::Vector64 | Input | false | false | false |  |  | (0,100,0) | 
Outputs/Geometry | >geometryout | maxon::GeometryObject | Output | false | false | false |  |  |  | 

