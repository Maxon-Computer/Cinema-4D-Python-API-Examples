# Node Template: Ivy Generator

- **Node Space ID:** `net.maxon.neutron.nodespace`
- **Template ID:** `com.rocketlasso.neutron.asset.generator.ivy`
- **Template Name:** `Ivy Generator`

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
Basic/Show Tag | net.maxon.neutron.showtag | maxon::Bool | Attribute | false | false | false |  |  |  | 
Filter Tags | net.maxon.node.base.filtertags | maxon::CString | Attribute | false | false | false |  |  |  | 
IVY/Spline Guide/Spline Object/Geometry | <in@LJqFgomKLJmiyDMcf3gVeg/geometry | maxon::GeometryObject | Attribute | false | false | false |  |  |  | 
IVY/Spline Guide/Spline Object/Matrix | <in@LJqFgomKLJmiyDMcf3gVeg/matrix | maxon::Matrix | Attribute | false | false | false |  |  |  | 
IVY/Surface Object/Geometry | <in@ABjB_V1yJ9Um5AdznNDcon/geometry | maxon::GeometryObject | Attribute | false | false | false |  |  |  | 
IVY/Surface Object/Matrix | <in@ABjB_V1yJ9Um5AdznNDcon/matrix | maxon::Matrix | Attribute | false | false | false |  |  |  | 
IVY/Target/Target Object/Matrix | <in@JtLmqvPwCV4ucZE9Vh2bMl/matrix | maxon::Matrix | Attribute | false | false | false |  |  |  | 
Inputs/Object/Matrix | <objectinput/matrix | maxon::Matrix | Attribute | false | false | false |  |  |  | 
Node Category | net.maxon.node.base.category | maxon::InternedId | Attribute | false | false | true |  |  | functions | distributions = distributions, operators = operators, geometries = geometries, patterns = patterns, primitives = primitives, effectors = effectors, fields = fields, functions = functions, structures = structures, geomodifiers = geomodifiers, geogenerators = geogenerators
Outputs/Object/Matrix | >matrixout/matrix | maxon::Matrix | Attribute | false | false | false |  |  |  | 
Preview/Node | net.maxon.node.base.nodepreviewimage | maxon::ImageBaseRef | Attribute | false | false | false |  |  |  | 
Basic/Bypass | <net.maxon.node.bypassable.bypass | maxon::Bool | Input | false | false | false |  |  |  | 
Basic/Children | <net.maxon.neutron.op.objectbase.children | net.maxon.neutron.portbundle.object | Input | true | false | false |  |  |  | 
Coord/Matrix | <net.maxon.neutron.op.objectbase.matrix | maxon::Matrix64 | Input | false | false | false |  |  |  | 
Geometry/Branch Output | <in@LmJcZ9nSBF4rwFB_x9aH_S | maxon::Int64 | Input | false | false | true |  |  |  | Geometry = 0, All Splines = 1, Trunk Spline Only = 2, Branches Splines Only = 3, Branch 1 Splines = 4, Branch 2 Splines = 5
Geometry/Leaves/Cling Gravity | <in@Kz3u51JWC9DgWxVCjGqUyQ | maxon::Float64 | Input | false | false | false |  | 1.571 | 0.5 | 
Geometry/Leaves/Dangle Gravity | <in@NKFnwFR1BpgnAd7jk0AAsX | maxon::Float64 | Input | false | false | false |  | 1.571 | 0.5 | 
Geometry/Leaves/Every nth Segment | <integer2 | maxon::Int64 | Input | false | false | false |  |  | 4 | 
Geometry/Leaves/Leaf Angle Variation | <in@EGAvRe1fJtjoK3$qh90MDg | maxon::Vector64 | Input | false | false | false |  |  | (0.262,0.262,0.873) | 
Geometry/Leaves/Leaf Angle Variation | <in@awtRWzemNZhtoLo3qvlkEU | maxon::Vector64 | Input | false | false | false |  |  | (0.262,0.262,0.873) | 
Geometry/Leaves/Leaf Density | <in@ZlQgl2ZpFZjmwYyOvnaV7B | maxon::Float64 | Input | false | false | false |  |  | 1 | 
Geometry/Leaves/Leaf Scale | <in@aKsz4CfUDxyqOBNVzuhVKn | maxon::Float64 | Input | false | false | false |  |  | 1 | 
Geometry/Leaves/Leaf Size From End | <in@dC2F_z$OOlHpj1uDheS4zk | maxon::Float64 | Input | false | false | false |  |  | 24 | 
Geometry/Leaves/Leaf Size Variation | <in@fdJFitsRFBqpULUgdxhY$j | maxon::Float64 | Input | false | false | false |  |  | 0.1 | 
Geometry/Leaves/Leaves | <bool | maxon::Bool | Input | false | false | false |  |  | true | 
Geometry/Leaves/Mirror | <in@YbaL3f0UIhCiG9WbqJRe1Z | maxon::Float64 | Input | false | false | false |  | 1.571 | 0.262 | 
Geometry/Leaves/Stick To Wall | <in@ByWDHcDlLhGh8pWxHhFRgG | maxon::Bool | Input | false | false | false |  |  | true | 
Geometry/Leaves/Tug Upward | <in@a82GPomgFZGltQQ$1BPHMk | maxon::Float64 | Input | false | false | false |  | 1.571 | 0.524 | 
Geometry/Vine/Subdivisions/Subdivision Angle | <attr@JvnpR_sWL56p$$ORFG$XFm | maxon::Float64 | Input | false | false | false |  | 1.571 | 0.524 | 
Geometry/Vine/Subdivisions/Subdivision Length | <attr@MBzx7KNPKtql7bPAPRLNem | maxon::Int64 | Input | false | false | false |  | 100 | 8 | 
Geometry/Vine/Subdivisions/Vine Sides | <in@HHyA9i7$CZ7ojWrmXBU0h9 | maxon::Int64 | Input | false | false | false | 2 | 100 | 6 | 
Geometry/Vine/Thickness Max | <in@dPYODKfxAt3jUgcMDGvn9l | maxon::Float64 | Input | false | false | false |  |  | 0.3 | 
Geometry/Vine/Thickness Min           | <in@e5rz_e2MLZwv0yJPXpEb6j | maxon::Float64 | Input | false | false | false |  |  | 0.1 | 
IVY/Branch Length | <in@EslYqHhEIFApqabsilQYyX | maxon::Float64 | Input | false | false | false |  |  | 250 | 
IVY/Branching/Initial Angle            | <in@BMdRlVWUFppq$Stw_JPu2g | maxon::Float64 | Input | false | false | false |  |  | 0.524 | 
IVY/Branching/Kink | <in@KumWVcWLIBhj74A54NWBVh | maxon::Float64 | Input | false | false | false |  |  | 0.436 | 
IVY/Climb Force | <in@EoO3VXuhOtqof2nJ2Scl6X | maxon::Float64 | Input | false | false | false |  |  | 0.05 | 
IVY/Dangle Force | <in@TwL7nCy1OJckla_Kf18c_v | maxon::Float64 | Input | false | false | false |  |  | 0.15 | 
IVY/Density | <in@XTZvtvT1AZ5lvdgmte7wtQ | maxon::Float64 | Input | false | false | false |  | 1 | 0.1 | 
IVY/Length Variation | <in@J8ngZwtICRIvMpnzkzEToV | maxon::Float64 | Input | false | false | false |  |  | 0.5 | 
IVY/Max Cap                    | <integer | maxon::Int64 | Input | false | false | false |  |  | 100000 | 
IVY/Max Ivy Length | <in@YCudS3BRDB0qcHV_vJKuSl | maxon::Float64 | Input | false | false | false |  |  | 500 | 
IVY/Seed | <in@MJ9AyK_uBt6u8W0QUMUhrn | maxon::Float64 | Input | false | false | false |  |  | 12345 | 
IVY/Selection String | <in@e0LnUIQDNpflUHFd$l7nUn | maxon::String | Input | false | false | false |  |  | All | 
IVY/Spline Guide/Branches Force      | <in@N06hou00ERAtqBmVeKVC7g | maxon::Float64 | Input | false | false | false |  |  | 0 | 
IVY/Spline Guide/Spline Object | <in@LJqFgomKLJmiyDMcf3gVeg | net.maxon.neutron.portbundle.object | Input | false | true | false |  |  |  | 
IVY/Spline Guide/Stem Force | <in@XI0JSfFhIRIpRDuUksEyiS | maxon::Float64 | Input | false | false | false |  |  | 0.25 | 
IVY/Step Size                   | <in@eZh3evLoAlggQfc_nXJ4Ii | maxon::Float64 | Input | false | false | false |  |  | 2 | 
IVY/Surface Object | <in@ABjB_V1yJ9Um5AdznNDcon | net.maxon.neutron.portbundle.object | Input | false | true | false |  |  |  | 
IVY/Surface/Stick Distance Max | <in@MvB4uxLLEJqnS0l5ImgkDj | maxon::Float64 | Input | false | false | false |  |  | 40 | 
IVY/Surface/Surface Force | <in@P2HxLP6kL5ciR9pZyrqLPm | maxon::Float64 | Input | false | false | false |  |  | 0.2 | 
IVY/Surface/Surface Offset | <in@KRZWmoC_HJTltkXNH1f2Em | maxon::Float64 | Input | false | false | false |  |  | 5 | 
IVY/Target/Target Force           | <in@RNkpfawlIdZhp0cM7tgSsm | maxon::Float64 | Input | false | false | false |  |  | 0.5 | 
IVY/Target/Target Object | <in@JtLmqvPwCV4ucZE9Vh2bMl | net.maxon.neutron.portbundle.object | Input | false | true | false |  |  |  | 
IVY/Target/Target Object/Parent Matrix | <in@JtLmqvPwCV4ucZE9Vh2bMl/parentmatrix |  | Input | false | false | false |  |  |  | 
Inputs/Object | <objectinput | net.maxon.neutron.portbundle.object | Input | false | true | false |  |  |  | 
Inputs/Object/Parent Matrix | <objectinput/parentmatrix |  | Input | false | false | false |  |  |  | 
Inputs/Object/Position | <objectinput/translation |  | Input | false | false | false |  |  |  | 
Inputs/Object/Rotation/Scale/Shear | <objectinput/sqrmatrix |  | Input | false | false | false |  |  |  | 
Inputs/Object/Scope | <objectinput/domain |  | Input | false | false | false |  |  |  | 
Inputs/Op | <net.maxon.neutron.op.input | net.maxon.neutron.portbundle.object | Input | false | true | false |  |  |  | 
Inputs/Op/Position | <net.maxon.neutron.op.input/translation |  | Input | false | false | false |  |  |  | 
Inputs/Op/Rotation/Scale/Shear | <net.maxon.neutron.op.input/sqrmatrix |  | Input | false | false | false |  |  |  | 
Inputs/Op/Scope | <net.maxon.neutron.op.input/domain |  | Input | false | false | false |  |  |  | 
Object/Children | <in@KG8f$_KBBRto0PkVC2K9GR | net.maxon.neutron.portbundle.object | Input | true | false | false |  |  |  | 
Outputs/Object/Parent Matrix | >matrixout/parentmatrix |  | Input | false | false | false |  |  |  | 
Outputs/Object/Position | >matrixout/translation |  | Input | false | false | false |  |  |  | 
Outputs/Object/Rotation/Scale/Shear | >matrixout/sqrmatrix |  | Input | false | false | false |  |  |  | 
Outputs/Object/Scope | >matrixout/domain |  | Input | false | false | false |  |  |  | 
Outputs/Op/Children | >net.maxon.neutron.op.output/children |  | Input | false | false | false |  |  |  | 
Outputs/Op/Scope | >net.maxon.neutron.op.output/domain |  | Input | false | false | false |  |  |  | 
Selections/Branches | <in@WH0aQ1OpMtEh2OMN8QSB4n | maxon::String | Input | false | false | false |  |  | Branches | 
Selections/Leaves | <in@OTDf6wtOApzk5Bldf8YbOn | maxon::String | Input | false | false | false |  |  | Leaves | 
Outputs/Leaf Distribution | >out@Y9LHmzhxCdIla$yZ0NxsGe | maxon::ArrayContainer<maxon::Int64, maxon::Vector64, maxon::Matrix64, maxon::Color64> | Output | false | false | false |  |  |  | 
Outputs/Object | >matrixout | net.maxon.neutron.portbundle.object | Output | false | true | false |  |  |  | 
Outputs/Op | >net.maxon.neutron.op.output | net.maxon.neutron.portbundle.object | Output | false | true | false |  |  |  | 
Outputs/Output | >children.out |  | Output | false | false | false |  |  |  | 
Outputs/Vine Distribution | >out@cKGZAbk_Kl4nmx0kYhe17p | maxon::ArrayContainer<maxon::Int64, maxon::Vector64, maxon::Matrix64, maxon::Color64> | Output | false | false | false |  |  |  | 

