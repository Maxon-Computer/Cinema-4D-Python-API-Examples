# Description: Moves Pose Morph Helper

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/interop_moves/description/tfacepose.res`
- **Symbol:** `Tfacepose`
- **Category:** Tags

Use parameter symbols to access parameters and cycle option symbols for cycle values, never their numeric IDs. Treat Min and Max as constraints and Default as the declared initial value; blank cells mean the resource does not declare that metadata, not that the value is zero. Base Description Parameters lists inherited fields from each base; All Parameters lists the effective parameter set for this description.

## Base Description Parameters

### Base Tag (`Tbase`)

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Expose on Object | ID_EXPOSETAB | BOOL |  |  |  | 

### Basic Properties (`Obaselist`)

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Icon File / ID | ID_BASELIST_ICON_FILE | TEXTURE |  |  |  | 
Icon Color | ID_BASELIST_ICON_COLORIZE_MODE | BOOL |  |  |  | 
Color | ID_BASELIST_ICON_COLOR | COLOR |  |  | 1.0 0.9 0.4 | 
No label | ID_BASELIST_ICON_PRESET_BUTTONS | ICONCHOOSER |  |  |  | 
Name | ID_BASELIST_NAME | STRING |  |  |  | 
Layer | ID_LAYER_LINK | LINK |  |  |  | 
No label | ID_BASELIST_NODESPACE_ADD_REMOVE_BUTTONS | NODESPACE_ADD_REMOVE |  |  |  | 

## All Parameters

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Icon File / ID | ID_BASELIST_ICON_FILE | TEXTURE |  |  |  | 
Icon Color | ID_BASELIST_ICON_COLORIZE_MODE | BOOL |  |  |  | 
Color | ID_BASELIST_ICON_COLOR | COLOR |  |  | 1.0 0.9 0.4 | 
No label | ID_BASELIST_ICON_PRESET_BUTTONS | ICONCHOOSER |  |  |  | 
Name | ID_BASELIST_NAME | STRING |  |  |  | 
Layer | ID_LAYER_LINK | LINK |  |  |  | 
No label | ID_BASELIST_NODESPACE_ADD_REMOVE_BUTTONS | NODESPACE_ADD_REMOVE |  |  |  | 
Expose on Object | ID_EXPOSETAB | BOOL |  |  |  | 
Face Capture | TFACEPOSE_CAPTURE | LINK |  |  |  | 
Xpresso | TFACEPOSE_EXPRESSO | LINK |  |  |  | 
PoseMorph | TFACEPOSE_POSEMORPH | LINK |  |  |  | 
Create All Pose Morphs | TFACEPOSE_CREATEALL | BUTTON |  |  |  | 
Range Calibration Capture | TFACEPOSE_CALIBRATE_CAPTURE | FILENAME |  |  |  | 
Calibrate | TFACEPOSE_CALIBRATE | BUTTON |  |  |  | 
Bake BlendShapes | TFACEPOSE_BAKE_BLENDSHAPES | BUTTON |  |  |  | 
Bake Face Transform | TFACEPOSE_BAKE_FACE_TRANSFORM | BUTTON |  |  |  | 
Bake Eyes Transforms | TFACEPOSE_BAKE_EYES_TRANSFORMS | BUTTON |  |  |  | 
Bake Sound | TFACEPOSE_BAKE_SOUND | BUTTON |  |  |  | 
Bake All | TFACEPOSE_BAKE_ALL | BUTTON |  |  |  | 
Left Eye Blink | TFACEPOSE_BLENDSHAPE_LEFTEYE_BLINK | BUTTON |  |  |  | 
Left Eye Look Down | TFACEPOSE_BLENDSHAPE_LEFTEYE_LOOKDOWN | BUTTON |  |  |  | 
Left Eye Look In | TFACEPOSE_BLENDSHAPE_LEFTEYE_LOOKIN | BUTTON |  |  |  | 
Left Eye Look Out | TFACEPOSE_BLENDSHAPE_LEFTEYE_LOOKOUT | BUTTON |  |  |  | 
Left Eye Look Up | TFACEPOSE_BLENDSHAPE_LEFTEYE_LOOKUP | BUTTON |  |  |  | 
Left Eye Squint | TFACEPOSE_BLENDSHAPE_LEFTEYE_SQUINT | BUTTON |  |  |  | 
Left Eye Wide | TFACEPOSE_BLENDSHAPE_LEFTEYE_WIDE | BUTTON |  |  |  | 
Right Eye Blink | TFACEPOSE_BLENDSHAPE_RIGHTEYE_BLINK | BUTTON |  |  |  | 
Right Eye Look Down | TFACEPOSE_BLENDSHAPE_RIGHTEYE_LOOKDOWN | BUTTON |  |  |  | 
Right Eye Look In | TFACEPOSE_BLENDSHAPE_RIGHTEYE_LOOKIN | BUTTON |  |  |  | 
Right Eye Look Out | TFACEPOSE_BLENDSHAPE_RIGHTEYE_LOOKOUT | BUTTON |  |  |  | 
Right Eye Look Up | TFACEPOSE_BLENDSHAPE_RIGHTEYE_LOOKUP | BUTTON |  |  |  | 
Right Eye Squint | TFACEPOSE_BLENDSHAPE_RIGHTEYE_SQUINT | BUTTON |  |  |  | 
Right Eye Wide | TFACEPOSE_BLENDSHAPE_RIGHTEYE_WIDE | BUTTON |  |  |  | 
Jaw Foward | TFACEPOSE_BLENDSHAPE_JAW_FORWARD | BUTTON |  |  |  | 
Jaw Left | TFACEPOSE_BLENDSHAPE_JAW_LEFT | BUTTON |  |  |  | 
Jaw Right | TFACEPOSE_BLENDSHAPE_JAW_RIGHT | BUTTON |  |  |  | 
Jaw Open | TFACEPOSE_BLENDSHAPE_JAW_OPEN | BUTTON |  |  |  | 
Mouth Left | TFACEPOSE_BLENDSHAPE_MOUTH_LEFT | BUTTON |  |  |  | 
Mouth Right | TFACEPOSE_BLENDSHAPE_MOUTH_RIGHT | BUTTON |  |  |  | 
Mouth Smile Left | TFACEPOSE_BLENDSHAPE_MOUTH_SMILELEFT | BUTTON |  |  |  | 
Mouth Smile Right | TFACEPOSE_BLENDSHAPE_MOUTH_SMILERIGHT | BUTTON |  |  |  | 
Mouth Frown Left | TFACEPOSE_BLENDSHAPE_MOUTH_FROWNLEFT | BUTTON |  |  |  | 
Mouth Frown Right | TFACEPOSE_BLENDSHAPE_MOUTH_FROWNRIGHT | BUTTON |  |  |  | 
Mouth Dimple Left | TFACEPOSE_BLENDSHAPE_MOUTH_DIMPLELEFT | BUTTON |  |  |  | 
Mouth Dimple Right | TFACEPOSE_BLENDSHAPE_MOUTH_DIMPLERIGHT | BUTTON |  |  |  | 
Mouth Stretch Left | TFACEPOSE_BLENDSHAPE_MOUTH_STRETCHLEFT | BUTTON |  |  |  | 
Mouth Stretch Right | TFACEPOSE_BLENDSHAPE_MOUTH_STRETCHRIGHT | BUTTON |  |  |  | 
Mouth Roll Lower Lip | TFACEPOSE_BLENDSHAPE_MOUTH_ROLLLOWER | BUTTON |  |  |  | 
Mouth Roll Upper Lip | TFACEPOSE_BLENDSHAPE_MOUTH_ROLLUPPER | BUTTON |  |  |  | 
Mouth Shrug Lower Lip | TFACEPOSE_BLENDSHAPE_MOUTH_SHRUGLOWER | BUTTON |  |  |  | 
Mouth Shrug Upper Lip | TFACEPOSE_BLENDSHAPE_MOUTH_SHRUGUPPER | BUTTON |  |  |  | 
Mouth Press Left | TFACEPOSE_BLENDSHAPE_MOUTH_PRESSLEFT | BUTTON |  |  |  | 
Mouth Press Right | TFACEPOSE_BLENDSHAPE_MOUTH_PRESSRIGHT | BUTTON |  |  |  | 
Mouth Lower Lip Down Left | TFACEPOSE_BLENDSHAPE_MOUTH_LOWERDOWNLEFT | BUTTON |  |  |  | 
Mouth Lower Lip Down Right | TFACEPOSE_BLENDSHAPE_MOUTH_LOWERDOWNRIGHT | BUTTON |  |  |  | 
Mouth Upper Lip Left | TFACEPOSE_BLENDSHAPE_MOUTH_UPPERUPLEFT | BUTTON |  |  |  | 
Mouth Upper Lip Right | TFACEPOSE_BLENDSHAPE_MOUTH_UPPERUPRIGHT | BUTTON |  |  |  | 
Mouth Close | TFACEPOSE_BLENDSHAPE_MOUTH_CLOSE | BUTTON |  |  |  | 
Mouth Funnel | TFACEPOSE_BLENDSHAPE_MOUTH_FUNNEL | BUTTON |  |  |  | 
Mouth Pucker | TFACEPOSE_BLENDSHAPE_MOUTH_PUCKER | BUTTON |  |  |  | 
Brow Down Left | TFACEPOSE_BLENDSHAPE_BROW_DOWNLEFT | BUTTON |  |  |  | 
Brow Down Right | TFACEPOSE_BLENDSHAPE_BROW_DOWNRIGHT | BUTTON |  |  |  | 
Brow Outer Up Left | TFACEPOSE_BLENDSHAPE_BROW_OUTERUPLEFT | BUTTON |  |  |  | 
Brow Outer Up Right | TFACEPOSE_BLENDSHAPE_BROW_OUTERUPRIGHT | BUTTON |  |  |  | 
Brow Inner Up | TFACEPOSE_BLENDSHAPE_BROW_INNERUP | BUTTON |  |  |  | 
Cheek Squint Left | TFACEPOSE_BLENDSHAPE_CHEEK_SQUINTLEFT | BUTTON |  |  |  | 
Cheek Squint Right | TFACEPOSE_BLENDSHAPE_CHEEK_SQUINTRIGHT | BUTTON |  |  |  | 
Cheek Puff | TFACEPOSE_BLENDSHAPE_CHEEK_PUFF | BUTTON |  |  |  | 
Nose Sneer Left | TFACEPOSE_BLENDSHAPE_NOSE_SNEERLEFT | BUTTON |  |  |  | 
Nose Sneer Right | TFACEPOSE_BLENDSHAPE_NOSE_SNEERRIGHT | BUTTON |  |  |  | 
Tongue Out | TFACEPOSE_BLENDSHAPE_TONGUE_OUT | BUTTON |  |  |  | 
