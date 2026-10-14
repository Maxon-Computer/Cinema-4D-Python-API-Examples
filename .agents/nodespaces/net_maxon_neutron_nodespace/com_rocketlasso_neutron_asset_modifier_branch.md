# Node Template: Branch Spline Modifier

- **Node Space ID:** `net.maxon.neutron.nodespace`
- **Template ID:** `com.rocketlasso.neutron.asset.modifier.branch`
- **Template Name:** `Branch Spline Modifier`

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
Direction/Branch Steps/ | <in@TjNx$dsSCpagoAQf8DVFgK |  | Input | false | false | false |  |  |  | 
Direction/Branch Steps/Noise Frequency | <in@AxJXWzg5NBytWZfLorKWs_ | maxon::Float64 | Input | false | false | false |  |  | 1 | 
Direction/Branch Steps/Start/End Influence | <in@WbJOuGQgJxnoxplh4mQwe8 | maxon::Float64 | Input | false | false | false | -1 | 1 | 0 | 
Direction/Branch Steps/Steps | <in@NQBZfrcGBJ8tr5zLTuUQFp | maxon::Int64 | Input | false | false | false | 0 | 999999 | 10 | 
Direction/Branch Steps/Total Angle | <in@LX4DvJ9DPVOowpu1SIeLEs | maxon::Float64 | Input | false | false | false |  |  | 0 | 
Direction/Branch Steps/Total Angle Variation | <in@ZxunxcZsHNHi7bQANg_$6t | maxon::Float64 | Input | false | false | false |  | 6.283 | 1.047 | 
Direction/Branch Steps/Total Roll | <in@AQRWsUViGFtkfBPV7Fk0$o | maxon::Float64 | Input | false | false | false |  |  | 0 | 
Direction/Branch Steps/Total Roll Variation | <in@LQYVD2yVEV3uRCHFIpTfU4 | maxon::Float64 | Input | false | false | false |  | 3.142 | 0 | 
Direction/Gravity/Gravity | <in@amne4wrFIdqnTInb3Zb8wu | maxon::Float64 | Input | false | false | false | -1 | 1 | 0 | 
Direction/Gravity/Gravity Mode | <in@R1w8WkFJO9VvXoF182Jfu_ | maxon::Int64 | Input | false | false | true |  |  | 2 | Global = 2, Local = 3, Spherical = 1, Local Spherical = 0
Global/Keep Original | <in@cgMNdwaDPxZpARLaxfnxWv | maxon::Bool | Input | false | false | false |  |  | true | 
Global/Point Cap | <in@JghTfr$BKFoioYN$w1iHLN | maxon::Int64 | Input | false | false | false |  |  | 100000 | 
Global/Relative Direction | <in@LFbJjst5Mhdq1asZLLhP55 | maxon::Vector64 | Input | false | false | false |  | (1,1,1) | (1,1,1) | 
Global/Reweight | <in@ANZiS5I5CVDk2t57IuD4ow | maxon::Bool | Input | false | false | false |  |  | false | 
Global/Seed | <in@BMytqNbkLhMl4K7FdZzCqo | maxon::Int64 | Input | false | false | false |  |  | 12345 | 
Global/Spawn From | <in@XrWHGAcoC1pkaqe7Ta1a1w | maxon::Int64 | Input | false | false | true |  |  | 0 | Last Generation = 0, All = 1
Inputs/Geometry | <geometryin | maxon::GenericInstantiation<maxon::GeometryObject, maxon::StaticMeshPlaceholder, maxon::StaticPolylinePlaceholder, maxon::StaticCurvePlaceholder> | Input | false | false | false |  |  |  | 
Inputs/Global Capsule Matrix | <globalmatin | maxon::Matrix64 | Input | false | false | false |  |  |  | 
Inputs/Global Object Matrix | <objectmatrix | maxon::Matrix64 | Input | false | false | false |  |  |  | 
Inputs/Local Capsule Matrix | <localmatin | maxon::Matrix64 | Input | false | false | false |  |  |  | 
Inputs/Local Modifier Matrix | <modifiermatrix | maxon::Matrix64 | Input | false | false | false |  |  |  | 
Inputs/Local Object Matrix | <localobjectmatrix | maxon::Matrix64 | Input | false | false | false |  |  |  | 
Object/Branch Count | <in@fGNGNMuKPxFuThLQBQwOTv |  | Input | false | false | false |  |  |  | 
Object/Branch Count/ | <in@A00D1IzPIR8kQjBESU7cbs |  | Input | false | false | false |  |  |  | 
Object/Branch Count/Angle | <in@EOnjN5e0Hx3oidUHntJNgo | maxon::Float64 | Input | false | false | false |  | 3.142 | 1.553 | 
Object/Branch Count/Branches Max | <in@SdmLBvKfBZQuWhszpf_pB9 | maxon::Int64 | Input | false | false | false | 0 |  | 2 | 
Object/Branch Count/Branches Min | <in@D6tp_lrpEl3hmRNRnbKPY6 | maxon::Int64 | Input | false | false | false | 0 |  | 2 | 
Object/Branch Count/Count | <in@dLeUA9iYGlFnZcBbsvqcbs | maxon::Int64 | Input | false | false | false |  | 0 | 10 | 
Object/Branch Count/Length | <in@S9nG0ZPKN5nv3ZfX_X12Oq | maxon::Float64 | Input | false | false | false |  |  | 10 | 
Object/Branch Count/Percentage | <in@exF16SFOCRDjPDPM4lWhTp | maxon::Float64 | Input | false | false | false |  | 0.5 | 0.35 | 
Object/Branch Count/Placement | <in@UMkquuHwIxmoN2YfTga4uo | maxon::Int64 | Input | false | false | true |  |  | 2 | Length = 1, Count = 2, Percent = 0, Angle = 4, Points = 3
Object/Branch Count/Spread                | <in@StTF6TUCD1UpDZiAaGqklI | maxon::Float64 | Input | false | false | false |  | 1 | 0 | 
Object/Branch Properties | <in@Qxyp$XZ8Nd6hfyEWTFzacp |  | Input | false | false | false |  |  |  | 
Object/Branch Properties/Length Mode | <in@MVbSqT04JdimX6i2Qs9A6r | maxon::Int64 | Input | false | false | true |  |  | 1 | Relative = 0, Absolute = 1
Object/Branch Properties/Length Variation | <in@Zk$EoE1MEheuaprMTR8D0v | maxon::Float64 | Input | false | false | false |  | 1 | 0 | 
Object/Branch Properties/Relative Length | <in@DxXUh6bwL9QrxX5H0FDdQr | maxon::Float64 | Input | false | false | false |  | 1 | 1 | 
Object/Branch Properties/Start/End Length | <in@euhiB3GVC9BqlPHPP$g3g5 | maxon::Float64 | Input | false | false | false | -1 | 1 | 0 | 
Object/Branch Properties/Total Length | <in@Ok4mU9LzKBchRU3AmWfS$q | maxon::Float64 | Input | false | false | false |  |  | 100 | 
Object/Initial Direction | <in@LhgcBpfQA5TriUnCRaJ0zs |  | Input | false | false | false |  |  |  | 
Object/Initial Direction/Angle Offset | <in@T8E0TgR9E5bqDWj8k4lL0$ | maxon::Float64 | Input | false | false | false | -12566.371 |  | 0.524 | 
Object/Initial Direction/Angle Variation | <in@NpWc$bWlAlxrGtUs8OuHh_ | maxon::Float64 | Input | false | false | false |  | 3.142 | 0 | 
Object/Initial Direction/Direction | <in@B_xabNvvGFXlPtWhdTvpLo | maxon::Int64 | Input | false | false | true |  |  | 0 | Aligned = 0, Random = 1, X+ = 2, Z- = 7, X- = 3, Y+ = 4, Y- = 5, Z+ = 6
Object/Initial Direction/Radial Symmetry | <in@FEVfx1vnFdCk0i9BDIL8Lr | maxon::Bool | Input | false | false | false |  |  | true | 
Object/Initial Direction/Roll Offset | <in@CGqdmSVsIJDi98_J3$OxK_ | maxon::Float64 | Input | false | false | false |  |  | 0 | 
Object/Initial Direction/Roll Per Step | <in@JX$XskGwEViokj7zUxyWEp | maxon::Float64 | Input | false | false | false |  |  | 0 | 
Object/Initial Direction/Roll Variation | <in@Jke2X6YaLVTveqN3TW_ml6 | maxon::Float64 | Input | false | false | false |  | 6.283 | 0 | 
Object/Placement | <in@PlYUxLoRFh8mN6wpUx6Bmq |  | Input | false | false | false |  |  |  | 
Object/Placement/End | <in@eGUDZYg8AhzoMje8IPZkqr | maxon::Float64 | Input | false | false | false |  | 1 | 1 | 
Object/Placement/Start | <in@AxVu$zO4PZEmtflEJwHM6p | maxon::Float64 | Input | false | false | false |  | 1 | 0 | 
Object/Placement/Variation              | <in@XRe7mX7gHtJgtPQwYK$Qiq | maxon::Float64 | Input | false | false | false |  | 1 | 0 | 
Direction | >out@Vi0N6wmkGVDt9cMuKHp28M |  | Output | false | false | false |  |  |  | 
Outputs/Geometry | >geometryout | maxon::GeometryObject | Output | false | false | false |  |  |  | 

