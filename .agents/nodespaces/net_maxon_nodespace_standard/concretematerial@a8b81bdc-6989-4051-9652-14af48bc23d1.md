# Node Template: Concrete Material

- **Node Space ID:** `net.maxon.nodespace.standard`
- **Template ID:** `concretematerial@a8b81bdc-6989-4051-9652-14af48bc23d1`
- **Template Name:** `Concrete Material`

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
Node Category | net.maxon.node.base.category | maxon::InternedId | Attribute | false | false | true |  |  | functions | operators = operators, distributions = distributions, geometries = geometries, patterns = patterns, primitives = primitives, effectors = effectors, fields = fields, functions = functions, structures = structures, geomodifiers = geomodifiers, geogenerators = geogenerators
Preview/Node | net.maxon.node.base.nodepreviewimage | maxon::ImageBaseRef | Attribute | false | false | false |  |  |  | 
Base/Color | <inport@ClsNMDM_I5HgrGX38vs7f5 | maxon::Color64 | Input | false | false | false |  |  | (0.2,0.209,0.214) | 
Base/Dirt | <inport@cNN8CtnLPNhvm6eHAUzH86 | maxon::Float64 | Input | false | false | false | 0 | 1 | 0.1 | 
Base/Grain | <inport@TLbfEoQRNV4tiugnSTL8B8 | maxon::Float64 | Input | false | false | false | 0 | 1 | 0.2 | 
Base/Turbulence | <inport@caDuJ6J4Bdnh$uvauoCv$_ | maxon::Float64 | Input | false | false | false | 0 | 1 | 0.4 | 
Deformation/Strength | <inport@WPERnK83BlbqaTkPv_CZ$9 | maxon::Float64 | Input | false | false | false |  | 1 | 0.15 | 
Reflectance/Reflectance | <inport@OkTxTbstL9Rpep88LubLM$ | maxon::Bool | Input | false | false | false |  |  | false | 
Reflectance/Strength | <inport@BtDoJ4D$Dt$h0E8jhGlnP6 | maxon::Float64 | Input | false | false | false |  | 1 | 0.1 | 
Variation/Seed | <inport@A83JwzFxIx4kNMhGo9NscX | maxon::UInt32 | Input | false | false | false |  |  | 250 | 

