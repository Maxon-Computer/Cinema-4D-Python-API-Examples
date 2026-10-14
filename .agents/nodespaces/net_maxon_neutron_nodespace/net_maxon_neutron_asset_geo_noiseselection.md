# Node Template: Noise Selection

- **Node Space ID:** `net.maxon.neutron.nodespace`
- **Template ID:** `net.maxon.neutron.asset.geo.noiseselection`
- **Template Name:** `Noise Selection`

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
Node Category | net.maxon.node.base.category | maxon::InternedId | Attribute | false | false | true |  |  | functions | distributions = distributions, operators = operators, geometries = geometries, patterns = patterns, primitives = primitives, effectors = effectors, fields = fields, functions = functions, structures = structures, geomodifiers = geomodifiers, geogenerators = geogenerators
Preview/Node | net.maxon.node.base.nodepreviewimage | maxon::ImageBaseRef | Attribute | false | false | false |  |  |  | 
Inputs/Exponent | <inport@OCc0nwIsEBOk$pd6fW_Svf | maxon::Float64 | Input | false | false | false | 0.1 | 5 | 2 | 
Inputs/Gain | <inport@bgKdoo9iKxhuAARZcZWZaZ | maxon::Float64 | Input | false | false | false | 0.1 | 4 | 0.5 | 
Inputs/Geometry | <geometryin | maxon::GeometryObject | Input | false | false | false |  |  |  | 
Inputs/Invert | <in@CCjkaFLNF9Ks81D0CKVNnS | maxon::Bool | Input | false | false | false |  |  |  | 
Inputs/Lacunarity | <inport@E7HZnEnNHBflOQt8iNTNoe | maxon::Float64 | Input | false | false | false | 0.1 | 10 | 2.1 | 
Inputs/Noise Type | <inport@bJbxQf24P5GoxdbEkPntjm | maxon::Id | Input | false | false | true |  |  | net.maxon.render.rendernoiseclass.perlin | registry#net.maxon.render.registry.rendernoiseclasses = registry#net.maxon.render.registry.rendernoiseclasses
Inputs/Octaves | <inport@TYgphZAHOJLmQ_dK3Q$6Vm | maxon::Float64 | Input | false | false | false |  | 20 | 6 | 
Inputs/Outer Scope | <inport@OGwtjInYE5QowOm3Qy7fwF |  | Input | false | false | false |  |  |  | 
Inputs/Scale | <inport@ZskPR27jDFHnxrTv1U2nMk | maxon::Float64 | Input | false | false | false |  | 1 | 1 | 
Inputs/Seed | <inport@St8NnW_UD9ihABAeENBtxj | maxon::UInt32 | Input | false | false | false |  |  | 123 | 
Inputs/Store Noise | <inport@aGtG6tI1Edcv8K2OH$$Xi6 | maxon::String | Input | false | false | false |  |  |  | 
Inputs/Store Selection | <in@WXgFtWWtJVUumnH_kjZdSw | maxon::String | Input | false | false | false |  |  |  | 
Inputs/Threshold | <inport@Sch3d_yTO9LuO$4i_Aowdi | maxon::Float64 | Input | false | false | false |  | 1 | 0.5 | 
Inputs/Time | <inport@X$g0hY4INR4r4n$sKLcMQg | maxon::Float64 | Input | false | false | false |  |  |  | 
Inputs/Type | <inport@ZQ7nYgAKFxAuJ5Vi2xb93b | maxon::Int64 | Input | false | false | true |  |  | 0 | Points = 1, Edges = 2, Polygons = 0
Outputs/Edges | >outport@FORdxfWHGNSqxjZYYxisUc | maxon::Array<maxon::Tuple<maxon::Int32, maxon::Int32>> | Output | false | false | false |  |  |  | 
Outputs/Geometry | >geometryout | maxon::GeometryObject | Output | false | false | false |  |  |  | 
Outputs/Selection | >outport@RpYqzOhwEBauCzEvo_UWZl | maxon::Array<maxon::Int64> | Output | false | false | false |  |  |  | 

