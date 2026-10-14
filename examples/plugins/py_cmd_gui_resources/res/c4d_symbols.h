#ifndef C4D_SYMBOLS_H__
#define C4D_SYMBOLS_H__

// This is the primary 'symbol' file of a plugin. A 'symbol' is just a numeric identifier for 
// something. Because Cinema 4D has its roots in C++, the symbols are defined as C++ header files.
//
// In this file dialogs, and general identifiers are defined. Description resource symbols (i.e.,
// things like objects, tags, materials, etc.) are defined in dedicated files for each description.

// The enumeration of all globals symbols for this plugin. Anything we want to reference via a 
// symbol must be defined here (except for description symbols).
enum
{
	ID_PLUGIN = 1065655,         // One thing we can store here is the plugin ID there is no necessity
	                             // for doing this, but it is an option.

	// Cinema 4D uses conventionally a handful of naming patterns in the context of resource symbols.
	// You do not have to follow them.
	//
	//   1. A symbol prefixed with `IDD_` is a dialog ID.
	//   2. A symbol prefixed with `IDC_` is a control ID.
	//   3. A symbol prefixed with `IDS_` is a string ID.
	//
	// This pattern is not without fault, I personally prefer naming things more verbosely, e.g.,
	// ID_DLG_MAIN (a dialog ID), ID_BTN_OK (a button ID), and ID_STR_PLUGIN_NAME (a string ID). But
	// this example follows strictly the Cinema 4D convention.

	// Custom string symbols for the name and help string of the plugin. These strings are defined in
	// the language respective generic string files, e.g., strings_en-US/c4d_strings.str.
	IDS_PLUGIN_NAME = 1000,        
	IDS_PLUGIN_HELP,       // Implicit value definition, i.e., 1001

	// The gadget IDs and strings IDs for dialogs/idd_values.res
	IDD_VALUES = 1100,
	IDC_VALUE_A,        // 1101
	IDC_VALUE_B,        // 1102		
	IDS_VALUE_A,        // ...
	IDS_VALUE_B,

	// The gadget IDs and strings IDs for dialogs/idd_buttons.res
	IDD_BUTTONS = 1200,
	IDC_ADD,
	IDC_SUBTRACT,
	IDS_ADD,
	IDS_SUBTRACT,

	// Dummy - end of the enumeration, this element is necessary to mark the end of the enumeration.
	__DUMMY__
};

#endif // C4D_SYMBOLS_H__
