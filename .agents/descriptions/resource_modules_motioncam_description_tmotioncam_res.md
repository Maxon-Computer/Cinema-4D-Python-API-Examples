# Description: Motion Camera

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/motioncam/description/tmotioncam.res`
- **Symbol:** `Tmotioncam`
- **Category:** Tags

Use parameter symbols to access parameters and cycle option symbols for cycle values, never their numeric IDs. Treat Min and Max as constraints and Default as the declared initial value; blank cells mean the resource does not declare that metadata, not that the value is zero. Base Description Parameters lists inherited fields from each base; All Parameters lists the effective parameter set for this description.

## Base Description Parameters

### Expression (`Texpression`)

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Priority | EXPRESSION_PRIORITY | PRIORITY |  |  |  | 
Enable | EXPRESSION_ENABLE | BOOL |  |  |  | 

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
Priority | EXPRESSION_PRIORITY | PRIORITY |  |  |  | 
Enable | EXPRESSION_ENABLE | BOOL |  |  |  | 
Camera | TMOTIONCAM_VIS_CAM | SEPARATOR |  |  |  | 
Vis: Use Custom Camera Color | TMOTIONCAM_VIS_CAM_ENABLED | BOOL |  |  |  | 
Vis: Camera Color | TMOTIONCAM_VIS_CAM_COL | COLOR |  |  |  | 
Vis: Rig | TMOTIONCAM_VIS_RIG | SEPARATOR |  |  |  | 
Vis: Draw Rig | TMOTIONCAM_VIS_RIG_ENABLED | BOOL |  |  |  | 
Vis: Rig Mode | TMOTIONCAM_VIS_RIG_MODE | LONG |  |  |  | TMOTIONCAM_VIS_RIG_MODE_SIMPLE; TMOTIONCAM_VIS_RIG_MODE_FIGURE
Vis: Rig Color | TMOTIONCAM_VIS_RIG_COL | COLOR |  |  |  | 
Vis: Targets | TMOTIONCAM_VIS_TARGET | SEPARATOR |  |  |  | 
Vis: Draw Marker | TMOTIONCAM_VIS_TARGET_ENABLED | BOOL |  |  |  | 
Vis: Marker Radius | TMOTIONCAM_VIS_TARGET_RADIUS | REAL | 0.0 |  |  | 
Vis: Draw Target Distance | TMOTIONCAM_VIS_TARGET_DRAWDISTTEXT | BOOL |  |  |  | 
Vis: Draw Aberration | TMOTIONCAM_VIS_TARGET_DRAWABERRATION | BOOL |  |  |  | 
Vis: Draw Single Targets | TMOTIONCAM_VIS_TARGET_DRAWSINGLETARGETS | BOOL |  |  |  | 
Vis: Target Color | TMOTIONCAM_VIS_TARGET_COLOR | COLOR |  |  |  | 
Target Pos: Link | TMOTIONCAM_EXPORT_TARGETPOS_LINK | LINK |  |  |  | 
Target Pos: Vector | TMOTIONCAM_EXPORT_TARGETPOS_VECTOR | VECTOR |  |  |  | 
Foot: Link | TMOTIONCAM_EXPORT_FOOTPOS_LINK | LINK |  |  |  | 
Foot: Pos Vector | TMOTIONCAM_EXPORT_FOOTPOS_VECTOR | VECTOR |  |  |  | 
Head: Link | TMOTIONCAM_EXPORT_HEADPOS_LINK | LINK |  |  |  | 
Head: Pos Vector | TMOTIONCAM_EXPORT_HEADPOS_VECTOR | VECTOR |  |  |  | 
Speed (Units/sec) | TMOTIONCAM_EXPORT_SPEED | REAL |  |  |  | 
Rig: Height | TMOTIONCAM_RIG_HEIGHT | REAL |  |  |  | 
Rig: Parallax | TMOTIONCAM_RIG_PARALLAX | VECTOR |  |  |  | 
Manual Rotation | TMOTIONCAM_ROT_MANUAL | SEPARATOR |  |  |  | 
Manual Head Rotation | TMOTIONCAM_ROT_MANUAL_HEAD | VECTOR | -180.0 | 180.0 |  | 
Manual Camera Rotation | TMOTIONCAM_ROT_MANUAL_CAM | VECTOR | -180.0 | 180.0 |  | 
Base | TMOTIONCAM_BASE | SEPARATOR |  |  |  | 
Base: Link | TMOTIONCAM_BASE_LINK | LINK |  |  |  | 
Base: Inherit Camera Parameters | TMOTIONCAM_BASE_INHERITPARAMS | BOOL |  |  |  | 
Base: Override Rig Dimensions | TMOTIONCAM_BASE_OVERRIDE_RIGHEIGHT | BOOL |  |  |  | 
Splines: Enabled | TMOTIONCAM_SPLINE_ENABLED | BOOL |  |  |  | 
Splines: Tangential  | TMOTIONCAM_SPLINE_TANGENTIAL | BOOL |  |  |  | 
Splines: Path Spline A | TMOTIONCAM_SPLINE_A | LINK |  |  |  | 
Splines: Rail Spline A | TMOTIONCAM_SPLINE_A_RAIL | LINK |  |  |  | 
Splines: Path Spline B | TMOTIONCAM_SPLINE_B | LINK |  |  |  | 
Splines: Rail Spline B | TMOTIONCAM_SPLINE_B_RAIL | LINK |  |  |  | 
Splines: Cam Pos A | TMOTIONCAM_SPLINE_POS_A | REAL | 0.0 | 100.0 |  | 
Splines: Cam Pos A Curve | TMOTIONCAM_SPLINE_POS_A_SPLINE | SPLINE |  |  |  | 
Splines: Auto. Anim A Enabled | TMOTIONCAM_SPLINE_AUTO_A_ENABLED | BOOL |  |  |  | 
Splines: Auto. Anim A Start | TMOTIONCAM_SPLINE_AUTO_A_START | BASETIME |  |  |  | 
Splines: Auto. Anim A End | TMOTIONCAM_SPLINE_AUTO_A_END | BASETIME |  |  |  | 
Splines: Cam Pos B | TMOTIONCAM_SPLINE_POS_B | REAL | 0.0 | 100.0 |  | 
Splines: Cam Pos B Curve | TMOTIONCAM_SPLINE_POS_B_SPLINE | SPLINE |  |  |  | 
Splines: Auto. Anim B Enabled | TMOTIONCAM_SPLINE_AUTO_B_ENABLED | BOOL |  |  |  | 
Splines: Auto. Anim B Start | TMOTIONCAM_SPLINE_AUTO_B_START | BASETIME |  |  |  | 
Splines: Auto. Anim B End | TMOTIONCAM_SPLINE_AUTO_B_END | BASETIME |  |  |  | 
Splines: Blend A &lt;-&gt; B | TMOTIONCAM_SPLINE_POS_BLEND | REAL | 0.0 | 100.0 |  | 
Splines: Cam Pos Blend Curve | TMOTIONCAM_SPLINE_POS_BLEND_SPLINE | SPLINE |  |  |  | 
Splines: Auto. Anim Blend Enabled | TMOTIONCAM_SPLINE_AUTO_BLEND_ENABLED | BOOL |  |  |  | 
Splines: Auto. Anim Blend Start | TMOTIONCAM_SPLINE_AUTO_BLEND_START | BASETIME |  |  |  | 
Splines: Auto. Anim Blend End | TMOTIONCAM_SPLINE_AUTO_BLEND_END | BASETIME |  |  |  | 
Splines: Intensity | TMOTIONCAM_SPLINE_INTENSITY | REAL | 0.0 | 100.0 |  | 
Targets: Enabled | TMOTIONCAM_TARGET_ENABLED | BOOL |  |  |  | 
Compensate Aberration | TMOTIONCAM_TARGET_COMPENSATE_PARALLAX | BOOL |  |  |  | 
Targets: Target A1 | TMOTIONCAM_TARGET_A1 | LINK |  |  |  | 
Targets: Target A1 Pos | TMOTIONCAM_TARGET_SPLINE_A1_POS | REAL | 0.0 | 100.0 |  | 
Targets: Target A2 | TMOTIONCAM_TARGET_A2 | LINK |  |  |  | 
Targets: Target A2 Pos | TMOTIONCAM_TARGET_SPLINE_A2_POS | REAL | 0.0 | 100.0 |  | 
Targets: Target B1 | TMOTIONCAM_TARGET_B1 | LINK |  |  |  | 
Targets: Target B1 Pos | TMOTIONCAM_TARGET_SPLINE_B1_POS | REAL | 0.0 | 100.0 |  | 
Targets: Target B2 | TMOTIONCAM_TARGET_B2 | LINK |  |  |  | 
Targets: Target B2 Pos | TMOTIONCAM_TARGET_SPLINE_B2_POS | REAL | 0.0 | 100.0 |  | 
Targets: Up Vector | TMOTIONCAM_TARGET_UPVECTOR | LINK |  |  |  | 
Targets: Target UpVector Pos | TMOTIONCAM_TARGET_SPLINE_UPVECTOR_POS | REAL | 0.0 | 100.0 |  | 
Targets: Target Pos A1 &lt;-&gt; A2 | TMOTIONCAM_TARGET_BLEND_A | REAL | 0.0 | 100.0 |  | 
Targets: Blend A Curve | TMOTIONCAM_TARGET_BLEND_A_SPLINE | SPLINE |  |  |  | 
Targets: Target Pos B1 &lt;-&gt; B2 | TMOTIONCAM_TARGET_BLEND_B | REAL | 0.0 | 100.0 |  | 
Targets: Blend B Curve | TMOTIONCAM_TARGET_BLEND_B_SPLINE | SPLINE |  |  |  | 
Targets: Target Pos A &lt;-&gt; B | TMOTIONCAM_TARGET_BLEND_AB | REAL | 0.0 | 100.0 |  | 
Targets: Blend AB Curve | TMOTIONCAM_TARGET_BLEND_AB_SPLINE | SPLINE |  |  |  | 
Targets: Intensity | TMOTIONCAM_TARGET_INTENSITY | REAL | 0.0 | 100.0 |  | 
Targets: Intensity Curve | TMOTIONCAM_TARGET_INTENSITY_SPLINE | SPLINE |  |  |  | 
Chase: Enabled | TMOTIONCAM_FOLLOW_ENABLED | BOOL |  |  |  | 
Chase: Link | TMOTIONCAM_FOLLOW_LINK | LINK |  |  |  | 
Chase: Max. Distance | TMOTIONCAM_FOLLOW_MAXDISTANCE | REAL | 0.0 |  |  | 
Chase: Min. Distance | TMOTIONCAM_FOLLOW_MINDISTANCE | REAL | 0.0 |  |  | 
Auto. Banking: Enabled | TMOTIONCAM_AUTOBANKING_ENABLED | BOOL |  |  |  | 
Auto. Banking: Intensity | TMOTIONCAM_AUTOBANKING_INTENSITY | REAL | 0.0 |  |  | 
Auto. Banking: Dampen | TMOTIONCAM_AUTOBANKING_DAMPEN | REAL | 0.0 | 100.0 |  | 
Foot Dynamics | TMOTIONCAM_FOOT_DYN | SEPARATOR |  |  |  | 
Foot Dyn: Enabled | TMOTIONCAM_FOOT_DYN_ENABLED | BOOL |  |  |  | 
Foot Dyn: Mode | TMOTIONCAM_FOOT_DYN_MODE | LONG |  |  |  | TMOTIONCAM_DYN_MODE_DAMPEN; TMOTIONCAM_DYN_MODE_SPRING
Foot Dyn: Damp Pos | TMOTIONCAM_FOOT_DYN_DAMP_POS | REAL | 0.0 | 100.0 |  | 
Foot Dyn: Damp Rot | TMOTIONCAM_FOOT_DYN_DAMP_ROT | REAL | 0.0 | 100.0 |  | 
Foot Dyn: Inertia Pos | TMOTIONCAM_FOOT_DYN_INERTIA_POS | REAL | 0.0 | 100.0 |  | 
Foot Dyn: Inertia Rot | TMOTIONCAM_FOOT_DYN_INERTIA_ROT | REAL | 0.0 | 100.0 |  | 
Head Dynamics | TMOTIONCAM_HEAD_DYN | SEPARATOR |  |  |  | 
Head Dyn: Enabled | TMOTIONCAM_HEAD_DYN_ENABLED | BOOL |  |  |  | 
Head Dyn: Mode | TMOTIONCAM_HEAD_DYN_MODE | LONG |  |  |  | TMOTIONCAM_DYN_MODE_DAMPEN; TMOTIONCAM_DYN_MODE_SPRING
Head Dyn: Damp Pos | TMOTIONCAM_HEAD_DYN_DAMP_POS | REAL | 0.0 | 100.0 |  | 
Head Dyn: Damp Rot | TMOTIONCAM_HEAD_DYN_DAMP_ROT | REAL | 0.0 | 100.0 |  | 
Head Dyn: Inertia Pos | TMOTIONCAM_HEAD_DYN_INERTIA_POS | REAL | 0.0 | 100.0 |  | 
Head Dyn: Inertia Rot | TMOTIONCAM_HEAD_DYN_INERTIA_ROT | REAL | 0.0 | 100.0 |  | 
Hands Dynamics | TMOTIONCAM_CAM_DYN | SEPARATOR |  |  |  | 
Hands Dyn: Enabled | TMOTIONCAM_CAM_DYN_ENABLED | BOOL |  |  |  | 
Hands Dyn: Mode | TMOTIONCAM_CAM_DYN_MODE | LONG |  |  |  | TMOTIONCAM_DYN_MODE_DAMPEN; TMOTIONCAM_DYN_MODE_SPRING
Hands Dyn: Damp Pos | TMOTIONCAM_CAM_DYN_DAMP_POS | REAL | 0.0 | 100.0 |  | 
Hands Dyn: Damp Rot | TMOTIONCAM_CAM_DYN_DAMP_ROT | REAL | 0.0 | 100.0 |  | 
Hands Dyn: Inertia Pos | TMOTIONCAM_CAM_DYN_INERTIA_POS | REAL | 0.0 | 100.0 |  | 
Hands Dyn:Inertia Rot | TMOTIONCAM_CAM_DYN_INERTIA_ROT | REAL | 0.0 | 100.0 |  | 
Focus Dynamics | TMOTIONCAM_FOCUS_DYN | SEPARATOR |  |  |  | 
Focus Dyn: Enabled | TMOTIONCAM_FOCUS_DYN_ENABLED | BOOL |  |  |  | 
Focus Dyn: Mode | TMOTIONCAM_FOCUS_DYN_MODE | LONG |  |  |  | TMOTIONCAM_DYN_MODE_DAMPEN; TMOTIONCAM_DYN_MODE_SPRING
Focus Dyn: Damp | TMOTIONCAM_FOCUS_DYN_DAMP | REAL | 0.0 | 100.0 |  | 
Focus Dyn: Inertia | TMOTIONCAM_FOCUS_DYN_INERTIA | REAL | 0.0 | 100.0 |  | 
Preset | TMOTIONCAM_NMOTION_PRESET | LONG |  |  |  | TMOTIONCAM_NMOTION_PRESET_CUSTOM; TMOTIONCAM_NMOTION_PRESET_QUIET; TMOTIONCAM_NMOTION_PRESET_STEADYCAM_1; TMOTIONCAM_NMOTION_PRESET_STEADYCAM_2; TMOTIONCAM_NMOTION_PRESET_EGO; TMOTIONCAM_NMOTION_PRESET_DOGMA
Footsteps | TMOTIONCAM_NMOTION_FOOT | SEPARATOR |  |  |  | 
Footsteps: Intensity | TMOTIONCAM_NMOTION_FOOT_INTENSITY | REAL | 0.0 |  |  | 
Footsteps: Scale | TMOTIONCAM_NMOTION_FOOT_SCALE | VECTOR |  |  |  | 
Footsteps: Frequency | TMOTIONCAM_NMOTION_FOOT_FREQ | REAL |  |  |  | 
Head Rotation | TMOTIONCAM_NMOTION_HEAD | SEPARATOR |  |  |  | 
Motion: Head Rot: Intensity | TMOTIONCAM_NMOTION_HEAD_ROT_INTENSITY | REAL | 0.0 |  |  | 
Motion: Head Rot: Max | TMOTIONCAM_NMOTION_HEAD_ROT_MAX | VECTOR |  |  |  | 
Motion: Head Rot: Frequency | TMOTIONCAM_NMOTION_HEAD_ROT_FREQ | VECTOR |  |  |  | 
Motion: Head Rot: Octaves | TMOTIONCAM_NMOTION_HEAD_ROT_OCT | REAL | 0.0 |  |  | 
Motion: Head Rot: DeSync | TMOTIONCAM_NMOTION_HEAD_ROT_DESYNC | REAL | 0.0 |  |  | 
Motion: Head Rot: Offset | TMOTIONCAM_NMOTION_HEAD_ROT_OFFSET | VECTOR |  |  |  | 
Camera Rotation | TMOTIONCAM_NMOTION_CAM_ROT | SEPARATOR |  |  |  | 
Motion: Cam Rot: Intensity | TMOTIONCAM_NMOTION_CAM_ROT_INTENSITY | REAL | 0.0 |  |  | 
Motion: Cam Rot: Max | TMOTIONCAM_NMOTION_CAM_ROT_MAX | VECTOR |  |  |  | 
Motion: Cam Rot: Frequency | TMOTIONCAM_NMOTION_CAM_ROT_FREQ | VECTOR |  |  |  | 
Motion: Cam Rot: Octaves | TMOTIONCAM_NMOTION_CAM_ROT_OCT | REAL | 0.0 |  |  | 
Motion: Cam Rot: DeSync | TMOTIONCAM_NMOTION_CAM_ROT_DESYNC | REAL | 0.0 |  |  | 
Motion: Cam Rot: Offset | TMOTIONCAM_NMOTION_CAM_ROT_OFFSET | VECTOR |  |  |  | 
Camera Position | TMOTIONCAM_NMOTION_CAM_POS | SEPARATOR |  |  |  | 
Motion: Cam Pos: Intensity | TMOTIONCAM_NMOTION_CAM_POS_INTENSITY | REAL | 0.0 |  |  | 
Motion: Cam Pos: Max | TMOTIONCAM_NMOTION_CAM_POS_MAX | VECTOR |  |  |  | 
Motion: Cam Pos: Frequency | TMOTIONCAM_NMOTION_CAM_POS_FREQ | VECTOR |  |  |  | 
Motion: Cam Pos: Octaves | TMOTIONCAM_NMOTION_CAM_POS_OCT | REAL | 0.0 |  |  | 
Motion: Cam Pos: DeSync | TMOTIONCAM_NMOTION_CAM_POS_DESYNC | REAL | 0.0 |  |  | 
Motion: Cam Pos: Offset | TMOTIONCAM_NMOTION_CAM_POS_OFFSET | VECTOR |  |  |  | 
Focus: Enable Focus Control | TMOTIONCAM_FOCUS_ENABLED | BOOL |  |  |  | 
Focus: Focal Length | TMOTIONCAM_FOCUS_FOCALLENGTH | REAL | 1 | 10000 |  | 
Focus: Sensor Size | TMOTIONCAM_FOCUS_APERTURE | REAL | 1.0 | 2000.0 |  | 
Target | TMOTIONCAM_FOCUS_DISTANCE | SEPARATOR |  |  |  | 
Focus: Enable Auto Focus | TMOTIONCAM_FOCUS_AUTO_ENABLED | BOOL |  |  |  | 
Focus: Target Distance | TMOTIONCAM_FOCUS_DISTANCE_DIST | REAL | 0.0 |  |  | 
Focus: Offset | TMOTIONCAM_FOCUS_DISTANCE_OFFSET | REAL |  |  |  | 
Dolly Zoom | TMOTIONCAM_FOCUS_VERTIGO | SEPARATOR |  |  |  | 
Dolly Zoom: Intensity | TMOTIONCAM_FOCUS_VERTIGO_INTENSITY | REAL | 0.0 | 100.0 |  | 
Depth | TMOTIONCAM_FOCUS_DEPTH | SEPARATOR |  |  |  | 
Focus: Enable Depth Control | TMOTIONCAM_FOCUS_DEPTH_ENABLED | BOOL |  |  |  | 
Focus: Depth Mode | TMOTIONCAM_FOCUS_DEPTH_MODE | LONG |  |  |  | TMOTIONCAM_FOCUS_DEPTH_MODE_STANDARD; TMOTIONCAM_FOCUS_DEPTH_MODE_FORPOST
Focus: Focus Area | TMOTIONCAM_FOCUS_DEPTH_AREA | REAL | 0.0 |  |  | 
Focus: Blur Area | TMOTIONCAM_FOCUS_DEPTH_SOFT | REAL | 0.0 | 100.0 |  | 
