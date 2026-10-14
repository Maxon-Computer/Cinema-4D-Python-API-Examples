# Node Template: Spline Chamfer

- **Node Space ID:** `net.maxon.neutron.nodespace`
- **Template ID:** `net.maxon.neutron.geometry.spline.splinechamfer`
- **Template Name:** `Spline Chamfer`

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
Node Category | net.maxon.node.base.category | maxon::InternedId | Attribute | false | false | true |  |  | geogenerators | operators = operators, distributions = distributions, geometries = geometries, patterns = patterns, primitives = primitives, effectors = effectors, fields = fields, functions = functions, structures = structures, geomodifiers = geomodifiers, geogenerators = geogenerators
Preview/Node | net.maxon.node.base.nodepreviewimage | maxon::ImageBaseRef | Attribute | false | false | false |  |  |  | 
Inputs/Distance | <distance | maxon::Float | Input | false | false | false |  |  | 5 | 
Inputs/Geometry | <geometryin |  | Input | false | false | false |  |  |  | 
Inputs/Offset | <offset | maxon::InternedId | Input | false | false | true |  |  | fixeddistance | Radial = radial, Fixed Distance = fixeddistance
Inputs/Radius | <radius | maxon::Float | Input | false | false | false |  |  | 5 | 
Inputs/Type | <style | maxon::InternedId | Input | false | false | true |  |  | fillet | Fillet = fillet, Chamfer = chamfer
Max Angle | <maxangle | maxon::Float | Input | false | false | false |  | 3.142 | 0.087 | 
Selection | <selection | maxon::IndexSelection | Input | false | false | false |  |  |  | 
Selection String | <selectionstring | maxon::String | Input | false | false | false |  |  | default | 
Use Angle | <useangle | maxon::Bool | Input | false | false | false |  |  |  | 
Outputs/Geometry | >geometryout |  | Output | false | false | false |  |  |  | 

