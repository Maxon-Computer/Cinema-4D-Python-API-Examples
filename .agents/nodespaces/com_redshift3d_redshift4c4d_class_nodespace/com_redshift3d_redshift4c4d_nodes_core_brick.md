# Node Template: Brick

- **Node Space ID:** `com.redshift3d.redshift4c4d.class.nodespace`
- **Template ID:** `com.redshift3d.redshift4c4d.nodes.core.brick`
- **Template Name:** `Brick`

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
Colors/Alt. Brick Color/Blendmode | <com.redshift3d.redshift4c4d.nodes.core.brick.brickalttextureblendmode | maxon::Int | Input | false | false | true |  |  | 0 | Normal = 0, Multiply = 4, Overlay = 13, Dodge = 17, Burn = 16, Darken = 7, Lighten = 6, Color = 18
Colors/Alt. Brick Color/Color | <com.redshift3d.redshift4c4d.nodes.core.brick.brickaltcolorinput | com.redshift3d.redshift4c4d.portbundle.gradient | Input | true | true | false |  |  |  | 
Colors/Alt. Brick Color/Color/Knot.1 | <com.redshift3d.redshift4c4d.nodes.core.brick.brickaltcolorinput/_0 | com.redshift3d.redshift4c4d.portbundle.gradient | Input | false | false | false |  |  |  | 
Colors/Alt. Brick Color/Color/Knot.1/Bias Position | <com.redshift3d.redshift4c4d.nodes.core.brick.brickaltcolorinput/_0/bias | maxon::Float | Input | false | false | false |  | 1 | 0.5 | 
Colors/Alt. Brick Color/Color/Knot.1/Color | <com.redshift3d.redshift4c4d.nodes.core.brick.brickaltcolorinput/_0/color | maxon::Color | Input | false | false | false |  |  | (1,1,1) | 
Colors/Alt. Brick Color/Color/Knot.1/Interpolation | <com.redshift3d.redshift4c4d.nodes.core.brick.brickaltcolorinput/_0/interpolation | maxon::InternedId | Input | false | false | true |  |  | smoothknot | Smooth = smoothknot, Cubic = cubicknot, Linear = linearknot, Step = none, Blend = blend, Cubic Bias = cubicbias
Colors/Alt. Brick Color/Color/Knot.1/Knot Position | <com.redshift3d.redshift4c4d.nodes.core.brick.brickaltcolorinput/_0/position | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Colors/Alt. Brick Color/Color/Knot.2 | <com.redshift3d.redshift4c4d.nodes.core.brick.brickaltcolorinput/_1 | com.redshift3d.redshift4c4d.portbundle.gradient | Input | false | false | false |  |  |  | 
Colors/Alt. Brick Color/Color/Knot.2/Bias Position | <com.redshift3d.redshift4c4d.nodes.core.brick.brickaltcolorinput/_1/bias | maxon::Float | Input | false | false | false |  | 1 | 0.5 | 
Colors/Alt. Brick Color/Color/Knot.2/Color | <com.redshift3d.redshift4c4d.nodes.core.brick.brickaltcolorinput/_1/color | maxon::Color | Input | false | false | false |  |  | (1,1,1) | 
Colors/Alt. Brick Color/Color/Knot.2/Interpolation | <com.redshift3d.redshift4c4d.nodes.core.brick.brickaltcolorinput/_1/interpolation | maxon::InternedId | Input | false | false | true |  |  | smoothknot | Smooth = smoothknot, Cubic = cubicknot, Linear = linearknot, Step = none, Blend = blend, Cubic Bias = cubicbias
Colors/Alt. Brick Color/Color/Knot.2/Knot Position | <com.redshift3d.redshift4c4d.nodes.core.brick.brickaltcolorinput/_1/position | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Colors/Alt. Brick Color/Flip | <com.redshift3d.redshift4c4d.nodes.core.brick.brickalttextureflip | maxon::Bool | Input | false | false | false |  |  | false | 
Colors/Alt. Brick Color/Offset | <com.redshift3d.redshift4c4d.nodes.core.brick.brickalttextureoffset | maxon::Float | Input | false | false | false | 0 | 2147483648 | 0.05 | 
Colors/Alt. Brick Color/Opacity | <com.redshift3d.redshift4c4d.nodes.core.brick.brickalttextureopacity | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Colors/Alt. Brick Color/Random Offset | <com.redshift3d.redshift4c4d.nodes.core.brick.brickalttexturerandom | maxon::Bool | Input | false | false | false |  |  | false | 
Colors/Alt. Brick Color/Scale | <com.redshift3d.redshift4c4d.nodes.core.brick.brickalttexturescale | maxon::Float | Input | false | false | false | 0 | 2147483648 | 1 | 
Colors/Alt. Brick Color/Texture | <com.redshift3d.redshift4c4d.nodes.core.brick.brickalttexture | maxon::Color64 | Input | false | false | false |  |  | (0,0,0) | 
Colors/Brick Color/Blendmode | <com.redshift3d.redshift4c4d.nodes.core.brick.bricktextureblendmode | maxon::Int | Input | false | false | true |  |  | 0 | Normal = 0, Multiply = 4, Overlay = 13, Dodge = 17, Burn = 16, Darken = 7, Lighten = 6, Color = 18
Colors/Brick Color/Color | <com.redshift3d.redshift4c4d.nodes.core.brick.brickcolorinput | com.redshift3d.redshift4c4d.portbundle.gradient | Input | true | true | false |  |  |  | 
Colors/Brick Color/Color/Knot.1 | <com.redshift3d.redshift4c4d.nodes.core.brick.brickcolorinput/_0 | com.redshift3d.redshift4c4d.portbundle.gradient | Input | false | false | false |  |  |  | 
Colors/Brick Color/Color/Knot.1/Bias Position | <com.redshift3d.redshift4c4d.nodes.core.brick.brickcolorinput/_0/bias | maxon::Float | Input | false | false | false |  | 1 | 0.5 | 
Colors/Brick Color/Color/Knot.1/Color | <com.redshift3d.redshift4c4d.nodes.core.brick.brickcolorinput/_0/color | maxon::Color | Input | false | false | false |  |  | (1,1,1) | 
Colors/Brick Color/Color/Knot.1/Interpolation | <com.redshift3d.redshift4c4d.nodes.core.brick.brickcolorinput/_0/interpolation | maxon::InternedId | Input | false | false | true |  |  | smoothknot | Smooth = smoothknot, Cubic = cubicknot, Linear = linearknot, Step = none, Blend = blend, Cubic Bias = cubicbias
Colors/Brick Color/Color/Knot.1/Knot Position | <com.redshift3d.redshift4c4d.nodes.core.brick.brickcolorinput/_0/position | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Colors/Brick Color/Color/Knot.2 | <com.redshift3d.redshift4c4d.nodes.core.brick.brickcolorinput/_1 | com.redshift3d.redshift4c4d.portbundle.gradient | Input | false | false | false |  |  |  | 
Colors/Brick Color/Color/Knot.2/Bias Position | <com.redshift3d.redshift4c4d.nodes.core.brick.brickcolorinput/_1/bias | maxon::Float | Input | false | false | false |  | 1 | 0.5 | 
Colors/Brick Color/Color/Knot.2/Color | <com.redshift3d.redshift4c4d.nodes.core.brick.brickcolorinput/_1/color | maxon::Color | Input | false | false | false |  |  | (1,1,1) | 
Colors/Brick Color/Color/Knot.2/Interpolation | <com.redshift3d.redshift4c4d.nodes.core.brick.brickcolorinput/_1/interpolation | maxon::InternedId | Input | false | false | true |  |  | smoothknot | Smooth = smoothknot, Cubic = cubicknot, Linear = linearknot, Step = none, Blend = blend, Cubic Bias = cubicbias
Colors/Brick Color/Color/Knot.2/Knot Position | <com.redshift3d.redshift4c4d.nodes.core.brick.brickcolorinput/_1/position | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Colors/Brick Color/Flip | <com.redshift3d.redshift4c4d.nodes.core.brick.bricktextureflip | maxon::Bool | Input | false | false | false |  |  | false | 
Colors/Brick Color/Offset | <com.redshift3d.redshift4c4d.nodes.core.brick.bricktextureoffset | maxon::Float | Input | false | false | false | 0 | 2147483648 | 0.05 | 
Colors/Brick Color/Opacity | <com.redshift3d.redshift4c4d.nodes.core.brick.bricktextureopacity | maxon::Float | Input | false | false | false | 0 | 2147483648 | 1 | 
Colors/Brick Color/Random Offset | <com.redshift3d.redshift4c4d.nodes.core.brick.bricktexturerandom | maxon::Bool | Input | false | false | false |  |  | false | 
Colors/Brick Color/Scale | <com.redshift3d.redshift4c4d.nodes.core.brick.bricktexturescale | maxon::Float | Input | false | false | false | 0 | 2147483648 | 1 | 
Colors/Brick Color/Texture | <com.redshift3d.redshift4c4d.nodes.core.brick.bricktexture | maxon::Color64 | Input | false | false | false |  |  | (0,0,0) | 
Colors/Other/Alt. Color Every n Columns | <com.redshift3d.redshift4c4d.nodes.core.brick.altcolorhperiod | maxon::Int | Input | false | false | false | -2147483647 | 2147483646 | 0 | 
Colors/Other/Alt. Color Every n Rows | <com.redshift3d.redshift4c4d.nodes.core.brick.altcolorvperiod | maxon::Int | Input | false | false | false | -2147483647 | 2147483646 | 7 | 
Colors/Other/Brick Noise Scale | <com.redshift3d.redshift4c4d.nodes.core.brick.brickcolornoisescaleinput | maxon::Float | Input | false | false | false | 0 | 2147483648 | 0.5 | 
Colors/Other/Detail | <com.redshift3d.redshift4c4d.nodes.core.brick.detailinput | maxon::Float | Input | false | false | false | 0 | 2147483648 | 0.025 | 
Colors/Other/Detail Scale | <com.redshift3d.redshift4c4d.nodes.core.brick.detailscaleinput | maxon::Float | Input | false | false | false | 0 | 2147483648 | 0.75 | 
Dirt/Brick | <com.redshift3d.redshift4c4d.nodes.core.brick.dirtenablebrick | maxon::Bool | Input | false | false | false |  |  | true | 
Dirt/Dirt Color/Alpha | <com.redshift3d.redshift4c4d.nodes.core.brick.dirtalphainput | net.maxon.render.portbundle.spline | Input | false | true | false |  |  |  | 
Dirt/Dirt Color/Alpha/Link End Positions | <com.redshift3d.redshift4c4d.nodes.core.brick.dirtalphainput/linkendpositions | maxon::Bool | Input | false | false | false |  |  |  | 
Dirt/Dirt Color/Alpha/Link End Tangents | <com.redshift3d.redshift4c4d.nodes.core.brick.dirtalphainput/linkendtangents | maxon::Bool | Input | false | false | false |  |  |  | 
Dirt/Dirt Color/Alpha/Max | <com.redshift3d.redshift4c4d.nodes.core.brick.dirtalphainput/max | maxon::Vector2d | Input | false | false | false |  |  | (1,1) | 
Dirt/Dirt Color/Alpha/Min | <com.redshift3d.redshift4c4d.nodes.core.brick.dirtalphainput/min | maxon::Vector2d | Input | false | false | false |  |  |  | 
Dirt/Dirt Color/Alpha/Points | <com.redshift3d.redshift4c4d.nodes.core.brick.dirtalphainput/points | net.maxon.render.portbundle.splinepoint | Input | true | false | false |  |  |  | 
Dirt/Dirt Color/Alpha/Points/Point.1 | <com.redshift3d.redshift4c4d.nodes.core.brick.dirtalphainput/points/_0 | net.maxon.render.portbundle.splinepoint | Input | false | false | false |  |  |  | 
Dirt/Dirt Color/Alpha/Points/Point.1/Break Tangent | <com.redshift3d.redshift4c4d.nodes.core.brick.dirtalphainput/points/_0/breaktangent | maxon::Bool | Input | false | false | false |  |  |  | 
Dirt/Dirt Color/Alpha/Points/Point.1/Interpolation | <com.redshift3d.redshift4c4d.nodes.core.brick.dirtalphainput/points/_0/interpolation | maxon::InternedId | Input | false | false | true |  |  | spline | Spline = spline, Cubic = cubic, Linear = linear
Dirt/Dirt Color/Alpha/Points/Point.1/Keep Visual Angle | <com.redshift3d.redshift4c4d.nodes.core.brick.dirtalphainput/points/_0/keepvisualangle | maxon::Bool | Input | false | false | false |  |  |  | 
Dirt/Dirt Color/Alpha/Points/Point.1/Lock Angle | <com.redshift3d.redshift4c4d.nodes.core.brick.dirtalphainput/points/_0/lockangle | maxon::Bool | Input | false | false | false |  |  |  | 
Dirt/Dirt Color/Alpha/Points/Point.1/Lock Length | <com.redshift3d.redshift4c4d.nodes.core.brick.dirtalphainput/points/_0/locklength | maxon::Bool | Input | false | false | false |  |  |  | 
Dirt/Dirt Color/Alpha/Points/Point.1/Lock X | <com.redshift3d.redshift4c4d.nodes.core.brick.dirtalphainput/points/_0/lockx | maxon::Bool | Input | false | false | false |  |  |  | 
Dirt/Dirt Color/Alpha/Points/Point.1/Lock Y | <com.redshift3d.redshift4c4d.nodes.core.brick.dirtalphainput/points/_0/locky | maxon::Bool | Input | false | false | false |  |  |  | 
Dirt/Dirt Color/Alpha/Points/Point.1/Position X | <com.redshift3d.redshift4c4d.nodes.core.brick.dirtalphainput/points/_0/positionx | maxon::Float | Input | false | false | false |  |  | 0 | 
Dirt/Dirt Color/Alpha/Points/Point.1/Position Y | <com.redshift3d.redshift4c4d.nodes.core.brick.dirtalphainput/points/_0/positiony | maxon::Float | Input | false | false | false |  |  | 0 | 
Dirt/Dirt Color/Alpha/Points/Point.1/Tangent Left | <com.redshift3d.redshift4c4d.nodes.core.brick.dirtalphainput/points/_0/tangentleft | maxon::Vector2d | Input | false | false | false |  |  |  | 
Dirt/Dirt Color/Alpha/Points/Point.1/Tangent Right | <com.redshift3d.redshift4c4d.nodes.core.brick.dirtalphainput/points/_0/tangentright | maxon::Vector2d | Input | false | false | false |  |  |  | 
Dirt/Dirt Color/Alpha/Points/Point.2 | <com.redshift3d.redshift4c4d.nodes.core.brick.dirtalphainput/points/_1 | net.maxon.render.portbundle.splinepoint | Input | false | false | false |  |  |  | 
Dirt/Dirt Color/Alpha/Points/Point.2/Break Tangent | <com.redshift3d.redshift4c4d.nodes.core.brick.dirtalphainput/points/_1/breaktangent | maxon::Bool | Input | false | false | false |  |  |  | 
Dirt/Dirt Color/Alpha/Points/Point.2/Interpolation | <com.redshift3d.redshift4c4d.nodes.core.brick.dirtalphainput/points/_1/interpolation | maxon::InternedId | Input | false | false | true |  |  | spline | Spline = spline, Cubic = cubic, Linear = linear
Dirt/Dirt Color/Alpha/Points/Point.2/Keep Visual Angle | <com.redshift3d.redshift4c4d.nodes.core.brick.dirtalphainput/points/_1/keepvisualangle | maxon::Bool | Input | false | false | false |  |  |  | 
Dirt/Dirt Color/Alpha/Points/Point.2/Lock Angle | <com.redshift3d.redshift4c4d.nodes.core.brick.dirtalphainput/points/_1/lockangle | maxon::Bool | Input | false | false | false |  |  |  | 
Dirt/Dirt Color/Alpha/Points/Point.2/Lock Length | <com.redshift3d.redshift4c4d.nodes.core.brick.dirtalphainput/points/_1/locklength | maxon::Bool | Input | false | false | false |  |  |  | 
Dirt/Dirt Color/Alpha/Points/Point.2/Lock X | <com.redshift3d.redshift4c4d.nodes.core.brick.dirtalphainput/points/_1/lockx | maxon::Bool | Input | false | false | false |  |  |  | 
Dirt/Dirt Color/Alpha/Points/Point.2/Lock Y | <com.redshift3d.redshift4c4d.nodes.core.brick.dirtalphainput/points/_1/locky | maxon::Bool | Input | false | false | false |  |  |  | 
Dirt/Dirt Color/Alpha/Points/Point.2/Position X | <com.redshift3d.redshift4c4d.nodes.core.brick.dirtalphainput/points/_1/positionx | maxon::Float | Input | false | false | false |  |  | 0 | 
Dirt/Dirt Color/Alpha/Points/Point.2/Position Y | <com.redshift3d.redshift4c4d.nodes.core.brick.dirtalphainput/points/_1/positiony | maxon::Float | Input | false | false | false |  |  | 0 | 
Dirt/Dirt Color/Alpha/Points/Point.2/Tangent Left | <com.redshift3d.redshift4c4d.nodes.core.brick.dirtalphainput/points/_1/tangentleft | maxon::Vector2d | Input | false | false | false |  |  |  | 
Dirt/Dirt Color/Alpha/Points/Point.2/Tangent Right | <com.redshift3d.redshift4c4d.nodes.core.brick.dirtalphainput/points/_1/tangentright | maxon::Vector2d | Input | false | false | false |  |  |  | 
Dirt/Dirt Color/Alpha/Tension | <com.redshift3d.redshift4c4d.nodes.core.brick.dirtalphainput/tension | maxon::Float | Input | false | false | false |  | 1 | 1 | 
Dirt/Dirt Color/Brick Blending | <com.redshift3d.redshift4c4d.nodes.core.brick.dirtblendingbrickinput | maxon::Float | Input | false | false | false | -1 | 1 | -0.5 | 
Dirt/Dirt Color/Color | <com.redshift3d.redshift4c4d.nodes.core.brick.dirtcolorinput | com.redshift3d.redshift4c4d.portbundle.gradient | Input | true | true | false |  |  |  | 
Dirt/Dirt Color/Color Scale | <com.redshift3d.redshift4c4d.nodes.core.brick.dirtcolorscaleinput | maxon::Float | Input | false | false | false | 0 | 2147483648 | 1 | 
Dirt/Dirt Color/Color/Knot.1 | <com.redshift3d.redshift4c4d.nodes.core.brick.dirtcolorinput/_0 | com.redshift3d.redshift4c4d.portbundle.gradient | Input | false | false | false |  |  |  | 
Dirt/Dirt Color/Color/Knot.1/Bias Position | <com.redshift3d.redshift4c4d.nodes.core.brick.dirtcolorinput/_0/bias | maxon::Float | Input | false | false | false |  | 1 | 0.5 | 
Dirt/Dirt Color/Color/Knot.1/Color | <com.redshift3d.redshift4c4d.nodes.core.brick.dirtcolorinput/_0/color | maxon::Color | Input | false | false | false |  |  | (1,1,1) | 
Dirt/Dirt Color/Color/Knot.1/Interpolation | <com.redshift3d.redshift4c4d.nodes.core.brick.dirtcolorinput/_0/interpolation | maxon::InternedId | Input | false | false | true |  |  | smoothknot | Smooth = smoothknot, Cubic = cubicknot, Linear = linearknot, Step = none, Blend = blend, Cubic Bias = cubicbias
Dirt/Dirt Color/Color/Knot.1/Knot Position | <com.redshift3d.redshift4c4d.nodes.core.brick.dirtcolorinput/_0/position | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Dirt/Dirt Color/Color/Knot.2 | <com.redshift3d.redshift4c4d.nodes.core.brick.dirtcolorinput/_2 | com.redshift3d.redshift4c4d.portbundle.gradient | Input | false | false | false |  |  |  | 
Dirt/Dirt Color/Color/Knot.2/Bias Position | <com.redshift3d.redshift4c4d.nodes.core.brick.dirtcolorinput/_2/bias | maxon::Float | Input | false | false | false |  | 1 | 0.5 | 
Dirt/Dirt Color/Color/Knot.2/Color | <com.redshift3d.redshift4c4d.nodes.core.brick.dirtcolorinput/_2/color | maxon::Color | Input | false | false | false |  |  | (1,1,1) | 
Dirt/Dirt Color/Color/Knot.2/Interpolation | <com.redshift3d.redshift4c4d.nodes.core.brick.dirtcolorinput/_2/interpolation | maxon::InternedId | Input | false | false | true |  |  | smoothknot | Smooth = smoothknot, Cubic = cubicknot, Linear = linearknot, Step = none, Blend = blend, Cubic Bias = cubicbias
Dirt/Dirt Color/Color/Knot.2/Knot Position | <com.redshift3d.redshift4c4d.nodes.core.brick.dirtcolorinput/_2/position | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Dirt/Dirt Color/Color/Knot.3 | <com.redshift3d.redshift4c4d.nodes.core.brick.dirtcolorinput/_3 | com.redshift3d.redshift4c4d.portbundle.gradient | Input | false | false | false |  |  |  | 
Dirt/Dirt Color/Color/Knot.3/Bias Position | <com.redshift3d.redshift4c4d.nodes.core.brick.dirtcolorinput/_3/bias | maxon::Float | Input | false | false | false |  | 1 | 0.5 | 
Dirt/Dirt Color/Color/Knot.3/Color | <com.redshift3d.redshift4c4d.nodes.core.brick.dirtcolorinput/_3/color | maxon::Color | Input | false | false | false |  |  | (1,1,1) | 
Dirt/Dirt Color/Color/Knot.3/Interpolation | <com.redshift3d.redshift4c4d.nodes.core.brick.dirtcolorinput/_3/interpolation | maxon::InternedId | Input | false | false | true |  |  | smoothknot | Smooth = smoothknot, Cubic = cubicknot, Linear = linearknot, Step = none, Blend = blend, Cubic Bias = cubicbias
Dirt/Dirt Color/Color/Knot.3/Knot Position | <com.redshift3d.redshift4c4d.nodes.core.brick.dirtcolorinput/_3/position | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Dirt/Dirt Color/Color/Knot.4 | <com.redshift3d.redshift4c4d.nodes.core.brick.dirtcolorinput/_1 | com.redshift3d.redshift4c4d.portbundle.gradient | Input | false | false | false |  |  |  | 
Dirt/Dirt Color/Color/Knot.4/Bias Position | <com.redshift3d.redshift4c4d.nodes.core.brick.dirtcolorinput/_1/bias | maxon::Float | Input | false | false | false |  | 1 | 0.5 | 
Dirt/Dirt Color/Color/Knot.4/Color | <com.redshift3d.redshift4c4d.nodes.core.brick.dirtcolorinput/_1/color | maxon::Color | Input | false | false | false |  |  | (1,1,1) | 
Dirt/Dirt Color/Color/Knot.4/Interpolation | <com.redshift3d.redshift4c4d.nodes.core.brick.dirtcolorinput/_1/interpolation | maxon::InternedId | Input | false | false | true |  |  | smoothknot | Smooth = smoothknot, Cubic = cubicknot, Linear = linearknot, Step = none, Blend = blend, Cubic Bias = cubicbias
Dirt/Dirt Color/Color/Knot.4/Knot Position | <com.redshift3d.redshift4c4d.nodes.core.brick.dirtcolorinput/_1/position | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Dirt/Dirt Color/Gap Blending | <com.redshift3d.redshift4c4d.nodes.core.brick.dirtblendinggapinput | maxon::Float | Input | false | false | false | -1 | 1 | -0.5 | 
Dirt/Dirt Color/Octaves | <com.redshift3d.redshift4c4d.nodes.core.brick.dirtalphaoct | maxon::Float | Input | false | false | false | 0 | 10 | 8 | 
Dirt/Dirt Color/Opacity | <com.redshift3d.redshift4c4d.nodes.core.brick.dirtopacityinput | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Dirt/Dirt Color/Opacity Scale | <com.redshift3d.redshift4c4d.nodes.core.brick.dirtalphascale | maxon::Float | Input | false | false | false | 0 | 2147483648 | 1 | 
Dirt/Dirt Color/Shift | <com.redshift3d.redshift4c4d.nodes.core.brick.dirtalphashift | maxon::Vector2d64 | Input | false | false | false |  |  | (0,0) | 
Dirt/Dirt Texture/Alpha Bias | <com.redshift3d.redshift4c4d.nodes.core.brick.dirttexturealphabias | maxon::Float | Input | false | false | false | -2147483648 | 2147483648 | 1 | 
Dirt/Dirt Texture/Alpha Contrast | <com.redshift3d.redshift4c4d.nodes.core.brick.dirttexturealphacontrast | maxon::Float | Input | false | false | false | 0 | 2147483648 | 1 | 
Dirt/Dirt Texture/Alpha Invert | <com.redshift3d.redshift4c4d.nodes.core.brick.dirttexturealphainvert | maxon::Bool | Input | false | false | false |  |  | false | 
Dirt/Dirt Texture/Color Texture | <com.redshift3d.redshift4c4d.nodes.core.brick.dirtcolortexture | maxon::Color64 | Input | false | false | false |  |  | (0,0,0) | 
Dirt/Dirt Texture/Flip | <com.redshift3d.redshift4c4d.nodes.core.brick.dirttextureflip | maxon::Bool | Input | false | false | false |  |  | false | 
Dirt/Dirt Texture/Multiply with Gradient | <com.redshift3d.redshift4c4d.nodes.core.brick.dirttexturemultiplywithgradient | maxon::Bool | Input | false | false | false |  |  | false | 
Dirt/Dirt Texture/Scale | <com.redshift3d.redshift4c4d.nodes.core.brick.dirttexturescale | maxon::Float | Input | false | false | false | 0 | 2147483648 | 1 | 
Dirt/Dirt Texture/Shift | <com.redshift3d.redshift4c4d.nodes.core.brick.dirttextureshift | maxon::Vector2d64 | Input | false | false | false |  |  | (0,0) | 
Dirt/Dirt Texture/Texture | <com.redshift3d.redshift4c4d.nodes.core.brick.dirttexture | maxon::Color64 | Input | false | false | false |  |  | (0,0,0) | 
Dirt/Enable | <com.redshift3d.redshift4c4d.nodes.core.brick.dirtenable | maxon::Bool | Input | false | false | false |  |  | false | 
Dirt/Gap | <com.redshift3d.redshift4c4d.nodes.core.brick.dirtenablegap | maxon::Bool | Input | false | false | false |  |  | true | 
Dirt/Rain/Blur Color Texture | <com.redshift3d.redshift4c4d.nodes.core.brick.dirttexturerainblurcolortexture | maxon::Bool | Input | false | false | false |  |  | true | 
Dirt/Rain/Rain | <com.redshift3d.redshift4c4d.nodes.core.brick.dirttexturerain | maxon::Float | Input | false | false | false | 0 | 2147483648 | 0 | 
Gaps/Gap Color/Color | <com.redshift3d.redshift4c4d.nodes.core.brick.gapcolorinput | com.redshift3d.redshift4c4d.portbundle.gradient | Input | true | true | false |  |  |  | 
Gaps/Gap Color/Color/Knot.1 | <com.redshift3d.redshift4c4d.nodes.core.brick.gapcolorinput/_0 | com.redshift3d.redshift4c4d.portbundle.gradient | Input | false | false | false |  |  |  | 
Gaps/Gap Color/Color/Knot.1/Bias Position | <com.redshift3d.redshift4c4d.nodes.core.brick.gapcolorinput/_0/bias | maxon::Float | Input | false | false | false |  | 1 | 0.5 | 
Gaps/Gap Color/Color/Knot.1/Color | <com.redshift3d.redshift4c4d.nodes.core.brick.gapcolorinput/_0/color | maxon::Color | Input | false | false | false |  |  | (1,1,1) | 
Gaps/Gap Color/Color/Knot.1/Interpolation | <com.redshift3d.redshift4c4d.nodes.core.brick.gapcolorinput/_0/interpolation | maxon::InternedId | Input | false | false | true |  |  | smoothknot | Smooth = smoothknot, Cubic = cubicknot, Linear = linearknot, Step = none, Blend = blend, Cubic Bias = cubicbias
Gaps/Gap Color/Color/Knot.1/Knot Position | <com.redshift3d.redshift4c4d.nodes.core.brick.gapcolorinput/_0/position | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Gaps/Gap Color/Color/Knot.2 | <com.redshift3d.redshift4c4d.nodes.core.brick.gapcolorinput/_1 | com.redshift3d.redshift4c4d.portbundle.gradient | Input | false | false | false |  |  |  | 
Gaps/Gap Color/Color/Knot.2/Bias Position | <com.redshift3d.redshift4c4d.nodes.core.brick.gapcolorinput/_1/bias | maxon::Float | Input | false | false | false |  | 1 | 0.5 | 
Gaps/Gap Color/Color/Knot.2/Color | <com.redshift3d.redshift4c4d.nodes.core.brick.gapcolorinput/_1/color | maxon::Color | Input | false | false | false |  |  | (1,1,1) | 
Gaps/Gap Color/Color/Knot.2/Interpolation | <com.redshift3d.redshift4c4d.nodes.core.brick.gapcolorinput/_1/interpolation | maxon::InternedId | Input | false | false | true |  |  | smoothknot | Smooth = smoothknot, Cubic = cubicknot, Linear = linearknot, Step = none, Blend = blend, Cubic Bias = cubicbias
Gaps/Gap Color/Color/Knot.2/Knot Position | <com.redshift3d.redshift4c4d.nodes.core.brick.gapcolorinput/_1/position | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Gaps/Gap Color/Flip | <com.redshift3d.redshift4c4d.nodes.core.brick.gaptextureflip | maxon::Bool | Input | false | false | false |  |  | false | 
Gaps/Gap Color/Gap Texture Blendmode | <com.redshift3d.redshift4c4d.nodes.core.brick.gaptextureblendmode | maxon::Int | Input | false | false | true |  |  | 0 | Normal = 0, Multiply = 4, Overlay = 13, Dodge = 17, Burn = 16, Darken = 7, Lighten = 6, Color = 18
Gaps/Gap Color/Opacity | <com.redshift3d.redshift4c4d.nodes.core.brick.gaptextureopacity | maxon::Float | Input | false | false | false | 0 | 1 | 1 | 
Gaps/Gap Color/Scale | <com.redshift3d.redshift4c4d.nodes.core.brick.gaptexturescale | maxon::Float | Input | false | false | false | 0 | 2147483648 | 1 | 
Gaps/Gap Color/Texture | <com.redshift3d.redshift4c4d.nodes.core.brick.gaptexture | maxon::Color64 | Input | false | false | false |  |  | (0,0,0) | 
Gaps/Other/Depth | <com.redshift3d.redshift4c4d.nodes.core.brick.gapdepthinput | maxon::Float | Input | false | false | false | 0 | 2147483648 | 0.05 | 
Gaps/Other/Gap Noise Scale | <com.redshift3d.redshift4c4d.nodes.core.brick.gapcolornoisescaleinput | maxon::Float | Input | false | false | false | 0 | 2147483648 | 0.005 | 
Gaps/Other/Groove | <com.redshift3d.redshift4c4d.nodes.core.brick.gapgrooveinput | maxon::Float | Input | false | false | false | -1 | 1 | 0.2 | 
Gaps/Other/Size | <com.redshift3d.redshift4c4d.nodes.core.brick.gapsizeinput | maxon::Float | Input | false | false | false | 0 | 2147483648 | 0.025 | 
Gaps/Other/Size Variation | <com.redshift3d.redshift4c4d.nodes.core.brick.gapnoiseintensity | maxon::Float | Input | false | false | false | 0 | 2147483648 | 0.9 | 
Gaps/Other/Size Variation Scale | <com.redshift3d.redshift4c4d.nodes.core.brick.gapnoisescale | maxon::Float | Input | false | false | false | 0 | 2147483648 | 0.25 | 
Shader/Displacement/Height Variation | <com.redshift3d.redshift4c4d.nodes.core.brick.brickdisplacementrandomheight | maxon::Float | Input | false | false | false | 0 | 1 | 0.75 | 
Shader/Displacement/Seed | <com.redshift3d.redshift4c4d.nodes.core.brick.brickdisplacementvariation | maxon::Int | Input | false | false | false |  |  | 123 | 
Shader/Displacement/Slope Direction | <com.redshift3d.redshift4c4d.nodes.core.brick.brickdisplacementmode | maxon::Int | Input | false | false | true |  |  | 4 | Random = 4, Left = 2, Right = 3, Up = 0, Down = 1
Shader/Displacement/Slope Intensity | <com.redshift3d.redshift4c4d.nodes.core.brick.brickdisplacementslopeintensity | maxon::Float | Input | false | false | false | 0 | 1 | 0.75 | 
Shader/Shader Properties/Balance Alt. Color Period | <com.redshift3d.redshift4c4d.nodes.core.brick.balancecolhperiod | maxon::Bool | Input | false | false | false |  |  | true | 
Shader/Shader Properties/Brick Height | <com.redshift3d.redshift4c4d.nodes.core.brick.brickheightinput | maxon::Float | Input | false | false | false | 0 | 2147483648 | 0.25 | 
Shader/Shader Properties/Brick Width | <com.redshift3d.redshift4c4d.nodes.core.brick.brickwidthinput | maxon::Float | Input | false | false | false | 0 | 2147483648 | 0.5 | 
Shader/Shader Properties/Half Width Every nth Row | <com.redshift3d.redshift4c4d.nodes.core.brick.brickhalfwidthfrequency | maxon::Int | Input | false | false | false | -2147483647 | 2147483646 | 0 | 
Shader/Shader Properties/Half Width Shift | <com.redshift3d.redshift4c4d.nodes.core.brick.brickhalfwidthshift | maxon::Float | Input | false | false | false | 0 | 2147483648 | 0.5 | 
Shader/Shader Properties/Reset every nth row | <com.redshift3d.redshift4c4d.nodes.core.brick.brickshiftreset | maxon::Int | Input | false | false | false | -2147483647 | 2147483646 | 0 | 
Shader/Shader Properties/Scale | <com.redshift3d.redshift4c4d.nodes.core.brick.brickscaleinput | maxon::Float | Input | false | false | false | 0 | 2147483648 | 0.25 | 
Shader/Shader Properties/Shift | <com.redshift3d.redshift4c4d.nodes.core.brick.brickshift | maxon::Float | Input | false | false | false | 0 | 2147483648 | 0.5 | 
Shader/Shader Properties/UV Channel | <com.redshift3d.redshift4c4d.nodes.core.brick.tspace_id | maxon::String | Input | false | false | false |  |  |  | 
Shader/Shader Properties/UV Context | <com.redshift3d.redshift4c4d.nodes.core.brick.uv_context | RSC4D::UVContext | Input | false | false | false |  |  |  | 
Outputs/outColor | >com.redshift3d.redshift4c4d.nodes.core.brick.outcolor | maxon::Color64 | Output | false | false | false |  |  | (0,0,0) | 
Outputs/outDirtMask | >com.redshift3d.redshift4c4d.nodes.core.brick.outdirtmask | maxon::Float | Output | false | false | false |  |  | 0 | 
Outputs/outDisplacementColor | >com.redshift3d.redshift4c4d.nodes.core.brick.outdisplacementcolor | maxon::Color64 | Output | false | false | false |  |  | (0,0,0) | 
Outputs/outGapsMask | >com.redshift3d.redshift4c4d.nodes.core.brick.outgapsmask | maxon::Float | Output | false | false | false |  |  | 0 | 

