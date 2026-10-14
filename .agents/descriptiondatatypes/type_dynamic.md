# Description Data Type: DYNAMIC

- **Cinema 4D Version:** `2027.0.0`

This file describes the DYNAMIC description data type and lists all flags encountered in the resources for Cinema 4D 2027.0.0.

## Flags

Flag | Arguments | Example
---- | --------- | -------
CREATEPORT | 2 | <code>DYNAMIC GV_EQU_INPUT { INPORT; MULTIPLE; CREATEPORT 2; }</code>
EDITPORT |  | <code>DYNAMIC GV_RANGEMAPPER_RANGE11 { INPORT; EDITPORT; }</code>
HIDDEN |  | <code>DYNAMIC GV_RESULT_OUTPUT { OUTPORT; STATICPORT; CREATEPORT; HIDDEN; }</code>
INPORT |  | <code>DYNAMIC GV_ITERATE_LINK_INPUT { INPORT; }</code>
MINPORTS | 1 | <code>DYNAMIC GV_CONDITION_INPUT { INPORT; MULTIPLE; CREATEPORT 2; MINPORTS 1; }</code>
MULTIPLE |  | <code>DYNAMIC GV_EQU_INPUT { INPORT; MULTIPLE; CREATEPORT 2; }</code>
OUTPORT |  | <code>DYNAMIC GV_ITERATE_LINK_OUTPUT { OUTPORT; }</code>
STATICPORT |  | <code>DYNAMIC GV_ABS_INPUT { INPORT; STATICPORT; CREATEPORT; }</code>
