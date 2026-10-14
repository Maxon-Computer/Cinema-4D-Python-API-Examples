# Node Template: Trefoil

- **Node Space ID:** `net.maxon.neutron.nodespace`
- **Template ID:** `net.maxon.neutron.asset.distribution.trefoil`
- **Template Name:** `Trefoil`

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
Node Category | net.maxon.node.base.category | maxon::InternedId | Attribute | false | false | true |  |  | distributions | operators = operators, distributions = distributions, geometries = geometries, patterns = patterns, primitives = primitives, effectors = effectors, fields = fields, functions = functions, structures = structures
Preview/Node | net.maxon.node.base.nodepreviewimage | maxon::ImageBaseRef | Attribute | false | false | false |  |  |  | 
Inputs/Angle | <inport@PmyseVMiAFglShU4YknT59 | maxon::Float64 | Input | false | false | false |  |  | 6.283 | 
Inputs/Count | <inport@PEU_MB5EAhBqq899NZyBV5 | maxon::Int64 | Input | false | false | false |  |  | 100 | 
Inputs/Index | <indexin | maxon::Int64 | Input | false | false | false |  |  |  | 
Inputs/Size | <inport@IMH7oWDRF9yhvOc84p1TjF | maxon::Vector64 | Input | false | false | false |  |  | (100,100,100) | 
Inputs/X Deform | <inport@PZ2RUkonER$gqByoEjZbA_ | maxon::Float64 | Input | false | false | false |  |  | 2 | 
Inputs/X Stretch | <inport@ZHNnsopYNZipcbSsDuyfy7 | maxon::Float64 | Input | false | false | false |  |  | 2 | 
Inputs/Y Deform | <inport@aSbPbU04MNYjECFxM0$7e$ | maxon::Float64 | Input | false | false | false |  |  | 2 | 
Inputs/Y Stretch | <inport@ehpFZG5LGpBoIImCW__Y4_ | maxon::Float64 | Input | false | false | false |  |  | 2 | 
Inputs/Z Deform | <inport@N1Uc09OeI5hnmBgpGy9EV_ | maxon::Float64 | Input | false | false | false |  |  | 2 | 
Inputs/Z Stretch | <inport@O2sEyQ7hMV9qSJyO_2YaH8 | maxon::Float64 | Input | false | false | false |  |  | -2 | 
Outputs/Count | >countout | maxon::Int64 | Output | false | false | false |  |  | 100 | 
Outputs/Distribution | >distchannelsout | net.maxon.neutron.portbundle.distributionbase | Output | false | true | false |  |  |  | 
Outputs/Distribution/Color | >distchannelsout/color |  | Output | false | false | false |  |  |  | 
Outputs/Distribution/Index | >distchannelsout/index |  | Output | false | false | false |  |  |  | 
Outputs/Distribution/Matrix | >distchannelsout/matrix |  | Output | false | false | false |  |  |  | 
Outputs/Distribution/Ratio | >distchannelsout/ratio |  | Output | false | false | false |  |  |  | 

