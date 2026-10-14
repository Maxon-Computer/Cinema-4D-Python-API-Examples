# Node Template: Color Layer

- **Node Space ID:** `com.redshift3d.redshift4c4d.class.nodespace`
- **Template ID:** `com.redshift3d.redshift4c4d.nodes.core.rscolorlayer`
- **Template Name:** `Color Layer`

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
Node Category | net.maxon.node.base.category | maxon::InternedId | Attribute | false | false | true |  |  | geometries | operators = operators, distributions = distributions, geometries = geometries, patterns = patterns, primitives = primitives, effectors = effectors, fields = fields, functions = functions, structures = structures, geomodifiers = geomodifiers, geogenerators = geogenerators
Preview/Node | net.maxon.node.base.nodepreviewimage | maxon::ImageBaseRef | Attribute | false | false | false |  |  |  | 
General/Advanced Overlay Options | <com.redshift3d.redshift4c4d.nodes.core.rscolorlayer.advanced_mode | maxon::Bool | Input | false | false | false |  |  | false | 
General/Base Layer/Color | <com.redshift3d.redshift4c4d.nodes.core.rscolorlayer.base_color | maxon::ColorA64 | Input | false | false | false |  |  | (0,0,0,1) | 
General/Base Layer/Color Has Premultiplied Alpha | <com.redshift3d.redshift4c4d.nodes.core.rscolorlayer.base_color_premult | maxon::Bool | Input | false | false | false |  |  | true | 
General/Layer 1/Blend Mode | <com.redshift3d.redshift4c4d.nodes.core.rscolorlayer.layer1_blend_mode | maxon::Int | Input | false | false | true |  |  | 0 | Normal = 0, Difference = 5, Average = 1, Add = 2, Subtract = 3, Multiply = 4, Darken = 7, Lighten = 6, Softlight = 10, Screen = 8, Hardlight = 9, Burn = 11, Dodge = 12, Overlay = 13, Exclusion = 14, Divide = 15
General/Layer 1/Color | <com.redshift3d.redshift4c4d.nodes.core.rscolorlayer.layer1_color | maxon::ColorA64 | Input | false | false | false |  |  | (0,0,0,1) | 
General/Layer 1/Color Has Premultiplied Alpha | <com.redshift3d.redshift4c4d.nodes.core.rscolorlayer.layer1_color_premult | maxon::Bool | Input | false | false | false |  |  | true | 
General/Layer 1/Enable | <com.redshift3d.redshift4c4d.nodes.core.rscolorlayer.layer1_enable | maxon::Bool | Input | false | false | false |  |  | true | 
General/Layer 1/Mask | <com.redshift3d.redshift4c4d.nodes.core.rscolorlayer.layer1_mask | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
General/Layer 1/Overlay Mode | <com.redshift3d.redshift4c4d.nodes.core.rscolorlayer.layer1_overlay_mode | maxon::Int | Input | false | false | true |  |  | 2 | Src = 0, Over = 2, Atop = 1, In = 3, Out = 4, Dest = 5, DestOver = 7, DestAtop = 6, DestIn = 8, DestOut = 9, Clear = 10, Xor = 11
General/Layer 2/Blend Mode | <com.redshift3d.redshift4c4d.nodes.core.rscolorlayer.layer2_blend_mode | maxon::Int | Input | false | false | true |  |  | 0 | Normal = 0, Difference = 5, Average = 1, Add = 2, Subtract = 3, Multiply = 4, Darken = 7, Lighten = 6, Softlight = 10, Screen = 8, Hardlight = 9, Burn = 11, Dodge = 12, Overlay = 13, Exclusion = 14, Divide = 15
General/Layer 2/Color | <com.redshift3d.redshift4c4d.nodes.core.rscolorlayer.layer2_color | maxon::ColorA64 | Input | false | false | false |  |  | (0,0,0,1) | 
General/Layer 2/Color Has Premultiplied Alpha | <com.redshift3d.redshift4c4d.nodes.core.rscolorlayer.layer2_color_premult | maxon::Bool | Input | false | false | false |  |  | true | 
General/Layer 2/Enable | <com.redshift3d.redshift4c4d.nodes.core.rscolorlayer.layer2_enable | maxon::Bool | Input | false | false | false |  |  | false | 
General/Layer 2/Mask | <com.redshift3d.redshift4c4d.nodes.core.rscolorlayer.layer2_mask | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
General/Layer 2/Overlay Mode | <com.redshift3d.redshift4c4d.nodes.core.rscolorlayer.layer2_overlay_mode | maxon::Int | Input | false | false | true |  |  | 2 | Src = 0, Over = 2, Atop = 1, In = 3, Out = 4, Dest = 5, DestOver = 7, DestAtop = 6, DestIn = 8, DestOut = 9, Clear = 10, Xor = 11
General/Layer 3/Blend Mode | <com.redshift3d.redshift4c4d.nodes.core.rscolorlayer.layer3_blend_mode | maxon::Int | Input | false | false | true |  |  | 0 | Normal = 0, Difference = 5, Average = 1, Add = 2, Subtract = 3, Multiply = 4, Darken = 7, Lighten = 6, Softlight = 10, Screen = 8, Hardlight = 9, Burn = 11, Dodge = 12, Overlay = 13, Exclusion = 14, Divide = 15
General/Layer 3/Color | <com.redshift3d.redshift4c4d.nodes.core.rscolorlayer.layer3_color | maxon::ColorA64 | Input | false | false | false |  |  | (0,0,0,1) | 
General/Layer 3/Color Has Premultiplied Alpha | <com.redshift3d.redshift4c4d.nodes.core.rscolorlayer.layer3_color_premult | maxon::Bool | Input | false | false | false |  |  | true | 
General/Layer 3/Enable | <com.redshift3d.redshift4c4d.nodes.core.rscolorlayer.layer3_enable | maxon::Bool | Input | false | false | false |  |  | false | 
General/Layer 3/Mask | <com.redshift3d.redshift4c4d.nodes.core.rscolorlayer.layer3_mask | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
General/Layer 3/Overlay Mode | <com.redshift3d.redshift4c4d.nodes.core.rscolorlayer.layer3_overlay_mode | maxon::Int | Input | false | false | true |  |  | 2 | Src = 0, Over = 2, Atop = 1, In = 3, Out = 4, Dest = 5, DestOver = 7, DestAtop = 6, DestIn = 8, DestOut = 9, Clear = 10, Xor = 11
General/Layer 4/Blend Mode | <com.redshift3d.redshift4c4d.nodes.core.rscolorlayer.layer4_blend_mode | maxon::Int | Input | false | false | true |  |  | 0 | Normal = 0, Difference = 5, Average = 1, Add = 2, Subtract = 3, Multiply = 4, Darken = 7, Lighten = 6, Softlight = 10, Screen = 8, Hardlight = 9, Burn = 11, Dodge = 12, Overlay = 13, Exclusion = 14, Divide = 15
General/Layer 4/Color | <com.redshift3d.redshift4c4d.nodes.core.rscolorlayer.layer4_color | maxon::ColorA64 | Input | false | false | false |  |  | (0,0,0,1) | 
General/Layer 4/Color Has Premultiplied Alpha | <com.redshift3d.redshift4c4d.nodes.core.rscolorlayer.layer4_color_premult | maxon::Bool | Input | false | false | false |  |  | true | 
General/Layer 4/Enable | <com.redshift3d.redshift4c4d.nodes.core.rscolorlayer.layer4_enable | maxon::Bool | Input | false | false | false |  |  | false | 
General/Layer 4/Mask | <com.redshift3d.redshift4c4d.nodes.core.rscolorlayer.layer4_mask | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
General/Layer 4/Overlay Mode | <com.redshift3d.redshift4c4d.nodes.core.rscolorlayer.layer4_overlay_mode | maxon::Int | Input | false | false | true |  |  | 2 | Src = 0, Over = 2, Atop = 1, In = 3, Out = 4, Dest = 5, DestOver = 7, DestAtop = 6, DestIn = 8, DestOut = 9, Clear = 10, Xor = 11
General/Layer 5/Blend Mode | <com.redshift3d.redshift4c4d.nodes.core.rscolorlayer.layer5_blend_mode | maxon::Int | Input | false | false | true |  |  | 0 | Normal = 0, Difference = 5, Average = 1, Add = 2, Subtract = 3, Multiply = 4, Darken = 7, Lighten = 6, Softlight = 10, Screen = 8, Hardlight = 9, Burn = 11, Dodge = 12, Overlay = 13, Exclusion = 14, Divide = 15
General/Layer 5/Color | <com.redshift3d.redshift4c4d.nodes.core.rscolorlayer.layer5_color | maxon::ColorA64 | Input | false | false | false |  |  | (0,0,0,1) | 
General/Layer 5/Color Has Premultiplied Alpha | <com.redshift3d.redshift4c4d.nodes.core.rscolorlayer.layer5_color_premult | maxon::Bool | Input | false | false | false |  |  | true | 
General/Layer 5/Enable | <com.redshift3d.redshift4c4d.nodes.core.rscolorlayer.layer5_enable | maxon::Bool | Input | false | false | false |  |  | false | 
General/Layer 5/Mask | <com.redshift3d.redshift4c4d.nodes.core.rscolorlayer.layer5_mask | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
General/Layer 5/Overlay Mode | <com.redshift3d.redshift4c4d.nodes.core.rscolorlayer.layer5_overlay_mode | maxon::Int | Input | false | false | true |  |  | 2 | Src = 0, Over = 2, Atop = 1, In = 3, Out = 4, Dest = 5, DestOver = 7, DestAtop = 6, DestIn = 8, DestOut = 9, Clear = 10, Xor = 11
General/Layer 6/Blend Mode | <com.redshift3d.redshift4c4d.nodes.core.rscolorlayer.layer6_blend_mode | maxon::Int | Input | false | false | true |  |  | 0 | Normal = 0, Difference = 5, Average = 1, Add = 2, Subtract = 3, Multiply = 4, Darken = 7, Lighten = 6, Softlight = 10, Screen = 8, Hardlight = 9, Burn = 11, Dodge = 12, Overlay = 13, Exclusion = 14, Divide = 15
General/Layer 6/Color | <com.redshift3d.redshift4c4d.nodes.core.rscolorlayer.layer6_color | maxon::ColorA64 | Input | false | false | false |  |  | (0,0,0,1) | 
General/Layer 6/Color Has Premultiplied Alpha | <com.redshift3d.redshift4c4d.nodes.core.rscolorlayer.layer6_color_premult | maxon::Bool | Input | false | false | false |  |  | true | 
General/Layer 6/Enable | <com.redshift3d.redshift4c4d.nodes.core.rscolorlayer.layer6_enable | maxon::Bool | Input | false | false | false |  |  | false | 
General/Layer 6/Mask | <com.redshift3d.redshift4c4d.nodes.core.rscolorlayer.layer6_mask | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
General/Layer 6/Overlay Mode | <com.redshift3d.redshift4c4d.nodes.core.rscolorlayer.layer6_overlay_mode | maxon::Int | Input | false | false | true |  |  | 2 | Src = 0, Over = 2, Atop = 1, In = 3, Out = 4, Dest = 5, DestOver = 7, DestAtop = 6, DestIn = 8, DestOut = 9, Clear = 10, Xor = 11
General/Layer 7/Blend Mode | <com.redshift3d.redshift4c4d.nodes.core.rscolorlayer.layer7_blend_mode | maxon::Int | Input | false | false | true |  |  | 0 | Normal = 0, Difference = 5, Average = 1, Add = 2, Subtract = 3, Multiply = 4, Darken = 7, Lighten = 6, Softlight = 10, Screen = 8, Hardlight = 9, Burn = 11, Dodge = 12, Overlay = 13, Exclusion = 14, Divide = 15
General/Layer 7/Color | <com.redshift3d.redshift4c4d.nodes.core.rscolorlayer.layer7_color | maxon::ColorA64 | Input | false | false | false |  |  | (0,0,0,1) | 
General/Layer 7/Color Has Premultiplied Alpha | <com.redshift3d.redshift4c4d.nodes.core.rscolorlayer.layer7_color_premult | maxon::Bool | Input | false | false | false |  |  | true | 
General/Layer 7/Enable | <com.redshift3d.redshift4c4d.nodes.core.rscolorlayer.layer7_enable | maxon::Bool | Input | false | false | false |  |  | false | 
General/Layer 7/Mask | <com.redshift3d.redshift4c4d.nodes.core.rscolorlayer.layer7_mask | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
General/Layer 7/Overlay Mode | <com.redshift3d.redshift4c4d.nodes.core.rscolorlayer.layer7_overlay_mode | maxon::Int | Input | false | false | true |  |  | 2 | Src = 0, Over = 2, Atop = 1, In = 3, Out = 4, Dest = 5, DestOver = 7, DestAtop = 6, DestIn = 8, DestOut = 9, Clear = 10, Xor = 11
Outputs/outColor | >com.redshift3d.redshift4c4d.nodes.core.rscolorlayer.outcolor | maxon::ColorA64 | Output | false | false | false |  |  | (0,0,0,1) | 

