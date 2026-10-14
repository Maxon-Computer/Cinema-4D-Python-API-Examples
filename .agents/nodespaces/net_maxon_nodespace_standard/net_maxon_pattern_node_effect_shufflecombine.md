# Node Template: Shuffle Combine

- **Node Space ID:** `net.maxon.nodespace.standard`
- **Template ID:** `net.maxon.pattern.node.effect.shufflecombine`
- **Template Name:** `Shuffle Combine`

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
Node Category | net.maxon.node.base.category | maxon::InternedId | Attribute | false | false | true |  |  | functions | operators = operators, distributions = distributions, geometries = geometries, patterns = patterns, primitives = primitives, effectors = effectors, fields = fields, functions = functions, structures = structures
Preview/Node | net.maxon.node.base.nodepreviewimage | maxon::ImageBaseRef | Attribute | false | false | false |  |  |  | 
Inputs/Alpha | <alphacomponent | maxon::InternedId | Input | false | false | true |  |  | alpha1 | Color1.red = red1, Color2.red = red2, Color1.green = green1, Color2.green = green2, Color1.blue = blue1, Color2.blue = blue2, Color1.alpha = alpha1, Color2.alpha = alpha2, Zero = zero, One = one
Inputs/Blue | <bluecomponent | maxon::InternedId | Input | false | false | true |  |  | blue1 | Color1.red = red1, Color2.red = red2, Color1.green = green1, Color2.green = green2, Color1.blue = blue1, Color2.blue = blue2, Color1.alpha = alpha1, Color2.alpha = alpha2, Zero = zero, One = one
Inputs/Color 1 | <color1 | maxon::ColorA | Input | false | false | false |  |  | (0,0,0,1) | 
Inputs/Color 2 | <color2 | maxon::ColorA | Input | false | false | false |  |  | (1,1,1,1) | 
Inputs/Green | <greencomponent | maxon::InternedId | Input | false | false | true |  |  | green1 | Color1.red = red1, Color2.red = red2, Color1.green = green1, Color2.green = green2, Color1.blue = blue1, Color2.blue = blue2, Color1.alpha = alpha1, Color2.alpha = alpha2, Zero = zero, One = one
Inputs/Red | <redcomponent | maxon::InternedId | Input | false | false | true |  |  | red1 | Color1.red = red1, Color2.red = red2, Color1.green = green1, Color2.green = green2, Color1.blue = blue1, Color2.blue = blue2, Color1.alpha = alpha1, Color2.alpha = alpha2, Zero = zero, One = one
Outputs/Result | >result | maxon::ColorA | Output | false | false | false |  |  |  | 

