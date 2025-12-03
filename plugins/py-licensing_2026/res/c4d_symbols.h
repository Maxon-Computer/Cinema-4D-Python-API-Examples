// Contains the symbol definitions for non description resources used in the py-licensing example.
enum
{
  // Resource ID for the License Manager dialog - we use the plugin ID of the License Manager 
  // plugin. Using the plugin ID is not a necessity, we could also define it as 1000 or so, but
  // good practice IMHO. We could also register a dedicated plugin ID for the dialog.
  DLG_LICENSE_MANAGER = 1066811,

  // Gadget and other IDs

  // Groups and Tabs
  ID_GRP_MAIN = 1000,
  ID_TAB_GROUPS,
  ID_GRP_DATA,
  ID_GRP_LICENSE,
  
  // Data tab gadgets
  ID_EDT_DATA_SALT,
  ID_EDT_DATA_FILE_KEY,
  ID_EDT_DATA_USER_ID,
  ID_EDT_DATA_USER_NAME,
  ID_EDT_DATA_USER_SURNAME,
  ID_EDT_DATA_SYSTEM_ID,
  ID_EDT_DATA_PRODUCT_VERSION,
  ID_EDT_DATA_PRODUCT_ID,
  ID_EDT_DATA_ACCOUNT_LICENSES,

  // License tab gadgets
  ID_CMB_LICENSE_TYPE,
    ID_CMB_LICENSE_TYPE_COMMERCIAL,
    ID_CMB_LICENSE_TYPE_DEMO,
    ID_CMB_LICENSE_TYPE_EDUCATIONAL,
    ID_CMB_LICENSE_TYPE_NFR,
  ID_CMB_LICENSE_STORAGE_MODE,
    ID_CMB_LICENSE_STORAGE_MODE_FILE,
    ID_CMB_LICENSE_STORAGE_MODE_SYSTEM,
  ID_CMB_LICENSE_ACTIVATION_MODE,
    ID_CMB_LICENSE_ACTIVATION_MODE_RESTART,
    ID_CMB_LICENSE_ACTIVATION_MODE_NO_RESTART,
  ID_CHK_LICENSE_USE_SYSTEM_ID,
  ID_CHK_LICENSE_USE_PRODUCT_ID,
  ID_EDT_LICENSE_KEY,
  ID_BTN_LICENSE_GENERATE,
  ID_ICN_LICENSE_KEY_VALID,
  ID_BTN_LICENSE_ACTIVATE,
  ID_BTN_LICENSE_DEACTIVATE,

  // The help area to the right
  ID_EDT_HELP,

  // Custom strings
  IDS_HLP_DATA = 2000,
  IDS_HLP_LICENSE,
  IDS_DLG_RESTART_REQUIRED,

  // End of symbol definition
  _DUMMY_ELEMENT_
};
