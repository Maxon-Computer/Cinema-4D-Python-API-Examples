# Description: Attributes

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/c4d_simulation/description/ofpattributes.res`
- **Symbol:** `ofpattributes`
- **Category:** Other

Use parameter symbols to access parameters and cycle option symbols for cycle values, never their numeric IDs. Treat Min and Max as constraints and Default as the declared initial value; blank cells mean the resource does not declare that metadata, not that the value is zero. Base Description Parameters lists inherited fields from each base; All Parameters lists the effective parameter set for this description.

## Base Description Parameters

No base descriptions.

## All Parameters

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Property | FP_ATTRIBUTES | LONG |  |  | FP_ATTRIBUTES_POSITION | FP_ATTRIBUTES_AGE; FP_ATTRIBUTES_ALIGNMENT; FP_ATTRIBUTES_ANGULARVELOCITY; FP_ATTRIBUTES_COLOR; FP_ATTRIBUTES_DISTANCE; FP_ATTRIBUTES_GROUP; FP_ATTRIBUTES_LIFETIME; FP_ATTRIBUTES_POSITION; FP_ATTRIBUTES_RADIUS; FP_ATTRIBUTES_VELOCITY; 0; FP_ATTRIBUTES_AGENORMALIZED; FP_ATTRIBUTES_ANGULARVELOCITYSPEED; FP_ATTRIBUTES_VELOCITYSPEED; 0; FP_ATTRIBUTES_CUSTOM
No label | FP_CUSTOMATTRIBUTE_NAME | STRING |  |  |  | 
No label | FP_CUSTOMATTRIBUTE_POPUP | POPUP |  |  |  | 
Extract | FP_VECTOR_EXTRACT | LONG |  |  | FP_EXTRACT_DEFAULT | FP_EXTRACT_COMPONENT_X; FP_EXTRACT_COMPONENT_Y; FP_EXTRACT_COMPONENT_Z; FP_EXTRACT_COMPONENTS_XYZ; FP_EXTRACT_LENGTH; FP_EXTRACT_DOT
Extract | FP_COLOR_EXTRACT | LONG |  |  | FP_EXTRACT_DEFAULT | FP_EXTRACT_COMPONENT_R; FP_EXTRACT_COMPONENT_G; FP_EXTRACT_COMPONENT_B; FP_EXTRACT_COMPONENT_A; FP_EXTRACT_COMPONENTS_RGB
Extract | FP_ALIGNMENT_EXTRACT | LONG |  |  | FP_EXTRACT_ALIGNMENTFORWARDDOT | FP_EXTRACT_ALIGNMENTFORWARDDOT; FP_EXTRACT_ALIGNMENTUPDOT; FP_EXTRACT_ALIGNMENTSIDEDOT
