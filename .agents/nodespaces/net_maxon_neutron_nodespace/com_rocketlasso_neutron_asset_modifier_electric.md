# Node Template: Electric Spline Modifer

- **Node Space ID:** `net.maxon.neutron.nodespace`
- **Template ID:** `com.rocketlasso.neutron.asset.modifier.electric`
- **Template Name:** `Electric Spline Modifer`

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
Electric/ | <in@OoFI7$QOK9OvHgimi0uUvD |  | Input | false | false | false |  |  |  | 
Electric/Animate | <in@YzYh7exjH5MrEkSwo9dUKD | maxon::TimeValue | Input | false | false | false |  |  | 1 | 
Electric/Animation Speed | <in@B92lJ6kQF9riuNuUmiZ0aY | maxon::Float64 | Input | false | false | false |  |  | 1 | 
Electric/Blend | <in@CcoA1agOAZZiOShZqjBg4F | maxon::Float64 | Input | false | false | false |  | 1 | 0.15 | 
Electric/Blend Start & End | <in@UMyOBY0xHdwjYwYdBzSygP | maxon::Float64 | Input | false | false | false |  |  | 0 | 
Electric/Circle Calc | <in@U3TwK3$nBpwpzDu4JcEmh8 | maxon::Bool | Input | false | false | false |  |  | false | 
Electric/Clone Count | <in@c8yNakokC9FvznW7xEJhDA | maxon::Int64 | Input | false | false | false | 1 |  |  | 
Electric/Displacement      | <in@M7HKUi6qD53sbqtZAjtV3d | maxon::Float64 | Input | false | false | false |  |  | 50 | 
Electric/End | <in@T183r5iXOJ7s11W5CqPD$Z | maxon::Float64 | Input | false | false | false |  | 1 | 1 | 
Electric/Fix Start & End | <in@Kw9r8uslHBAm04CdlmKDom |  | Input | false | false | false |  |  |  | 
Electric/Group | <in@c4VVWGu3NliuQAt5koRguc |  | Input | false | false | false |  |  |  | 
Electric/Loop Period | <in@NZgznyIqDZProC2wTCEP2Z | maxon::TimeValue | Input | false | false | false |  |  | 0 | 
Electric/Modify | <in@AxQ0DCg6Jdvhn2a2UxYxK8 |  | Input | false | false | false |  |  |  | 
Electric/Movement           | <in@JE1bN7lQBd6u1yj43CKH6H | maxon::Float64 | Input | false | false | false |  |  | 0 | 
Electric/Movement Rate | <in@BiylqFbeKxTp6nWf6otE6d | maxon::Float64 | Input | false | false | false |  |  | 0 | 
Electric/Noise | <in@H7R9WD9WFV0hF9e2_GShuC |  | Input | false | false | false |  |  |  | 
Electric/Noise | <in@Pj5ixm0UPxcl4CYnhdHDmB |  | Input | false | false | false |  |  |  | 
Electric/Noise Frequency | <in@U8MXviWnCxInyn1nOZZX6c | maxon::Float64 | Input | false | false | false |  |  | 1 | 
Electric/Noise Type  | <in@dvS8GXKaDlfj$B3krTQAUC | maxon::Id | Input | false | false | true |  |  | net.maxon.render.rendernoiseclass.perlin | registry#net.maxon.render.registry.rendernoiseclasses = registry#net.maxon.render.registry.rendernoiseclasses
Electric/Octaves | <in@S2hK4cuFFhSkkGerlmLe_b | maxon::Float64 | Input | false | false | false |  | 20 | 8 | 
Electric/Override Time      | <in@ZvkVU9fsKlGmBW1rnCs1f5 | maxon::Bool | Input | false | false | false |  |  |  | 
Electric/Per Segment Seed | <in@YFk4l$ByJtfqtDSKLCq5KG | maxon::Bool | Input | false | false | false |  |  | true | 
Electric/Pivot From | <in@GH2NfovIMRItN4zgtH_NWe | maxon::Float64 | Input | false | false | false |  |  | 0 | 
Electric/Relative Scale | <in@JuVw$MbLGR3h8Kd7Uq0XHU | maxon::Vector64 | Input | false | false | false |  | (1,1,1) |  | 
Electric/Resample Group | <in@NfElUwmNDNjhtyF2HSeLPE |  | Input | false | false | false |  |  |  | 
Electric/Resample Group/Resample             | <in@C4fBCBUjLh2ko66QcUFOWD | maxon::Bool | Input | false | false | false |  |  | true | 
Electric/Resample Group/Step | <in@JcH9oLamCB7ipt8JH6qZsd | maxon::Float64 | Input | false | false | false |  |  | 1 | 
Electric/Seed                    | <in@S3ySdK4$Cl5iAfjE15BzMe | maxon::Int64 | Input | false | false | false |  | 99999999 | 12345 | 
Electric/Smooth Iterations | <in@OUtbe25fExpjoFLVS6xRKa | maxon::Int64 | Input | false | false | false |  |  | 0 | 
Electric/Start               | <in@Xg_$F3eqOx2qvdIMt2tuab | maxon::Float64 | Input | false | false | false |  | 1 | 1 | 
Electric/Time | <in@HtCoilZlMdNnax9fZ1Jg4G | maxon::TimeValue | Input | false | false | false |  |  |  | 
Inputs/Capsule In Object Space | <modifiermatrix | maxon::Matrix64 | Input | false | false | false |  |  |  | 
Inputs/Geometry | <geometryin | maxon::GeometryObject | Input | false | false | false |  |  |  | 
Inputs/Global Capsule Matrix | <globalmatin | maxon::Matrix64 | Input | false | false | false |  |  |  | 
Inputs/Global Object Matrix | <objectmatrix | maxon::Matrix64 | Input | false | false | false |  |  |  | 
Inputs/Local Capsule Matrix | <localmatin | maxon::Matrix64 | Input | false | false | false |  |  |  | 
Inputs/Local Object Matrix | <localobjectmatrix | maxon::Matrix64 | Input | false | false | false |  |  |  | 
Outputs/Geometry | >geometryout | maxon::GeometryObject | Output | false | false | false |  |  |  | 

