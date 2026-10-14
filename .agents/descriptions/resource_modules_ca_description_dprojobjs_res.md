# Description: Project Objects

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/ca/description/dprojobjs.res`
- **Symbol:** `Dprojobjs`
- **Category:** Other

Use parameter symbols to access parameters and cycle option symbols for cycle values, never their numeric IDs. Treat Min and Max as constraints and Default as the declared initial value; blank cells mean the resource does not declare that metadata, not that the value is zero. Base Description Parameters lists inherited fields from each base; All Parameters lists the effective parameter set for this description.

## Base Description Parameters

No base descriptions.

## All Parameters

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Children | ID_CA_PROJOBJS_CHILDREN | BOOL |  |  |  | 
Default | ID_CA_PROJOBJS_DEF_MODE | LONG |  |  |  | ID_CA_PROJOBJS_MODE_PROJECT; ID_CA_PROJOBJS_MODE_SURFACE; ID_CA_PROJOBJS_MODE_POINTS; ID_CA_PROJOBJS_MODE_COLLIDE
Control | ID_CA_PROJOBJS_CTRL_MODE | LONG |  |  |  | ID_CA_PROJOBJS_MODE_PROJECT; ID_CA_PROJOBJS_MODE_SURFACE; ID_CA_PROJOBJS_MODE_POINTS; ID_CA_PROJOBJS_MODE_COLLIDE
Shift | ID_CA_PROJOBJS_SHIFT_MODE | LONG |  |  |  | ID_CA_PROJOBJS_MODE_PROJECT; ID_CA_PROJOBJS_MODE_SURFACE; ID_CA_PROJOBJS_MODE_POINTS; ID_CA_PROJOBJS_MODE_COLLIDE
