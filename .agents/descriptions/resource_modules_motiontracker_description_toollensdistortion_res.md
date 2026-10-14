# Description: Lens Distortion

- **Cinema 4D Version:** `2027.0.0`
- **ID:** `resource/modules/motiontracker/description/toollensdistortion.res`
- **Symbol:** `Toollensdistortion`
- **Category:** Other

Use parameter symbols to access parameters and cycle option symbols for cycle values, never their numeric IDs. Treat Min and Max as constraints and Default as the declared initial value; blank cells mean the resource does not declare that metadata, not that the value is zero. Base Description Parameters lists inherited fields from each base; All Parameters lists the effective parameter set for this description.

## Base Description Parameters

No base descriptions.

## All Parameters

Name | Symbol | Data Type | Min | Max | Default | Cycle Symbols
---- | ------ | --------- | --- | --- | ------- | -------------
Image | CM_IMAGE_FILENAME | FILENAME |  |  |  | 
Film Aspect | CM_RDATA_FILMASPECT | REAL | 0.001 | 1000.0 |  | 
No label | CM_RDATA_FILMPRESET | LONG |  |  |  | CM_RDATA_FILMPRESET_CUSTOM; CM_RDATA_FILMPRESET_SQUARE; CM_RDATA_FILMPRESET_STANDARD; CM_RDATA_FILMPRESET_HDTV; CM_RDATA_FILMPRESET_35MMSTILL; CM_RDATA_FILMPRESET_WIDESCREEN; CM_RDATA_FILMPRESET_35MM; CM_RDATA_FILMPRESET_PANAVISION
No label | CM_RDATA_RENDER_FILM_ASPECT | STATICTEXT |  |  |  | 
Image Scale | CM_IMAGE_VIEW_SCALE | REAL | 1.0 | 10000.0 |  | 
Image Offset X | CM_IMAGE_VIEW_OFFSET_X | REAL | -500.0 | 500.0 |  | 
Image Offset Y | CM_IMAGE_VIEW_OFFSET_Y | REAL | -500.0 | 500.0 |  | 
Brightness | CM_IMAGE_BRIGHTNESS | REAL | 0.0 | 200.0 |  | 
Full Image | CM_IMAGE_VIEW_FULL | BUTTON |  |  |  | 
Match Width | CM_IMAGE_MATCH_VIEW_WIDTH | BUTTON |  |  |  | 
Match Height | CM_IMAGE_MATCH_VIEW_HEIGHT | BUTTON |  |  |  | 
Solve Mode | PH_LENS_DISTORT_SOLVE_MODE | LONG |  |  |  | PH_LENS_DISTORT_SOLVE_MODE_MANUAL; PH_LENS_DISTORT_SOLVE_MODE_AUTOMATIC
Add Line | ADD_NEW_LINE | BUTTON |  |  |  | 
Delete Selected Line | DELETE_SELECTED_LINE_MANUAL | BUTTON |  |  |  | 
Add N-Point Line | ADD_NEW_TRIPLINE | BUTTON |  |  |  | 
Auto Solve | PH_LENS_DISTORT_AUTO_SOLVE | BUTTON |  |  |  | 
Delete Selected Line | DELETE_SELECTED_LINE_AUTOMATIC | BUTTON |  |  |  | 
Lens Distortion Model | PH_LENS_DISTORT_MODEL | LONG |  |  |  | PH_LENS_MODEL_NONE; PH_LENS_MODEL_3DE_RADIAL_STANDARD_DEG4; PH_LENS_MODEL_3DE_CLASSIC; PH_LENS_MODEL_3DE_ANAMORPHIC_DEG4_ROT_SQZ; PH_LENS_MODEL_3DE_ANAMORPHIC_DEG6; PH_LENS_MODEL_3DE_RADIAL_DEG8
Experimental | PH_LENS_M1_PARAM | REAL | -100.0 | 200.0 |  | 
Quadratic | PH_LENS_M2_QUADRATIC_DISTORTION | REAL | -500.0 | 500.0 |  | 
Cubic | PH_LENS_M2_CUBIC_DISTORTION | REAL | -500.0 | 500.0 |  | 
X Offset | PH_LENS_A3_OFFX | REAL | -100.0 | 100.0 |  | 
Y Offset | PH_LENS_A3_OFFY | REAL | -100.0 | 100.0 |  | 
Quadratic | PH_LENS_M3_C2 | REAL | -100.0 | 100.0 |  | 
U Degree 2 | PH_LENS_M3_U1 | REAL | -100.0 | 100.0 |  | 
V Degree 2 | PH_LENS_M3_V1 | REAL | -100.0 | 100.0 |  | 
Quartic | PH_LENS_M3_C4 | REAL | -100.0 | 100.0 |  | 
U Degree 4 | PH_LENS_M3_U3 | REAL | -100.0 | 100.0 |  | 
V Degree 4 | PH_LENS_M3_V3 | REAL | -100.0 | 100.0 |  | 
Phi Cylindric Direction | PH_LENS_M3_PHI_CYL_DIR | REAL | -180.0 | 180.0 |  | 
B Cylindric Bending | PH_LENS_M3_B_CYL_BEND | REAL | -20.0 | 20.0 |  | 
X Offset | PH_LENS_A4_OFFX | REAL | -100.0 | 100.0 |  | 
Y Offset | PH_LENS_A4_OFFY | REAL | -100.0 | 100.0 |  | 
Quadratic | PH_LENS_M4_C2 | REAL | -100.0 | 100.0 |  | 
Quartic | PH_LENS_M4_C4 | REAL | -100.0 | 100.0 |  | 
Curvature X | PH_LENS_M4_XCRV | REAL | -100.0 | 100.0 |  | 
Curvature Y | PH_LENS_M4_YCRV | REAL | -100.0 | 100.0 |  | 
Anamorphic Squeeze | PH_LENS_M4_ASQZ | REAL | 12 | 800.0 |  | 
X Offset | PH_LENS_A5_OFFX | REAL | -100.0 | 100.0 |  | 
Y Offset | PH_LENS_A5_OFFY | REAL | -100.0 | 100.0 |  | 
Cx02 | PH_LENS_M5_Cx02 | REAL | -100.0 | 100.0 |  | 
Cy02 | PH_LENS_M5_Cy02 | REAL | -100.0 | 100.0 |  | 
Cx22 | PH_LENS_M5_Cx22 | REAL | -100.0 | 100.0 |  | 
Cy22 | PH_LENS_M5_Cy22 | REAL | -100.0 | 100.0 |  | 
Cx04 | PH_LENS_M5_Cx04 | REAL | -100.0 | 100.0 |  | 
Cy04 | PH_LENS_M5_Cy04 | REAL | -100.0 | 100.0 |  | 
Cx24 | PH_LENS_M5_Cx24 | REAL | -100.0 | 100.0 |  | 
Cy24 | PH_LENS_M5_Cy24 | REAL | -100.0 | 100.0 |  | 
Cx44 | PH_LENS_M5_Cx44 | REAL | -100.0 | 100.0 |  | 
Cy44 | PH_LENS_M5_Cy44 | REAL | -100.0 | 100.0 |  | 
Lens Rotation | PH_LENS_M5_ROT | REAL | -4.0 | 4.0 |  | 
Squeeze-X | PH_LENS_M5_XSQZ | REAL | 80.0 | 120.0 |  | 
Squeeze-Y | PH_LENS_M5_YSQZ | REAL | 80.0 | 120.0 |  | 
X Offset | PH_LENS_A6_OFFX | REAL | -100.0 | 100.0 |  | 
Y Offset | PH_LENS_A6_OFFY | REAL | -100.0 | 100.0 |  | 
Cx02 | PH_LENS_M6_Cx02 | REAL | -100.0 | 100.0 |  | 
Cy02 | PH_LENS_M6_Cy02 | REAL | -100.0 | 100.0 |  | 
Cx22 | PH_LENS_M6_Cx22 | REAL | -100.0 | 100.0 |  | 
Cy22 | PH_LENS_M6_Cy22 | REAL | -100.0 | 100.0 |  | 
Cx04 | PH_LENS_M6_Cx04 | REAL | -100.0 | 100.0 |  | 
Cy04 | PH_LENS_M6_Cy04 | REAL | -100.0 | 100.0 |  | 
Cx24 | PH_LENS_M6_Cx24 | REAL | -100.0 | 100.0 |  | 
Cy24 | PH_LENS_M6_Cy24 | REAL | -100.0 | 100.0 |  | 
Cx44 | PH_LENS_M6_Cx44 | REAL | -100.0 | 100.0 |  | 
Cy44 | PH_LENS_M6_Cy44 | REAL | -100.0 | 100.0 |  | 
Cx06 | PH_LENS_M6_Cx06 | REAL | -100.0 | 100.0 |  | 
Cy06 | PH_LENS_M6_Cy06 | REAL | -100.0 | 100.0 |  | 
Cx26 | PH_LENS_M6_Cx26 | REAL | -100.0 | 100.0 |  | 
Cy26 | PH_LENS_M6_Cy26 | REAL | -100.0 | 100.0 |  | 
Cx46 | PH_LENS_M6_Cx46 | REAL | -100.0 | 100.0 |  | 
Cy46 | PH_LENS_M6_Cy46 | REAL | -100.0 | 100.0 |  | 
Cx66 | PH_LENS_M6_Cx66 | REAL | -100.0 | 100.0 |  | 
Cy66 | PH_LENS_M6_Cy66 | REAL | -100.0 | 100.0 |  | 
X Offset | PH_LENS_A7_OFFX | REAL | -100.0 | 100.0 |  | 
Y Offset | PH_LENS_A7_OFFY | REAL | -100.0 | 100.0 |  | 
Quadratic | PH_LENS_M7_C2 | REAL | -100.0 | 100.0 |  | 
Quartic | PH_LENS_M7_C4 | REAL | -100.0 | 100.0 |  | 
Degree 6 | PH_LENS_M7_C6 | REAL | -100.0 | 100.0 |  | 
Degree 8 | PH_LENS_M7_C8 | REAL | -100.0 | 100.0 |  | 
Load Lens Profile | LD_LENS_LOAD_PROFILE | BUTTON |  |  |  | 
Save Lens Profile | LD_LENS_SAVE_PROFILE | BUTTON |  |  |  | 
