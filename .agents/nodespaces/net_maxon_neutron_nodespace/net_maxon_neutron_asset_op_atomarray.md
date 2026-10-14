# Node Template: Atom Array

- **Node Space ID:** `net.maxon.neutron.nodespace`
- **Template ID:** `net.maxon.neutron.asset.op.atomarray`
- **Template Name:** `Atom Array`

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
Basic/Show Tag | net.maxon.neutron.showtag | maxon::Bool | Attribute | false | false | false |  |  |  | 
Filter Tags | net.maxon.node.base.filtertags | maxon::CString | Attribute | false | false | false |  |  |  | 
Inputs/Op/Matrix | <objectinput/matrix | maxon::Matrix | Attribute | false | false | false |  |  |  | 
Node Category | net.maxon.node.base.category | maxon::InternedId | Attribute | false | false | true |  |  | functions | distributions = distributions, operators = operators, geometries = geometries, patterns = patterns, primitives = primitives, effectors = effectors, fields = fields, functions = functions, structures = structures, geomodifiers = geomodifiers, geogenerators = geogenerators
Object/Objects/Object Bundle.1/Color | <inport@QKxTnKS4NdJnT2RA7UuvfI/_0/color | maxon::Color | Attribute | false | false | false |  |  | (1,1,1) | 
Object/Objects/Object Bundle.1/Geometry | <inport@QKxTnKS4NdJnT2RA7UuvfI/_0/geometry | maxon::GeometryObject | Attribute | false | false | false |  |  |  | 
Object/Objects/Object Bundle.1/Matrix | <inport@QKxTnKS4NdJnT2RA7UuvfI/_0/matrix | maxon::Matrix | Attribute | false | false | false |  |  |  | 
Object/Objects/Object Bundle.2/Color | <inport@QKxTnKS4NdJnT2RA7UuvfI/_1/color | maxon::Color | Attribute | false | false | false |  |  | (1,1,1) | 
Object/Objects/Object Bundle.2/Geometry | <inport@QKxTnKS4NdJnT2RA7UuvfI/_1/geometry | maxon::GeometryObject | Attribute | false | false | false |  |  |  | 
Object/Objects/Object Bundle.2/Matrix | <inport@QKxTnKS4NdJnT2RA7UuvfI/_1/matrix | maxon::Matrix | Attribute | false | false | false |  |  |  | 
Outputs/Op/Matrix | >matrixout/matrix | maxon::Matrix | Attribute | false | false | false |  |  |  | 
Preview/Node | net.maxon.node.base.nodepreviewimage | maxon::ImageBaseRef | Attribute | false | false | false |  |  |  | 
Basic/Bypass | <net.maxon.node.bypassable.bypass | maxon::Bool | Input | false | false | false |  |  |  | 
Basic/Children | <net.maxon.neutron.op.objectbase.children | net.maxon.neutron.portbundle.object | Input | true | false | false |  |  |  | 
Coord/Matrix | <net.maxon.neutron.op.objectbase.matrix | maxon::Matrix64 | Input | false | false | false |  |  |  | 
Inputs/Op | <net.maxon.neutron.op.input | net.maxon.neutron.portbundle.object | Input | false | true | false |  |  |  | 
Inputs/Op | <objectinput | net.maxon.neutron.portbundle.object | Input | false | true | false |  |  |  | 
Inputs/Op/Children | <objectinput/children |  | Input | false | false | false |  |  |  | 
Inputs/Op/Parent Matrix | <objectinput/parentmatrix |  | Input | false | false | false |  |  |  | 
Inputs/Op/Position | <net.maxon.neutron.op.input/translation |  | Input | false | false | false |  |  |  | 
Inputs/Op/Position | <objectinput/translation |  | Input | false | false | false |  |  |  | 
Inputs/Op/Rotation/Scale/Shear | <net.maxon.neutron.op.input/sqrmatrix |  | Input | false | false | false |  |  |  | 
Inputs/Op/Rotation/Scale/Shear | <objectinput/sqrmatrix |  | Input | false | false | false |  |  |  | 
Inputs/Op/Scope | <net.maxon.neutron.op.input/domain |  | Input | false | false | false |  |  |  | 
Inputs/Op/Scope | <objectinput/domain |  | Input | false | false | false |  |  |  | 
Object/Cylinder | <VaoCjviMMdbm4Ui8ymlaEL |  | Input | false | false | false |  |  |  | 
Object/Height Segments | <inport@Inpg2e6IOF3n46dyDdihLA | maxon::Int64 | Input | false | false | false | 1 | 5000 | 1 | 
Object/Hide Input Geometry | <inport@Jh_JX$ITL1Ck0_FVwkmNWP | maxon::Bool | Input | false | false | false |  |  |  | 
Object/Material | <inport@QOanl7RVMhkg86Us8dCQ4M | maxon::nbo::ParametrizedMaterial | Input | false | false | false |  |  |  | 
Object/Material | <inport@Qep0qJL8HJdjzH_93fsBKP | maxon::nbo::ParametrizedMaterial | Input | false | false | false |  |  |  | 
Object/Objects | <inport@QKxTnKS4NdJnT2RA7UuvfI | net.maxon.neutron.portbundle.object | Input | true | true | false |  |  |  | 
Object/Objects/Object Bundle.1 | <inport@QKxTnKS4NdJnT2RA7UuvfI/_0 | net.maxon.neutron.portbundle.object | Input | false | false | false |  |  |  | 
Object/Objects/Object Bundle.1/Children | <inport@QKxTnKS4NdJnT2RA7UuvfI/_0/children |  | Input | false | false | false |  |  |  | 
Object/Objects/Object Bundle.1/Filter | <inport@QKxTnKS4NdJnT2RA7UuvfI/_0/filter | maxon::Bool | Input | false | false | false |  |  |  | 
Object/Objects/Object Bundle.1/Material | <inport@QKxTnKS4NdJnT2RA7UuvfI/_0/material | maxon::DataDictionary | Input | false | false | false |  |  |  | 
Object/Objects/Object Bundle.1/Scope | <inport@QKxTnKS4NdJnT2RA7UuvfI/_0/domain |  | Input | false | false | false |  |  |  | 
Object/Objects/Object Bundle.2 | <inport@QKxTnKS4NdJnT2RA7UuvfI/_1 | net.maxon.neutron.portbundle.object | Input | false | false | false |  |  |  | 
Object/Objects/Object Bundle.2/Children | <inport@QKxTnKS4NdJnT2RA7UuvfI/_1/children |  | Input | false | false | false |  |  |  | 
Object/Objects/Object Bundle.2/Filter | <inport@QKxTnKS4NdJnT2RA7UuvfI/_1/filter | maxon::Bool | Input | false | false | false |  |  |  | 
Object/Objects/Object Bundle.2/Material | <inport@QKxTnKS4NdJnT2RA7UuvfI/_1/material | maxon::DataDictionary | Input | false | false | false |  |  |  | 
Object/Objects/Object Bundle.2/Scope | <inport@QKxTnKS4NdJnT2RA7UuvfI/_1/domain |  | Input | false | false | false |  |  |  | 
Object/Radius | <inport@FGwhAtwUJxai3vzk0R_fKK | maxon::Float64 | Input | false | false | false |  |  | 5 | 
Object/Radius | <inport@exs4xL1_ApEjUhD3s_W3IN | maxon::Float64 | Input | false | false | false |  |  | 15 | 
Object/Rotate | <inport@TR1KMDOtIl4lqSyqHD28DA | maxon::Float64 | Input | false | false | false |  |  |  | 
Object/Rotation Segments | <inport@C4xHtKxLJhrppjuHhLUNIH | maxon::Int64 | Input | false | false | false | 3 | 5000 | 16 | 
Object/Scaling | <inport@A4EBjUaRL9osTaaxUk_aaP | maxon::Float64 | Input | false | false | false |  |  | 1 | 
Object/Segments | <inport@DMMr7Q_UDFOs$YD8qcLmmE | maxon::Int64 | Input | false | false | false | 3 | 5000 | 24 | 
Object/Spheres | <C4CY0JqWMBZu_1nLoo6rIN |  | Input | false | false | false |  |  |  | 
Outputs/Op/Children | >matrixout/children |  | Input | false | false | false |  |  |  | 
Outputs/Op/Children | >net.maxon.neutron.op.output/children |  | Input | false | false | false |  |  |  | 
Outputs/Op/Parent Matrix | >matrixout/parentmatrix |  | Input | false | false | false |  |  |  | 
Outputs/Op/Position | >matrixout/translation |  | Input | false | false | false |  |  |  | 
Outputs/Op/Rotation/Scale/Shear | >matrixout/sqrmatrix |  | Input | false | false | false |  |  |  | 
Outputs/Op/Scope | >matrixout/domain |  | Input | false | false | false |  |  |  | 
Outputs/Op/Scope | >net.maxon.neutron.op.output/domain |  | Input | false | false | false |  |  |  | 
Outputs/Op | >matrixout | net.maxon.neutron.portbundle.object | Output | false | true | false |  |  |  | 
Outputs/Op | >net.maxon.neutron.op.output | net.maxon.neutron.portbundle.object | Output | false | true | false |  |  |  | 
Outputs/Output | >children.out |  | Output | false | false | false |  |  |  | 

