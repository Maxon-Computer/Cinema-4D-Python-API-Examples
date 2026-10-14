# Node Template: UV Context Projection

- **Node Space ID:** `com.redshift3d.redshift4c4d.class.nodespace`
- **Template ID:** `com.redshift3d.redshift4c4d.nodes.core.uvcontextprojection`
- **Template Name:** `UV Context Projection`

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
Node Category | net.maxon.node.base.category | maxon::InternedId | Attribute | false | false | true |  |  | fields | distributions = distributions, operators = operators, geometries = geometries, patterns = patterns, primitives = primitives, effectors = effectors, fields = fields, functions = functions, structures = structures, geomodifiers = geomodifiers, geogenerators = geogenerators
Preview/Node | net.maxon.node.base.nodepreviewimage | maxon::ImageBaseRef | Attribute | false | false | false |  |  |  | 
General/IsLeftHanded | <com.redshift3d.redshift4c4d.nodes.core.uvcontextprojection.islefthanded | maxon::Bool | Input | false | false | false |  |  | true | 
General/UV Source/Coordinates/Film Aspect | <com.redshift3d.redshift4c4d.nodes.core.uvcontextprojection.camera_film_aspect | maxon::Float | Input | false | false | false | 0 | 32 | 1.778 | 
General/UV Source/Coordinates/Object Picker | <com.redshift3d.redshift4c4d.nodes.core.uvcontextprojection.coord_object_id | maxon::Uuid | Input | false | false | false |  |  |  | 
General/UV Source/Coordinates/Physical Size | <com.redshift3d.redshift4c4d.nodes.core.uvcontextprojection.coord_physical_size | maxon::Bool | Input | false | false | false |  |  | true | 
General/UV Source/Coordinates/Pixel Aspect | <com.redshift3d.redshift4c4d.nodes.core.uvcontextprojection.camera_pixel_aspect | maxon::Float | Input | false | false | false | 0 | 32 | 1 | 
General/UV Source/Coordinates/Position | <com.redshift3d.redshift4c4d.nodes.core.uvcontextprojection.coord_offset | maxon::Vector64 | Input | false | false | false |  |  | (0,0,0) | 
General/UV Source/Coordinates/Rotation | <com.redshift3d.redshift4c4d.nodes.core.uvcontextprojection.coord_rotate | maxon::Vector64 | Input | false | false | false |  |  | (0,0,0) | 
General/UV Source/Coordinates/Size X | <com.redshift3d.redshift4c4d.nodes.core.uvcontextprojection.coord_size_x | maxon::Float | Input | false | false | false | 0 | 2147483648 | 200 | 
General/UV Source/Coordinates/Size Y | <com.redshift3d.redshift4c4d.nodes.core.uvcontextprojection.coord_size_y | maxon::Float | Input | false | false | false | 0 | 2147483648 | 200 | 
General/UV Source/Coordinates/Size Z | <com.redshift3d.redshift4c4d.nodes.core.uvcontextprojection.coord_size_z | maxon::Float | Input | false | false | false | 0 | 2147483648 | 200 | 
General/UV Source/Coordinates/Transform Source | <com.redshift3d.redshift4c4d.nodes.core.uvcontextprojection.coord_source | maxon::Int | Input | false | false | true |  |  | 0 | Shader = 0, Object = 1
General/UV Source/Coordinates/Uniform Size | <com.redshift3d.redshift4c4d.nodes.core.uvcontextprojection.coord_uniform_size | maxon::Bool | Input | false | false | false |  |  | true | 
General/UV Source/Projection | <com.redshift3d.redshift4c4d.nodes.core.uvcontextprojection.proj_type | maxon::Int | Input | false | false | true |  |  | 0 | Passthrough = 0, UV Channel = 1, Spatial = 7, Tri-Planar = 2, Cubic = 3, Spherical = 4, Cylindrical = 5, Flat = 6, Shrinkwrap = 8, Camera = 9
General/UV Source/Projection Space | <com.redshift3d.redshift4c4d.nodes.core.uvcontextprojection.proj_space | maxon::Int | Input | false | false | true |  |  | 2 | World = 0, Object = 1, Reference Object = 2
General/UV Source/Tri-Planar/Axis Blend | <com.redshift3d.redshift4c4d.nodes.core.uvcontextprojection.tp_blend_amount | maxon::Float | Input | false | false | false | 0 | 1 | 0.5 | 
General/UV Source/Tri-Planar/Axis Rotate | <com.redshift3d.redshift4c4d.nodes.core.uvcontextprojection.tp_axis_rotate | maxon::Vector64 | Input | false | false | false | (-360,-360,-360) | (360,360,360) | (0,0,0) | 
General/UV Source/Tri-Planar/Blend Curve | <com.redshift3d.redshift4c4d.nodes.core.uvcontextprojection.tp_blend_curve | maxon::Float | Input | false | false | false | 1 | 100 | 10 | 
General/UV Source/Tri-Planar/Blend Noise | <com.redshift3d.redshift4c4d.nodes.core.uvcontextprojection.tp_blend_noise | maxon::Float | Input | false | false | false | 0 | 100 | 5 | 
General/UV Source/Tri-Planar/Noise Scale | <com.redshift3d.redshift4c4d.nodes.core.uvcontextprojection.tp_noise_scale | maxon::Float | Input | false | false | false | 0.1 | 100 | 1 | 
General/UV Source/UV Channel | <com.redshift3d.redshift4c4d.nodes.core.uvcontextprojection.tspace_id | maxon::String | Input | false | false | false |  |  |  | 
General/UV Transform/Blend Curve | <com.redshift3d.redshift4c4d.nodes.core.uvcontextprojection.hex_blend_curve | maxon::Float | Input | false | false | false | 0 | 1 | 0.5 | 
General/UV Transform/Blend Noise | <com.redshift3d.redshift4c4d.nodes.core.uvcontextprojection.hex_blend_noise | maxon::Float | Input | false | false | false | 0 | 1 | 0.2 | 
General/UV Transform/Flip U | <com.redshift3d.redshift4c4d.nodes.core.uvcontextprojection.flip_u | maxon::Bool | Input | false | false | false |  |  | false | 
General/UV Transform/Flip V | <com.redshift3d.redshift4c4d.nodes.core.uvcontextprojection.flip_v | maxon::Bool | Input | false | false | false |  |  | false | 
General/UV Transform/Noise Scale | <com.redshift3d.redshift4c4d.nodes.core.uvcontextprojection.hex_noise_scale | maxon::Float | Input | false | false | false | 0 | 1 | 0.5 | 
General/UV Transform/Offset | <com.redshift3d.redshift4c4d.nodes.core.uvcontextprojection.uv_offset | maxon::Vector2d64 | Input | false | false | false |  |  | (0,0) | 
General/UV Transform/Pivot | <com.redshift3d.redshift4c4d.nodes.core.uvcontextprojection.uv_pivot | maxon::Vector2d64 | Input | false | false | false |  |  | (0.5,0.5) | 
General/UV Transform/Random Flip | <com.redshift3d.redshift4c4d.nodes.core.uvcontextprojection.hex_random_flip | maxon::Bool | Input | false | false | false |  |  | false | 
General/UV Transform/Random Offset | <com.redshift3d.redshift4c4d.nodes.core.uvcontextprojection.hex_random_offset | maxon::Float | Input | false | false | false |  |  | 1 | 
General/UV Transform/Random Rotate | <com.redshift3d.redshift4c4d.nodes.core.uvcontextprojection.hex_random_rotate | maxon::Float | Input | false | false | false | 0 | 360 | 20 | 
General/UV Transform/Random Scale | <com.redshift3d.redshift4c4d.nodes.core.uvcontextprojection.hex_random_scale | maxon::Float | Input | false | false | false | 0 | 32 | 0 | 
General/UV Transform/Random Seed | <com.redshift3d.redshift4c4d.nodes.core.uvcontextprojection.hex_random_seed | maxon::Int | Input | false | false | false | 0 | 1000 | 123 | 
General/UV Transform/Rotate | <com.redshift3d.redshift4c4d.nodes.core.uvcontextprojection.uv_rotate | maxon::Float | Input | false | false | false | -360 | 360 | 0 | 
General/UV Transform/Rotate Mode | <com.redshift3d.redshift4c4d.nodes.core.uvcontextprojection.hex_random_rotate_mode | maxon::Int | Input | false | false | true |  |  | 0 | Range = 0, Stepped = 1
General/UV Transform/Scale | <com.redshift3d.redshift4c4d.nodes.core.uvcontextprojection.hex_uniform_scale | maxon::Float | Input | false | false | false | 0 | 8 | 1 | 
General/UV Transform/Tile Blend | <com.redshift3d.redshift4c4d.nodes.core.uvcontextprojection.hex_tile_blend | maxon::Float | Input | false | false | false | 0 | 1 | 0.5 | 
General/UV Transform/Tiles U | <com.redshift3d.redshift4c4d.nodes.core.uvcontextprojection.uv_tiles_u | maxon::Float | Input | false | false | false | 0 | 65536 | 1 | 
General/UV Transform/Tiles V | <com.redshift3d.redshift4c4d.nodes.core.uvcontextprojection.uv_tiles_v | maxon::Float | Input | false | false | false | 0 | 65536 | 1 | 
General/UV Transform/Tiling | <com.redshift3d.redshift4c4d.nodes.core.uvcontextprojection.uv_tiling | maxon::Int | Input | false | false | true |  |  | 0 | Square = 0, Hex = 1
General/UV Transform/Uniform Tiles | <com.redshift3d.redshift4c4d.nodes.core.uvcontextprojection.uv_uniform_tiles | maxon::Bool | Input | false | false | false |  |  | true | 
General/UV Transform/Wrap U | <com.redshift3d.redshift4c4d.nodes.core.uvcontextprojection.wrap_u | maxon::Int | Input | false | false | true |  |  | 0 | Repeat = 0, Mirror = 1, Clip = 2
General/UV Transform/Wrap V | <com.redshift3d.redshift4c4d.nodes.core.uvcontextprojection.wrap_v | maxon::Int | Input | false | false | true |  |  | 0 | Repeat = 0, Mirror = 1, Clip = 2
General/YIsUp | <com.redshift3d.redshift4c4d.nodes.core.uvcontextprojection.yisup | maxon::Bool | Input | false | false | false |  |  | true | 
Outputs/outContext | >com.redshift3d.redshift4c4d.nodes.core.uvcontextprojection.outcontext | RSC4D::UVContext | Output | false | false | false |  |  |  | 

