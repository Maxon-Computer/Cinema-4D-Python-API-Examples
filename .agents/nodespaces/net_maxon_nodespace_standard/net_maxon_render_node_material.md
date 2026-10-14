# Node Template: Material

- **Node Space ID:** `net.maxon.nodespace.standard`
- **Template ID:** `net.maxon.render.node.material`
- **Template Name:** `Material`

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
Node Category | net.maxon.node.base.category | maxon::InternedId | Attribute | false | false | true |  |  | patterns | operators = operators, distributions = distributions, geometries = geometries, patterns = patterns, primitives = primitives, effectors = effectors, fields = fields, functions = functions, structures = structures, geomodifiers = geomodifiers, geogenerators = geogenerators
Preview/Node | net.maxon.node.base.nodepreviewimage | maxon::ImageBaseRef | Attribute | false | false | false |  |  |  | 
Context/Context | <context | maxon::ShadingContext | Input | false | false | false |  |  |  | 
Inputs/AOV Multi-Passes/AOV | <aovs | net.maxon.render.portbundle.aovmultipass | Input | true | false | false |  |  |  | 
Inputs/Absorption | <absorption | maxon::Color | Input | false | false | false |  |  | (1,1,1) | 
Inputs/Absorption Distance | <absorptiondistance | maxon::Float | Input | false | false | false |  |  | 100 | 
Inputs/Alpha | <alpha | maxon::Float | Input | false | false | false |  |  |  | 
Inputs/Blurriness | <blurriness | maxon::Float | Input | false | false | false |  | 1 | 0 | 
Inputs/Displacement | <displacement | maxon::Vector | Input | false | false | false |  |  |  | 
Inputs/Displacement Height | <displacementheight | maxon::Float | Input | false | false | false |  |  | 10 | 
Inputs/Emission | <emission | maxon::Color | Input | false | false | false |  |  |  | 
Inputs/Exit Reflections | <exitreflections | maxon::Bool | Input | false | false | false |  |  | true | 
Inputs/Fresnel Reflectivity | <fresnelreflectivity | maxon::Float | Input | false | false | false |  | 1 | 1 | 
Inputs/IOR | <ior | maxon::Float | Input | false | false | false | 1 | 5 | 1.517 | 
Inputs/Layer Alpha | <alphacontrol | maxon::Bool | Input | false | false | false |  |  |  | 
Inputs/Normal | <normal | maxon::Vector | Input | false | false | false |  |  |  | 
Inputs/Roughness | <roughness | maxon::Float | Input | false | false | false |  | 1 | 0 | 
Inputs/Round Geometry | <roundgeometry | maxon::Bool | Input | false | false | false |  |  | true | 
Inputs/Sampling Subdivision | <samplesubdiv | maxon::Float | Input | false | false | false | 0 | 16 | 4 | 
Inputs/Sub-Polygon Displacement | <spd | maxon::Bool | Input | false | false | false |  |  |  | 
Inputs/Subdivision Level | <spdlevel | maxon::Int | Input | false | false | false | 1 | 10 | 4 | 
Inputs/Surface | <bsdflayers | net.maxon.render.portbundle.bsdflayer | Input | true | true | false |  |  |  | 
Inputs/Surface/BSDF Layer.1 | <bsdflayers/_0 | net.maxon.render.portbundle.bsdflayer | Input | false | false | false |  |  |  | 
Inputs/Surface/BSDF Layer.1/Active | <bsdflayers/_0/active | maxon::Bool | Input | false | false | false |  |  | true | 
Inputs/Surface/BSDF Layer.1/BSDF Layer | <bsdflayers/_0/bsdflayer | maxon::BSDFLayer | Input | false | false | false |  |  |  | 
Inputs/Surface/BSDF Layer.1/Opacity | <bsdflayers/_0/strength | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Inputs/Surface/BSDF Layer.2 | <bsdflayers/_1 | net.maxon.render.portbundle.bsdflayer | Input | false | false | false |  |  |  | 
Inputs/Surface/BSDF Layer.2/Active | <bsdflayers/_1/active | maxon::Bool | Input | false | false | false |  |  | true | 
Inputs/Surface/BSDF Layer.2/BSDF Layer | <bsdflayers/_1/bsdflayer | maxon::BSDFLayer | Input | false | false | false |  |  |  | 
Inputs/Surface/BSDF Layer.2/Opacity | <bsdflayers/_1/strength | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Inputs/Transparency | <transparency | maxon::Color | Input | false | false | false |  |  | (1,1,1) | 
Inputs/Transparent | <enabletransparency | maxon::Bool | Input | false | false | false |  |  |  | 

