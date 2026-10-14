# Node Template: Multi Shader

- **Node Space ID:** `net.maxon.nodespace.standard`
- **Template ID:** `multishader@a5b3ccd0f11041d9a2a73bd8798fab6c`
- **Template Name:** `Multi Shader`

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
Inputs/Color Mode | <mode@TLZ3ZCgtDp6tH0wx3TOGhW | maxon::InternedId | Input | false | false | true |  |  | luminance | Red (x) = red, Green (y) = green, Blue (z) = blue, Alpha = alpha, Average = average, Length = length, Squared Length = squaredlength, Luminance = luminance, Sum = sum, Min = min, Max = max
Inputs/Mode | <index@EpGLQ5A1NVHlbIMW8$yEVW | maxon::Int64 | Input | false | false | true |  |  |  | Random = 3, Color = 0, Iterate = 1, UVW = 2
Inputs/Seed | <seed@S2nfIt6hIldoiR5euF$3YW | maxon::Int64 | Input | false | false | false |  |  | 12345 | 
Inputs/Shaders | <in@EUAqQnPvIRzjqm3QQ0cKDQ | maxon::Color64 | Input | true | true | false |  |  |  | 
Inputs/Shaders/Shaders.1 | <in@EUAqQnPvIRzjqm3QQ0cKDQ/_0 | maxon::Color64 | Input | false | false | false |  |  |  | 
Inputs/Shaders/Shaders.2 | <in@EUAqQnPvIRzjqm3QQ0cKDQ/_1 | maxon::Color64 | Input | false | false | false |  |  |  | 
Inputs/Shaders/Shaders.3 | <in@EUAqQnPvIRzjqm3QQ0cKDQ/CNjr7OTjAdCkks9EeoQ57Q | maxon::Color64 | Input | false | false | false |  |  |  | 
Inputs/UVW Mode | <index@NMlCHoR4BBNjaAU_SQjqBW | maxon::Int64 | Input | false | false | true |  |  |  | U = 0, V = 1, W = 2
Outputs/Color | >color@B0sxjLtJLBouGpQwpOf5_R | maxon::Color64 | Output | false | false | false |  |  |  | 
Outputs/Mask | >outport@XYcWYsN7Dh7ivPH1gvsPPR | maxon::Float64 | Output | false | false | false |  |  |  | 

