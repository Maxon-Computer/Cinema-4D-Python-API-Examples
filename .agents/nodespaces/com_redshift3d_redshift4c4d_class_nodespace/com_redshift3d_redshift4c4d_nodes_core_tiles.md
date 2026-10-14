# Node Template: Tiles

- **Node Space ID:** `com.redshift3d.redshift4c4d.class.nodespace`
- **Template ID:** `com.redshift3d.redshift4c4d.nodes.core.tiles`
- **Template Name:** `Tiles`

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
Node Category | net.maxon.node.base.category | maxon::InternedId | Attribute | false | false | true |  |  | patterns | operators = operators, distributions = distributions, geometries = geometries, patterns = patterns, primitives = primitives, effectors = effectors, fields = fields, functions = functions, structures = structures, geomodifiers = geomodifiers, geogenerators = geogenerators
Preview/Node | net.maxon.node.base.nodepreviewimage | maxon::ImageBaseRef | Attribute | false | false | false |  |  |  | 
Shader/Color/Grout Color | <com.redshift3d.redshift4c4d.nodes.core.tiles.ingroutcolor | maxon::Color64 | Input | false | false | false |  |  | (0,0,0) | 
Shader/Color/Randomize Color | <com.redshift3d.redshift4c4d.nodes.core.tiles.inrandomizecolor | maxon::Bool | Input | false | false | false |  |  | false | 
Shader/Color/Tiles Color 1 | <com.redshift3d.redshift4c4d.nodes.core.tiles.intilescolor1 | maxon::Color64 | Input | false | false | false |  |  | (0.502,0,0) | 
Shader/Color/Tiles Color 2 | <com.redshift3d.redshift4c4d.nodes.core.tiles.intilescolor2 | maxon::Color64 | Input | false | false | false |  |  | (0.502,0.502,0.502) | 
Shader/Color/Tiles Color 3 | <com.redshift3d.redshift4c4d.nodes.core.tiles.intilescolor3 | maxon::Color64 | Input | false | false | false |  |  | (0,0,0.502) | 
Shader/Noise/Seed | <com.redshift3d.redshift4c4d.nodes.core.tiles.innoiseseed | maxon::Int | Input | false | false | false |  |  | 123 | 
Shader/Pattern/Bevel Width | <com.redshift3d.redshift4c4d.nodes.core.tiles.inbevelwidth | maxon::Float | Input | false | false | false | 0 | 1 | 0.3 | 
Shader/Pattern/Global Scale | <com.redshift3d.redshift4c4d.nodes.core.tiles.inglobalscale | maxon::Float | Input | false | false | false | 0 | 2147483648 | 1 | 
Shader/Pattern/Grout Width | <com.redshift3d.redshift4c4d.nodes.core.tiles.ingroutwidth | maxon::Float | Input | false | false | false | 0 | 1 | 0.05 | 
Shader/Pattern/Orientation | <com.redshift3d.redshift4c4d.nodes.core.tiles.inorientation | maxon::Int | Input | false | false | true |  |  | 0 | U = 0, V = 1
Shader/Pattern/Pattern | <com.redshift3d.redshift4c4d.nodes.core.tiles.inpattern | maxon::Int | Input | false | false | true |  |  | 21 | Weave = 27, Spiral 1 = 19, Random = 12, Spiral 2 = 20, Radial Lines 1 = 10, Lines 1 = 6, Sawtooth 1 = 15, Radial Lines 2 = 11, Lines 2 = 7, Planks = 9, Sawtooth 2 = 16, Brick 1 = 0, Brick 2 = 1, Hexagons = 5, Rings 1 = 13, Circles 1 = 2, Parquet = 8, Rings 2 = 14, Circles 2 = 3, Squares = 21, Circles 3 = 4, Scales 1 = 17, Scales 2 = 18, Triangles 1 = 22, Triangles 2 = 23, Triangles 3 = 24, Waves 1 = 25, Waves 2 = 26
Shader/Pattern/Radial Scale | <com.redshift3d.redshift4c4d.nodes.core.tiles.inradialscale | maxon::Float | Input | false | false | false | 0 | 2147483648 | 1 | 
Shader/Pattern/Rotate | <com.redshift3d.redshift4c4d.nodes.core.tiles.inrotate | maxon::Float | Input | false | false | false | -2147483648 | 2147483648 | 0 | 
Shader/Pattern/Smooth Bevel | <com.redshift3d.redshift4c4d.nodes.core.tiles.inbevel | maxon::Bool | Input | false | false | false |  |  | true | 
Shader/Pattern/U Scale | <com.redshift3d.redshift4c4d.nodes.core.tiles.inuscale | maxon::Float | Input | false | false | false | 0 | 2147483648 | 1 | 
Shader/Pattern/V Scale | <com.redshift3d.redshift4c4d.nodes.core.tiles.invscale | maxon::Float | Input | false | false | false | 0 | 2147483648 | 1 | 
Shader/UV Channel | <com.redshift3d.redshift4c4d.nodes.core.tiles.tspace_id | maxon::String | Input | false | false | false |  |  |  | 
Shader/UV Context | <com.redshift3d.redshift4c4d.nodes.core.tiles.uv_context | RSC4D::UVContext | Input | false | false | false |  |  |  | 
Outputs/outColor | >com.redshift3d.redshift4c4d.nodes.core.tiles.outcolor | maxon::Color64 | Output | false | false | false |  |  | (0,0,0) | 

