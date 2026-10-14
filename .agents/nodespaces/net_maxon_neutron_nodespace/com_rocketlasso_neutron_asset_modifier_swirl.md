# Node Template: Swirl

- **Node Space ID:** `net.maxon.neutron.nodespace`
- **Template ID:** `com.rocketlasso.neutron.asset.modifier.swirl`
- **Template Name:** `Swirl`

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
Node Category | net.maxon.node.base.category | maxon::InternedId | Attribute | false | false | true |  |  | geomodifiers | operators = operators, distributions = distributions, geometries = geometries, patterns = patterns, primitives = primitives, effectors = effectors, fields = fields, functions = functions, structures = structures, geomodifiers = geomodifiers, geogenerators = geogenerators
Preview/Node | net.maxon.node.base.nodepreviewimage | maxon::ImageBaseRef | Attribute | false | false | false |  |  |  | 
Advanced | <in@YZW8LN7BC58jhzezYByqt_ |  | Input | false | false | false |  |  |  | 
Advanced/Bias | <in@GmdeQXrTEFNhVeUCmwdtmW | maxon::Float64 | Input | false | false | false |  |  | -0.5 | 
Advanced/Fade | <in@ECgWlkWOBFassGUQ0RxU4o | maxon::Float64 | Input | false | false | false |  | 1 | 0 | 
Advanced/Individual Group/ | <in@YqMrmwa6Gh7vfm8fhyWDsR |  | Input | false | false | false |  |  |  | 
Advanced/Individual Group/Bias | <in@GuckL4D8P5ZiDOjtIaQ3UW | maxon::Float64 | Input | false | false | false |  |  | -0.5 | 
Advanced/Individual Group/Bias | <in@W2sz_khhFtWo299S2Zdvu3 | maxon::Float64 | Input | false | false | false |  |  | -0.75 | 
Advanced/Individual Group/Bias Height | <in@LPmpaaq$Ml1lcdgdHojxVS | maxon::Float64 | Input | false | false | false |  |  | -0.5 | 
Advanced/Individual Group/Ridge Shape | <in@C3Mz$2PsPRfug_G_JCrCsS | maxon::Float64 | Input | false | false | false |  |  | 0.5 | 
Advanced/Individual Group/Smooth | <in@J4nWcnE1DB6tcmCtj2BqL3 | maxon::Float64 | Input | false | false | false |  |  | 0.1 | 
Advanced/Individual Group/Smooth | <in@TXCKe9$xIt6i8efUG_O1bX | maxon::Float64 | Input | false | false | false |  |  | 0.1 | 
Advanced/Individual Group/Smooth Height | <in@CJ39P28FKxJn2gftQmuFjX | maxon::Float64 | Input | false | false | false |  |  | 0.1 | 
Advanced/Individual Group/Smooth Shape | <in@UZB6REeDBhenvKk2vW_faV | maxon::Float64 | Input | false | false | false |  |  | 0.5 | 
Advanced/Inner Radius     | <in@CFZVCamiHp1lYvHoyM8LTY | maxon::Float64 | Input | false | false | false |  |  | 0 | 
Advanced/Smooth | <in@MRiUCZVmMpFiPH3jWgwjKT | maxon::Float64 | Input | false | false | false |  |  | 0.1 | 
Inputs/Geometry | <geometryin | maxon::GeometryObject | Input | false | false | false |  |  |  | 
Inputs/Global Capsule Matrix | <globalmatin | maxon::Matrix64 | Input | false | false | false |  |  |  | 
Inputs/Global Object Matrix | <objectmatrix | maxon::Matrix64 | Input | false | false | false |  |  |  | 
Inputs/Local Capsule Matrix | <localmatin | maxon::Matrix64 | Input | false | false | false |  |  |  | 
Inputs/Local Modifier Matrix | <modifiermatrix | maxon::Matrix64 | Input | false | false | false |  |  |  | 
Inputs/Local Object Matrix | <localobjectmatrix | maxon::Matrix64 | Input | false | false | false |  |  |  | 
Object/ | <in@NnR4M5xTHRvtv3ZHexJvNo |  | Input | false | false | false |  |  |  | 
Object/ | <in@Spolr314BVcp5uhky8YpB_ |  | Input | false | false | false |  |  |  | 
Object/ | <in@cA8zE0eiHRcgatWMuMyQLt |  | Input | false | false | false |  |  |  | 
Object/Height | <in@AbCguwnPGBVsczOGiU00xr | maxon::Float64 | Input | false | false | false |  |  | 0 | 
Object/Offset Group | <in@JM8EDSRoFZVn$1DshgBIng |  | Input | false | false | false |  |  |  | 
Object/Offset Group/Rate | <in@UMgMUV7$CdquJzSY_7n5ok | maxon::Float64 | Input | false | false | false |  |  |  | 
Object/Offset Group/Ridge Offset  | <in@JYZe5yFyN9viFiPJEsvyKh | maxon::Float64 | Input | false | false | false |  |  |  | 
Object/Pull | <in@J6apv2B$AV2o9JyTbe1vts | maxon::Float64 | Input | false | false | false |  |  | 0 | 
Object/Radius | <in@KOIF5zd0C5rnXplNRIlsos | maxon::Float64 | Input | false | false | false |  |  | 200 | 
Object/Ridge Count | <in@XUBNa4a5KpZu_D8q56rJhk | maxon::Int64 | Input | false | false | false |  |  | 3 | 
Object/Ridge Height | <in@KmI3$mdwKFjiXH94ELz0Xl | maxon::Float64 | Input | false | false | false |  |  | 25 | 
Object/Swirl | <in@YeH9nnrLH57lswxa3VVS1q | maxon::Float64 | Input | false | false | false |  |  | 6.283 | 
Outputs/Geometry | >geometryout | maxon::GeometryObject | Output | false | false | false |  |  |  | 

