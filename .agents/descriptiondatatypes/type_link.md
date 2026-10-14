# Description Data Type: LINK

- **Cinema 4D Version:** `2027.0.0`

This file describes the LINK description data type and lists all flags encountered in the resources for Cinema 4D 2027.0.0.

## Flags

Flag | Arguments | Example
---- | --------- | -------
ACCEPT | Mrsgraph Mmaterial | <code>LINK REDSHIFT_AOV_GRAPH<br>{<br>&nbsp;&nbsp;ACCEPT { Mrsgraph; Mmaterial; }<br>}</code>
ANIM | OFF | <code>LINK INTERACTIONTAG_POLYINFO_SELECTIONTAG { ANIM OFF; }</code>
ANIM | MIX | <code>LINK TARGETEXPRESSIONTAG_LINK { ANIM MIX; ACCEPT { Obase; } }</code>
ANIM | ON | <code>LINK CS_SOURCE_CHARACTER<br>{<br>&nbsp;&nbsp;ANIM ON;<br>&nbsp;&nbsp;ACCEPT { 1054858;} // CHARACTERDEFINITION_TAG_ID<br>}</code>
CREATEPORT |  | <code>LINK OP_LBW_IN_OBJECT { INPORT; PORTONLY; CREATEPORT; }</code>
CUSTOMGUI | INLINE | <code>LINK GV_REDSHIFT_C4DSHADER_SHADER { CUSTOMGUI INLINE; }</code>
EDITPORT |  | <code>LINK OUT_PG_LINK { INPORT; EDITPORT; ACCEPT{ 1001381; }}</code>
EMPTY_TEXT | MGSCATTER_SURFACE_LINK_EMPTY_TEXT | <code>LINK MGSCATTER_SURFACE_LINK<br>{<br>&nbsp;&nbsp;REFUSE<br>&nbsp;&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;Osky;<br>&nbsp;&nbsp;&nbsp;&nbsp;Oforeground;<br>&nbsp;&nbsp;&nbsp;&nbsp;Obackground;<br>&nbsp;&nbsp;&nbsp;&nbsp;GVbase;<br>&nbsp;&nbsp;&nbsp;&nbsp;VPbase;<br>&nbsp;&nbsp;&nbsp;&nbsp;Mbase;<br>&nbsp;&nbsp;&nbsp;&nbsp;Xbase;<br>&nbsp;&nbsp;&nbsp;&nbsp;Ovolumebuilder;<br>&nbsp;&nbsp;&nbsp;&nbsp;Ovolume;<br>&nbsp;&nbsp;&nbsp;&nbsp;Ovolumeset;<br>&nbsp;&nbsp;&nbsp;&nbsp;1039866; // Ovolumeloader for some reason this is not accepted as name<br>&nbsp;&nbsp;&nbsp;&nbsp;Ovolumefilter;<br>&nbsp;&nbsp;&nbsp;&nbsp;Tpointselection;<br>&nbsp;&nbsp;&nbsp;&nbsp;Tedgeselection;<br>&nbsp;&nbsp;&nbsp;&nbsp;1001381;<br>&nbsp;&nbsp;&nbsp;&nbsp;Oparticle;<br>&nbsp;&nbsp;&nbsp;&nbsp;1064655; // Scatter object.<br>&nbsp;&nbsp;}<br>&nbsp;&nbsp;ACCEPT<br>&nbsp;&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;Tpolygonselection;<br>&nbsp;&nbsp;&nbsp;&nbsp;Obase;<br>&nbsp;&nbsp;}<br><br>&nbsp;&nbsp;HIDE_ICON;<br>&nbsp;&nbsp;HIDE_FIND_OBJECT;<br>&nbsp;&nbsp;EMPTY_TEXT MGSCATTER_SURFACE_LINK_EMPTY_TEXT;<br>&nbsp;&nbsp;FORCE_UPDATE;<br>}</code>
FIELD | HIDE | <code>LINK ID_MG_NODEDISTRIBUTION_LINK_INTERNAL_DEPRECATED<br>{<br>&nbsp;&nbsp;ACCEPT { 190000011; } // Distribution capsule<br>&nbsp;&nbsp;HIDE_ICON;<br>&nbsp;&nbsp;NO_PICKER;<br>&nbsp;&nbsp;CUSTOMGUI INLINE;<br>&nbsp;&nbsp;FIELD HIDE;<br>}</code>
FIT_H |  | <code>LINK CAMERAOBJECT_TARGETOBJECT { FIT_H; ACCEPT { Obase; } }</code>
FORBID_INLINE_FOLDING |  | <code>LINK ID_MT_CLIP_SOURCE { FIT_H; ANIM OFF; FORBID_INLINE_FOLDING; ACCEPT { Obase; } }</code>
FORCE_UPDATE |  | <code>LINK MGSCATTER_SURFACE_LINK<br>{<br>&nbsp;&nbsp;REFUSE<br>&nbsp;&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;Osky;<br>&nbsp;&nbsp;&nbsp;&nbsp;Oforeground;<br>&nbsp;&nbsp;&nbsp;&nbsp;Obackground;<br>&nbsp;&nbsp;&nbsp;&nbsp;GVbase;<br>&nbsp;&nbsp;&nbsp;&nbsp;VPbase;<br>&nbsp;&nbsp;&nbsp;&nbsp;Mbase;<br>&nbsp;&nbsp;&nbsp;&nbsp;Xbase;<br>&nbsp;&nbsp;&nbsp;&nbsp;Ovolumebuilder;<br>&nbsp;&nbsp;&nbsp;&nbsp;Ovolume;<br>&nbsp;&nbsp;&nbsp;&nbsp;Ovolumeset;<br>&nbsp;&nbsp;&nbsp;&nbsp;1039866; // Ovolumeloader for some reason this is not accepted as name<br>&nbsp;&nbsp;&nbsp;&nbsp;Ovolumefilter;<br>&nbsp;&nbsp;&nbsp;&nbsp;Tpointselection;<br>&nbsp;&nbsp;&nbsp;&nbsp;Tedgeselection;<br>&nbsp;&nbsp;&nbsp;&nbsp;1001381;<br>&nbsp;&nbsp;&nbsp;&nbsp;Oparticle;<br>&nbsp;&nbsp;&nbsp;&nbsp;1064655; // Scatter object.<br>&nbsp;&nbsp;}<br>&nbsp;&nbsp;ACCEPT<br>&nbsp;&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;Tpolygonselection;<br>&nbsp;&nbsp;&nbsp;&nbsp;Obase;<br>&nbsp;&nbsp;}<br><br>&nbsp;&nbsp;HIDE_ICON;<br>&nbsp;&nbsp;HIDE_FIND_OBJECT;<br>&nbsp;&nbsp;EMPTY_TEXT MGSCATTER_SURFACE_LINK_EMPTY_TEXT;<br>&nbsp;&nbsp;FORCE_UPDATE;<br>}</code>
HIDDEN |  | <code>LINK REDSHIFT_LIGHT_PARENT<br>{<br>&nbsp;&nbsp;HIDDEN;<br>}</code>
HIDE_FIND_OBJECT |  | <code>LINK MGSCATTER_SURFACE_LINK<br>{<br>&nbsp;&nbsp;REFUSE<br>&nbsp;&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;Osky;<br>&nbsp;&nbsp;&nbsp;&nbsp;Oforeground;<br>&nbsp;&nbsp;&nbsp;&nbsp;Obackground;<br>&nbsp;&nbsp;&nbsp;&nbsp;GVbase;<br>&nbsp;&nbsp;&nbsp;&nbsp;VPbase;<br>&nbsp;&nbsp;&nbsp;&nbsp;Mbase;<br>&nbsp;&nbsp;&nbsp;&nbsp;Xbase;<br>&nbsp;&nbsp;&nbsp;&nbsp;Ovolumebuilder;<br>&nbsp;&nbsp;&nbsp;&nbsp;Ovolume;<br>&nbsp;&nbsp;&nbsp;&nbsp;Ovolumeset;<br>&nbsp;&nbsp;&nbsp;&nbsp;1039866; // Ovolumeloader for some reason this is not accepted as name<br>&nbsp;&nbsp;&nbsp;&nbsp;Ovolumefilter;<br>&nbsp;&nbsp;&nbsp;&nbsp;Tpointselection;<br>&nbsp;&nbsp;&nbsp;&nbsp;Tedgeselection;<br>&nbsp;&nbsp;&nbsp;&nbsp;1001381;<br>&nbsp;&nbsp;&nbsp;&nbsp;Oparticle;<br>&nbsp;&nbsp;&nbsp;&nbsp;1064655; // Scatter object.<br>&nbsp;&nbsp;}<br>&nbsp;&nbsp;ACCEPT<br>&nbsp;&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;Tpolygonselection;<br>&nbsp;&nbsp;&nbsp;&nbsp;Obase;<br>&nbsp;&nbsp;}<br><br>&nbsp;&nbsp;HIDE_ICON;<br>&nbsp;&nbsp;HIDE_FIND_OBJECT;<br>&nbsp;&nbsp;EMPTY_TEXT MGSCATTER_SURFACE_LINK_EMPTY_TEXT;<br>&nbsp;&nbsp;FORCE_UPDATE;<br>}</code>
HIDE_ICON |  | <code>LINK CID_MORPHKEY_LINK { ACCEPT { Obase; } HIDE_ICON; }</code>
INPORT |  | <code>LINK IN_LINK {INPORT; MULTIPLE;}</code>
LAYERMODE |  | <code>LINK LBWIMPORT_MATERIAL_LAYER<br>{<br>&nbsp;&nbsp;LAYERMODE;<br>&nbsp;&nbsp;ACCEPT<br>&nbsp;&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;100004801;<br>&nbsp;&nbsp;}<br>}</code>
MATEDNOTEXT |  | <code>LINK ID_LAYER_LINK<br>{<br>&nbsp;&nbsp;UNIMPORTANTFORDEFAULTS;<br>&nbsp;&nbsp;LAYERMODE;<br>&nbsp;&nbsp;ANIM OFF;<br>&nbsp;&nbsp;MATEDNOTEXT;<br>&nbsp;&nbsp;ACCEPT<br>&nbsp;&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;100004801;<br>&nbsp;&nbsp;}<br>}</code>
MULTIPLE |  | <code>LINK IN_LINK {INPORT; MULTIPLE;}</code>
NO_PICKER |  | <code>LINK MOGRAPH_NODEDISTRIBUTION_LINK_INTERNAL<br>{<br>&nbsp;&nbsp;ACCEPT { 190000011; } // Distribution capsule<br>&nbsp;&nbsp;HIDE_ICON;<br>&nbsp;&nbsp;NO_PICKER;<br>&nbsp;&nbsp;CUSTOMGUI INLINE;<br>}</code>
OUTPORT |  | <code>LINK OUT_LINK {OUTPORT; MULTIPLE;}</code>
PARENTCOLLAPSE | SKY_ASTRO_MOON_SHOW | <code>LINK SKY_OBJECT_MOON_OBJECT { PARENTCOLLAPSE SKY_ASTRO_MOON_SHOW; }</code>
PARENTID | FIELDDRIVER_MATRIXMODE | <code>LINK FIELDDRIVER_MATRIXMODE_OVERWRITE_OB { PARENTID FIELDDRIVER_MATRIXMODE; ACCEPT { Obase; }}</code>
PORTONLY |  | <code>LINK OP_LBW_IN_OBJECT { INPORT; PORTONLY; CREATEPORT; }</code>
REFUSE | Obase | <code>LINK TENSIONTAG_FOLD<br>{<br>&nbsp;&nbsp;ACCEPT { Tbase; }<br>&nbsp;&nbsp;REFUSE { Obase; }<br>}</code>
SCALE_H |  | <code>LINK RIGIDBODY_PBD_INITIAL_VELOCITY_TARGET { SCALE_H; ACCEPT { Obase; } }</code>
STATICPORT |  | <code>LINK GV_LINK_OUTPUT { OUTPORT; STATICPORT; CREATEPORT; }</code>
UNIMPORTANTFORDEFAULTS |  | <code>LINK ID_LAYER_LINK<br>{<br>&nbsp;&nbsp;UNIMPORTANTFORDEFAULTS;<br>&nbsp;&nbsp;LAYERMODE;<br>&nbsp;&nbsp;ANIM OFF;<br>&nbsp;&nbsp;MATEDNOTEXT;<br>&nbsp;&nbsp;ACCEPT<br>&nbsp;&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;100004801;<br>&nbsp;&nbsp;}<br>}</code>
