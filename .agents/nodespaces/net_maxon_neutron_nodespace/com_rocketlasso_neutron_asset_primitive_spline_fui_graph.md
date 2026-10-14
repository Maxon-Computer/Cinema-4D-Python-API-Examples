# Node Template: FUI Graph

- **Node Space ID:** `net.maxon.neutron.nodespace`
- **Template ID:** `com.rocketlasso.neutron.asset.primitive.spline.fui.graph`
- **Template Name:** `FUI Graph`

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
Data/CSV/Data Columns/Color | <GFECZgFrEx4g5ZbKVqS56S | maxon::InternedId | Input | false | false | false |  |  |  | 
Data/CSV/Data Columns/Height | <Mkc3x9pMEhWk7l7_fsiWBW | maxon::InternedId | Input | false | false | false |  |  |  | 
Data/CSV/Data Columns/Width | <JW$QUG3YBNgudHp1oaM5NS | maxon::InternedId | Input | false | false | false |  |  |  | 
Data/CSV/File (*.csv) | <inport@fRSZLMWMJBynt8JdhDsz_U | maxon::Url | Input | false | false | false |  |  |  | 
Data/Input | <QGCezmReGhZmK73Vf$UwoA | maxon::Int64 | Input | false | false | true |  |  | 4 | Manual = 0, Noise = 4, Random = 1, Spline = 2
Data/Manual/Data | <inport@Ibtj$dIYP1EpC6dBz8yml4 | maxon::Vector2d64 | Input | true | true | false |  |  |  | 
Data/Manual/Data/Data.1 | <inport@Ibtj$dIYP1EpC6dBz8yml4/_0 | maxon::Vector2d64 | Input | false | false | false |  |  |  | 
Data/Manual/Data/Data.2 | <inport@Ibtj$dIYP1EpC6dBz8yml4/_2 | maxon::Vector2d64 | Input | false | false | false |  |  |  | 
Data/Manual/Data/Data.3 | <inport@Ibtj$dIYP1EpC6dBz8yml4/_3 | maxon::Vector2d64 | Input | false | false | false |  |  |  | 
Data/Manual/Data/Data.4 | <inport@Ibtj$dIYP1EpC6dBz8yml4/_4 | maxon::Vector2d64 | Input | false | false | false |  |  |  | 
Data/Manual/Data/Data.5 | <inport@Ibtj$dIYP1EpC6dBz8yml4/_5 | maxon::Vector2d64 | Input | false | false | false |  |  |  | 
Data/Manual/Data/Data.6 | <inport@Ibtj$dIYP1EpC6dBz8yml4/_1 | maxon::Vector2d64 | Input | false | false | false |  |  |  | 
Data/Noise Group/  | <D32O2e6CHJysEuCvorSmYD | maxon::String | Input | false | false | false |  |  | Warning Shuffle Is Activated | 
Data/Noise Group/Horizontal/Noise Scale Group2/Noise Scale | <bexGJRacBR_odyLEMvl1tB | maxon::Float64 | Input | false | false | false |  |  | 1 | 
Data/Noise Group/Horizontal/Noise Scale Group2/Octaves       | <O1q_oUILBtGt84IvEyJlud | maxon::Float64 | Input | false | false | false |  | 20 | 5 | 
Data/Noise Group/Horizontal/Variation     | <U026s_hhMdskPlDsSPN_PV | maxon::Float64 | Input | false | false | false |  | 1 | 0 | 
Data/Noise Group/Horizontal/Width/Loop Frame | <F3fpgMBXMlKjqznAGi9GVv | maxon::TimeValue | Input | false | false | false |  |  |  | 
Data/Noise Group/Horizontal/Width/Speed         | <Jt4Bh2cPEhtsFfcAgKxNNi | maxon::Float64 | Input | false | false | false |  |  | 0 | 
Data/Noise Group/Noise Seed Group/Noise | <inport@SYAyQULJFxWoANwpl1W9BZ | maxon::Id | Input | false | false | true |  |  | net.maxon.render.rendernoiseclass.perlin | registry#net.maxon.render.registry.rendernoiseclasses = registry#net.maxon.render.registry.rendernoiseclasses
Data/Noise Group/Noise Seed Group/Seed        | <ErUGtpfQGlMgKuLguY16Mr | maxon::Int64 | Input | false | false | false |  | 99999999 | 12345 | 
Data/Noise Group/Vertical/Contrast Noise/Bias             | <MEuV1dHoAdDvCUB3BDHrjH | maxon::Float64 | Input | false | false | false |  |  | 0 | 
Data/Noise Group/Vertical/Contrast Noise/Max | <Z5_n$Im_KFsqz1US3XmSzh | maxon::Float64 | Input | false | false | false |  | 1 | 1 | 
Data/Noise Group/Vertical/Contrast Noise/Min | <TvZ7t9BuP1nsuutr69PG2l | maxon::Float64 | Input | false | false | false |  | 1 | 0 | 
Data/Noise Group/Vertical/Contrast Noise/Shift | <NF3MlAvyIBOuoEsk4M$BQm | maxon::Float64 | Input | false | false | false |  | 1 | 0 | 
Data/Noise Group/Vertical/Height Group 2/Offset          | <FA0HPiT2NBxo3wFCClcLkA | maxon::Float64 | Input | false | false | false |  |  | 0 | 
Data/Noise Group/Vertical/Height Group 2/Quantize | <EMEebr$_IBNoR2vcJ0x9cd | maxon::Bool | Input | false | false | false |  |  |  | 
Data/Noise Group/Vertical/Height Group 2/Speed          | <Ws7bMxIEBVjpY0WmbFsdnx | maxon::Float64 | Input | false | false | false |  |  | 0 | 
Data/Noise Group/Vertical/Noise Scale Group/Noise Scale | <WiSk2mC6FplgmC1n36R_sS | maxon::Float64 | Input | false | false | false |  |  | 1 | 
Data/Noise Group/Vertical/Noise Scale Group/Octaves       | <TsiYIB$nKNlmNxbt1lWMMY | maxon::Float64 | Input | false | false | false |  | 20 | 5 | 
Data/Noise Group/Vertical/Speed group/Loop Frame | <GwD2OC$CKp4syyUzwPsZTB | maxon::TimeValue | Input | false | false | false |  |  |  | 
Data/Noise Group/Vertical/Speed group/Speed          | <YNkrKajZO5NuGxVhiwyDeQ | maxon::Float64 | Input | false | false | false |  |  | 0.25 | 
Data/Random Group/Contrast X/Variation | <Wf8FpPBYNlsjRypUkItoYQ | maxon::Float64 | Input | false | false | false | 0 | 1 | 0 | 
Data/Random Group/Contrast Y/Bias | <ASwCw6MQGtagB0ORmqBFo8 | maxon::Float64 | Input | false | false | false |  | 1 | 0 | 
Data/Random Group/Contrast Y/Max | <BUlkSjREKFDtHA51SGKy8R | maxon::Float64 | Input | false | false | false |  | 1 | 1 | 
Data/Random Group/Contrast Y/Min | <KVKzlqb0Eh2qUNh6GHEJ4Q | maxon::Float64 | Input | false | false | false |  | 1 | 0 | 
Data/Random Group/Contrast Y/Shift | <Eg9q_VOYClFquzp92CZkV6 | maxon::Float64 | Input | false | false | false |  | 1 | 0 | 
Data/Random Group/Seed      | <YV9ZOVt3I16op4qaZBTp8G | maxon::Int64 | Input | false | false | false |  | 99999999 | 12345 | 
Data/Spline Group/Horizontal/Horizontal Details Group/Variation | <TzV$rfWGDRbvOlDSS0Mbmj | maxon::Float64 | Input | false | false | false | 0 | 1 | 0.25 | 
Data/Spline Group/Horizontal/Horizontal Spline/Spline | <spline@bkoCZAXMCFnrFm53dRDcAr | net.maxon.render.portbundle.spline | Input | false | true | false |  |  |  | 
Data/Spline Group/Horizontal/Horizontal Spline/Spline/Link End Positions | <spline@bkoCZAXMCFnrFm53dRDcAr/linkendpositions | maxon::Bool | Input | false | false | false |  |  |  | 
Data/Spline Group/Horizontal/Horizontal Spline/Spline/Link End Tangents | <spline@bkoCZAXMCFnrFm53dRDcAr/linkendtangents | maxon::Bool | Input | false | false | false |  |  |  | 
Data/Spline Group/Horizontal/Horizontal Spline/Spline/Max | <spline@bkoCZAXMCFnrFm53dRDcAr/max | maxon::Vector2d | Input | false | false | false |  |  | (1,1) | 
Data/Spline Group/Horizontal/Horizontal Spline/Spline/Min | <spline@bkoCZAXMCFnrFm53dRDcAr/min | maxon::Vector2d | Input | false | false | false |  |  |  | 
Data/Spline Group/Horizontal/Horizontal Spline/Spline/Points | <spline@bkoCZAXMCFnrFm53dRDcAr/points | net.maxon.render.portbundle.splinepoint | Input | true | false | false |  |  |  | 
Data/Spline Group/Horizontal/Horizontal Spline/Spline/Points/Point.1 | <spline@bkoCZAXMCFnrFm53dRDcAr/points/_0 | net.maxon.render.portbundle.splinepoint | Input | false | false | false |  |  |  | 
Data/Spline Group/Horizontal/Horizontal Spline/Spline/Points/Point.1/Break Tangent | <spline@bkoCZAXMCFnrFm53dRDcAr/points/_0/breaktangent | maxon::Bool | Input | false | false | false |  |  |  | 
Data/Spline Group/Horizontal/Horizontal Spline/Spline/Points/Point.1/Interpolation | <spline@bkoCZAXMCFnrFm53dRDcAr/points/_0/interpolation | maxon::InternedId | Input | false | false | true |  |  | spline | Spline = spline, Cubic = cubic, Linear = linear
Data/Spline Group/Horizontal/Horizontal Spline/Spline/Points/Point.1/Keep Visual Angle | <spline@bkoCZAXMCFnrFm53dRDcAr/points/_0/keepvisualangle | maxon::Bool | Input | false | false | false |  |  |  | 
Data/Spline Group/Horizontal/Horizontal Spline/Spline/Points/Point.1/Lock Angle | <spline@bkoCZAXMCFnrFm53dRDcAr/points/_0/lockangle | maxon::Bool | Input | false | false | false |  |  |  | 
Data/Spline Group/Horizontal/Horizontal Spline/Spline/Points/Point.1/Lock Length | <spline@bkoCZAXMCFnrFm53dRDcAr/points/_0/locklength | maxon::Bool | Input | false | false | false |  |  |  | 
Data/Spline Group/Horizontal/Horizontal Spline/Spline/Points/Point.1/Lock X | <spline@bkoCZAXMCFnrFm53dRDcAr/points/_0/lockx | maxon::Bool | Input | false | false | false |  |  |  | 
Data/Spline Group/Horizontal/Horizontal Spline/Spline/Points/Point.1/Lock Y | <spline@bkoCZAXMCFnrFm53dRDcAr/points/_0/locky | maxon::Bool | Input | false | false | false |  |  |  | 
Data/Spline Group/Horizontal/Horizontal Spline/Spline/Points/Point.1/Position X | <spline@bkoCZAXMCFnrFm53dRDcAr/points/_0/positionx | maxon::Float | Input | false | false | false |  |  | 0 | 
Data/Spline Group/Horizontal/Horizontal Spline/Spline/Points/Point.1/Position Y | <spline@bkoCZAXMCFnrFm53dRDcAr/points/_0/positiony | maxon::Float | Input | false | false | false |  |  | 0 | 
Data/Spline Group/Horizontal/Horizontal Spline/Spline/Points/Point.1/Tangent Left | <spline@bkoCZAXMCFnrFm53dRDcAr/points/_0/tangentleft | maxon::Vector2d | Input | false | false | false |  |  |  | 
Data/Spline Group/Horizontal/Horizontal Spline/Spline/Points/Point.1/Tangent Right | <spline@bkoCZAXMCFnrFm53dRDcAr/points/_0/tangentright | maxon::Vector2d | Input | false | false | false |  |  |  | 
Data/Spline Group/Horizontal/Horizontal Spline/Spline/Points/Point.2 | <spline@bkoCZAXMCFnrFm53dRDcAr/points/_1 | net.maxon.render.portbundle.splinepoint | Input | false | false | false |  |  |  | 
Data/Spline Group/Horizontal/Horizontal Spline/Spline/Points/Point.2/Break Tangent | <spline@bkoCZAXMCFnrFm53dRDcAr/points/_1/breaktangent | maxon::Bool | Input | false | false | false |  |  |  | 
Data/Spline Group/Horizontal/Horizontal Spline/Spline/Points/Point.2/Interpolation | <spline@bkoCZAXMCFnrFm53dRDcAr/points/_1/interpolation | maxon::InternedId | Input | false | false | true |  |  | spline | Spline = spline, Cubic = cubic, Linear = linear
Data/Spline Group/Horizontal/Horizontal Spline/Spline/Points/Point.2/Keep Visual Angle | <spline@bkoCZAXMCFnrFm53dRDcAr/points/_1/keepvisualangle | maxon::Bool | Input | false | false | false |  |  |  | 
Data/Spline Group/Horizontal/Horizontal Spline/Spline/Points/Point.2/Lock Angle | <spline@bkoCZAXMCFnrFm53dRDcAr/points/_1/lockangle | maxon::Bool | Input | false | false | false |  |  |  | 
Data/Spline Group/Horizontal/Horizontal Spline/Spline/Points/Point.2/Lock Length | <spline@bkoCZAXMCFnrFm53dRDcAr/points/_1/locklength | maxon::Bool | Input | false | false | false |  |  |  | 
Data/Spline Group/Horizontal/Horizontal Spline/Spline/Points/Point.2/Lock X | <spline@bkoCZAXMCFnrFm53dRDcAr/points/_1/lockx | maxon::Bool | Input | false | false | false |  |  |  | 
Data/Spline Group/Horizontal/Horizontal Spline/Spline/Points/Point.2/Lock Y | <spline@bkoCZAXMCFnrFm53dRDcAr/points/_1/locky | maxon::Bool | Input | false | false | false |  |  |  | 
Data/Spline Group/Horizontal/Horizontal Spline/Spline/Points/Point.2/Position X | <spline@bkoCZAXMCFnrFm53dRDcAr/points/_1/positionx | maxon::Float | Input | false | false | false |  |  | 0 | 
Data/Spline Group/Horizontal/Horizontal Spline/Spline/Points/Point.2/Position Y | <spline@bkoCZAXMCFnrFm53dRDcAr/points/_1/positiony | maxon::Float | Input | false | false | false |  |  | 0 | 
Data/Spline Group/Horizontal/Horizontal Spline/Spline/Points/Point.2/Tangent Left | <spline@bkoCZAXMCFnrFm53dRDcAr/points/_1/tangentleft | maxon::Vector2d | Input | false | false | false |  |  |  | 
Data/Spline Group/Horizontal/Horizontal Spline/Spline/Points/Point.2/Tangent Right | <spline@bkoCZAXMCFnrFm53dRDcAr/points/_1/tangentright | maxon::Vector2d | Input | false | false | false |  |  |  | 
Data/Spline Group/Horizontal/Horizontal Spline/Spline/Tension | <spline@bkoCZAXMCFnrFm53dRDcAr/tension | maxon::Float | Input | false | false | false |  | 1 | 1 | 
Data/Spline Group/Vertical/Vertical Details Group/Offset | <KfPTGv03CBMtD7NXUK7kwa | maxon::Float64 | Input | false | false | false |  |  | 0 | 
Data/Spline Group/Vertical/Vertical Details Group/Speed | <HfdCH6IGJh5lBoKPf1IdLc | maxon::Float64 | Input | false | false | false |  |  | 0 | 
Data/Spline Group/Vertical/Vertical Spline/Spline | <inport@D14umuujMFEnaiVRgdCILX | net.maxon.render.portbundle.spline | Input | false | true | false |  |  |  | 
Data/Spline Group/Vertical/Vertical Spline/Spline/Link End Positions | <inport@D14umuujMFEnaiVRgdCILX/linkendpositions | maxon::Bool | Input | false | false | false |  |  |  | 
Data/Spline Group/Vertical/Vertical Spline/Spline/Link End Tangents | <inport@D14umuujMFEnaiVRgdCILX/linkendtangents | maxon::Bool | Input | false | false | false |  |  |  | 
Data/Spline Group/Vertical/Vertical Spline/Spline/Max | <inport@D14umuujMFEnaiVRgdCILX/max | maxon::Vector2d | Input | false | false | false |  |  | (1,1) | 
Data/Spline Group/Vertical/Vertical Spline/Spline/Min | <inport@D14umuujMFEnaiVRgdCILX/min | maxon::Vector2d | Input | false | false | false |  |  |  | 
Data/Spline Group/Vertical/Vertical Spline/Spline/Points | <inport@D14umuujMFEnaiVRgdCILX/points | net.maxon.render.portbundle.splinepoint | Input | true | false | false |  |  |  | 
Data/Spline Group/Vertical/Vertical Spline/Spline/Points/Point.1 | <inport@D14umuujMFEnaiVRgdCILX/points/_0 | net.maxon.render.portbundle.splinepoint | Input | false | false | false |  |  |  | 
Data/Spline Group/Vertical/Vertical Spline/Spline/Points/Point.1/Break Tangent | <inport@D14umuujMFEnaiVRgdCILX/points/_0/breaktangent | maxon::Bool | Input | false | false | false |  |  |  | 
Data/Spline Group/Vertical/Vertical Spline/Spline/Points/Point.1/Interpolation | <inport@D14umuujMFEnaiVRgdCILX/points/_0/interpolation | maxon::InternedId | Input | false | false | true |  |  | spline | Spline = spline, Cubic = cubic, Linear = linear
Data/Spline Group/Vertical/Vertical Spline/Spline/Points/Point.1/Keep Visual Angle | <inport@D14umuujMFEnaiVRgdCILX/points/_0/keepvisualangle | maxon::Bool | Input | false | false | false |  |  |  | 
Data/Spline Group/Vertical/Vertical Spline/Spline/Points/Point.1/Lock Angle | <inport@D14umuujMFEnaiVRgdCILX/points/_0/lockangle | maxon::Bool | Input | false | false | false |  |  |  | 
Data/Spline Group/Vertical/Vertical Spline/Spline/Points/Point.1/Lock Length | <inport@D14umuujMFEnaiVRgdCILX/points/_0/locklength | maxon::Bool | Input | false | false | false |  |  |  | 
Data/Spline Group/Vertical/Vertical Spline/Spline/Points/Point.1/Lock X | <inport@D14umuujMFEnaiVRgdCILX/points/_0/lockx | maxon::Bool | Input | false | false | false |  |  |  | 
Data/Spline Group/Vertical/Vertical Spline/Spline/Points/Point.1/Lock Y | <inport@D14umuujMFEnaiVRgdCILX/points/_0/locky | maxon::Bool | Input | false | false | false |  |  |  | 
Data/Spline Group/Vertical/Vertical Spline/Spline/Points/Point.1/Position X | <inport@D14umuujMFEnaiVRgdCILX/points/_0/positionx | maxon::Float | Input | false | false | false |  |  | 0 | 
Data/Spline Group/Vertical/Vertical Spline/Spline/Points/Point.1/Position Y | <inport@D14umuujMFEnaiVRgdCILX/points/_0/positiony | maxon::Float | Input | false | false | false |  |  | 0 | 
Data/Spline Group/Vertical/Vertical Spline/Spline/Points/Point.1/Tangent Left | <inport@D14umuujMFEnaiVRgdCILX/points/_0/tangentleft | maxon::Vector2d | Input | false | false | false |  |  |  | 
Data/Spline Group/Vertical/Vertical Spline/Spline/Points/Point.1/Tangent Right | <inport@D14umuujMFEnaiVRgdCILX/points/_0/tangentright | maxon::Vector2d | Input | false | false | false |  |  |  | 
Data/Spline Group/Vertical/Vertical Spline/Spline/Points/Point.2 | <inport@D14umuujMFEnaiVRgdCILX/points/_2 | net.maxon.render.portbundle.splinepoint | Input | false | false | false |  |  |  | 
Data/Spline Group/Vertical/Vertical Spline/Spline/Points/Point.2/Break Tangent | <inport@D14umuujMFEnaiVRgdCILX/points/_2/breaktangent | maxon::Bool | Input | false | false | false |  |  |  | 
Data/Spline Group/Vertical/Vertical Spline/Spline/Points/Point.2/Interpolation | <inport@D14umuujMFEnaiVRgdCILX/points/_2/interpolation | maxon::InternedId | Input | false | false | true |  |  | spline | Spline = spline, Cubic = cubic, Linear = linear
Data/Spline Group/Vertical/Vertical Spline/Spline/Points/Point.2/Keep Visual Angle | <inport@D14umuujMFEnaiVRgdCILX/points/_2/keepvisualangle | maxon::Bool | Input | false | false | false |  |  |  | 
Data/Spline Group/Vertical/Vertical Spline/Spline/Points/Point.2/Lock Angle | <inport@D14umuujMFEnaiVRgdCILX/points/_2/lockangle | maxon::Bool | Input | false | false | false |  |  |  | 
Data/Spline Group/Vertical/Vertical Spline/Spline/Points/Point.2/Lock Length | <inport@D14umuujMFEnaiVRgdCILX/points/_2/locklength | maxon::Bool | Input | false | false | false |  |  |  | 
Data/Spline Group/Vertical/Vertical Spline/Spline/Points/Point.2/Lock X | <inport@D14umuujMFEnaiVRgdCILX/points/_2/lockx | maxon::Bool | Input | false | false | false |  |  |  | 
Data/Spline Group/Vertical/Vertical Spline/Spline/Points/Point.2/Lock Y | <inport@D14umuujMFEnaiVRgdCILX/points/_2/locky | maxon::Bool | Input | false | false | false |  |  |  | 
Data/Spline Group/Vertical/Vertical Spline/Spline/Points/Point.2/Position X | <inport@D14umuujMFEnaiVRgdCILX/points/_2/positionx | maxon::Float | Input | false | false | false |  |  | 0 | 
Data/Spline Group/Vertical/Vertical Spline/Spline/Points/Point.2/Position Y | <inport@D14umuujMFEnaiVRgdCILX/points/_2/positiony | maxon::Float | Input | false | false | false |  |  | 0 | 
Data/Spline Group/Vertical/Vertical Spline/Spline/Points/Point.2/Tangent Left | <inport@D14umuujMFEnaiVRgdCILX/points/_2/tangentleft | maxon::Vector2d | Input | false | false | false |  |  |  | 
Data/Spline Group/Vertical/Vertical Spline/Spline/Points/Point.2/Tangent Right | <inport@D14umuujMFEnaiVRgdCILX/points/_2/tangentright | maxon::Vector2d | Input | false | false | false |  |  |  | 
Data/Spline Group/Vertical/Vertical Spline/Spline/Points/Point.3 | <inport@D14umuujMFEnaiVRgdCILX/points/_3 | net.maxon.render.portbundle.splinepoint | Input | false | false | false |  |  |  | 
Data/Spline Group/Vertical/Vertical Spline/Spline/Points/Point.3/Break Tangent | <inport@D14umuujMFEnaiVRgdCILX/points/_3/breaktangent | maxon::Bool | Input | false | false | false |  |  |  | 
Data/Spline Group/Vertical/Vertical Spline/Spline/Points/Point.3/Interpolation | <inport@D14umuujMFEnaiVRgdCILX/points/_3/interpolation | maxon::InternedId | Input | false | false | true |  |  | spline | Spline = spline, Cubic = cubic, Linear = linear
Data/Spline Group/Vertical/Vertical Spline/Spline/Points/Point.3/Keep Visual Angle | <inport@D14umuujMFEnaiVRgdCILX/points/_3/keepvisualangle | maxon::Bool | Input | false | false | false |  |  |  | 
Data/Spline Group/Vertical/Vertical Spline/Spline/Points/Point.3/Lock Angle | <inport@D14umuujMFEnaiVRgdCILX/points/_3/lockangle | maxon::Bool | Input | false | false | false |  |  |  | 
Data/Spline Group/Vertical/Vertical Spline/Spline/Points/Point.3/Lock Length | <inport@D14umuujMFEnaiVRgdCILX/points/_3/locklength | maxon::Bool | Input | false | false | false |  |  |  | 
Data/Spline Group/Vertical/Vertical Spline/Spline/Points/Point.3/Lock X | <inport@D14umuujMFEnaiVRgdCILX/points/_3/lockx | maxon::Bool | Input | false | false | false |  |  |  | 
Data/Spline Group/Vertical/Vertical Spline/Spline/Points/Point.3/Lock Y | <inport@D14umuujMFEnaiVRgdCILX/points/_3/locky | maxon::Bool | Input | false | false | false |  |  |  | 
Data/Spline Group/Vertical/Vertical Spline/Spline/Points/Point.3/Position X | <inport@D14umuujMFEnaiVRgdCILX/points/_3/positionx | maxon::Float | Input | false | false | false |  |  | 0 | 
Data/Spline Group/Vertical/Vertical Spline/Spline/Points/Point.3/Position Y | <inport@D14umuujMFEnaiVRgdCILX/points/_3/positiony | maxon::Float | Input | false | false | false |  |  | 0 | 
Data/Spline Group/Vertical/Vertical Spline/Spline/Points/Point.3/Tangent Left | <inport@D14umuujMFEnaiVRgdCILX/points/_3/tangentleft | maxon::Vector2d | Input | false | false | false |  |  |  | 
Data/Spline Group/Vertical/Vertical Spline/Spline/Points/Point.3/Tangent Right | <inport@D14umuujMFEnaiVRgdCILX/points/_3/tangentright | maxon::Vector2d | Input | false | false | false |  |  |  | 
Data/Spline Group/Vertical/Vertical Spline/Spline/Points/Point.4 | <inport@D14umuujMFEnaiVRgdCILX/points/_4 | net.maxon.render.portbundle.splinepoint | Input | false | false | false |  |  |  | 
Data/Spline Group/Vertical/Vertical Spline/Spline/Points/Point.4/Break Tangent | <inport@D14umuujMFEnaiVRgdCILX/points/_4/breaktangent | maxon::Bool | Input | false | false | false |  |  |  | 
Data/Spline Group/Vertical/Vertical Spline/Spline/Points/Point.4/Interpolation | <inport@D14umuujMFEnaiVRgdCILX/points/_4/interpolation | maxon::InternedId | Input | false | false | true |  |  | spline | Spline = spline, Cubic = cubic, Linear = linear
Data/Spline Group/Vertical/Vertical Spline/Spline/Points/Point.4/Keep Visual Angle | <inport@D14umuujMFEnaiVRgdCILX/points/_4/keepvisualangle | maxon::Bool | Input | false | false | false |  |  |  | 
Data/Spline Group/Vertical/Vertical Spline/Spline/Points/Point.4/Lock Angle | <inport@D14umuujMFEnaiVRgdCILX/points/_4/lockangle | maxon::Bool | Input | false | false | false |  |  |  | 
Data/Spline Group/Vertical/Vertical Spline/Spline/Points/Point.4/Lock Length | <inport@D14umuujMFEnaiVRgdCILX/points/_4/locklength | maxon::Bool | Input | false | false | false |  |  |  | 
Data/Spline Group/Vertical/Vertical Spline/Spline/Points/Point.4/Lock X | <inport@D14umuujMFEnaiVRgdCILX/points/_4/lockx | maxon::Bool | Input | false | false | false |  |  |  | 
Data/Spline Group/Vertical/Vertical Spline/Spline/Points/Point.4/Lock Y | <inport@D14umuujMFEnaiVRgdCILX/points/_4/locky | maxon::Bool | Input | false | false | false |  |  |  | 
Data/Spline Group/Vertical/Vertical Spline/Spline/Points/Point.4/Position X | <inport@D14umuujMFEnaiVRgdCILX/points/_4/positionx | maxon::Float | Input | false | false | false |  |  | 0 | 
Data/Spline Group/Vertical/Vertical Spline/Spline/Points/Point.4/Position Y | <inport@D14umuujMFEnaiVRgdCILX/points/_4/positiony | maxon::Float | Input | false | false | false |  |  | 0 | 
Data/Spline Group/Vertical/Vertical Spline/Spline/Points/Point.4/Tangent Left | <inport@D14umuujMFEnaiVRgdCILX/points/_4/tangentleft | maxon::Vector2d | Input | false | false | false |  |  |  | 
Data/Spline Group/Vertical/Vertical Spline/Spline/Points/Point.4/Tangent Right | <inport@D14umuujMFEnaiVRgdCILX/points/_4/tangentright | maxon::Vector2d | Input | false | false | false |  |  |  | 
Data/Spline Group/Vertical/Vertical Spline/Spline/Points/Point.5 | <inport@D14umuujMFEnaiVRgdCILX/points/_5 | net.maxon.render.portbundle.splinepoint | Input | false | false | false |  |  |  | 
Data/Spline Group/Vertical/Vertical Spline/Spline/Points/Point.5/Break Tangent | <inport@D14umuujMFEnaiVRgdCILX/points/_5/breaktangent | maxon::Bool | Input | false | false | false |  |  |  | 
Data/Spline Group/Vertical/Vertical Spline/Spline/Points/Point.5/Interpolation | <inport@D14umuujMFEnaiVRgdCILX/points/_5/interpolation | maxon::InternedId | Input | false | false | true |  |  | spline | Spline = spline, Cubic = cubic, Linear = linear
Data/Spline Group/Vertical/Vertical Spline/Spline/Points/Point.5/Keep Visual Angle | <inport@D14umuujMFEnaiVRgdCILX/points/_5/keepvisualangle | maxon::Bool | Input | false | false | false |  |  |  | 
Data/Spline Group/Vertical/Vertical Spline/Spline/Points/Point.5/Lock Angle | <inport@D14umuujMFEnaiVRgdCILX/points/_5/lockangle | maxon::Bool | Input | false | false | false |  |  |  | 
Data/Spline Group/Vertical/Vertical Spline/Spline/Points/Point.5/Lock Length | <inport@D14umuujMFEnaiVRgdCILX/points/_5/locklength | maxon::Bool | Input | false | false | false |  |  |  | 
Data/Spline Group/Vertical/Vertical Spline/Spline/Points/Point.5/Lock X | <inport@D14umuujMFEnaiVRgdCILX/points/_5/lockx | maxon::Bool | Input | false | false | false |  |  |  | 
Data/Spline Group/Vertical/Vertical Spline/Spline/Points/Point.5/Lock Y | <inport@D14umuujMFEnaiVRgdCILX/points/_5/locky | maxon::Bool | Input | false | false | false |  |  |  | 
Data/Spline Group/Vertical/Vertical Spline/Spline/Points/Point.5/Position X | <inport@D14umuujMFEnaiVRgdCILX/points/_5/positionx | maxon::Float | Input | false | false | false |  |  | 0 | 
Data/Spline Group/Vertical/Vertical Spline/Spline/Points/Point.5/Position Y | <inport@D14umuujMFEnaiVRgdCILX/points/_5/positiony | maxon::Float | Input | false | false | false |  |  | 0 | 
Data/Spline Group/Vertical/Vertical Spline/Spline/Points/Point.5/Tangent Left | <inport@D14umuujMFEnaiVRgdCILX/points/_5/tangentleft | maxon::Vector2d | Input | false | false | false |  |  |  | 
Data/Spline Group/Vertical/Vertical Spline/Spline/Points/Point.5/Tangent Right | <inport@D14umuujMFEnaiVRgdCILX/points/_5/tangentright | maxon::Vector2d | Input | false | false | false |  |  |  | 
Data/Spline Group/Vertical/Vertical Spline/Spline/Points/Point.6 | <inport@D14umuujMFEnaiVRgdCILX/points/_6 | net.maxon.render.portbundle.splinepoint | Input | false | false | false |  |  |  | 
Data/Spline Group/Vertical/Vertical Spline/Spline/Points/Point.6/Break Tangent | <inport@D14umuujMFEnaiVRgdCILX/points/_6/breaktangent | maxon::Bool | Input | false | false | false |  |  |  | 
Data/Spline Group/Vertical/Vertical Spline/Spline/Points/Point.6/Interpolation | <inport@D14umuujMFEnaiVRgdCILX/points/_6/interpolation | maxon::InternedId | Input | false | false | true |  |  | spline | Spline = spline, Cubic = cubic, Linear = linear
Data/Spline Group/Vertical/Vertical Spline/Spline/Points/Point.6/Keep Visual Angle | <inport@D14umuujMFEnaiVRgdCILX/points/_6/keepvisualangle | maxon::Bool | Input | false | false | false |  |  |  | 
Data/Spline Group/Vertical/Vertical Spline/Spline/Points/Point.6/Lock Angle | <inport@D14umuujMFEnaiVRgdCILX/points/_6/lockangle | maxon::Bool | Input | false | false | false |  |  |  | 
Data/Spline Group/Vertical/Vertical Spline/Spline/Points/Point.6/Lock Length | <inport@D14umuujMFEnaiVRgdCILX/points/_6/locklength | maxon::Bool | Input | false | false | false |  |  |  | 
Data/Spline Group/Vertical/Vertical Spline/Spline/Points/Point.6/Lock X | <inport@D14umuujMFEnaiVRgdCILX/points/_6/lockx | maxon::Bool | Input | false | false | false |  |  |  | 
Data/Spline Group/Vertical/Vertical Spline/Spline/Points/Point.6/Lock Y | <inport@D14umuujMFEnaiVRgdCILX/points/_6/locky | maxon::Bool | Input | false | false | false |  |  |  | 
Data/Spline Group/Vertical/Vertical Spline/Spline/Points/Point.6/Position X | <inport@D14umuujMFEnaiVRgdCILX/points/_6/positionx | maxon::Float | Input | false | false | false |  |  | 0 | 
Data/Spline Group/Vertical/Vertical Spline/Spline/Points/Point.6/Position Y | <inport@D14umuujMFEnaiVRgdCILX/points/_6/positiony | maxon::Float | Input | false | false | false |  |  | 0 | 
Data/Spline Group/Vertical/Vertical Spline/Spline/Points/Point.6/Tangent Left | <inport@D14umuujMFEnaiVRgdCILX/points/_6/tangentleft | maxon::Vector2d | Input | false | false | false |  |  |  | 
Data/Spline Group/Vertical/Vertical Spline/Spline/Points/Point.6/Tangent Right | <inport@D14umuujMFEnaiVRgdCILX/points/_6/tangentright | maxon::Vector2d | Input | false | false | false |  |  |  | 
Data/Spline Group/Vertical/Vertical Spline/Spline/Points/Point.7 | <inport@D14umuujMFEnaiVRgdCILX/points/_7 | net.maxon.render.portbundle.splinepoint | Input | false | false | false |  |  |  | 
Data/Spline Group/Vertical/Vertical Spline/Spline/Points/Point.7/Break Tangent | <inport@D14umuujMFEnaiVRgdCILX/points/_7/breaktangent | maxon::Bool | Input | false | false | false |  |  |  | 
Data/Spline Group/Vertical/Vertical Spline/Spline/Points/Point.7/Interpolation | <inport@D14umuujMFEnaiVRgdCILX/points/_7/interpolation | maxon::InternedId | Input | false | false | true |  |  | spline | Spline = spline, Cubic = cubic, Linear = linear
Data/Spline Group/Vertical/Vertical Spline/Spline/Points/Point.7/Keep Visual Angle | <inport@D14umuujMFEnaiVRgdCILX/points/_7/keepvisualangle | maxon::Bool | Input | false | false | false |  |  |  | 
Data/Spline Group/Vertical/Vertical Spline/Spline/Points/Point.7/Lock Angle | <inport@D14umuujMFEnaiVRgdCILX/points/_7/lockangle | maxon::Bool | Input | false | false | false |  |  |  | 
Data/Spline Group/Vertical/Vertical Spline/Spline/Points/Point.7/Lock Length | <inport@D14umuujMFEnaiVRgdCILX/points/_7/locklength | maxon::Bool | Input | false | false | false |  |  |  | 
Data/Spline Group/Vertical/Vertical Spline/Spline/Points/Point.7/Lock X | <inport@D14umuujMFEnaiVRgdCILX/points/_7/lockx | maxon::Bool | Input | false | false | false |  |  |  | 
Data/Spline Group/Vertical/Vertical Spline/Spline/Points/Point.7/Lock Y | <inport@D14umuujMFEnaiVRgdCILX/points/_7/locky | maxon::Bool | Input | false | false | false |  |  |  | 
Data/Spline Group/Vertical/Vertical Spline/Spline/Points/Point.7/Position X | <inport@D14umuujMFEnaiVRgdCILX/points/_7/positionx | maxon::Float | Input | false | false | false |  |  | 0 | 
Data/Spline Group/Vertical/Vertical Spline/Spline/Points/Point.7/Position Y | <inport@D14umuujMFEnaiVRgdCILX/points/_7/positiony | maxon::Float | Input | false | false | false |  |  | 0 | 
Data/Spline Group/Vertical/Vertical Spline/Spline/Points/Point.7/Tangent Left | <inport@D14umuujMFEnaiVRgdCILX/points/_7/tangentleft | maxon::Vector2d | Input | false | false | false |  |  |  | 
Data/Spline Group/Vertical/Vertical Spline/Spline/Points/Point.7/Tangent Right | <inport@D14umuujMFEnaiVRgdCILX/points/_7/tangentright | maxon::Vector2d | Input | false | false | false |  |  |  | 
Data/Spline Group/Vertical/Vertical Spline/Spline/Points/Point.8 | <inport@D14umuujMFEnaiVRgdCILX/points/_1 | net.maxon.render.portbundle.splinepoint | Input | false | false | false |  |  |  | 
Data/Spline Group/Vertical/Vertical Spline/Spline/Points/Point.8/Break Tangent | <inport@D14umuujMFEnaiVRgdCILX/points/_1/breaktangent | maxon::Bool | Input | false | false | false |  |  |  | 
Data/Spline Group/Vertical/Vertical Spline/Spline/Points/Point.8/Interpolation | <inport@D14umuujMFEnaiVRgdCILX/points/_1/interpolation | maxon::InternedId | Input | false | false | true |  |  | spline | Spline = spline, Cubic = cubic, Linear = linear
Data/Spline Group/Vertical/Vertical Spline/Spline/Points/Point.8/Keep Visual Angle | <inport@D14umuujMFEnaiVRgdCILX/points/_1/keepvisualangle | maxon::Bool | Input | false | false | false |  |  |  | 
Data/Spline Group/Vertical/Vertical Spline/Spline/Points/Point.8/Lock Angle | <inport@D14umuujMFEnaiVRgdCILX/points/_1/lockangle | maxon::Bool | Input | false | false | false |  |  |  | 
Data/Spline Group/Vertical/Vertical Spline/Spline/Points/Point.8/Lock Length | <inport@D14umuujMFEnaiVRgdCILX/points/_1/locklength | maxon::Bool | Input | false | false | false |  |  |  | 
Data/Spline Group/Vertical/Vertical Spline/Spline/Points/Point.8/Lock X | <inport@D14umuujMFEnaiVRgdCILX/points/_1/lockx | maxon::Bool | Input | false | false | false |  |  |  | 
Data/Spline Group/Vertical/Vertical Spline/Spline/Points/Point.8/Lock Y | <inport@D14umuujMFEnaiVRgdCILX/points/_1/locky | maxon::Bool | Input | false | false | false |  |  |  | 
Data/Spline Group/Vertical/Vertical Spline/Spline/Points/Point.8/Position X | <inport@D14umuujMFEnaiVRgdCILX/points/_1/positionx | maxon::Float | Input | false | false | false |  |  | 0 | 
Data/Spline Group/Vertical/Vertical Spline/Spline/Points/Point.8/Position Y | <inport@D14umuujMFEnaiVRgdCILX/points/_1/positiony | maxon::Float | Input | false | false | false |  |  | 0 | 
Data/Spline Group/Vertical/Vertical Spline/Spline/Points/Point.8/Tangent Left | <inport@D14umuujMFEnaiVRgdCILX/points/_1/tangentleft | maxon::Vector2d | Input | false | false | false |  |  |  | 
Data/Spline Group/Vertical/Vertical Spline/Spline/Points/Point.8/Tangent Right | <inport@D14umuujMFEnaiVRgdCILX/points/_1/tangentright | maxon::Vector2d | Input | false | false | false |  |  |  | 
Data/Spline Group/Vertical/Vertical Spline/Spline/Tension | <inport@D14umuujMFEnaiVRgdCILX/tension | maxon::Float | Input | false | false | false |  | 1 | 1 | 
Graph/Chart/Align | <IhkNjvlSHZ9pI0jXQLAtHh | maxon::Int64 | Input | false | false | true |  |  | 1 | Left = 0, Middle = 1, Right = 2
Graph/Chart/Angle End | <CVlnDL9nP9vuyPE1HTbi9W | maxon::Float64 | Input | false | false | false |  | 6.283 | 6.283 | 
Graph/Chart/Angle Start | <Ls_BkLF9NpVn$nDq5OD_cW | maxon::Float64 | Input | false | false | false |  | 6.283 |  | 
Graph/Chart/Close | <IhKnwmZ_PFNoqvB5nd44Uf | maxon::Bool | Input | false | false | false |  |  |  | 
Graph/Chart/Expand Group/H.Scale | <bqJngIE6INOr9DBG7gpSlA | maxon::Float64 | Input | false | false | false |  |  | 1 | 
Graph/Chart/Expand Group/Height | <G0FJBKlvIpsoZ$zYlTSxnA | maxon::Float64 | Input | false | false | false |  |  | 5 | 
Graph/Chart/Expand Group/Rounding | <e91nkK_YI9mub0kz1v5q0Z | maxon::Float64 | Input | false | false | false |  |  | 0 | 
Graph/Chart/Expand Group/W.Expand | <ToJJUX9IAhCrobVxo40wHF | maxon::Float64 | Input | false | false | false |  |  | 0 | 
Graph/Chart/Gap | <f4PGz$NIPtvo7OoMID0tpV | maxon::Float64 | Input | false | false | false |  |  | 0 | 
Graph/Chart/Height | <WL8KMuCGPFsqSb8aJq_I_D | maxon::Float64 | Input | false | false | false |  |  | 100 | 
Graph/Chart/Inner Radius | <VvcuTxgeGljqZRHBO$xW6g | maxon::Float64 | Input | false | false | false |  |  | 0 | 
Graph/Chart/Line Mode | <Gwkj$IboL1sjuJW5Rxyb1B | maxon::Bool | Input | false | false | false |  |  |  | 
Graph/Chart/Output | <GUriL$IzCtHuonrpQ50eeD | maxon::Int64 | Input | false | false | true |  |  | 3 | Graph = 3, Maximum = 4, Rectangle = 0, Circle = 1, Line = 2
Graph/Chart/Plane | <HGBy8nXlFZIgQ_upNJBy6b | maxon::Int64 | Input | false | false | true |  |  |  | XY = 0, ZY = 1, XZ = 2
Graph/Chart/Radius | <M9nGFpf3Ftyud178TLRZTi | maxon::Float64 | Input | false | false | false |  |  | 200 | 
Graph/Chart/Rotation   | <VsuXNGo5OZbpXlHbOFUAA6 | maxon::Float64 | Input | false | false | false | 2 |  | 0 | 
Graph/Chart/Rounding | <CWvusGUdGhYjTUgS2QRRWZ | maxon::Float64 | Input | false | false | false |  |  | 0 | 
Graph/Chart/Shift | <FUauHqg1JZcnXiTZkk8wVY | maxon::Float64 | Input | false | false | false |  |  | 1 | 
Graph/Chart/Sides        | <HKA6UQEAHJQmhNY3gRBKm5 | maxon::Float64 | Input | false | false | false | 2 |  | 24 | 
Graph/Chart/Spacing Group/Gap               | <WKdakQ0yO1ivRgkmhteFOj | maxon::Float64 | Input | false | false | false |  | 6.283 |  | 
Graph/Chart/Spacing Group/Parallel | <EnBobc3DMRUhnMsCdKUDhX | maxon::Bool | Input | false | false | false |  |  |  | 
Graph/Chart/V.Align     | <GNp0HFfGL5gpHxDsiNgTFq | maxon::Float64 | Input | false | false | false |  |  | 0 | 
Graph/Chart/Width | <SsqSJ$MrCFPjCg3ynzwOAE | maxon::Float64 | Input | false | false | false |  |  | 400 | 
Graph/Count | <fTEfeTwXCFprC45ybvmu7A | maxon::Int64 | Input | false | false | false |  | 99999999 | 100 | 
Graph/Type | <HywgMSlpKtghgK9SaTIYWD | maxon::Int64 | Input | false | false | true |  |  | 2 | Bar = 2, Pie = 3, Step = 1, Line = 0
Modify Data/Data Multiplier Spline/Data Multiplier | <inport@PAwpgyJDBlOuLsqkqpMZEk | net.maxon.render.portbundle.spline | Input | false | true | false |  |  |  | 
Modify Data/Data Multiplier Spline/Data Multiplier/Link End Positions | <inport@PAwpgyJDBlOuLsqkqpMZEk/linkendpositions | maxon::Bool | Input | false | false | false |  |  |  | 
Modify Data/Data Multiplier Spline/Data Multiplier/Link End Tangents | <inport@PAwpgyJDBlOuLsqkqpMZEk/linkendtangents | maxon::Bool | Input | false | false | false |  |  |  | 
Modify Data/Data Multiplier Spline/Data Multiplier/Max | <inport@PAwpgyJDBlOuLsqkqpMZEk/max | maxon::Vector2d | Input | false | false | false |  |  | (1,1) | 
Modify Data/Data Multiplier Spline/Data Multiplier/Min | <inport@PAwpgyJDBlOuLsqkqpMZEk/min | maxon::Vector2d | Input | false | false | false |  |  |  | 
Modify Data/Data Multiplier Spline/Data Multiplier/Points | <inport@PAwpgyJDBlOuLsqkqpMZEk/points | net.maxon.render.portbundle.splinepoint | Input | true | false | false |  |  |  | 
Modify Data/Data Multiplier Spline/Data Multiplier/Points/Point.1 | <inport@PAwpgyJDBlOuLsqkqpMZEk/points/_0 | net.maxon.render.portbundle.splinepoint | Input | false | false | false |  |  |  | 
Modify Data/Data Multiplier Spline/Data Multiplier/Points/Point.1/Break Tangent | <inport@PAwpgyJDBlOuLsqkqpMZEk/points/_0/breaktangent | maxon::Bool | Input | false | false | false |  |  |  | 
Modify Data/Data Multiplier Spline/Data Multiplier/Points/Point.1/Interpolation | <inport@PAwpgyJDBlOuLsqkqpMZEk/points/_0/interpolation | maxon::InternedId | Input | false | false | true |  |  | spline | Spline = spline, Cubic = cubic, Linear = linear
Modify Data/Data Multiplier Spline/Data Multiplier/Points/Point.1/Keep Visual Angle | <inport@PAwpgyJDBlOuLsqkqpMZEk/points/_0/keepvisualangle | maxon::Bool | Input | false | false | false |  |  |  | 
Modify Data/Data Multiplier Spline/Data Multiplier/Points/Point.1/Lock Angle | <inport@PAwpgyJDBlOuLsqkqpMZEk/points/_0/lockangle | maxon::Bool | Input | false | false | false |  |  |  | 
Modify Data/Data Multiplier Spline/Data Multiplier/Points/Point.1/Lock Length | <inport@PAwpgyJDBlOuLsqkqpMZEk/points/_0/locklength | maxon::Bool | Input | false | false | false |  |  |  | 
Modify Data/Data Multiplier Spline/Data Multiplier/Points/Point.1/Lock X | <inport@PAwpgyJDBlOuLsqkqpMZEk/points/_0/lockx | maxon::Bool | Input | false | false | false |  |  |  | 
Modify Data/Data Multiplier Spline/Data Multiplier/Points/Point.1/Lock Y | <inport@PAwpgyJDBlOuLsqkqpMZEk/points/_0/locky | maxon::Bool | Input | false | false | false |  |  |  | 
Modify Data/Data Multiplier Spline/Data Multiplier/Points/Point.1/Position X | <inport@PAwpgyJDBlOuLsqkqpMZEk/points/_0/positionx | maxon::Float | Input | false | false | false |  |  | 0 | 
Modify Data/Data Multiplier Spline/Data Multiplier/Points/Point.1/Position Y | <inport@PAwpgyJDBlOuLsqkqpMZEk/points/_0/positiony | maxon::Float | Input | false | false | false |  |  | 0 | 
Modify Data/Data Multiplier Spline/Data Multiplier/Points/Point.1/Tangent Left | <inport@PAwpgyJDBlOuLsqkqpMZEk/points/_0/tangentleft | maxon::Vector2d | Input | false | false | false |  |  |  | 
Modify Data/Data Multiplier Spline/Data Multiplier/Points/Point.1/Tangent Right | <inport@PAwpgyJDBlOuLsqkqpMZEk/points/_0/tangentright | maxon::Vector2d | Input | false | false | false |  |  |  | 
Modify Data/Data Multiplier Spline/Data Multiplier/Points/Point.2 | <inport@PAwpgyJDBlOuLsqkqpMZEk/points/_2 | net.maxon.render.portbundle.splinepoint | Input | false | false | false |  |  |  | 
Modify Data/Data Multiplier Spline/Data Multiplier/Points/Point.2/Break Tangent | <inport@PAwpgyJDBlOuLsqkqpMZEk/points/_2/breaktangent | maxon::Bool | Input | false | false | false |  |  |  | 
Modify Data/Data Multiplier Spline/Data Multiplier/Points/Point.2/Interpolation | <inport@PAwpgyJDBlOuLsqkqpMZEk/points/_2/interpolation | maxon::InternedId | Input | false | false | true |  |  | spline | Spline = spline, Cubic = cubic, Linear = linear
Modify Data/Data Multiplier Spline/Data Multiplier/Points/Point.2/Keep Visual Angle | <inport@PAwpgyJDBlOuLsqkqpMZEk/points/_2/keepvisualangle | maxon::Bool | Input | false | false | false |  |  |  | 
Modify Data/Data Multiplier Spline/Data Multiplier/Points/Point.2/Lock Angle | <inport@PAwpgyJDBlOuLsqkqpMZEk/points/_2/lockangle | maxon::Bool | Input | false | false | false |  |  |  | 
Modify Data/Data Multiplier Spline/Data Multiplier/Points/Point.2/Lock Length | <inport@PAwpgyJDBlOuLsqkqpMZEk/points/_2/locklength | maxon::Bool | Input | false | false | false |  |  |  | 
Modify Data/Data Multiplier Spline/Data Multiplier/Points/Point.2/Lock X | <inport@PAwpgyJDBlOuLsqkqpMZEk/points/_2/lockx | maxon::Bool | Input | false | false | false |  |  |  | 
Modify Data/Data Multiplier Spline/Data Multiplier/Points/Point.2/Lock Y | <inport@PAwpgyJDBlOuLsqkqpMZEk/points/_2/locky | maxon::Bool | Input | false | false | false |  |  |  | 
Modify Data/Data Multiplier Spline/Data Multiplier/Points/Point.2/Position X | <inport@PAwpgyJDBlOuLsqkqpMZEk/points/_2/positionx | maxon::Float | Input | false | false | false |  |  | 0 | 
Modify Data/Data Multiplier Spline/Data Multiplier/Points/Point.2/Position Y | <inport@PAwpgyJDBlOuLsqkqpMZEk/points/_2/positiony | maxon::Float | Input | false | false | false |  |  | 0 | 
Modify Data/Data Multiplier Spline/Data Multiplier/Points/Point.2/Tangent Left | <inport@PAwpgyJDBlOuLsqkqpMZEk/points/_2/tangentleft | maxon::Vector2d | Input | false | false | false |  |  |  | 
Modify Data/Data Multiplier Spline/Data Multiplier/Points/Point.2/Tangent Right | <inport@PAwpgyJDBlOuLsqkqpMZEk/points/_2/tangentright | maxon::Vector2d | Input | false | false | false |  |  |  | 
Modify Data/Data Multiplier Spline/Data Multiplier/Points/Point.3 | <inport@PAwpgyJDBlOuLsqkqpMZEk/points/_1 | net.maxon.render.portbundle.splinepoint | Input | false | false | false |  |  |  | 
Modify Data/Data Multiplier Spline/Data Multiplier/Points/Point.3/Break Tangent | <inport@PAwpgyJDBlOuLsqkqpMZEk/points/_1/breaktangent | maxon::Bool | Input | false | false | false |  |  |  | 
Modify Data/Data Multiplier Spline/Data Multiplier/Points/Point.3/Interpolation | <inport@PAwpgyJDBlOuLsqkqpMZEk/points/_1/interpolation | maxon::InternedId | Input | false | false | true |  |  | spline | Spline = spline, Cubic = cubic, Linear = linear
Modify Data/Data Multiplier Spline/Data Multiplier/Points/Point.3/Keep Visual Angle | <inport@PAwpgyJDBlOuLsqkqpMZEk/points/_1/keepvisualangle | maxon::Bool | Input | false | false | false |  |  |  | 
Modify Data/Data Multiplier Spline/Data Multiplier/Points/Point.3/Lock Angle | <inport@PAwpgyJDBlOuLsqkqpMZEk/points/_1/lockangle | maxon::Bool | Input | false | false | false |  |  |  | 
Modify Data/Data Multiplier Spline/Data Multiplier/Points/Point.3/Lock Length | <inport@PAwpgyJDBlOuLsqkqpMZEk/points/_1/locklength | maxon::Bool | Input | false | false | false |  |  |  | 
Modify Data/Data Multiplier Spline/Data Multiplier/Points/Point.3/Lock X | <inport@PAwpgyJDBlOuLsqkqpMZEk/points/_1/lockx | maxon::Bool | Input | false | false | false |  |  |  | 
Modify Data/Data Multiplier Spline/Data Multiplier/Points/Point.3/Lock Y | <inport@PAwpgyJDBlOuLsqkqpMZEk/points/_1/locky | maxon::Bool | Input | false | false | false |  |  |  | 
Modify Data/Data Multiplier Spline/Data Multiplier/Points/Point.3/Position X | <inport@PAwpgyJDBlOuLsqkqpMZEk/points/_1/positionx | maxon::Float | Input | false | false | false |  |  | 0 | 
Modify Data/Data Multiplier Spline/Data Multiplier/Points/Point.3/Position Y | <inport@PAwpgyJDBlOuLsqkqpMZEk/points/_1/positiony | maxon::Float | Input | false | false | false |  |  | 0 | 
Modify Data/Data Multiplier Spline/Data Multiplier/Points/Point.3/Tangent Left | <inport@PAwpgyJDBlOuLsqkqpMZEk/points/_1/tangentleft | maxon::Vector2d | Input | false | false | false |  |  |  | 
Modify Data/Data Multiplier Spline/Data Multiplier/Points/Point.3/Tangent Right | <inport@PAwpgyJDBlOuLsqkqpMZEk/points/_1/tangentright | maxon::Vector2d | Input | false | false | false |  |  |  | 
Modify Data/Data Multiplier Spline/Data Multiplier/Tension | <inport@PAwpgyJDBlOuLsqkqpMZEk/tension | maxon::Float | Input | false | false | false |  | 1 | 1 | 
Modify Data/Flip | <GRwjTztlEBbpZ3iIQKgv7s | maxon::Bool | Input | false | false | false |  |  |  | 
Modify Data/Offset Index | <HZAbbp85AJnkuUIGGxHhTV | maxon::Float64 | Input | false | false | false |  |  | 0 | 
Modify Data/Reverse | <d0vWTRt$PZXg_jRobjZGVR | maxon::Bool | Input | false | false | false |  |  |  | 
Modify Data/Shuffle Seed | <H7o19njQLFRmZ4aXt4dEtu | maxon::Int64 | Input | false | false | false |  | 99999999 | 12345 | 
Modify Data/Sort By | <GIvQxfgsEFlspiCRXo7E14 | maxon::Int64 | Input | false | false | true |  |  | 10 | None = 10, Width = 0, Height = 1, Shuffle = 3
Outputs/Geometry | >geometryout | maxon::GeometryObject | Output | false | false | false |  |  |  | 

