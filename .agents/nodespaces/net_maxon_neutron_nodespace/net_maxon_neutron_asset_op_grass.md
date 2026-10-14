# Node Template: Grass

- **Node Space ID:** `net.maxon.neutron.nodespace`
- **Template ID:** `net.maxon.neutron.asset.op.grass`
- **Template Name:** `Grass`

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
Inputs/Op/Geometry | <net.maxon.neutron.op.input/geometry | maxon::GeometryObject | Attribute | false | false | false |  |  |  | 
Node Category | net.maxon.node.base.category | maxon::InternedId | Attribute | false | false | true |  |  | functions | distributions = distributions, operators = operators, geometries = geometries, patterns = patterns, primitives = primitives, effectors = effectors, fields = fields, functions = functions, structures = structures, geomodifiers = geomodifiers, geogenerators = geogenerators
Outputs/Op/Color | >net.maxon.neutron.op.output/color | maxon::Color | Attribute | false | false | false |  |  | (1,1,1) | 
Outputs/Op/Geometry | >net.maxon.neutron.op.output/geometry | maxon::GeometryObject | Attribute | false | false | false |  |  |  | 
Outputs/Op/Matrix | >net.maxon.neutron.op.output/matrix | maxon::Matrix | Attribute | false | false | false |  |  |  | 
Preview/Node | net.maxon.node.base.nodepreviewimage | maxon::ImageBaseRef | Attribute | false | false | false |  |  |  | 
Show Tag | net.maxon.neutron.showtag |  | Attribute | false | false | false |  |  |  | 
Inputs/Bypass | <net.maxon.node.bypassable.bypass | maxon::Bool | Input | false | false | false |  |  |  | 
Inputs/Op | <net.maxon.neutron.op.input | net.maxon.neutron.portbundle.object | Input | false | true | false |  |  |  | 
Object/Bend | <inport@QC0U48_XFBjjz4tGU7IUvt | maxon::Float64 | Input | false | false | false |  |  | 0.8 | 
Object/Blade Length | <inport@CRK$VBD3NBVjknvuwGC78r | maxon::Float64 | Input | false | false | false |  |  | 20 | 
Object/Blade Width | <inport@IAaOD9Q4LpzmKmSFnBCwzp | maxon::Float64 | Input | false | false | false |  |  | 2 | 
Object/Color | <inport@eJCqBV$ALBDjDSoLKr4J27 | maxon::ColorA64 | Input | false | false | false |  |  | (0.089,0.319,0.048,1) | 
Object/Color Texture | <inport@Nk4RTLsVJJbh$qEhTi_S0t | maxon::Color64 | Input | false | false | false |  |  | (1,1,1,1) | 
Object/Crinkle | <inport@WSKTsyRjFdfo4kp25Ilpgu | maxon::Float64 | Input | false | false | false |  |  | 0 | 
Object/Density | <inport@fZrwFF4DDdWt6XewJHsy0s | maxon::Float64 | Input | false | false | false |  |  | 0.5 | 
Object/Density Texture | <inport@FSYXkcU7JdllFu_fUQWE$p | maxon::Float64 | Input | false | false | false |  |  |  | 
Object/Mix Strength | <inport@ZDbXKa7tCl0vOlIghTEhp9 | maxon::Float64 | Input | false | false | false |  | 1 | 0 | 
Object/Randomize | <inport@UuoRmJuiANki_Nrad0LqSr | maxon::Float64 | Input | false | false | false |  |  | 0.5 | 
Object/Segments | <inport@f2qPhVIUK9Kmm44KVBqdYt | maxon::Int64 | Input | false | false | false | 1 | 100 | 16 | 
Object/Taper | <inport@dsl4F4ZLEtbjdqhrei6Pms | maxon::Float64 | Input | false | false | false |  | 1 | 0.8 | 
Outputs/Op/Filter | >net.maxon.neutron.op.output/filter | maxon::Bool | Input | false | false | false |  |  |  | 
Outputs/Op/Position | >net.maxon.neutron.op.output/translation |  | Input | false | false | false |  |  |  | 
Outputs/Op/Rotation/Scale/Shear | >net.maxon.neutron.op.output/sqrmatrix |  | Input | false | false | false |  |  |  | 
Outputs/Op/Scope | >net.maxon.neutron.op.output/domain |  | Input | false | false | false |  |  |  | 
Outputs/Op | >net.maxon.neutron.op.output | net.maxon.neutron.portbundle.object | Output | false | true | false |  |  |  | 

