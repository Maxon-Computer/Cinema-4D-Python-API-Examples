# Node Template: Partition Modifier

- **Node Space ID:** `net.maxon.neutron.nodespace`
- **Template ID:** `com.rocketlasso.neutron.asset.modifier.partition`
- **Template Name:** `Partition Modifier`

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
Object/Cut Algorithm         | <input_count2 | maxon::Int64 | Input | false | false | true |  |  | 1 | Largest (Stable Geo Dependent) = 0, Simple = 1
Object/Cut Iterations | <in@SwhAqUjOLRWrT2WalDbQNs | maxon::Int64 | Input | false | false | false |  |  | 2 | 
Object/Cut Orientation | <in@L$dtwYUNB9EiJKyQo$4UVr | maxon::Int64 | Input | false | false | true |  |  | 1 | Manual = 0, Alternating = 1, Longest Edge (Stable Geo Dependent) = 3
Object/Cuts | <input_count | maxon::Int64 | Input | false | false | false |  |  | 25 | 
Object/Global/Cut Cap | <in@Qnm1GZRlF9XjuvYd8Itn42 | maxon::Float64 | Input | false | false | false |  |  | 5000 | 
Object/Global/Gap | <in_float3 | maxon::Float64 | Input | false | false | false |  |  | 0.25 | 
Object/Global/Interpret Tris | <in@QdEY51swKxKgXlxm9z6nl2 | maxon::Int64 | Input | false | false | true |  |  | 1 | Ignore = 0, Subdivide = 1
Object/Global/Random Islands | <input_bool2 | maxon::Bool | Input | false | false | false |  |  | true | 
Object/Global/Randomize Order | <in@BMYGbjI_PVMg2iVrK46Xlr | maxon::Bool | Input | false | false | false |  |  | true | 
Object/Global/Seed | <in_float1 | maxon::Float64 | Input | false | false | false |  |  | 12345 | 
Object/Orientation H/W | <in@YWByGBLaC1tuohfh5rJQS8 | maxon::Float64 | Input | false | false | false | 0 | 1 | 0.5 | 
Object/Per Polygon | <bool | maxon::Bool | Input | false | false | false |  |  | false | 
Object/Polygon Orientation/Random Spin | <in@QoBaNM64Cl7p2ozVvcWN06 | maxon::Float64 | Input | false | false | false |  | 6.283 |  | 
Object/Polygon Orientation/Spin | <in_angle | maxon::Float64 | Input | false | false | false |  | 6.283 |  | 
Object/Polygon Orientation/UV Mapping         | <in@XuTnjBuvDVom7OjRoBTEet | maxon::Int64 | Input | false | false | true |  |  | 0 | Original = 0, Per Polygon = 1
Object/Random Animation/Animation Speed | <in@ScNsEh2TDZLiwvwGtNR9a9 | maxon::Float64 | Input | false | false | false |  | 1 | 0.5 | 
Object/Random Animation/Loop Period         | <in_time1 | maxon::TimeValue | Input | false | false | false |  |  | 0 | 
Object/Random Animation/Noise Frequency | <in_float2 | maxon::Float64 | Input | false | false | false |  |  | 1 | 
Object/Random Animation/Override Time | <input_bool | maxon::Bool | Input | false | false | false |  |  | false | 
Object/Random Animation/Random Offset | <in_float | maxon::Float64 | Input | false | false | false |  | 1 | 0 | 
Object/Random Animation/Time | <in_time | maxon::TimeValue | Input | false | false | false |  |  | 1 | 
Object/Random Density | <in@SpDS5z_HD1ZjaRt$jMH875 | maxon::Float64 | Input | false | false | false |  | 1 | 0.5 | 
Object/Randomize Cuts | <in@IHnMuHpLJVAmOZdAUHI_8w | maxon::Float64 | Input | false | false | false |  | 1 | 0.5 | 
Object/Selection String | <in@JuA2_so8K9AifTGGugM3_n | maxon::String | Input | false | false | false |  |  | All | 
Object/Skew | <in@Vay2fOnlARXoXDXjOdy0Cn | maxon::Float64 | Input | false | false | false | -1 | 1 |  | 
Object/Subdivision Type | <in@TPKCthkWFRDukzYnVDI2oo | maxon::Int64 | Input | false | false | true |  |  | 0 | Single = 0, Double = 1, Quad = 2
Outputs/Geometry | >geometryout | maxon::GeometryObject | Output | false | false | false |  |  |  | 

