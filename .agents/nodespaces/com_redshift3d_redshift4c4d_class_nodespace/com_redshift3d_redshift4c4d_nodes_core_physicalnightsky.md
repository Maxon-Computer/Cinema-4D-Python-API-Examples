# Node Template: Physical Night Sky

- **Node Space ID:** `com.redshift3d.redshift4c4d.class.nodespace`
- **Template ID:** `com.redshift3d.redshift4c4d.nodes.core.physicalnightsky`
- **Template Name:** `Physical Night Sky`

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
Node Category | net.maxon.node.base.category | maxon::InternedId | Attribute | false | false | true |  |  | operators | operators = operators, distributions = distributions, geometries = geometries, patterns = patterns, primitives = primitives, effectors = effectors, fields = fields, functions = functions, structures = structures, geomodifiers = geomodifiers, geogenerators = geogenerators
Preview/Node | net.maxon.node.base.nodepreviewimage | maxon::ImageBaseRef | Attribute | false | false | false |  |  |  | 
Inputs/Atmosphere/Horizon Height | <com.redshift3d.redshift4c4d.nodes.core.physicalnightsky.horizon_height | maxon::Float | Input | false | false | false |  |  | 0 | 
Inputs/Atmosphere/Ozone | <com.redshift3d.redshift4c4d.nodes.core.physicalnightsky.ozone | maxon::Float | Input | false | false | false | 0 | 1 | 0.35 | 
Inputs/Atmosphere/Turbidity | <com.redshift3d.redshift4c4d.nodes.core.physicalnightsky.haze | maxon::Float | Input | false | false | false |  |  | 2 | 
Inputs/Color Adjustment/Red-Blue Shift | <com.redshift3d.redshift4c4d.nodes.core.physicalnightsky.redblueshift | maxon::Float | Input | false | false | false |  |  | 0 | 
Inputs/Color Adjustment/Saturation | <com.redshift3d.redshift4c4d.nodes.core.physicalnightsky.saturation | maxon::Float | Input | false | false | false |  |  | 1 | 
Inputs/Color Adjustment/Saturation Affects Color Adjustments | <com.redshift3d.redshift4c4d.nodes.core.physicalnightsky.saturation_affects_color_adjustments | maxon::Bool | Input | false | false | false |  |  | true | 
Inputs/Fade_with_sun_position | <com.redshift3d.redshift4c4d.nodes.core.physicalnightsky.fade_with_sun_position | maxon::Bool | Input | false | false | false |  |  | false | 
Inputs/General/Intensity Multiplier | <com.redshift3d.redshift4c4d.nodes.core.physicalnightsky.multiplier | maxon::Float | Input | false | false | false |  |  | 1 | 
Inputs/General/Model | <com.redshift3d.redshift4c4d.nodes.core.physicalnightsky.model | maxon::Int | Input | false | false | true |  |  | 2 | Hosek-Wilkie = 0, Preetham et al = 1, PRG Clear Sky = 2
Inputs/General/Normalization Mode | <com.redshift3d.redshift4c4d.nodes.core.physicalnightsky.normalization_mode | maxon::Int | Input | false | false | true |  |  | 2 | None = 0, Lighting = 1, Disk+Lighting = 2
Inputs/General/On | <com.redshift3d.redshift4c4d.nodes.core.physicalnightsky.on | maxon::Bool | Input | false | false | false |  |  | true | 
Inputs/General/RGB Unit Conversion | <com.redshift3d.redshift4c4d.nodes.core.physicalnightsky.rgb_unit_conversion | maxon::Color64 | Input | false | false | false |  |  | (0.318,0.318,0.318) | 
Inputs/General/Use Non-Physical Intensity | <com.redshift3d.redshift4c4d.nodes.core.physicalnightsky.usenonphysicalintensity | maxon::Bool | Input | false | false | false |  |  | false | 
Inputs/Latitude | <com.redshift3d.redshift4c4d.nodes.core.physicalnightsky.latitude | maxon::Float | Input | false | false | false |  |  | 0 | 
Inputs/Local_sidereal_time | <com.redshift3d.redshift4c4d.nodes.core.physicalnightsky.local_sidereal_time | maxon::Float | Input | false | false | false |  |  | 0 | 
Inputs/Mia_compatibility | <com.redshift3d.redshift4c4d.nodes.core.physicalnightsky.mia_compatibility | maxon::Bool | Input | false | false | false |  |  | false | 
Inputs/Milkyway_intensity | <com.redshift3d.redshift4c4d.nodes.core.physicalnightsky.milkyway_intensity | maxon::Float | Input | false | false | false |  |  | 1 | 
Inputs/Moon_direction | <com.redshift3d.redshift4c4d.nodes.core.physicalnightsky.moon_direction | maxon::Vector64 | Input | false | false | false |  |  | (0,1,0) | 
Inputs/Moon_distance | <com.redshift3d.redshift4c4d.nodes.core.physicalnightsky.moon_distance | maxon::Float | Input | false | false | false |  |  | 384400 | 
Inputs/Moon_enable | <com.redshift3d.redshift4c4d.nodes.core.physicalnightsky.moon_enable | maxon::Bool | Input | false | false | false |  |  | false | 
Inputs/Moon_intensity | <com.redshift3d.redshift4c4d.nodes.core.physicalnightsky.moon_intensity | maxon::Float | Input | false | false | false |  |  | 1 | 
Inputs/Moon_radius | <com.redshift3d.redshift4c4d.nodes.core.physicalnightsky.moon_radius | maxon::Float | Input | false | false | false |  |  | 1 | 
Inputs/Moon_tint | <com.redshift3d.redshift4c4d.nodes.core.physicalnightsky.moon_tint | maxon::Color64 | Input | false | false | false |  |  | (1,1,1) | 
Inputs/North_offset | <com.redshift3d.redshift4c4d.nodes.core.physicalnightsky.north_offset | maxon::Float | Input | false | false | false |  |  | 0 | 
Inputs/Overrides/Force Alpha To Zero | <com.redshift3d.redshift4c4d.nodes.core.physicalnightsky.forcealphatozero | maxon::Bool | Input | false | false | false |  |  | false | 
Inputs/Overrides/Ray Type Enable/Background | <com.redshift3d.redshift4c4d.nodes.core.physicalnightsky.background_enable | maxon::Bool | Input | false | false | false |  |  | true | 
Inputs/Overrides/Ray Type Enable/GI | <com.redshift3d.redshift4c4d.nodes.core.physicalnightsky.gi_enable | maxon::Bool | Input | false | false | false |  |  | true | 
Inputs/Overrides/Ray Type Enable/GI Intensity | <com.redshift3d.redshift4c4d.nodes.core.physicalnightsky.gi_intensity | maxon::Float | Input | false | false | false |  |  | 1 | 
Inputs/Overrides/Ray Type Enable/Reflection | <com.redshift3d.redshift4c4d.nodes.core.physicalnightsky.reflection_enable | maxon::Bool | Input | false | false | false |  |  | true | 
Inputs/Overrides/Ray Type Enable/Reflection Intensity | <com.redshift3d.redshift4c4d.nodes.core.physicalnightsky.reflection_intensity | maxon::Float | Input | false | false | false |  |  | 1 | 
Inputs/Overrides/Ray Type Enable/Refraction | <com.redshift3d.redshift4c4d.nodes.core.physicalnightsky.refraction_enable | maxon::Bool | Input | false | false | false |  |  | true | 
Inputs/Overrides/Ray Type Enable/Refraction Intensity | <com.redshift3d.redshift4c4d.nodes.core.physicalnightsky.refraction_intensity | maxon::Float | Input | false | false | false |  |  | 1 | 
Inputs/Star_intensity | <com.redshift3d.redshift4c4d.nodes.core.physicalnightsky.star_intensity | maxon::Float | Input | false | false | false |  |  | 1 | 
Inputs/Stars_enable | <com.redshift3d.redshift4c4d.nodes.core.physicalnightsky.stars_enable | maxon::Bool | Input | false | false | false |  |  | false | 
Inputs/Sun/Sun | <com.redshift3d.redshift4c4d.nodes.core.physicalnightsky.sun | maxon::Uuid | Input | false | false | false |  |  |  | 
Inputs/Sun/Sun Direction | <com.redshift3d.redshift4c4d.nodes.core.physicalnightsky.sun_direction | maxon::Vector64 | Input | false | false | false |  |  | (0,1,0) | 
Inputs/Sun/Sun Disk Intensity | <com.redshift3d.redshift4c4d.nodes.core.physicalnightsky.sun_disk_intensity | maxon::Float | Input | false | false | false |  |  | 1 | 
Inputs/Sun/Sun Disk Scale | <com.redshift3d.redshift4c4d.nodes.core.physicalnightsky.sun_disk_scale | maxon::Float | Input | false | false | false |  |  | 1 | 
Inputs/Sun/Sun Tint | <com.redshift3d.redshift4c4d.nodes.core.physicalnightsky.sun_tint | maxon::Color64 | Input | false | false | false |  |  | (1,1,1) | 
Inputs/Y_is_up | <com.redshift3d.redshift4c4d.nodes.core.physicalnightsky.y_is_up | maxon::Bool | Input | false | false | false |  |  | true | 
Outputs/outColor | >com.redshift3d.redshift4c4d.nodes.core.physicalnightsky.outcolor | maxon::ColorA64 | Output | false | false | false |  |  | (0,0,0,1) | 

