# Description: Add Reference

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/ca/description/dxrefadd.res`
- **Symbol:** `Dxrefadd`
- **Category:** Other

Use parameter symbols to access parameters and cycle option symbols for cycle values, never their numeric IDs. Treat Min and Max as constraints and Default as the declared initial value; blank cells mean the resource does not declare that metadata, not that the value is zero. Base Description Parameters lists inherited fields from each base; All Parameters lists the effective parameter set for this description.

## Base Description Parameters

No base descriptions.

## All Parameters

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Encapsulated | ID_CA_XREFADD_ENCAPSULATED | BOOL |  |  |  | 
Generator | ID_CA_XREFADD_GENERATOR | BOOL |  |  |  | 
Name Space | ID_CA_XREFADD_NAMESPACE | LONG |  |  |  | ID_CA_XREFADD_NAMESPACE_NONE; ID_CA_XREFADD_NAMESPACE_REFNAME; ID_CA_XREFADD_NAMESPACE_CUSTOM
Auto Match | ID_CA_XREFADD_NAMESPACE_AUTO | BOOL |  |  |  | 
Prefix | ID_CA_XREFADD_PREFIX | STRING |  |  |  | 
Separator | ID_CA_XREFADD_NAMESPACE_SEP | STRING |  |  |  | 
Animation | ID_CA_XREFADD_ANIM | BOOL |  |  |  | 
Frame | ID_CA_XREFADD_ANIM_FRAME | BASETIME |  |  |  | 
Offset | ID_CA_XREFADD_ANIM_OFFSET | BASETIME |  |  |  | 
Scale | ID_CA_XREFADD_ANIM_SCALE | REAL |  |  |  | 
Materials | ID_CA_XREFADD_MATERIALS | BOOL |  |  |  | 
Point Cache | ID_CA_XREFADD_POINTCACHE | BOOL |  |  |  | 
Hierarchy | ID_CA_XREFADD_HIERARCHY | BOOL |  |  |  | 
Transform | ID_CA_XREFADD_PSR | BOOL |  |  |  | 
Mode | ID_CA_XREFADD_PSR_MODE | LONG |  |  |  | ID_CA_XREFADD_PSR_MODE_ABS; ID_CA_XREFADD_PSR_MODE_REL
Parameters | ID_CA_XREFADD_PARAMETERS | BOOL |  |  |  | 
Mode | ID_CA_XREFADD_PARAMETERS_MODE | LONG |  |  |  | ID_CA_XREFADD_PSR_MODE_ABS; ID_CA_XREFADD_PSR_MODE_REL
User Data | ID_CA_XREFADD_USERDATA | BOOL |  |  |  | 
Mode | ID_CA_XREFADD_USERDATA_MODE | LONG |  |  |  | ID_CA_XREFADD_PSR_MODE_ABS; ID_CA_XREFADD_PSR_MODE_REL
Points | ID_CA_XREFADD_POINTS | BOOL |  |  |  | 
Mode | ID_CA_XREFADD_POINTS_MODE | LONG |  |  |  | ID_CA_XREFADD_PSR_MODE_ABS; ID_CA_XREFADD_PSR_MODE_REL
Relative to Project | ID_CA_XREFADD_RELATIVE | BOOL |  |  |  | 
Incremental | ID_CA_XREFADD_INCREMENTAL | BOOL |  |  |  | 
Position | ID_CA_XREFADD_PIVOT_POS | VECTOR |  |  |  | 
Rotation | ID_CA_XREFADD_PIVOT_ROT | VECTOR |  |  |  | 
Scale | ID_CA_XREFADD_PIVOT_SCL | VECTOR |  |  |  | 
