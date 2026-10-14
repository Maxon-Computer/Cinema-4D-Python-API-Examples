# Node Template: Physical Sky

- **Node Space ID:** `com.redshift3d.redshift4c4d.class.nodespace`
- **Template ID:** `com.redshift3d.redshift4c4d.nodes.core.physicalsky`
- **Template Name:** `Physical Sky`

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
Basic/Show Preview | net.maxon.node.base.displaypreview | maxon::Bool | Attribute | false | false | false |  |  | false | 
Filter Tags | net.maxon.node.base.filtertags | maxon::CString | Attribute | false | false | false |  |  |  | 
Node Category | net.maxon.node.base.category | maxon::InternedId | Attribute | false | false | true |  |  | operators | operators = operators, distributions = distributions, geometries = geometries, patterns = patterns, primitives = primitives, effectors = effectors, fields = fields, functions = functions, structures = structures, geomodifiers = geomodifiers, geogenerators = geogenerators
Preview/Node | net.maxon.node.base.nodepreviewimage | maxon::ImageBaseRef | Attribute | false | false | false |  |  |  | 
Inputs/Atmosphere/Ground Color | <com.redshift3d.redshift4c4d.nodes.core.physicalsky.ground_color | maxon::Color64 | Input | false | false | false |  |  | (0.2,0.2,0.2) | 
Inputs/Atmosphere/Horizon Blur | <com.redshift3d.redshift4c4d.nodes.core.physicalsky.horizon_blur | maxon::Float | Input | false | false | false |  |  | 0.1 | 
Inputs/Atmosphere/Horizon Height | <com.redshift3d.redshift4c4d.nodes.core.physicalsky.horizon_height | maxon::Float | Input | false | false | false |  |  | 0 | 
Inputs/Atmosphere/Night Color | <com.redshift3d.redshift4c4d.nodes.core.physicalsky.night_color | maxon::Color64 | Input | false | false | false |  |  | (0,0,0) | 
Inputs/Atmosphere/Ozone | <com.redshift3d.redshift4c4d.nodes.core.physicalsky.ozone | maxon::Float | Input | false | false | false | 0 | 1 | 0.35 | 
Inputs/Atmosphere/Turbidity | <com.redshift3d.redshift4c4d.nodes.core.physicalsky.haze | maxon::Float | Input | false | false | false |  |  | 2 | 
Inputs/Color Adjustment/Red-Blue Shift | <com.redshift3d.redshift4c4d.nodes.core.physicalsky.redblueshift | maxon::Float | Input | false | false | false |  |  | 0 | 
Inputs/Color Adjustment/Saturation | <com.redshift3d.redshift4c4d.nodes.core.physicalsky.saturation | maxon::Float | Input | false | false | false |  |  | 1 | 
Inputs/Color Adjustment/Saturation Affects Color Adjustments | <com.redshift3d.redshift4c4d.nodes.core.physicalsky.saturation_affects_color_adjustments | maxon::Bool | Input | false | false | false |  |  | true | 
Inputs/Diffuse_horizontal_illuminance | <com.redshift3d.redshift4c4d.nodes.core.physicalsky.diffuse_horizontal_illuminance | maxon::Float | Input | false | false | false |  |  | 0 | 
Inputs/Flags | <com.redshift3d.redshift4c4d.nodes.core.physicalsky.flags | maxon::Int | Input | false | false | false |  |  | 0 | 
Inputs/General/Intensity Multiplier | <com.redshift3d.redshift4c4d.nodes.core.physicalsky.multiplier | maxon::Float | Input | false | false | false |  |  | 1 | 
Inputs/General/Model | <com.redshift3d.redshift4c4d.nodes.core.physicalsky.model | maxon::Int | Input | false | false | true |  |  | 2 | Hosek-Wilkie = 0, Preetham et al = 1, PRG Clear Sky = 2
Inputs/General/Normalization Mode | <com.redshift3d.redshift4c4d.nodes.core.physicalsky.normalization_mode | maxon::Int | Input | false | false | true |  |  | 2 | None = 0, Lighting = 1, Disk+Lighting = 2
Inputs/General/On | <com.redshift3d.redshift4c4d.nodes.core.physicalsky.on | maxon::Bool | Input | false | false | false |  |  | true | 
Inputs/General/RGB Unit Conversion | <com.redshift3d.redshift4c4d.nodes.core.physicalsky.rgb_unit_conversion | maxon::Color64 | Input | false | false | false |  |  | (0.318,0.318,0.318) | 
Inputs/General/Use Non-Physical Intensity | <com.redshift3d.redshift4c4d.nodes.core.physicalsky.usenonphysicalintensity | maxon::Bool | Input | false | false | false |  |  | false | 
Inputs/Mia_compatibility | <com.redshift3d.redshift4c4d.nodes.core.physicalsky.mia_compatibility | maxon::Bool | Input | false | false | false |  |  | false | 
Inputs/Overrides/Force Alpha To Zero | <com.redshift3d.redshift4c4d.nodes.core.physicalsky.forcealphatozero | maxon::Bool | Input | false | false | false |  |  | false | 
Inputs/Overrides/Ray Type Enable/Background | <com.redshift3d.redshift4c4d.nodes.core.physicalsky.background_enable | maxon::Bool | Input | false | false | false |  |  | true | 
Inputs/Overrides/Ray Type Enable/GI | <com.redshift3d.redshift4c4d.nodes.core.physicalsky.gi_enable | maxon::Bool | Input | false | false | false |  |  | true | 
Inputs/Overrides/Ray Type Enable/GI Intensity | <com.redshift3d.redshift4c4d.nodes.core.physicalsky.gi_intensity | maxon::Float | Input | false | false | false |  |  | 1 | 
Inputs/Overrides/Ray Type Enable/Reflection | <com.redshift3d.redshift4c4d.nodes.core.physicalsky.reflection_enable | maxon::Bool | Input | false | false | false |  |  | true | 
Inputs/Overrides/Ray Type Enable/Reflection Intensity | <com.redshift3d.redshift4c4d.nodes.core.physicalsky.reflection_intensity | maxon::Float | Input | false | false | false |  |  | 1 | 
Inputs/Overrides/Ray Type Enable/Refraction | <com.redshift3d.redshift4c4d.nodes.core.physicalsky.refraction_enable | maxon::Bool | Input | false | false | false |  |  | true | 
Inputs/Overrides/Ray Type Enable/Refraction Intensity | <com.redshift3d.redshift4c4d.nodes.core.physicalsky.refraction_intensity | maxon::Float | Input | false | false | false |  |  | 1 | 
Inputs/Perez_a | <com.redshift3d.redshift4c4d.nodes.core.physicalsky.perez_a | maxon::Float | Input | false | false | false |  |  | 0 | 
Inputs/Perez_b | <com.redshift3d.redshift4c4d.nodes.core.physicalsky.perez_b | maxon::Float | Input | false | false | false |  |  | 0 | 
Inputs/Perez_c | <com.redshift3d.redshift4c4d.nodes.core.physicalsky.perez_c | maxon::Float | Input | false | false | false |  |  | 0 | 
Inputs/Perez_d | <com.redshift3d.redshift4c4d.nodes.core.physicalsky.perez_d | maxon::Float | Input | false | false | false |  |  | 0 | 
Inputs/Perez_e | <com.redshift3d.redshift4c4d.nodes.core.physicalsky.perez_e | maxon::Float | Input | false | false | false |  |  | 0 | 
Inputs/Sky_luminance_mode | <com.redshift3d.redshift4c4d.nodes.core.physicalsky.sky_luminance_mode | maxon::Int | Input | false | false | false |  |  | 0 | 
Inputs/Sun/Sun | <com.redshift3d.redshift4c4d.nodes.core.physicalsky.sun | maxon::Uuid | Input | false | false | false |  |  |  | 
Inputs/Sun/Sun Direction | <com.redshift3d.redshift4c4d.nodes.core.physicalsky.sun_direction | maxon::Vector64 | Input | false | false | false |  |  | (0,1,0) | 
Inputs/Sun/Sun Disk Intensity | <com.redshift3d.redshift4c4d.nodes.core.physicalsky.sun_disk_intensity | maxon::Float | Input | false | false | false |  |  | 1 | 
Inputs/Sun/Sun Disk Scale | <com.redshift3d.redshift4c4d.nodes.core.physicalsky.sun_disk_scale | maxon::Float | Input | false | false | false |  |  | 1 | 
Inputs/Sun/Sun Glow Intensity | <com.redshift3d.redshift4c4d.nodes.core.physicalsky.sun_glow_intensity | maxon::Float | Input | false | false | false |  |  | 1 | 
Inputs/Sun/Sun Tint | <com.redshift3d.redshift4c4d.nodes.core.physicalsky.sun_tint | maxon::Color64 | Input | false | false | false |  |  | (1,1,1) | 
Inputs/Use_background | <com.redshift3d.redshift4c4d.nodes.core.physicalsky.use_background | maxon::Bool | Input | false | false | false |  |  | false | 
Inputs/Visibility_distance | <com.redshift3d.redshift4c4d.nodes.core.physicalsky.visibility_distance | maxon::Float | Input | false | false | false |  |  | 1 | 
Inputs/Y_is_up | <com.redshift3d.redshift4c4d.nodes.core.physicalsky.y_is_up | maxon::Bool | Input | false | false | false |  |  | true | 
Inputs/Zenith_luminance | <com.redshift3d.redshift4c4d.nodes.core.physicalsky.zenith_luminance | maxon::Float | Input | false | false | false |  |  | 0 | 
Outputs/outColor | >com.redshift3d.redshift4c4d.nodes.core.physicalsky.outcolor | maxon::ColorA64 | Output | false | false | false |  |  | (0,0,0,1) | 

