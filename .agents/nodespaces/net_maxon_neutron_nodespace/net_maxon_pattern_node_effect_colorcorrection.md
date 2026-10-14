# Node Template: Selective Color

- **Node Space ID:** `net.maxon.neutron.nodespace`
- **Template ID:** `net.maxon.pattern.node.effect.colorcorrection`
- **Template Name:** `Selective Color`

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
Node Category | net.maxon.node.base.category | maxon::InternedId | Attribute | false | false | true |  |  | functions | distributions = distributions, operators = operators, geometries = geometries, patterns = patterns, primitives = primitives, effectors = effectors, fields = fields, functions = functions, structures = structures
Preview/Node | net.maxon.node.base.nodepreviewimage | maxon::ImageBaseRef | Attribute | false | false | false |  |  |  | 
Inputs/Color | <color | maxon::ColorA | Input | false | false | false |  |  |  | 
Inputs/Hue/Aqua | <hueaqua | maxon::Float | Input | false | false | false | -6.283 | 6.283 | 0 | 
Inputs/Hue/Blue | <hueblue | maxon::Float | Input | false | false | false | -6.283 | 6.283 | 0 | 
Inputs/Hue/Green | <huegreen | maxon::Float | Input | false | false | false | -6.283 | 6.283 | 0 | 
Inputs/Hue/Magenta | <huemagenta | maxon::Float | Input | false | false | false | -6.283 | 6.283 | 0 | 
Inputs/Hue/Orange | <hueorange | maxon::Float | Input | false | false | false | -6.283 | 6.283 | 0 | 
Inputs/Hue/Purple | <huepurple | maxon::Float | Input | false | false | false | -6.283 | 6.283 | 0 | 
Inputs/Hue/Red | <huered | maxon::Float | Input | false | false | false | -6.283 | 6.283 | 0 | 
Inputs/Hue/Yellow | <hueyellow | maxon::Float | Input | false | false | false | -6.283 | 6.283 | 0 | 
Inputs/Luminance/Aqua | <luminanceaqua | maxon::Float | Input | false | false | false | -1 | 1 | 0 | 
Inputs/Luminance/Blue | <luminanceblue | maxon::Float | Input | false | false | false | -1 | 1 | 0 | 
Inputs/Luminance/Green | <luminancegreen | maxon::Float | Input | false | false | false | -1 | 1 | 0 | 
Inputs/Luminance/Magenta | <luminancemagenta | maxon::Float | Input | false | false | false | -1 | 1 | 0 | 
Inputs/Luminance/Orange | <luminanceorange | maxon::Float | Input | false | false | false | -1 | 1 | 0 | 
Inputs/Luminance/Purple | <luminancepurple | maxon::Float | Input | false | false | false | -1 | 1 | 0 | 
Inputs/Luminance/Red | <luminancered | maxon::Float | Input | false | false | false | -1 | 1 | 0 | 
Inputs/Luminance/Yellow | <luminanceyellow | maxon::Float | Input | false | false | false | -1 | 1 | 0 | 
Inputs/Saturation/Aqua | <saturationaqua | maxon::Float | Input | false | false | false | -1 | 1 | 0 | 
Inputs/Saturation/Blue | <saturationblue | maxon::Float | Input | false | false | false | -1 | 1 | 0 | 
Inputs/Saturation/Green | <saturationgreen | maxon::Float | Input | false | false | false | -1 | 1 | 0 | 
Inputs/Saturation/Magenta | <saturationmagenta | maxon::Float | Input | false | false | false | -1 | 1 | 0 | 
Inputs/Saturation/Orange | <saturationorange | maxon::Float | Input | false | false | false | -1 | 1 | 0 | 
Inputs/Saturation/Purple | <saturationpurple | maxon::Float | Input | false | false | false | -1 | 1 | 0 | 
Inputs/Saturation/Red | <saturationred | maxon::Float | Input | false | false | false | -1 | 1 | 0 | 
Inputs/Saturation/Yellow | <saturationyellow | maxon::Float | Input | false | false | false | -1 | 1 | 0 | 
Mask/Blend | <maskblend | maxon::Float | Input | false | false | false |  | 1 | 1 | 
Mask/Components/Alpha | <maskalpha | maxon::Bool | Input | false | false | false |  |  |  | 
Mask/Components/Blue | <maskblue | maxon::Bool | Input | false | false | false |  |  | true | 
Mask/Components/Green | <maskgreen | maxon::Bool | Input | false | false | false |  |  | true | 
Mask/Components/Red | <maskred | maxon::Bool | Input | false | false | false |  |  | true | 
Outputs/Result | >result | maxon::ColorA | Output | false | false | false |  |  |  | 

