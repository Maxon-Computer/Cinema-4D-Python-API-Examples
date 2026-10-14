# Description: Joint tag

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/dynamics/description/tjointsettings.res`
- **Symbol:** `tjointsettings`
- **Category:** Other

Use parameter symbols to access parameters and cycle option symbols for cycle values, never their numeric IDs. Treat Min and Max as constraints and Default as the declared initial value; blank cells mean the resource does not declare that metadata, not that the value is zero. Base Description Parameters lists inherited fields from each base; All Parameters lists the effective parameter set for this description.

## Base Description Parameters

No base descriptions.

## All Parameters

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Object | JOINT_OBJECT | LINK |  |  |  | 
Connect Selection | JOINT_MOGRAPH_SELECTION_CONNECT | LINK |  |  |  | 
Reference Axis | JOINT_REFERENCE | LONG |  |  |  | JOINT_REFERENCE_X; JOINT_REFERENCE_Y; JOINT_REFERENCE_Z; JOINT_REFERENCE_DIRECTION
Attachment | JOINT_APPLICATION | LONG |  |  |  | JOINT_APPLICATION_COM; JOINT_APPLICATION_POLYPOINT; JOINT_APPLICATION_POINT_SELECTION
Index | JOINT_POINT | LONG |  |  |  | 
Map | JOINT_POINT_SELECTION | LINK |  |  |  | 
Region Of Influence | JOINT_REGION | REAL | 1.0 | 1000.0 |  | 
Shape Conservation | JOINT_POINT_SELECTION_SHAPE_CONSERVATION | REAL | 0.0 |  |  | 
Damping | JOINT_POINT_SELECTION_SHAPE_CONSERVATION_DAMPING | REAL | 0.0 |  |  | 
Pin to World | JOINT_PIN_TO_WORLD | BOOL |  |  |  | 
Selection | JOINT_MOGRAPH_SELECTION_PIN | LINK |  |  |  | 
