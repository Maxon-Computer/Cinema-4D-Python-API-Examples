# Node Template: Landscape Mask

- **Node Space ID:** `net.maxon.nodespace.standard`
- **Template ID:** `landscapemask@d6bddd94-a639-4d04-b67a-261e80f60e37`
- **Template Name:** `Landscape Mask`

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
Node Category | net.maxon.node.base.category | maxon::InternedId | Attribute | false | false | true |  |  | functions | distributions = distributions, operators = operators, geometries = geometries, patterns = patterns, primitives = primitives, effectors = effectors, fields = fields, functions = functions, structures = structures, geomodifiers = geomodifiers, geogenerators = geogenerators
Preview/Node | net.maxon.node.base.nodepreviewimage | maxon::ImageBaseRef | Attribute | false | false | false |  |  |  | 
Landscape Mask/Elevation/Elevation Position | <inport@$wqWsap3M5No25ne0HeBVB | maxon::Float64 | Input | false | false | false |  |  | 350 | 
Landscape Mask/Elevation/Elevation Transition Range | <inport@Oa_sdskyMVdriGSVLJ5yeB | maxon::Float64 | Input | false | false | false |  |  | 300 | 
Landscape Mask/Elevation/Elevation Turbulence | <inport@7gsfeFRzAlSkEdWKnpsdaB | maxon::Float64 | Input | false | false | false | 0 | 1 | 0.6 | 
Landscape Mask/Elevation/Elevation Turbulence Scale | <inport@cxdSnt8CGVGhuuja9ozpIs | maxon::Vector64 | Input | false | false | false |  |  | (2,2,2) | 
Landscape Mask/Elevation/Elevation Wavy Turbulence | <inport@3UKhC810Ppvoday5oiIJ9D | maxon::Float64 | Input | false | false | false | 0 | 1 | 0.4 | 
Landscape Mask/Filter Contrast | <inport@RySQqkn0PNyvJh5vsHD2l1 | maxon::Float64 | Input | false | false | false | 0 | 1 |  | 
Landscape Mask/Global Turbulence/Global Turbulence | <inport@Ut6e7ay_O9GjBWfsSO7lUN | maxon::Float64 | Input | false | false | false | 0 | 1 | 0.1 | 
Landscape Mask/Global Turbulence/Global Turbulence Scale | <inport@PsnLVNH0LVVmsBdQJtdZrO | maxon::Vector64 | Input | false | false | false |  |  | (5,5,5) | 
Landscape Mask/Ridges/Ridges Intensity | <inport@XIbD6sRWHVohx6IGmVg5iA | maxon::Float64 | Input | false | false | false | 0 | 1 | 0.7 | 
Landscape Mask/Ridges/Ridges Range | <inport@ENGF_9AsMlllnqXWympbdA | maxon::Float64 | Input | false | false | false |  |  | 150 | 
Landscape Mask/Seed | <inport@f7C96DdZHp6tyuU_O7q8i2 | maxon::Int64 | Input | false | false | false |  | 10000 | 50 | 
Landscape Mask/Slope/Slope Coverage | <inport@OUoGixoyFZknL8B1KhfVtD | maxon::Float64 | Input | false | false | false |  | 1 | 0.3 | 
Landscape Mask/Slope/Slope Intensity | <inport@QT2AXCfPKZ8hLl7pPFCH8L | maxon::Float64 | Input | false | false | false | 0 | 1 | 0.95 | 
Landscape Mask/Stratification/Stratification Intensity | <inport@KPnjSaQnH1IpMRIJg39Qft | maxon::Float64 | Input | false | false | false |  | 1 | 0.35 | 
Landscape Mask/Stratification/Stratification Scale | <inport@KI0s8pXCEt3uC9okcp0juu | maxon::Vector64 | Input | false | false | false |  |  | (4,4,4) | 
Outputs/Color | >result@214jl3YFPRUjQ1InjU6bFB | maxon::ColorA64 | Output | false | false | false |  |  |  | 

