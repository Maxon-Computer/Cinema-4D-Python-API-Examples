# Description: Glow

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/advanced_render/description/glow.res`
- **Symbol:** `Glow`
- **Category:** Video Posts

Use parameter symbols to access parameters and cycle option symbols for cycle values, never their numeric IDs. Treat Min and Max as constraints and Default as the declared initial value; blank cells mean the resource does not declare that metadata, not that the value is zero. Base Description Parameters lists inherited fields from each base; All Parameters lists the effective parameter set for this description.

## Base Description Parameters

### Post Effect (`VPbase`)

No parameters.

## All Parameters

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Use Object ID | GW_CH_OBJON | BOOL |  |  |  | 
Object ID | GW_CH_OBJ | LONG | 0 | 1000 |  | 
Size | GW_MAXSIZE | REAL | 0.0 | 100.0 |  | 
Intensity | GW_DENS | REAL | 0.0 |  |  | 
Back Intensity | GW_BDENS | REAL | 0.0 |  |  | 
Luminosity | GW_LUM | REAL | 0.0 | 100.0 |  | 
Use Back Luminosity | GW_BLUMON | BOOL |  |  |  | 
Back Luminosity | GW_BLUM | REAL | 0.0 | 100.0 |  | 
Use Color | GW_GCOL | BOOL |  |  |  | 
Color | GW_COL | COLOR |  |  |  | 
Glow Edges | GW_GEDGES | BOOL |  |  |  | 
Zoom Scale | GW_ZSCALE | BOOL |  |  |  | 
Distance Scale | GW_DSCALE | BOOL |  |  |  | 
Balance | GW_BAL | REAL | 0.0 | 100.0 |  | 
Use | GW_NC_USE | BOOL |  |  |  | 
Min. Intensity | GW_NC_MIN | REAL | 0.0 |  |  | 
Max. Intensity | GW_NC_MAX | REAL | 0.0 |  |  | 
Use Key Color | GW_NC_COLON | BOOL |  |  |  | 
Key Color | GW_NC_COL | COLOR |  |  |  | 
Color Variation | GW_NC_COLVAR | REAL | 0.0 | 100.0 |  | 
Use Size Gradient | GW_NC_SIZEON | BOOL |  |  |  | 
Size Gradient | GW_NC_GSIZE | GRADIENT |  |  |  | 
Use Density Gradient | GW_NC_DENSON | BOOL |  |  |  | 
Density Gradient | GW_NC_GDENS | GRADIENT |  |  |  | 
Use Luminosity Gradient | GW_NC_LUMON | BOOL |  |  |  | 
Luminosity Gradient | GW_NC_GLUM | GRADIENT |  |  |  | 
Use Color Gradient | GW_NC_GCOL | BOOL |  |  |  | 
Color Gradient | GW_NC_GRAD | GRADIENT |  |  |  | 
Use | GW_AT_USE | BOOL |  |  |  | 
Start Range | GW_AT_START | REAL | 0.0 |  |  | 
End Range | GW_AT_END | REAL | 0.0 |  |  | 
Distance Position | GW_AT_POS | LONG |  |  |  | GW_AT_ZBUFFER; GW_AT_3DPOS
Use Size Gradient | GW_AT_SIZEON | BOOL |  |  |  | 
Size Gradient | GW_AT_GSIZE | GRADIENT |  |  |  | 
Use Density Gradient | GW_AT_DENSON | BOOL |  |  |  | 
Density Gradient | GW_AT_GDENS | GRADIENT |  |  |  | 
Use Luminosity Gradient | GW_AT_LUMON | BOOL |  |  |  | 
Luminosity Gradient | GW_AT_GLUM | GRADIENT |  |  |  | 
Use Color Gradient | GW_AT_GCOL | BOOL |  |  |  | 
Color Gradient | GW_AT_GRAD | GRADIENT |  |  |  | 
Use | GW_SN_USE | BOOL |  |  |  | 
Shininess | GW_SN_SH | REAL | 0.0 | 100.0 |  | 
Use Size Gradient | GW_SN_SIZEON | BOOL |  |  |  | 
Size Gradient | GW_SN_GSIZE | GRADIENT |  |  |  | 
Use Density Gradient | GW_SN_DENSON | BOOL |  |  |  | 
Density Gradient | GW_SN_GDENS | GRADIENT |  |  |  | 
Use Luminosity Gradient | GW_SN_LUMON | BOOL |  |  |  | 
Luminosity Gradient | GW_SN_GLUM | GRADIENT |  |  |  | 
Use Color Gradient | GW_SN_GCOL | BOOL |  |  |  | 
Color Gradient | GW_SN_GRAD | GRADIENT |  |  |  | 
Use | GW_FF_USE | BOOL |  |  |  | 
Noise Type | GW_FF_TYPE | LONG |  |  |  | GW_FF_TYPE_GAS; GW_FF_TYPE_FIRE; GW_FF_TYPE_ELEC
Intensity | GW_FF_INT | REAL | 0.0 |  |  | 
Density | GW_FF_DENS | REAL | 0.0 |  |  | 
Brightness | GW_FF_BRIGHT | REAL |  |  |  | 
Luminosity | GW_FF_LUM | REAL | 0.0 | 100.0 |  | 
Use Color | GW_FF_COLORON | BOOL |  |  |  | 
Color | GW_FF_COLOR | COLOR |  |  |  | 
Scale | GW_FF_SCALE | REAL | 0.0 |  |  | 
Peak Blend | GW_FF_EXP | REAL |  |  |  | 
Details | GW_FF_LEVEL | REAL | 1.0 |  |  | 
Phase | GW_FF_PHASE | REAL |  |  |  | 
Angle | GW_FF_ANGLE | REAL |  |  |  | 
Drift | GW_FF_SPEED | REAL |  |  |  | 
Static Pos. | GW_FF_PSTATIC | BOOL |  |  |  | 
Ground Glow | GW_FF_ADD | BOOL |  |  |  | 
Stretch | GW_FF_STR | REAL | 0.0 |  |  | 
