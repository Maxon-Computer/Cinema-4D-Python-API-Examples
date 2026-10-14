# Node Template: Uber Material

- **Node Space ID:** `net.maxon.nodespace.standard`
- **Template ID:** `net.maxon.node.ubermaterial.node`
- **Template Name:** `Uber Material`

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
Bump/3D Epsilon | <epsilon3d@Z2FMkdjpHVtkkWBjmvSYRr | maxon::Float64 | Input | false | false | false | -1 | 1 | 1 | 
Bump/Strength | <strength@fghxMJqtAR$kJrJq7SpoTo | maxon::Float64 | Input | false | false | false | -1 | 1 | 1 | 
Bump/UV Epsilon | <epsilonuv@rt5Oz77UP9ft$NT$NhJoPp | maxon::Float64 | Input | false | false | false | -1 | 1 | 1 | 
Bump/Value | <color@sCehtnSsFpSrpHP1YK80kr | maxon::Color64 | Input | false | false | false |  |  |  | 
Channels/Bump | <bIcO7O2WDRGjXeKlYkhrms | maxon::Bool | Input | false | false | false |  |  |  | 
Channels/Coating | <j49Hqh6cNJOnwz6_YzLoHT | maxon::Bool | Input | false | false | false |  |  | false | 
Channels/Diffuse | <pAAkn8tfFpZmCB5gh_W2NM | maxon::Bool | Input | false | false | false |  |  | true | 
Channels/Displacement | <FGh8stFaDlBgoGWYn797wb | maxon::Bool | Input | false | false | false |  |  |  | 
Channels/Emission | <sTJKCSEgCp0qZ5EyUueGtS | maxon::Bool | Input | false | false | false |  |  | false | 
Channels/Normal | <F4LV6t7UPFkjHGqeDDYn32 | maxon::Bool | Input | false | false | false |  |  |  | 
Channels/Opacity | <FRwneP4bF9grsPzYmhvD5u | maxon::Bool | Input | false | false | false |  |  |  | 
Channels/Reflection | <bV9mCnVWAZVpI2A7935GSQ | maxon::Bool | Input | false | false | false |  |  | true | 
Channels/Transparency | <46ICwiQAAtIkHV5Obv6z0T | maxon::Bool | Input | false | false | false |  |  | false | 
Coating/3D Epsilon | <epsilon3d@hJHBscRSClVut9V9dDyC5o | maxon::Float64 | Input | false | false | false | -1 | 1 | 1 | 
Coating/Bump Map | <color@2Tgx1FjIJhuuv5moI2bt0q | maxon::Color64 | Input | false | false | false |  |  |  | 
Coating/Bump Strength | <strength@9iJI2qL5INJnCPeY7hNAKq | maxon::Float64 | Input | false | false | false | -1 | 1 | 1 | 
Coating/Color | <AxZ9Vzm2LNbq9vdcGR1oBI | maxon::Color64 | Input | false | false | false |  |  | (1,1,1) | 
Coating/Diffuse Tint | <HCiYzJ4iCxfgj2fyCRaDuM | maxon::Float64 | Input | false | false | false |  | 1 |  | 
Coating/Flip X | <flipx@lxtetZmGCNtn8BIwltqUip | maxon::Bool | Input | false | false | false |  |  |  | 
Coating/Flip Y | <flipy@lJ7RsfAKEFWmUg_SqyKfmo | maxon::Bool | Input | false | false | false |  |  | true | 
Coating/Flip Z | <flipz@0JPCh2yIAFfkTwPcgEMdop | maxon::Bool | Input | false | false | false |  |  |  | 
Coating/IOR | <dielectricior@2E9h2TD8BdcmD6okZqYkCb | maxon::Float64 | Input | false | false | false | 1 | 5 | 1.5 | 
Coating/Intensity | <dsW6bbayC5WpbYuxwDj7YM | maxon::Float64 | Input | false | false | false |  | 10000000 | 1 | 
Coating/Normal | <RhWVmtpVB98q_hkxw5aybr@QBensg3DA96mmjMHFxskLr | maxon::Vector64 | Input | false | false | false |  |  |  | 
Coating/Normal Map | <color@r95NiF2XEtdsxshLr_X0Fr | maxon::Color64 | Input | false | false | false |  |  |  | 
Coating/Normal Mode | <y4$lVjgAFxwmRj5E8n34wo | maxon::Int64 | Input | false | false | true |  |  |  | Normal Map = 2, Global = 0, Bump Map = 1, Custom Normal = 3
Coating/Normal Strength | <strength@kKH7JwqDFdbq6_V8YqWY5p | maxon::Float64 | Input | false | false | false | -1 | 1 | 1 | 
Coating/Opacity | <U53ZTQRcNlwkQqhM2xVjCB | maxon::Float64 | Input | false | false | false | 0 | 1 | 1 | 
Coating/Roughness | <jOsXbs35BBkt8xhsTG68yD | maxon::Float64 | Input | false | false | false |  | 1 | 0.1 | 
Coating/Space | <space@fqmWzmAXARskYzM24hUOqp | maxon::InternedId | Input | false | false | true |  |  | tangent | Object = object, World = world, Tangent = tangent
Coating/Strength | <in3@HpcWsB_0I5$lYmaFcV9Msr | maxon::Float64 | Input | false | false | false |  | 1 | 0 | 
Coating/Swap Y and Z | <swapyz@IaQLLi14Ih4vsq3V_n7x7o | maxon::Bool | Input | false | false | false |  |  |  | 
Coating/UV Epsilon | <epsilonuv@KsCcIFjlBx6pVoNW3Nvu5p | maxon::Float64 | Input | false | false | false | -1 | 1 | 1 | 
Diffuse/3D Epsilon | <epsilon3d@PicfFH1cBxPq46BMsJpeUr | maxon::Float64 | Input | false | false | false | -1 | 1 | 1 | 
Diffuse/Bump Map | <color@miI15glrGRSkRGXck42jNr | maxon::Color64 | Input | false | false | false |  |  |  | 
Diffuse/Bump Strength | <strength@Ek3HBJWnGtxrKELGowOPir | maxon::Float64 | Input | false | false | false | -1 | 1 | 1 | 
Diffuse/Color | <ZrX$ufShIJ1nEDmW1oC0uB | maxon::Color64 | Input | false | false | false |  |  | (0.604,0.604,0.604) | 
Diffuse/Flip X | <flipx@EGRJZU$$D1sjJwRHe64ygo | maxon::Bool | Input | false | false | false |  |  |  | 
Diffuse/Flip Y | <flipy@LSbZjh_9NdfixP_WBhx8$p | maxon::Bool | Input | false | false | false |  |  | true | 
Diffuse/Flip Z | <flipz@HeW8wBimB15p7BDvjAueFp | maxon::Bool | Input | false | false | false |  |  |  | 
Diffuse/Intensity | <nc7YBitlK9KgAdPwVjiiYN | maxon::Float64 | Input | false | false | false |  | 10000000 | 1 | 
Diffuse/Normal | <RhWVmtpVB98q_hkxw5aybr@MBHpUpVEL9Uqlb3VBi8pHp | maxon::Vector64 | Input | false | false | false |  |  |  | 
Diffuse/Normal Map | <color@nfZ5dZTIFdKgEMZzjJiKbq | maxon::Color64 | Input | false | false | false |  |  |  | 
Diffuse/Normal Mode | <Akw7UXH3O1vilkNBW3K3Yo | maxon::Int64 | Input | false | false | true |  |  |  | Normal Map = 2, Global = 0, Bump Map = 1, Custom Normal = 3
Diffuse/Normal Strength | <strength@0R$TBhRjBFmkwrR9P$zvar | maxon::Float64 | Input | false | false | false | -1 | 1 | 1 | 
Diffuse/Opacity | <inport@3J52Jwa7FpdiI_m1FBW58p | maxon::Float64 | Input | false | false | false | 0 | 1 | 1 | 
Diffuse/Roughness | <mSLzVMt0Ed3sJMmuAU4CBM | maxon::Float64 | Input | false | false | false |  | 1 | 0 | 
Diffuse/Space | <space@xEAra3elCV7iAsrntEhU9p | maxon::InternedId | Input | false | false | true |  |  | tangent | Object = object, World = world, Tangent = tangent
Diffuse/Strength | <fwytuPOHH9qhST6xkG0jLq | maxon::Float64 | Input | false | false | false |  | 1 | 1 | 
Diffuse/Swap Y and Z | <swapyz@qOJK8osCDFdiTXzNMirW4q | maxon::Bool | Input | false | false | false |  |  |  | 
Diffuse/UV Epsilon | <epsilonuv@OvKvGgv0LFrgjw9Jt$su1p | maxon::Float64 | Input | false | false | false | -1 | 1 | 1 | 
Displacement/Displacement Height | <displacementheight@gb3VD3ZoO9yp0L_6f0FWSh | maxon::Float64 | Input | false | false | false |  |  | 10 | 
Displacement/Round Geometry | <roundgeometry@CvoFmNb4MBTkZkWUbzztzJ | maxon::Bool | Input | false | false | false |  |  | true | 
Displacement/Strength | <strength@wjgl2AyWO5BrjnuH1NJUwj | maxon::Float64 | Input | false | false | false |  |  | 1 | 
Displacement/Sub-Polygon Displacement | <spd@_duxR__3E9Sn64lea5C3Dh | maxon::Bool | Input | false | false | false |  |  |  | 
Displacement/Subdivision Level | <spdlevel@70_pQgt1NJmnTinXSamR_g | maxon::Int64 | Input | false | false | false | 1 | 10 | 4 | 
Displacement/Type | <dtype@Q3Kh1QZUBpJgcvYkZMZq3j | maxon::InternedId | Input | false | false | true |  |  | intensitycentered | RGB (XYZ World) = world, Intensity = intensity, Intensity (Centered) = intensitycentered, Red / Green = redgreen, RGB (XYZ Tangent) = tangent, RGB (XYZ Object) = object
Displacement/Value | <color@N7zziz97BlroDPNwiftX6j | maxon::Color64 | Input | false | false | false |  |  |  | 
Emission/Color | <UsCptWtoO5CkkJT2ZfVGsR | maxon::Color64 | Input | false | false | false |  |  | (1,1,1) | 
Emission/Intensity | <js0Polv7GRGgOUCQQ7a8HT | maxon::Float64 | Input | false | false | false |  | 10000000 | 1 | 
Normal/Flip X | <flipx@nIzre2SgJZclLb_u9snxWr | maxon::Bool | Input | false | false | false |  |  |  | 
Normal/Flip Y | <flipy@oS$g_oOQNRIuRaZ6MCHONr | maxon::Bool | Input | false | false | false |  |  | true | 
Normal/Flip Z | <flipz@QBr5cPMnEdPkfDmfTe6I_p | maxon::Bool | Input | false | false | false |  |  |  | 
Normal/Space | <space@7tjR4rbJA1zhoEqYdFrqqr | maxon::InternedId | Input | false | false | true |  |  | tangent | Object = object, World = world, Tangent = tangent
Normal/Strength | <strength@RrIO9d$7GRqgSlnHA3uA$r | maxon::Float64 | Input | false | false | false | -1 | 1 | 1 | 
Normal/Swap Y and Z | <swapyz@2p3vafKVBxujj_eS_N4Flr | maxon::Bool | Input | false | false | false |  |  |  | 
Normal/Value | <color@0NHhLhs3Fx7r$DKzWIyWrq | maxon::Color64 | Input | false | false | false |  |  |  | 
Opacity/Invert | <xlvsmBloI5Bok$0kEqlRtv | maxon::Bool | Input | false | false | false |  |  |  | 
Opacity/Layer Opacity | <alphacontrol@MvDbrU3uPVWnVpKBrYDt2h | maxon::Bool | Input | false | false | false |  |  |  | 
Opacity/Value | <aJBfhlpnAtVtzD15Lpi4Ou | maxon::Float64 | Input | false | false | false |  | 1 | 1 | 
Reflection/3D Epsilon | <epsilon3d@5YMotQXNLlIlIyG6ODYjOo | maxon::Float64 | Input | false | false | false | -1 | 1 | 1 | 
Reflection/Absorption (k) | <absorption@gRN2W6JtNFSmk58X80W$fh | maxon::Vector64 | Input | false | false | false |  |  | (2,2,2) | 
Reflection/Anisotropy | <TnRxIAgzIRFv8VkIbCW7ft@vxuWnHikMhNnDCOXazd_Bo | maxon::Float64 | Input | false | false | false |  | 1 | 0.5 | 
Reflection/BSDF Type | <bsdftype@thGgV$GlBhKr_YiGRVOR3d | maxon::InternedId | Input | false | false | true |  |  | ggxbrdf | Diffuse = orennayerbrdf, Beckmann = beckmannbrdf, GGX = ggxbrdf, Phong = phongbrdf, Ward = wardbrdf, Anisotropic = anisotropicbrdf
Reflection/Bump Map | <color@17uTOqFhFhXugPuqh8D7pq | maxon::Color64 | Input | false | false | false |  |  |  | 
Reflection/Bump Strength | <strength@Gc_w4rS_P1hjtAEt9HJ5Aq | maxon::Float64 | Input | false | false | false | -1 | 1 | 1 | 
Reflection/Color | <0zXK8tkrEVJj31yYaFq1f_ | maxon::Color64 | Input | false | false | false |  |  | (1,1,1) | 
Reflection/Diffuse Tint | <uB1BEPbNGZalyHWaEaVfpA | maxon::Float64 | Input | false | false | false |  | 1 |  | 
Reflection/Edge Color | <9zagsfUCDtpkzJ0dRrSAE_ | maxon::Color64 | Input | false | false | false |  |  | (1,1,1) | 
Reflection/Edge Intensity | <AiW73l59CRLmD63JDXhkGX | maxon::Float64 | Input | false | false | false |  | 1 | 1 | 
Reflection/Edge Opacity | <HZjnRx6GNhErIa82LsatwA | maxon::Float64 | Input | false | false | false |  | 1 | 1 | 
Reflection/Flip X | <flipx@ej4eCIRPFFDqfJTGV712oq | maxon::Bool | Input | false | false | false |  |  |  | 
Reflection/Flip Y | <flipy@EBQKOh5UGZ$kBMg0g$O0yp | maxon::Bool | Input | false | false | false |  |  | true | 
Reflection/Flip Z | <flipz@wCvkzwWJGFwt6J1$waNiqq | maxon::Bool | Input | false | false | false |  |  |  | 
Reflection/Fresnel Exponent | <inport@y9WC5G4ODdGlxCzKPfUUAv | maxon::Float64 | Input | false | false | false |  | 10 | 5 | 
Reflection/Fresnel Mode | <CMUmbs45MNLnTThFRcTf38 | maxon::Int64 | Input | false | false | true |  |  | 1 | Artistic = 0, Dielectric = 1, Conductor = 2, None = 3
Reflection/Frontal Opacity | <P4WU8fLXCJ3q4NVefYUWQB | maxon::Float64 | Input | false | false | false |  | 1 | 0.04 | 
Reflection/IOR | <ior@K0oZU1JgO57qohbB6ERUE9 | maxon::Float64 | Input | false | false | false |  | 1000 | 1.5 | 
Reflection/IOR (n) | <ior@3kuVHDAgN1LnAjTebTbWxg | maxon::Vector64 | Input | false | false | false |  |  | (1.5,1.5,1.5) | 
Reflection/Intensity | <ovUIVOVxJ1VtdGe$kPtPYM | maxon::Float64 | Input | false | false | false |  | 10000000 | 1 | 
Reflection/Normal | <RhWVmtpVB98q_hkxw5aybr@bxCtDhcMEVxumiLDD15XJp | maxon::Vector64 | Input | false | false | false |  |  |  | 
Reflection/Normal Map | <color@uVgWxGSxI1rsbPR_CgAGmp | maxon::Color64 | Input | false | false | false |  |  |  | 
Reflection/Normal Mode | <PEm3AFRMFFCicmbY6BJVTW | maxon::Int64 | Input | false | false | true |  |  |  | Normal Map = 2, Global = 0, Bump Map = 1, Custom Normal = 3
Reflection/Normal Strength | <strength@oDkBRmxlDJPs9WcwCuasJo | maxon::Float64 | Input | false | false | false | -1 | 1 | 1 | 
Reflection/Opacity | <Op_W2ctwNpcnFFqtgcrCwS | maxon::Float64 | Input | false | false | false |  | 1 | 1 | 
Reflection/Pattern | <v8pQvTbhLheuvGWkgkBGSn@R_f9osOJIRntfd2pTMUoHo | maxon::Int64 | Input | false | false | true |  |  |  | None = 0, Radial = 1, Radial Pattern = 2
Reflection/Rotation | <hsJA6lwLEdHs9EKJlq4x$p@iCXvbFXJOhAugdnL0YLgRq | maxon::Float64 | Input | false | false | false | -6.283 | 6.283 |  | 
Reflection/Rotation | <localrotation@vQ99HxnRI9nuR_G7zvk7Xj | maxon::Float64 | Input | false | false | false |  |  |  | 
Reflection/Roughness | <et73gnVWDJClg$mzgaindD | maxon::Float64 | Input | false | false | false |  | 1 | 0.5 | 
Reflection/Scratches | <WtSJ$zCBOFGhTjj7y6smIv@GwBz9OgMNV7iuOgu1YruYp | maxon::Float64 | Input | false | false | false |  | 1 | 0 | 
Reflection/Scratches Density | <b0I2Oz7JMxOiUjqXso1yFs@pIul0yEgFxugodMWSf0POq | maxon::Float64 | Input | false | false | false |  | 10000 | 10 | 
Reflection/Space | <space@M6T1LOz_K1Qs276RPj5usr | maxon::InternedId | Input | false | false | true |  |  | tangent | Object = object, World = world, Tangent = tangent
Reflection/Strength | <in3@N_iWiknsLZXu5E0IO3BbIo | maxon::Float64 | Input | false | false | false |  | 1 | 1 | 
Reflection/Swap Y and Z | <swapyz@H1PmO4$WP9aoQyQwOoFTbr | maxon::Bool | Input | false | false | false |  |  |  | 
Reflection/Tiles U | <oUqEtgGNLRhhLXU3fyHtBs@wZjHS4XSKV0rKFiIubORjp | maxon::Float64 | Input | false | false | false | 1 | 10000 | 1 | 
Reflection/Tiles V | <ydZHxYiVJNpqm1vYXSSyru@yaUL6Ra$L57lCPZdgrKsdp | maxon::Float64 | Input | false | false | false | 1 | 10000 | 1 | 
Reflection/UV Epsilon | <epsilonuv@IkhHVzfSBZQs6qLIUcV1Wq | maxon::Float64 | Input | false | false | false | -1 | 1 | 1 | 
Transparency/Absorption | <absorption@2CU8AkjSHNzq3XznZFKKLa | maxon::Color64 | Input | false | false | false |  |  | (1,1,1) | 
Transparency/Absorption Distance | <absorptiondistance@V1EoPATkPNVrBQHbxwqSmY | maxon::Float64 | Input | false | false | false |  |  | 100 | 
Transparency/Blurriness | <blurriness@BTt8Ez2SDRKp2pPXhc56UZ | maxon::Float64 | Input | false | false | false |  | 1 | 0 | 
Transparency/Exit Reflections | <exitreflections@TDmT7TgWOhYqmfmrd$UbZa | maxon::Bool | Input | false | false | false |  |  | true | 
Transparency/Fresnel Reflectivity | <fresnelreflectivity@1oBZ58WXBRpmfQqtQ$3K6P | maxon::Float64 | Input | false | false | false |  | 1 | 1 | 
Transparency/IOR | <ior@Sx_WsZEXJxhnvYEYl27sDZ | maxon::Float64 | Input | false | false | false | 1 | 5 | 1.5 | 
Transparency/Roughness | <inport@btoNbZnzF9WlwoOwAQAwgN | maxon::Float64 | Input | false | false | false |  | 1 |  | 
Transparency/Transparency | <transparency@u3W_aFdkAxpkwAbH1IW6vZ | maxon::Color64 | Input | false | false | false |  |  | (1,1,1) | 

