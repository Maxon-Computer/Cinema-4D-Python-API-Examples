// The GUI markup (res) for a dialog. 
//
// This follows the same principles as the `idd_values.res` file, read it for more information.
// We will load this dialog resource into the same dialog instance as the `idd_values.res`
// resource, so that we effectively compose a dialog out of multiple resources.
DIALOG IDD_BUTTONS
{
	SCALE_H; SCALE_V;

	GROUP
	{
		COLUMNS 2;
		SPACE 5, 5;

		BUTTON IDC_ADD { NAME IDS_ADD; SIZE 100,0; SCALE_H; }
		BUTTON IDC_SUBTRACT { NAME IDS_SUBTRACT; SIZE 100,0; SCALE_H; }
	}
}