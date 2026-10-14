# Node Template: Contour

- **Node Space ID:** `com.redshift3d.redshift4c4d.class.nodespace`
- **Template ID:** `com.redshift3d.redshift4c4d.nodes.core.contour`
- **Template Name:** `Contour`

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
Node Category | net.maxon.node.base.category | maxon::InternedId | Attribute | false | false | true |  |  | structures | distributions = distributions, operators = operators, geometries = geometries, patterns = patterns, primitives = primitives, effectors = effectors, fields = fields, functions = functions, structures = structures, geomodifiers = geomodifiers, geogenerators = geogenerators
Preview/Node | net.maxon.node.base.nodepreviewimage | maxon::ImageBaseRef | Attribute | false | false | false |  |  |  | 
Advanced/Alpha Mask/Custom Time | <com.redshift3d.redshift4c4d.nodes.core.contour.alphamaskanimationtime | maxon::Float | Input | false | false | false |  |  | 0 | 
Advanced/Alpha Mask/Enable | <com.redshift3d.redshift4c4d.nodes.core.contour.alphamaskenable | maxon::Bool | Input | false | false | false |  |  | false | 
Advanced/Alpha Mask/Loop Period | <com.redshift3d.redshift4c4d.nodes.core.contour.alphamaskanimationloopperiod | maxon::Float | Input | false | false | false |  |  | 0 | 
Advanced/Alpha Mask/Mode | <com.redshift3d.redshift4c4d.nodes.core.contour.alphamaskmode | maxon::Int | Input | false | false | true |  |  | 0 | Pencil = 0, Fountain Pen = 1
Advanced/Alpha Mask/Rotation | <com.redshift3d.redshift4c4d.nodes.core.contour.alphamaskrotation | maxon::Float | Input | false | false | false | 0 | 360 | 0 | 
Advanced/Alpha Mask/Scale | <com.redshift3d.redshift4c4d.nodes.core.contour.alphamaskscale | maxon::Float | Input | false | false | false |  |  | 1 | 
Advanced/Alpha Mask/Seed | <com.redshift3d.redshift4c4d.nodes.core.contour.seed | maxon::Int | Input | false | false | false | -2147483647 | 2147483646 | 123 | 
Advanced/Alpha Mask/Speed | <com.redshift3d.redshift4c4d.nodes.core.contour.alphamaskanimationspeed | maxon::Float | Input | false | false | false |  |  | 0 | 
Advanced/Alpha Mask/Time Source | <com.redshift3d.redshift4c4d.nodes.core.contour.alphamaskanimationsource | maxon::Int | Input | false | false | true |  |  | 0 | Global = 0, Custom = 1
Advanced/Backfacing/Angle Threshold | <com.redshift3d.redshift4c4d.nodes.core.contour.backfacinganglethreshold | maxon::Float | Input | false | false | false | 0 | 180 | 180 | 
Advanced/Backfacing/Color | <com.redshift3d.redshift4c4d.nodes.core.contour.backfacingcolor | maxon::Color64 | Input | false | false | false |  |  | (0,0,0) | 
Advanced/Backfacing/Depth Threshold | <com.redshift3d.redshift4c4d.nodes.core.contour.backfacingdepththreshold | maxon::Float | Input | false | false | false | 0 | 1000000 | 10 | 
Advanced/Backfacing/Detect Separate Meshes | <com.redshift3d.redshift4c4d.nodes.core.contour.backfacingdetectseparatemeshesmode | maxon::Int | Input | false | false | true |  |  | 0 | Off = 0, Overlapping = 1, Intersecting = 2, Overlapping and Intersecting = 3
Advanced/Backfacing/Enable | <com.redshift3d.redshift4c4d.nodes.core.contour.backfacingenable | maxon::Bool | Input | false | false | false |  |  | false | 
Advanced/Backfacing/Normal Type | <com.redshift3d.redshift4c4d.nodes.core.contour.backfacingnormaltype | maxon::Int | Input | false | false | true |  |  | 1 | Smooth Normal = 1, Geometric Normal = 2
Advanced/Backfacing/Opacity | <com.redshift3d.redshift4c4d.nodes.core.contour.backfacingopacity | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Advanced/Backfacing/Thickness | <com.redshift3d.redshift4c4d.nodes.core.contour.backfacingthickness | maxon::Float | Input | false | false | false | 0 | 32 | 4 | 
Advanced/Backfacing/Thickness Modifier | <com.redshift3d.redshift4c4d.nodes.core.contour.backfacingthicknessmodifier | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Advanced/Backfacing/Tonemap | <com.redshift3d.redshift4c4d.nodes.core.contour.backfacingtonemap | maxon::Color64 | Input | false | false | false |  |  |  | 
Advanced/Tonemapping/Mode | <com.redshift3d.redshift4c4d.nodes.core.contour.tonemapmode | maxon::Int | Input | false | false | true |  |  | 1 | Light and Shadow = 0, Light and Opaque Shadow = 1
Advanced/Tonemapping/Shadow Opacity | <com.redshift3d.redshift4c4d.nodes.core.contour.tonemapshadowopacity | maxon::Float | Input | false | false | false | -1 | 1 | 0 | 
General Properties/External/Color | <com.redshift3d.redshift4c4d.nodes.core.contour.externalcolor | maxon::Color64 | Input | false | false | false |  |  | (0,0,0) | 
General Properties/External/Detect Separate Meshes | <com.redshift3d.redshift4c4d.nodes.core.contour.externaldetectseparatemeshesmode | maxon::Int | Input | false | false | true |  |  | 0 | Off = 0, Overlapping = 1, Intersecting = 2, Overlapping and Intersecting = 3
General Properties/External/Enable | <com.redshift3d.redshift4c4d.nodes.core.contour.externalenable | maxon::Bool | Input | false | false | false |  |  | true | 
General Properties/External/Opacity | <com.redshift3d.redshift4c4d.nodes.core.contour.externalopacity | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
General Properties/External/Thickness | <com.redshift3d.redshift4c4d.nodes.core.contour.externalthickness | maxon::Float | Input | false | false | false | 0 | 32 | 4 | 
General Properties/External/Thickness Modifier | <com.redshift3d.redshift4c4d.nodes.core.contour.externalthicknessmodifier | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
General Properties/External/Tonemap | <com.redshift3d.redshift4c4d.nodes.core.contour.externaltonemap | maxon::Color64 | Input | false | false | false |  |  |  | 
General Properties/General/Visible in reflection | <com.redshift3d.redshift4c4d.nodes.core.contour.generalvisibleinreflection | maxon::Bool | Input | false | false | false |  |  | true | 
General Properties/General/Visible in refraction | <com.redshift3d.redshift4c4d.nodes.core.contour.generalvisibleinrefraction | maxon::Bool | Input | false | false | false |  |  | true | 
General Properties/Internal/Angle Threshold | <com.redshift3d.redshift4c4d.nodes.core.contour.internalanglethreshold | maxon::Float | Input | false | false | false | 0 | 180 | 180 | 
General Properties/Internal/Color | <com.redshift3d.redshift4c4d.nodes.core.contour.internalcolor | maxon::Color64 | Input | false | false | false |  |  | (0,0,0) | 
General Properties/Internal/Depth Threshold | <com.redshift3d.redshift4c4d.nodes.core.contour.internaldepththreshold | maxon::Float | Input | false | false | false | 0 | 1000000 | 10 | 
General Properties/Internal/Detect Separate Meshes | <com.redshift3d.redshift4c4d.nodes.core.contour.internaldetectseparatemeshesmode | maxon::Int | Input | false | false | true |  |  | 0 | Off = 0, Overlapping = 1, Intersecting = 2, Overlapping and Intersecting = 3
General Properties/Internal/Enable | <com.redshift3d.redshift4c4d.nodes.core.contour.internalenable | maxon::Bool | Input | false | false | false |  |  | true | 
General Properties/Internal/Normal Type | <com.redshift3d.redshift4c4d.nodes.core.contour.internalnormaltype | maxon::Int | Input | false | false | true |  |  | 1 | Smooth Normal = 1, Geometric Normal = 2
General Properties/Internal/Opacity | <com.redshift3d.redshift4c4d.nodes.core.contour.internalopacity | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
General Properties/Internal/Thickness | <com.redshift3d.redshift4c4d.nodes.core.contour.internalthickness | maxon::Float | Input | false | false | false | 0 | 32 | 4 | 
General Properties/Internal/Thickness Modifier | <com.redshift3d.redshift4c4d.nodes.core.contour.internalthicknessmodifier | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
General Properties/Internal/Tonemap | <com.redshift3d.redshift4c4d.nodes.core.contour.internaltonemap | maxon::Color64 | Input | false | false | false |  |  |  | 
Outputs/outColor | >com.redshift3d.redshift4c4d.nodes.core.contour.outcolor | maxon::Color64 | Output | false | false | false |  |  | (0,0,0) | 

