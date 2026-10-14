# Node Template: Color Composite

- **Node Space ID:** `com.redshift3d.redshift4c4d.class.nodespace`
- **Template ID:** `com.redshift3d.redshift4c4d.nodes.core.rscolorcomposite`
- **Template Name:** `Color Composite`

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
General/Alpha Source | <com.redshift3d.redshift4c4d.nodes.core.rscolorcomposite.alpha_source | maxon::Int | Input | false | false | true |  |  | 0 | Composite = 0, Base Alpha = 2, Blend Alpha = 1
General/Base Color | <com.redshift3d.redshift4c4d.nodes.core.rscolorcomposite.base_color | maxon::ColorA64 | Input | false | false | false |  |  | (0,0,0,1) | 
General/Blend Color | <com.redshift3d.redshift4c4d.nodes.core.rscolorcomposite.blend_color | maxon::ColorA64 | Input | false | false | false |  |  | (0,0,0,1) | 
General/Composite Mode | <com.redshift3d.redshift4c4d.nodes.core.rscolorcomposite.comp_mode | maxon::Int | Input | false | false | true |  |  | 0 | Subtract = 4, Blend Color = 1, Base Color = 0, Difference = 6, Average = 2, Add = 3, Multiply = 5, Darken = 8, Lighten = 7, Mask = 17, Softlight = 11, Screen = 9, Hardlight = 10, Burn = 12, Dodge = 13, Overlay = 14, Exclusion = 15, Divide = 16, Stencil = 18, Matte = 19
Outputs/outColor | >com.redshift3d.redshift4c4d.nodes.core.rscolorcomposite.outcolor | maxon::ColorA64 | Output | false | false | false |  |  | (0,0,0,1) | 

