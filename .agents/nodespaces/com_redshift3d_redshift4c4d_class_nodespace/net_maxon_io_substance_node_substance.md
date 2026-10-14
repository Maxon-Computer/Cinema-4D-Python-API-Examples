# Node Template: Substance 3D Material

- **Node Space ID:** `com.redshift3d.redshift4c4d.class.nodespace`
- **Template ID:** `net.maxon.io_substance.node.substance`
- **Template Name:** `Substance 3D Material`

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
Commands | commands |  | Attribute | false | false | false |  |  |  | 
Commands/Export | net.maxon.io_substance.node.substance.export |  | Attribute | false | false | false |  |  |  | 
Commands/Reload | net.maxon.io_substance.node.substance.reload |  | Attribute | false | false | false |  |  |  | 
Filter Tags | net.maxon.node.base.filtertags | maxon::CString | Attribute | false | false | false |  |  |  | 
Node Category | net.maxon.node.base.category | maxon::InternedId | Attribute | false | false | true |  |  | functions | operators = operators, distributions = distributions, geometries = geometries, patterns = patterns, primitives = primitives, effectors = effectors, fields = fields, functions = functions, structures = structures, geomodifiers = geomodifiers, geogenerators = geogenerators
Preview/Node | net.maxon.node.base.nodepreviewimage | maxon::ImageBaseRef | Attribute | false | false | false |  |  |  | 
Inputs/File | <net.maxon.io_substance.node.substance.file | maxon::Url | Input | false | false | false |  |  |  | 
Inputs/Height | <net.maxon.io_substance.node.substance.resolution.height | maxon::Int | Input | false | false | true |  |  | 1024 | 16 = 16, 32 = 32, 64 = 64, 128 = 128, 256 = 256, 512 = 512, 1024 = 1024, 2048 = 2048, 4096 = 4096, 8192 = 8192, 16384 = 16384
Inputs/Lock Ratio | <net.maxon.io_substance.node.substance.lockratio | maxon::Bool | Input | false | false | false |  |  | true | 
Inputs/Physical Size | <net.maxon.io_substance.node.substance.physicalsize_input | maxon::Vector | Input | false | false | false |  | (50,50,50) |  | 
Inputs/Preset | <net.maxon.io_substance.node.substance.presets | maxon::Int | Input | false | false | true |  |  | -1 | Default = -1
Inputs/Random Seed | <net.maxon.io_substance.node.substance.randomseed | maxon::Int | Input | false | false | false |  | 50 |  | 
Inputs/Width | <net.maxon.io_substance.node.substance.resolution.width | maxon::Int | Input | false | false | true |  |  | 1024 | 16 = 16, 32 = 32, 64 = 64, 128 = 128, 256 = 256, 512 = 512, 1024 = 1024, 2048 = 2048, 4096 = 4096, 8192 = 8192, 16384 = 16384
Outputs/Physical Size | >net.maxon.io_substance.node.substance.physicalsize_output | maxon::Vector | Output | false | false | false |  | (50,50,50) |  | 

