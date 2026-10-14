# Node Template: Break Spline Modifer

- **Node Space ID:** `net.maxon.neutron.nodespace`
- **Template ID:** `com.rocketlasso.neutron.asset.break.modifier`
- **Template Name:** `Break Spline Modifer`

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
Inputs/Capsule In Object Space | <modifiermatrix | maxon::Matrix64 | Input | false | false | false |  |  |  | 
Inputs/Geometry | <geometryin | maxon::GenericInstantiation<maxon::GeometryObject, maxon::StaticMeshPlaceholder, maxon::StaticPolylinePlaceholder, maxon::StaticCurvePlaceholder> | Input | false | false | false |  |  |  | 
Inputs/Global Capsule Matrix | <globalmatin | maxon::Matrix64 | Input | false | false | false |  |  |  | 
Inputs/Global Object Matrix | <objectmatrix | maxon::Matrix64 | Input | false | false | false |  |  |  | 
Inputs/Local Capsule Matrix | <localmatin | maxon::Matrix64 | Input | false | false | false |  |  |  | 
Inputs/Local Object Matrix | <localobjectmatrix | maxon::Matrix64 | Input | false | false | false |  |  |  | 
Object/Angle Group/Angle             | <in@S0Ff7CVWLFFnsisAvq4MRS | maxon::Float64 | Input | false | false | false |  | 3.142 | 1.553 | 
Object/Break | <in@aFN9hwFeAR1i4GhG9jnLlQ | maxon::Int64 | Input | false | false | true |  |  | 2 | Length = 1, Count = 2, Percentage = 0, Angle = 4, Points = 3
Object/Count Group/Count             | <in@W$CP3Qt8NJivyot3MmCbJU | maxon::Int64 | Input | false | false | false |  |  | 10 | 
Object/Gap Group/End Snap        | <in@bwjHdlkHBRorR2rVKMS0cJ | maxon::Bool | Input | false | false | false |  |  |  | 
Object/Gap Group/Gap | <in@OwBedflVD9nmcpMe4L8uIP | maxon::Float64 | Input | false | false | false |  |  | 2 | 
Object/Gap Group/Mode | <in@dCiuO6ySKJYo5otXBA3Xrm | maxon::Int64 | Input | false | false | true |  |  | 1 | Subdivide = 0, Split = 1
Object/Length Group/Length            | <attr@ZtfouorFL16tHpOGAlsHrY | maxon::Float64 | Input | false | false | false |  |  | 10 | 
Object/Noise/Brightness | <in@A6xFiP6vOtptWsI8yi8GYx | maxon::Float64 | Input | false | false | false |  | 1 | 0 | 
Object/Noise/Contrast | <in@GvA0v16MIpkujAGMh6zgr$ | maxon::Float64 | Input | false | false | false |  | 1 | 0.1 | 
Object/Noise/High Clip | <in@GI1aCPhzA5Ahv8AykGgSs2 | maxon::Float64 | Input | false | false | false |  | 1 | 1 | 
Object/Noise/Loop Period | <attr@XoncdKuCGJijlD9iTri8h8 | maxon::TimeValue | Input | false | false | false |  |  | 0 | 
Object/Noise/Low Clip | <in@b6GZqIyGC50kQlWJ$Sd5D2 | maxon::Float64 | Input | false | false | false |  | 1 | 0 | 
Object/Noise/Noise             | <in@D85AnUAVAtxlvpwbbyQcFw | maxon::Id | Input | false | false | true |  |  | net.maxon.render.rendernoiseclass.perlin | registry#net.maxon.render.registry.rendernoiseclasses = registry#net.maxon.render.registry.rendernoiseclasses
Object/Noise/Octaves | <in@XKAAMTy_GhFiaSUvB87t5y | maxon::Float64 | Input | false | false | false |  | 20 | 2 | 
Object/Noise/Scale | <in@Psnk8qTxL1onBLn7wdRaIw | maxon::Float64 | Input | false | false | false |  |  | 1 | 
Object/Noise/Speed | <in@eBh92phhAd2r43nUwpp8Fz | maxon::Float64 | Input | false | false | false |  |  | 0.25 | 
Object/Offset           | <attr@U0pY_pIfFJDgVIfmSdrfot | maxon::Float64 | Input | false | false | false |  |  | 0 | 
Object/Percentage Group/Percentage     | <in@YW0zNdOpP1ntnkvco5QhAS | maxon::Float64 | Input | false | false | false |  | 0.5 | 0.25 | 
Object/Random Group/Random Mode | <in@ENdyqeRIANkg30Lw3pVLCm | maxon::Int64 | Input | false | false | true |  |  | 0 | Random = 0, Noise = 1
Object/Random Group/Randomness | <in@Kasd0cQhFpeqpo9DMBXgUR | maxon::Float64 | Input | false | false | false |  | 1 | 0 | 
Object/Seed                 | <attr@SORStSnHNZQnh9Hfk2brNp | maxon::Int64 | Input | false | false | false |  |  | 12345 | 
Object/Start/End Bias | <in@ZC2hrVLkH9Pndq6EfPslHN | maxon::Float64 | Input | false | false | false | -1 | 1 | 0 | 
Object | >out@SzF$I6BdLVihMstQFI5e9f |  | Output | false | false | false |  |  |  | 
Outputs/Geometry | >geometryout | maxon::GeometryObject | Output | false | false | false |  |  |  | 

