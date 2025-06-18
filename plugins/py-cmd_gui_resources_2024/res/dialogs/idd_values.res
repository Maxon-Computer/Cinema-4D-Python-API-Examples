// The GUI markup (res) for a dialog. 
// 
// Here we define the groups and controls of a dialog and Cinema 4D's res markup language. While 
// res markup is unavoidable for description resources (objects, tags, materials, etc.), it is not
// necessary for dialogs. Some parts of our documentation sell dialog markup as the more powerful
// alternative to defining dialogs in code. This is simply not true anymore. Dialog resources are
// an option, especially when one has to define many dialogs composed out of reoccurring parts.
//
// See also: https://developers.maxon.net/docs/cpp/2025_2_0a/page_dialog_resource.html

// Define a dialog resource, this does not necessarily mean that this will be all that is being
// loaded into the the final dialog, as one can load multiple dialog resources into a single
// dialog class.
DIALOG IDD_VALUES
{
	// Define the scaling behaviour of this component, we want it to consume all available
	// horizontal and vertical space.
	SCALE_H;
	SCALE_V;

	// A unnamed group with an anonymous ID
	GROUP
	{
		// Which has two columns and places a five pixel wide horizontal and vertical padding between
		// elements placed in this group.
		COLUMNS 2;
		SPACE 5, 5;

		// Now apply the same layout rules as when we do this in code, since we have a two column
		// layout and we add here label, edit, label, edit, we will end up with:
		//
		//  Label: Edit
		//  Label: Edit
		//

		// The label of the first edit control, we use here one of our string IDs, so that Cinema 4D
		// knows which string to display for the label (picking the active language). The label could
		// also have a gadget ID (`STATICTEXT IDC_LBL_VALUE_A { NAME IDS_VALUE_A; }`), but since we
		// do not want to address this gadget in code, we an use an anonymous ID here.
		STATICTEXT { NAME IDS_VALUE_A; }
		// The first edit control, we use the `EDITNUMBERARROWS` gadget type. Here we used a gadget
		// ID (`IDC_VALUE_A` defined in c4d_symbols.h) so that we can address this control in code. 
		// We also set some flags such as the default size of the control and that it should scale 
		// horizontally.
		EDITNUMBERARROWS IDC_VALUE_A { SIZE 100,0; SCALE_H; }

		// The second label edit control pair.
		STATICTEXT { NAME IDS_VALUE_B; }
		EDITNUMBERARROWS IDC_VALUE_B { SIZE 100,0; SCALE_H; }
	}
}