# Node Template: Projection

- **Node Space ID:** `net.maxon.nodespace.standard`
- **Template ID:** `net.maxon.render.node.projection`
- **Template Name:** `Projection`

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
Context/Context | <context | maxon::ShadingContext | Input | false | false | false |  |  |  | 
Inputs/Additional Transform | <enablespacetransformation | maxon::Bool | Input | false | false | false |  |  |  | 
Inputs/Camera | <camera | maxon::Uuid | Input | false | false | false |  |  |  | 
Inputs/Coordinate System | <spacetype | maxon::InternedId | Input | false | false | true |  |  | texture | World = world, Object = object, Texture = texture, Camera = camera
Inputs/Film Aspect | <filmaspect | maxon::Float | Input | false | false | false | 0.1 | 10 | 1.333 | 
Inputs/Local Decal U | <localdecalu | maxon::Bool | Input | false | false | false |  |  | false | 
Inputs/Local Decal V | <localdecalv | maxon::Bool | Input | false | false | false |  |  | false | 
Inputs/Local Length | <locallength | maxon::Vector2d | Input | false | false | false |  |  | (1,1) | 
Inputs/Local Mode U | <localmodeu | maxon::InternedId | Input | false | false | true |  |  | extend | Repeat = repeat, Clamp = clamp, Extend = extend, Mirror = mirror
Inputs/Local Mode V | <localmodev | maxon::InternedId | Input | false | false | true |  |  | extend | Repeat = repeat, Clamp = clamp, Extend = extend, Mirror = mirror
Inputs/Local Offset | <localoffset | maxon::Vector2d | Input | false | false | false |  |  |  | 
Inputs/Local Pivot | <localpivot | maxon::Vector2d | Input | false | false | false |  |  | (0.5,0.5) | 
Inputs/Local Repetitions | <localrepetitions | maxon::Vector2d | Input | false | false | false |  |  | (1,1) | 
Inputs/Local Rotation | <localrotation | maxon::Float | Input | false | false | false |  |  |  | 
Inputs/Pixel Aspect | <pixelaspect | maxon::Float | Input | false | false | false | 0.1 | 10 | 1 | 
Inputs/Position | <spaceposition | maxon::Vector | Input | false | false | false |  |  |  | 
Inputs/Projection | <projectiontype | maxon::InternedId | Input | false | false | true |  |  | none | Spherical = spherical, Cylindrical = cylindrical, Flat = flat, Cubic = cubic, Frontal = frontal, Spatial = spatial, Shrink Wrap = shrinkwrap, Camera Mapping = cameramapping, None (use 3D coordinate) = none
Inputs/Reference Size | <referencesize | maxon::Float | Input | false | false | false |  |  | 200 | 
Inputs/Rotation | <spacerotation | maxon::Vector | Input | false | false | false |  |  |  | 
Inputs/Rotation Order | <spacerotationorder | maxon::Id | Input | false | false | true |  |  | yxzlocal | Local ZYX = zyxlocal, Local XYZ = xyzlocal, Local YZX = yzxlocal, Local XZY = xzylocal, Local ZXY = zxylocal, Local YXZ = yxzlocal, Global ZYX = zyxglobal, Global XYZ = xyzglobal, Global YZX = yzxglobal, Global XZY = xzyglobal, Global ZXY = zxyglobal, Global YXZ = yxzglobal
Inputs/Scale | <spacescale | maxon::Vector | Input | false | false | false |  |  | (1,1,1) | 
Outputs/Result | >result | maxon::ShadingContext | Output | false | false | false |  |  |  | 

