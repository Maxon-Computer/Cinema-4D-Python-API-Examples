CONTAINER Opyassetcontainer
{
    NAME Opyassetcontainer;
    INCLUDE Obase;

    GROUP ID_OBJECTPROPERTIES
    {
        // The horizontal layout group of the selection, add and delete buttons.
        GROUP
        {
            COLUMNS 3;

            LONG PY_ASSETCONTAINER_SELECTION
            {
                CYCLE
                {
                    PY_ASSETCONTAINER_SELECTION_NONE;
                }
            }

            BUTTON PY_ASSETCONTAINER_ADD {}
            BUTTON PY_ASSETCONTAINER_DELETE {}
        }

        // The source field for an asset to add, and the instructions parameter where we display
        // the instructions fore how to use the example.
        LINK PY_ASSETCONTAINER_SOURCE { ACCEPT { Obase; } }
        STATICTEXT PY_ASSETCONTAINER_INSTRUCTIONS {}
    }
}
