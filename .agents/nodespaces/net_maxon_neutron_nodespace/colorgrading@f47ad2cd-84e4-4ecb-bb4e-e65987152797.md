# Node Template: Color Grading

- **Node Space ID:** `net.maxon.neutron.nodespace`
- **Template ID:** `colorgrading@f47ad2cd-84e4-4ecb-bb4e-e65987152797`
- **Template Name:** `Color Grading`

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
Node Category | net.maxon.node.base.category | maxon::InternedId | Attribute | false | false | true |  |  | functions | operators = operators, distributions = distributions, geometries = geometries, patterns = patterns, primitives = primitives, effectors = effectors, fields = fields, functions = functions, structures = structures, geomodifiers = geomodifiers, geogenerators = geogenerators
Preview/Node | net.maxon.node.base.nodepreviewimage | maxon::ImageBaseRef | Attribute | false | false | false |  |  |  | 
Inputs/Clamp/Clamp | <in1@Mpr1UVQUA9dskhyhMGECrU | maxon::Bool | Input | false | false | false |  |  |  | 
Inputs/Clamp/Clamp Maximum | <in3@TahSguWZHJ4sPbrnHS4AOS | maxon::Color64 | Input | false | false | false |  |  | 1 | 
Inputs/Clamp/Clamp Minimum | <in2@F3tGQO9uPNZjXwNE4YE4pV | maxon::Color64 | Input | false | false | false |  |  | 0 | 
Inputs/Color | <inport@Jp0P0LPgNVKn8z_5hSslvW | maxon::ColorA64 | Input | false | false | false |  |  |  | 
Inputs/Exposure/Contrast | <contrast@Owe4UkWGOhQiWwwuMSIN4V | maxon::Float64 | Input | false | false | false | -1 | 1 | 0 | 
Inputs/Exposure/Exposure | <exposure@aAvhp92uH90v$3BVTefnCW | maxon::Float64 | Input | false | false | false | -100 | 100 | 0 | 
Inputs/Exposure/Gamma | <gamma@TzEMHgtVC15r9XWTlUZwAR | maxon::Float64 | Input | false | false | false | 0.001 | 100 | 1 | 
Inputs/Filter/Offset | <in2@Y2jx9U76BJqvt1uPLXKp9R | maxon::Color64 | Input | false | false | false |  |  |  | 
Inputs/Filter/Tint | <in2@JQRFdxhLPBckNWxryvaE8X | maxon::Color64 | Input | false | false | false |  |  | (1,1,1) | 
Inputs/Hue / Saturation/Hue | <hue@H$HHVWsZJdHv7gvuFzjj$T | maxon::Float64 | Input | false | false | false | -6.283 | 6.283 | 0 | 
Inputs/Hue / Saturation/Saturation | <saturation@e6Zen8VqFl_g4G34qTTbTX | maxon::Float64 | Input | false | false | false | -1 | 1 | 0 | 
Inputs/Split Toning/Balance | <in2@KJNuoFboItTqFBBO5$5GAW | maxon::Float64 | Input | false | false | false | -1 | 1 |  | 
Inputs/Split Toning/Highlights Saturation | <maskblend@Qu8ESzhHJRXknK1DIRRxmS | maxon::Float64 | Input | false | false | false |  | 1 |  | 
Inputs/Split Toning/Hue Highlights | <hue@XNiAPSQpLJbjb6lk6mXahO | maxon::Float64 | Input | false | false | false | 0 | 6.283 | 0 | 
Inputs/Split Toning/Hue Shadows | <hue@IR0QCOgqOdqr0fv3JIVPmK | maxon::Float64 | Input | false | false | false | 0 | 6.283 | 0 | 
Inputs/Split Toning/Shadows Saturation | <maskblend@KW5vIAdaGlbpGqPDfUYMkS | maxon::Float64 | Input | false | false | false |  | 1 |  | 
Inputs/Tones/Blacks | <in2@cs4UTHfYAhdhnvFxhGD3wU | maxon::Float64 | Input | false | false | false |  |  |  | 
Inputs/Tones/Mids | <exposure@KYxQmJ06K1RsT9WDBhOAvT | maxon::Float64 | Input | false | false | false |  |  |  | 
Inputs/Tones/Whites | <in2@cywe7MXXK17gqIURY5atwV | maxon::Float64 | Input | false | false | false |  |  | 0 | 
Inputs/White Balance/Temperature | <temperature@O24FndC_MRUrYbcmDiu0wV | maxon::Float64 | Input | false | false | false | -5 | 1 | 0 | 
Inputs/White Balance/Tint | <tint@S8bK3ihkHpciI50Hfk1L7S | maxon::Float64 | Input | false | false | false | -1 | 1 | 0 | 
Inputs/White Balance/White Point | <whitepoint@euvRVKxeKNZlW8g7py1FRK | maxon::Color64 | Input | false | false | false |  |  | (1,1,1) | 
Outputs/Result | >outport@S8iKyKDKL5vmVj8U_7mvbV | maxon::Color64 | Output | false | false | false |  |  |  | 

